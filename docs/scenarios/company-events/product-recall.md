# Product Recall: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “product recall” · 2,400/month India · 368,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [product-recall.json](../../examples/scenarios/product-recall.json).

**Question.** How many product recall events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `company_announcement`, `regulatory` and the word “recall” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 12 |
| Companies (with a domain) | 10 |
| Source articles | 12 |
| Busiest month | Nov 2025 (4 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 75% · 0.0% · 25% of 4 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Announcement | Regulatory |  |
| --- | ---: | ---: | ---: | --- |
| May 2025 | 0 | 0 | 0 |  |
| Jun 2025 | 0 | 0 | 0 |  |
| Jul 2025 | 1 | 1 | 0 | █████ |
| Aug 2025 | 3 | 1 | 2 | ███████████████ |
| Sep 2025 | 0 | 0 | 0 |  |
| Oct 2025 | 0 | 0 | 0 |  |
| Nov 2025 | 4 | 3 | 1 | ████████████████████ |
| Dec 2025 | 1 | 1 | 0 | █████ |
| Jan 2026 | 0 | 0 | 0 |  |
| Feb 2026 | 3 | 3 | 0 | ███████████████ |
| Mar 2026 | 0 | 0 | 0 |  |
| Apr 2026 | 0 | 0 | 0 |  |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 1 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 20 Feb 2026 | gm.com | Announcement | GM struck a deal in 2021 with the battery manufacturer to recover $1.9 billion of the $2 billion in costs for a recall of batteries in the Bolt EVs. | article unavailable |
| 13 Feb 2026 | spirit.com | Announcement | Spirit Airlines on Thursday moved to recall 500 of the more than 1,300 flight attendants who were furloughed in December due to its ongoing… | [Spirit Airlines to sell 20 jets, recalls furloughed flight…](https://nypost.com/2026/02/13/business/spirit-airlines-to-sell-20-jets-recalls-furloughed-flight-attendants/) · nypost.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type company_announcement --event-type regulatory --q recall --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type company_announcement --event-type regulatory --q recall --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type company_announcement --event-type regulatory --q recall --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["company_announcement", "regulatory"], "q": "recall", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["company_announcement", "regulatory"], "q": "recall", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Article filters require a matching source article in the same window; records without a matching article are excluded. Each deal still counts once.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.
- Zero-count periods are included; partial_period marks buckets only partly covered by the window.
- shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)

## Related demonstrations

- [IPO](ipo.md)
- [Upcoming IPO](upcoming-ipo.md)
- [Layoffs](layoffs.md)
- [Lawsuit](lawsuit.md)
