"""_common — what every business feature does around the general one:
scope injection, the linkage-window default, subject/notes decoration, and
the per-page events lookup."""
from __future__ import annotations

import time

from prism_news_api import ch
from prism_news_api.features import _common as gc

from .. import tables
from ..filters import BusinessFilters
from ..scope import apply_business_scope


def prepare(f: BusinessFilters) -> tuple[BusinessFilters, dict, list[str]]:
    """Business scope (caller classes win) + when the filter set links
    companies and no `until` was given, end the window where linkage ends
    (2026-05-05 on 2026-09-13) instead of at the news data_through — a
    default window past that point is empty by construction, not by news."""
    f2, scope = apply_business_scope(f)
    notes: list[str] = []
    if f.links_companies() and not f.until:
        dt = tables.linkage_data_through()
        f2 = f2.model_copy(update={"until": dt})
        notes.append(tables.linkage_note(dt))
    return f2, scope, notes


def finish(env: dict, f: BusinessFilters, scope: dict, notes=(), feature: str | None = None) -> dict:
    if feature:
        env["feature"] = feature
    subj = env.setdefault("subject", {})
    subj.setdefault("filters", {}).update(f.business_subject())
    subj["scope"] = scope
    meta = env.setdefault("meta", {})
    meta["notes"] = list(dict.fromkeys(list(meta.get("notes") or []) + [n for n in notes if n]))
    return env


def events_for_ids(ids: list[str]) -> dict[str, list[dict]]:
    """target_id -> [{event_type, domain, role}] from the events table, one
    IN query (40 ms for 100 ids; target_id is not in the sort key, the table
    is small)."""
    if not ids:
        return {}
    sql = (f"SELECT target_id, groupUniqArray((event_type, domain, role)) FROM {tables.EVENTS_TABLE} "
           f"WHERE target_id IN {ch.sql_in(ids)} GROUP BY target_id")
    rows = gc.run_ch(lambda: ch.rows(sql))
    out: dict[str, list[dict]] = {}
    for tid, evs in rows:
        items = [{"event_type": e[0], "domain": e[1], "role": e[2]} for e in evs or []]
        items.sort(key=lambda e: (e["event_type"], e["domain"], e["role"]))
        out[str(tid)] = items
    return out


def meta(t0: float, notes=None, **extra) -> dict:
    m = {"seconds": round(time.time() - t0, 3), "coverage": ch.coverage_summary(),
         "notes": [n for n in (notes or []) if n]}
    m.update(extra)
    return m
