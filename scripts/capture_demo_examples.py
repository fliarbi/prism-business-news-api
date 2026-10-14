#!/usr/bin/env python3
"""Capture the API responses behind the animated use-case demos.

Runs real requests against a running Business News API and saves each response
under docs/examples/demo/. Listing requests can follow `next_cursor` for a fixed
number of pages so that charts computed by the client cover the whole window.
Account details (plan, quota, key) are removed before saving.

    PRISM_API_BASE=http://127.0.0.1:8801 PRISM_API_KEY=pna_... \\
        python3 scripts/capture_demo_examples.py [--only NAME]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "docs/examples/demo"

# name -> (path, POST body, max pages)
CAPTURES: dict[str, tuple[str, dict, int]] = {
    "ai-funding-april-2026": ("/v1/business/funding", {
        "sector": ["Artificial Intelligence"], "since": "2026-04-01", "until": "2026-04-30",
        "sort": "amount", "limit": 40}, 1),
    "layoffs-april-2026": ("/v1/business/events", {
        "event_type": ["layoffs"], "since": "2026-04-01", "until": "2026-04-30", "limit": 100}, 10),
    "openai-events": ("/v1/business/events", {
        "company": "openai.com", "since": "2025-11-01", "until": "2026-04-30", "limit": 100}, 1),
    "sequoia-portfolio": ("/v1/business/funding", {
        "investor": "Sequoia", "since": "2025-11-01", "until": "2026-04-30", "limit": 100}, 5),
    "india-early-stage-q1-2026": ("/v1/business/funding", {
        "country": "India", "round_type": ["Seed", "Series A", "Series B"],
        "since": "2026-01-01", "until": "2026-03-31", "limit": 100}, 10),
    "hiring-vs-layoffs-q1-2026": ("/v1/business/events", {
        "event_type": ["job_creation", "layoffs"], "since": "2026-01-01", "until": "2026-03-31",
        "limit": 100}, 25),
}

PRIVATE_META = ("plan", "quota", "key", "account")


def post(base: str, key: str, path: str, body: dict) -> dict:
    req = urllib.request.Request(base + path, data=json.dumps(body).encode(), method="POST",
                                 headers={"X-API-Key": key, "Content-Type": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 3:
                time.sleep(int(e.headers.get("Retry-After") or 20))
                continue
            payload = json.loads(e.read() or b"{}")
            raise SystemExit(f"{path}: HTTP {e.code} {payload.get('error')}")
    raise SystemExit(f"{path}: rate limited")


def capture(base: str, key: str, name: str) -> Path:
    path, body, max_pages = CAPTURES[name]
    first = post(base, key, path, body)
    if not first.get("ok"):
        raise SystemExit(f"{name}: {first.get('error')}")
    items = list(first["data"].get("items") or [])
    pages, cursor = 1, first["data"].get("next_cursor")
    while cursor and pages < max_pages:
        page = post(base, key, path, {**body, "cursor": cursor})
        if not page.get("ok"):
            raise SystemExit(f"{name} page {pages + 1}: {page.get('error')}")
        items += page["data"].get("items") or []
        cursor, pages = page["data"].get("next_cursor"), pages + 1
    first["meta"] = {k: v for k, v in (first.get("meta") or {}).items() if k not in PRIVATE_META}
    if "items" in first["data"]:
        first["data"]["items"] = items
        first["data"]["returned"] = len(items)
        first["data"]["next_cursor"] = cursor
    record = {"name": name, "kind": "captured",
              "captured_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "request": {"method": "POST", "path": path, "body": body},
              "pages_fetched": pages, "complete": cursor is None, "response": first}
    DEST.mkdir(parents=True, exist_ok=True)
    out = DEST / f"{name}.json"
    out.write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n")
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=sorted(CAPTURES))
    args = ap.parse_args()
    base = os.environ.get("PRISM_API_BASE", "http://127.0.0.1:8801").rstrip("/")
    key = os.environ.get("PRISM_API_KEY") or sys.exit("set PRISM_API_KEY")
    for name in [args.only] if args.only else CAPTURES:
        out = capture(base, key, name)
        rec = json.loads(out.read_text())
        print(f"{name}: {rec['response']['data'].get('returned')} items, "
              f"{rec['pages_fetched']} page(s), complete={rec['complete']}")


if __name__ == "__main__":
    main()
