"""filters — BusinessFilters: the general ✱ set plus the business lanes.

    company       a DOMAIN (`amazon.com`, `https://www.amazon.com/` is normalised)
                  or a NAME (`Amazon`). Decided by shape, echoed as
                  subject.filters.company_match.
    event_type    csv of the 19 company-event types
    sector, round_type, min_amount_usd, investor     funding only
    resolve       events only: also fetch url/publisher from the article store

How the news-table lanes are built (measured, see tables.py):

  * domain -> `org_domains` holds the SPECIFIC sites the article links
    (`aws.amazon.com`, `amazonpay.in`; `amazon.com` itself almost never), so
    the match is the domain OR any subdomain of it — 5,482 hits for amazon.com
    over Feb–May 2026 against 0 for equality. OR the article is one the events
    table attributes to that domain (`target_id GLOBAL IN (...)`, 413 more).
  * name -> word-bounded, case-insensitive match on the canonical entity
    arrays `Organization` / `pri_organization` (they hold 'amazon web services',
    'tesla, inc.' — substring, never equality) OR the name as one of the
    article's `tags` (100% fill, which is what still answers after 2026-05
    when entity enrichment stops).
  * event_type -> `target_id GLOBAL IN (SELECT target_id FROM events WHERE
    event_type IN (...))`. GLOBAL because the news table is distributed and
    the business database exists only on the initiator. The subquery is bounded to
    the window plus an equal-length period before it (so the previous-period
    comparison in /themes still works) — earnings, the largest type, is 23k
    ids per 90 days and the whole clause costs 0.9 s.
  * Sector labels in the corpus are BARE ('healthcare', not 'healthcare
    industry'): trailing generic descriptors are stripped and the match is
    word-bounded — `ILIKE '%space%'` once turned 'space' into aerospace and
    workspace (175 vs 98 rows in a 90-day window).
"""
from __future__ import annotations

import base64
import json
import re
from datetime import date, timedelta
from typing import Optional

from pydantic import Field, field_validator

from prism_news_api import ch
from prism_news_api.envelope import ApiError
from prism_news_api.filters import Filters, Resolved, q_regex, re2_escape, split_list

from . import tables

CURSOR_VERSION = 1
NAME_MIN, NAME_MAX = 2, 120

# news-only parameters a funding / events query must not silently drop
NEWS_ONLY = ("sentiment", "classes", "class_prefix", "themes", "priority_min", "priority_max", "match")
FUNDING_ONLY = ("sector", "round_type", "min_amount_usd", "investor")

_DOMAIN_RE = re.compile(r"^(?=.{4,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,24}$")
_DT_RE = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$")
_ID_RE = re.compile(r"^[0-9a-fA-F]{24}$")
_K_RE = re.compile(r"^\d{1,20}$")

_SECTOR_TAILS = ("industry", "sector", "market", "space", "vertical", "segment",
                 "business", "companies", "company")
COUNTRY_ALIASES: dict[str, tuple[str, ...]] = {
    # measured labels: India 58,630 · USA 39,276 · United States 36,311 · US 4,002 ·
    # UK 13,846 · United Kingdom 7,336 — the same country under several spellings
    "united states": ("united states", "usa", "us", "u.s.", "u.s.a.", "united states of america"),
    "united kingdom": ("united kingdom", "uk", "u.k.", "great britain", "britain"),
    "united arab emirates": ("united arab emirates", "uae", "u.a.e."),
}


def _bad(reason: str) -> ApiError:
    return ApiError("bad_request", reason)


# ── the model ────────────────────────────────────────────────────────────────
class BusinessFilters(Filters):
    event_type: Optional[str] = Field(None, description="csv of company-event types, such as earnings, layoffs or ipo")
    company: Optional[str] = Field(None, description="a company domain (amazon.com) or name (Amazon)")
    sector: Optional[str] = Field(None, description="funding only: csv of sectors, word-bounded ('fintech', 'space')")
    round_type: Optional[str] = Field(None, description="funding only: csv ('series b', 'seed', 'private placement')")
    min_amount_usd: Optional[float] = Field(None, ge=0, allow_inf_nan=False, description="minimum reported funding amount in USD")
    investor: Optional[str] = Field(None, description="funding only: investor name (substring) or domain")
    resolve: Optional[bool] = Field(False, description="event listings only: add original article URL, publisher and title")

    # NOTE: distinct method names — a validator with the parent's name REPLACES
    # the parent's (pydantic v2), which silently broke list bodies for `sentiment`.
    @field_validator("event_type", "sector", "round_type", mode="before")
    @classmethod
    def _biz_lists_to_csv(cls, v):
        if isinstance(v, (list, tuple)):
            return "|".join(str(x) for x in v)
        return v

    @field_validator("company", "investor", "sector", "round_type", "event_type", mode="before")
    @classmethod
    def _biz_none_if_blank(cls, v):
        if isinstance(v, str) and not v.strip():
            return None
        return v

    # ── the hook the general resolve() calls ─────────────────────────────────
    def extra_where(self, r: Resolved) -> list[str]:
        """News-table fragments for company / event_type. Funding-only
        parameters on a news endpoint are a 400, not a silent no-op."""
        bad = [k for k in FUNDING_ONLY if getattr(self, k) is not None]
        if bad:
            raise _bad(f"{', '.join(f'`{k}`' for k in bad)} apply to /v1/business/funding only; "
                       f"on news endpoints use q, classes, class_prefix or themes")
        parts: list[str] = []
        types = self.event_types()
        kind, value = self.company_parts()
        lo, hi = _linkage_bounds(r)
        if kind == "name":
            parts.append(name_lane_sql(value))
        if types or kind == "domain":
            sub = [f"news_publish_datetime >= toDateTime({ch.sql_str(lo)})",
                   f"news_publish_datetime < toDateTime({ch.sql_str(hi)})"]
            if types:
                sub.append(f"event_type IN {ch.sql_in(types)}")
            if kind == "domain":
                sub.append(f"domain = {ch.sql_str(value)}")
            events_lane = (f"target_id GLOBAL IN (SELECT target_id FROM {tables.EVENTS_TABLE} "
                           f"WHERE {' AND '.join(sub)})")
            if kind == "domain" and not types:
                parts.append(f"({domain_lane_sql(value)} OR {events_lane})")
            else:
                parts.append(events_lane)
        return parts

    # ── normalised pieces ────────────────────────────────────────────────────
    def event_types(self) -> list[str]:
        return validate_event_types(split_list(self.event_type))

    def company_parts(self) -> tuple[Optional[str], Optional[str]]:
        if not self.company:
            return None, None
        return company_kind(self.company)

    def sectors(self) -> list[str]:
        return list(dict.fromkeys(s for s in (norm_sector(x) for x in split_list(self.sector)) if s))

    def round_types(self) -> list[str]:
        return list(dict.fromkeys(s for s in (norm_round_type(x) for x in split_list(self.round_type)) if s))

    def business_subject(self) -> dict:
        """The business extras as they ran, for subject.filters."""
        out: dict = {}
        kind, value = self.company_parts()
        if kind:
            out["company"], out["company_match"] = value, kind
        types = self.event_types()
        if types:
            out["event_type"] = types
        if self.sector:
            out["sector"] = self.sectors()
        if self.round_type:
            out["round_type"] = self.round_types()
        if self.min_amount_usd is not None:
            out["min_amount_usd"] = self.min_amount_usd
        if self.investor:
            out["investor"] = " ".join(self.investor.split()).lower()
        if self.resolve:
            out["resolve"] = True
        return out

    def links_companies(self) -> bool:
        return bool(self.company or self.event_type)

    def common(self, **override) -> Filters:
        """A plain general Filters with only the ✱ fields (for events/funding,
        which resolve the window/limit/q through the general code but build
        their own WHERE)."""
        d = {k: getattr(self, k) for k in Filters.model_fields}
        d.update(override)
        return Filters(**d)

    def reject_news_only(self, endpoint: str, allow: tuple[str, ...] = ()) -> None:
        bad = [k for k in NEWS_ONLY if k not in allow and getattr(self, k) is not None]
        if bad:
            raise _bad(f"{', '.join(f'`{k}`' for k in bad)} are news filters and do not apply to "
                       f"{endpoint}; they were not ignored — remove them")


# ── lane SQL ─────────────────────────────────────────────────────────────────
def validate_event_types(tokens) -> list[str]:
    out, bad = [], []
    for t in tokens:
        t = str(t).strip().lower()
        if not t:
            continue
        if t in tables.EVENT_TYPES:
            if t not in out:
                out.append(t)
        else:
            bad.append(t)
    if bad:
        raise _bad(f"unknown event_type(s): {', '.join(bad)}; valid types are "
                   f"{', '.join(tables.EVENT_TYPES)}")
    return out


def company_kind(value: str) -> tuple[str, str]:
    """('domain', 'amazon.com') or ('name', 'amazon'). A URL is reduced to its
    host; `www.` is dropped. Names are whitespace-collapsed and lowercased."""
    s = (value or "").strip().lower()
    host = re.sub(r"^[a-z][a-z0-9+.-]*://", "", s).split("/")[0].split("?")[0].split(":")[0]
    host = re.sub(r"^www\d?\.", "", host)
    if host and " " not in host and _DOMAIN_RE.match(host):
        return "domain", host
    name = " ".join(s.split())
    if len(name) < NAME_MIN or len(name) > NAME_MAX:
        raise _bad(f"`company` must be a domain (amazon.com) or a name of {NAME_MIN}–{NAME_MAX} characters")
    return "name", name


def require_domain(value: str, what: str) -> str:
    kind, v = company_kind(value)
    if kind != "domain":
        raise _bad(f"{what} is keyed by company DOMAIN (amazon.com, tesla.com); {value!r} is not one. "
                   f"Names work on /v1/business/headlines via `company`.")
    return v


def domain_lane_sql(domain: str) -> str:
    d = ch.sql_str(domain)
    return f"arrayExists(d -> d = {d} OR endsWith(d, {ch.sql_str('.' + domain)}), org_domains)"


def name_lane_sql(name: str) -> str:
    rx = ch.sql_str(q_regex(name))
    return (f"(arrayExists(x -> match(lower(x), {rx}), Organization) "
            f"OR arrayExists(x -> match(lower(x), {rx}), pri_organization) "
            f"OR has(tags, {ch.sql_str(name)}))")


def _linkage_bounds(r: Resolved) -> tuple[str, str]:
    """[since - days - 1, until + 2) — covers the window and the equal-length
    period before it, so /themes' previous-period count is not zeroed."""
    since = date.fromisoformat(r.since)
    until_x = date.fromisoformat(r.until_exclusive)
    lo = since - timedelta(days=r.days + 1)
    hi = until_x + timedelta(days=1)
    return lo.isoformat(), hi.isoformat()


def word_regex(term: str) -> str:
    return "(^|[^a-z0-9])" + re2_escape(term) + "([^a-z0-9]|$)"


def norm_sector(s: str) -> str:
    """'Healthcare Industry' -> 'healthcare'; 'space' stays 'space' (a bare
    label is never emptied)."""
    words = " ".join((s or "").lower().split()).split(" ")
    while len(words) > 1 and words[-1] in _SECTOR_TAILS:
        words.pop()
    return " ".join(w for w in words if w)


def norm_round_type(s: str) -> str:
    """'Series-B' / 'series_b' / 'Series B' -> 'series b'."""
    return " ".join(re.sub(r"[-_]+", " ", (s or "").lower()).split())


ROUND_TYPE_COL = "lowerUTF8(replaceRegexpAll(coalesce(round_type, ''), '[-_]+', ' '))"


def sector_sql(sectors: list[str]) -> str:
    alts = [f"match(lowerUTF8(coalesce(sector, '')), {ch.sql_str(word_regex(s))})" for s in sectors]
    return "(" + " OR ".join(alts) + ")"


def round_type_sql(types: list[str]) -> str:
    alts = [f"match({ROUND_TYPE_COL}, {ch.sql_str(word_regex(t))})" for t in types]
    return "(" + " OR ".join(alts) + ")"


def country_sql(country: str) -> str:
    c = " ".join((country or "").lower().split())
    for group in COUNTRY_ALIASES.values():
        if c in group:
            return f"lowerUTF8(coalesce(country, '')) IN {ch.sql_in(group)}"
    return f"lowerUTF8(coalesce(country, '')) = {ch.sql_str(c)}"


def investor_sql(investor: str) -> str:
    s = " ".join((investor or "").lower().split())
    if len(s) < NAME_MIN or len(s) > NAME_MAX:
        raise _bad(f"`investor` must be {NAME_MIN}–{NAME_MAX} characters")
    kind, v = company_kind(s)
    if kind == "domain":
        return (f"arrayExists(i -> lowerUTF8(coalesce(i.2, '')) = {ch.sql_str(v)} "
                f"OR endsWith(lowerUTF8(coalesce(i.2, '')), {ch.sql_str('.' + v)}), investor)")
    return f"arrayExists(i -> position(lowerUTF8(i.1), {ch.sql_str(v)}) > 0, investor)"


def funding_company_sql(company: str) -> str:
    kind, v = company_kind(company)
    if kind == "domain":
        return f"lowerUTF8(coalesce(domain, '')) = {ch.sql_str(v)}"
    return f"match(lowerUTF8(coalesce(company_name, '')), {ch.sql_str(word_regex(v))})"


# ── cursors ──────────────────────────────────────────────────────────────────
def _b64(obj: dict) -> str:
    raw = json.dumps(obj, separators=(",", ":")).encode()
    return base64.urlsafe_b64encode(raw).decode().rstrip("=")


def _unb64(s: str) -> dict:
    try:
        pad = "=" * (-len(s) % 4)
        obj = json.loads(base64.urlsafe_b64decode((s + pad).encode()).decode())
    except Exception:
        raise ValueError("not a cursor this API issued")
    if not isinstance(obj, dict) or obj.get("v") != CURSOR_VERSION:
        raise ValueError("unknown cursor version")
    return obj


def encode_events_cursor(sort: str, dt: str, target_id: str, domain: str,
                         event_type: str, role: str) -> str:
    return _b64({"v": CURSOR_VERSION, "t": "ev", "s": sort, "d": dt, "i": target_id,
                 "dm": domain, "et": event_type, "ro": role})


def decode_events_cursor(s: str, sort: str) -> dict:
    try:
        c = _unb64(s)
        if c.get("t") != "ev" or c.get("s") not in tables.EVENT_SORTS:
            raise ValueError("not an events cursor")
        if not isinstance(c.get("d"), str) or not _DT_RE.match(c["d"]):
            raise ValueError("bad datetime in cursor")
        if not isinstance(c.get("i"), str) or not _ID_RE.match(c["i"]):
            raise ValueError("bad id in cursor")
        if not isinstance(c.get("dm"), str) or len(c["dm"]) > 253 or not re.match(r"^[a-z0-9.\-]*$", c["dm"]):
            raise ValueError("bad domain in cursor")
        if c.get("et") not in tables.EVENT_TYPES or c.get("ro") not in tables.ROLES:
            raise ValueError("bad event type or role in cursor")
    except ValueError as e:
        raise _bad(f"invalid cursor: {e}")
    if c["s"] != sort:
        raise _bad(f"cursor was issued for sort={c['s']!r}, not {sort!r}")
    return c


def events_keyset_sql(c: dict, sort: str) -> str:
    op = ">" if sort == "oldest" else "<"
    return (f"(news_publish_datetime, target_id, domain, event_type, role) {op} "
            f"(toDateTime({ch.sql_str(c['d'])}), {ch.sql_str(c['i'])}, {ch.sql_str(c['dm'])}, "
            f"{ch.sql_str(c['et'])}, {ch.sql_str(c['ro'])})")


def encode_funding_cursor(sort: str, dt: str, k: int, amount: float | None = None) -> str:
    obj = {"v": CURSOR_VERSION, "t": "fr", "s": sort, "d": dt, "k": str(int(k))}
    if sort == "amount":
        obj["a"] = float(amount or 0)
    return _b64(obj)


def decode_funding_cursor(s: str, sort: str) -> dict:
    try:
        c = _unb64(s)
        if c.get("t") != "fr" or c.get("s") not in tables.FUNDING_SORTS:
            raise ValueError("not a funding cursor")
        if not isinstance(c.get("d"), str) or not _DT_RE.match(c["d"]):
            raise ValueError("bad datetime in cursor")
        if not isinstance(c.get("k"), str) or not _K_RE.match(c["k"]):
            raise ValueError("bad row key in cursor")
        if c["s"] == "amount" and not isinstance(c.get("a"), (int, float)):
            raise ValueError("bad amount in cursor")
    except ValueError as e:
        raise _bad(f"invalid cursor: {e}")
    if c["s"] != sort:
        raise _bad(f"cursor was issued for sort={c['s']!r}, not {sort!r}")
    return c


FUNDING_K = ("cityHash64(coalesce(target_id, ''), coalesce(company_name, ''), coalesce(round_type, ''), "
             "coalesce(amount_usd, 0.), coalesce(news_publish_datetime, toDateTime(0)), "
             "coalesce(source_sentence, ''))")
FUNDING_DT = "assumeNotNull(news_publish_datetime)"
FUNDING_AMT = tables.USABLE_AMOUNT


def funding_order_sql(sort: str) -> str:
    if sort == "oldest":
        return f"{FUNDING_DT} ASC, {FUNDING_K} ASC"
    if sort == "amount":
        return f"{FUNDING_AMT} DESC, {FUNDING_DT} DESC, {FUNDING_K} DESC"
    return f"{FUNDING_DT} DESC, {FUNDING_K} DESC"


def funding_keyset_sql(c: dict, sort: str) -> str:
    d, k = f"toDateTime({ch.sql_str(c['d'])})", f"toUInt64({ch.sql_str(c['k'])})"
    if sort == "oldest":
        return f"({FUNDING_DT}, {FUNDING_K}) > ({d}, {k})"
    if sort == "amount":
        return f"({FUNDING_AMT}, {FUNDING_DT}, {FUNDING_K}) < ({float(c['a'])!r}, {d}, {k})"
    return f"({FUNDING_DT}, {FUNDING_K}) < ({d}, {k})"
