#!/usr/bin/env python3
"""smoke_test — hit EVERY endpoint of a running prism-business-news-api with a real key.

    python3 smoke_test.py --key pna_…  [--base http://127.0.0.1:8801] [--samples] [--domain amazon.com]

Asserts, per call: the HTTP status is the expected one, the body is the
envelope (ok/feature/subject/data/window/meta[/error]), `ok` agrees with the
status, and every authenticated response carries the five quota headers.
Prints a table and exits non-zero on any failure. `--samples` prints trimmed
payloads for the headline, events, funding, company, themes and export calls.

The free tier allows 30 calls a minute and this script makes ~36, so it expects
to meet one 429 and honours Retry-After (reported in the table, not a failure).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ENVELOPE_KEYS = {"ok", "feature", "subject", "data", "window", "meta"}
QUOTA_HEADERS = ("x-ratelimit-limit", "x-ratelimit-remaining", "x-quota-requests-remaining",
                 "x-quota-exports-remaining", "x-plan")


def assert_public(value):
    if isinstance(value, dict):
        private = {"table", "tables", "sql", "extra_sql", "query_sql", "source_target_ids", "target_id", "subcats", "tags"}
        assert not private.intersection(value), "internal fields in public response"
        if isinstance(value.get("themes"), list):
            assert len(value["themes"]) <= 5, "too many themes"
        if "theme" in value:
            assert "type" not in value and "origin" not in value, "internal theme metadata"
        for item in value.values():
            assert_public(item)
    elif isinstance(value, list):
        for item in value:
            assert_public(item)


class Result:
    def __init__(self, status, headers, text, ms):
        self.status, self.text, self.ms = status, text, ms
        self.headers = {k.lower(): v for k, v in dict(headers).items()}
        try:
            self.json = json.loads(text) if text and text.lstrip().startswith("{") else None
        except Exception:
            self.json = None


def call(base, method, path, params=None, body=None, headers=None, timeout=90) -> Result:
    url = base.rstrip("/") + path
    if params:
        url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=headers or {})
    if data is not None:
        req.add_header("Content-Type", "application/json")
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return Result(r.status, dict(r.headers), r.read().decode("utf-8", "replace"), (time.time() - t0) * 1000)
    except urllib.error.HTTPError as e:
        return Result(e.code, dict(e.headers), e.read().decode("utf-8", "replace"), (time.time() - t0) * 1000)


def trim(o, depth=0):
    if isinstance(o, dict):
        return {k: trim(v, depth + 1) for k, v in list(o.items())[:40]}
    if isinstance(o, list):
        if o and all(isinstance(x, int) for x in o) and len(o) > 6:
            return f"[{len(o)} ints: {o[:4]}…]"
        return [trim(x, depth + 1) for x in o[:2]] + ([f"… +{len(o) - 2} more"] if len(o) > 2 else [])
    if isinstance(o, str) and len(o) > 120:
        return o[:120] + f"… ({len(o)} chars)"
    return o


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default=os.environ.get("PRISM_API_BASE", "http://127.0.0.1:8801"))
    ap.add_argument("--key", default=os.environ.get("PRISM_API_KEY"))
    ap.add_argument("--samples", action="store_true")
    ap.add_argument("--domain", default="amazon.com", help="a company domain present in the events table")
    a = ap.parse_args()
    if not a.key:
        print("need --key or PRISM_API_KEY", file=sys.stderr)
        return 2
    H = {"X-API-Key": a.key}
    B = {"Authorization": f"Bearer {a.key}"}
    rows, samples, failures = [], {}, 0
    ctx: dict = {}

    def run(name, method, path, params=None, body=None, headers=None, expect=(200,),
            kind=None, check=None, authed=True, sample=False, envelope=True):
        nonlocal failures
        r = call(a.base, method, path, params, body, headers)
        note = ""
        if r.status == 429 and 429 not in expect:
            wait = int(r.headers.get("retry-after", "5"))
            note = f"429 met, slept {wait}s; "
            time.sleep(wait + 0.5)
            r = call(a.base, method, path, params, body, headers)
        ok = r.status in expect
        is_json = r.json is not None
        if is_json and envelope:
            try:
                assert_public(r.json)
            except AssertionError as e:
                ok, note = False, note + f"public contract: {e}; "
            if not ENVELOPE_KEYS <= set(r.json):
                ok, note = False, note + "not an envelope; "
            elif r.json["ok"] != (200 <= r.status < 300):
                ok, note = False, note + "ok/status disagree; "
            if kind and (r.json.get("error") or {}).get("kind") != kind:
                ok, note = False, note + f"kind={((r.json.get('error') or {}).get('kind'))}; "
        elif not is_json and r.status < 400 and "text/csv" not in r.headers.get("content-type", "") \
                and "ndjson" not in r.headers.get("content-type", ""):
            ok, note = False, note + "non-JSON body; "
        if authed and r.status not in (401,):
            missing = [h for h in QUOTA_HEADERS if h not in r.headers]
            if missing:
                ok, note = False, note + f"missing headers {missing}; "
        if ok and check:
            try:
                msg = check(r)
                if msg:
                    note += msg
            except AssertionError as e:
                ok, note = False, note + f"check failed: {e}; "
            except Exception as e:
                ok, note = False, note + f"check error: {type(e).__name__}: {e}; "
        if not ok:
            failures += 1
        rows.append((name, f"{method} {path}", r.status, "/".join(map(str, expect)), f"{r.ms:.0f}",
                     "PASS" if ok else "FAIL", note.strip()))
        if sample and r.json:
            samples[name] = r.json
        return r

    # ── no key / liveness ────────────────────────────────────────────────────
    def health_check(r):
        assert r.json == {"ok": True}, "liveness must contain only ok"
        return "alive"
    run("healthz", "GET", "/healthz", authed=False, envelope=False, check=health_check)
    run("openapi", "GET", "/v1/openapi.json", authed=False, envelope=False,
        check=lambda r: (lambda s: f"{len(s['paths'])} paths; business scope={s['info'].get('x-business-scope')}")(json.loads(r.text)))
    run("no key → 401", "GET", "/v1/business/headlines", expect=(401,), kind="unauthenticated", authed=False)
    run("bad key → 401", "GET", "/v1/business/events", headers={"X-API-Key": "pna_" + "0" * 40},
        expect=(401,), kind="invalid_key", authed=False)

    # ── shared general routes (unmetered) ────────────────────────────────────
    run("me (Bearer)", "GET", "/v1/me", headers=B,
        check=lambda r: f"plan={r.json['data']['plan']['name']} used={r.json['data']['usage']['requests']['used']}")
    run("status", "GET", "/v1/status", headers=H,
        check=lambda r: f"healthy={r.json['data']['healthy']}; coverage={r.json['meta']['coverage']}")
    run("vocabulary", "GET", "/v1/vocabulary", headers=H,
        check=lambda r: f"{r.json['data']['class_count']} classes")
    run("classes/0", "GET", "/v1/classes/0", headers=H, check=lambda r: r.json["data"]["path"])

    # ── business headlines ───────────────────────────────────────────────────
    def hl_check(r):
        d = r.json["data"]
        assert d["returned"] >= 1, "no items"
        it = d["items"][0]
        for k in ("id", "headline", "url", "publisher", "published_at", "lede", "sentiment", "priority",
                  "classes", "organizations", "people", "events"):
            assert k in it, f"item lacks {k}"
        assert "themes" not in it, "theme discovery requires a topic query"
        assert r.json["subject"]["scope"]["applied"] in ("default", "caller")
        ctx.setdefault("ids", []).extend(i["id"] for i in d["items"])
        ctx["lede_len"] = len(it["lede"] or "")
        return (f"{d['returned']} items / {d['total_estimate']:,} total; with_events={d.get('with_events')}; "
                f"scope={r.json['subject']['scope']['applied']} ({len(r.json['subject']['filters'].get('classes') or [])} codes)")

    run("headlines q=acquisition neg", "GET", "/v1/business/headlines",
        {"q": "acquisition", "sentiment": "negative", "limit": 5}, headers=H, check=hl_check, sample=True)
    run("headlines company=domain", "GET", "/v1/business/headlines", {"company": a.domain, "limit": 5}, headers=H,
        check=lambda r: hl_check(r) + f"; window={r.json['window']['since']}..{r.json['window']['until']}")
    run("headlines company=name + event_type", "GET", "/v1/business/headlines",
        {"company": "Amazon", "event_type": "layoffs", "limit": 3}, headers=H, check=hl_check)
    run("headlines classes=0 (caller scope)", "GET", "/v1/business/headlines", {"classes": 0, "limit": 2}, headers=H,
        check=lambda r: f"scope={r.json['subject']['scope']['applied']} classes={r.json['subject']['filters']['classes']}")
    run("headlines POST body", "POST", "/v1/business/headlines",
        body={"event_type": ["ipo"], "sentiment": ["positive"], "limit": 3}, headers=H, check=hl_check)
    run("headlines bad event_type → 400", "GET", "/v1/business/headlines", {"event_type": "mergers"}, headers=H,
        expect=(400,), kind="bad_request")
    run("headlines sector → 400", "GET", "/v1/business/headlines", {"sector": "fintech"}, headers=H,
        expect=(400,), kind="bad_request")

    # ── events ───────────────────────────────────────────────────────────────
    def ev_check(r):
        d = r.json["data"]
        assert d["returned"] >= 1, "no events"
        it = d["items"][0]
        for k in ("id", "headline", "event_type", "role", "domain", "published_at"):
            assert k in it, f"event lacks {k}"
        assert set(d["by_type"]) <= {"layoffs", "ipo"}, d["by_type"]
        ctx["ev_cursor"] = d.get("next_cursor")
        ctx["ev_ids"] = [i["id"] for i in d["items"]]
        return f"{d['returned']} / {d['total_estimate']:,}; by_type={d['by_type']}; window={r.json['window']['since']}..{r.json['window']['until']}"
    run("events layoffs,ipo x20", "GET", "/v1/business/events", {"event_type": "layoffs,ipo", "limit": 20}, headers=H,
        check=ev_check, sample=True)
    run("events page 2 (cursor)", "GET", "/v1/business/events",
        {"event_type": "layoffs,ipo", "limit": 20, "cursor": ctx.get("ev_cursor")}, headers=H,
        check=lambda r: (lambda ids: f"{len(ids)} items, disjoint={not (set(ids) & set(ctx['ev_ids']))}")(
            [i["id"] for i in r.json["data"]["items"]]))
    run("events company resolve=true", "GET", "/v1/business/events", {"company": a.domain, "resolve": "true", "limit": 5},
        headers=H, check=lambda r: f"{r.json['data']['returned']} items; urls={sum(1 for i in r.json['data']['items'] if i.get('url'))}")
    run("events q=tariff", "GET", "/v1/business/events", {"q": "tariff", "limit": 5}, headers=H,
        check=lambda r: f"{r.json['data']['returned']} / {r.json['data']['total_estimate']}")
    run("events bad event_type → 400", "GET", "/v1/business/events", {"event_type": "mergers"}, headers=H,
        expect=(400,), kind="bad_request")
    run("events company=name → 400", "GET", "/v1/business/events", {"company": "Amazon"}, headers=H,
        expect=(400,), kind="bad_request")
    run("events sentiment → 400", "GET", "/v1/business/events", {"sentiment": "negative"}, headers=H,
        expect=(400,), kind="bad_request")

    # ── funding ──────────────────────────────────────────────────────────────
    def fr_check(r):
        d = r.json["data"]
        assert d["returned"] >= 1, "no deals"
        it = d["items"][0]
        for k in ("company_name", "domain", "round_type", "amount_usd", "valuation_usd", "currency", "investors",
                  "sector", "country", "city", "use_of_funds", "source_sentence", "published_at", "coverage_count",
                  "article_ids"):
            assert k in it, f"deal lacks {k}"
        assert all((i["amount_usd"] or 0) >= 50_000_000 for i in d["items"]), "amount below min"
        ctx["fr_cursor"] = d.get("next_cursor")
        return f"{d['returned']} / {d['total_estimate']}; totals={ {k: v for k, v in d['totals'].items() if k != 'note'} }"
    run("funding ≥50M series b", "GET", "/v1/business/funding",
        {"min_amount_usd": 50000000, "round_type": "series b", "limit": 5}, headers=H, check=fr_check, sample=True)
    run("funding page 2 (cursor)", "GET", "/v1/business/funding",
        {"min_amount_usd": 50000000, "round_type": "series b", "limit": 5, "cursor": ctx.get("fr_cursor")}, headers=H,
        check=lambda r: f"{r.json['data']['returned']} items")
    run("funding sector=space sort=amount", "GET", "/v1/business/funding", {"sector": "space", "sort": "amount", "limit": 3},
        headers=H, check=lambda r: "amounts=" + str([i["amount_usd"] for i in r.json["data"]["items"]]))
    run("funding investor=sequoia country=USA", "GET", "/v1/business/funding",
        {"investor": "sequoia", "country": "USA", "limit": 3}, headers=H,
        check=lambda r: f"{r.json['data']['returned']} / {r.json['data']['total_estimate']}")
    run("funding min_amount_usd=abc → 400", "GET", "/v1/business/funding", {"min_amount_usd": "abc"}, headers=H,
        expect=(400,), kind="bad_request")

    # ── one company ──────────────────────────────────────────────────────────
    run(f"companies/{a.domain}/news", "GET", f"/v1/business/companies/{a.domain}/news", {"limit": 5}, headers=H,
        check=lambda r: f"counts={r.json['data']['counts']}; linkage_through={r.json['window']['linkage_data_through']}",
        sample=True)
    run("companies/Amazon/news → 400", "GET", "/v1/business/companies/Amazon/news", headers=H, expect=(400,), kind="bad_request")

    # ── scoped lenses ────────────────────────────────────────────────────────
    run("themes without q → 400", "GET", "/v1/business/themes", headers=H, expect=(400,), kind="bad_request")
    run("themes limit>5 → 400", "GET", "/v1/business/themes", {"q": "tariff", "limit": 6}, headers=H, expect=(400,), kind="bad_request")
    run("themes q=tariff", "GET", "/v1/business/themes", {"q": "tariff", "limit": 5}, headers=H,
        check=lambda r: f"top={r.json['data']['items'][0]['theme']!r} n={r.json['data']['items'][0]['count']}; feature={r.json['feature']}",
        sample=True)
    run("sentiment company monthly", "GET", "/v1/business/sentiment", {"company": a.domain, "granularity": "monthly"},
        headers=H, check=lambda r: f"carrying={r.json['data']['carrying']} ratio={r.json['data']['negative_to_positive_ratio']}")
    run("trends event_type=layoffs monthly", "GET", "/v1/business/trends", {"event_type": "layoffs", "granularity": "monthly"},
        headers=H, check=lambda r: f"total={r.json['data']['total']} pts={len(r.json['data']['points'])}")

    def aggregate_check(r):
        d, w = r.json["data"], r.json["window"]
        assert 1 <= w["days"] <= 366
        if r.json["feature"] == "business.overview":
            assert d["archive"]["article_count_display"] == "450M+"
            assert d["news"]["articles"] >= 0
            totals = d["funding"]
        elif r.json["feature"] == "business.event_trends":
            assert sum(p["events"] for p in d["points"]) == d["totals"]["events"]
            assert sum(d["by_type"].values()) == d["totals"]["events"]
            return f"{d['totals']['events']} events over {w['days']} days"
        else:
            totals = d["totals"]
            assert sum(p["deals"] for p in d["points"]) == totals["deals"]
            assert abs(sum(p["sum_amount_usd"] or 0 for p in d["points"]) - (totals["sum_amount_usd"] or 0)) <= 0.01 * (len(d["points"]) + 1)
        assert totals["deals"] == totals["deals_with_amount"] + totals["deals_without_amount"]
        assert totals["note"] and totals["currency"] == "USD"
        if totals["deals_with_amount"] == 0:
            assert totals["sum_amount_usd"] is None and totals["median_amount_usd"] is None
        return f"{totals['deals']} measured deals; USD={totals['sum_amount_usd']}"

    for endpoint in ("overview", "event-trends", "funding/summary"):
        run(endpoint + " GET", "GET", "/v1/business/" + endpoint, headers=H, check=aggregate_check, sample=True)
        run(endpoint + " POST", "POST", "/v1/business/" + endpoint, body={}, headers=H, check=aggregate_check)

    # ── export + article (the general routes, same behaviour) ────────────────
    def exp_check(r):
        d = r.json["data"]
        assert d["returned"] >= 1, "nothing exported"
        short = [i["id"] for i in d["items"] if (i.get("body_chars") or 0) <= len(i.get("lede") or "")]
        assert not short, f"bodies not longer than lede for {short}"
        return f"{d['returned']} delivered, charged={d['charged_exports']}, min body={min(i['body_chars'] for i in d['items'])} chars; feature={r.json['feature']}"
    run("export json x3 (business)", "POST", "/v1/export",
        body={"class_prefix": "/News/Business News", "q": "acquisition", "limit": 3, "format": "json"}, headers=H,
        check=exp_check, sample=True)
    aid = (ctx.get("ids") or ["000000000000000000000000"])[0]
    run("articles/{id}", "GET", f"/v1/articles/{aid}", headers=H,
        check=lambda r: f"body_chars={r.json['data']['article']['body_chars']}; feature={r.json['feature']}")
    # an unknown route is answered by the 404 handler before the auth chain runs (as on the general host),
    # so no quota headers are expected on it
    run("unknown route → 404", "GET", "/v1/headlines", headers=H, expect=(404,), kind="no_data", authed=False)

    # ── table ────────────────────────────────────────────────────────────────
    hdr = ("case", "call", "status", "expect", "ms", "result", "note")
    w = [max(len(str(r[i])) for r in rows + [hdr]) for i in range(7)]
    fmt = "  ".join("{:<%d}" % x for x in w)
    print(fmt.format(*hdr))
    print("-" * (sum(w) + 12))
    for r in rows:
        print(fmt.format(*[str(x) for x in r]))
    print(f"\n{len(rows) - failures}/{len(rows)} passed")
    if a.samples:
        print("\n=== samples (trimmed) ===")
        for k, v in samples.items():
            print(f"\n--- {k}")
            print(json.dumps(trim(v), indent=1, ensure_ascii=False, default=str))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
