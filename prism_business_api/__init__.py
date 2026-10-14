"""prism_business_api — the Prism Business News Exploration API.

A thin second product on top of `prism_news_api` (imported, never copied):
the same key, quota, envelope, ClickHouse client and article store, with

  * a default BUSINESS SCOPE (GCP classes under /News/Business News,
    /Business & Industrial and /Finance) on every news lens,
  * two extra tables — company events (`PRISM_EVENTS_TABLE`)
    and funding rounds (`PRISM_FUNDING_TABLE`),
  * `company` / `event_type` lanes that link articles to company domains.

Configuration is `PRISM_*` environment variables; this repo's `.env` (or
`PRISM_ENV_FILE`) is read here, before the general package reads its own.
"""
from __future__ import annotations

import os as _os
from pathlib import Path as _Path


def _load_env(path) -> None:
    try:
        lines = _Path(path).read_text().splitlines()
    except OSError:
        return
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            _os.environ.setdefault(k.strip().removeprefix("export ").strip(), v.strip().strip("'\""))


_load_env(_os.environ.get("PRISM_ENV_FILE") or _Path(__file__).resolve().parent.parent / ".env")

__version__ = "0.2.0"
