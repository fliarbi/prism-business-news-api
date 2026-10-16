# Hdfc Bank News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “hdfc bank news” · 22,200/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [hdfc-bank-news.json](../../examples/scenarios/hdfc-bank-news.json).

**Question.** What has the news reported about Hdfc Bank in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `hdfcbank.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `hdfcbank.com` |
| Headlines, Jan – Apr 2026 (estimate) | 2,909 |
| Events, May 2025 – Apr 2026 | 200 |
| Most frequent event types | Earnings (116), Key people (35), Regulatory (13) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 43% · 1.6% · 56% of 2,909 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 4 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [BT Closing Bell \| Sensex settles 582 pts lower, Nifty below 24,000; Eternal, HUL lead index losers -…](https://www.businesstoday.in/markets/stocks/story/bt-closing-bell-sensex-settles-582-pts-lower-nifty-below-24000-eternal-hul-lead-index-losers-528248-2026-04-30) | businesstoday.in | 7 | negative | — |
| 30 Apr 2026 | [Sensex, Nifty fall nearly 1 pc as oil surge weighs on sentiment](https://www.ibtimes.co.in/sensex-nifty-fall-nearly-1-pc-oil-surge-weighs-sentiment-901640) | ibtimes.co.in | 6 | negative | — |
| 30 Apr 2026 | [Sensex down 400 points: Why is the stock market falling today?](https://www.indiatoday.in/business/market/story/sensex-down-nifty-tanks-stock-market-fall-reason-crude-oil-rupee-fii-selling-iran-us-war-hormuz-block-2903586-2026-04-30) | indiatoday.in | 8 | negative | — |
| 30 Apr 2026 | [Infosys Falls Out of India’s Top 10 Most Valuable Companies](https://www.indianweb2.com/2026/04/infosys-falls-out-of-indias-top-10-most.html) | indianweb2.com | 7 | negative | — |
| 30 Apr 2026 | [IDFC First Bank vs Federal Bank: One stock is near 5-year valuation lows despite a 20% loan surge](https://www.financialexpress.com/market/stock-insights/idfc-first-bank-vs-federal-bank-one-stock-is-near-5-year-valuation-lows-despite-a-20-loan-surge/4222513/) | financialexpress.com | 7 | positive | — |
| 29 Apr 2026 | [Asia Intelligence Brief for Wednesday, April 29, 2026](https://www.riotimesonline.com/asia-pulse-sk-hynix-softbank-china-india-april-2026/) | riotimesonline.com | 8 | positive | IPO |
| 29 Apr 2026 | [Most valuable companies in India in 2026: Infosys loses more than Rs 2 lakh crore, slips out of top 10;…](https://indianexpress.com/article/trending/top-10-listing/top-10-most-valuable-companies-in-india-in-2026-infosys-tcs-reliance-industries-10662698/) | indianexpress.com | 8 | negative | — |
| 29 Apr 2026 | [FD vs mutual funds vs liquid funds: Where should you park short term money in current conditions? -…](https://www.businesstoday.in/personal-finance/investment/story/fd-vs-mutual-funds-vs-liquid-funds-where-should-you-park-short-term-money-in-current-conditions-528080-2026-04-29) | businesstoday.in | 6 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 116 |
| Key people | 35 |
| Regulatory | 13 |
| Board | 8 |
| Announcement | 6 |
| M&A | 5 |
| Lawsuit | 5 |
| New product | 4 |
| Contracts | 3 |
| Asset acquisition | 2 |
| IPO | 2 |
| Layoffs | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Key people | Regulatory | Board |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2 | 0 | 0 | 0 | 0 | █ |
| Jun 2025 | 7 | 0 | 1 | 0 | 0 | ███ |
| Jul 2025 | 42 | 40 | 0 | 0 | 0 | ████████████████████ |
| Aug 2025 | 15 | 8 | 0 | 0 | 0 | ███████ |
| Sep 2025 | 4 | 0 | 0 | 3 | 0 | ██ |
| Oct 2025 | 24 | 20 | 1 | 1 | 1 | ███████████ |
| Nov 2025 | 3 | 0 | 1 | 0 | 0 | █ |
| Dec 2025 | 5 | 0 | 1 | 3 | 0 | ██ |
| Jan 2026 | 28 | 23 | 1 | 2 | 0 | █████████████ |
| Feb 2026 | 2 | 0 | 1 | 0 | 0 | █ |
| Mar 2026 | 36 | 0 | 26 | 4 | 3 | █████████████████ |
| Apr 2026 | 32 | 25 | 3 | 0 | 4 | ███████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 7 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 29 Apr 2026 | Key people | The shareholders of HDFC Bank have Dr. Sunita Maheshwari confirmed as an independent director and thus set a sign of continuity. | article unavailable |
| 21 Apr 2026 | Earnings | The bank reported a 9% year-on-year rise in net profit to Rs. 19,221 crore in Q4 FY26. | article unavailable |
| 20 Apr 2026 | Earnings | HDFC Bank reported a net profit of Rs 19,221 crore for the March quarter, registering a 9% increase from Rs 17,616 crore in the same period last year. | [HDFC Bank vs ICICI Bank vs YES Bank: Which one to buy after Q4…](https://economictimes.indiatimes.com/market-data/stock-recos/hdfc-bank-vs-icici-bank-vs-yes-bank-which-one-to-buy-after-q4-results/articleshow/130383905.cms) · economictimes.indiatimes.com |
| 20 Apr 2026 | Earnings | India’s largest private lender reported a net profit of about Rs 19,221 crore for the fourth quarter, up around 9% from a year ago. | [HDFC Bank drops 1% after Q4 results: Profit rises, so why is stock…](https://www.indiatoday.in/business/market/story/hdfc-bank-q4-profit-up-9-stock-drops-1-on-growth-concerns-2898754-2026-04-20) · indiatoday.in |
| 20 Apr 2026 | Earnings | HDFC Bank, India’s leading private lender, reported a net profit of Rs 19,221 crore in the March quarter, marking an increase of 9% from Rs 17,616… | [Stocks in news: HDFC Bank, ICICI Bank, RIL, Trent, Jio Financial](http://economictimes.indiatimes.com/markets/stocks/news/stocks-in-news-hdfc-bank-icici-bank-ril-trent-jio-financial/articleshow/130380208.cms) · economictimes.indiatimes.com |
| 19 Apr 2026 | Board | HDFC Bank on Saturday said the process for reappointing its Managing Director and CEO Sashidhar Jagdishan will be taken up 'in due course', with the… | [HDFC Bank to decide on Sashidhar Jagdishan's reappointment 'in due…](https://www.ibtimes.co.in/hdfc-bank-decide-sashidhar-jagdishans-reappointment-due-course-icici-bank-net-profit-rises-9-901286) · ibtimes.co.in |
| 19 Apr 2026 | Earnings | HDFC Bank Saturday reported an 8.04 per cent jump in March quarter consolidated net profit to Rs 20,350.76 crore, but flagged near-term risks from… | article unavailable |
| 18 Apr 2026 | Key people | HDFC Bank on Saturday said the reappointment processes for both Chairman Keki Mistry and Managing Director & CEO Sashidhar Jagdishan are underway | article unavailable |
| 18 Apr 2026 | Key people | New Delhi: HDFC Bank on Saturday said the process for re-appointing its Managing Director and CEO Sashidhar Jagdishan will be taken up ‘in due… | article unavailable |
| 18 Apr 2026 | Earnings | Total revenue grew 5% to Rs 46,280 crore for the quarter. | article unavailable |
| 18 Apr 2026 | Earnings | Bank’s standalone net profit increased by 9% to Rs 19,221 crore in this quarter ended 31st March 2026. | article unavailable |
| 18 Apr 2026 | Earnings | The Bank has said that the total net profit has been Rs. 19221 crore during March 2026 from January. | [HDFC Bank को Q4 में हुआ 19221 करोड़ रुपये का नेट प्रॉफिट, 13 रुपये…](https://www.livehindustan.com/business/hdfc-bank-q4-results-2026-net-profit-19221-crore-rupee-in-march-quarter-dividend-announced-201776513210352.html) · livehindustan.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company hdfcbank.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company hdfcbank.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company hdfcbank.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company hdfcbank.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$PRISM_BUSINESS_API_BASE/v1/business/companies/hdfcbank.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "hdfcbank.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Ola Electric News](ola-electric-news.md)
- [Zomato News](zomato-news.md)
- [Oracle News](oracle-news.md)
- [AMD News](amd-news.md)
