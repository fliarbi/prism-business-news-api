"""tables — the two business tables, their vocabularies and their own freshness.

Both live on the ClickHouse initiator (plain MergeTree / refreshable MV, not
Distributed), so a read either answers or fails — there is no partial-shard
case — but the news table IS distributed, and a subquery against these tables
from inside a news query must be `GLOBAL IN` (a plain IN is evaluated on every
shard, where the business database does not exist: UNKNOWN_TABLE).

Measured 2026-09-13:

  company_events_flat   4,199,638 rows = 3,403,910 distinct (article, company,
                        type, role) — 19% are repeated sentences from one
                        article and are grouped away. 374,163 domains,
                        2,650,570 articles. news_publish_datetime 2010-01-01 →
                        2026-05-05 (84 rows carry garbage future dates up to
                        2074 and are excluded by every window). ~31–49k rows a
                        month through 2026-04, 4,244 for the partial May.
                        Refreshed daily (REFRESH EVERY 1 DAY) from 19 per-type
                        extraction tables. `headline` is the extracted source
                        SENTENCE, not the article title.
  funding_rounds        365,555 deduplicated deals, 2010-01-02 → 2026-05-05,
                        ~3.2–3.9k a month through 2026-04. amount_usd is a
                        fixed-rate conversion done in the view (USD 1, EUR 1.08,
                        GBP 1.27, INR 0.012, …); it is 0, never NULL, when no
                        amount was extracted (320,125 deals, 88%, carry one).
                        domain 83% filled, sector 82%, country 79%, investors
                        82%. investor is Array(Tuple(name, domain|NULL, amount)).
  join                  of 200 sampled event target_ids, 137 (69%) have a row
                        in the news table; funding source_target_ids 145/200
                        (73%). Event news_publish_datetime equals the article
                        `datetime` wherever both exist (75/75).
"""
from __future__ import annotations

import threading
import time

from prism_news_api import ch, config
from prism_news_api.envelope import ApiError

EVENTS_TABLE = config._env("PRISM_EVENTS_TABLE", "business.company_events")
FUNDING_TABLE = config._env("PRISM_FUNDING_TABLE", "business.funding_rounds")

EVENT_TYPES: tuple[str, ...] = (
    "earnings", "key_people", "ma", "company_announcement", "contracts",
    "funding_rounds", "asset_acquisition", "lawsuit", "new_product", "regulatory",
    "capital_infusion", "ipo", "job_creation", "layoffs", "board_updates",
    "funds_raising", "buyback", "incorporation", "fda_approval",
)
ROLES: tuple[str, ...] = ("primary", "acquirer", "target", "contractor", "client",
                          "seller", "defendant", "plaintiff")
EVENT_SORTS: tuple[str, ...] = ("newest", "oldest")
FUNDING_SORTS: tuple[str, ...] = ("newest", "oldest", "amount")

# Amount guard. The extracted amount_usd is unusable at the top end: unit errors
# (a $3.9M placement stored as $3.9T), valuations stored as round sizes, and
# local currencies (KES, PKR, COP, UGX ...) passed through unconverted. Measured
# 2026-10-13: 227 deals above $50bn, max $1.6e15. A usable amount is finite,
# positive, at most MAX_PLAUSIBLE_USD, and either USD or actually converted.
# Flagged amounts still count as deals and are reported as excluded.
MAX_PLAUSIBLE_USD = 25_000_000_000
_AMT = "coalesce(amount_usd, 0.)"
REPORTED_AMOUNT = f"isFinite({_AMT}) AND {_AMT} > 0"
UNCONVERTED_AMOUNT = (f"(coalesce(amount, 0.) = {_AMT} AND "
                      "upperUTF8(trimBoth(coalesce(currency, ''))) NOT IN ('', 'USD', 'US$', '$'))")
VALID_AMOUNT = (f"({REPORTED_AMOUNT} AND {_AMT} <= {MAX_PLAUSIBLE_USD} "
                f"AND NOT {UNCONVERTED_AMOUNT})")
USABLE_AMOUNT = f"if({VALID_AMOUNT}, {_AMT}, 0.)"

# Sanity floors: an empty or near-empty table after a botched refresh is a
# failure, not "no news". Measured 4,199,638 / 365,555 on 2026-09-13.
EVENTS_MIN_ROWS = 1_000_000
FUNDING_MIN_ROWS = 100_000

_LOCK = threading.Lock()
_CACHE: dict[str, tuple[object, float]] = {}


def _cached(name: str, fn, ttl: int):
    with _LOCK:
        hit = _CACHE.get(name)
        if hit and time.time() - hit[1] < ttl:
            return hit[0]
    val = fn()
    with _LOCK:
        _CACHE[name] = (val, time.time())
    return val


def invalidate() -> None:
    with _LOCK:
        _CACHE.clear()


def _dt(table: str) -> str:
    r = ch.one(f"SELECT toString(toDate(max(news_publish_datetime))) FROM {table} "
               f"WHERE news_publish_datetime <= now()", timeout=20)
    if not r or not r[0] or str(r[0]).startswith("1970"):
        raise ApiError("coverage_unavailable", "could not determine the latest available business data date")
    return str(r[0])


def events_data_through() -> str:
    """max(news_publish_datetime) that is not in the future, cached hourly."""
    return _cached("events_dt", lambda: _dt(EVENTS_TABLE), config.DATA_THROUGH_TTL)


def funding_data_through() -> str:
    return _cached("funding_dt", lambda: _dt(FUNDING_TABLE), config.DATA_THROUGH_TTL)


def linkage_data_through() -> str:
    """The last day on which articles can be linked to companies at all: the
    events table ends here and the news table's organisation entities
    (Organization / pri_organization / org_domains) stop being filled at the
    same point (25–30% fill through 2026-04, 2.6% for May, 0 after)."""
    ev = events_data_through()
    news = ch.data_through()
    return min(ev, news)


def _count(table: str) -> int:
    return ch.scalar_int(f"SELECT count() FROM {table}", timeout=20)


def require_table(which: str) -> dict:
    """Reachability + row floor for events/funding, cached hourly. Below the
    floor -> 503 coverage_unavailable, never a thin answer."""
    table, floor = ((EVENTS_TABLE, EVENTS_MIN_ROWS) if which == "events"
                    else (FUNDING_TABLE, FUNDING_MIN_ROWS))
    try:
        n = _cached(f"rows:{which}", lambda: _count(table), config.COVERAGE_TTL)
    except ch.CHError as e:
        raise ch.as_api_error(e)
    if n < floor:
        with _LOCK:
            _CACHE.pop(f"rows:{which}", None)
        raise ApiError("coverage_unavailable",
                       f"{which} data is temporarily below the required completeness level; "
                       "please retry later")
    return {"table": table, "rows": n, "floor": floor}


def freshness_note(dt: str) -> str:
    return (f"this business dataset is available through {dt}; company events, "
            "funding and company-linked news may have different latest available dates")


def linkage_note(dt: str) -> str:
    return (f"company-linked news is available through {dt}; the window was "
            "defaulted to end there — pass `until` to override")
