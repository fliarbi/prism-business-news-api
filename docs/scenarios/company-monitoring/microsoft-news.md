# Microsoft News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “microsoft news” · 3,600/month India · 14,800/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [microsoft-news.json](../../examples/scenarios/microsoft-news.json).

**Question.** What has the news reported about Microsoft in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `microsoft.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `microsoft.com` |
| Headlines, Jan – Apr 2026 (estimate) | 14,610 |
| Events, May 2025 – Apr 2026 | 707 |
| Most frequent event types | Key people (206), Contracts (128), Earnings (114) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 24% · 0.7% · 75% of 14,610 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 5 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Top AI Stocks to Buy in the US 2026 for Long-Term Growth](https://www.analyticsinsight.net/stocks/top-ai-stocks-to-buy-in-the-us-2026-for-long-term-growth) | analyticsinsight.net | 8 | positive | — |
| 30 Apr 2026 | [Anthropic Valuation Soars to $900B in Explosive AI Funding Round Closing Within Two Weeks](https://bitcoinworld.co.in/anthropic-valuation-ai-funding-round/) | bitcoinworld.co.in | 7 | positive | — |
| 30 Apr 2026 | [Breitbart Business Digest: The Best Month for Stocks in Five Years](https://www.breitbart.com/economy/2026/04/30/breitbart-business-digest-the-best-month-for-stocks-in-five-years/) | breitbart.com | 6 | positive | — |
| 30 Apr 2026 | [Here's Why This Remains My Least Favorite "Magnificent Seven" Stock -- Even After a Strong Earnings Report \|…](https://www.fool.com/investing/2026/04/30/heres-why-this-remains-my-least-favorite-magnifice/) | fool.com | 8 | positive | Earnings |
| 30 Apr 2026 | [Israel Missile Defense Organization (IMDO) & RAFAEL deliver 1st batch of Tamir interceptors for U.S. Marine…](https://www.edrmagazine.eu/israel-missile-defense-organization-imdo-rafael-deliver-1st-batch-of-tamir-interceptors-for-u-s-marine-corps-mric-program) | edrmagazine.eu | 5 | positive | — |
| 30 Apr 2026 | [Apple, Amazon, Google, Meta and Microsoft: revenues of 541.8 billion](https://en.ilsole24ore.com/art/apple-amazon-google-meta-and-microsoft-revenues-5418-billion-AIG02MoC) | en.ilsole24ore.com | 8 | positive | — |
| 30 Apr 2026 | [Stocks Reach New Record As Nasdaq Composite Climbs Over 15% In April](https://www.ibtimes.com/stocks-reach-new-record-nasdaq-composite-climbs-over-15-april-3802222) | ibtimes.com | 8 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Key people | 206 |
| Contracts | 128 |
| Earnings | 114 |
| Announcement | 68 |
| Layoffs | 60 |
| Lawsuit | 34 |
| New product | 32 |
| Regulatory | 17 |
| M&A | 15 |
| Asset acquisition | 12 |
| Capital infusion | 12 |
| Job creation | 7 |
| Funding round | 1 |
| Buyback | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Key people | Contracts | Earnings | Announcement |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 43 | 5 | 9 | 8 | 0 | █████████ |
| Jun 2025 | 52 | 28 | 6 | 1 | 2 | ███████████ |
| Jul 2025 | 78 | 16 | 4 | 23 | 9 | █████████████████ |
| Aug 2025 | 56 | 19 | 6 | 9 | 5 | ████████████ |
| Sep 2025 | 62 | 6 | 28 | 3 | 15 | █████████████ |
| Oct 2025 | 94 | 33 | 16 | 23 | 2 | ████████████████████ |
| Nov 2025 | 44 | 2 | 18 | 5 | 6 | █████████ |
| Dec 2025 | 37 | 6 | 10 | 1 | 8 | ████████ |
| Jan 2026 | 57 | 9 | 9 | 16 | 4 | ████████████ |
| Feb 2026 | 58 | 36 | 4 | 8 | 3 | ████████████ |
| Mar 2026 | 53 | 25 | 4 | 1 | 8 | ███████████ |
| Apr 2026 | 73 | 21 | 14 | 16 | 6 | ████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 5 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Earnings | Software giant Microsoft (MSFT 3.90%) reported its fiscal third quarter of 2026 (the period ended March 31, 2026) this week, and the headline… | [Here's Why This Remains My Least Favorite "Magnificent Seven" Stock…](https://www.fool.com/investing/2026/04/30/heres-why-this-remains-my-least-favorite-magnifice/) · fool.com |
| 30 Apr 2026 | Earnings | For the quarter ended March 31, the company posted revenue of $82.9 billion, up 18% year over year. Operating income rose 20% to $38.4 billion,… | article unavailable |
| 30 Apr 2026 | New product | Microsoft packages AI, identity, and security together Microsoft appears to be focused on building an all-in-one platform for AI services, recently… | article unavailable |
| 30 Apr 2026 | Earnings | The tech giant posted revenue of $82.9 billion for the quarter ended March 31, up 18 percent from a year earlier and topping analyst consensus… | article unavailable |
| 30 Apr 2026 | Earnings | Microsoft (MSFT 3.90%) just reported a quarter that beat on basically every number that matters. | [Stock Market Today (LIVE): Markets Close Out April With a Bang; Data…](https://www.fool.com/investing/2026/04/30/stock-market-today-live-coverage/) · fool.com |
| 30 Apr 2026 | Earnings | Microsoft (NASDAQ: MSFT) beat on earnings and revenue but slipped after reporting $31.9 billion in capex for its fiscal third quarter. EPS of $4.27… | [Stock Market Live April 30, 2026: S&P 500 (SPY) Boosted by Earnings…](https://247wallst.com/investing/2026/04/30/stock-market-live-april-30-2026-sp-500-spy-boosted-by-earnings-and-lower-oil/) · 247wallst.com |
| 30 Apr 2026 | Announcement | In its last fiscal quarter, Microsoft spent $32 billion on the | [Trimestriels Microsoft : les dépenses en IA s’envolent, pas le ROI](https://www.channelnews.fr/trimestriels-microsoft-les-depenses-en-ia-senvolent-pas-le-roi-156530) · channelnews.fr |
| 30 Apr 2026 | Earnings | Microsoft’s Intelligent Cloud segment, reported as part of its Q3 FY26 results, earned $34.68 billion in revenue, up 30% from a year earlier. | [Google Crushes AWS, Microsoft Azure as Hypergrowth Hits the Cloud \|…](https://analyticsindiamag.com/global-tech/google-crushes-aws-microsoft-azure-as-hypergrowth-hits-the-cloud) · analyticsindiamag.com |
| 30 Apr 2026 | Earnings | The company reported revenue of $82.9 billion for the quarter ended March 31, an 18 percent increase from a year earlier, while net income rose 23… | [HUL Q4 adex up by 6% at Rs 1,509 crore \| YouTube powers Alphabet’s…](https://www.storyboard18.com/special-coverage/hul-q4-adex-up-by-6-at-rs-1509-crore-youtube-powers-alphabets-ai-push-96814.htm) · storyboard18.com |
| 30 Apr 2026 | Earnings | Microsoft posted strong top- and bottom-line growth for the third quarter of its 2026 fiscal year, ... the company’s total revenue increased 18%… | article unavailable |
| 30 Apr 2026 | Earnings | Microsoft delivered a strong Q3 FY2026 beat across the board, with revenues up 18% YoY to $82.9 billion, surpassing expectations of $81.4 billions. | article unavailable |
| 30 Apr 2026 | Earnings | Microsoft reported $77.7 billion in revenue for its FY26 Q1 (ended September 30, 2025), up 18% | [Big Tech Q1 results: AI may be the story, but ads are still the…](https://www.exchange4media.com/digital-news/big-tech-q1-results-ai-may-be-the-story-but-ads-are-still-the-business-154268.html) · exchange4media.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company microsoft.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company microsoft.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company microsoft.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company microsoft.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$PRISM_BUSINESS_API_BASE/v1/business/companies/microsoft.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "microsoft.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [AMD News](amd-news.md)
- [Anthropic News](anthropic-news.md)
- [Walmart News](walmart-news.md)
- [Rivian News](rivian-news.md)
