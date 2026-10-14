"""Counts, filter propagation, bounded windows and public business contracts."""
from __future__ import annotations

import json
import pytest

from prism_news_api import ch, public
from prism_news_api.envelope import ApiError

from prism_business_api import __version__, tables
from prism_business_api.features import aggregates as a
from prism_business_api.filters import BusinessFilters
from tests.conftest import H

PATHS = ("overview", "event-trends", "funding/summary")


@pytest.mark.parametrize("path", PATHS)
def test_get_post_parity_and_metering(client, path):
    params = {"since": "2026-04-01", "until": "2026-05-05"}
    get = client.get(f"/v1/business/{path}", params=params, headers=H(client))
    post = client.post(f"/v1/business/{path}", json=params, headers=H(client))
    assert get.status_code == post.status_code == 200, (get.text, post.text)
    for key in ("feature", "subject", "window", "data"):
        assert get.json()[key] == post.json()[key]
    assert get.headers["X-Plan"] == "free"
    assert "X-Quota-Requests-Remaining" in get.headers
    assert client.get(f"/v1/business/{path}").status_code == 401


def test_overview_measured_populations_and_archive_are_separate(client):
    b = client.get("/v1/business/overview", headers=H(client)).json()
    assert b["data"]["archive"] == public.archive()
    assert b["data"]["archive"]["article_count_display"] == "450M+"
    assert b["data"]["news"]["articles"] == 2
    assert b["data"]["events"]["events"] == 3
    assert b["data"]["funding"]["deals"] == 3
    assert b["data"]["funding"]["sum_amount_usd"] == 190_000_000
    assert b["window"]["until"] == "2026-05-05"
    assert b["window"]["datasets"] == {"news": "2026-08-24", "events": "2026-05-05", "funding": "2026-05-05"}
    assert b["subject"]["scope"]["applied"] == "default"
    assert "SQL" not in json.dumps(b["subject"])
    assert tables.EVENTS_MIN_ROWS == 1_000_000 and tables.FUNDING_MIN_ROWS == 100_000


def test_event_duplicates_zero_periods_and_partial_edges(client):
    client.fake.event_rows.append(client.fake.event_rows[0][:5] + ["A second sentence about the same event."])
    b = client.get("/v1/business/event-trends", params={"since": "2026-04-01", "until": "2026-05-05", "granularity": "monthly"}, headers=H(client)).json()
    assert b["data"]["totals"]["events"] == 3
    assert b["data"]["totals"]["articles"] == 3
    assert b["data"]["by_type"]["layoffs"] == 2
    assert b["data"]["by_type"]["earnings"] == 0
    assert [pt["events"] for pt in b["data"]["points"]] == [2, 1]
    assert [pt["partial_period"] for pt in b["data"]["points"]] == [False, True]
    assert sum(b["data"]["by_type"].values()) == b["data"]["totals"]["events"]
    daily = client.get("/v1/business/event-trends", params={"since": "2026-04-01", "until": "2026-05-05", "granularity": "daily"}, headers=H(client)).json()
    assert len(daily["data"]["points"]) == 35 and daily["data"]["points"][0]["events"] == 0


def test_funding_counts_all_rows_and_ignores_unknown_amounts(client):
    for amount in (None, -10, float("nan"), float("inf")):
        row = client.fake.funding_rows[0].copy()
        row[3] = amount
        client.fake.funding_rows.append(row)
    b = client.get("/v1/business/funding/summary", headers=H(client)).json()
    total = b["data"]["totals"]
    assert total["deals"] == 7 and total["deals_with_amount"] == 2 and total["deals_without_amount"] == 5
    assert total["sum_amount_usd"] == 190_000_000
    assert sum(pt["deals"] for pt in b["data"]["points"]) == 7
    assert "fixed conversion rates" in total["note"] and "Each matched deal record counts once" in total["note"]
    assert any("arraySum(" in sql and "isFinite" in sql and "<= 25000000000" in sql for sql in client.fake.sql)


@pytest.mark.parametrize("amounts", [[], [0, None, -1, float("nan")]])
def test_unknown_and_empty_funding_amount_statistics_are_null(client, amounts):
    row = client.fake.funding_rows[0]
    client.fake.funding_rows = []
    for amount in amounts:
        item = row.copy()
        item[3] = amount
        client.fake.funding_rows.append(item)
    response = client.get("/v1/business/funding/summary", headers=H(client))
    assert response.status_code == 200
    total = response.json()["data"]["totals"]
    assert total["deals"] == len(amounts) and total["deals_with_amount"] == 0
    assert all(total[k] is None for k in ("sum_amount_usd", "median_amount_usd", "largest_amount_usd"))


def test_full_funding_filters_are_propagated_and_membership_does_not_multiply_deals(client):
    params = {"q": "funding", "match": "focused", "company": "avoca.com", "country": "USA", "sector": ["Space Industry"],
              "round_type": ["Series-B"], "min_amount_usd": 10, "investor": "Sequoia", "event_type": ["funding_rounds"],
              "sentiment": ["positive"], "classes": [0], "themes": ["business"], "priority_min": 3, "priority_max": 9,
              "since": "2026-04-01", "until": "2026-05-05"}
    r = client.post("/v1/business/funding/summary", json=params, headers=H(client))
    assert r.status_code == 200, r.text
    sql = next(s for s in client.fake.sql if s.startswith("SELECT count(), countIf((isFinite"))
    for fragment in ("'funding'", "'avoca.com'", "'united states','usa','us'", "space([^a-z0-9]|$)",
                     "series b([^a-z0-9]|$)", "amount_usd >= 10.0", "'sequoia'", "'funding_rounds'",
                     "'slight_pos'", "classification", "subcats", ">= 3", "<= 9", "'2026-04-01'", "'2026-05-06'"):
        assert fragment in sql, fragment
    assert "arrayExists(source_id -> source_id GLOBAL IN" in sql and " JOIN " not in sql
    assert "LIMIT" not in sql
    assert "records without a matching article are excluded" in " ".join(r.json()["meta"]["notes"])


def test_overview_funding_filters_also_constrain_news_and_events(client):
    r = client.get("/v1/business/overview", params={"sector": "space", "class_prefix": "/Finance"}, headers=H(client))
    assert r.status_code == 200, r.text
    assert r.json()["subject"]["scope"]["applied"] == "caller"
    assert sum("SELECT arrayJoin(source_target_ids)" in sql for sql in client.fake.sql) == 2


def test_window_clamps_history_and_duration_before_queries(client, stub_auth):
    stub_auth.plan_cfg["history_days"] = None
    r = client.get("/v1/business/funding/summary", params={"since": "2010-01-01", "until": "2099-01-01"}, headers=H(client))
    assert r.status_code == 200, r.text
    b = r.json()
    assert b["window"]["days"] == 366 and b["window"]["until"] == "2026-05-05"
    assert all("'2010-01-01'" not in sql for sql in client.fake.sql)
    stub_auth.plan_cfg["history_days"] = 30
    r = client.get("/v1/business/funding/summary", params={"since": "2010-01-01"}, headers=H(client))
    assert r.json()["window"]["days"] == 31
    r = client.get("/v1/business/funding/summary", params={"until": "2025-01-01"}, headers=H(client))
    assert r.status_code == 400 and "history" in r.json()["error"]["reason"]


@pytest.mark.parametrize("path", PATHS)
@pytest.mark.parametrize("params", [{"cursor": "x"}, {"sort": "amount"}, {"limit": 1}, {"resolve": True},
                                    {"since": "bad-date"}, {"match": "tags"}, {"sentiment": "invalid"}, {"company": "a"},
                                    {"themes": "one|two|three|four|five|six"}])
def test_invalid_and_inapplicable_filters_are_explicit_errors(client, path, params):
    for method in ("get", "post"):
        r = getattr(client, method)(f"/v1/business/{path}", **({"params": params} if method == "get" else {"json": params}), headers=H(client))
        assert r.status_code == 400 and r.json()["error"]["kind"] == "bad_request", r.text
    assert client.fake.sql == []


@pytest.mark.parametrize("path", PATHS)
def test_coverage_failures_are_private_and_fail_before_aggregate_queries(client, monkeypatch, path):
    def missing(which):
        raise ApiError("coverage_unavailable", f"{tables.FUNDING_TABLE} unavailable at 10.0.0.5")
    monkeypatch.setattr(tables, "require_table", missing)
    r = client.get(f"/v1/business/{path}", headers=H(client))
    assert r.status_code == 503 and r.json()["error"]["kind"] == "coverage_unavailable"
    assert tables.FUNDING_TABLE not in r.text and "10.0.0.5" not in r.text
    assert client.fake.sql == []


def test_health_liveness_avoids_all_dependencies(client, monkeypatch):
    def fail(*args, **kwargs):
        raise AssertionError("health must not probe dependencies")
    for obj, name in ((ch, "coverage"), (ch, "data_through"), (tables, "events_data_through"), (tables, "funding_data_through")):
        monkeypatch.setattr(obj, name, fail)
    r = client.get("/healthz")
    assert r.status_code == 200 and r.json() == {"ok": True}
    assert client.fake.sql == []


@pytest.mark.parametrize("params", [{}, {"q": "  "}, {"q": "**"}, {"q": "a"}, {"q": "x" * 121},
                                    {"q": "tariff", "limit": 6}, {"q": "tariff", "cursor": "x"}])
def test_theme_directory_requests_rejected(client, params):
    for method in ("get", "post"):
        r = getattr(client, method)("/v1/business/themes", **({"params": params} if method == "get" else {"json": params}), headers=H(client))
        assert r.status_code == 400, r.text
    assert client.fake.sql == []


def test_theme_cap_inherited_and_no_item_themes(client, monkeypatch):
    original = ch.rows
    def rows(sql, **kw):
        if "GROUP BY label HAVING" in sql:
            return [[f"theme {i}", 40, 20] for i in range(12)]
        return original(sql, **kw)
    monkeypatch.setattr(ch, "rows", rows)
    b = client.get("/v1/business/themes", params={"q": "tariff"}, headers=H(client)).json()
    assert len(b["data"]["items"]) == b["data"]["returned"] == 5
    assert all("type" not in item and "origin" not in item for item in b["data"]["items"])
    b = client.get("/v1/business/headlines", headers=H(client)).json()
    assert all("themes" not in item for item in b["data"]["items"])


def test_openapi_relevant_fields_and_public_contract(client):
    s = client.get("/v1/openapi.json").json()
    assert s["info"]["version"] == __version__ == "0.2.0"
    for path in PATHS:
        route = s["paths"][f"/v1/business/{path}"]
        assert {"get", "post"} <= route.keys()
        fields = {p["name"] for p in route["get"]["parameters"]}
        assert {"q", "company", "country", "since", "until", "classes", "sentiment", "themes"} <= fields
        assert not fields.intersection({"cursor", "limit", "sort", "resolve"})
        if path == "event-trends":
            assert "investor" not in fields
    theme = s["paths"]["/v1/business/themes"]["get"]["parameters"]
    assert next(p for p in theme if p["name"] == "q")["required"]
    assert next(p for p in theme if p["name"] == "limit")["schema"]["maximum"] == 5
    assert s["paths"]["/healthz"]["get"]["responses"]["200"]["content"]["application/json"]["schema"]["required"] == ["ok"]
    for path, methods in s["paths"].items():
        if path.startswith("/v1/"):
            for operation in methods.values():
                responses = operation["responses"]
                assert "422" not in responses
                for code in ("400", "401", "402", "404", "429", "500", "502", "503"):
                    assert responses[code]["content"]["application/json"]["schema"] == {"$ref": "#/components/schemas/Envelope"}
    exports = s["paths"]["/v1/export"]["post"]["responses"]["200"]["content"]
    assert exports["application/json"]["schema"] == {"$ref": "#/components/schemas/Envelope"}
    for media in ("text/csv", "application/x-ndjson"):
        assert exports[media]["schema"] == {"type": "string"}
    text = json.dumps(s).lower()
    for private in ("clickhouse", "redis", "mongodb", "country_pri", "subcats", "source_target_ids", "plans.json", "cluster", "article store"):
        assert private not in text, private


def test_guide_serves_packaged_text_without_auth(client, monkeypatch, tmp_path):
    from prism_business_api import main
    # Test loading independently of the documentation agent's concurrent write.
    data = tmp_path / "data"
    data.mkdir()
    (data / "user_guide.md").write_text("# Business user guide\n")
    monkeypatch.setattr(main, "files", lambda package: tmp_path)
    r = client.get("/guide")
    assert r.status_code == 200 and r.text == "# Business user guide\n"
    assert r.headers["content-type"].startswith("text/markdown")


def test_implausible_unconverted_and_duplicate_amounts_stay_out_of_statistics(client):
    base = client.fake.funding_rows[0]
    huge = base.copy(); huge[3] = huge[6] = 3_888_888_000_000.0           # unit error, $3.9T
    local = base.copy(); local[0], local[1] = "kcb", "kcb.co.ke"
    local[3] = local[6] = 2_000_000_000.0; local[5] = "KES"              # never converted
    dup = base.copy(); dup[2] = "Series-B extension"                     # same round, another label
    client.fake.funding_rows += [huge, local, dup]
    total = client.get("/v1/business/funding/summary", params={"since": "2026-04-01", "until": "2026-05-05"},
                       headers=H(client)).json()["data"]["totals"]
    assert total["deals"] == 6 and total["deals_with_amount"] == 3 and total["deals_amount_excluded"] == 2
    assert total["sum_amount_usd"] == 190_000_000 and total["largest_amount_usd"] == 125_000_000
    items = client.get("/v1/business/funding", params={"since": "2026-04-01", "until": "2026-05-05", "sort": "amount"},
                       headers=H(client)).json()["data"]["items"]
    flags = {(i["company_name"], i["amount_flag"]) for i in items if i["amount_flag"]}
    assert flags == {("avoca", "implausible_size"), ("kcb", "unconverted_currency")}
    assert all(i["amount_usd"] is None for i in items if i["amount_flag"])
