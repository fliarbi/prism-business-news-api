"""events — GET /v1/business/events over the company events table.

One item = one (article, company domain, event type, role); the table's
repeated sentences for the same article are grouped away (19% of rows).
`headline` is the extracted sentence the event was read from — the table
already has it, so the article store is only consulted with `resolve=true`
(url, publisher, title). Keyset on the full grouped key so a page boundary
inside one article's several events does not skip any."""
from __future__ import annotations

import time

from prism_news_api import articles, ch, envelope, filters
from prism_news_api.auth import Principal
from prism_news_api.envelope import ApiError
from prism_news_api.features import _common as gc

from .. import tables
from ..filters import (BusinessFilters, decode_events_cursor, encode_events_cursor,
                       events_keyset_sql, require_domain, word_regex)
from . import _common as c

FEATURE = "business.events"
GROUP_KEY = "target_id, domain, event_type, role, news_publish_datetime"


def _order(sort: str) -> str:
    d = "ASC" if sort == "oldest" else "DESC"
    return f"news_publish_datetime {d}, target_id {d}, domain {d}, event_type {d}, role {d}"


def events(p: Principal, f: BusinessFilters, *, feature: str = FEATURE,
           domain: str | None = None) -> dict:
    t0 = time.time()
    f.reject_news_only("/v1/business/events")
    if f.country:
        raise ApiError("bad_request", "`country` is unavailable for event listings; use /v1/business/event-trends for country-filtered analysis")
    for k in ("sector", "round_type", "min_amount_usd", "investor"):
        if getattr(f, k) is not None:
            raise ApiError("bad_request", f"`{k}` applies to /v1/business/funding only")
    sort = (f.sort or "newest").strip().lower()
    if sort not in tables.EVENT_SORTS:
        raise ApiError("bad_request", f"`sort` must be one of {', '.join(tables.EVENT_SORTS)} for events")
    tables.require_table("events")
    dt = tables.events_data_through()
    cap = int(p.plan_cfg.get("max_results") or 100)
    r = filters.resolve(f.common(sort="newest", cursor=None, country=None), p.plan_cfg, dt,
                        default_limit=min(100, cap), cap=cap)
    r.sort = sort
    cur = decode_events_cursor(f.cursor, sort) if f.cursor else None
    types = f.event_types()
    dom = domain or (require_domain(f.company, "/v1/business/events") if f.company else None)

    parts = [f"news_publish_datetime >= {ch.sql_str(r.since)}",
             f"news_publish_datetime < {ch.sql_str(r.until_exclusive)}"]
    if types:
        parts.append(f"event_type IN {ch.sql_in(types)}")
    if dom:
        parts.append(f"domain = {ch.sql_str(dom)}")
    if r.q:
        parts.append(f"match(lowerUTF8(headline), {ch.sql_str(word_regex(r.q))})")
    where_nocursor = " AND ".join(parts)
    where = where_nocursor + (f" AND {events_keyset_sql(cur, sort)}" if cur else "")

    sql_rows = (f"SELECT target_id, domain, event_type, role, toString(news_publish_datetime), any(headline) "
                f"FROM {tables.EVENTS_TABLE} WHERE {where} GROUP BY {GROUP_KEY} "
                f"ORDER BY {_order(sort)} LIMIT {r.limit + 1}")
    sql_types = (f"SELECT event_type, uniqExact((target_id, domain, role, news_publish_datetime)) AS n "
                 f"FROM {tables.EVENTS_TABLE} WHERE {where_nocursor} GROUP BY event_type ORDER BY n DESC")
    rows, by_type_rows = gc.run_ch(lambda: ch.parallel([lambda: ch.rows(sql_rows), lambda: ch.rows(sql_types)]))
    by_type = {str(t): int(n) for t, n in by_type_rows}
    total = sum(by_type.values())
    notes = list(r.notes)
    if total == 0:
        raise ApiError("no_data", "no company event matches these filters in the window",
                       meta={"seconds": round(time.time() - t0, 3), "notes": notes})
    has_more = len(rows) > r.limit
    page = rows[:r.limit]
    next_cursor = None
    if has_more and page:
        last = page[-1]
        next_cursor = encode_events_cursor(sort, last[4], last[0], last[1], last[2], last[3])

    recs, store_errors = ({}, [])
    if f.resolve:
        recs, store_errors = articles.resolve(list(dict.fromkeys(row[0] for row in page)), full=False)
    items = []
    for tid, dom_, et, role, d, headline in page:
        it = {"id": tid, "headline": headline or None, "event_type": et, "role": role,
              "domain": dom_, "published_at": d.replace(" ", "T")}
        if f.resolve:
            rec = recs.get(tid) or {}
            it.update({"url": rec.get("url"), "publisher": rec.get("publisher"),
                       "title": rec.get("headline")})
        items.append(it)
    if f.resolve:
        notes += gc.store_notes(store_errors)
        missing = sum(1 for it in items if not it.get("url"))
        if missing:
            notes.append(f"original article details are unavailable for {missing} event(s)")

    subject = {**r.subject(), "sort": sort, **f.business_subject()}
    subject.pop("match", None)                       # a news-lede mode; not used here
    if dom:
        subject["company"], subject["company_match"] = dom, "domain"
    if f.cursor:
        subject["cursor"] = True
    window = {"since": r.since, "until": r.until, "days": r.days, "data_through": dt,
              "freshness": tables.freshness_note(dt)}
    data = envelope.list_data(items, total_estimate=total, next_cursor=next_cursor,
                              by_type=by_type, limit=r.limit, sort=sort, resolved=bool(f.resolve))
    return envelope.ok(feature, data, subject={"filters": subject}, window=window,
                       meta=c.meta(t0, notes))
