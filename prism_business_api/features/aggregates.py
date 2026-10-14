"""Bounded business aggregations over the existing news, event and deal data.

No listing or page totals are reused. Semi-joins retain one counted deal even
when several source articles match. Overview uses one common window and the
business article scope; standalone summaries retain unlinked business records
unless an article filter explicitly requires a match.
"""
from __future__ import annotations

import math
import time
from dataclasses import replace
from datetime import date, timedelta

from prism_news_api import ch, config, envelope, filters, public
from prism_news_api.auth import Principal
from prism_news_api.envelope import ApiError
from prism_news_api.features import _common as gc

from .. import tables
from ..filters import (BusinessFilters, FUNDING_ONLY, country_sql, domain_lane_sql, funding_company_sql,
                       investor_sql, name_lane_sql, round_type_sql, sector_sql, word_regex)
from ..scope import apply_business_scope
from . import _common as c

MAX_WINDOW_DAYS = 366
EVENT_KEY = "(target_id, domain, event_type, role, news_publish_datetime)"
VALID_AMOUNT = tables.VALID_AMOUNT
# Sums and medians run over distinct (company, amount) pairs: one round is often
# extracted several times under different round_type labels.
_DEDUP = (f"arrayMap(x -> x.2, groupUniqArrayIf((lowerUTF8(coalesce(nullIf(domain, ''), company_name, '')), "
          f"coalesce(amount_usd, 0.)), {VALID_AMOUNT}))")
AMOUNT_SQL = (f"count(), countIf({VALID_AMOUNT}), "
              f"arraySum({_DEDUP}), "
              f"arrayReduce('quantileExactInclusive(0.5)', {_DEDUP}), "
              f"maxIf(coalesce(amount_usd, 0.), {VALID_AMOUNT}), "
              f"countIf({tables.REPORTED_AMOUNT} AND NOT {VALID_AMOUNT})")
FUNDING_COUNTING = (
    "Each matched deal record counts once, regardless of how many articles report it. "
    "Counts are measured over the entire filtered window, independent of result limits. "
    "USD amounts use fixed conversion rates, not current or transaction-date exchange rates. "
    "Only usable amounts enter sums, medians and maxima: finite, positive, converted to USD "
    f"and at most {tables.MAX_PLAUSIBLE_USD:,} USD. Larger or unconverted figures are counted in "
    "deals_amount_excluded. Sums and medians count one company and amount once, because the same "
    "round is often reported under several round labels. Missing, zero, negative and non-finite "
    "amounts count as unknown; amount statistics are null when no matched deal has a usable amount. "
    "Deal records include equity rounds, debt facilities, placements and announced commitments. "
    "Amounts are reported figures, not independently verified financial amounts."
)
EVENT_COUNTING = (
    "One event is a distinct article, company domain, event type, role and publication time. "
    "Repeated sentences with the same event identity count once. One article can contain "
    "multiple events; company counts exclude missing domains."
)


def funding_totals(row) -> dict:
    deals, known = int(row[0] or 0), int(row[1] or 0)
    def amount(v):
        if not known or v is None:
            return None
        n = float(v)
        return round(n, 2) if math.isfinite(n) else None
    excluded = int(row[5] or 0) if len(row) > 5 else 0
    return {"deals": deals, "deals_with_amount": known, "deals_without_amount": deals - known,
            "deals_amount_excluded": excluded,
            "sum_amount_usd": amount(row[2]), "median_amount_usd": amount(row[3]),
            "largest_amount_usd": amount(row[4]), "currency": "USD", "note": FUNDING_COUNTING}


def _dates(r, column="news_publish_datetime") -> str:
    return (f"{column} >= {ch.sql_str(r.since)} AND "
            f"{column} < {ch.sql_str(r.until_exclusive)}")


def _funding_where(f, r) -> str:
    parts = [_dates(r)]
    if f.round_type:
        parts.append(round_type_sql(f.round_types()))
    if f.sector:
        parts.append(sector_sql(f.sectors()))
    if f.min_amount_usd is not None:
        parts.append(f"({VALID_AMOUNT}) AND amount_usd >= {float(f.min_amount_usd)!r}")
    if f.country:
        parts.append(country_sql(f.country))
    if f.investor:
        parts.append(investor_sql(f.investor))
    if f.company:
        parts.append(funding_company_sql(f.company))
    if r.q and not f.match:
        rx = ch.sql_str(word_regex(r.q))
        parts.append("(" + " OR ".join(f"match(lowerUTF8(coalesce({col}, '')), {rx})"
                                     for col in ("source_sentence", "company_name", "use_of_funds")) + ")")
    return " AND ".join(parts)


def _event_where(f, r) -> str:
    parts = [_dates(r)]
    types = f.event_types()
    if types:
        parts.append(f"event_type IN {ch.sql_in(types)}")
    kind, company = f.company_parts()
    if kind == "domain":
        parts.append(f"domain = {ch.sql_str(company)}")
    if r.q and not f.match:
        parts.append(f"match(lowerUTF8(headline), {ch.sql_str(word_regex(r.q))})")
    return " AND ".join(parts)


def _article_where(f, r, *, q=True, company=True, country=True) -> str:
    # BusinessFilters' normal hook rejects funding-only filters. Here each lane
    # is applied explicitly, and all membership subqueries use this exact window.
    ar = replace(r, extra_sql=[], cursor=None, country=r.country if country else None,
                 q=r.q if q else None)
    parts = [filters.where_sql(ar, with_cursor=False)]
    kind, value = f.company_parts()
    if company and kind == "name":
        parts.append(name_lane_sql(value))
    if f.event_type or (company and kind == "domain"):
        lane = f.model_copy(update={"q": None, "company": f.company if company else None})
        er = replace(r, q=None)
        events_lane = (f"target_id GLOBAL IN (SELECT target_id FROM {tables.EVENTS_TABLE} "
                       f"WHERE {_event_where(lane, er)})")
        parts.append(f"({domain_lane_sql(value)} OR {events_lane})"
                     if company and kind == "domain" and not f.event_type else events_lane)
    return " AND ".join(parts)


def _prepare(p: Principal, f: BusinessFilters, which: str):
    if f.cursor or f.resolve or f.sort != "newest":
        raise ApiError("bad_request", "aggregations do not accept cursor, resolve or listing sort options")
    # Validate business tokens even if there are no rows to query.
    f.business_subject()
    if f.investor:
        investor_sql(f.investor)
    if which == "events" and any(getattr(f, k) is not None for k in FUNDING_ONLY):
        raise ApiError("bad_request", "funding filters apply to /v1/business/funding/summary or /v1/business/overview")
    ch.require_coverage()
    through = {"news": ch.data_through()}
    if which in ("events", "overview") or f.event_type:
        tables.require_table("events")
        through["events"] = tables.events_data_through()
    if which in ("funding", "overview"):
        tables.require_table("funding")
        through["funding"] = tables.funding_data_through()
    dt = min(through.values())
    scoped, scope = apply_business_scope(f) if which == "overview" else (f, None)
    r = filters.resolve(scoped.common(cursor=None), p.plan_cfg, dt)
    max_days = min(MAX_WINDOW_DAYS, int(p.plan_cfg.get("max_window_days") or MAX_WINDOW_DAYS))
    if r.days > max_days:
        r.since = (date.fromisoformat(r.until) - timedelta(days=max_days - 1)).isoformat()
        r.notes.append(f"aggregation window is limited to {max_days} days; since clamped to {r.since}")
    window = {"since": r.since, "until": r.until, "days": r.days, "data_through": dt,
              "datasets": through, "freshness": tables.freshness_note(dt), "max_days": max_days}
    # Source-article filters constrain events/deals through membership, never
    # joins that multiply deals by source-article count.
    article_lens = bool(scope or f.match or f.sentiment or f.classes or f.class_prefix or
                        f.themes or f.priority_min is not None or f.priority_max is not None)
    ew, fw = _event_where(f, r), _funding_where(f, r)
    if which in ("events", "overview") and (article_lens or f.country or f.company_parts()[0] == "name"):
        aw = _article_where(f, r, q=bool(f.match), company=f.company_parts()[0] == "name")
        ew += f" AND target_id GLOBAL IN (SELECT target_id FROM {ch.TABLE} WHERE {aw})"
    if which in ("funding", "overview") and (article_lens or f.event_type):
        aw = _article_where(f, r, q=bool(f.match), company=False, country=False)
        fw += (f" AND arrayExists(source_id -> source_id GLOBAL IN "
               f"(SELECT target_id FROM {ch.TABLE} WHERE {aw}), source_target_ids)")
    aw = _article_where(f, r)
    if which == "overview" and any(getattr(f, k) is not None for k in FUNDING_ONLY):
        deals = f"SELECT arrayJoin(source_target_ids) FROM {tables.FUNDING_TABLE} WHERE {_funding_where(f, r)}"
        aw += f" AND target_id GLOBAL IN ({deals})"
        ew += f" AND target_id GLOBAL IN ({deals})"
    subject = {"filters": {**r.subject(), **f.business_subject()}}
    if scope:
        subject["scope"] = scope
    notes = list(r.notes)
    if article_lens or f.event_type or (which != "funding" and (f.country or f.company_parts()[0] == "name")):
        notes.append("Article filters require a matching source article in the same window; records without a matching article are excluded. Each deal still counts once.")
    notes.append("Dates refer to source publication dates, not necessarily the date an event or deal occurred.")
    return r, window, subject, notes, aw, ew, fw


def _event_totals_sql(where):
    return (f"SELECT uniqExact({EVENT_KEY}), uniqExact(target_id), "
            f"uniqExactIf(domain, notEmpty(domain)) FROM {tables.EVENTS_TABLE} WHERE {where}")


def _event_totals(row):
    return {"events": int(row[0] or 0), "articles": int(row[1] or 0),
            "companies": int(row[2] or 0), "counting": EVENT_COUNTING}


def overview(p: Principal, f: BusinessFilters) -> dict:
    t0 = time.time()
    r, window, subject, notes, aw, ew, fw = _prepare(p, f, "overview")
    ns = (f"SELECT uniqExact(target_id), uniqExactIf(target_id, {ch.TOP_PRIORITY} >= {config.CRITICAL_PRIORITY}), "
          f"uniqExactIf(target_id, {ch.POLARITY} = 'neg'), uniqExactIf(target_id, {ch.POLARITY} = 'pos') "
          f"FROM {ch.TABLE} WHERE {aw}")
    news, events, funding = gc.run_ch(lambda: ch.parallel([
        lambda: ch.one(ns), lambda: ch.one(_event_totals_sql(ew)),
        lambda: ch.one(f"SELECT {AMOUNT_SQL} FROM {tables.FUNDING_TABLE} WHERE {fw}")]))
    data = {"archive": public.archive(),
            "news": {"articles": int(news[0] or 0), "critical": int(news[1] or 0),
                     "negative": int(news[2] or 0), "positive": int(news[3] or 0),
                     "counting": "Distinct articles matching the requested business scope and filters."},
            "events": _event_totals(events), "funding": funding_totals(funding)}
    notes.append("News, events and funding are separate populations and must not be added together. Topic search checks article text for news, event descriptions for events and deal descriptions for funding; an explicit match mode uses source articles.")
    return envelope.ok("business.overview", data, subject=subject, window=window, meta=c.meta(t0, notes))


def event_trends(p: Principal, f: BusinessFilters, granularity: str | None = None) -> dict:
    t0 = time.time()
    g = gc.check_granularity(granularity)
    r, window, subject, notes, _aw, ew, _fw = _prepare(p, f, "events")
    bucket = ch.GRANULARITY_SQL[g].replace("datetime", "news_publish_datetime")
    sql = (f"SELECT toString({bucket}) AS period, event_type, uniqExact({EVENT_KEY}) "
           f"FROM {tables.EVENTS_TABLE} WHERE {ew} GROUP BY period, event_type ORDER BY period, event_type")
    rows, total = gc.run_ch(lambda: ch.parallel([lambda: ch.rows(sql), lambda: ch.one(_event_totals_sql(ew))]))
    types = f.event_types() or list(tables.EVENT_TYPES)
    got = {(str(period), str(kind)): int(n) for period, kind, n in rows}
    points = []
    for period in gc.periods(r.since, r.until, g):
        by_type = {kind: got.get((period["period"], kind), 0) for kind in types}
        points.append({**period, "events": sum(by_type.values()), "by_type": by_type})
    by_type = {kind: sum(pt["by_type"][kind] for pt in points) for kind in types}
    data = {"granularity": g, "points": points, "totals": _event_totals(total), "by_type": by_type,
            "complete_periods": sum(not pt["partial_period"] for pt in points),
            "partial_periods": sum(pt["partial_period"] for pt in points)}
    notes.append("Zero-count periods are included; partial_period marks buckets only partly covered by the window.")
    return envelope.ok("business.event_trends", data, subject={**subject, "granularity": g},
                       window={**window, "granularity": g}, meta=c.meta(t0, notes))


def funding_summary(p: Principal, f: BusinessFilters, granularity: str | None = None) -> dict:
    t0 = time.time()
    g = gc.check_granularity(granularity)
    r, window, subject, notes, _aw, _ew, fw = _prepare(p, f, "funding")
    bucket = ch.GRANULARITY_SQL[g].replace("datetime", "news_publish_datetime")
    sql = (f"SELECT toString({bucket}) AS period, {AMOUNT_SQL} FROM {tables.FUNDING_TABLE} "
           f"WHERE {fw} GROUP BY period ORDER BY period")
    total, rows = gc.run_ch(lambda: ch.parallel([
        lambda: ch.one(f"SELECT {AMOUNT_SQL} FROM {tables.FUNDING_TABLE} WHERE {fw}"), lambda: ch.rows(sql)]))
    got = {str(row[0]): row[1:] for row in rows}
    points = []
    for period in gc.periods(r.since, r.until, g):
        totals = funding_totals(got.get(period["period"], [0, 0, None, None, None, 0]))
        totals.pop("note")
        points.append({**period, **totals})
    data = {"totals": funding_totals(total), "granularity": g, "points": points}
    return envelope.ok("business.funding_summary", data, subject={**subject, "granularity": g},
                       window={**window, "granularity": g}, meta=c.meta(t0, notes))
