# Palantir News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “palantir news” · 260/month India · 9,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [palantir-news.json](../../examples/scenarios/palantir-news.json).

**Question.** What has the news reported about Palantir in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `palantir.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `palantir.com` |
| Headlines, Jan – Apr 2026 (estimate) | 2,356 |
| Events, May 2025 – Apr 2026 | 120 |
| Most frequent event types | Earnings (53), Contracts (31), Lawsuit (12) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 36% · 0.6% · 64% of 2,356 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 2 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Stagwell’s communications segment posts 5.3% Q1 organic net revenue increase](https://www.prweek.com/article/1956684/stagwells-communications-segment-posts-53-q1-organic-net-revenue-increase) | prweek.com | 5 | positive | Earnings |
| 30 Apr 2026 | [GC Wealth Management RIA LLC Cuts Stake in Palantir Technologies Inc. $PLTR](https://www.dailypolitical.com/2026/04/30/gc-wealth-management-ria-llc-cuts-stake-in-palantir-technologies-inc-pltr.html) | dailypolitical.com | 4 | positive | — |
| 30 Apr 2026 | [Polymarket adds Chainalysis tools to detect insider trading](https://cryptobriefing.com/polymarket-insider-trading-detection-tools/) | cryptobriefing.com | 8 | negative | — |
| 30 Apr 2026 | [Stagwell announces ‘strongest Q1 in 4 years’ in ‘pivotal’ moment for AI reposition](https://www.thedrum.com/news/stagwell-announces-strongest-q1-in-4-years-in-pivotal-moment-for-ai-reposition) | thedrum.com | 7 | positive | Earnings |
| 30 Apr 2026 | [Required Reading: Market Leadership Requires Market Engineering](https://www.destinationcrm.com/Articles/CRM-Insights/Insight/Required-Reading-Market-Leadership-Requires-Market-Engineering-174609.aspx) | destinationcrm.com | 5 | positive | — |
| 29 Apr 2026 | [Earnings To Watch: Wabash (WNC) Reports Q1 Results Tomorrow](https://www.theglobeandmail.com/investing/markets/stocks/WNC/pressreleases/1606688/earnings-to-watch-wabash-wnc-reports-q1-results-tomorrow/) | theglobeandmail.com | 5 | positive | — |
| 29 Apr 2026 | [Palantir's AI Moment: Why Analysts Predict An 11th Straight Quarter Of Growth - Palantir Technologies (NA](https://benzinga.com/analyst-stock-ratings/analyst-color/26/04/52133606/palantirs-ai-moment-why-analysts-predict-an-11th-straight-quarter-of-growth) | benzinga.com | 7 | negative | — |
| 29 Apr 2026 | [Northern Re to scale capital intelligence via Palantir platform selection - Artemis.bm](https://www.artemis.bm/news/northern-re-to-scale-capital-intelligence-via-palantir-platform-selection/) | artemis.bm | 7 | positive | Contracts |
| 29 Apr 2026 | [Pentagon inks deal with Google for AI services](https://www.nbclosangeles.com/news/national-international/pentagon-deal-google-ai-services/3883385/) | nbclosangeles.com | 8 | positive | — |
| 29 Apr 2026 | [Cleveland-Cliffs partners with Palantir on AI-driven steelmaking](https://www.manufacturingdive.com/news/cleveland-cliffs-partners-palantir-ai-steelmaking/818800/) | manufacturingdive.com | 7 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 53 |
| Contracts | 31 |
| Lawsuit | 12 |
| Announcement | 10 |
| Job creation | 4 |
| New product | 3 |
| Key people | 2 |
| M&A | 2 |
| Regulatory | 2 |
| Incorporation | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Contracts | Lawsuit | Announcement |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 9 | 8 | 1 | 0 | 0 | ████████ |
| Jun 2025 | 1 | 0 | 1 | 0 | 0 | █ |
| Jul 2025 | 4 | 2 | 1 | 1 | 0 | ███ |
| Aug 2025 | 13 | 8 | 3 | 0 | 2 | ███████████ |
| Sep 2025 | 6 | 0 | 1 | 0 | 1 | █████ |
| Oct 2025 | 17 | 4 | 4 | 6 | 1 | ██████████████ |
| Nov 2025 | 9 | 9 | 0 | 0 | 0 | ████████ |
| Dec 2025 | 13 | 3 | 6 | 1 | 1 | ███████████ |
| Jan 2026 | 6 | 0 | 4 | 2 | 0 | █████ |
| Feb 2026 | 24 | 13 | 3 | 0 | 5 | ████████████████████ |
| Mar 2026 | 11 | 3 | 4 | 2 | 0 | █████████ |
| Apr 2026 | 7 | 3 | 3 | 0 | 0 | ██████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 4 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 29 Apr 2026 | Contracts | Northern Re, the collateralized reinsurance company that provides investors access to returns of its long-tail casualty underwriting business, has… | [Northern Re to scale capital intelligence via Palantir platform…](https://www.artemis.bm/news/northern-re-to-scale-capital-intelligence-via-palantir-platform-selection/) · artemis.bm |
| 28 Apr 2026 | Earnings | For the March-ended quarter, Palantir is expected to have generated $1.54 billion in sales, up 74% from the comparable quarter last year, and $0.28… | article unavailable |
| 26 Apr 2026 | Contracts | Palantir then released a statement to investors confirming the company was contracted by the FAA to “provide a data analytics tool that will help… | [America Trembles as Transportation Secretary Announces Plans for Air…](https://futurism.com/artificial-intelligence/ai-air-traffic-duffy) · futurism.com |
| 23 Apr 2026 | Contracts | Shares of Palantir Technologies (PLTR 5.32%) climbed on Wednesday after the data analytics provider struck a $300 million deal with the U.S.… | [Why Palantir Stock Popped Today \| The Motley Fool](https://www.fool.com/investing/2026/04/22/why-palantir-stock-is-up-today/) · fool.com |
| 9 Apr 2026 | Earnings | It posted a net income margin of approximately 43% for the quarter ended Dec. 31, 2025, and recently struck multiple partnerships and several… | [C3.ai vs. Palantir Technologies: Diverging Paths in Revenue \| The…](https://www.fool.com/coverage/charts/2026/04/09/c3ai-vs-palantir-technologies-diverging-paths-in-revenue/) · fool.com |
| 4 Apr 2026 | Earnings | calling for more than 60% revenue growth to a range of $7.18 billion to $7.19 billion. | article unavailable |
| 3 Apr 2026 | Job creation | Fortune reported that Palantir’s first class drew more than 500 applicants and accepted 22 people. | [Palantir CEO makes blunt AI claim and investors should care](https://finance.yahoo.com/sectors/technology/articles/palantir-ceo-makes-blunt-ai-181700441.html) · finance.yahoo.com |
| 31 Mar 2026 | Earnings | For full-year 2026, Palantir guided revenue between $7.182 billion and $7.198 billion, implying roughly 61% growth from 2025 levels. | article unavailable |
| 30 Mar 2026 | Contracts | On Monday, the software company confirmed a five-year extension to the contract with Autobauer Stellantis. | [Palantir Aktie: Stellantis-Deal fixiert](https://www.boerse-express.com/news/articles/palantir-aktie-stellantis-deal-fixiert-885361) · boerse-express.com |
| 27 Mar 2026 | Earnings | Palantir’s GAAP profitability is real and growing: GAAP net income reached $1.625 billion for full-year 2025, up 251.59% year-over‑year. | article unavailable |
| 27 Mar 2026 | Contracts | The contract with NYC Health + Hospitals, which runs until October 2026, will not be renewed. | [Palantir Aktie: Rückschlag in New York](https://www.boerse-express.com/news/articles/palantir-aktie-rueckschlag-in-new-york-883926) · boerse-express.com |
| 26 Mar 2026 | Contracts | The contract will give the controversial AI firm access to flag fraud, money laundering, and insider trading. | [Palantir just got access to something highly sensitive](https://finance.yahoo.com/markets/stocks/articles/palantir-just-got-access-something-180300954.html) · finance.yahoo.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company palantir.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company palantir.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company palantir.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company palantir.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$PRISM_BUSINESS_API_BASE/v1/business/companies/palantir.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "palantir.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Paytm News](paytm-news.md)
- [General Motors News](general-motors-news.md)
- [Qualcomm News](qualcomm-news.md)
- [Wipro News](wipro-news.md)
