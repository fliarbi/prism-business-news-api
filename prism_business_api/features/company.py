"""company — GET /v1/business/companies/{domain}/news: headlines, events and
funding for one company domain in one envelope. Each block carries its own
count and window because the three sources end on different days; a block
with nothing is served empty, and only when all three are empty is the answer
404 no_data."""
from __future__ import annotations

import time

from prism_news_api import ch
from prism_news_api.auth import Principal
from prism_news_api.envelope import ApiError

from .. import tables
from ..filters import BusinessFilters, require_domain
from ..scope import scope_block
from . import _common as c
from . import events as ev
from . import funding as fr
from . import headlines as hl

FEATURE = "business.company_news"


def _block(fn) -> dict:
    try:
        env = fn()
    except ApiError as e:
        if e.kind != "no_data":
            raise
        return {"items": [], "returned": 0, "total_estimate": 0, "next_cursor": None,
                "window": None, "notes": list((e.meta or {}).get("notes") or []),
                "empty_reason": e.reason}
    d = dict(env["data"])
    d["window"] = env.get("window")
    d["notes"] = list((env.get("meta") or {}).get("notes") or [])
    return d


def company_news(p: Principal, domain: str, f: BusinessFilters) -> dict:
    t0 = time.time()
    dom = require_domain(domain, "/v1/business/companies/{domain}/news")
    if f.company and require_domain(f.company, "`company`") != dom:
        raise ApiError("bad_request", "`company` in the query disagrees with the domain in the path")
    f_news = f.model_copy(update={"company": dom, "cursor": None, "sector": None, "round_type": None,
                                  "min_amount_usd": None, "investor": None, "resolve": False})
    # events / funding take only the window and limit; news lenses stay on the headlines block
    f_tbl = BusinessFilters(since=f.since, until=f.until, limit=f.limit)
    headlines = _block(lambda: hl.headlines(p, f_news))
    events = _block(lambda: ev.events(p, f_tbl, domain=dom))
    funding = _block(lambda: fr.funding(p, f_tbl, domain=dom))
    if not (headlines["returned"] or events["returned"] or funding["returned"]):
        raise ApiError("no_data", f"no business headlines, company events or funding rounds for {dom} in the window",
                       meta={"seconds": round(time.time() - t0, 3),
                             "notes": headlines["notes"] + events["notes"] + funding["notes"]})
    scope = scope_block("caller" if (f.classes or f.class_prefix) else "default")
    ldt = tables.linkage_data_through()
    data = {"domain": dom, "headlines": headlines, "events": events, "funding": funding,
            "counts": {"headlines": headlines["total_estimate"], "events": events["total_estimate"],
                       "funding": funding["total_estimate"]}}
    notes = list(dict.fromkeys(headlines["notes"] + events["notes"] + funding["notes"]))
    window = {"headlines": headlines["window"], "events": events["window"], "funding": funding["window"],
              "data_through": ch.data_through(), "linkage_data_through": ldt,
              "freshness": tables.freshness_note(ldt)}
    subject = {"domain": dom, "filters": {**f_news.business_subject(), "since": f.since, "until": f.until,
                                          "limit": f.limit}, "scope": scope}
    from prism_news_api import envelope
    return envelope.ok(FEATURE, data, subject=subject, window=window, meta=c.meta(t0, notes))
