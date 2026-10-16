# Bajaj Finance News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “bajaj finance news” · 5,400/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [bajaj-finance-news.json](../../examples/scenarios/bajaj-finance-news.json).

**Question.** What has the news reported about Bajaj Finance in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `bajajfinserv.in`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `bajajfinserv.in` |
| Headlines, Jan – Apr 2026 (estimate) | 440 |
| Events, May 2025 – Apr 2026 | 34 |
| Most frequent event types | Earnings (22), Key people (3), Announcement (3) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 30% · 0.5% · 69% of 440 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 4 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Best Home Loan Rate of Interest in April 2026 - Compare & Save Lakhs!](https://www.franchiseindia.com/insights/en/article/best-home-loan-rate-of-interest-in-april-2026-compare-save-lakhs.58815) | franchiseindia.com | 6 | positive | — |
| 30 Apr 2026 | [Bajaj Finserv announces dividend, reports strong FY26 growth](https://www.indiatoday.in/business/story/bajaj-finserv-announces-dividend-reports-strong-fy26-growth-2903742-2026-04-30) | indiatoday.in | 7 | positive | Earnings |
| 30 Apr 2026 | [Bajaj Finserv Q4 FY26 results: Net profit up 5% to Rs 2,539 crore, Net Income jumps to Rs 14,209 crore](https://www.financialexpress.com/business/industry-bajaj-finserv-q4-fy26-results-net-profit-up-5-to-rs-2539-crore-net-income-jumps-to-rs-14209-crorenbsp-4223194/) | financialexpress.com | 7 | positive | Earnings |
| 30 Apr 2026 | [Stock Markets Dive In Early Trade As Oil Prices Surge Above $120 Per Barrel – Outlook Business](https://www.outlookbusiness.com/markets/stock-markets-dive-in-early-trade-as-oil-prices-surge-above-120-per-barrel) | outlookbusiness.com | 6 | negative | — |
| 30 Apr 2026 | [Sensex down 400 points: Why is the stock market falling today?](https://www.indiatoday.in/business/market/story/sensex-down-nifty-tanks-stock-market-fall-reason-crude-oil-rupee-fii-selling-iran-us-war-hormuz-block-2903586-2026-04-30) | indiatoday.in | 8 | negative | — |
| 30 Apr 2026 | [Top stocks in news: Bajaj Finance, Vedanta, L&T, Indegene, Schaeffler, MOIL, HindZinc, HUL - BusinessToday](https://www.businesstoday.in/markets/stocks/story/top-stocks-in-news-bajaj-finance-vedanta-lt-indegene-schaeffler-moil-hindzinc-hul-528123-2026-04-30) | businesstoday.in | 8 | positive | Earnings |
| 30 Apr 2026 | [7 Best Unsecured Personal Loan Options Without Collateral in India (2026)](https://www.indiaherald.com/Viral/Read/994889398/-Best-Unsecured-Personal-Loan-Options-Without-Collateral-in-India-) | indiaherald.com | 6 | positive | — |
| 29 Apr 2026 | [Sensex rises 609 points as UAE’s OPEC exit spurs crude hopes; rupee hits record low](https://www.thehindubusinessline.com/markets/sensex-rises-609-points-as-uaes-opec-exit-spurs-crude-hopes-rupee-hits-record-low/article70920331.ece) | thehindubusinessline.com | 8 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 22 |
| Key people | 3 |
| Announcement | 3 |
| M&A | 2 |
| Regulatory | 2 |
| Asset acquisition | 1 |
| Capital infusion | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Key people | Announcement | M&A |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 0 | 0 | 0 | 0 | 0 |  |
| Jun 2025 | 3 | 0 | 2 | 0 | 1 | ██████ |
| Jul 2025 | 10 | 7 | 0 | 1 | 0 | ████████████████████ |
| Aug 2025 | 1 | 1 | 0 | 0 | 0 | ██ |
| Sep 2025 | 1 | 0 | 0 | 1 | 0 | ██ |
| Oct 2025 | 1 | 1 | 0 | 0 | 0 | ██ |
| Nov 2025 | 6 | 5 | 1 | 0 | 0 | ████████████ |
| Dec 2025 | 1 | 0 | 0 | 0 | 0 | ██ |
| Jan 2026 | 2 | 0 | 0 | 1 | 1 | ████ |
| Feb 2026 | 5 | 4 | 0 | 0 | 0 | ██████████ |
| Mar 2026 | 0 | 0 | 0 | 0 | 0 |  |
| Apr 2026 | 4 | 4 | 0 | 0 | 0 | ████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 2 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Earnings | The company reported its highest‑ever consolidated total income of Rs 150,530 crore for FY26, with profit after tax at Rs 9,801 crore. | [Bajaj Finserv announces dividend, reports strong FY26 growth](https://www.indiatoday.in/business/story/bajaj-finserv-announces-dividend-reports-strong-fy26-growth-2903742-2026-04-30) · indiatoday.in |
| 30 Apr 2026 | Earnings | The company reported a consolidated net profit of Rs 2,539 crore in Q4 FY26. | [Bajaj Finserv Q4 FY26 results: Net profit up 5% to Rs 2,539 crore,…](https://www.financialexpress.com/business/industry-bajaj-finserv-q4-fy26-results-net-profit-up-5-to-rs-2539-crore-net-income-jumps-to-rs-14209-crorenbsp-4223194/) · financialexpress.com |
| 30 Apr 2026 | Earnings | MOFSL said that Bajaj Finserv's GWP growth is expected to remain subdued, hurt by soft momentum in the lumpy govt. health and crop segments. | article unavailable |
| 29 Apr 2026 | Earnings | Bajaj Finserv stated that its revenuePAT is expected to clock a CAGR of 15 per cent 17 per cent in FY26-28... | [Stock up 9% in a month: Bajaj Finserv Q4 results, dividend 2026…](https://www.businesstoday.in/markets/stocks/story/stock-up-9-in-a-month-bajaj-finserv-q4-results-dividend-2026-announcement-date-and-time-earnings-schedule-527974-2026-04-29) · businesstoday.in |
| 20 Feb 2026 | Capital infusion | Bajaj Finserv's alternative investment arm plans to raise up to the equivalent of $1 billion. | [Bajaj Finserv all set to launch $1-billion alts investment platform](https://economictimes.indiatimes.com/markets/stocks/news/bajaj-finserv-all-set-to-launch-1-billion-alts-investment-platform/articleshow/128583669.cms) · economictimes.indiatimes.com |
| 5 Feb 2026 | Earnings | Bajaj Finserv on Wednesday reported a consolidated net profit of ₹2,229 crore for the third quarter of FY26 and a consolidated total income of… | [Q3 results today: Airtel, Hero MotoCorp, IOCL, and LIC among 199 firms](https://www.business-standard.com/companies/quarterly-results/q3-results-today-airtel-hero-motocorp-iocl-and-lic-among-199-firms-126020500213_1.html) · business-standard.com |
| 4 Feb 2026 | Earnings | Bajaj Finserv has reported a consolidated net profit of Rs 2,229 crore for the third quarter ending December 2025, experiencing almost flat growth… | article unavailable |
| 4 Feb 2026 | Earnings | Nine-month Performance Signals Strong Base For the 9M FY26 period, Bajaj Finserv reported total income of Rupees 1,12,562 crore, up 16 percent YoY,… | [Bajaj Finserv Q3 Net Profit Climbs 32% YoY To ₹2,229 Crore, Revenue…](https://www.freepressjournal.in/business/bajaj-finserv-q3-net-profit-climbs-32-yoy-to-2229-crore-revenue-surges-to-39708-crore) · freepressjournal.in |
| 4 Feb 2026 | Earnings | Total revenue surged 24% to ₹39,708.6 crore from ₹32,041.8 crore a year earlier. | [Bajaj Finserv Q3 profit remains flat; revenue rises 24% - CNBC TV18](https://www.cnbctv18.com/market/earnings/bajaj-finserv-q3-profit-flat-revenue-net-interest-income-share-price-ws-l-19841911.htm) · cnbctv18.com |
| 9 Jan 2026 | Announcement | Bajaj Finserv, one of India’s largest and most diversified financial services companies, has completed the acquisition, together with Bajaj Holdings… | [Hot stocks: Reliance, Bharat Forge, Bajaj Finserv, IEX, Bartronics,…](https://www.thehindubusinessline.com/markets/hot-stocks-reliance-bharat-forge-bajaj-finserv-iex-bartronics-prestige-estates-sundaram-clayton-powermech-upl-eureka-forbes-groww/article70487856.ece) · thehindubusinessline.com |
| 8 Jan 2026 | M&A | Bajaj Finserv Limited on Thursday, January 8, said it has completed the acquisition of a 23% equity stake in its insurance businesses from Allianz… | [Bajaj Finserv’s ₹21,390 crore Allianz buyout ends 24-year insurance…](https://www.cnbctv18.com/market/bajaj-finservs-rs-21390-crore-allianz-buyout-ends-24-year-insurance-partnership-share-price-ws-l-19817100.htm) · cnbctv18.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company bajajfinserv.in --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company bajajfinserv.in --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company bajajfinserv.in --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company bajajfinserv.in --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/bajajfinserv.in/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "bajajfinserv.in", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Coinbase News](coinbase-news.md)
- [Spotify News](spotify-news.md)
- [Stripe News](stripe-news.md)
