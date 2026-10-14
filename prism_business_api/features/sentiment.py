"""sentiment — GET /v1/business/sentiment: the general distribution + timeline
under the business scope (+ company / event_type lanes)."""
from __future__ import annotations

from prism_news_api.auth import Principal
from prism_news_api.features import sentiment as general

from ..filters import BusinessFilters
from . import _common as c

FEATURE = "business.sentiment"


def sentiment(p: Principal, f: BusinessFilters, granularity: str | None = None) -> dict:
    f2, scope, notes = c.prepare(f)
    return c.finish(general.sentiment(p, f2, granularity), f, scope, notes, feature=FEATURE)
