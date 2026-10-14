"""trends — GET /v1/business/trends: article volume over time under the
business scope (+ company / event_type lanes)."""
from __future__ import annotations

from prism_news_api.auth import Principal
from prism_news_api.features import trends as general

from ..filters import BusinessFilters
from . import _common as c

FEATURE = "business.trends"


def trends(p: Principal, f: BusinessFilters, granularity: str | None = None) -> dict:
    f2, scope, notes = c.prepare(f)
    return c.finish(general.trends(p, f2, granularity), f, scope, notes, feature=FEATURE)
