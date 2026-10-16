# Meta News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “meta news” · 2,900/month India · 14,800/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [meta-news.json](../../examples/scenarios/meta-news.json).

**Question.** What has the news reported about Meta in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `meta.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `meta.com` |
| Headlines, Jan – Apr 2026 (estimate) | 137 |
| Events, May 2025 – Apr 2026 | 359 |
| Most frequent event types | Earnings (61), Key people (55), Contracts (54) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 45% · 1.5% · 54% of 137 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 5 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Stock Market Today (LIVE): Markets Close Out April With a Bang; Data Center Surprise Sends QCOM Up 15% \| The…](https://www.fool.com/investing/2026/04/30/stock-market-today-live-coverage/) | fool.com | 7 | negative | Earnings |
| 30 Apr 2026 | [Ad engines power Big Tech: Alphabet ads hit $77 billion, Meta surges 33%, Amazon crosses $70 billion run rate](https://www.storyboard18.com/how-it-works/ad-engines-power-big-tech-alphabet-ads-hit-77-billion-meta-surges-33-amazon-crosses-70-billion-run-rate-96705.htm) | storyboard18.com | 8 | positive | Earnings |
| 29 Apr 2026 | [This Super Semiconductor Stock Is Obliterating Nvidia, AMD, and Broadcom in 2026](https://www.theglobeandmail.com/investing/markets/stocks/GLW/pressreleases/1594991/this-super-semiconductor-stock-is-obliterating-nvidia-amd-and-broadcom-in-2026/) | theglobeandmail.com | 8 | positive | Announcement |
| 29 Apr 2026 | [Meta is paying top executives to hit a $9.5 trillion valuation—and no one’s ever done it before \| Fortune](https://www.fortune.com/2026/04/28/meta-q1-executive-stock-options-zuckerberg-9-trillion-valuation-moonshot/) | fortune.com | 8 | positive | Earnings |
| 28 Apr 2026 | [China Blocks Meta Manus Deal Citing AI Tech Transfer Risks](https://www.mirrorreview.com/news/china-blocks-meta-manus-deal/) | mirrorreview.com | 8 | negative | Regulatory |
| 27 Apr 2026 | [China Blocks Meta's $2 Billion Acquisition of AI Startup Manus Citing Regulatory Grounds](http://www.ibtimes.com/china-blocks-metas-2-billion-acquisition-ai-startup-manus-citing-regulatory-grounds-3802011) | ibtimes.com | 8 | negative | Regulatory |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 61 |
| Key people | 55 |
| Contracts | 54 |
| Lawsuit | 45 |
| M&A | 29 |
| Regulatory | 29 |
| New product | 23 |
| Layoffs | 23 |
| Announcement | 18 |
| Job creation | 10 |
| Funding round | 5 |
| Capital infusion | 4 |
| Asset acquisition | 2 |
| Buyback | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Key people | Contracts | Lawsuit |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 8 | 6 | 0 | 0 | 0 | ███ |
| Jun 2025 | 27 | 0 | 7 | 2 | 2 | █████████ |
| Jul 2025 | 59 | 6 | 25 | 3 | 16 | ████████████████████ |
| Aug 2025 | 24 | 2 | 0 | 8 | 4 | ████████ |
| Sep 2025 | 19 | 2 | 3 | 4 | 3 | ██████ |
| Oct 2025 | 42 | 17 | 5 | 8 | 2 | ██████████████ |
| Nov 2025 | 17 | 3 | 1 | 4 | 3 | ██████ |
| Dec 2025 | 21 | 1 | 3 | 3 | 0 | ███████ |
| Jan 2026 | 39 | 11 | 3 | 5 | 1 | █████████████ |
| Feb 2026 | 19 | 1 | 1 | 4 | 6 | ██████ |
| Mar 2026 | 33 | 0 | 4 | 6 | 7 | ███████████ |
| Apr 2026 | 51 | 12 | 3 | 7 | 1 | █████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 5 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Earnings | Meta (META 8.49%) just dropped a monster Q1 2026, posting $56.31 billion in revenue, which is up 33% year over year. | [Stock Market Today (LIVE): Markets Close Out April With a Bang; Data…](https://www.fool.com/investing/2026/04/30/stock-market-today-live-coverage/) · fool.com |
| 30 Apr 2026 | Earnings | The company reported total revenue of $56.3 billion, up 33% year-on-year, ... Net income surged 61% to $26.8 billion. | [Ad engines power Big Tech: Alphabet ads hit $77 billion, Meta surges…](https://www.storyboard18.com/how-it-works/ad-engines-power-big-tech-alphabet-ads-hit-77-billion-meta-surges-33-amazon-crosses-70-billion-run-rate-96705.htm) · storyboard18.com |
| 30 Apr 2026 | Earnings | Advertising revenue, which remains the company’s economic backbone, rose to $55.02 billion in the quarter, accounting for the vast majority of total… | [Facebook and Instagram parent Meta reports $55 billion in ad revenue…](https://www.storyboard18.com/how-it-works/facebook-and-instagram-parent-meta-reports-55-billion-in-ad-revenue-in-q1-2026-96698.htm) · storyboard18.com |
| 30 Apr 2026 | Earnings | Meta Platforms, Inc. posted a robust performance for the first quarter ended March 31, 2026, with net income surging 61 per cent year-on-year to… | article unavailable |
| 29 Apr 2026 | Earnings | Q1 total revenue was $56.3 billion, up 33%, or 29% on a constant currency basis. | article unavailable |
| 29 Apr 2026 | Earnings | Meta Platforms, Inc. (Nasdaq: META ) today reported financial results for the quarter ended March 31, 2026. | article unavailable |
| 29 Apr 2026 | Announcement | In January, Facebook parent Meta Platforms(NASDAQ: META) signed an agreement to buy $6 billion worth of Corning's optical fiber over the next few… | [This Super Semiconductor Stock Is Obliterating Nvidia, AMD, and…](https://www.theglobeandmail.com/investing/markets/stocks/GLW/pressreleases/1594991/this-super-semiconductor-stock-is-obliterating-nvidia-amd-and-broadcom-in-2026/) · theglobeandmail.com |
| 29 Apr 2026 | Earnings | Analysts expect Meta to report Q1 revenue near $55.5 billion, up roughly 31% year-over-year, and in the middle of the $53.5 billion to $56.5 billion… | article unavailable |
| 29 Apr 2026 | Earnings | Analysts expect Meta to report Q1 revenue near $55.5 billion, up roughly 31% year-over-year, and in the middle of the $53.5 billion to $56.5 billion… | [Meta is paying top executives to hit a $9.5 trillion valuation—and…](https://www.fortune.com/2026/04/28/meta-q1-executive-stock-options-zuckerberg-9-trillion-valuation-moonshot/) · fortune.com |
| 28 Apr 2026 | Regulatory | On Monday, April 27, 2026, China’s National Development and Reform Commission (NDRC) ordered Meta Platforms Inc. to unwind its $2 billion… | [China Blocks Meta Manus Deal Citing AI Tech Transfer Risks](https://www.mirrorreview.com/news/china-blocks-meta-manus-deal/) · mirrorreview.com |
| 28 Apr 2026 | Regulatory | China’s National Development and Reform Commission (NDRC) has ordered Meta Platforms to unwind its US$2 billion acquisition of Singapore-based AI… | article unavailable |
| 27 Apr 2026 | Regulatory | China has blocked Meta Platforms' planned acquisition of artificial intelligence startup Manus, ordering the deal to be unwound after months of… | [China Blocks Meta's $2 Billion Acquisition of AI Startup Manus…](http://www.ibtimes.com/china-blocks-metas-2-billion-acquisition-ai-startup-manus-citing-regulatory-grounds-3802011) · ibtimes.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company meta.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company meta.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company meta.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company meta.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/meta.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "meta.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Rivian News](rivian-news.md)
- [Netflix News](netflix-news.md)
- [Jpmorgan News](jpmorgan-news.md)
- [SBI News](sbi-news.md)
