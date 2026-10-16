# It Layoffs: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “it layoffs” · 1,900/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [it-layoffs.json](../../examples/scenarios/it-layoffs.json).

**Question.** How many it layoffs events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `layoffs` and the word “IT” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 666 |
| Companies (with a domain) | 509 |
| Source articles | 625 |
| Busiest month | Oct 2025 (86 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 83% · 0.2% · 17% of 508 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 60 | ██████████████ |
| Jun 2025 | 34 | ████████ |
| Jul 2025 | 57 | █████████████ |
| Aug 2025 | 59 | ██████████████ |
| Sep 2025 | 57 | █████████████ |
| Oct 2025 | 86 | ████████████████████ |
| Nov 2025 | 55 | █████████████ |
| Dec 2025 | 38 | █████████ |
| Jan 2026 | 39 | █████████ |
| Feb 2026 | 83 | ███████████████████ |
| Mar 2026 | 39 | █████████ |
| Apr 2026 | 59 | ██████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 8 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | wrenkitchens.com | Layoffs | The company says the move, which has resulted in job losses and store closures, will enable it to channel investment into its UK business, which… | [Wren Kitchens' Barton HQ unaffected by US closure and bankruptcy](https://www.business-live.co.uk/retail-consumer/wren-kitchens-confirms-barton-head-33867304) · business-live.co.uk |
| 30 Apr 2026 | faradaypharma.com | Layoffs | In February, Faraday Pharmaceuticals announced it had ceased operations and was winding down its business. | article unavailable |
| 29 Apr 2026 | vidrala.com | Layoffs | Vidrala announced this Wednesday that it is carrying out a 10% cut of its workforce in the UK and Ireland despite it hopes to have a good year… | [Vidrala recortará su plantilla en Reino Unido e Irlanda pese a que…](https://www.expansion.com/pais-vasco/2026/04/29/69f201f7e5fdeaa1788b4587.html) · expansion.com |
| 28 Apr 2026 | forvismazars.com | Layoffs | The firm informed affected staff last week it would be letting go of roughly 250 people, or 3% of its U.S. workforce totaling more than 7,700, the… | [Layoff Watch '26: Forvis Mazars Cuts 3% of the Workforce in Unusual…](https://www.goingconcern.com/layoff-watch-26-forvis-mazars-cuts-3-of-the-workforce-in-unusual-post-busy-season-culling/) · goingconcern.com |
| 28 Apr 2026 | rogers.com | Layoffs | Rogers said Monday it is offering voluntary departure and retirement packages to an undisclosed number of its employees, with Bloomberg reporting… | article unavailable |
| 25 Apr 2026 | metavision.com ⚠ check link: not Meta's domain | Layoffs | Meta has also confirmed it plans to cut 10 percent of its workforce and walk away from 6,000 roles it had been looking to fill. | article unavailable |
| 24 Apr 2026 | nike.com | Layoffs | Nike announced that it will fire about 1,400 people, focusing on technology, as part of a new restructuring phase. | article unavailable |
| 24 Apr 2026 | kpmgspark.com | Layoffs | KPMG is reducing its senior workforce in the US, with close to 100 audit partners set to leave the firm as it looks to rebalance its team structure. | [KPMG cuts 100 audit partner roles, says need to align team skills…](https://www.indiatoday.in/jobs/story/kpmg-cuts-100-jobs-says-need-to-align-team-skills-and-size-tchc-2900853-2026-04-24) · indiatoday.in |
| 24 Apr 2026 | maverickgaming.com | Layoffs | Maverick Gaming will lay off about 65 employees as it proceeds with the closure of its Silver Dollar SeaTac Casino in Washington, according to a… | article unavailable |
| 23 Apr 2026 | fedex.com | Layoffs | In December, after a major client pulled the plug on its Coppell logistics service, FedEx told state authorities it was closing the operation and… | [North Texas Job Market Shifts From Boom to Standstill](https://www.governing.com/workforce/north-texas-job-market-shifts-from-boom-to-standstill) · governing.com |
| 23 Apr 2026 | spicejet.com | Layoffs | It desperately needs capital infusion, is trying to lay off at least 15% of its 6,000-strong employee base, and is struggling for survival. | article unavailable |
| 23 Apr 2026 | microsoft.com | Layoffs | The software giant plans to make the offers in early May to about 8,750 people, or 7% of its U.S. workforce, according to two people familiar with… | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type layoffs --q IT --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type layoffs --q IT --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type layoffs --q IT --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["layoffs"], "q": "IT", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["layoffs"], "q": "IT", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Article filters require a matching source article in the same window; records without a matching article are excluded. Each deal still counts once.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.
- Zero-count periods are included; partial_period marks buckets only partly covered by the window.
- shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)

## Related demonstrations

- [Job Cuts](job-cuts.md)
- [Strategic Partnership](strategic-partnership.md)
- [New Product Launch](new-product-launch.md)
- [Dividend Announcement](dividend-announcement.md)
