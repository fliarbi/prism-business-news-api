"""HTTP surface with every store stubbed: business routes, envelope kinds,
the shared general routes, and the byte-identical shape of /v1/export and
/v1/articles/{id} across the two apps."""
from __future__ import annotations

import json

import pytest

from prism_news_api import ch
from prism_news_api.envelope import ApiError

from prism_business_api.filters import FUNDING_AMT
from prism_business_api import tables
from tests.conftest import EVENT_ROWS, H, ID1, ID2, USER_ID


def _env(r):
    b = r.json()
    assert set(b) >= {"ok", "feature", "subject", "data", "window", "meta"}, b
    assert b["ok"] == (200 <= r.status_code < 300)
    return b


# ── auth / envelope kinds ────────────────────────────────────────────────────
def test_no_key_401_bad_key_401_unknown_route_404(client):
    r = client.get("/v1/business/headlines")
    assert r.status_code == 401 and _env(r)["error"]["kind"] == "unauthenticated"
    r = client.get("/v1/business/events", headers={"Authorization": "Bearer pna_" + "cd" * 20})
    assert r.status_code == 401 and _env(r)["error"]["kind"] == "invalid_key"
    r = client.get("/v1/business/nothing", headers=H(client))
    assert r.status_code == 404 and _env(r)["error"]["kind"] == "no_data"
    assert client.get("/healthz").status_code == 200 and client.get("/healthz").json() == {"ok": True}


def test_coverage_gate_503_before_any_query(client, monkeypatch):
    monkeypatch.setattr(ch, "coverage", lambda force=False: {"rows": 1, "expected": 255_586_690, "pct": 0.0,
                                                             "partial": True, "checked_at": 0})
    n = len(client.fake.sql)
    r = client.get("/v1/business/headlines", headers=H(client))
    assert r.status_code == 503 and _env(r)["error"]["kind"] == "coverage_unavailable"
    assert len(client.fake.sql) == n


def test_events_table_floor_503(client, monkeypatch):
    def thin(which):
        raise ApiError("coverage_unavailable", "table mid-refresh")
    monkeypatch.setattr(tables, "require_table", thin)
    r = client.get("/v1/business/events", headers=H(client))
    assert r.status_code == 503 and _env(r)["error"]["kind"] == "coverage_unavailable"
    assert not any(tables.EVENTS_TABLE in s for s in client.fake.sql)


def test_internal_error_is_an_envelope(client, monkeypatch):
    def boom(*a, **k):
        raise RuntimeError("secret " * 100)
    monkeypatch.setattr(ch, "rows", boom)
    r = client.get("/v1/business/events", headers=H(client))
    b = _env(r)
    assert r.status_code == 500 and b["error"]["kind"] == "internal" and b["feature"] == "business.events"
    assert "Traceback" not in r.text and len(b["error"]["reason"]) < 260


# ── headlines ────────────────────────────────────────────────────────────────
def test_headlines_scope_events_and_headers(client, fake_redis):
    r = client.get("/v1/business/headlines", params={"q": "amazon jobs", "limit": 2}, headers=H(client))
    b = _env(r)
    assert r.status_code == 200 and b["feature"] == "business.headlines"
    assert b["subject"]["scope"]["applied"] == "default" and b["subject"]["scope"]["class_count"] == 138
    assert len(b["subject"]["filters"]["classes"]) == 138 and 0 in b["subject"]["filters"]["classes"]
    items = b["data"]["items"]
    assert b["data"]["returned"] == 2 and b["data"]["next_cursor"]
    assert items[0]["id"] == ID1 and items[0]["headline"] == "Amazon to cut 1,000 jobs"
    assert items[0]["events"] == [{"event_type": "layoffs", "domain": "amazon.com", "role": "primary"}]
    assert items[1]["events"] == [{"event_type": "ipo", "domain": "coinbase.com", "role": "primary"}]
    assert b["data"]["with_events"] == 2
    assert b["window"]["until"] == "2026-08-24" and b["window"]["freshness"].startswith("volume thins")
    for h in ("X-RateLimit-Limit", "X-RateLimit-Remaining", "X-Quota-Requests-Remaining",
              "X-Quota-Exports-Remaining", "X-Plan"):
        assert h in r.headers, h
    assert fake_redis.get(f"pna:req:u:{USER_ID}:" + b["meta"]["quota"]["month"]) == "1"
    # the class filter ran with the 138 paths, and the events lookup was one IN query
    assert any("arrayExists(x -> x.1 IN ('/News/Business News/Company News'" in s for s in client.fake.sql)
    assert sum(1 for s in client.fake.sql if "groupUniqArray" in s) == 1


def test_headlines_caller_scope_wins(client):
    r = client.get("/v1/business/headlines", params={"classes": "0"}, headers=H(client))
    b = _env(r)
    assert b["subject"]["scope"]["applied"] == "caller" and b["subject"]["filters"]["classes"] == [0]
    r = client.get("/v1/business/headlines", params={"class_prefix": "/Sports"}, headers=H(client))
    assert _env(r)["subject"]["filters"]["class_prefix"] == "/Sports"


def test_headlines_company_defaults_window_to_linkage_end(client):
    r = client.get("/v1/business/headlines", params={"company": "https://www.Amazon.com/", "limit": 2}, headers=H(client))
    b = _env(r)
    assert b["window"]["until"] == "2026-05-05" and b["window"]["since"] == "2026-02-04"
    assert any("defaulted to end there" in n for n in b["meta"]["notes"])
    assert b["subject"]["filters"]["company"] == "amazon.com" and b["subject"]["filters"]["company_match"] == "domain"
    sql = [s for s in client.fake.sql if f"FROM {ch.TABLE}" in s and "GLOBAL IN" in s]
    assert sql and "endsWith(d, '.amazon.com'), org_domains)" in sql[0]
    r = client.get("/v1/business/headlines", params={"company": "amazon.com", "until": "2026-08-01"}, headers=H(client))
    assert _env(r)["window"]["until"] == "2026-08-01"


def test_headlines_post_body_and_event_type(client):
    r = client.post("/v1/business/headlines", json={"event_type": ["layoffs", "IPO"], "sentiment": ["negative"], "limit": 2},
                    headers=H(client))
    b = _env(r)
    assert r.status_code == 200 and b["subject"]["filters"]["event_type"] == ["layoffs", "ipo"]
    assert b["subject"]["filters"]["sentiment"][0] == "extreme_neg"


def test_headlines_400s(client):
    r = client.get("/v1/business/headlines", params={"event_type": "mergers"}, headers=H(client))
    b = _env(r)
    assert r.status_code == 400 and b["error"]["kind"] == "bad_request" and "mergers" in b["error"]["reason"]
    r = client.get("/v1/business/headlines", params={"sector": "fintech"}, headers=H(client))
    assert r.status_code == 400 and "funding" in r.json()["error"]["reason"]
    r = client.get("/v1/business/headlines", params={"company": "a"}, headers=H(client))
    assert r.status_code == 400
    r = client.get("/v1/business/headlines", params={"priority_min": 12}, headers=H(client))
    assert r.status_code == 400 and "priority_min" in r.json()["error"]["reason"]


def test_headlines_no_data_404(client):
    client.fake.total = 0
    r = client.get("/v1/business/headlines", params={"q": "zzzz qqqq"}, headers=H(client))
    assert r.status_code == 404 and _env(r)["error"]["kind"] == "no_data"


# ── events ───────────────────────────────────────────────────────────────────
def test_events_items_by_type_window_and_cursor(client):
    r = client.get("/v1/business/events", params={"event_type": "layoffs,ipo", "limit": 2}, headers=H(client))
    b = _env(r)
    assert r.status_code == 200 and b["feature"] == "business.events"
    d = b["data"]
    assert d["returned"] == 2 and d["total_estimate"] == 3 and d["by_type"] == {"layoffs": 2, "ipo": 1}
    it = d["items"][0]
    assert it == {"id": ID1, "headline": "Amazon said it will cut 1,000 corporate jobs.", "event_type": "layoffs",
                  "role": "primary", "domain": "amazon.com", "published_at": "2026-05-01T10:00:00"}
    assert "url" not in it and d["resolved"] is False
    assert b["window"] == {"since": "2026-02-04", "until": "2026-05-05", "days": 91, "data_through": "2026-05-05",
                           "freshness": tables.freshness_note("2026-05-05")}
    assert b["subject"]["filters"]["event_type"] == ["layoffs", "ipo"] and "match" not in b["subject"]["filters"]
    sql = [s for s in client.fake.sql if "GROUP BY target_id, domain, event_type, role, news_publish_datetime" in s][0]
    assert "event_type IN ('layoffs','ipo')" in sql and "LIMIT 3" in sql
    cur = d["next_cursor"]
    assert cur
    r2 = client.get("/v1/business/events", params={"event_type": "layoffs,ipo", "limit": 2, "cursor": cur}, headers=H(client))
    b2 = _env(r2)
    assert r2.status_code == 200 and b2["subject"]["filters"]["cursor"] is True
    assert any("(news_publish_datetime, target_id, domain, event_type, role) < (toDateTime('2026-04-30 09:00:00'), "
               f"'{ID2}', 'coinbase.com', 'ipo', 'primary')" in s for s in client.fake.sql)
    r3 = client.get("/v1/business/events", params={"limit": 2, "cursor": cur, "sort": "oldest"}, headers=H(client))
    assert r3.status_code == 400 and "sort" in r3.json()["error"]["reason"]


def test_events_resolve_and_q_and_domain(client):
    r = client.get("/v1/business/events", params={"company": "amazon.com", "resolve": "true", "q": "cut jobs"},
                   headers=H(client))
    b = _env(r)
    it = b["data"]["items"][0]
    assert it["url"] == "https://www.cnbc.com/x" and it["publisher"] == "cnbc.com" and it["title"] == "Amazon to cut 1,000 jobs"
    assert b["data"]["resolved"] is True and b["subject"]["filters"]["resolve"] is True
    sql = [s for s in client.fake.sql if "GROUP BY target_id, domain" in s][0]
    assert "domain = 'amazon.com'" in sql and "match(lowerUTF8(headline), '(^|[^a-z0-9])cut jobs([^a-z0-9]|$)')" in sql
    assert "'2026-02-04'" in sql and "'2026-05-06'" in sql


def test_events_400s(client):
    for params, needle in ((({"event_type": "mergers"}), "mergers"),
                           (({"company": "Amazon"}), "DOMAIN"),
                           (({"sort": "priority"}), "sort"),
                           (({"sentiment": "negative"}), "sentiment"),
                           (({"min_amount_usd": 5}), "funding"),
                           (({"country": "india"}), "country"),
                           (({"cursor": "garbage"}), "cursor")):
        r = client.get("/v1/business/events", params=params, headers=H(client))
        b = _env(r)
        assert r.status_code == 400 and b["error"]["kind"] == "bad_request" and needle in b["error"]["reason"], params


def test_events_no_data_404(client):
    client.fake.event_rows = []
    r = client.get("/v1/business/events", params={"event_type": "fda_approval"}, headers=H(client))
    assert r.status_code == 404 and _env(r)["error"]["kind"] == "no_data"


# ── funding ──────────────────────────────────────────────────────────────────
def test_funding_items_totals_and_normalised_subject(client):
    r = client.get("/v1/business/funding", params={"min_amount_usd": 50000000, "round_type": "Series-B",
                                                  "sector": "Space Industry", "limit": 2}, headers=H(client))
    b = _env(r)
    assert r.status_code == 200 and b["feature"] == "business.funding"
    d = b["data"]
    assert d["returned"] == 2 and d["total_estimate"] == 3 and d["next_cursor"]
    it = d["items"][0]
    assert it["company_name"] == "avoca" and it["domain"] == "avoca.com" and it["amount_usd"] == 125000000.0
    assert it["valuation_usd"] is None and it["id"] == f"{12345678901234567:016x}"
    assert it["investors"] == [{"name": "Sequoia Capital", "domain": "sequoiacap.com", "amount": None},
                               {"name": "Angel One", "domain": None, "amount": 5000000.0}]
    assert it["article_ids"] == [ID1] and it["published_at"] == "2026-05-04T21:30:02" and it["coverage_count"] == 1
    assert d["totals"]["deals"] == 3 and d["totals"]["deals_with_amount"] == 2
    assert d["totals"]["sum_amount_usd"] == 190000000.0 and d["totals"]["median_amount_usd"] == 95000000.0
    f = b["subject"]["filters"]
    assert f["round_type"] == ["series b"] and f["sector"] == ["space"] and f["min_amount_usd"] == 50000000.0
    assert "match" not in f
    assert b["window"]["data_through"] == "2026-05-05"
    sql = [s for s in client.fake.sql if tables.FUNDING_TABLE in s and "ORDER BY" in s][0]
    assert f"{FUNDING_AMT} >= 50000000.0" in sql
    assert "(^|[^a-z0-9])series b([^a-z0-9]|$)" in sql and "(^|[^a-z0-9])space([^a-z0-9]|$)" in sql and "ILIKE" not in sql


def test_funding_sort_amount_cursor_country_investor(client):
    r = client.get("/v1/business/funding", params={"sort": "amount", "country": "USA", "investor": "Sequoia", "limit": 2},
                   headers=H(client))
    b = _env(r)
    assert r.status_code == 200 and b["subject"]["filters"]["country"] == "usa"
    sql = [s for s in client.fake.sql if tables.FUNDING_TABLE in s and "ORDER BY" in s][0]
    assert "IN ('united states','usa','us'" in sql and "position(lowerUTF8(i.1), 'sequoia') > 0" in sql
    assert f"ORDER BY {FUNDING_AMT} DESC" in sql
    cur = b["data"]["next_cursor"]
    r2 = client.get("/v1/business/funding", params={"sort": "amount", "limit": 2, "cursor": cur}, headers=H(client))
    assert r2.status_code == 200
    assert any("< (65000000.0, toDateTime('2026-05-04 20:28:50'), toUInt64('7654321'))" in s for s in client.fake.sql)
    r3 = client.get("/v1/business/funding", params={"sort": "newest", "limit": 2, "cursor": cur}, headers=H(client))
    assert r3.status_code == 400


def test_funding_400s(client):
    r = client.get("/v1/business/funding", params={"min_amount_usd": "abc"}, headers=H(client))
    b = _env(r)
    assert r.status_code == 400 and b["error"]["kind"] == "bad_request" and "min_amount_usd" in b["error"]["reason"]
    for params in ({"min_amount_usd": -1}, {"sort": "priority"}, {"event_type": "ipo"}, {"classes": "0"},
                   {"investor": "a"}, {"resolve": "true"}):
        r = client.get("/v1/business/funding", params=params, headers=H(client))
        assert r.status_code == 400, params


def test_funding_no_data_404(client):
    client.fake.funding_rows = []
    r = client.get("/v1/business/funding", params={"sector": "zzz"}, headers=H(client))
    assert r.status_code == 404 and _env(r)["error"]["kind"] == "no_data"


# ── one company ──────────────────────────────────────────────────────────────
def test_company_news_three_blocks(client):
    r = client.get("/v1/business/companies/Amazon.com/news", params={"limit": 2}, headers=H(client))
    b = _env(r)
    assert r.status_code == 200 and b["feature"] == "business.company_news"
    d = b["data"]
    assert d["domain"] == "amazon.com" and set(d) >= {"headlines", "events", "funding", "counts"}
    assert d["headlines"]["returned"] == 2 and d["headlines"]["window"]["until"] == "2026-05-05"
    assert d["headlines"]["items"][0]["events"]
    assert d["events"]["returned"] == 2 and d["events"]["by_type"] and d["events"]["window"]["data_through"] == "2026-05-05"
    assert d["funding"]["returned"] == 2 and d["funding"]["totals"]["deals"] == 3
    assert d["counts"] == {"headlines": 2, "events": 3, "funding": 3}
    assert b["window"]["linkage_data_through"] == "2026-05-05" and b["subject"]["domain"] == "amazon.com"
    assert b["subject"]["scope"]["applied"] == "default"
    sqls = [s for s in client.fake.sql if tables.EVENTS_TABLE in s and "GROUP BY target_id, domain" in s]
    assert sqls and "domain = 'amazon.com'" in sqls[0]
    assert any("lowerUTF8(coalesce(domain, '')) = 'amazon.com'" in s for s in client.fake.sql)


def test_company_news_empty_blocks_and_404(client):
    client.fake.funding_rows = []
    r = client.get("/v1/business/companies/amazon.com/news", headers=H(client))
    b = _env(r)
    assert r.status_code == 200 and b["data"]["funding"]["returned"] == 0 and b["data"]["funding"]["empty_reason"]
    client.fake.total, client.fake.event_rows = 0, []
    r = client.get("/v1/business/companies/amazon.com/news", headers=H(client))
    assert r.status_code == 404 and _env(r)["error"]["kind"] == "no_data"
    r = client.get("/v1/business/companies/Amazon/news", headers=H(client))
    assert r.status_code == 400 and "DOMAIN" in r.json()["error"]["reason"]


# ── scoped lenses ────────────────────────────────────────────────────────────
def test_themes_sentiment_trends_are_business_features(client):
    r = client.get("/v1/business/themes", params={"q": "tariff"}, headers=H(client))
    b = _env(r)
    assert r.status_code == 200 and b["feature"] == "business.themes" and b["subject"]["scope"]["applied"] == "default"
    assert b["data"]["items"][0]["theme"].startswith("layoffs") and len(b["subject"]["filters"]["classes"]) == 138
    r = client.get("/v1/business/sentiment", params={"granularity": "monthly", "company": "amazon.com"}, headers=H(client))
    b = _env(r)
    assert b["feature"] == "business.sentiment" and b["window"]["granularity"] == "monthly"
    assert b["window"]["until"] == "2026-05-05" and len(b["data"]["labels"]) == 9
    r = client.post("/v1/business/trends", json={"granularity": "weekly", "event_type": ["layoffs"]}, headers=H(client))
    b = _env(r)
    assert b["feature"] == "business.trends" and b["data"]["total"] == 10 and b["subject"]["filters"]["event_type"] == ["layoffs"]
    r = client.get("/v1/business/trends", params={"granularity": "hourly"}, headers=H(client))
    assert r.status_code == 400


# ── the general routes served here ───────────────────────────────────────────
def test_shared_general_routes_unmetered(client, fake_redis):
    for p, feat in (("/v1/me", "api.me"), ("/v1/status", "api.status"), ("/v1/vocabulary", "news.vocabulary"),
                    ("/v1/classes/0", "news.class")):
        r = client.get(p, headers=H(client))
        assert r.status_code == 200 and _env(r)["feature"] == feat, p
    assert fake_redis.keys("pna:req:*") == []
    r = client.get("/v1/classes", params={"q": "venture"}, headers=H(client))
    assert any(i["code"] == 55 for i in r.json()["data"]["items"])
    r = client.get("/v1/headlines", headers=H(client))                  # the general list endpoints are NOT here
    assert r.status_code == 404


def _strip(b: dict) -> dict:
    b = json.loads(json.dumps(b))
    b.get("meta", {}).pop("seconds", None)
    b.get("meta", {}).pop("request_seconds", None)
    return b


def test_export_and_article_identical_to_general_app(client, general_client):
    body = {"class_prefix": "/Finance", "limit": 2, "format": "json"}
    r1 = client.post("/v1/export", json=body, headers=H(client))
    r2 = general_client.post("/v1/export", json=body, headers=H(general_client))
    assert r1.status_code == r2.status_code == 200
    b1, b2 = _strip(r1.json()), _strip(r2.json())
    b1["meta"]["quota"] = b2["meta"]["quota"] = {}      # both apps share one fake Redis: counters differ by call order
    assert b1 == b2 and b1["feature"] == "news.export" and b1["data"]["items"][0]["body"].startswith("full body")
    assert r1.headers["X-Plan"] == r2.headers["X-Plan"]
    for fmt in ("ndjson", "csv"):
        a = client.post("/v1/export", json={**body, "format": fmt}, headers=H(client))
        g = general_client.post("/v1/export", json={**body, "format": fmt}, headers=H(general_client))
        assert a.status_code == g.status_code == 200 and a.headers["content-type"] == g.headers["content-type"]
        assert a.headers["X-Export-Delivered"] == g.headers["X-Export-Delivered"] == "2"
        if fmt == "csv":
            assert a.text == g.text
        else:
            assert a.text.split("\n")[1:] == g.text.split("\n")[1:]
    r1 = client.get(f"/v1/articles/{ID1}", headers=H(client))
    r2 = general_client.get(f"/v1/articles/{ID1}", headers=H(general_client))
    b1, b2 = _strip(r1.json()), _strip(r2.json())
    for b in (b1, b2):
        b["meta"]["quota"] = {}
    assert r1.status_code == 200 and b1 == b2 and b1["data"]["article"]["body_chars"] == 500
    r = client.get("/v1/articles/not-an-id", headers=H(client))
    assert r.status_code == 400
    r = client.post("/v1/export", json={"format": "xml"}, headers=H(client))
    assert r.status_code == 400


def test_openapi_lists_business_and_shared_paths(client):
    s = client.get("/v1/openapi.json").json()
    for p in ("/v1/business/headlines", "/v1/business/events", "/v1/business/funding",
              "/v1/business/companies/{domain}/news", "/v1/export", "/v1/articles/{article_id}", "/v1/me"):
        assert p in s["paths"], p
    assert "/v1/headlines" not in s["paths"]
    assert "ApiKeyAuth" in s["components"]["securitySchemes"]
    assert s["info"]["x-business-scope"] == ["/News/Business News", "/Business & Industrial", "/Finance"]
    assert client.get("/docs").status_code == 200


def test_rate_limit_and_quota_shared_with_general_chain(client, stub_auth):
    stub_auth.plan_cfg["requests_per_month"] = 1
    assert client.get("/v1/business/events", headers=H(client)).status_code == 200
    r = client.get("/v1/business/funding", headers=H(client))
    b = _env(r)
    assert r.status_code == 402 and b["error"]["kind"] == "quota_exceeded"
    assert b["error"]["upgrade_url"].startswith("https://fliarbi.com/")
    assert client.get("/v1/me", headers=H(client)).status_code == 200
    stub_auth.plan_cfg["rate_per_minute"] = 2
    client.get("/v1/me", headers=H(client))
    r = client.get("/v1/me", headers=H(client))
    assert r.status_code == 429 and "Retry-After" in r.headers
