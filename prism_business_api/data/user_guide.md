# Prism Business News API user guide

Explore business news within **450M+ historical and real-time news articles** from Fliar. The article count is supplied by Fliar; query counts reflect available matching coverage.

Search business headlines, monitor company events, and analyze funding deals. This guide covers the business workflows and endpoint reference. The [shared News API guide](https://github.com/fliarbi/prism-news-api/blob/main/docs/USER_GUIDE.md) explains common filters, GCP content codes, export formats, quotas and errors in detail.

**Access status: live.** Base URL `https://radar-api.fliarbi.com/business-news`; general news endpoints are at `https://radar-api.fliarbi.com/news`. Create a key in the Fliar dashboard under **API keys** (one key works on the Radar API and both News APIs). Free, Pro (₹4,000/month), Business (₹15,000/month) and Enterprise plans; prices exclude GST.

## Contents

- [Access and first query](#access-and-first-query)
- [Choose the right endpoint](#choose-the-right-endpoint)
- [Business scope and filters](#business-scope-and-filters)
- [Discover themes and read 100 headlines](#discover-themes-and-read-100-headlines)
- [Company events](#company-events)
- [Funding deals](#funding-deals)
- [Overview and summaries](#overview-and-summaries)
- [Company briefing and comparison workflows](#company-briefing-and-comparison-workflows)
- [Pagination and full-article retrieval](#pagination-and-full-article-retrieval)
- [Coverage and freshness](#coverage-and-freshness)
- [Quotas, errors and retry](#quotas-errors-and-retry)
- [Endpoint reference](#endpoint-reference)

## Access and first query

1. Sign in to the [Fliar dashboard](https://fliarbi.com/radar/dashboard?tab=radarapi), open **API keys** (in the Radar or the Fliar Prism workspace) and choose **Create or manage API keys**. On the key page, choose **Connect Radar session**, pick **All data** or **News only** access and create a key. It starts with `rdr_` and also works on the Radar API.
2. You receive the key once; copy it when shown. The same key works on the general News API.
3. Set `PRISM_BUSINESS_API_BASE=https://radar-api.fliarbi.com/business-news` and `PRISM_API_KEY` to the issued key. Keep the key private and out of public application code.

```bash
PRISM_BUSINESS_API_BASE=https://radar-api.fliarbi.com/business-news
read -r -s -p 'API key: ' PRISM_API_KEY
export PRISM_BUSINESS_API_BASE PRISM_API_KEY

curl -sS "$PRISM_BUSINESS_API_BASE/v1/me" -H "X-API-Key: $PRISM_API_KEY"
```

Either `X-API-Key` or `Authorization: Bearer` is accepted:

```bash
curl -sS --get "$PRISM_BUSINESS_API_BASE/v1/business/headlines" \
  -H "Authorization: Bearer $PRISM_API_KEY" \
  --data-urlencode 'q=acquisition' --data-urlencode 'limit=100'
```

One key works on both APIs, with account-level request, export and rate allowances shared across them. `/v1/me` returns your key summary, plan, limits and usage. Revoke or replace a key through the dashboard when available, or through your access contact during preview.

The Python examples use `requests` and this helper. `GET/POST` endpoints accept the same parameters as a GET query string or a flat JSON object:

```python
import os
import requests

BASE = os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news")
session = requests.Session()
session.headers["X-API-Key"] = os.environ["PRISM_API_KEY"]

def call(method, path, **kwargs):
    response = session.request(method, BASE + path, timeout=60, **kwargs)
    payload = response.json()
    if not response.ok or not payload.get("ok"):
        error = payload.get("error") or {}
        raise RuntimeError(
            f"HTTP {response.status_code}: {error.get('kind')} — {error.get('reason')}"
        )
    return payload

page = call("POST", "/v1/business/headlines", json={"q": "acquisition", "limit": 100})
print(page["subject"], page["window"], page["meta"].get("notes", []))
for article in page["data"]["items"]:
    print(article["headline"], article["url"], article["events"])
```

The envelope is `ok`, `feature`, `subject`, `data`, `window` and `meta`, with `error.kind` and `error.reason` on failures. `subject.filters` describes the normalized request that actually ran. Use `window` and `meta.notes` to see date and access adjustments.

Once access is enabled, `/guide` serves this user guide as Markdown. `/docs` and `/v1/openapi.json` describe the endpoint contract at your supplied base URL.

## Choose the right endpoint

| Need | Endpoint | Unit counted |
|---|---|---|
| Read coverage | `/v1/business/headlines` | Articles, with linked event summaries when available |
| Discover themes | `/v1/business/themes` | At most five suggestions for a required `q` |
| Analyze article tone or volume | `/v1/business/sentiment`, `/v1/business/trends` | Articles |
| Follow company activity | `/v1/business/events` | Distinct events; several can share an article |
| Measure events over time | `/v1/business/event-trends` | Events, with article and company totals |
| Inspect financing | `/v1/business/funding` | Funding deal records |
| Analyze funding over time | `/v1/business/funding/summary` | Deals and usable reported amounts |
| Review all three populations | `/v1/business/overview` | Separate news, event and funding counts in one window |
| Read a company briefing | `/v1/business/companies/{domain}/news` | Three separate lists with their own windows |

The general News API adds `/v1/overview`, `/v1/compare`, `/v1/geography`, `/v1/coverage` and related-article reading on its supplied base URL. Its geography search requires `q` and returns at most five results. See the [shared endpoint reference](https://github.com/fliarbi/prism-news-api/blob/main/docs/USER_GUIDE.md#endpoint-reference) before switching products; business-only filters do not apply to general news operations.

## Business scope and filters

Business headline, theme, sentiment and trend requests default to GCP content paths under `/News/Business News`, `/Business & Industrial` and `/Finance`. Overview also applies this business scope. Supplying `classes` or `class_prefix` **replaces** that default scope. Inspect `subject.scope.applied` and `subject.filters.classes` to confirm what ran.

GCP content codes represent public standardized content paths. Code **`0`** is `/News/Business News/Company News`, and is a valid filter even though its value is zero.

```bash
curl -sS --get "$PRISM_BUSINESS_API_BASE/v1/classes" \
  -H "X-API-Key: $PRISM_API_KEY" \
  --data-urlencode 'q=company' --data-urlencode 'limit=5'
curl -sS "$PRISM_BUSINESS_API_BASE/v1/classes/0" -H "X-API-Key: $PRISM_API_KEY"

curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/headlines" \
  -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  --data '{"q":"acquisition","sentiment":"negative","priority_min":7,"classes":[0],"limit":100}'
```

Class search requires a meaningful `q` or a nonroot `prefix`, with `limit` from 1 to 5 and default 5. Class detail returns at most five children and no theme suggestions. `/v1/vocabulary` supplies static public sentiment, priority and request options, with no dynamic theme dictionary.

### Common news filters

| Filter | Meaning |
|---|---|
| `q` | Case-insensitive phrase, 2–120 characters. On news queries this searches the opening text and available subject/entity matches, not full article bodies. |
| `match` | `any` (default), `opening`, or `focused`. `opening` requires a match in the opening text; `focused` favors stories centrally about the subject and reduces broad roundups. |
| `sentiment` | Groups `negative`, `neutral`, `positive`, or exact labels listed below. |
| `priority_min`, `priority_max` | Inclusive integers 1–9. Higher means more consequential; 7–9 are critical. |
| `classes`, `class_prefix` | GCP codes or a content path; qualifying code score must exceed `0.39`. Replaces the default business scope. |
| `themes` | Up to five exact names returned by discovery. Prefer JSON arrays. |
| `country` | On news, the article's available country information; on funding, the deal country. Not supported by the events listing. |
| `since`, `until` | Inclusive `YYYY-MM-DD` dates, bounded by available coverage and access. Read the returned window. |
| `limit`, `sort`, `cursor` | Listing controls. Default list size 100; the cap depends on your plan. News sort: `newest`, `oldest`, `priority`. Discovery and aggregations have separate rules. |
| `granularity` | `daily`, `weekly` (default), `monthly` on time-series endpoints. |

Sentiment labels are `extreme_neg`, `very_neg`, `fair_neg`, `slight_neg` for negative; `none` for neutral; and `slight_pos`, `fair_pos`, `very_pos`, `extreme_pos` for positive. Each article uses its highest-scoring label. Different filters combine with AND; multiple sentiment labels, codes or themes within one filter combine with OR. `classes` and `class_prefix` also form a union when supplied together.

Useful combinations include:

| Question | Filters |
|---|---|
| What is being reported about a company? | `{"company":"amazon.com"}` |
| Which company stories have negative tone? | `{"sentiment":"negative","classes":[0]}` |
| Which acquisition stories have high priority? | `{"q":"acquisition","priority_min":7,"classes":[0]}` |
| Which stories satisfy all three signals? | `{"q":"acquisition","sentiment":"negative","priority_min":7,"classes":[0]}` |

### Business-specific filters

| Parameter | Meaning and supported operations |
|---|---|
| `company` | Domain such as `amazon.com` or name such as `Amazon` on business news and funding. The events listing and company briefing require a domain. Names are broader matches; domains are more specific and depend on available company attribution. |
| `event_type` | One or more public event types listed below. Available on business news, events, and the three aggregate endpoints; not on the funding listing. |
| `sector` | One or more funding sectors, matched case-insensitively. Available on funding, funding summary and overview. |
| `round_type` | One or more funding round descriptions; spacing, hyphens and underscores are normalized. Available on funding, funding summary and overview. |
| `min_amount_usd` | Nonnegative amount threshold for funding, funding summary and overview. |
| `investor` | Investor name or domain for funding, funding summary and overview. Name matching is broader than a domain match. |
| `resolve` | `true` on the events listing adds article `title`, `url` and `publisher`; default `false`. |

Pass list values as JSON arrays or comma-separated GET values. Preserve returned theme punctuation by using arrays.

The **events and funding listings reject news-only filters** such as sentiment, GCP codes, themes, priority and `match`. The new **aggregate endpoints accept these filters** and apply them to source articles, as described below. Funding-only filters on ordinary business news endpoints produce `400 bad_request`.

## Discover themes and read 100 headlines

`GET/POST /v1/business/themes` requires a specific `q`: **2–120 characters, including at least two alphanumeric characters**. `limit` defaults to **5** and must be between **1 and 5**; values above 5 return `400 bad_request`. `cursor` is rejected. A company or GCP code alone does not replace the required phrase.

```python
discovery = call("POST", "/v1/business/themes", json={
    "q": "acquisition", "sentiment": "negative",
    "priority_min": 7, "classes": [0], "limit": 5,
})
selected_theme = discovery["data"]["items"][0]["theme"]
filters = dict(discovery["subject"]["filters"])
filters.pop("cursor", None)
filters.pop("company_match", None)
filters.update(themes=[selected_theme], limit=100)
headlines = call("POST", "/v1/business/headlines", json=filters)
print(headlines["data"]["returned"], headlines["data"]["next_cursor"])
```

There is no separate business theme-headlines path: supply `themes` to `/v1/business/headlines`. Keep the original phrase, sentiment, priority, GCP codes, company/event filters and normalized dates when moving from discovery to reading.

Discovery items include `theme`, support `count`, `share`, `lift` and previous-period comparison fields. If the preceding equal-length window is outside your plan’s history allowance, `previous_period`, `previous_period_count` and `delta_pct` are `null`. A zero previous count also makes `delta_pct` null. Shares divide by matching articles carrying themes. Lift compares against the general 30-day all-news baseline, so a theme common in business coverage can be prominent relative to that broader baseline. `null` ratios represent an unavailable comparison, not zero.

Headlines, single articles and exports **do not return theme metadata**. Select themes through the bounded discovery operation. A selected theme yields **100 headlines per page by default** and **100 full articles per export batch by default**; higher caps depend on your plan. See [full-article retrieval](#pagination-and-full-article-retrieval) to preserve scope when exporting.

## Company events

```bash
curl -sS --get "$PRISM_BUSINESS_API_BASE/v1/business/events" \
  -H "X-API-Key: $PRISM_API_KEY" \
  --data-urlencode 'company=amazon.com' \
  --data-urlencode 'event_type=layoffs,ipo' \
  --data-urlencode 'resolve=true' --data-urlencode 'limit=100'
```

| Public `event_type` | Meaning |
|---|---|
| `earnings` | Earnings and results |
| `key_people` | Leadership or other key personnel changes |
| `ma` | Mergers and acquisitions |
| `company_announcement` | Company announcements |
| `contracts` | Contract activity |
| `funding_rounds` | Funding-round events reported in articles |
| `asset_acquisition` | Asset acquisitions |
| `lawsuit` | Lawsuits |
| `new_product` | Product announcements |
| `regulatory` | Regulatory activity |
| `capital_infusion` | Capital infusions |
| `ipo` | Initial public offerings |
| `job_creation` | Job creation |
| `layoffs` | Layoffs |
| `board_updates` | Board changes |
| `funds_raising` | Fundraising activity |
| `buyback` | Buybacks |
| `incorporation` | Incorporations |
| `fda_approval` | FDA approvals |

An event item has `id`, `headline`, `event_type`, `role`, `domain` and `published_at`. **`headline` is the source sentence describing the event**, not necessarily the article title. With `resolve=true`, `title`, `url` and `publisher` are added when available; missing details do not remove the event.

Roles include `primary`, `acquirer`, `target`, `seller`, `contractor`, `client`, `plaintiff` and `defendant`. Several roles or event types can share the same article ID. An event represents an article, company domain, event type, role and publication time; repeated sentences with the same identity count once. Do not deduplicate an events list by article ID alone.

`q` searches the event sentence. `company` must be a domain on this listing. Sort is `newest` or `oldest`; `country`, funding filters and news-only filters are rejected. `data.by_type` counts all matches by type, and `total_estimate` covers the full filtered listing, not just the current page.

The event's `id` is usable with `GET /v1/articles/{article_id}` if the article is available. It is not guaranteed that every event has a retrievable full article.

## Funding deals

```python
funding = call("POST", "/v1/business/funding", json={
    "round_type": "series b", "min_amount_usd": 50_000_000,
    "country": "USA", "sort": "amount", "limit": 100,
})
print(funding["window"], funding["data"]["totals"])
for deal in funding["data"]["items"]:
    print(deal["company_name"], deal["amount_usd"], deal["coverage_count"])
```

`q` searches deal descriptions, company names and stated use of funds. `company` accepts a name or domain. Sort is `newest`, `oldest` or `amount` (largest first). `event_type`, `resolve` and news-only filters are rejected on the listing.

| Returned fields | How to use them |
|---|---|
| `id` | Deal ID; it is not an article ID. |
| `company_name`, `domain`, `round_type` | Recipient company and reported round description. |
| `amount_usd`, `valuation_usd` | Fixed-rate USD conversions; not current or transaction-date exchange rates. Missing or withheld values are `null`. |
| `amount_flag` | `null` when `amount_usd` is usable; `implausible_size` when the reported figure exceeds 25 billion USD (usually a unit or valuation error); `unconverted_currency` when a local-currency figure was not converted. Flagged amounts are left out of totals and of `sort=amount`. |
| `amount`, `valuation`, `currency` | Reported amount and currency details. |
| `investors` | Entries with `name`, `domain` and `amount` when reported. |
| `sector`, `country`, `city`, `use_of_funds` | Reported deal context; some values may be unavailable. |
| `source_sentence`, `published_at` | Evidence sentence and publication time, not necessarily the transaction date. |
| `coverage_count` | Number of articles reporting the deal; not the number of deals. |
| `article_id`, `article_ids` | Article IDs for source reading, subject to availability. |

The listing's `data.totals` includes `deals`, `deals_with_amount`, `deals_without_amount`, `deals_amount_excluded`, `sum_amount_usd`, `median_amount_usd`, `largest_amount_usd` and `currency`. Totals describe all matches. Amount statistics are `null` when no deal has a usable amount. Use `/v1/business/funding/summary` for the corresponding time series.

Round descriptions and sectors may contain spelling variations. `Series-B`, `series_b` and `Series B` normalize equivalently for matching. A broad `seed` filter can also match pre-seed; use `pre-seed` when that is the intended subset. Funding country filters recognize common aliases such as `USA`, `US` and `United States`, or `UK` and `United Kingdom`.

## Overview and summaries

These are full-window aggregations, not summaries of a retrieved page. They accept JSON bodies on POST and query parameters on GET. **Do not send `limit`, `cursor`, `sort` or `resolve`**; these listing controls are rejected, including `sort=newest`. Overview has no `granularity`; the two time-series summaries accept it.

The aggregation window is at most **366 days**, possibly shorter under account limits. It ends no later than the oldest applicable `data_through`. `window.datasets` shows the dates for news, events and/or funding used by the request; `window.max_days` and notes describe the bound. Inspect effective dates after every request.

### Business overview

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/overview" \
  -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  --data '{"q":"acquisition","sentiment":"negative","priority_min":7,"classes":[0]}'
```

`data` contains:

- `archive`: publisher-supplied description of the news data (450M+ historical and real-time articles), separate from measured results.
- `news`: `articles`, `critical`, `negative`, `positive` and a counting explanation.
- `events`: `events`, `articles`, `companies` and a counting explanation.
- `funding`: `deals`, `deals_with_amount`, `deals_without_amount`, amount statistics, `currency` and a note.

News, events and funding are separate populations; do not add them. Overview uses one common date window and a business article scope. Funding-specific filters also restrict the linked news and events in the overview. Without an explicit `match`, `q` searches news text, event descriptions and deal descriptions in their respective blocks; set `match` deliberately if you want source-article matching across them.

### Event trends

```python
events = call("POST", "/v1/business/event-trends", json={
    "event_type": ["layoffs", "job_creation"], "granularity": "monthly",
})
print(events["data"]["totals"], events["data"]["by_type"])
for point in events["data"]["points"]:
    print(point["period"], point["events"], point["by_type"], point["partial_period"])
```

Returns `granularity`, `points`, `totals`, `by_type`, `complete_periods` and `partial_periods`. Each point has `period`, `events`, `by_type` and `partial_period`. `totals` distinguishes event, article and company counts. Empty periods are included as zero. Funding-only parameters are rejected.

### Funding summary

```python
summary = call("POST", "/v1/business/funding/summary", json={
    "round_type": "series b", "country": "USA", "granularity": "monthly",
})
print(summary["window"], summary["data"]["totals"])
for point in summary["data"]["points"]:
    print(point["period"], point["deals"], point["deals_without_amount"], point["sum_amount_usd"])
```

Returns `totals`, `granularity` and `points`. Totals include `deals`, `deals_with_amount`, `deals_without_amount`, `deals_amount_excluded`, `sum_amount_usd`, `median_amount_usd`, `largest_amount_usd` and `currency="USD"`. Points include the same measures plus `period` and `partial_period`.

Each deal counts once even if several source articles match. Only usable amounts enter amount statistics: finite, positive, converted to USD and at most 25 billion USD. Larger or unconverted figures are counted in `deals_amount_excluded`. Sums and medians count each company and amount once, because one round is often reported under several labels. Unknown, zero and non-finite amounts are excluded from those statistics but still count as deals. The median is the conventional median: with an even number of usable amounts, it averages the middle two (10 and 20 give 15). If no matched deal has a usable amount, summary amount statistics are `null`; zero matched deals remains a valid aggregate result. Medians across periods cannot be averaged to obtain an overall median.

### Combining article signals with events and deals

Unlike the listings, the aggregate endpoints accept sentiment, priority, GCP codes and themes. These filters require a matching source article in the same window, so records without a suitable source article are excluded. Explicit `match=any`, `opening` or `focused` also uses source-article matching for `q`; omitting `match` lets event and funding descriptions supply the phrase match.

Standalone event trends and funding summary do not add the default business GCP scope. Without source-article filters, they preserve event/deal coverage that lacks a matching article; adding article signals narrows the result to records with a suitable source article. In event trends, `country` refers to the source article; in funding summary it refers to the deal. Read normalized filters and notes before comparing a listing with a summary using additional article signals.

## Company briefing and comparison workflows

### One company

```python
briefing = call("GET", "/v1/business/companies/amazon.com/news", params={"limit": 100})
print(briefing["data"]["counts"])
for name in ("headlines", "events", "funding"):
    block = briefing["data"][name]
    print(name, block["returned"], block["window"], block.get("empty_reason"))
```

The response has `domain`, `counts`, `headlines`, `events` and `funding`. Each list block has its own items, count, continuation token, window and notes. A block can be empty with `empty_reason`; the route returns `404 no_data` only if all three blocks are empty. This is one metered request.

News filters apply to the headlines block. `since`, `until` and `limit` apply to all three; a headline `event_type` does not filter the briefing's separate events block. Use dedicated endpoints to filter or page the event and funding lists. To continue a block, send its cursor and effective dates to the corresponding listing, with the same company and supported filters. Do not use one cursor for the entire briefing.

### Compare companies or funding segments

Use explicit common dates, preserve scope, and compare the same unit. The following compares overview results for two domains after obtaining one permitted common window:

```python
first = call("POST", "/v1/business/overview", json={"company": "amazon.com"})
window = {key: first["window"][key] for key in ("since", "until")}
reports = {"amazon.com": first}
reports["tesla.com"] = call("POST", "/v1/business/overview", json={
    **window, "company": "tesla.com",
})
for company, report in reports.items():
    print(company, report["window"], report["data"]["news"]["articles"],
          report["data"]["events"]["events"], report["data"]["funding"]["deals"])
```

For funding comparisons, call funding summary with identical dates and different country, investor or round filters. Compare deal counts separately from reported amount totals; compare amount availability before drawing conclusions from sums.

The general News API offers **`POST /v1/compare`** for 2–5 named news filter sets. A valid request body is:

```json
{
  "queries": [
    {"name": "Acquisitions", "filters": {"q": "acquisition", "classes": [0]}},
    {"name": "Earnings", "filters": {"q": "earnings", "classes": [0]}}
  ]
}
```

It compares news article counts and overlapping shares. Use the News API's supplied base URL, public GCP codes and news filters; it does not accept the business `company` filter. See the [comparison example](https://github.com/fliarbi/prism-news-api/blob/main/docs/USER_GUIDE.md#compare-25-named-queries).

### Practical sequences

| Workflow | Sequence |
|---|---|
| Daily reading list | Business overview → themes with a specific `q` and `limit=5` → selected theme headlines with `limit=100` → chosen full articles. |
| Company activity | Company briefing → filtered events → event trends using the same dates → source articles for the events that matter. |
| Funding landscape | Funding summary → inspect amount availability → funding listing sorted by amount → source sentences and articles. |
| Tone comparison | Choose consistent company or subject filters and dates → business sentiment for each → compare group shares and carrying counts → inspect headlines. |

## Pagination and full-article retrieval

For a listing, preserve the original supported filters, replace dates with the first response's effective dates, and pass `data.next_cursor` to the same endpoint. `subject.filters.cursor=true` is only a marker, not the token. Do not send derived fields such as `company_match` back as parameters.

```python
filters = {"company": "amazon.com", "event_type": "layoffs", "limit": 100, "sort": "newest"}
page = call("POST", "/v1/business/headlines", json=filters)
fixed = {**filters, **{key: page["subject"]["filters"][key] for key in ("since", "until", "classes")}}

while True:
    for item in page["data"]["items"]:
        print(item["id"], item["headline"])
    cursor = page["data"].get("next_cursor")
    if not cursor:
        break
    page = call("POST", "/v1/business/headlines", json={**fixed, "cursor": cursor})
```

This consumes one request per page until the listing ends; set a page budget if only a sample is needed. A short headline page can still have a cursor. Deduplicate articles by ID or URL across pages, but preserve distinct event roles and types. Funding cursors belong to funding listings and depend on the original sort.

### Export a theme or news filter set

The business host serves the shared `POST /v1/export`, which accepts **general news filters** and has **no default business scope**. It does not apply `company` or `event_type`. Do not blindly replay a company-filtered business request into this endpoint: unsupported filters can be ignored, producing a broader result.

For a theme workflow using only common news filters, carry over the normalized GCP codes, dates, phrase, sentiment and priority. The following starts from the `headlines` result in the theme example above and validates that no business-only selection would be lost:

```python
export_filters = dict(headlines["subject"]["filters"])
if export_filters.get("company") or export_filters.get("event_type"):
    raise ValueError("Retrieve the returned article IDs individually to preserve company/event selection.")
export_filters.pop("cursor", None)
export_filters.pop("company_match", None)
export_filters.update(limit=100, format="json")
exported = call("POST", "/v1/export", json=export_filters)
print(exported["data"]["returned"], exported["data"]["charged_exports"])
```

For a company/event-filtered reading list, retrieve each selected headline's ID through `GET /v1/articles/{article_id}`. This preserves the selected articles and consumes one request plus one export allowance per delivered article. An event's `id` or a deal's `article_id` can also be used; a deal's own `id` cannot.

```python
selected = call("POST", "/v1/business/headlines", json={"company": "amazon.com", "limit": 1})
article_id = selected["data"]["items"][0]["id"]
full = call("GET", f"/v1/articles/{article_id}")
print(full["data"]["article"]["body"])
```

Exports default to **100** full articles per batch; `data.limits.max_export_batch` in `/v1/me` gives your plan cap. Remaining allowance can reduce the batch further. JSON provides items and the next cursor; NDJSON begins with an envelope followed by one article per line; CSV provides a download. Use JSON or NDJSON for paged exports and start with no cursor when changing endpoints. Full articles and exports omit theme metadata. See [shared export examples](https://github.com/fliarbi/prism-news-api/blob/main/docs/USER_GUIDE.md#full-articles-and-exports) for parsing and columns.

## Coverage and freshness

- News, company attribution, events and funding can end on different dates. Read `window.data_through`, nested briefing windows, aggregation `window.datasets`, `freshness` and `meta.notes`.
- Listings normally begin 90 days before their relevant end date, inclusively. Company-linked news can default to an earlier attribution horizon when you omit `until`. Supplying a recent date does not create missing coverage.
- Aggregations use a common bounded window ending at the oldest applicable coverage date. This can differ from the default of a standalone listing.
- A recent volume decline may reflect incomplete coverage. `partial_period` marks an incomplete interval at the edge of the requested window; an unflagged interval is not a guarantee of complete reporting.
- News articles, events and deals are different units. Event counts are not unique real-world incident counts, and funding `coverage_count` is not a deal count. Multiple source articles do not multiply a deal in the funding summary.
- Theme and sentiment shares use articles carrying the respective information. Check the available denominator before comparing percentages. A missing ratio or amount statistic should remain `null`.
- Dates describe source publication, not necessarily when an event or investment occurred. USD conversions use fixed rates; use original currency and amount fields when that distinction matters.
- An event or deal may be available while its full source article is not. Missing article details are not evidence that the event did not occur.

The article count is supplied by Fliar; query counts reflect the available matching coverage. `/v1/status` and `/v1/me` should be interpreted together with each business response's own window; `/healthz` establishes liveness only.

## Quotas, errors and retry

`/v1/me` gives your effective limits and usage. Both APIs and all account keys share request, delivered-article and rate allowances. Monthly allowances reset on the first day of the UTC month. Draft plans and prices do not imply an active checkout or public launch.

Headlines and exports default to 100 on every plan. Caps are 100 for Free/Pro, 500 for Business and 1,000 for Enterprise; verify your own `max_results` and `max_export_batch` in `/v1/me`. Theme and GCP discovery remain capped at five on every plan. Each account may also run a limited number of requests at once (`concurrent_requests`: 2 on Free, 5 on Pro, 10 on Business, 25 on Enterprise); extra requests receive `429 rate_limited` with `Retry-After`. Usage levels lift the per-minute and concurrent limits as an account's lifetime prepaid credit usage grows (Growth from 10,000 credits, Scale from 100,000, Premier from 1,000,000); `/v1/me` returns `data.level` and the effective `data.limits`.

Every business operation listed below uses monthly request allowance, including the three aggregations and the combined company briefing. Single articles and exports additionally consume allowance per full article delivered. Validation or data failures after metering can consume a request. Repeating a successful full-article request consumes export allowance again.

Shared `/v1/me`, `/v1/status`, `/v1/vocabulary`, GCP code search and GCP code detail do not consume monthly request allowance, but still count toward the rate limit. **GCP class headlines are metered.**

| HTTP / kind | Action |
|---|---|
| `400 bad_request` | Correct parameters. Check discovery `q` and limit, domain-only company operations, unsupported filters, listing controls on summaries and cursor/sort consistency. |
| `401 unauthenticated` / `invalid_key` | Supply a valid key header or replace the key through your access process. |
| `402 quota_exceeded` | The plan allowance is used and no prepaid credits are available. Add credits and a monthly spending limit on the API key page (pay-as-you-go: 1 credit per request or full-text article, ₹0.84 or US$0.01), upgrade the plan, or wait for the monthly reset. |
| `404 no_data` | Read the reason; verify the route, dates, company and filters. A missing source article is possible even when an event/deal exists. |
| `429 rate_limited` | Honor `Retry-After` and reduce concurrency. |
| `500 internal` / `502 upstream` | Retry a limited number of times with backoff; report persistent failures with sanitized request details. |
| `503 coverage_unavailable` | Coverage could not be established; retry later, and do not record the result as zero. |
| Note: *Part of the news index is temporarily offline* | The answer uses the available part of the news index; treat its counts as minimums. |

Use bounded exponential backoff with jitter for transient failures, for example up to three retries with roughly 1, 2 and 4 seconds between attempts, or a longer `Retry-After`. Retries can consume request allowance. After a full-article or export timeout, check saved output and usage before repeating; there is no documented idempotency key.

Quota information is available in `meta.quota` and, when present, `X-Plan`, `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-Quota-Requests-Remaining` and `X-Quota-Exports-Remaining`. CSV and NDJSON exports also report `X-Export-Delivered`. See [shared quota and error guidance](https://github.com/fliarbi/prism-news-api/blob/main/docs/USER_GUIDE.md#quotas-errors-and-retry).

## Endpoint reference

All `/v1` endpoints require a key. Common news filters and business extras are defined above; the summary models intentionally exclude listing controls.

| Method and path | Accepted inputs / result |
|---|---|
| `GET/POST /v1/business/headlines` | News filters plus `company`, `event_type`; 100 headline items by default with `events`, cursor pagination. |
| `GET/POST /v1/business/themes` | News filters plus `company`, `event_type`; specific `q` required, default/max 5 suggestions, no cursor. |
| `GET/POST /v1/business/sentiment` | News filters plus `company`, `event_type`, `granularity`; label/group distribution and timeline. |
| `GET/POST /v1/business/trends` | News filters plus `company`, `event_type`, `granularity`; article volume series. |
| `GET/POST /v1/business/events` | `q`, `company` domain, `event_type`, dates, `limit`, `sort=newest\|oldest`, `cursor`, `resolve`; events and `by_type`. |
| `GET/POST /v1/business/funding` | `q`, `company`, `sector`, `round_type`, `min_amount_usd`, `investor`, `country`, dates, `limit`, `sort=newest\|oldest\|amount`, `cursor`; deals and totals. |
| `GET /v1/business/companies/{domain}/news` | Domain plus news filters; dates and limit apply to all three blocks. Continue each block through its own listing. |
| `GET/POST /v1/business/overview` | News filters plus `company`, `event_type` and funding filters; no listing controls or granularity. News, event and funding totals in one bounded window. |
| `GET/POST /v1/business/event-trends` | News filters plus `company`, `event_type`, `granularity`; no funding filters or listing controls. Full-window event totals and series. |
| `GET/POST /v1/business/funding/summary` | News filters plus `company`, `event_type`, funding filters and `granularity`; no listing controls. Full-window deal/amount totals and series. |
| `POST /v1/export` | General news filters plus `format=json\|ndjson\|csv`; no implicit business scope or business-only filters. 100 full articles by default; cap depends on your plan. |
| `GET /v1/articles/{article_id}` | Full source article; one export allowance on delivery. |
| `GET /v1/classes` | `q` or nonroot `prefix`, `limit=1–5` (default 5); bounded GCP code search. |
| `GET /v1/classes/{code}` | Code detail, at most five children, no theme suggestions. Code `0` is valid. |
| `GET /v1/classes/{code}/headlines` | Common news filters and a GCP code; 100 headlines by default. Metered. |
| `GET /v1/vocabulary` | Static public sentiment/priority and request options; plan metadata, no dynamic dictionary. |
| `GET /v1/me` | Key summary, access limits and usage. |
| `GET /v1/status` | Public availability and freshness with the publisher-supplied description of the news data. |

`GET /healthz` is a liveness check without a key. `GET /guide` serves this guide as Markdown. `/docs` and `/v1/openapi.json` are the interactive and machine-readable references for the supplied access environment. General news exploration routes are available on the News API base URL, not implied by the business base URL.
