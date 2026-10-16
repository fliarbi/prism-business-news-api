# Layoffs: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “layoffs” · 90,500/month India · 165,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [layoffs.json](../../examples/scenarios/layoffs.json).

**Question.** How many layoffs events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `layoffs`.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 4,005 |
| Companies (with a domain) | 2,122 |
| Source articles | 3,518 |
| Busiest month | Apr 2026 (419 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 83% · 0.6% · 17% of 1,242 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 340 | ████████████████ |
| Jun 2025 | 233 | ███████████ |
| Jul 2025 | 353 | █████████████████ |
| Aug 2025 | 346 | █████████████████ |
| Sep 2025 | 383 | ██████████████████ |
| Oct 2025 | 399 | ███████████████████ |
| Nov 2025 | 317 | ███████████████ |
| Dec 2025 | 213 | ██████████ |
| Jan 2026 | 286 | ██████████████ |
| Feb 2026 | 394 | ███████████████████ |
| Mar 2026 | 322 | ███████████████ |
| Apr 2026 | 419 | ████████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 8 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | saks.global | Layoffs | Saks Global is slashing the headcount at its corporate headquarters by 16 percent, impacting a wide spectrum of positions. | [Saks Global Triggers Corporate Layoffs](https://wwd.com/business-news/retail/saks-global-sets-more-layoffs-at-corporate-office-1238935066/) · wwd.com |
| 30 Apr 2026 | bbva.es | Layoffs | BBVA CEO Onur Gen , has clarified that the voluntary departure of approximately 750 employees of the group in the first quarter of 2026 is not… | article unavailable |
| 30 Apr 2026 | wrenkitchens.com | Layoffs | The company says the move, which has resulted in job losses and store closures, will enable it to channel investment into its UK business, which… | [Wren Kitchens' Barton HQ unaffected by US closure and bankruptcy](https://www.business-live.co.uk/retail-consumer/wren-kitchens-confirms-barton-head-33867304) · business-live.co.uk |
| 30 Apr 2026 | somfysystems.com | Layoffs | the job safeguard plan (PES) announced in February, which provides for up to 534 job deletions in France, or 20%. | [PSE chez Somfy : les syndicats dénoncent la rémunération des…](https://www.lejournaldesentreprises.com/article/pse-chez-somfy-les-syndicats-denoncent-la-remuneration-des-actionnaires-2142135) · lejournaldesentreprises.com |
| 30 Apr 2026 | quixote.com | Layoffs | About 70 jobs will be cut across Atlanta and Los Angeles. | [Amid decline in film production, equipment rental company exits…](https://www.ajc.com/business/2026/04/amid-decline-in-film-production-equipment-rental-company-exits-atlanta/) · ajc.com |
| 30 Apr 2026 | metavision.com ⚠ check link: not Meta's domain | Layoffs | Sama said would result in 1,108 workers being made redundant. | article unavailable |
| 30 Apr 2026 | whitbread.co.uk | Layoffs | This operational shift is driving the painful reduction of approximately 3,800 jobs | [Premier Inn owner Whitbread (LON: WTB) has announced a major…](https://www.asktraders.com/analysis/whitbread-five-year-overhaul/) · asktraders.com |
| 30 Apr 2026 | mediapro.com | Layoffs | Grup Mediapro confirms the dismissal of 189 workers, a figure 'below the expected' by the previous 'unlinking' of about twenty managers and savings… | [Mediapro defiende su ERE de 189 personas como paso necesario para…](https://www.panoramaaudiovisual.com/2026/04/30/mediapro-defiende-re-189-personas-paso-necesario-competir-sector/) · panoramaaudiovisual.com |
| 30 Apr 2026 | aws.amazon.com | Layoffs | Amazon Web Services (AWS) CEO Matt Garman has addressed the internal shifts within the tech giant, clarifying the strategy behind the recent Amazon… | article unavailable |
| 30 Apr 2026 | hmgroup.com | Layoffs | Earlier, plans had emerged to close the site and cut 440 jobs. | [H&M is working on a rescue plan for its Ghlin warehouse -…](https://www.retaildetail.eu/news/fashion/hm-is-working-on-a-rescue-plan-for-its-ghlin-warehouse/) · retaildetail.eu |
| 30 Apr 2026 | rampartbio.com | Layoffs | In January, news broke that La Jolla, California–based Rampart Bioscience had ended operations. | article unavailable |
| 30 Apr 2026 | faradaypharma.com | Layoffs | In February, Faraday Pharmaceuticals announced it had ceased operations and was winding down its business. | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type layoffs --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type layoffs --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type layoffs --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["layoffs"], "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["layoffs"], "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Upcoming IPO](upcoming-ipo.md)
- [Product Recall](product-recall.md)
- [Lawsuit](lawsuit.md)
- [Stock Split](stock-split.md)
