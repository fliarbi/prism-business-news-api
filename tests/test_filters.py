import pytest

from prism_news_api import ch, config, filters as gf
from prism_news_api.envelope import ApiError

from prism_business_api import tables
from prism_business_api.filters import (FUNDING_AMT, BusinessFilters, company_kind, country_sql, decode_events_cursor,
                                        decode_funding_cursor, encode_events_cursor, encode_funding_cursor,
                                        events_keyset_sql, funding_keyset_sql, investor_sql, norm_round_type,
                                        norm_sector, round_type_sql, sector_sql, validate_event_types, word_regex)

FREE = dict(config.plans()["free"])
DT = "2026-08-24"


def where(**kw) -> str:
    r = gf.resolve(BusinessFilters(**kw), FREE, DT)
    return gf.where_sql(r)


# ── company detection ────────────────────────────────────────────────────────
@pytest.mark.parametrize("raw,kind,val", [
    ("amazon.com", "domain", "amazon.com"),
    ("AMAZON.COM", "domain", "amazon.com"),
    ("https://www.amazon.com/about?x=1", "domain", "amazon.com"),
    ("www2.tesla.com", "domain", "tesla.com"),
    ("Amazon", "name", "amazon"),
    ("  Amazon   Web Services ", "name", "amazon web services"),
    ("tesla, inc.", "name", "tesla, inc."),
])
def test_company_kind(raw, kind, val):
    assert company_kind(raw) == (kind, val)


def test_company_too_short_is_400():
    with pytest.raises(ApiError) as e:
        company_kind("a")
    assert e.value.status == 400


# ── SQL lanes on the news table ──────────────────────────────────────────────
def test_domain_lane_is_suffix_match_or_global_in_events():
    s = where(company="amazon.com", since="2026-02-05", until="2026-05-05")
    assert "arrayExists(d -> d = 'amazon.com' OR endsWith(d, '.amazon.com'), org_domains)" in s
    assert f"target_id GLOBAL IN (SELECT target_id FROM {tables.EVENTS_TABLE}" in s
    assert "domain = 'amazon.com'" in s and "event_type IN" not in s
    # subquery bounded to the window plus an equal-length period before it
    assert "news_publish_datetime >= toDateTime('2025-11-06')" in s
    assert "news_publish_datetime < toDateTime('2026-05-07')" in s
    assert " IN (SELECT" not in s.replace("GLOBAL IN (SELECT", "")   # never a plain IN subquery


def test_name_lane_is_word_bounded_on_entities_plus_tags():
    s = where(company="Amazon")
    assert "arrayExists(x -> match(lower(x), '(^|[^a-z0-9])amazon([^a-z0-9]|$)'), Organization)" in s
    assert "match(lower(x), '(^|[^a-z0-9])amazon([^a-z0-9]|$)'), pri_organization)" in s
    assert "has(tags, 'amazon')" in s
    assert "GLOBAL IN" not in s and "= 'amazon'" not in s              # substring, never equality


def test_event_type_lane_and_validation():
    s = where(event_type="layoffs,IPO")
    assert "event_type IN ('layoffs','ipo')" in s and "GLOBAL IN" in s
    s = where(event_type="layoffs", company="amazon.com")
    assert s.count("GLOBAL IN") == 1 and "domain = 'amazon.com'" in s and "org_domains" not in s
    s = where(event_type="layoffs", company="Amazon")
    assert "has(tags, 'amazon')" in s and "event_type IN ('layoffs')" in s
    with pytest.raises(ApiError) as e:
        where(event_type="layoffs,mergers")
    assert e.value.status == 400 and "mergers" in e.value.reason and "earnings" in e.value.reason
    assert validate_event_types(["earnings", "earnings", " ma "]) == ["earnings", "ma"]
    assert len(tables.EVENT_TYPES) == 19 and len(tables.ROLES) == 8


def test_injection_safe_quoting():
    s = where(company="x'); DROP TABLE news.articles; --")
    assert "drop table" in s                                            # names are lowercased
    assert "x\\'); drop table" in s and "'x');" not in s               # the quote is escaped, never closes the literal
    s = where(company="o'reilly.com")                                   # apostrophe -> not a domain -> name lane
    assert "has(tags, 'o\\'reilly.com')" in s
    s = sector_sql(["a.b(c)"])
    assert ch.sql_str(word_regex("a.b(c)")) in s and "a\\\\.b\\\\(c\\\\)" in s   # re2-escaped, then SQL-escaped


def test_funding_only_params_are_400_on_news_endpoints():
    for kw in ({"sector": "fintech"}, {"round_type": "seed"}, {"min_amount_usd": 1}, {"investor": "sequoia"}):
        with pytest.raises(ApiError) as e:
            where(**kw)
        assert e.value.status == 400 and "funding" in e.value.reason


def test_news_only_params_are_rejected_for_tables():
    with pytest.raises(ApiError) as e:
        BusinessFilters(sentiment="negative").reject_news_only("/v1/business/events")
    assert e.value.status == 400 and "sentiment" in e.value.reason
    BusinessFilters(q="x y", since="2026-01-01").reject_news_only("/v1/business/events")


def test_business_subject_and_common():
    f = BusinessFilters(company="https://Amazon.com", event_type="ma,earnings", q="tariff", sentiment="negative")
    assert f.business_subject() == {"company": "amazon.com", "company_match": "domain",
                                    "event_type": ["ma", "earnings"]}
    assert f.links_companies() and not BusinessFilters(q="x y").links_companies()
    c = f.common(sort="newest", cursor=None)
    assert type(c) is gf.Filters and c.q == "tariff" and c.sentiment == "negative"


# ── funding normalisation ────────────────────────────────────────────────────
@pytest.mark.parametrize("raw,norm", [
    ("Healthcare Industry", "healthcare"), ("space", "space"), ("Space Industry", "space"),
    ("fintech companies", "fintech"), ("  AI  sector market ", "ai"), ("Oil & Gas", "oil & gas"),
    ("financial services", "financial services"), ("business", "business"),
])
def test_norm_sector(raw, norm):
    assert norm_sector(raw) == norm


def test_sector_sql_is_word_bounded_not_ilike():
    s = sector_sql(["space", "oil & gas"])
    assert "ILIKE" not in s
    assert "match(lowerUTF8(coalesce(sector, '')), '(^|[^a-z0-9])space([^a-z0-9]|$)')" in s
    assert "'(^|[^a-z0-9])oil & gas([^a-z0-9]|$)'" in s
    assert BusinessFilters(sector="Space Industry|Fintech Companies").sectors() == ["space", "fintech"]


@pytest.mark.parametrize("raw,norm", [("Series-B", "series b"), ("series_b", "series b"),
                                      (" Series  B ", "series b"), ("Pre-Seed", "pre seed")])
def test_norm_round_type(raw, norm):
    assert norm_round_type(raw) == norm


def test_round_type_sql_normalises_the_column_too():
    s = round_type_sql(["series b"])
    assert "replaceRegexpAll(coalesce(round_type, ''), '[-_]+', ' ')" in s
    assert "(^|[^a-z0-9])series b([^a-z0-9]|$)" in s


def test_country_aliases():
    assert "IN ('united states','usa','us'" in country_sql("USA")
    assert country_sql("India") == "lowerUTF8(coalesce(country, '')) = 'india'"
    assert "'uk'" in country_sql("United Kingdom")


def test_investor_sql_name_vs_domain():
    assert investor_sql("Sequoia") == "arrayExists(i -> position(lowerUTF8(i.1), 'sequoia') > 0, investor)"
    assert "coalesce(i.2, '')) = 'sequoiacap.com'" in investor_sql("sequoiacap.com")
    with pytest.raises(ApiError):
        investor_sql("a")


# ── cursors ──────────────────────────────────────────────────────────────────
def test_events_cursor_round_trip_and_tamper():
    c = encode_events_cursor("newest", "2026-05-05 10:00:00", "69f881d343843dd771cf50f2", "amazon.com", "layoffs", "primary")
    d = decode_events_cursor(c, "newest")
    assert d["i"] == "69f881d343843dd771cf50f2" and d["dm"] == "amazon.com" and d["et"] == "layoffs"
    assert events_keyset_sql(d, "newest").startswith("(news_publish_datetime, target_id, domain, event_type, role) < (toDateTime('2026-05-05 10:00:00'), '69f881d343843dd771cf50f2', 'amazon.com', 'layoffs', 'primary')")
    assert " > (" in events_keyset_sql(d, "oldest")
    with pytest.raises(ApiError) as e:
        decode_events_cursor(c, "oldest")
    assert e.value.status == 400 and "sort" in e.value.reason
    bad = encode_events_cursor("newest", "2026-05-05 10:00:00", "69f881d343843dd771cf50f2", "amazon.com", "mergers", "primary")
    with pytest.raises(ApiError):
        decode_events_cursor(bad, "newest")
    with pytest.raises(ApiError):
        decode_events_cursor("not-a-cursor", "newest")
    with pytest.raises(ApiError):                                        # a funding cursor on events
        decode_events_cursor(encode_funding_cursor("newest", "2026-05-05 10:00:00", 1), "newest")


def test_funding_cursor_round_trip():
    c = encode_funding_cursor("amount", "2026-05-04 21:30:02", 12345678901234567, 125000000.0)
    d = decode_funding_cursor(c, "amount")
    assert d["k"] == "12345678901234567" and d["a"] == 125000000.0
    s = funding_keyset_sql(d, "amount")
    assert s.startswith(f"({FUNDING_AMT}, assumeNotNull(news_publish_datetime), cityHash64(") and "< (125000000.0, toDateTime('2026-05-04 21:30:02'), toUInt64('12345678901234567'))" in s
    c2 = encode_funding_cursor("newest", "2026-05-04 21:30:02", 7)
    assert "> (" in funding_keyset_sql(decode_funding_cursor(c2, "newest") | {"s": "oldest"}, "oldest")
    with pytest.raises(ApiError):
        decode_funding_cursor(c2, "amount")
