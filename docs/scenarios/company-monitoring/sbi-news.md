# SBI News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “sbi news” · 12,100/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [sbi-news.json](../../examples/scenarios/sbi-news.json).

**Question.** What has the news reported about SBI in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `sbi.co.in`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `sbi.co.in` |
| Headlines, Jan – Apr 2026 (estimate) | 2,017 |
| Events, May 2025 – Apr 2026 | 20 |
| Most frequent event types | Earnings (11), Key people (3), Contracts (2) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 28% · 2.6% · 69% of 2,017 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 5 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [BT Closing Bell \| Sensex settles 582 pts lower, Nifty below 24,000; Eternal, HUL lead index losers -…](https://www.businesstoday.in/markets/stocks/story/bt-closing-bell-sensex-settles-582-pts-lower-nifty-below-24000-eternal-hul-lead-index-losers-528248-2026-04-30) | businesstoday.in | 7 | negative | — |
| 30 Apr 2026 | [Infosys Falls Out of India’s Top 10 Most Valuable Companies](https://www.indianweb2.com/2026/04/infosys-falls-out-of-indias-top-10-most.html) | indianweb2.com | 7 | negative | — |
| 29 Apr 2026 | [Asia Intelligence Brief for Wednesday, April 29, 2026](https://www.riotimesonline.com/asia-pulse-sk-hynix-softbank-china-india-april-2026/) | riotimesonline.com | 8 | positive | IPO |
| 29 Apr 2026 | [ICICI Bank enables facial recognition, fingerprint authentication services for UPI transactions up to Rs…](https://economictimes.indiatimes.com/wealth/save/icici-bank-enables-biometric-authentication-for-upi-transactions-up-to-rs-5000-how-to-activate-service-on-imobile-app/articleshow/130604696.cms) | economictimes.indiatimes.com | 7 | positive | — |
| 29 Apr 2026 | [BT Closing Bell \| Sensex settles 609 pts higher, Nifty above 24,150; ITC, Tech Mahindra lead index gainers -…](https://www.businesstoday.in/markets/stocks/story/bt-closing-bell-sensex-settles-609-pts-higher-nifty-above-24150-itc-tech-mahindra-lead-index-gainers-528048-2026-04-29) | businesstoday.in | 6 | positive | — |
| 29 Apr 2026 | [Sensex, Nifty end higher as Q4 earnings boost outweighs crude oil surge](https://www.indiatoday.in/business/market/story/market-closing-bell-sensex-ends-609-points-higher-nifty-tops-24100-ril-maruti-itc-up-3-2903218-2026-04-29) | indiatoday.in | 6 | positive | — |
| 29 Apr 2026 | [Suzlon Energy, Tata Power, GRSE, Bandhan Bank shares: Globe Capital's Gaurav Sharma weighs in on targets -…](https://www.businesstoday.in/markets/stocks/story/suzlon-energy-tata-power-grse-bandhan-bank-shares-globe-capitals-gaurav-sharma-weighs-in-on-targets-527985-2026-04-29) | businesstoday.in | 6 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 11 |
| Key people | 3 |
| Contracts | 2 |
| Lawsuit | 2 |
| Announcement | 1 |
| Capital infusion | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Key people | Contracts | Lawsuit |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2 | 2 | 0 | 0 | 0 | ████████ |
| Jun 2025 | 1 | 0 | 0 | 0 | 0 | ████ |
| Jul 2025 | 0 | 0 | 0 | 0 | 0 |  |
| Aug 2025 | 5 | 5 | 0 | 0 | 0 | ████████████████████ |
| Sep 2025 | 1 | 1 | 0 | 0 | 0 | ████ |
| Oct 2025 | 0 | 0 | 0 | 0 | 0 |  |
| Nov 2025 | 1 | 0 | 0 | 0 | 0 | ████ |
| Dec 2025 | 1 | 0 | 1 | 0 | 0 | ████ |
| Jan 2026 | 4 | 1 | 1 | 2 | 0 | ████████████████ |
| Feb 2026 | 2 | 2 | 0 | 0 | 0 | ████████ |
| Mar 2026 | 1 | 0 | 1 | 0 | 0 | ████ |
| Apr 2026 | 2 | 0 | 0 | 0 | 2 | ████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 5 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 27 Apr 2026 | Lawsuit | In 2018, ICICI Bank filed the first insolvency petition against JAL, followed by SBI in 2022. | article unavailable |
| 20 Apr 2026 | Lawsuit | The agency had registered a case following a complaint by SBI, accusing RCOM, its promoter Anil Ambani, and others of fraudulent diversion of loan… | [CBI arrests two RCOM senior executives in bank fraud case](https://indianexpress.com/article/india/cbi-arrests-two-rcom-senior-executives-in-bank-fraud-case-10646986/) · indianexpress.com |
| 17 Mar 2026 | Key people | Chugh had stepped down from his role as Deputy Managing Director and Head (Digital Banking and Transformation) at SBI on March 2, 2026, after his… | [Perfios appoints Nitin Chugh as the group CEO - The Economic Times](https://economictimes.indiatimes.com/tech/startups/perfios-appoints-nitin-chugh-as-the-group-ceo/articleshow/129636470.cms) · economictimes.indiatimes.com |
| 12 Feb 2026 | Earnings | The bank posted a record net profit of Rs. 21,028 crore in Q3 FY26. | article unavailable |
| 9 Feb 2026 | Earnings | SBI reported a net profit of over Rs. 21,000 crore in Q3 FY26, a year-on-year growth of nearly 25% | [SBI Share Price Up 6.9% at Rs. 1,140 on Strong Q3 FY26 Results](https://www.analyticsinsight.net/stocks/sbi-share-price-up-69-at-rs-1140-on-strong-q3-fy26-results) · analyticsinsight.net |
| 31 Jan 2026 | Earnings | SBI’s profits alone crossed Rs 79,000 crore. | article unavailable |
| 7 Jan 2026 | Contracts | Cash logistics-focused CMS Info Systems on Wednesday said it has bagged a ₹1,000-crore deal from SBI to look after 5,000 automated teller machines… | article unavailable |
| 7 Jan 2026 | Contracts | Cash logistics-focused CMS Info Systems on Wednesday said it has bagged a ₹1,000-crore deal from SBI to look after 5,000 automated teller machines… | article unavailable |
| 5 Jan 2026 | Key people | In 2022, SBI hired Nitin Chugh as deputy managing director and head of digital payments. | [Staff at your neighbourhood PSU bank is working harder than you…](https://www.livemint.com/industry/banking/india-public-sector-bank-employee-productivity-private-sector-11767514556546.html) · livemint.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company sbi.co.in --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company sbi.co.in --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company sbi.co.in --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company sbi.co.in --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/sbi.co.in/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "sbi.co.in", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Meta News](meta-news.md)
- [Jpmorgan News](jpmorgan-news.md)
- [Samsung News](samsung-news.md)
- [Reliance Industries News](reliance-industries-news.md)
