# Toyota News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “toyota news” · 390/month India · 8,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [toyota-news.json](../../examples/scenarios/toyota-news.json).

**Question.** What has the news reported about Toyota in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `toyota.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `toyota.com` |
| Headlines, Jan – Apr 2026 (estimate) | 1 |
| Events, May 2025 – Apr 2026 | 10 |
| Most frequent event types | Announcement (3), Capital infusion (3), Key people (2) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 0.0% · 0.0% · 100% of 1 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Announcement | 3 |
| Capital infusion | 3 |
| Key people | 2 |
| Contracts | 1 |
| Job creation | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Announcement | Capital infusion | Key people | Contracts |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1 | 0 | 0 | 0 | 1 | ███████ |
| Jun 2025 | 1 | 0 | 0 | 1 | 0 | ███████ |
| Jul 2025 | 0 | 0 | 0 | 0 | 0 |  |
| Aug 2025 | 0 | 0 | 0 | 0 | 0 |  |
| Sep 2025 | 0 | 0 | 0 | 0 | 0 |  |
| Oct 2025 | 0 | 0 | 0 | 0 | 0 |  |
| Nov 2025 | 3 | 0 | 2 | 0 | 0 | ████████████████████ |
| Dec 2025 | 3 | 3 | 0 | 0 | 0 | ████████████████████ |
| Jan 2026 | 0 | 0 | 0 | 0 | 0 |  |
| Feb 2026 | 2 | 0 | 1 | 1 | 0 | █████████████ |
| Mar 2026 | 0 | 0 | 0 | 0 | 0 |  |
| Apr 2026 | 0 | 0 | 0 | 0 | 0 |  |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 1 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 19 Feb 2026 | Key people | John Waldron has joined Toyota Motor North America as Group Manager – Executive Compensation and Compensation Strategy, where he will lead executive… | [John Waldron Joins Toyota Motor North America to Lead Executive…](https://hrtoday.in/john-waldron-joins-toyota-motor-north-america-to-lead-executive-compensation-and-compensation-strategy/) · hrtoday.in |
| 9 Feb 2026 | Capital infusion | At the Jackson facility, a $71.4 million investment will support three new production lines to increase output of hybrid transaxle cases, housings… | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company toyota.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company toyota.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company toyota.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company toyota.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/toyota.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "toyota.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.
- Zero-count periods are included; partial_period marks buckets only partly covered by the window.
- shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)

## Related demonstrations

- [Wipro News](wipro-news.md)
- [Ongc News](ongc-news.md)
- [Lucid News](lucid-news.md)
- [Uber News](uber-news.md)
