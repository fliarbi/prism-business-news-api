# Samsung News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “samsung news” · 5,400/month India · 6,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [samsung-news.json](../../examples/scenarios/samsung-news.json).

**Question.** What has the news reported about Samsung in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `samsung.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `samsung.com` |
| Headlines, Jan – Apr 2026 (estimate) | 3,312 |
| Events, May 2025 – Apr 2026 | 421 |
| Most frequent event types | Announcement (168), Earnings (53), Contracts (49) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 25% · 0.5% · 74% of 3,312 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 1 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Air Products and Chemicals (NYSE:APD) Issues Earnings Results](https://www.tickerreport.com/banking-finance/13424257/air-products-and-chemicals-nyseapd-issues-earnings-results.html) | tickerreport.com | 5 | positive | — |
| 30 Apr 2026 | [Taiwan Semiconductor Manufacturing Company Ltd. $TSM Shares Acquired by Jennison Associates LLC](https://www.tickerreport.com/banking-finance/13424169/taiwan-semiconductor-manufacturing-company-ltd-tsm-shares-acquired-by-jennison-associates-llc.html) | tickerreport.com | 4 | positive | — |
| 30 Apr 2026 | [Apple, Amazon, Google, Meta and Microsoft: revenues of 541.8 billion](https://en.ilsole24ore.com/art/apple-amazon-google-meta-and-microsoft-revenues-5418-billion-AIG02MoC) | en.ilsole24ore.com | 8 | positive | — |
| 30 Apr 2026 | [The MATCH Act Is Industrial Policy Dressed as National Security - R Street Institute](https://www.rstreet.org/commentary/the-match-act-is-industrial-policy-dressed-as-national-security/) | rstreet.org | 7 | negative | — |
| 30 Apr 2026 | [Samsung's Lee family wealth doubles to $45.5B on AI chip boom as 30,000 workers demand profit share and…](https://thenextweb.com/news/samsung-dynasty-ai-boom-wealth-doubles) | thenextweb.com | 8 | positive | — |
| 30 Apr 2026 | [Qualcomm jumps as optimism on smartphones, AI chips outweigh dismal forecast](https://www.thestar.com.my/tech/tech-news/2026/04/30/qualcomm-shares-jump-as-optimism-on-smartphones-ai-chips-outweigh-dismal-forecast) | thestar.com.my | 7 | positive | — |
| 30 Apr 2026 | [Samsung's memory division posts massive profits for Q1, smartphones still profitable](https://www.gsmarena.com/samsungs_memory_division_posts_massive_profits_for_q1_smartphones_still_profitable-news-72628.php) | gsmarena.com | 7 | positive | Earnings |
| 30 Apr 2026 | [Samsung warns memory shortage will be worse next year](https://www.mashable.com/article/samsung-memory-shortage-ram-ai-worse-2027) | mashable.com | 6 | negative | — |
| 30 Apr 2026 | [Samsung says the RAM shortage could get even worse next year](https://www.theverge.com/tech/921190/samsung-ram-shortage-getting-worse-2027) | theverge.com | 7 | negative | — |
| 30 Apr 2026 | [Asia Intelligence Brief for Thursday, April 30, 2026](https://www.riotimesonline.com/asia-pulse-brent-samsung-boj-india-april-30-2026/) | riotimesonline.com | 8 | negative | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Announcement | 168 |
| Earnings | 53 |
| Contracts | 49 |
| Key people | 41 |
| New product | 29 |
| Lawsuit | 22 |
| M&A | 18 |
| Regulatory | 15 |
| Job creation | 9 |
| Capital infusion | 6 |
| Buyback | 5 |
| Asset acquisition | 4 |
| Funding round | 1 |
| Layoffs | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Announcement | Earnings | Contracts | Key people |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 36 | 13 | 0 | 2 | 3 | ███████████ |
| Jun 2025 | 10 | 2 | 1 | 1 | 1 | ███ |
| Jul 2025 | 57 | 12 | 9 | 22 | 0 | ██████████████████ |
| Aug 2025 | 59 | 29 | 3 | 6 | 9 | ██████████████████ |
| Sep 2025 | 23 | 4 | 2 | 2 | 4 | ███████ |
| Oct 2025 | 23 | 3 | 7 | 5 | 4 | ███████ |
| Nov 2025 | 42 | 18 | 1 | 0 | 16 | █████████████ |
| Dec 2025 | 18 | 9 | 2 | 1 | 0 | ██████ |
| Jan 2026 | 65 | 39 | 14 | 0 | 1 | ████████████████████ |
| Feb 2026 | 18 | 7 | 2 | 5 | 1 | ██████ |
| Mar 2026 | 18 | 10 | 0 | 1 | 1 | ██████ |
| Apr 2026 | 52 | 22 | 12 | 4 | 1 | ████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 1 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 29 Apr 2026 | Contracts | Greek buyers acquired the resale “Advantage Summit” – 158K/2026 Samsung for USD 120 mills each. | [More tankers and LNGs have been on the newbuilding ordering “menu”…](https://www.hellenicshippingnews.com/newbuilding-orders-picking-up-pace-in-the-wet-sector/) · hellenicshippingnews.com |
| 26 Apr 2026 | Regulatory | Samsung has applied to a court in South Korea for an injunction that would prohibit the company’s unionized employees from engaging in “illegal… | article unavailable |
| 25 Apr 2026 | Announcement | The complex is currently undergoing rapid expansion to meet surging global demand for memory chips. | [Samsung is making record profits. But why are employees leaving in…](https://koreajoongangdaily.joins.com/news/2026-04-26/business/industry/Samsung-is-making-record-profits-But-why-are-employees-leaving-in-droves-for-a-key-competitor/2577395) · koreajoongangdaily.joins.com |
| 24 Apr 2026 | Announcement | Elon Musk confirmed Samsung will produce the upgraded AI4+ self-driving chip for Tesla. Production set for mid-2027, bridging to the more powerful… | [Tesla & Samsung: AI4+ Chip Production Confirmed](https://www.newkerala.com/news/a/musk-confirms-samsung-will-produce-upgraded-ai4-self-driving-702.htm) · newkerala.com |
| 24 Apr 2026 | Announcement | The company recently announced progress in next generation HBM4 chips. | [Samsung Workers Demand 400K Per Person Bonuses And Threaten Massive…](https://wonderfulengineering.com/samsung-workers-demand-400k-per-person-bonuses-and-threaten-massive-strike-over-ai-profits/) · wonderfulengineering.com |
| 23 Apr 2026 | Announcement | Samsung, which together with SK Hynix produces about two-thirds of global memory chips, forecast earlier this month that its first-quarter operating… | [Samsung employees threaten strike, demand profit share amid AI boom](http://www.euronews.com/next/2026/04/23/samsung-employees-protest-and-threaten-strike-demanding-share-of-profits-amid-ai-boom) · euronews.com |
| 23 Apr 2026 | Announcement | Samsung, which together with SK Hynix produces about two-thirds of global memory chips, forecast earlier this month that its first‑quarter operating… | [Samsung workers rally in South Korea, demanding higher pay and…](https://economictimes.indiatimes.com/tech/technology/samsung-workers-rally-in-south-korea-demanding-higher-pay-and-threatening-to-strike/articleshow/130465568.cms) · economictimes.indiatimes.com |
| 23 Apr 2026 | Announcement | Samsung forecast earlier this month that its first-quarter operating profit would reach a record 57.2 trillion won (€33 billion). | [Samsung employees threaten strike, demand profit share amid AI boom](https://www.euronews.com/next/2026/04/23/samsung-employees-protest-and-threaten-strike-demanding-share-of-profits-amid-ai-boom) · euronews.com |
| 23 Apr 2026 | Announcement | Samsung has delivered the strongest quarterly performance in South Korean corporate history, propelled by a surge in demand for memory chips tied to… | [Samsung’s $203 billion question: Who gets what? - KED Global](https://www.kedglobal.com/deep-insights/newsView/ked202604220007) · kedglobal.com |
| 23 Apr 2026 | Announcement | Samsung, which together with SK Hynix produces about two‑thirds of global memory chips, forecast earlier this month that its first‑quarter operating… | [Samsung workers rally in South Korea, demanding higher pay and…](https://www.manilatimes.net/2026/04/23/business/foreign-business/samsung-workers-rally-in-south-korea-demanding-higher-pay-and-threatening-to-strike/2326784) · manilatimes.net |
| 23 Apr 2026 | Announcement | Samsung, forecast earlier this month that its first-quarter operating profit would reach a record 57.2 trillion won ($38.6 billion). | [Samsung workers rally in South Korea, demanding higher pay and…](https://www.wral.com/news/ap/38e7a-samsung-workers-rally-in-south-korea-demanding-higher-pay-and-threatening-to-strike/) · wral.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company samsung.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company samsung.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company samsung.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company samsung.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/samsung.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "samsung.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Jpmorgan News](jpmorgan-news.md)
- [SBI News](sbi-news.md)
- [Reliance Industries News](reliance-industries-news.md)
- [ITC News](itc-news.md)
