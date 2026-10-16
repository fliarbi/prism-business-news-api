# Bank Results: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “bank results” · 1,300/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [bank-results.json](../../examples/scenarios/bank-results.json).

**Question.** How many bank results events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `earnings` and the word “bank” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 2,465 |
| Companies (with a domain) | 719 |
| Source articles | 2,128 |
| Busiest month | Jul 2025 (392 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 13% · 1.2% · 85% of 3,306 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 215 | ███████████ |
| Jun 2025 | 39 | ██ |
| Jul 2025 | 392 | ████████████████████ |
| Aug 2025 | 324 | █████████████████ |
| Sep 2025 | 48 | ██ |
| Oct 2025 | 321 | ████████████████ |
| Nov 2025 | 127 | ██████ |
| Dec 2025 | 39 | ██ |
| Jan 2026 | 330 | █████████████████ |
| Feb 2026 | 196 | ██████████ |
| Mar 2026 | 65 | ███ |
| Apr 2026 | 369 | ███████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 5 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | bancochile.cl | Earnings | The bank reported $0.57 EPS for the quarter, missing the consensus estimate of $0.58 by ($0.01), FiscalAI reports. | [Banco De Chile (NYSE:BCH) Posts Earnings Results, Misses Estimates…](https://www.tickerreport.com/banking-finance/13424255/banco-de-chile-nysebch-posts-earnings-results-misses-estimates-by-0-01-eps.html) · tickerreport.com |
| 30 Apr 2026 | mashreqbank.com | Earnings | Mashreq Bank, one of the leading financial institutions in the MENA region, has delivered a strong first-quarter performance, with operating income… | article unavailable |
| 30 Apr 2026 | wemabank.com | Earnings | Wema Bank Plc reported a profit after tax of ₦63.13 billion for the first quarter (Q1) ended March 31, 2026, representing a 76.1 percent increase… | [Wema Bank Profit Rises To ₦63.13 Billion As Interest Income Drives…](https://investorsking.com/2026/04/30/wema-bank-profit-rises-to-%e2%82%a663-13-billion-as-interest-income-drives-strong-q1-2026-performance/) · investorsking.com |
| 30 Apr 2026 | crdbbank.com | Earnings | CRDB Bank Plc has cemented its position as the undisputed leader in Tanzania’s banking sector, after reporting a Profit After Tax (PAT) of Sh206… | [CRDB Bank becomes undisputed market leader as Q1 profit surges to…](https://www.thecitizen.co.tz/tanzania/supplement/crdb-bank-becomes-undisputed-market-leader-as-q1-profit-surges-to-sh206-billion--5442062) · thecitizen.co.tz |
| 30 Apr 2026 | indianbank.in | Earnings | Indian Bank reported its quarterly results on April 29. | article unavailable |
| 30 Apr 2026 | idbibank.in | Earnings | Shares of IDBI Bank fell around 3 per cent from day’s high after the LIC-promoted lender reported a 5.26 per cent year-on-year (YoY) drop in net… | article unavailable |
| 30 Apr 2026 | idbibank.in | Earnings | IDBI Bank reported a standalone net profit of ₹1,943.2 crore in the fourth quarter of FY26, registering a fall of 5.3% from ₹2,051.2 crore in the… | article unavailable |
| 30 Apr 2026 | nbp.com.pk | Earnings | National Bank of Pakistan (PSX: NBP) reported a 26% decline in its consolidated profit after taxation for the first quarter ended March 31, 2026,… | [MG Morning Breeze: Updates to Skim before Market](https://mettisglobal.news/MG-Morning-Breeze-Updates-to-Skim-before-Market-60114) · mettisglobal.news |
| 30 Apr 2026 | jsbl.com | Earnings | JS Bank Limited (PSX: JSBL) reported a 62.68% year-on-year contraction in profit after taxation for the three months ended March 31, 2026, recording… | [MG Morning Breeze: Updates to Skim before Market](https://mettisglobal.news/MG-Morning-Breeze-Updates-to-Skim-before-Market-60114) · mettisglobal.news |
| 30 Apr 2026 | federalbank.co.in | Earnings | The lender reported a 22 percent rise in consolidated net profit for the quarter ended March, led by stronger core earnings. The Kochi-based bank… | [Risk reward 'less favourable' for this Jhunjhunwala stock post Q4…](https://www.businesstoday.in/markets/stocks/story/risk-reward-less-favourable-for-this-jhunjhunwala-stock-post-q4-earnings-buy-or-sell-528155-2026-04-30) · businesstoday.in |
| 30 Apr 2026 | finobank.com | Earnings | "Fino Payments Bank: The private lender’s net profit sank 70.4 per cent YoY to Rs 7.1 crore, while revenue grew 31.5 per cent YoY to Rs 35.2 crore… | [Top stocks in news: Bajaj Finance, Vedanta, L&T, Indegene,…](https://www.businesstoday.in/markets/stocks/story/top-stocks-in-news-bajaj-finance-vedanta-lt-indegene-schaeffler-moil-hindzinc-hul-528123-2026-04-30) · businesstoday.in |
| 29 Apr 2026 | finobank.com | Earnings | Fino Payments Bank net profit for the quarter ended March 31, 2026 (Q4 FY26) plummeted 70% to ₹7.1 Cr from ₹24 Cr in the year-ago quarter. | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type earnings --q bank --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type earnings --q bank --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type earnings --q bank --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["earnings"], "q": "bank", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["earnings"], "q": "bank", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Article filters require a matching source article in the same window; records without a matching article are excluded. Each deal still counts once.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.
- Zero-count periods are included; partial_period marks buckets only partly covered by the window.
- shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)

## Related demonstrations

- [Dividend Announcement](dividend-announcement.md)
- [AI Partnership](ai-partnership.md)
- [SEBI Order](sebi-order.md)
- [Capital Infusion](capital-infusion.md)
