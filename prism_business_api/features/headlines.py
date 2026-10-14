"""headlines — GET /v1/business/headlines: the general headlines under the
business scope, plus `company` / `event_type` lanes, and each item carries
`events`: the (event_type, domain, role) rows the events table holds for it."""
from __future__ import annotations

from prism_news_api.auth import Principal
from prism_news_api.features import headlines as general

from ..filters import BusinessFilters
from . import _common as c

FEATURE = "business.headlines"


def headlines(p: Principal, f: BusinessFilters, *, feature: str = FEATURE) -> dict:
    f2, scope, notes = c.prepare(f)
    env = general.headlines(p, f2, feature=feature)
    items = env["data"]["items"]
    ev = c.events_for_ids([it["id"] for it in items])
    for it in items:
        it["events"] = ev.get(it["id"], [])
    env["data"]["with_events"] = sum(1 for it in items if it["events"])
    return c.finish(env, f, scope, notes)
