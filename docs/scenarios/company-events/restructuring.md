# Restructuring: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “restructuring” · 6,600/month India · 8,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [restructuring.json](../../examples/scenarios/restructuring.json).

**Question.** How many restructuring events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `company_announcement` and the word “restructuring” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 340 |
| Companies (with a domain) | 192 |
| Source articles | 329 |
| Busiest month | Oct 2025 (44 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 39% · 2.4% · 59% of 125 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 19 | █████████ |
| Jun 2025 | 28 | █████████████ |
| Jul 2025 | 24 | ███████████ |
| Aug 2025 | 30 | ██████████████ |
| Sep 2025 | 38 | █████████████████ |
| Oct 2025 | 44 | ████████████████████ |
| Nov 2025 | 28 | █████████████ |
| Dec 2025 | 27 | ████████████ |
| Jan 2026 | 23 | ██████████ |
| Feb 2026 | 35 | ████████████████ |
| Mar 2026 | 17 | ████████ |
| Apr 2026 | 27 | ████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 2 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | drax.com | Announcement | In February Drax confirmed a major restructuring which will lead to 350 redundancies as part of plans to build “a strong, resilient business for the… | [Drax hails good performance as it 'supports UK energy at a critical…](https://www.business-live.co.uk/economic-development/drax-hails-good-performance-supports-33866317) · business-live.co.uk |
| 29 Apr 2026 | ups.com | Announcement | United Parcel Service plans to close an additional 27 parcel distribution centers this year as the company continues its aggressive cost… | article unavailable |
| 29 Apr 2026 | adstec-energy.com | Announcement | 2025 marked a transition year, with ADS-TEC Energy restructuring its sales approach, prioritizing higher-quality projects and expanding recurring… | [Where flexibility becomes a business model: ADS-TEC Energy releases…](https://ads-tec-com.mynewsdesk.com/pressreleases/where-flexibility-becomes-a-business-model-ads-tec-energy-releases-updated-investor-presentation-3445668) · ads-tec-com.mynewsdesk.com |
| 27 Apr 2026 | unitedrentals.com | Announcement | The company did some restructuring with some facility consolidation, and improved operational efficiency yielded estimated cost benefits. | [Specialty Rental, Big Projects Continue Strong in United Rentals’…](http://rermag.com/news-analysis/headline-news/article/55373515/specialty-rental-big-projects-continue-strong-in-united-rentals-first-quarter-flannery-says) · rermag.com |
| 25 Apr 2026 | hzlindia.com | Announcement | Talks about a potential demerger could resume once parent Vedanta completes its own restructuring. | [Hindustan Zinc Eyes Capacity Doubling by 2030, Demerger Talks May…](https://www.outlookbusiness.com/corporate/hindustan-zinc-eyes-capacity-doubling-by-2030-demerger-talks-may-resume) · outlookbusiness.com |
| 23 Apr 2026 | agilyx.com | Announcement | The same month, Agilyx transferred ownership of a Houston plastics sorting center to partners LyondellBasell and ExxonMobil as part of a… | [LyondellBasell upgrade to PreZero assets on hold](https://resource-recycling.com/plastics/2026/04/23/lyondellbasell-upgrade-to-prezero-assets-on-hold/) · resource-recycling.com |
| 22 Apr 2026 | speedcast.com | Announcement | As of late 2025, Speedcast is undergoing a significant financial restructuring, with S&P Global Ratings reporting a “Negative” outlook due to free… | [Speedcast claims business rise of 50% in Q1](https://www.advanced-television.com/2026/04/22/speedcast-claims-business-rise-of-50-in-q1/) · advanced-television.com |
| 21 Apr 2026 | sktelecom.com | Announcement | He also highlighted a restructuring of corporate culture. | [SKT chief targets B2B AI push](https://www.mobileworldlive.com/asia-pacific/skt-chief-targets-b2b-ai-push/) · mobileworldlive.com |
| 18 Apr 2026 | vietravelairlines.com | Announcement | Currently part of the ecosystem of T&T Group, Vietravel Airlines is undergoing restructuring and strengthening its operations. | [Vietravel Airlines adds new aircraft, plans fleet expansion](https://vietnamnews.vn/bizhub/1779729/vietravel-airlines-adds-new-aircraft-plans-fleet-expansion.html) · vietnamnews.vn |
| 17 Apr 2026 | honda.co.jp | Announcement | Honda Motor Co. is restructuring its China business as it navigates declining sales and intensifying competition from domestic electric vehicle (EV)… | [Honda scales back China operations amid weak sales and EV transition…](https://www.domain-b.com/industry/industry-general/honda-china-restructuring-ev-shift-2026) · domain-b.com |
| 17 Apr 2026 | suzlon.com | Announcement | Suzlon has reported progress in strengthening its financial position in recent years through: Debt reduction and restructuring efforts Improved cash… | article unavailable |
| 15 Apr 2026 | clearwaterpaper.com | Announcement | US cartonboard producer Clearwater Paper Corporation has announced the restructuring of its Cypress Bend mill in Arkansas. | [Clearwater Paper to reduce board production in Arkansas](https://www.euwid-paper.com/news/companies/clearwater-paper-to-reduce-board-production-in-arkansas-150426/) · euwid-paper.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type company_announcement --q restructuring --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type company_announcement --q restructuring --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type company_announcement --q restructuring --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["company_announcement"], "q": "restructuring", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["company_announcement"], "q": "restructuring", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Share Buyback](share-buyback.md)
- [Tech Layoffs](tech-layoffs.md)
- [Quarterly Results](quarterly-results.md)
- [FDA Approval](fda-approval.md)
