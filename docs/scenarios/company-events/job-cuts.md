# Job Cuts: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “job cuts” · 1,300/month India · 2,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [job-cuts.json](../../examples/scenarios/job-cuts.json).

**Question.** How many job cuts events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `layoffs` and the word “job cuts” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 138 |
| Companies (with a domain) | 108 |
| Source articles | 133 |
| Busiest month | Oct 2025 (19 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 91% · 0.0% · 9.4% of 212 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 12 | █████████████ |
| Jun 2025 | 9 | █████████ |
| Jul 2025 | 14 | ███████████████ |
| Aug 2025 | 11 | ████████████ |
| Sep 2025 | 11 | ████████████ |
| Oct 2025 | 19 | ████████████████████ |
| Nov 2025 | 10 | ███████████ |
| Dec 2025 | 5 | █████ |
| Jan 2026 | 10 | ███████████ |
| Feb 2026 | 15 | ████████████████ |
| Mar 2026 | 12 | █████████████ |
| Apr 2026 | 10 | ███████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 8 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 22 Apr 2026 | meta.com | Layoffs | Meta Platforms has laid off 2,000 employees this year in several rounds of job cuts. | [Meta Tracks Employee Mouse Clicks And Keystrokes To Train A.I.](https://www.baystreet.ca/techinsider/5515/Meta-Tracks-Employee-Mouse-Clicks-And-Keystrokes-To-Train-AI) · baystreet.ca |
| 20 Apr 2026 | manrolandsheetfed.com | Layoffs | Almost all of the 740 employees are affected by job cuts. | article unavailable |
| 17 Apr 2026 | amazon.com | Layoffs | Amazon followed with around 16,000 job cuts amid efforts to streamline operations and improve efficiency. | [Tech Layoffs Surge Globally: Job Cuts Across Sector Cross Over…](https://www.latestly.com/technology/tech-layoffs-surge-globally-job-cuts-across-sector-cross-over-80000-in-q1-as-tech-giants-shift-toward-ai-infrastructure-7396737.html) · latestly.com |
| 15 Apr 2026 | elma.care | Layoffs | The job cuts affect locations in Switzerland, Romania, Germany and the USA, as the company announced on Wednesday. A maximum of 50 jobs are to be… | article unavailable |
| 10 Apr 2026 | oracle.com | Layoffs | about 700 employees in California set to lose their jobs by June 1, and an additional 491 job cuts have already been reported in Seattle. | article unavailable |
| 10 Apr 2026 | life360.com | Layoffs | On Friday, another former ASX market darling in Life360 also flagged job cuts. | article unavailable |
| 9 Apr 2026 | hsbc.com | Layoffs | Meanwhile, another report said that global banking major HSBC is also considering job cuts over the coming years, as Chief Executive Officer Georges… | article unavailable |
| 8 Apr 2026 | oracle.com | Layoffs | Oracle is set to lay off 710 employees across California in the United States, with job cuts spanning the San Francisco Bay Area and Santa Monica,… | [Oracle to lay off 710 employees across California sites by June](https://www.peoplematters.in/news/strategic-hr/oracle-to-lay-off-710-employees-across-california-sites-by-june-49147) · peoplematters.in |
| 1 Apr 2026 | oracle.com | Layoffs | The US technology giant Oracle creates controversy after a wave of massive layoffs. A method considered brutal, revealing the changes in the… | [Oracle : jusqu’à 11 000 postes supprimés en un claquement de doigts](https://www.lerevenu.com/reussir-bourse/avis-des-pros/oracle-jusqu-a-11-000-postes-supprimes-en-un-claquement-de-doigts/) · lerevenu.com |
| 1 Apr 2026 | oracle.com | Layoffs | US-based IT firm Oracle on Tuesday laid off employees in India, with another round of job cuts expected within a month. | [From Oracle to Amazon: Tech layoffs sweep across global IT industry](https://www.business-standard.com/industry/news/global-tech-layoffs-oracle-tcs-amazon-microsoft-intel-meta-it-job-cut-126040100376_1.html) · business-standard.com |
| 30 Mar 2026 | home.kpmg | Layoffs | The move could result in up to 440 job cuts, according to a Bloomberg report, though final numbers remain subject to an ongoing consultation process. | article unavailable |
| 24 Mar 2026 | blueovalsk.com | Layoffs | A Worker Adjustment and Retraining Notification filed with the state indicates that job cuts affecting around 10% of the remaining workforce will… | [Ford Delays US Battery Plant Layoffs Amid EV Demand Slowdown](https://www.electronicsforyou.biz/industry-buzz/ford-delays-us-battery-plant-layoffs-amid-ev-demand-slowdown/) · electronicsforyou.biz |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type layoffs --q "job cuts" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type layoffs --q "job cuts" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type layoffs --q "job cuts" --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["layoffs"], "q": "job cuts", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["layoffs"], "q": "job cuts", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [IPO India](ipo-india.md)
- [Q4 Results](q4-results.md)
- [Strategic Partnership](strategic-partnership.md)
- [It Layoffs](it-layoffs.md)
