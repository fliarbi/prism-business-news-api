# Intel News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “intel news” · 6,600/month India · 40,500/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [intel-news.json](../../examples/scenarios/intel-news.json).

**Question.** What has the news reported about Intel in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `intel.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `intel.com` |
| Headlines, Jan – Apr 2026 (estimate) | 4,276 |
| Events, May 2025 – Apr 2026 | 304 |
| Most frequent event types | Key people (96), Earnings (47), Layoffs (43) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 24% · 0.3% · 75% of 4,276 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 3 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Top AI Stocks to Buy in the US 2026 for Long-Term Growth](https://www.analyticsinsight.net/stocks/top-ai-stocks-to-buy-in-the-us-2026-for-long-term-growth) | analyticsinsight.net | 8 | positive | — |
| 30 Apr 2026 | [The MATCH Act Is Industrial Policy Dressed as National Security - R Street Institute](https://www.rstreet.org/commentary/the-match-act-is-industrial-policy-dressed-as-national-security/) | rstreet.org | 7 | negative | — |
| 30 Apr 2026 | [Nvidia vs. Intel: Diverging Paths in Quarterly Revenue \| The Motley Fool](https://www.fool.com/coverage/charts/2026/04/30/nvidia-vs-intel-diverging-paths-in-quarterly-revenue/) | fool.com | 8 | positive | — |
| 30 Apr 2026 | [China blocks tech acquisitions to weaken America. The U.S. shouldn’t follow suit.](https://reason.com/2026/04/30/china-blocks-tech-acquisitions-to-weaken-america-the-u-s-shouldnt-follow-suit/) | reason.com | 8 | negative | — |
| 30 Apr 2026 | [State of New Jersey Common Pension Fund D Acquires 23,282 Shares of Intel Corporation $INTC](https://www.dailypolitical.com/2026/04/30/state-of-new-jersey-common-pension-fund-d-acquires-23282-shares-of-intel-corporation-intc.html) | dailypolitical.com | 4 | positive | — |
| 30 Apr 2026 | [North Star Investment Management Corp. Lowers Stock Position in Intel Corporation $INTC](https://www.dailypolitical.com/2026/04/30/north-star-investment-management-corp-lowers-stock-position-in-intel-corporation-intc.html) | dailypolitical.com | 4 | positive | — |
| 30 Apr 2026 | [GC Wealth Management RIA LLC Sells 58,113 Shares of Intel Corporation $INTC](https://www.dailypolitical.com/2026/04/30/gc-wealth-management-ria-llc-sells-58113-shares-of-intel-corporation-intc.html) | dailypolitical.com | 4 | positive | — |
| 30 Apr 2026 | [Dealer Playbook: 5 Takeaways for Auto Retailers Using AI](https://www.autoremarketing.com/whitepapers/dealer-playbook-5-takeaways-for-auto-retailers-using-ai/) | autoremarketing.com | 6 | positive | — |
| 30 Apr 2026 | [Stock Market Today (LIVE): Markets Close Out April With a Bang; Data Center Surprise Sends QCOM Up 15% \| The…](https://www.fool.com/investing/2026/04/30/stock-market-today-live-coverage/) | fool.com | 7 | negative | Earnings |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Key people | 96 |
| Earnings | 47 |
| Layoffs | 43 |
| M&A | 30 |
| Announcement | 26 |
| Contracts | 21 |
| Funding round | 9 |
| Asset acquisition | 9 |
| Regulatory | 8 |
| Capital infusion | 4 |
| Lawsuit | 3 |
| Job creation | 3 |
| New product | 2 |
| Board | 2 |
| Buyback | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Key people | Earnings | Layoffs | M&A |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 5 | 1 | 0 | 2 | 0 | ██ |
| Jun 2025 | 14 | 9 | 0 | 3 | 1 | █████ |
| Jul 2025 | 40 | 1 | 3 | 26 | 0 | █████████████ |
| Aug 2025 | 62 | 13 | 4 | 4 | 15 | ████████████████████ |
| Sep 2025 | 43 | 25 | 1 | 1 | 2 | ██████████████ |
| Oct 2025 | 26 | 1 | 14 | 4 | 3 | ████████ |
| Nov 2025 | 21 | 15 | 0 | 0 | 0 | ███████ |
| Dec 2025 | 18 | 5 | 0 | 2 | 4 | ██████ |
| Jan 2026 | 20 | 1 | 18 | 0 | 0 | ██████ |
| Feb 2026 | 7 | 2 | 0 | 1 | 0 | ██ |
| Mar 2026 | 10 | 7 | 1 | 0 | 0 | ███ |
| Apr 2026 | 38 | 16 | 6 | 0 | 5 | ████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 6 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Earnings | Intel (INTC 0.28%) just delivered the kind of quarter that rewrites the narrative on a struggling business. | [Stock Market Today (LIVE): Markets Close Out April With a Bang; Data…](https://www.fool.com/investing/2026/04/30/stock-market-today-live-coverage/) · fool.com |
| 30 Apr 2026 | Key people | Intel announced the appointment of João Bortone as CEO for Latin America. | article unavailable |
| 27 Apr 2026 | Earnings | Intel reported first-quarter 2026 revenue of $13.6 billion, a 7 per cent year-on-year increase, as demand for artificial intelligence (AI) and data… | [Intel Sees 7% YoY Revenue Growth in Q1 2026](https://www.electronicsforyou.biz/industry-buzz/intel-sees-7-yoy-revenue-growth-in-q1-2026/) · electronicsforyou.biz |
| 25 Apr 2026 | Earnings | Intel reported first-quarter 2026 results with revenue again beating expectations, marking a sixth consecutive quarter of outperformance as demand… | [Intel Q1 Results Highlight CPU Role In Expanding AI Stack -…](https://hostingjournalist.com/news/intel-q1-results-highlight-cpu-role-in-expanding-ai-stack) · hostingjournalist.com |
| 24 Apr 2026 | Earnings | It is forecasting revenue of up to $14.8 billion for Q2/2026. | [Why Investors Will Trade SAP, Intel, and ServiceNow Today](https://www.baystreet.ca/stockstowatch/23170/Why-Investors-Will-Trade-SAP-Intel-and-ServiceNow-Today) · baystreet.ca |
| 23 Apr 2026 | Earnings | Intel reported that it delivered a net loss of $3.7 billion on revenues of $13.6 billion in the quarter ending March 28, 2026. | article unavailable |
| 23 Apr 2026 | Earnings | The company provided earnings per share guidance of 0.200-0.200 for the period, compared to the consensus earnings per share estimate of 0.060. The… | [Intel (NASDAQ:INTC) Updates Q2 2026 Earnings Guidance](https://baseballnewssource.com/2026/04/23/intel-nasdaqintc-updates-q2-2026-earnings-guidance/11097598.html) · baseballnewssource.com |
| 23 Apr 2026 | Contracts | Tesla CEO Elon Musk said on Wednesday the EV maker plans to use Intel's next-generation 14A manufacturing process to make chips at its Terafab… | article unavailable |
| 20 Apr 2026 | Key people | Intel has appointed semiconductor industry veteran Shawn Han as senior vice president and general manager of foundry services. | article unavailable |
| 18 Apr 2026 | M&A | Intel CEO Li Bu Tan signed deals with Elon Musk’s Terafab and Google | [Intel CEO signs deals with Terafab, Google; acquires 49% stake in…](https://bitcoinethereumnews.com/tech/intel-ceo-signs-deals-with-terafab-google-acquires-49-stake-in-irish-fab/) · bitcoinethereumnews.com |
| 18 Apr 2026 | Contracts | Intel said it is proud to join the Terafab project with SpaceX, xAI and Tesla to refactor silicon fab technology. | article unavailable |
| 17 Apr 2026 | Key people | Intel this week announced that Shawn 'Seung Hoon' Han will join the company as senior vice president and general manager of Foundry Services, where… | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company intel.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company intel.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company intel.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company intel.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/intel.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "intel.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [TCS News](tcs-news.md)
- [Jio News](jio-news.md)
- [Infosys News](infosys-news.md)
- [Openai News](openai-news.md)
