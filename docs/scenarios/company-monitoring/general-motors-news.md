# General Motors News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “general motors news” · 260/month India · 9,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [general-motors-news.json](../../examples/scenarios/general-motors-news.json).

**Question.** What has the news reported about General Motors in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `gm.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `gm.com` |
| Headlines, Jan – Apr 2026 (estimate) | 1,864 |
| Events, May 2025 – Apr 2026 | 342 |
| Most frequent event types | Announcement (130), Earnings (48), Key people (44) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 40% · 0.5% · 59% of 1,864 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 4 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [General Motors announces $830 million investment at Romulus, Saginaw, Toledo sites](https://www.cbsnews.com/detroit/news/general-motors-830-million-investment-romulus-saginaw-toledo-sites/) | cbsnews.com | 7 | positive | Capital infusion |
| 30 Apr 2026 | [International Posts Q1 Loss on Sales Slump, One-Time Costs - TT](https://www.ttnews.com/articles/international-earnings-q1-2026) | ttnews.com | 5 | negative | — |
| 30 Apr 2026 | [Slotkin, Moreno introduce bill intended to ban connected vehicles from China, other countries in U.S.](https://www.cbsnews.com/detroit/news/slotkin-moreno-bill-ban-connected-vehicles-china/) | cbsnews.com | 7 | positive | — |
| 30 Apr 2026 | [ROX and JINGDONG Logistics anchor a next-day spare parts promise in Jebel Ali \| The National](https://thenational.ae/advertorial/2026/04/30/rox-and-jingdong-logistics-anchor-a-next-day-spare-parts-promise-in-jebel-ali/) | thenational.ae | 6 | positive | — |
| 30 Apr 2026 | [Automakers Expect $2.3 Billion In Tariff Refunds Whether Trump Likes It Or Not - Jalopnik](https://www.jalopnik.com/2161072/automakers-expect-billion-dollar-tariff-refunds-despite-testy-trump/) | jalopnik.com | 8 | negative | — |
| 30 Apr 2026 | [GM Invests $500 Million For A Third V8 Production Plant](https://www.autoguide.com/auto/manufacturers/gm/gm-invests-500-million-for-a-third-v8-production-plant-44632492) | autoguide.com | 7 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Announcement | 130 |
| Earnings | 48 |
| Key people | 44 |
| Layoffs | 25 |
| Job creation | 21 |
| Contracts | 18 |
| Lawsuit | 12 |
| New product | 12 |
| Capital infusion | 11 |
| Regulatory | 8 |
| Asset acquisition | 6 |
| M&A | 4 |
| Buyback | 3 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Announcement | Earnings | Key people | Layoffs |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 32 | 12 | 4 | 8 | 2 | ████████ |
| Jun 2025 | 15 | 5 | 0 | 5 | 0 | ████ |
| Jul 2025 | 30 | 12 | 10 | 0 | 0 | ███████ |
| Aug 2025 | 81 | 31 | 7 | 5 | 3 | ████████████████████ |
| Sep 2025 | 16 | 13 | 0 | 0 | 0 | ████ |
| Oct 2025 | 61 | 16 | 9 | 3 | 16 | ███████████████ |
| Nov 2025 | 13 | 2 | 0 | 9 | 2 | ███ |
| Dec 2025 | 16 | 3 | 0 | 9 | 1 | ████ |
| Jan 2026 | 23 | 9 | 10 | 2 | 0 | ██████ |
| Feb 2026 | 18 | 6 | 2 | 3 | 0 | ████ |
| Mar 2026 | 6 | 5 | 0 | 0 | 1 | █ |
| Apr 2026 | 31 | 16 | 6 | 0 | 0 | ████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 3 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Capital infusion | Saginaw Metal Casting Operations: A $150 million investment was recently announced for this Michigan site to increase production of engine blocks… | [General Motors announces $830 million investment at Romulus,…](https://www.cbsnews.com/detroit/news/general-motors-830-million-investment-romulus-saginaw-toledo-sites/) · cbsnews.com |
| 30 Apr 2026 | Capital infusion | General Motors is pouring $680 million into two U.S. plants and another half a billion into a plant in Canada to increase production of… | [GM to pour millions into Michigan, Ohio plants for truck, SUV parts](https://www.freep.com/story/money/cars/general-motors/2026/04/29/gm-1b-michigan-ohio-canada-parts-plants/89864333007/) · freep.com |
| 28 Apr 2026 | Regulatory | General Motors expects to receive a $500 million refund of customs duties after the Supreme Court has invalidated some of President Donald Trump's… | [Droits de douane américains \| GM espère obtenir un remboursement de…](https://www.lapresse.ca/affaires/2026-04-28/droits-de-douane-americains/gm-espere-obtenir-un-remboursement-de-500-millions.php) · lapresse.ca |
| 28 Apr 2026 | Regulatory | The court in February ruled that the levies Trump imposed using the International Emergency Economic Powers Act, or IEEPA, were illegal. | article unavailable |
| 28 Apr 2026 | Earnings | General Motors Co. in Detroit today reported first-quarter 2026 revenue of $43.6 billion, net income attributable to stockholders of $2.6 billion,… | article unavailable |
| 28 Apr 2026 | Earnings | GM posted Q1 revenue of $43.62 billion, against an estimated $43.68 billion, down slightly from the $44 billion reported a year ago. The company… | [GM earnings top estimates, company raises profit forecast after…](https://finance.yahoo.com/markets/article/gm-earnings-top-estimates-company-raises-profit-forecast-after-supreme-court-ruling-reduces-tariff-costs-143121594.html) · finance.yahoo.com |
| 28 Apr 2026 | Earnings | Metric (GAAP unless noted) Q1 2026 Q1 2025 Y/Y Change EPS – Diluted Adjusted (Non-GAAP) $3.70 $2.78 +33% Revenue (billions) $43 $44 (0.9%) Net… | article unavailable |
| 28 Apr 2026 | Earnings | Here are the first-quarter numbers GM reported: Net income of $2.63 billion, down 5.7% compared with the prior year’s quarter of $2.78 billion.… | [GM posts strong earnings for Q1 despite costs from tariffs, suppliers](https://www.freep.com/story/money/cars/general-motors/2026/04/28/gm-earnings-q1-first-quarter-software-services/89811911007/) · freep.com |
| 28 Apr 2026 | Earnings | General Motors (NYSE: GM ) today reported first-quarter 2026 revenue of $43.6 billion , net income attributable to stockholders of $2.6 billion ,… | [GM trims tariff hit after court ruling, keeps $0.18 dividend](https://www.stocktitan.net/news/GM/gm-releases-2026-first-quarter-results-declares-quarterly-mociz0sv0yox.html) · stocktitan.net |
| 28 Apr 2026 | Regulatory | General Motors expects to receive roughly $500 million in tariff refunds from the federal government following the US Supreme Court’s decision to… | [Tariff refunds could provide relief for companies facing margin…](https://www.emarketer.com/content/gm-tariff-refunds-supreme-court-impact) · emarketer.com |
| 22 Apr 2026 | Announcement | General Motors Co. has indefinitely delayed development of its next-generation full-size electric trucks, including refreshed versions of the… | [GM Suspends Next-Gen Electric Trucks as It Pivots to Gas Engines and…](https://www.ibtimes.com/gm-suspends-next-gen-electric-trucks-it-pivots-gas-engines-hybrids-amid-slowing-ev-demand-3801731) · ibtimes.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company gm.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company gm.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company gm.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company gm.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/gm.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "gm.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Tata Steel News](tata-steel-news.md)
- [Paytm News](paytm-news.md)
- [Palantir News](palantir-news.md)
- [Qualcomm News](qualcomm-news.md)
