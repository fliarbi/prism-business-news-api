"""Opt-in engine checks with inline synthetic data only; no real tables or writes.

PRISM_TEST_READ_ONLY_SQL=1 python3 -m pytest tests/test_aggregate_sql.py
Uses the configured query service to execute SELECT ... FROM values(...).
"""
from __future__ import annotations

import os

import pytest

from prism_news_api import ch
from prism_business_api import tables
from tests.conftest import H

_rows = ch.rows
pytestmark = pytest.mark.skipif(os.environ.get("PRISM_TEST_READ_ONLY_SQL") != "1",
                                reason="opt-in pure SELECT checks against the configured query service")


REAL_TABLES = (ch.TABLE, tables.EVENTS_TABLE, tables.FUNDING_TABLE)


@pytest.fixture
def sql_client(client, monkeypatch):
    # Fixture data is embedded in table functions, never created or inserted.
    news_schema = ("target_id String, datetime DateTime, sentiments Array(Tuple(String,Float64)), "
                   "priorities Array(Tuple(Int32,Float64)), classification Array(Tuple(String,Float64)), "
                   "subcats Array(Tuple(String,Float64)), country_pri Nullable(String), "
                   "Organization Array(String), pri_organization Array(String), Person Array(String), "
                   "org_domains Array(String), tags Array(String), text Nullable(String)")
    news = []
    for aid, day, country in (("a", "01", "india"), ("b", "02", "usa")):
        news.append(f"('{aid}', '2026-05-{day} 12:00:00', [('slight_pos', 0.9)], [(7, 0.9)], "
                    "[('/News/Business News/Company News', 0.9)], [('business', 0.9)], "
                    f"'{country}', ['avoca'], ['avoca'], [], ['avoca.com'], ['funding'], 'Avoca raised funding')")
    news_table = f"values({ch.sql_str(news_schema)}, {', '.join(news)})"
    event_schema = "target_id String, domain String, event_type String, role String, news_publish_datetime DateTime, headline String"
    events = ["('a', 'avoca.com', 'funding_rounds', 'primary', '2026-05-01 12:00:00', 'Avoca raised funding')",
              "('a', 'avoca.com', 'funding_rounds', 'primary', '2026-05-01 12:00:00', 'Repeated event sentence')",
              "('a', 'avoca.com', 'funding_rounds', 'target', '2026-05-01 12:00:00', 'Avoca raised funding')",
              "('b', 'avoca.com', 'ipo', 'primary', '2026-05-02 12:00:00', 'Avoca raised funding')"]
    events_table = f"values({ch.sql_str(event_schema)}, {', '.join(events)})"
    funding_schema = ("news_publish_datetime DateTime, amount_usd Nullable(Float64), source_target_ids Array(String), "
                      "company_name String, domain Nullable(String), round_type Nullable(String), sector Nullable(String), "
                      "country Nullable(String), investor Array(Tuple(String,Nullable(String),Float64)), "
                      "source_sentence Nullable(String), use_of_funds Nullable(String), "
                      "amount Nullable(Float64), currency Nullable(String)")
    deals = []
    for amount, sources, country in (("10.", "['a','b']", "India"), ("20.", "['a']", "USA"),
                                     ("0.", "['b']", "United States"), ("30.", "['unlinked']", "US"),
                                     ("NULL", "['a']", "India"), ("-4.", "['a']", "India"),
                                     ("nan", "['a']", "India"), ("inf", "['a']", "India")):
        deals.append(f"('2026-05-04 12:00:00', {amount}, {sources}, 'avoca', 'avoca.com', 'Series B', 'space', "
                     f"'{country}', [('Sequoia', 'sequoiacap.com', 0.)], 'Avoca raised funding', 'Hiring', {amount}, 'USD')")
    funding_table = f"values({ch.sql_str(funding_schema)}, {', '.join(deals)})"
    monkeypatch.setattr(ch, "TABLE", news_table)
    monkeypatch.setattr(tables, "EVENTS_TABLE", events_table)
    monkeypatch.setattr(tables, "FUNDING_TABLE", funding_table)
    queries = []
    def run(fn, sql, **kw):
        assert sql.startswith("SELECT ")
        assert not any(name in sql for name in REAL_TABLES)
        queries.append(sql)
        return fn(sql, timeout=10)
    monkeypatch.setattr(ch, "rows", lambda sql, **kw: run(_rows, sql, **kw))
    monkeypatch.setattr(ch, "one", lambda sql, **kw: run(_rows, sql, **kw)[0])
    client.queries = queries
    return client


def test_real_sql_counts_deal_rows_with_multiple_source_articles_once(sql_client):
    c = sql_client
    r = c.get("/v1/business/funding/summary", params={"since": "2026-05-01", "until": "2026-05-05"}, headers=H(c))
    assert r.status_code == 200, r.text
    totals = r.json()["data"]["totals"]
    assert (totals["deals"], totals["deals_with_amount"], totals["sum_amount_usd"]) == (8, 3, 60)
    assert totals["deals_without_amount"] == 5
    assert totals["median_amount_usd"] == 20
    r = c.get("/v1/business/funding/summary", params={"classes": "0"}, headers=H(c))
    assert r.status_code == 200, r.text
    totals = r.json()["data"]["totals"]
    assert (totals["deals"], totals["deals_with_amount"], totals["sum_amount_usd"]) == (7, 2, 30)
    assert totals["median_amount_usd"] == 15
    assert next(pt for pt in r.json()["data"]["points"] if pt["deals_with_amount"])["median_amount_usd"] == 15


def test_real_sql_full_filters_and_country_aliases(sql_client):
    c = sql_client
    r = c.post("/v1/business/funding/summary", json={"q": "funding", "match": "focused", "company": "avoca.com",
               "country": "USA", "sector": ["space"], "round_type": ["Series-B"], "min_amount_usd": 1,
               "investor": "Sequoia", "event_type": ["funding_rounds"], "classes": [0], "themes": ["business"],
               "sentiment": ["positive"], "priority_min": 7, "priority_max": 7}, headers=H(c))
    assert r.status_code == 200, r.text
    totals = r.json()["data"]["totals"]
    assert totals["deals"] == 1 and totals["sum_amount_usd"] == 20


def test_real_sql_overview_and_deduplicated_event_timeline(sql_client):
    c = sql_client
    r = c.get("/v1/business/overview", headers=H(c))
    assert r.status_code == 200, r.text
    data = r.json()["data"]
    assert data["news"]["articles"] == 2
    assert data["events"]["events"] == 3 and data["events"]["articles"] == 2 and data["events"]["companies"] == 1
    assert data["funding"]["deals"] == 7 and data["funding"]["sum_amount_usd"] == 30
    assert data["funding"]["median_amount_usd"] == 15
    r = c.get("/v1/business/event-trends", params={"company": "Avoca", "country": "India", "granularity": "daily"}, headers=H(c))
    assert r.status_code == 200, r.text
    data = r.json()["data"]
    assert data["totals"]["events"] == 2
    assert sum(pt["events"] for pt in data["points"]) == 2 and data["by_type"]["funding_rounds"] == 2


def test_real_sql_empty_window_is_not_an_all_time_total(sql_client):
    c = sql_client
    r = c.get("/v1/business/funding/summary", params={"since": "2026-04-01", "until": "2026-04-30"}, headers=H(c))
    assert r.status_code == 200, r.text
    totals = r.json()["data"]["totals"]
    assert totals["deals"] == 0 and totals["sum_amount_usd"] is None
    assert totals["median_amount_usd"] is None and totals["largest_amount_usd"] is None
