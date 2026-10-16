# Demerger: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “demerger” · 5,400/month India · 390/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [demerger.json](../../examples/scenarios/demerger.json).

**Question.** How many demerger events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `company_announcement`, `ma` and the word “demerger” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 27 |
| Companies (with a domain) | 21 |
| Source articles | 25 |
| Busiest month | Jul 2025 (5 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 0.0% · 0.0% · 100% of 3 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Announcement | M&A |  |
| --- | ---: | ---: | ---: | --- |
| May 2025 | 0 | 0 | 0 |  |
| Jun 2025 | 0 | 0 | 0 |  |
| Jul 2025 | 5 | 4 | 1 | ████████████████████ |
| Aug 2025 | 2 | 1 | 1 | ████████ |
| Sep 2025 | 3 | 1 | 2 | ████████████ |
| Oct 2025 | 5 | 4 | 1 | ████████████████████ |
| Nov 2025 | 3 | 1 | 2 | ████████████ |
| Dec 2025 | 1 | 1 | 0 | ████ |
| Jan 2026 | 2 | 1 | 1 | ████████ |
| Feb 2026 | 2 | 2 | 0 | ████████ |
| Mar 2026 | 3 | 0 | 3 | ████████████ |
| Apr 2026 | 1 | 1 | 0 | ████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 4 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 25 Apr 2026 | hzlindia.com | Announcement | Talks about a potential demerger could resume once parent Vedanta completes its own restructuring. | [Hindustan Zinc Eyes Capacity Doubling by 2030, Demerger Talks May…](https://www.outlookbusiness.com/corporate/hindustan-zinc-eyes-capacity-doubling-by-2030-demerger-talks-may-resume) · outlookbusiness.com |
| 24 Mar 2026 | talktalkbusiness.co.uk | M&A | TalkTalk Business has acquired Oxfordshire-based Planet IT, as part of its plans to expand its managed services and cyber, following its demerger… | article unavailable |
| 24 Mar 2026 | planet-limited.com | M&A | TalkTalk Business has acquired Oxfordshire-based Planet IT, as part of its plans to expand its managed services and cyber, following its demerger… | article unavailable |
| 18 Mar 2026 | unilever.com | M&A | The open offer was triggered pursuant to the share purchase agreement executed between certain Magnum entities and Unilever entities whereby Magnum… | [Khaitan & Co advises Magnum Ice Cream Company on stake acquisition…](https://www.barandbench.com/dealstreet/khaitan-co-advises-magnum-ice-cream-company-on-stake-acquisition-in-kwality-walls) · barandbench.com |
| 16 Feb 2026 | religare.com | Announcement | Religare Enterprises: The boards of Religare Enterprises and Religare Finvest have approved a demerger to separate the financial services and… | [Stocks in Focus: Garden Reach Shipbuilder, Hindustan Copper, and…](https://www.equitypandit.com/stocks-in-focus-garden-reach-shipbuilder-hindustan-copper-and-others/) · equitypandit.com |
| 6 Feb 2026 | kongsberg.com | Announcement | Later today, you will also have the opportunity to follow company presentations of Kongsberg Maritime and Kongsberg following the demerger -- the… | article unavailable |
| 14 Jan 2026 | dlfcybercity.com | M&A | This was followed by the amalgamation of DLF City Centre Limited, DLF Lands India Private Limited, DLF Info City Developers (Kolkata) Limited, and… | article unavailable |
| 2 Jan 2026 | samsungbiologics.com | Announcement | Rim pointed to last year’s milestones as groundwork for the next phase, citing the company’s completed demerger, the securing of land for a third… | [Samsung Biologics CEO lays out 2026 strategy as competition…](https://www.koreabiomed.com/news/articleView.html?idxno=30163) · koreabiomed.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type company_announcement --event-type ma --q demerger --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type company_announcement --event-type ma --q demerger --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type company_announcement --event-type ma --q demerger --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["company_announcement", "ma"], "q": "demerger", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["company_announcement", "ma"], "q": "demerger", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Rights Issue](rights-issue.md)
- [AI Layoffs](ai-layoffs.md)
- [IPO India](ipo-india.md)
- [Q4 Results](q4-results.md)
