# Icici Bank News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “icici bank news” · 5,400/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [icici-bank-news.json](../../examples/scenarios/icici-bank-news.json).

**Question.** What has the news reported about Icici Bank in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `icicibank.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `icicibank.com` |
| Headlines, Jan – Apr 2026 (estimate) | 1,587 |
| Events, May 2025 – Apr 2026 | 112 |
| Most frequent event types | Earnings (89), M&A (8), Contracts (4) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 33% · 1.6% · 65% of 1,587 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 4 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Smartworks Posts ₹17 Cr Profit In Q4, Revenue Crosses ₹500 Cr Mark](https://startupnews.fyi/business/smartworks-posts-17-cr-profit-in-q4-revenue-crosses-500-cr-mark) | startupnews.fyi | 8 | negative | — |
| 30 Apr 2026 | [Vedanta demerger: Stock may fall sharply today; here's why - BusinessToday](https://www.businesstoday.in/markets/stocks/story/vedanta-demerger-stock-may-fall-sharply-today-heres-why-528118-2026-04-30) | businesstoday.in | 4 | negative | — |
| 29 Apr 2026 | [Kotak Mahindra Bank Q4 earnings preview: Brokerages see steady NII growth, muted profit expansion \| Stock…](https://www.livemint.com/market/stock-market-news/kotak-mahindra-bank-q4-earnings-preview-brokerages-see-steady-nii-growth-muted-profit-expansion-11777480586804.html) | livemint.com | 7 | positive | — |
| 29 Apr 2026 | [Most valuable companies in India in 2026: Infosys loses more than Rs 2 lakh crore, slips out of top 10;…](https://indianexpress.com/article/trending/top-10-listing/top-10-most-valuable-companies-in-india-in-2026-infosys-tcs-reliance-industries-10662698/) | indianexpress.com | 8 | negative | — |
| 29 Apr 2026 | [Haryana women's panel chief visits suicide-hit NIT Kurukshetra, cites 'online gambling, credit card debt'](https://theprint.in/india/education/haryana-womens-panel-chief-visits-suicide-hit-nit-kurukshetra-cites-online-gambling-credit-card-debt/2917297/) | theprint.in | 8 | negative | — |
| 29 Apr 2026 | [MakeMyTrip eyes India IPO By Q1 2027, Ropes In Bankers: Report](https://inc42.com/buzz/makemytrip-eyes-india-ipo-by-q1-2027-ropes-in-bankers-report/) | inc42.com | 8 | positive | IPO |
| 29 Apr 2026 | [UPI यूजर्स के लिए खुशखबरी! बिना पिन अब फिंगरप्रिंट और फेस ID से होगी पेमेंट, ये है नया तरीका](https://www.livehindustan.com/business/icici-bank-launches-biometric-authentication-for-upi-payments-on-imobile-know-how-it-works-201777461327014.html) | livehindustan.com | 6 | positive | — |
| 29 Apr 2026 | [ICICI Bank enables facial recognition, fingerprint authentication services for UPI transactions up to Rs…](https://economictimes.indiatimes.com/wealth/save/icici-bank-enables-biometric-authentication-for-upi-transactions-up-to-rs-5000-how-to-activate-service-on-imobile-app/articleshow/130604696.cms) | economictimes.indiatimes.com | 7 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 89 |
| M&A | 8 |
| Contracts | 4 |
| Regulatory | 4 |
| Announcement | 3 |
| Lawsuit | 2 |
| Key people | 1 |
| IPO | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | M&A | Contracts | Regulatory |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1 | 1 | 0 | 0 | 0 | █ |
| Jun 2025 | 3 | 0 | 3 | 0 | 0 | ██ |
| Jul 2025 | 26 | 24 | 1 | 0 | 0 | ████████████████████ |
| Aug 2025 | 5 | 3 | 0 | 1 | 0 | ████ |
| Sep 2025 | 4 | 0 | 0 | 2 | 2 | ███ |
| Oct 2025 | 15 | 14 | 0 | 0 | 0 | ████████████ |
| Nov 2025 | 2 | 0 | 1 | 0 | 0 | ██ |
| Dec 2025 | 5 | 2 | 1 | 1 | 0 | ████ |
| Jan 2026 | 23 | 21 | 1 | 0 | 1 | ██████████████████ |
| Feb 2026 | 1 | 1 | 0 | 0 | 0 | █ |
| Mar 2026 | 2 | 0 | 1 | 0 | 0 | ██ |
| Apr 2026 | 25 | 23 | 0 | 0 | 1 | ███████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 5 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 27 Apr 2026 | Lawsuit | In 2018, ICICI Bank filed the first insolvency petition against JAL, followed by SBI in 2022. | article unavailable |
| 20 Apr 2026 | Earnings | ICICI Securities noted that the bank delivered a robust quarter with improvement in margins and growth momentum. | [Yes Bank Climbs on Strong Q4, But Brokerages Flag Limited Upside –…](https://www.outlookbusiness.com/markets/yes-bank-shares-rise-on-strong-q4-but-brokerages-flag-limited-upside) · outlookbusiness.com |
| 20 Apr 2026 | Earnings | ICICI Bank reported a net profit of Rs 13,702 crore in the fourth quarter of FY26, marking an increase of 8.5% year-on-year from Rs 12,630 crore… | [HDFC Bank vs ICICI Bank vs YES Bank: Which one to buy after Q4…](https://economictimes.indiatimes.com/market-data/stock-recos/hdfc-bank-vs-icici-bank-vs-yes-bank-which-one-to-buy-after-q4-results/articleshow/130383905.cms) · economictimes.indiatimes.com |
| 20 Apr 2026 | Earnings | Shares of ICICI Bank, one of India’s leading private lenders, rose 2% to their day’s high of Rs 1,369 on the BSE on Monday after reporting a net… | [ICICI Bank shares rise 2% after Q4 results. What Jefferies,…](http://economictimes.indiatimes.com/markets/stocks/news/icici-bank-shares-rise-2-after-q4-results-what-are-jefferies-bernstein-and-other-brokerages-are-saying/articleshow/130382097.cms) · economictimes.indiatimes.com |
| 20 Apr 2026 | Earnings | ICICI’s PAT beat Q4 estimate driven by a sharp beat on provisions on the back of lower slippages, strong recoveries and higher write-backs from the… | article unavailable |
| 20 Apr 2026 | Earnings | ICICI Bank, one of India's leading private lenders, on Saturday reported a net profit of Rs 13,702 crore in the fourth quarter of FY26, marking an… | [Stocks in news: HDFC Bank, ICICI Bank, RIL, Trent, Jio Financial](http://economictimes.indiatimes.com/markets/stocks/news/stocks-in-news-hdfc-bank-icici-bank-ril-trent-jio-financial/articleshow/130380208.cms) · economictimes.indiatimes.com |
| 19 Apr 2026 | Earnings | ICICI Bank on Saturday reported a 9.28 per cent rise in consolidated net profit to Rs 14,755 crore for the March quarter, helped by a nearly 90 per… | article unavailable |
| 18 Apr 2026 | Earnings | The Bank reported on Saturday that during the 4th quarter of the fiscal year ended March 2026, his profit increased by 9.28 percent to Rs 14,755… | [ICICI बैंक के मुनाफे में आया उछाल, सोमवार को शेयर पर रहेगी नजर](https://www.livehindustan.com/business/icici-bank-net-profit-up-above-9-percent-in-q4-fy26-now-share-in-focus-201776540084302.html) · livehindustan.com |
| 18 Apr 2026 | Earnings | BANK’S NET PROFIT STOOD AT RS 13,701 CRORE IN THE QUARTER OF MARCH 2026 FROM JANUARY. | article unavailable |
| 18 Apr 2026 | Earnings | Profit before tax (PBT), excluding treasury, rose 10.1% year over year to INR 182.09 billion in Q4 FY2026, while core operating profit increased… | [ICICI Bank Q4 Earnings Call Highlights](https://www.themarketsdaily.com/2026/04/18/icici-bank-q4-earnings-call-highlights.html) · themarketsdaily.com |
| 18 Apr 2026 | Earnings | ICICI Bank reported a strong performance for the quarter ended March 2026 as it marked a 8.5% Year on Year (YoY) increase in net profit to ₹ 13,702… | [ICICI Bank Q4 Net Profit Jumps 8% YoY, ₹12 dividend declared - Hello…](https://helloentrepreneurs.com/business/icici-bank-q4-net-profit-jumps-8-yoy-rs-12-dividend-declared-82251/) · helloentrepreneurs.com |
| 18 Apr 2026 | Earnings | ICICI Bank on Saturday posted a consolidated net profit of Rs 14,755 crore for the fourth quarter of FY26, a 9 per cent year-on-year (YoY) rise. | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company icicibank.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company icicibank.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company icicibank.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company icicibank.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/icicibank.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "icicibank.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Coal India News](coal-india-news.md)
- [Paypal News](paypal-news.md)
- [Coinbase News](coinbase-news.md)
- [Spotify News](spotify-news.md)
