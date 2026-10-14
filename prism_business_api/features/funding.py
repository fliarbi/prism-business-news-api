"""funding — GET /v1/business/funding over the funding rounds table.

One row = one deduplicated deal (the view groups the per-article extractions
by fingerprint and keeps the earliest article's fields; `coverage_count` is
how many articles reported it, `source_target_ids` which ones). amount_usd is
the view's fixed-rate conversion and is 0 when no amount was extracted —
served as null, and the totals say how many deals carried one.

Sort newest | oldest | amount. Keyset on (published_at, row key) where the row
key is a hash of the deal's identifying fields (365,513 distinct of 365,555)."""
from __future__ import annotations

import time
import math

from prism_news_api import ch, envelope, filters
from prism_news_api.auth import Principal
from prism_news_api.envelope import ApiError
from prism_news_api.features import _common as gc

from .. import tables
from ..filters import (FUNDING_K, BusinessFilters, country_sql, decode_funding_cursor,
                       encode_funding_cursor, funding_company_sql, funding_keyset_sql,
                       funding_order_sql, investor_sql, round_type_sql, sector_sql, word_regex)
from . import _common as c
from .aggregates import AMOUNT_SQL, funding_totals

FEATURE = "business.funding"
COLS = ("company_name, domain, round_type, amount_usd, valuation_usd, currency, amount, valuation, "
        "investor, sector, country, city, use_of_funds, source_sentence, "
        f"toString(assumeNotNull(news_publish_datetime)), coverage_count, source_target_ids, target_id, {FUNDING_K}, "
        f"{tables.USABLE_AMOUNT}")


def _num(v):
    try:
        x = float(v)
    except (TypeError, ValueError):
        return None
    return x if math.isfinite(x) and x > 0 else None


def _flag(amt_usd, usable, cur, amt) -> str | None:
    """Why a reported amount is withheld from amount_usd and from the totals."""
    if _num(usable) or not _num(amt_usd):
        return None
    if _num(amt) == _num(amt_usd) and (cur or "").strip().upper() not in ("", "USD", "US$", "$"):
        return "unconverted_currency"
    return "implausible_size"


def _item(row: list) -> dict:
    (name, domain, rt, amt_usd, val_usd, cur, amt, val, inv, sector, country, city, use,
     sent, d, cov, srcs, tid, k, usable) = row
    investors = [{"name": i[0], "domain": i[1] or None, "amount": _num(i[2])} for i in (inv or [])]
    return {"id": f"{int(k):016x}", "company_name": name, "domain": domain or None,
            "round_type": rt, "amount_usd": _num(usable), "amount_flag": _flag(amt_usd, usable, cur, amt),
            "valuation_usd": _num(val_usd),
            "currency": cur, "amount": _num(amt), "valuation": _num(val),
            "investors": investors, "sector": sector, "country": country, "city": city,
            "use_of_funds": use, "source_sentence": sent,
            "published_at": d.replace(" ", "T"), "coverage_count": int(cov or 0),
            "article_ids": list(srcs or []), "article_id": tid}


def funding(p: Principal, f: BusinessFilters, *, feature: str = FEATURE,
            domain: str | None = None) -> dict:
    t0 = time.time()
    f.reject_news_only("/v1/business/funding")
    if f.event_type or f.resolve:
        raise ApiError("bad_request", "`event_type` / `resolve` apply to /v1/business/events, not funding")
    sort = (f.sort or "newest").strip().lower()
    if sort not in tables.FUNDING_SORTS:
        raise ApiError("bad_request", f"`sort` must be one of {', '.join(tables.FUNDING_SORTS)} for funding")
    tables.require_table("funding")
    dt = tables.funding_data_through()
    cap = int(p.plan_cfg.get("max_results") or 100)
    r = filters.resolve(f.common(sort="newest", cursor=None, country=None), p.plan_cfg, dt,
                        default_limit=min(100, cap), cap=cap)
    r.sort = sort
    cur = decode_funding_cursor(f.cursor, sort) if f.cursor else None

    parts = [f"news_publish_datetime >= {ch.sql_str(r.since)}",
             f"news_publish_datetime < {ch.sql_str(r.until_exclusive)}"]
    rts, sectors = f.round_types(), f.sectors()
    if rts:
        parts.append(round_type_sql(rts))
    if f.min_amount_usd is not None:
        parts.append(f"{tables.USABLE_AMOUNT} >= {float(f.min_amount_usd)!r}")
    if sectors:
        parts.append(sector_sql(sectors))
    if f.country:
        parts.append(country_sql(f.country))
    if f.investor:
        parts.append(investor_sql(f.investor))
    if domain:
        parts.append(f"lowerUTF8(coalesce(domain, '')) = {ch.sql_str(domain)}")
    elif f.company:
        parts.append(funding_company_sql(f.company))
    if r.q:
        rx = ch.sql_str(word_regex(r.q))
        parts.append(f"(match(lowerUTF8(coalesce(source_sentence, '')), {rx}) "
                     f"OR match(lowerUTF8(coalesce(company_name, '')), {rx}) "
                     f"OR match(lowerUTF8(coalesce(use_of_funds, '')), {rx}))")
    where_nocursor = " AND ".join(parts)
    where = where_nocursor + (f" AND {funding_keyset_sql(cur, sort)}" if cur else "")

    sql_rows = (f"SELECT {COLS} FROM {tables.FUNDING_TABLE} WHERE {where} "
                f"ORDER BY {funding_order_sql(sort)} LIMIT {r.limit + 1}")
    sql_tot = f"SELECT {AMOUNT_SQL} FROM {tables.FUNDING_TABLE} WHERE {where_nocursor}"
    rows, tot = gc.run_ch(lambda: ch.parallel([lambda: ch.rows(sql_rows), lambda: ch.one(sql_tot)]))
    deals = int(tot[0] or 0)
    notes = list(r.notes)
    if deals == 0:
        raise ApiError("no_data", "no funding round matches these filters in the window",
                       meta={"seconds": round(time.time() - t0, 3), "notes": notes})
    has_more = len(rows) > r.limit
    page = rows[:r.limit]
    items = [_item(row) for row in page]
    next_cursor = None
    if has_more and page:
        last = page[-1]
        next_cursor = encode_funding_cursor(sort, last[14], int(last[18]), float(last[19] or 0))
    totals = funding_totals(tot)
    subject = {**r.subject(), "sort": sort, **f.business_subject()}
    subject.pop("match", None)                       # a news-lede mode; not used here
    if domain:
        subject["company"], subject["company_match"] = domain, "domain"
    if f.country:
        subject["country"] = " ".join(f.country.lower().split())
    if f.cursor:
        subject["cursor"] = True
    window = {"since": r.since, "until": r.until, "days": r.days, "data_through": dt,
              "freshness": tables.freshness_note(dt)}
    data = envelope.list_data(items, total_estimate=deals, next_cursor=next_cursor,
                              totals=totals, limit=r.limit, sort=sort)
    return envelope.ok(feature, data, subject={"filters": subject}, window=window,
                       meta=c.meta(t0, notes))
