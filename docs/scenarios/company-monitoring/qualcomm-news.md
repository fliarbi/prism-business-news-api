# Qualcomm News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “qualcomm news” · 4,400/month India · 5,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [qualcomm-news.json](../../examples/scenarios/qualcomm-news.json).

**Question.** What has the news reported about Qualcomm in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `qualcomm.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `qualcomm.com` |
| Headlines, Jan – Apr 2026 (estimate) | 1,097 |
| Events, May 2025 – Apr 2026 | 152 |
| Most frequent event types | Earnings (63), M&A (19), Announcement (17) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 21% · 0.3% · 79% of 1,097 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 3 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Qualcomm jumps as optimism on smartphones, AI chips outweigh dismal forecast](https://www.thestar.com.my/tech/tech-news/2026/04/30/qualcomm-shares-jump-as-optimism-on-smartphones-ai-chips-outweigh-dismal-forecast) | thestar.com.my | 7 | positive | — |
| 30 Apr 2026 | [Apple earnings become sideshow with new CEO ready to grab reins](https://www.mercurynews.com/2026/04/30/apple-earnings-become-sideshow-with-new-ceo-ready-to-grab-reins/) | mercurynews.com | 7 | positive | — |
| 30 Apr 2026 | [Stock Market Today (LIVE): Markets Close Out April With a Bang; Data Center Surprise Sends QCOM Up 15% \| The…](https://www.fool.com/investing/2026/04/30/stock-market-today-live-coverage/) | fool.com | 7 | negative | Earnings |
| 30 Apr 2026 | [Samsung Admits Exynos 2700 Is Coming and Plans Bigger Role in Galaxy S27 - OnMSFT](https://onmsft.com/news/samsung-admits-exynos-2700-is-coming-and-plans-bigger-role-in-galaxy-s27/) | onmsft.com | 8 | positive | — |
| 30 Apr 2026 | [Qualcomm shares jump as optimism on smartphones, AI chips outweigh dismal forecast](https://www.theglobeandmail.com/investing/article-qualcomm-forecast-smartphones-ai-chips-ceo-cristiano-amon/) | theglobeandmail.com | 7 | positive | — |
| 30 Apr 2026 | [Why Qualcomm shares jumped after CEO Cristiano Amon's comments - BusinessToday](https://www.businesstoday.in/markets/stocks/story/why-qualcomm-shares-jumped-after-ceo-cristiano-amons-comments-key-details-528176-2026-04-30) | businesstoday.in | 7 | positive | Announcement |
| 30 Apr 2026 | [AMD Appoints Vinay Awasthi as SVP, Asia Pacific, Japan and India (APJ) Sales](https://digitalterminal.in/tech-companies/amd-appoints-vinay-awasthi-as-svp-asia-pacific-japan-and-india-apj-sales) | digitalterminal.in | 7 | positive | Key people |
| 30 Apr 2026 | [Qualcomm Stock Surges Despite Weak Guidance After Q2 2026 Earnings Beat - EconoTimes](https://econotimes.com/Qualcomm-Stock-Surges-Despite-Weak-Guidance-After-Q2-2026-Earnings-Beat-1740418) | econotimes.com | 7 | positive | Earnings |
| 29 Apr 2026 | [Qualcomm stock jumps 17% on earnings beat and major AI chip sale](https://timesofsandiego.com/business/2026/04/29/qualcomm-stock-jumps-17-earnings-beat-major-ai-chip-sale/) | timesofsandiego.com | 7 | positive | Earnings |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 63 |
| M&A | 19 |
| Announcement | 17 |
| Key people | 10 |
| Contracts | 10 |
| Regulatory | 10 |
| Lawsuit | 8 |
| New product | 6 |
| Layoffs | 3 |
| Buyback | 2 |
| Asset acquisition | 1 |
| Capital infusion | 1 |
| IPO | 1 |
| Board | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | M&A | Announcement | Key people |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 7 | 5 | 0 | 0 | 0 | ████ |
| Jun 2025 | 17 | 0 | 12 | 2 | 2 | ██████████ |
| Jul 2025 | 5 | 5 | 0 | 0 | 0 | ███ |
| Aug 2025 | 14 | 5 | 0 | 4 | 0 | ████████ |
| Sep 2025 | 1 | 0 | 0 | 1 | 0 | █ |
| Oct 2025 | 26 | 2 | 2 | 0 | 0 | ███████████████ |
| Nov 2025 | 11 | 9 | 0 | 2 | 0 | ██████ |
| Dec 2025 | 8 | 1 | 5 | 0 | 2 | █████ |
| Jan 2026 | 4 | 3 | 0 | 0 | 0 | ██ |
| Feb 2026 | 35 | 25 | 0 | 2 | 4 | ████████████████████ |
| Mar 2026 | 7 | 0 | 0 | 4 | 1 | ████ |
| Apr 2026 | 17 | 8 | 0 | 2 | 1 | ██████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 8 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Earnings | More important than lackluster guidance Qualcomm turned $10.6 billion worth of revenue into a per-share profit of $2.65 for the three months ending… | article unavailable |
| 30 Apr 2026 | Earnings | Q2 Fiscal 2026: EPS (Non-GAAP) $2.65 | [Stock Market Today (LIVE): Markets Close Out April With a Bang; Data…](https://www.fool.com/investing/2026/04/30/stock-market-today-live-coverage/) · fool.com |
| 30 Apr 2026 | Earnings | For the second quarter, Qualcomm reported earnings per share (EPS) of $2.65 on revenue of $10.59 billion. | article unavailable |
| 30 Apr 2026 | Announcement | Qualcomm recently partnered with OpenAI to develop an AI chip for a future device. | [Why Qualcomm shares jumped after CEO Cristiano Amon's comments -…](https://www.businesstoday.in/markets/stocks/story/why-qualcomm-shares-jumped-after-ceo-cristiano-amons-comments-key-details-528176-2026-04-30) · businesstoday.in |
| 30 Apr 2026 | Earnings | The semiconductor giant reported adjusted earnings per share of $2.65, surpassing analyst expectations of $2.55. Quarterly revenue reached $10.6… | [Qualcomm Stock Surges Despite Weak Guidance After Q2 2026 Earnings…](https://econotimes.com/Qualcomm-Stock-Surges-Despite-Weak-Guidance-After-Q2-2026-Earnings-Beat-1740418) · econotimes.com |
| 29 Apr 2026 | Earnings | Qualcomm reported quarterly earnings on Wednesday that beat Wall Street estimates and announced a major sale of AI chips, prompting its stock to… | [Qualcomm stock jumps 17% on earnings beat and major AI chip sale](https://timesofsandiego.com/business/2026/04/29/qualcomm-stock-jumps-17-earnings-beat-major-ai-chip-sale/) · timesofsandiego.com |
| 29 Apr 2026 | Earnings | In fiscal Q2, we delivered revenues of $10.6 billion and non-GAAP earnings per share of $2.65 with EPS coming in at the high end of our guidance. | article unavailable |
| 29 Apr 2026 | Earnings | We delivered revenues of $10.6 billion and non‑GAAP earnings per share of $2.65 with EPS coming in at the high end of our guidance. | article unavailable |
| 28 Apr 2026 | Asset acquisition | Qualcomm leased 2.56 lakh sq ft in Bengaluru for five years at a total rent of ₹184 crore. | article unavailable |
| 27 Apr 2026 | IPO | Qualcomm IPO'd in 1991 and has grown 27,052% since going public. | article unavailable |
| 24 Apr 2026 | Announcement | That message was highlighted at Mobile World Congress when the company announced a broad industry coalition focused on a milestone-driven 6G… | article unavailable |
| 23 Apr 2026 | Earnings | In its most recent quarter, Qualcomm delivered steady results. Revenue rose 5% year-over-year to $12.2 billion, while earnings increased 3% to $3.5… | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company qualcomm.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company qualcomm.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company qualcomm.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company qualcomm.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/qualcomm.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "qualcomm.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.
- Zero-count periods are included; partial_period marks buckets only partly covered by the window.
- shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)

## Related demonstrations

- [General Motors News](general-motors-news.md)
- [Palantir News](palantir-news.md)
- [Wipro News](wipro-news.md)
- [Ongc News](ongc-news.md)
