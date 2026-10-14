"""Shared fixtures. No network anywhere in tests: Redis, Mongo, ClickHouse, the
article-store ring and the business tables' freshness probes are replaced by
in-memory stubs — the same pattern as prism-news-api/tests/conftest.py."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from prism_news_api import articles, auth, ch, config, quota  # noqa: E402
from prism_news_api.envelope import ApiError  # noqa: E402

from prism_business_api import tables  # noqa: E402


class FakePipeline:
    def __init__(self, r):
        self.r, self.ops = r, []

    def __getattr__(self, name):
        def rec(*a, **k):
            self.ops.append((name, a, k))
            return self
        return rec

    def execute(self):
        return [getattr(self.r, n)(*a, **k) for n, a, k in self.ops]


class FakeRedis:
    def __init__(self):
        self.d: dict = {}
        self.ttl: dict = {}

    def get(self, k):
        return self.d.get(k)

    def set(self, k, v, nx=False, ex=None):
        if nx and k in self.d:
            return None
        self.d[k] = str(v)
        if ex:
            self.ttl[k] = ex
        return True

    def incr(self, k):
        return self.incrby(k, 1)

    def incrby(self, k, n):
        self.d[k] = str(int(self.d.get(k) or 0) + int(n))
        return int(self.d[k])

    def decr(self, k):
        return self.incrby(k, -1)

    def decrby(self, k, n):
        return self.incrby(k, -int(n))

    def expire(self, k, s):
        self.ttl[k] = s
        return True

    def delete(self, *ks):
        return sum(1 for k in ks if self.d.pop(k, None) is not None)

    def keys(self, pattern="*"):
        import fnmatch
        return [k for k in self.d if fnmatch.fnmatch(k, pattern)]

    def ping(self):
        return True

    def pipeline(self):
        return FakePipeline(self)


@pytest.fixture
def fake_redis(monkeypatch):
    r = FakeRedis()
    monkeypatch.setattr(quota, "redis_client", lambda: r)
    return r


@pytest.fixture
def free_cfg():
    return dict(config.plans()["free"])


USER_ID = "64f000000000000000000abc"


@pytest.fixture
def principal(free_cfg):
    return auth.Principal(user_id=USER_ID, key_id="000000000000000000000001",
                          key_prefix="pna_test0000", key_name="t", email="t@example.com",
                          plan="free", plan_cfg=free_cfg, source="free", expired=False,
                          expires=None, account_flag=None, notes=[])


DATA_THROUGH = "2026-08-24"
EVENTS_THROUGH = "2026-05-05"

# ── canned rows ──────────────────────────────────────────────────────────────
ID1, ID2 = "69f881d343843dd771cf50f2", "6a2ec2438e67a2fcb3c9a517"
ROW = [ID1, "2026-05-01 10:00:00", 7, ["very_neg", 0.51],
       [["/News/Business News/Company News", 0.44]], [["layoffs and workforce reductions", 0.96]],
       None, ["amazon"], [], "amazon said it will cut 1,000 corporate jobs"]
ROW2 = [ID2, "2026-04-30 09:00:00", 5, ["slight_pos", 0.56], [], [], None, [], [],
        "coinbase files for a secondary listing"]
REC = {ID1: {"id": ID1, "headline": "Amazon to cut 1,000 jobs", "url": "https://www.cnbc.com/x",
             "publisher": "cnbc.com", "body": "full body " * 50, "body_chars": 500, "authors": ["A"],
             "top_image": None, "meta_description": "d", "publish_date": None, "language": "en"},
       ID2: {"id": ID2, "headline": "Coinbase listing", "url": "https://m/x", "publisher": "minichart.com.sg",
             "body": "b" * 900, "body_chars": 900, "authors": [], "top_image": None,
             "meta_description": None, "publish_date": None, "language": "en"}}
EVENT_ROWS = [
    [ID1, "amazon.com", "layoffs", "primary", "2026-05-01 10:00:00", "Amazon said it will cut 1,000 corporate jobs."],
    [ID2, "coinbase.com", "ipo", "primary", "2026-04-30 09:00:00", "Coinbase filed for a secondary listing."],
    ["6a2ec2438e67a2fcb3c9a518", "nissan.co.jp", "layoffs", "primary", "2026-04-29 08:00:00", "Nissan will cut 900 jobs in Europe."],
]
FUNDING_ROWS = [
    ["avoca", "avoca.com", "Series B", 125000000.0, 0.0, "USD", 125000000.0, 0.0,
     [["Sequoia Capital", "sequoiacap.com", 0], ["Angel One", None, 5000000]], "AI customer support agents",
     "USA", "New York", "hiring", "Avoca raised $125M in Series B funding led by Sequoia.",
     "2026-05-04 21:30:02", 1, [ID1], ID1, 12345678901234567],
    ["panthalassa", "panthalassa.org", "Series-B", 65000000.0, 0.0, "USD", 65000000.0, 0.0,
     [], "space", "United States", "Portland", None, "Panthalassa closed a $65M Series B.",
     "2026-05-04 20:28:50", 2, [ID2, ID1], ID2, 7654321],
    ["juliahub", None, None, 0.0, 0.0, None, 0.0, 0.0, [], None, None, None, None, "JuliaHub raised funding.",
     "2026-05-01 07:04:52", 1, [ID2], ID2, 99],
]


class FakeCH:
    """Answers by table and SQL shape; records every SQL so tests can assert on it."""

    def __init__(self):
        self.sql = []
        self.total = 2
        self.event_rows = list(EVENT_ROWS)
        self.funding_rows = list(FUNDING_ROWS)

    def _page(self, rows, sql):
        # the feature asks for limit + 1 rows: hand back that many when we have them
        import re
        m = re.search(r"LIMIT (\d+)$", sql.strip())
        n = int(m.group(1)) if m else len(rows)
        return rows[:n]

    def rows(self, sql, timeout=None):
        self.sql.append(sql)
        s = " ".join(sql.split())
        if "GROUP BY period, event_type" in s:
            from datetime import date
            from prism_news_api.features._common import _bucket_start
            g = "monthly" if "toStartOfMonth" in s else "weekly" if "toMonday" in s else "daily"
            out = {}
            for row in self.event_rows:
                key = (_bucket_start(date.fromisoformat(row[4][:10]), g).isoformat(), row[2])
                out.setdefault(key, set()).add(tuple(row[:5]))
            return [[*key, len(values)] for key, values in sorted(out.items())]
        if "AS period" in s and "quantileExactInclusive(0.5)" in s:
            from datetime import date
            from prism_news_api.features._common import _bucket_start
            g = "monthly" if "toStartOfMonth" in s else "weekly" if "toMonday" in s else "daily"
            out = {}
            for row in self.funding_rows:
                key = _bucket_start(date.fromisoformat(row[14][:10]), g).isoformat()
                out.setdefault(key, []).append(row)
            return [[key, *self.amounts(rows)] for key, rows in sorted(out.items())]
        if tables.EVENTS_TABLE in s and f"FROM {ch.TABLE}" not in s:
            if "groupUniqArray" in s:
                return [[r[0], [[r[2], r[1], r[3]]]] for r in self.event_rows if r[0] in s]
            if "GROUP BY event_type" in s:
                out: dict = {}
                for r in self.event_rows:
                    out[r[2]] = out.get(r[2], 0) + 1
                return [[k, v] for k, v in sorted(out.items(), key=lambda kv: -kv[1])]
            return self._page(self.event_rows, s)
        if tables.FUNDING_TABLE in s:
            return self._page([r[:19] + [self.usable(r)] for r in self.funding_rows], s)
        if "GROUP BY label HAVING" in s:                              # themes
            return [["layoffs and workforce reductions", 40, 20], ["tiny", 3, 0]]
        if "arrayJoin(" in s and "GROUP BY label" in s:                # baselines
            if "subcats" in s:
                return [["layoffs and workforce reductions", 10], ["professional league updates", 900]]
            if "sentiments" in s:
                return [["very_neg", 300], ["slight_pos", 500], ["none", 100]]
            if "priorities" in s:
                return [[7, 700], [4, 400]]
            return [["/News/Business News/Company News", 1234]]
        if "GROUP BY period, label" in s:
            return [["2026-04-27", "very_neg", 3], ["2026-04-27", "slight_pos", 1]]
        if "AS band" in s:
            return [[7, 5], [4, 5]]
        if "GROUP BY period" in s:
            return [["2026-04-27", 10, 4, 3, 2]]
        if "ORDER BY" in s and "LIMIT" in s and "target_id" in s:      # headline rows
            return self._page([ROW, ROW2, ROW2], s) if self.total else []
        return []

    def one(self, sql, timeout=None):
        self.sql.append(sql)
        s = " ".join(sql.split())
        if s.startswith("SELECT uniqExact((target_id, domain, event_type, role, news_publish_datetime))"):
            return [len({tuple(r[:5]) for r in self.event_rows}), len({r[0] for r in self.event_rows}),
                    len({r[1] for r in self.event_rows if r[1]})]
        if s.startswith("SELECT uniqExact(target_id), uniqExactIf"):
            return [self.total, self.total, self.total, 0]
        if tables.FUNDING_TABLE in s and "quantileExactInclusive(0.5)" in s:
            return self.amounts(self.funding_rows)
        if "countIf(" in s:
            if "'2026-07-26'" in s:                                    # the 30-day baseline window
                return [2000, 1200]
            return [self.total, self.total]
        if "target_id =" in s:
            return ROW if ID1 in s else None
        return [self.total]

    @staticmethod
    def usable(r):
        """Mirror of tables.VALID_AMOUNT for one funding row."""
        import math
        a = r[3]
        if a is None or not math.isfinite(a) or a <= 0 or a > tables.MAX_PLAUSIBLE_USD:
            return 0.
        if (r[6] or 0.) == a and (r[5] or "").strip().upper() not in ("", "USD", "US$", "$"):
            return 0.
        return a

    @classmethod
    def amounts(cls, rows):
        import math
        import statistics
        valid = [r for r in rows if cls.usable(r)]
        reported = [r for r in rows if r[3] is not None and math.isfinite(r[3]) and r[3] > 0]
        uniq = list({((r[1] or r[0] or "").lower(), r[3]): r[3] for r in valid}.values())
        return [len(rows), len(valid), sum(uniq), statistics.median(uniq) if uniq else None,
                max(uniq) if uniq else None, len(reported) - len(valid)]

    def scalar_int(self, sql, timeout=None):
        self.sql.append(sql)
        return self.total


@pytest.fixture
def fake_ch(monkeypatch):
    fake = FakeCH()
    monkeypatch.setattr(ch, "rows", fake.rows)
    monkeypatch.setattr(ch, "one", fake.one)
    monkeypatch.setattr(ch, "scalar_int", fake.scalar_int)
    monkeypatch.setattr(ch, "coverage", lambda force=False: {"rows": 255_586_690, "expected": 255_586_690,
                                                             "pct": 100.0, "partial": False, "checked_at": 0})
    monkeypatch.setattr(ch, "data_through", lambda force=False: DATA_THROUGH)
    monkeypatch.setattr(tables, "events_data_through", lambda: EVENTS_THROUGH)
    monkeypatch.setattr(tables, "funding_data_through", lambda: EVENTS_THROUGH)
    monkeypatch.setattr(tables, "require_table", lambda which: {"table": which, "rows": 4_199_638, "floor": 1})
    monkeypatch.setattr(articles, "resolve", lambda ids, full=False: ({i: REC[i] for i in ids if i in REC}, []))
    monkeypatch.setattr(articles, "health", lambda all_nodes=False: {"available": True, "ring_nodes": 31})
    monkeypatch.setattr(quota, "record_daily", lambda *a, **k: None)
    return fake


KEY = "pna_" + "ab" * 20


@pytest.fixture
def stub_auth(monkeypatch, principal):
    def fake_auth(headers):
        k = headers.get("x-api-key") or (headers.get("authorization") or "")[7:]
        if not k:
            raise ApiError("unauthenticated", "no key")
        if k != KEY:
            raise ApiError("invalid_key", "unknown API key")
        return principal
    monkeypatch.setattr(auth, "authenticate", fake_auth)
    return principal


@pytest.fixture
def client(fake_redis, fake_ch, stub_auth):
    from fastapi.testclient import TestClient
    from prism_business_api.main import app
    c = TestClient(app, raise_server_exceptions=False)
    c.fake, c.key = fake_ch, KEY
    return c


@pytest.fixture
def general_client(fake_redis, fake_ch, stub_auth):
    from fastapi.testclient import TestClient
    from prism_news_api.main import app
    c = TestClient(app, raise_server_exceptions=False)
    c.fake, c.key = fake_ch, KEY
    return c


def H(c):
    return {"X-API-Key": c.key}
