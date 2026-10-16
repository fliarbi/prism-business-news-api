# Quarterly Results: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “quarterly results” · 12,100/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [quarterly-results.json](../../examples/scenarios/quarterly-results.json).

**Question.** How many quarterly results events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `earnings` and the word “quarter” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 40,072 |
| Companies (with a domain) | 9,514 |
| Source articles | 38,220 |
| Busiest month | Feb 2026 (5,417 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 16% · 1.0% · 83% of 13,762 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 5,292 | ████████████████████ |
| Jun 2025 | 841 | ███ |
| Jul 2025 | 3,266 | ████████████ |
| Aug 2025 | 4,903 | ██████████████████ |
| Sep 2025 | 1,464 | █████ |
| Oct 2025 | 3,820 | ██████████████ |
| Nov 2025 | 4,400 | ████████████████ |
| Dec 2025 | 1,020 | ████ |
| Jan 2026 | 3,818 | ██████████████ |
| Feb 2026 | 5,417 | ████████████████████ |
| Mar 2026 | 1,707 | ██████ |
| Apr 2026 | 4,124 | ███████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 5 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | lillyinsulinedu.com | Earnings | The company reported $8.55 EPS for the quarter, topping the consensus estimate of $7.26 by $1.29. Eli Lilly and Company had revenue of $19.80… | article unavailable |
| 30 Apr 2026 | illumina.com | Earnings | Illumina (NASDAQ:ILMN – Get Free Report) posted its earnings results on Thursday. The life sciences company reported $1.15 earnings per share (EPS)… | [Illumina (NASDAQ:ILMN) Releases Earnings Results, Beats Estimates By…](https://www.tickerreport.com/banking-finance/13424267/illumina-nasdaqilmn-releases-earnings-results-beats-estimates-by-0-10-eps.html) · tickerreport.com |
| 30 Apr 2026 | brunswickgroup.com | Earnings | The company reported $0.70 earnings per share for the quarter, missing analysts’ consensus estimates of $1.53 by ($0.83). The company’s quarterly… | [Brunswick (NYSE:BC) Updates FY 2026 Earnings Guidance](https://baseballnewssource.com/2026/04/30/brunswick-nysebc-updates-fy-2026-earnings-guidance/11105196.html) · baseballnewssource.com |
| 30 Apr 2026 | five9.com | Earnings | The software maker reported $0.76 EPS for the quarter, beating analysts’ consensus estimates of $0.68 by $0.08, FiscalAI reports. Five9 had a net… | [Five9 (NASDAQ:FIVN) Releases Earnings Results, Beats Estimates By…](https://baseballnewssource.com/2026/04/30/five9-nasdaqfivn-releases-earnings-results-beats-estimates-by-0-08-eps/11105195.html) · baseballnewssource.com |
| 30 Apr 2026 | irhythmtech.com | Earnings | The company reported ($0.35) EPS for the quarter, topping analysts’ consensus estimates of ($0.66) by $0.31, and had revenue of $199.39 million for… | [iRhythm Technologies (NASDAQ:IRTC) Issues Earnings Results, Beats…](https://baseballnewssource.com/2026/04/30/irhythm-technologies-nasdaqirtc-issues-earnings-results-beats-estimates-by-0-31-eps/11105193.html) · baseballnewssource.com |
| 30 Apr 2026 | brunswickgroup.com | Earnings | The company reported $0.70 earnings per share (EPS) for the quarter, missing analysts’ consensus estimates of $1.53 by ($0.83). | [Brunswick (NYSE:BC) Releases Q2 2026 Earnings Guidance](https://www.thelincolnianonline.com/2026/04/30/brunswick-nysebc-releases-q2-2026-earnings-guidance.html) · thelincolnianonline.com |
| 30 Apr 2026 | theensigngroup.com | Earnings | The Ensign Group (NASDAQ:ENSG – Get Free Report) announced its quarterly earnings data on Thursday. The company reported $1.85 earnings per share… | article unavailable |
| 30 Apr 2026 | orthopediatrics.com | Earnings | The company reported ($0.42) EPS for the quarter, beating the consensus estimate of ($0.44) by $0.02, FiscalAI reports. | article unavailable |
| 30 Apr 2026 | bancochile.cl | Earnings | The bank reported $0.57 EPS for the quarter, missing the consensus estimate of $0.58 by ($0.01), FiscalAI reports. | [Banco De Chile (NYSE:BCH) Posts Earnings Results, Misses Estimates…](https://www.tickerreport.com/banking-finance/13424255/banco-de-chile-nysebch-posts-earnings-results-misses-estimates-by-0-01-eps.html) · tickerreport.com |
| 30 Apr 2026 | fortive.com | Earnings | Fortive last released its earnings results on Thursday, April 30th. The technology company reported $0.70 earnings per share (EPS) for the quarter,… | article unavailable |
| 30 Apr 2026 | belden.com | Earnings | The firm had revenue of $696.38 million for the quarter, compared to analyst estimates of $678.11 million. | article unavailable |
| 30 Apr 2026 | apigroupinc.com | Earnings | The company reported $0.32 earnings per share for the quarter, topping analysts’ consensus estimates of $0.30 by $0.02, Briefing.com reports. | [APi Group (NYSE:APG) Announces Earnings Results, Beats Estimates By…](https://baseballnewssource.com/2026/04/30/api-group-nyseapg-announces-earnings-results-beats-estimates-by-0-02-eps/11105183.html) · baseballnewssource.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type earnings --q quarter --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type earnings --q quarter --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type earnings --q quarter --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["earnings"], "q": "quarter", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["earnings"], "q": "quarter", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Tech Layoffs](tech-layoffs.md)
- [Restructuring](restructuring.md)
- [FDA Approval](fda-approval.md)
- [Rights Issue](rights-issue.md)
