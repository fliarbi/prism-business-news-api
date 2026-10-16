# Tech Layoffs: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “tech layoffs” · 3,600/month India · 14,800/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [tech-layoffs.json](../../examples/scenarios/tech-layoffs.json).

**Question.** How many tech layoffs events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `layoffs` and the word “tech” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 56 |
| Companies (with a domain) | 36 |
| Source articles | 55 |
| Busiest month | Apr 2026 (12 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 88% · 0.0% · 12% of 154 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 3 | █████ |
| Jun 2025 | 4 | ███████ |
| Jul 2025 | 6 | ██████████ |
| Aug 2025 | 4 | ███████ |
| Sep 2025 | 6 | ██████████ |
| Oct 2025 | 5 | ████████ |
| Nov 2025 | 4 | ███████ |
| Dec 2025 | 4 | ███████ |
| Jan 2026 | 2 | ███ |
| Feb 2026 | 3 | █████ |
| Mar 2026 | 3 | █████ |
| Apr 2026 | 12 | ████████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 7 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | aws.amazon.com | Layoffs | Amazon Web Services (AWS) CEO Matt Garman has addressed the internal shifts within the tech giant, clarifying the strategy behind the recent Amazon… | article unavailable |
| 24 Apr 2026 | superops.com | Layoffs | Enterprise tech startup SuperOps has laid off around 60 employees as part of a restructuring exercise aimed at improving efficiency and accelerating… | [SuperOps Lays Off 30% Staff In AI-Led Restructuring Push](https://inc42.com/buzz/superops-lays-off-30-staff-in-ai-led-restructuring-push/) · inc42.com |
| 24 Apr 2026 | microsoft.com | Layoffs | Meanwhile, the layoff wave sweeping through Big Tech showed no signs of slowing, with Meta and Microsoft both announcing fresh cuts this week. | [Launched This Week: JBL Bar series, Dyson Supersonic Travel and 3…](https://www.indiatoday.in/technology/features/story/launched-this-week-jbl-bar-series-dyson-supersonic-travel-and-3-more-devices-to-check-out-2901139-2026-04-24) · indiatoday.in |
| 24 Apr 2026 | microsoft.com | Layoffs | Also on Thursday, US media reported that tech giant Microsoft was planning to offer voluntary early retirement buyouts for around 8.700 workers, or… | article unavailable |
| 24 Apr 2026 | techmahindra.com | Layoffs | Tech Mahindra’s headcount fell by 1,108. | [AI Boom, Job Bust: Meta, Microsoft Eye 23,000 Cuts as Hiring Slows…](https://www.outlookbusiness.com/corporate/ai-boom-job-bust-meta-microsoft-eye-23000-cuts-as-hiring-slows-across-tech) · outlookbusiness.com |
| 10 Apr 2026 | opel.com | Layoffs | The workforce at the Tech Center is shrinking from currently 1650 to 1000 engineers. | [Kahlschlag bei Opel: Diese Stellen baut Stellantis jetzt ab](https://de.finance.yahoo.com/nachrichten/kahlschlag-opel-diese-stellen-baut-145902996.html) · de.finance.yahoo.com |
| 10 Apr 2026 | oracle.com | Layoffs | According to state records, the tech giant plans to cut around 700 jobs in California by the first of June. | article unavailable |
| 9 Apr 2026 | pendo.io | Layoffs | April 7: Pendo cuts 10% of workforce Raleigh, N.C.-based tech startup Pendo, with a valuation of more than $1 billion, has laid off 90 of its 850… | [2026 tech company layoffs](https://informationweek.com/it-staffing-careers/2026-tech-company-layoffs) · informationweek.com |
| 9 Apr 2026 | techmahindra.com | Layoffs | Tech Mahindra, which is working to turn around its fortune, has reported a reduction of over 3,500 employees in the past three quarters. | article unavailable |
| 9 Apr 2026 | oracle.com | Layoffs | On Tuesday, it was announced that some 700 workers at another Bay Area tech company, Oracle, would be out of work by June statewide. | article unavailable |
| 9 Apr 2026 | oracle.com | Layoffs | On Tuesday, it was announced that some 700 workers at another Bay Area tech company, Oracle, would be out of work by June statewide. The statewide… | article unavailable |
| 2 Apr 2026 | meta.com | Layoffs | Meta Platforms has decided to slash almost 200 jobs in the Bay Area, marking the tech company’s most recent downsizing in the region, a state… | [Meta to eliminate nearly 200 Bay Area jobs](https://www.siliconvalley.com/2026/04/02/economy-jobs-tech-facebook-meta-layoff-work-ai-bay-area-sunnyvale/) · siliconvalley.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type layoffs --q tech --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type layoffs --q tech --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type layoffs --q tech --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["layoffs"], "q": "tech", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["layoffs"], "q": "tech", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [SME IPO](sme-ipo.md)
- [Share Buyback](share-buyback.md)
- [Restructuring](restructuring.md)
- [Quarterly Results](quarterly-results.md)
