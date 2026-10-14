"""themes — GET /v1/business/themes: the general lift-ranked themes under the
business scope (+ company / event_type lanes)."""
from __future__ import annotations

from prism_news_api.auth import Principal
from prism_news_api.envelope import ApiError
from prism_news_api.features import themes as general

from ..filters import BusinessFilters
from . import _common as c

FEATURE = "business.themes"


def themes(p: Principal, f: BusinessFilters) -> dict:
    if not f.q or not f.q.strip():
        raise ApiError("bad_request", "`q` is required to explore themes for a topic")
    f2, scope, notes = c.prepare(f)
    f2 = f2.model_copy(update={"limit": min(f.limit or 5, 5)})
    if f.limit and f.limit > 5:
        notes.append("theme results are limited to 5")
    return c.finish(general.themes(p, f2), f, scope, notes, feature=FEATURE)
