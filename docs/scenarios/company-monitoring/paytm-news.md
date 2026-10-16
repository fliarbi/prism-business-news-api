# Paytm News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “paytm news” · 9,900/month India · 70/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [paytm-news.json](../../examples/scenarios/paytm-news.json).

**Question.** What has the news reported about Paytm in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `paytm.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `paytm.com` |
| Headlines, Jan – Apr 2026 (estimate) | 672 |
| Events, May 2025 – Apr 2026 | 65 |
| Most frequent event types | Earnings (34), Key people (13), Regulatory (6) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 22% · 0.9% · 77% of 672 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 6 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Amazon, Meta join fight to end Google Pay, PhonePe dominance in India \| TechCrunch](https://techcrunch.com/2026/04/29/amazon-meta-join-fight-to-end-google-pay-phonepe-dominance-in-india/) | techcrunch.com | 8 | positive | — |
| 29 Apr 2026 | [Why RBI Cancelled Paytm Payments Bank Licence: Vijay Shekhar Sharma Exit And Fintech Shake-Up Explained](https://www.newsx.com/business/why-rbi-cancelled-paytm-payments-bank-licence-vijay-shekhar-sharma-exit-and-fintech-shake-up-explained-207198/) | newsx.com | 8 | negative | — |
| 29 Apr 2026 | [Paytm’s post-PPBL pivot: How the shift to multi-bank model shielded it from Payments Bank ban fallout](https://www.financialexpress.com/business/industry-paytms-post-ppbl-pivot-how-the-shift-to-multi-bank-model-shielded-it-from-payments-bank-ban-fallout-4221758/) | financialexpress.com | 8 | negative | — |
| 28 Apr 2026 | [RBI Revokes Paytm Payments Bank Licence](https://paymentsindustryintelligence.com/rbi-revokes-paytm-payments-bank-licence/) | paymentsindustryintelligence.com | 8 | negative | — |
| 28 Apr 2026 | [Paytm stock: Up 40% from 52 week low, should you 'buy' after Payments Bank licence issue? - BusinessToday](https://www.businesstoday.in/markets/stocks/story/paytm-stock-up-from-52-week-low-should-you-buy-after-payments-bank-licence-issue-527830-2026-04-28) | businesstoday.in | 7 | negative | — |
| 28 Apr 2026 | [Word of the Day: ONDC (Open Network for Digital Commerce) - Indian Retailer](https://www.indianretailer.com/news/word-day-ondc-open-network-digital-commerce) | indianretailer.com | 6 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 34 |
| Key people | 13 |
| Regulatory | 6 |
| Lawsuit | 2 |
| New product | 2 |
| Job creation | 2 |
| M&A | 1 |
| Announcement | 1 |
| Contracts | 1 |
| Funding round | 1 |
| IPO | 1 |
| Layoffs | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Key people | Regulatory | Lawsuit |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 10 | 2 | 4 | 0 | 2 | █████████ |
| Jun 2025 | 0 | 0 | 0 | 0 | 0 |  |
| Jul 2025 | 23 | 17 | 5 | 0 | 0 | ████████████████████ |
| Aug 2025 | 7 | 1 | 1 | 1 | 0 | ██████ |
| Sep 2025 | 1 | 0 | 0 | 0 | 0 | █ |
| Oct 2025 | 3 | 1 | 0 | 0 | 0 | ███ |
| Nov 2025 | 6 | 5 | 0 | 1 | 0 | █████ |
| Dec 2025 | 1 | 0 | 0 | 1 | 0 | █ |
| Jan 2026 | 9 | 6 | 2 | 1 | 0 | ████████ |
| Feb 2026 | 2 | 2 | 0 | 0 | 0 | ██ |
| Mar 2026 | 1 | 0 | 0 | 1 | 0 | █ |
| Apr 2026 | 2 | 0 | 1 | 1 | 0 | ██ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 6 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 10 Apr 2026 | Key people | Rakesh Menon has joined Paytm as assistant vice president – lending, taking on a new role focused on strengthening the company’s lending and credit… | [Rakesh Menon joins Paytm as avp – lending](https://indiantelevision.com/mam/rakesh-menon-joins-paytm-as-avp-lending/) · indiantelevision.com |
| 7 Apr 2026 | Regulatory | RBI's new guidelines on digital lending eliminate a significant regulatory burden from Paytm and are consistent with the fintech giant's financial… | article unavailable |
| 17 Mar 2026 | Regulatory | Financial technology company Paytm was hit with a compounding order worth INR 18.8 lakh last month by the central bank. | [RBI Imposes Penalty on Cashfree Over Compliance Breach](https://startuptalky.com/news/reserve-bank-of-india-imposes-penalty-on-cashfree/) · startuptalky.com |
| 12 Feb 2026 | Earnings | On a consolidated basis, it posted a net profit of ₹225 crore during the quarter under review. | article unavailable |
| 9 Feb 2026 | Earnings | Paytm reported a sharp turnaround in H1 FY26, taking total H1 FY26 profit to ₹144 crore. | article unavailable |
| 31 Jan 2026 | Key people | Saujanya Shrivastava has shared on LinkedIn that he has been named as the CEO - New Initiatives at Paytm. | [Saujanya Shrivastava appointed CEO - New Initiatives at Paytm -…](https://www.exchange4media.com/people-movement-news/saujanya-shrivastava-appointed-ceo-new-initiatives-at-paytm-151525.html) · exchange4media.com |
| 31 Jan 2026 | Key people | Paytm has appointed Saujanya Shrivastava as ceo, new initiatives, strengthening its leadership bench as the company sharpens its focus on building… | [Paytm names Saujanya Shrivastava as ceo, new initiatives](https://indiantelevision.com/mam/paytm-names-saujanya-shrivastava-as-ceo-new-initiatives/) · indiantelevision.com |
| 30 Jan 2026 | Earnings | On Friday, Paytm reported a profit after tax of ₹225 crore in the December quarter compared with a loss a year earlier and a profit of ₹21 crore in… | article unavailable |
| 30 Jan 2026 | Earnings | Paytm shares fell around 5% in early trade despite reporting a strong operational performance in Q3 FY26. | [Paytm Shares Slide Nearly 5% Despite Solid Q3 Showing, Highlighting…](https://startupnews.fyi/business/paytm-stock-falls-despite-strong-q3) · startupnews.fyi |
| 30 Jan 2026 | Earnings | Consolidated net income was ₹225 crore ($24.5 million) in the quarter through December, Paytm said Thursday in a disclosure to stock exchanges.… | article unavailable |
| 30 Jan 2026 | Earnings | Paytm Q3FY26 net profit at Rs 225 crore, revenue up 20% to Rs 2,194 crore | article unavailable |
| 29 Jan 2026 | Earnings | Revenue from operations jumped 20% to INR 2,194 Cr in Q3 FY26 from INR 1,828 Cr in the same period last year. | [Paytm Q3: Profit At INR 225 Cr, Revenue Jumps 20% YoY](https://inc42.com/buzz/paytm-q3-posts-inr-225-cr-profit-revenue-jumps-20-yoy/) · inc42.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company paytm.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company paytm.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company paytm.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company paytm.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/paytm.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "paytm.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [ITC News](itc-news.md)
- [Tata Steel News](tata-steel-news.md)
- [General Motors News](general-motors-news.md)
- [Palantir News](palantir-news.md)
