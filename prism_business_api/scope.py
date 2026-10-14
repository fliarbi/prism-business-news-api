"""scope — the default business scope and how a caller overrides it.

Business = every GCP content class under the three prefixes below (138 codes
on 2026-09-13: 5 + 93 + 40). Measured monthly volume of that scope in the news
table: 578k (2026-03), 760k (Apr), 537k (May), 140k (Jun), 4.5k (Jul), 1.2k
(Aug) against 3.1M / 3.9M / 2.4M / 514k / 52k / 9k for the whole corpus — it
thins after May 2026 exactly as the corpus does.

If the caller sets `classes` or `class_prefix` THEIR scope is used as-is (they
may be narrowing to one class or deliberately leaving business); otherwise the
138 codes are injected as `classes`. Either way `subject.scope` says which
happened, and `subject.filters.classes` carries the codes that actually ran
so the filter set can be replayed into POST /v1/export unchanged.
"""
from __future__ import annotations

from functools import lru_cache

from prism_news_api import taxonomy
from prism_news_api.filters import Filters

BUSINESS_PREFIXES: tuple[str, ...] = ("/News/Business News", "/Business & Industrial", "/Finance")


@lru_cache(maxsize=1)
def business_codes() -> tuple[int, ...]:
    """The union of every class under the business prefixes, sorted by code."""
    out: set[int] = set()
    for p in BUSINESS_PREFIXES:
        out.update(taxonomy.expand_prefix(p))
    return tuple(sorted(out))


def scope_block(applied: str) -> dict:
    return {"applied": applied,
            "class_prefixes": list(BUSINESS_PREFIXES),
            "class_count": len(business_codes()),
            "note": ("default: articles classified under the business categories; "
                     "pass classes or class_prefix to replace it"
                     if applied == "default" else
                     "caller-supplied classes / class_prefix used instead of the business default")}


def apply_business_scope(f: Filters) -> tuple[Filters, dict]:
    """-> (filters to run, subject.scope). Caller classes / class_prefix win."""
    if (f.classes and f.classes.strip()) or (f.class_prefix and f.class_prefix.strip()):
        return f, scope_block("caller")
    codes = ",".join(str(c) for c in business_codes())
    return f.model_copy(update={"classes": codes}), scope_block("default")
