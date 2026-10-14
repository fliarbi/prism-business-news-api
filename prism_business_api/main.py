"""main — create_app(); the ASGI entry point is `prism_business_api.main:app`.

    gunicorn -k uvicorn.workers.UvicornWorker -w 2 -b 0.0.0.0:8801 prism_business_api.main:app

Same key, same quota, same envelope and error handlers as the general API
(`prism_news_api.routers.install_handlers`); /healthz needs no key.
"""
from __future__ import annotations

import logging
import os
import sys
from importlib.resources import files

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import PlainTextResponse

from prism_news_api import envelope
from prism_news_api.main import EXPOSE_HEADERS
from prism_news_api.routers import install_handlers

from . import __version__, routers
from .scope import BUSINESS_PREFIXES

DESCRIPTION = """
Explore business headlines, company events, funding deals and measured trends.
Filter by topic, company, event type, sentiment, category, country and date.
Funding analysis also supports sector, round type, investor and minimum USD amount.

Prism's owner-provided archive size is 450M+ articles. This product-wide figure
is separate from measured API counts for a requested dataset and date window.
Aggregations use at most 366 days per request, within your plan's history access.
Theme exploration requires a search query and returns at most five results.
Read the [user guide](/guide) for examples, pagination and quota rules.

Every response is one envelope — `ok, feature, subject, data, window, meta`
and `error` when `ok` is false. Every number states the window it was counted
over. Freshness dates identify the latest available data for each dataset.

Authenticate with `X-API-Key: pna_…` or `Authorization: Bearer pna_…` — the
same key, plan and monthly quota as the Prism News API.
"""


def _logging() -> None:
    level = os.environ.get("PRISM_LOG_LEVEL", "INFO").upper()
    root = logging.getLogger()
    if not root.handlers:
        h = logging.StreamHandler(sys.stderr)
        h.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
        root.addHandler(h)
    root.setLevel(level)
    logging.getLogger("pymongo").setLevel(logging.WARNING)


def create_app() -> FastAPI:
    _logging()
    app = FastAPI(title="Prism Business News Exploration API", version=__version__,
                  description=DESCRIPTION.strip(), docs_url="/docs", redoc_url=None,
                  openapi_url="/v1/openapi.json",
                  contact={"name": "Fliar Business Intelligence", "url": "https://fliarbi.com"})
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=False,
                       allow_methods=["*"], allow_headers=["*"], expose_headers=EXPOSE_HEADERS)
    app.include_router(routers.router)
    app.include_router(routers.shared_router())
    install_handlers(app)

    @app.get("/healthz", tags=["meta"], summary="Liveness (no auth)")
    def healthz():
        return {"ok": True}

    @app.get("/guide", include_in_schema=False)
    def guide():
        return PlainTextResponse(files("prism_business_api").joinpath("data/user_guide.md").read_text(),
                                 media_type="text/markdown")

    def openapi():
        if app.openapi_schema:
            return app.openapi_schema
        schema = get_openapi(title=app.title, version=app.version, description=app.description,
                             routes=app.routes, contact=app.contact)
        comps = schema.setdefault("components", {})
        comps["securitySchemes"] = {
            "ApiKeyAuth": {"type": "apiKey", "in": "header", "name": "X-API-Key"},
            "BearerAuth": {"type": "http", "scheme": "bearer"}}
        comps.setdefault("schemas", {})["Envelope"] = {
            "type": "object",
            "properties": {"ok": {"type": "boolean"}, "feature": {"type": "string"},
                           "subject": {"type": "object"}, "data": {},
                           "window": {"type": "object"}, "meta": {"type": "object"},
                           "error": {"type": "object", "properties": {
                               "kind": {"type": "string", "enum": list(envelope.KINDS)},
                               "reason": {"type": "string"}}}},
            "required": ["ok", "feature", "subject", "data", "window", "meta"]}
        for path, ops in schema.get("paths", {}).items():
            for op in ops.values():
                if not isinstance(op, dict):
                    continue
                if path == "/healthz":
                    op["responses"]["200"]["content"]["application/json"]["schema"] = {
                        "type": "object", "properties": {"ok": {"type": "boolean"}},
                        "required": ["ok"], "additionalProperties": False}
                    continue
                if not path.startswith("/v1/"):
                    continue
                op["security"] = [{"ApiKeyAuth": []}, {"BearerAuth": []}]
                responses = op.setdefault("responses", {})
                responses.pop("422", None)
                for code, description in (("400", "Invalid parameters"), ("401", "API key required or invalid"),
                    ("402", "Monthly quota reached"), ("404", "No matching data"),
                    ("429", "Rate limit reached; respect Retry-After"), ("500", "Request could not be completed"),
                    ("502", "Data temporarily unavailable"), ("503", "Reliable coverage temporarily unavailable")):
                    responses.setdefault(code, {"description": description})
                for resp in responses.values():
                    resp.setdefault("content", {}).setdefault("application/json", {})["schema"] = {
                        "$ref": "#/components/schemas/Envelope"}
                if path == "/v1/export":
                    for media in ("text/csv", "application/x-ndjson"):
                        responses["200"]["content"][media] = {"schema": {"type": "string"}}
        schema["info"]["x-business-scope"] = list(BUSINESS_PREFIXES)
        app.openapi_schema = schema
        return schema

    app.openapi = openapi
    return app


app = create_app()
