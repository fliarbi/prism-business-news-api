# Pharma Layoffs: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “pharma layoffs” · 40/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [pharma-layoffs.json](../../examples/scenarios/pharma-layoffs.json).

**Question.** How many pharma layoffs events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `layoffs` and the word “pharma” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 8 |
| Companies (with a domain) | 6 |
| Source articles | 8 |
| Busiest month | Sep 2025 (3 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 79% · 0.0% · 21% of 14 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 0 |  |
| Jun 2025 | 0 |  |
| Jul 2025 | 1 | ███████ |
| Aug 2025 | 1 | ███████ |
| Sep 2025 | 3 | ████████████████████ |
| Oct 2025 | 1 | ███████ |
| Nov 2025 | 0 |  |
| Dec 2025 | 0 |  |
| Jan 2026 | 0 |  |
| Feb 2026 | 1 | ███████ |
| Mar 2026 | 0 |  |
| Apr 2026 | 1 | ███████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 1 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 14 Apr 2026 | astellas.com | Layoffs | Tokyo-based Astellas Pharma will close the Seattle office of Universal Cells, its wholly owned subsidiary that creates engineered, allogeneic stem… | [50 employees impacted as Astellas closes Universal Cells' Seattle…](https://www.biospace.com/job-trends/50-employees-impacted-as-astellas-closes-universal-cells-seattle-office) · biospace.com |
| 17 Feb 2026 | marburg-immobilien.de | Layoffs | If it remains with the known figures, Marburg will count at least 1000 digits less on the Pharma Campus in a few months than half a year ago. | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type layoffs --q pharma --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type layoffs --q pharma --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type layoffs --q pharma --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["layoffs"], "q": "pharma", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["layoffs"], "q": "pharma", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [New Factory](new-factory.md)
- [Semiconductor Plant](semiconductor-plant.md)
- [Antitrust Lawsuit](antitrust-lawsuit.md)
- [Bank Layoffs](bank-layoffs.md)
