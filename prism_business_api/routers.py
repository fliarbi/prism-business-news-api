"""routers — /v1/business/* on the general dependency chain, plus the general
routes this host serves byte-identically (/v1/export, /v1/articles/{id},
/v1/me, /v1/status, /v1/vocabulary, /v1/classes*): the same APIRoute objects
from prism_news_api.routers are re-included, so one client library works on
both hosts and one key / one quota meters both."""
from __future__ import annotations

from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Path, Query, Request
from pydantic import BaseModel, ConfigDict, Field, create_model, field_validator

from prism_news_api.auth import Principal
from prism_news_api.routers import feature, guard, metered
from prism_news_api.routers import router as general_router

from .features import aggregates, company, events, funding, headlines, sentiment, themes, trends
from .filters import BusinessFilters

router = APIRouter(prefix="/v1/business")

# ── parameter models (the FastAPI 0.116 rule: no standalone Query() beside a
# query model, so granularity lives inside the model) ────────────────────────
BusinessFiltersQ = Annotated[BusinessFilters, Query()]


class BusinessFiltersWithGranularity(BusinessFilters):
    granularity: Optional[str] = Field(None, description="daily | weekly | monthly (default weekly)")


BusinessFiltersGranQ = Annotated[BusinessFiltersWithGranularity, Query()]


class BusinessThemeFilters(BusinessFilters):
    q: str = Field(..., min_length=2, max_length=120, description="A specific business topic to explore")
    limit: int = Field(5, ge=1, le=5, description="Number of suggestions, at most five")


BusinessThemeFiltersQ = Annotated[BusinessThemeFilters, Query()]


class AnalysisRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    @field_validator("*", mode="before")
    @classmethod
    def lists_to_csv(cls, value, info):
        if info.field_name in {"sentiment", "classes", "themes", "event_type", "sector", "round_type"} and isinstance(value, (list, tuple)):
            return "|".join(str(x) for x in value)
        return value

    def business(self) -> BusinessFilters:
        return BusinessFilters(**self.model_dump(exclude={"granularity"}))


# Copy field definitions, not listing controls: unsupported cursor/sort/limit/
# resolve fields fail validation instead of being silently discarded.
_ANALYSIS_FIELDS = ("q", "match", "sentiment", "classes", "class_prefix", "themes",
                    "priority_min", "priority_max", "country", "since", "until", "company", "event_type")
_FUNDING_FIELDS = ("sector", "round_type", "min_amount_usd", "investor")


def _analysis_model(name, names, *, timeline=False):
    fields = {k: (BusinessFilters.model_fields[k].annotation, BusinessFilters.model_fields[k]) for k in names}
    if timeline:
        fields["granularity"] = (Optional[str], Field(None, description="daily | weekly | monthly (default weekly)"))
    return create_model(name, __base__=AnalysisRequest, **fields)


OverviewFilters = _analysis_model("OverviewFilters", _ANALYSIS_FIELDS + _FUNDING_FIELDS)
EventTrendsFilters = _analysis_model("EventTrendsFilters", _ANALYSIS_FIELDS, timeline=True)
FundingSummaryFilters = _analysis_model("FundingSummaryFilters", _ANALYSIS_FIELDS + _FUNDING_FIELDS, timeline=True)
OverviewQ = Annotated[OverviewFilters, Query()]
EventTrendsQ = Annotated[EventTrendsFilters, Query()]
FundingSummaryQ = Annotated[FundingSummaryFilters, Query()]

SHARED_PATHS = ("/v1/export", "/v1/articles/{article_id}", "/v1/me", "/v1/status",
                "/v1/vocabulary", "/v1/classes", "/v1/classes/{code}", "/v1/classes/{code}/headlines")


@router.get("/overview", tags=["business"], summary="Measured business news, events and funding in one bounded window")
@feature("business.overview")
def overview_get(request: Request, f: OverviewQ, p: Principal = Depends(metered)):
    return guard(request, "business.overview", lambda: aggregates.overview(p, f.business()))


@router.post("/overview", tags=["business"], summary="Business overview (JSON body)")
@feature("business.overview")
def overview_post(request: Request, f: OverviewFilters, p: Principal = Depends(metered)):
    return guard(request, "business.overview", lambda: aggregates.overview(p, f.business()))


@router.get("/event-trends", tags=["business"], summary="Distinct company events over time, with totals by event type")
@feature("business.event_trends")
def event_trends_get(request: Request, f: EventTrendsQ, p: Principal = Depends(metered)):
    return guard(request, "business.event_trends", lambda: aggregates.event_trends(p, f.business(), f.granularity))


@router.post("/event-trends", tags=["business"], summary="Company event trends (JSON body)")
@feature("business.event_trends")
def event_trends_post(request: Request, f: EventTrendsFilters, p: Principal = Depends(metered)):
    return guard(request, "business.event_trends", lambda: aggregates.event_trends(p, f.business(), f.granularity))


@router.get("/funding/summary", tags=["business"], summary="Measured deal counts and reported USD amounts over time")
@feature("business.funding_summary")
def funding_summary_get(request: Request, f: FundingSummaryQ, p: Principal = Depends(metered)):
    return guard(request, "business.funding_summary", lambda: aggregates.funding_summary(p, f.business(), f.granularity))


@router.post("/funding/summary", tags=["business"], summary="Funding summary (JSON body)")
@feature("business.funding_summary")
def funding_summary_post(request: Request, f: FundingSummaryFilters, p: Principal = Depends(metered)):
    return guard(request, "business.funding_summary", lambda: aggregates.funding_summary(p, f.business(), f.granularity))


# ── headlines ────────────────────────────────────────────────────────────────
@router.get("/headlines", tags=["business"], summary="Business headlines (+ company / event_type lanes)")
@feature("business.headlines")
def headlines_get(request: Request, f: BusinessFiltersQ, p: Principal = Depends(metered)):
    return guard(request, "business.headlines", lambda: headlines.headlines(p, f))


@router.post("/headlines", tags=["business"], summary="Business headlines (JSON body)")
@feature("business.headlines")
def headlines_post(request: Request, f: BusinessFilters, p: Principal = Depends(metered)):
    return guard(request, "business.headlines", lambda: headlines.headlines(p, f))


# ── events ───────────────────────────────────────────────────────────────────
@router.get("/events", tags=["business"], summary="Company events (earnings, layoffs, M&A, …)")
@feature("business.events")
def events_get(request: Request, f: BusinessFiltersQ, p: Principal = Depends(metered)):
    return guard(request, "business.events", lambda: events.events(p, f))


@router.post("/events", tags=["business"], summary="Company events (JSON body)")
@feature("business.events")
def events_post(request: Request, f: BusinessFilters, p: Principal = Depends(metered)):
    return guard(request, "business.events", lambda: events.events(p, f))


# ── funding ──────────────────────────────────────────────────────────────────
@router.get("/funding", tags=["business"], summary="Funding rounds")
@feature("business.funding")
def funding_get(request: Request, f: BusinessFiltersQ, p: Principal = Depends(metered)):
    return guard(request, "business.funding", lambda: funding.funding(p, f))


@router.post("/funding", tags=["business"], summary="Funding rounds (JSON body)")
@feature("business.funding")
def funding_post(request: Request, f: BusinessFilters, p: Principal = Depends(metered)):
    return guard(request, "business.funding", lambda: funding.funding(p, f))


# ── one company ──────────────────────────────────────────────────────────────
@router.get("/companies/{domain}/news", tags=["business"],
            summary="Headlines + events + funding for one company domain")
@feature("business.company_news")
def company_news_get(request: Request, f: BusinessFiltersQ,
                     domain: str = Path(..., min_length=4, max_length=253),
                     p: Principal = Depends(metered)):
    return guard(request, "business.company_news", lambda: company.company_news(p, domain, f))


# ── scoped versions of the general lenses ────────────────────────────────────
@router.get("/themes", tags=["business"], summary="Themes ranked by lift inside business news")
@feature("business.themes")
def themes_get(request: Request, f: BusinessThemeFiltersQ, p: Principal = Depends(metered)):
    return guard(request, "business.themes", lambda: themes.themes(p, f))


@router.post("/themes", tags=["business"], summary="Themes (JSON body)")
@feature("business.themes")
def themes_post(request: Request, f: BusinessThemeFilters, p: Principal = Depends(metered)):
    return guard(request, "business.themes", lambda: themes.themes(p, f))


@router.get("/sentiment", tags=["business"], summary="Sentiment distribution and timeline, business scope")
@feature("business.sentiment")
def sentiment_get(request: Request, f: BusinessFiltersGranQ, p: Principal = Depends(metered)):
    return guard(request, "business.sentiment", lambda: sentiment.sentiment(p, f, f.granularity))


@router.post("/sentiment", tags=["business"], summary="Sentiment (JSON body)")
@feature("business.sentiment")
def sentiment_post(request: Request, f: BusinessFiltersWithGranularity, p: Principal = Depends(metered)):
    return guard(request, "business.sentiment", lambda: sentiment.sentiment(p, f, f.granularity))


@router.get("/trends", tags=["business"], summary="Article volume over time, business scope")
@feature("business.trends")
def trends_get(request: Request, f: BusinessFiltersGranQ, p: Principal = Depends(metered)):
    return guard(request, "business.trends", lambda: trends.trends(p, f, f.granularity))


@router.post("/trends", tags=["business"], summary="Trends (JSON body)")
@feature("business.trends")
def trends_post(request: Request, f: BusinessFiltersWithGranularity, p: Principal = Depends(metered)):
    return guard(request, "business.trends", lambda: trends.trends(p, f, f.granularity))


# ── the general routes this host also serves, unchanged ──────────────────────
def shared_router() -> APIRouter:
    """The general router's own APIRoute objects for SHARED_PATHS. Nothing is
    re-declared: same endpoint functions, dependencies, models and feature ids."""
    shared = APIRouter()
    for route in general_router.routes:
        if getattr(route, "path", None) in SHARED_PATHS:
            shared.routes.append(route)
    found = {r.path for r in shared.routes}
    missing = [p for p in SHARED_PATHS if p not in found]
    if missing:
        raise RuntimeError(f"prism_news_api.routers no longer declares {missing}")
    return shared


__all__ = ["router", "shared_router", "SHARED_PATHS", "BusinessFiltersQ", "BusinessFiltersGranQ",
           "BusinessFiltersWithGranularity"]
