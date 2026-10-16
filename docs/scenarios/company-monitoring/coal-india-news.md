# Coal India News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “coal india news” · 5,400/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [coal-india-news.json](../../examples/scenarios/coal-india-news.json).

**Question.** What has the news reported about Coal India in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `coalindia.in`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `coalindia.in` |
| Headlines, Jan – Apr 2026 (estimate) | 1,117 |
| Events, May 2025 – Apr 2026 | 114 |
| Most frequent event types | Earnings (69), Contracts (15), Announcement (14) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 25% · 1.6% · 74% of 1,117 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 7 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 29 Apr 2026 | [Asia Intelligence Brief for Wednesday, April 29, 2026](https://www.riotimesonline.com/asia-pulse-sk-hynix-softbank-china-india-april-2026/) | riotimesonline.com | 8 | positive | IPO |
| 29 Apr 2026 | [Closing Bell \| Sensex, Nifty end higher but off highs; largecaps outperform midcaps - CNBC TV18](https://www.cnbctv18.com/market/closing-bell-sensex-nifty-end-higher-but-off-highs-largecaps-outperform-midcaps-ws-l-19895831.htm) | cnbctv18.com | 6 | positive | — |
| 29 Apr 2026 | [Sensex jumps 1,000 points: What's driving the rally on Dalal Street today?](https://www.indiatoday.in/business/market/story/sensex-jumps-1000-points-maruti-leads-broad-based-rally-after-q4-2903152-2026-04-29) | indiatoday.in | 6 | positive | — |
| 29 Apr 2026 | [End of Hormuz blockade? How Trump could be forced into winding down Iran war](https://www.financialexpress.com/shorts/world-news/us-news/end-of-hormuz-blockade-how-trump-could-be-forced-into-winding-down-iran-war-4221595/) | financialexpress.com | 7 | negative | Earnings |
| 28 Apr 2026 | [Dhanbad News: सहायक कंपनियों के कमजोर प्रदर्शन से कोल इंडिया का मुनाफा घटा](https://www.prabhatkhabar.com/state/jharkhand/dhanbad/cils-profit-falls-due-to-weak-performance-of-subsidiaries) | prabhatkhabar.com | 7 | negative | Earnings |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 69 |
| Contracts | 15 |
| Announcement | 14 |
| Key people | 10 |
| Regulatory | 5 |
| Capital infusion | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Contracts | Announcement | Key people |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 18 | 16 | 1 | 1 | 0 | ██████████████████ |
| Jun 2025 | 1 | 0 | 0 | 0 | 1 | █ |
| Jul 2025 | 6 | 5 | 1 | 0 | 0 | ██████ |
| Aug 2025 | 9 | 5 | 2 | 2 | 0 | █████████ |
| Sep 2025 | 12 | 1 | 1 | 4 | 3 | ████████████ |
| Oct 2025 | 10 | 7 | 1 | 2 | 0 | ██████████ |
| Nov 2025 | 4 | 2 | 0 | 1 | 1 | ████ |
| Dec 2025 | 10 | 1 | 2 | 0 | 5 | ██████████ |
| Jan 2026 | 2 | 1 | 1 | 0 | 0 | ██ |
| Feb 2026 | 20 | 19 | 1 | 0 | 0 | ████████████████████ |
| Mar 2026 | 7 | 2 | 2 | 2 | 0 | ███████ |
| Apr 2026 | 15 | 10 | 3 | 2 | 0 | ███████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 7 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 28 Apr 2026 | Earnings | The net profit consolidated in the results of Coal India’s fiscal year 2025-26 stood at Rs. 31,071 crore from Rs. 35,450 crore, indicating a… | [Dhanbad News: सहायक कंपनियों के कमजोर प्रदर्शन से कोल इंडिया का…](https://www.prabhatkhabar.com/state/jharkhand/dhanbad/cils-profit-falls-due-to-weak-performance-of-subsidiaries) · prabhatkhabar.com |
| 28 Apr 2026 | Earnings | Coal India shares surged over 4% in early trade to reach around Rs. 473.90 after strong Q4 FY26 results. The state‑run major recorded a net profit… | article unavailable |
| 28 Apr 2026 | Earnings | Coal India reported consolidated net revenue growth of 6 per cent YoY, due to adjustment made to revenues on account of statutory levies on coal… | article unavailable |
| 28 Apr 2026 | Earnings | The company posted a standalone net profit after tax of INR 5,533.67 crore for the quarter ended March 2026, marking a sharp 75.6% increase y-o-y… | article unavailable |
| 28 Apr 2026 | Earnings | Coal India reported a net profit of ₹10,839 crore in the fourth quarter of FY26, registering a growth of 11.15% from ₹9,751 crore in the same period… | article unavailable |
| 28 Apr 2026 | Earnings | Coal India: The state-run coal miner reported a 11.2 per cent YoY jump in the net profit at Rs 10,839.18 crore, while revenue rose 5.8 per cent YoY… | [Top stocks in news: Coal India, M&M, Trent, Adani Gas, AU SFB,…](https://www.businesstoday.in/markets/stocks/story/top-stocks-in-news-coal-india-mm-trent-adani-gas-au-sfb-railtel-bajaj-housing-psb-527690-2026-04-28) · businesstoday.in |
| 27 Apr 2026 | Earnings | Coal India, the world’s largest coal miner, announced its financial performance for the March-ended quarter and financial year ended March 31 after… | article unavailable |
| 27 Apr 2026 | Earnings | Coal production/offtake improved QoQ in 4Q. E-auction premium to improve on account of import disruptions. | article unavailable |
| 26 Apr 2026 | Earnings | For 4QFY26E, we expect adjusted EBITDA to fall by 8.7 per cent YoY to Rs 10,250 crore, reflecting weaker e-auction realisations amid elevated coal… | article unavailable |
| 20 Apr 2026 | Contracts | The company said it has been declared the L1 bidder for a turnkey EPC package from Coal India for the development of an 875 MW (AC) grid-connected… | [SW Solar shares rally 17% after Rs 3,500 crore order from Coal…](https://economictimes.indiatimes.com/markets/stocks/news/sw-solar-shares-rally-17-after-rs-3500-crore-order-from-coal-india-check-details/articleshow/130386399.cms) · economictimes.indiatimes.com |
| 20 Apr 2026 | Contracts | The contract, awarded by Coal India, carries a value of about Rs 3,490 crore, including operations and maintenance as well as applicable taxes. | [Sterling & Wilson Renewable Energy Wins ₹3,550 Crore Solar Orders,…](https://www.freepressjournal.in/business/sterling-wilson-renewable-energy-wins-3550-crore-solar-orders-crosses-10062-crore-epc-order-inflows) · freepressjournal.in |
| 20 Apr 2026 | Contracts | Sterling and Wilson Renewable Energy has been declared the lowest bidder for a turnkey EPC package for development of an 875 MW AC grid-connected… | [SWREL shares rise 9% after winning ₹3,550 crore orders](https://www.businessupturn.com/finance/stock-market/swrel-shares-surge-9-after-securing-new-domestic-orders-worth-%e2%82%b93550-crore/) · businessupturn.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company coalindia.in --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company coalindia.in --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company coalindia.in --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company coalindia.in --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$PRISM_BUSINESS_API_BASE/v1/business/companies/coalindia.in/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "coalindia.in", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Larsen and Toubro News](larsen-and-toubro-news.md)
- [Salesforce News](salesforce-news.md)
- [Paypal News](paypal-news.md)
- [Icici Bank News](icici-bank-news.md)
