# Boeing News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “boeing news” · 3,600/month India · 33,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [boeing-news.json](../../examples/scenarios/boeing-news.json).

**Question.** What has the news reported about Boeing in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `boeing.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `boeing.com` |
| Headlines, Jan – Apr 2026 (estimate) | 7,652 |
| Events, May 2025 – Apr 2026 | 471 |
| Most frequent event types | Announcement (142), Contracts (125), Regulatory (44) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 26% · 1.9% · 72% of 7,652 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 3 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Air China (OTCMKTS:AIRYY) Trading Down 8.3% – Time to Sell?](https://www.tickerreport.com/banking-finance/13424280/air-china-otcmktsairyy-trading-down-8-3-time-to-sell.html) | tickerreport.com | 4 | negative | — |
| 30 Apr 2026 | [Biman Bangladesh Airlines Orders 10 Boeing 787s, Four MAX 8s \| Aviation Week Network](https://aviationweek.com/air-transport/airlines-lessors/biman-bangladesh-airlines-orders-10-boeing-787s-four-max-8s) | aviationweek.com | 5 | positive | — |
| 30 Apr 2026 | [Demand is strong, but airlines are facing an aging workforce](https://www.marketplace.org/story/2026/04/30/demand-is-strong-but-airlines-are-facing-an-aging-workforce%23demand-is-strong-but-airlines-are-facing-an-aging-workforce) | marketplace.org | 6 | negative | — |
| 30 Apr 2026 | [Rolls-Royce Maintains Buoyant 2026 Outlook Despite Middle East Uncertainty \| Aviation Week Network](https://aviationweek.com/air-transport/aircraft-propulsion/rolls-royce-maintains-buoyant-2026-outlook-despite-middle-east) | aviationweek.com | 7 | negative | Earnings |
| 30 Apr 2026 | [Biman Bangladesh Airlines Orders 14 Boeing 787 Dreamliner and 737 MAX Jets](https://www.nationaltribune.com.au/biman-bangladesh-airlines-orders-14-boeing-787-dreamliner-and-737-max-jets/) | nationaltribune.com.au | 7 | positive | — |
| 30 Apr 2026 | [US Air Force seeking long-range anti-ship missile deployed from transport aircraft](https://www.flightglobal.com/archive/2026/04/us-air-force-seeking-long-range-anti-ship-missile-deployed-from-transport-aircraft/) | flightglobal.com | 7 | negative | — |
| 30 Apr 2026 | [Bangladesh's flag carrier picks 14 Boeing jets to expand routes](https://www.stocktitan.net/news/BA/biman-bangladesh-airlines-orders-14-boeing-787-dreamliner-and-737-yiqylvvbszd1.html) | stocktitan.net | 5 | positive | — |
| 30 Apr 2026 | [Air India Express Restores Qatar, Bahrain Flights and Expands Gulf Network - IndUS Business Journal](https://indusbusinessjournal.com/2026/04/air-india-express-restores-qatar-bahrain-flights-and-expands-gulf-network/) | indusbusinessjournal.com | 6 | positive | Announcement |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Announcement | 142 |
| Contracts | 125 |
| Regulatory | 44 |
| Asset acquisition | 40 |
| Earnings | 29 |
| Key people | 27 |
| Lawsuit | 27 |
| Job creation | 21 |
| M&A | 9 |
| New product | 3 |
| Layoffs | 2 |
| Capital infusion | 1 |
| Board | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Announcement | Contracts | Regulatory | Asset acquisition |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 47 | 8 | 20 | 5 | 5 | ██████████████ |
| Jun 2025 | 30 | 13 | 0 | 3 | 0 | █████████ |
| Jul 2025 | 49 | 15 | 9 | 3 | 7 | ███████████████ |
| Aug 2025 | 55 | 10 | 15 | 7 | 8 | ████████████████ |
| Sep 2025 | 67 | 18 | 25 | 9 | 3 | ████████████████████ |
| Oct 2025 | 38 | 16 | 5 | 10 | 0 | ███████████ |
| Nov 2025 | 47 | 9 | 19 | 0 | 7 | ██████████████ |
| Dec 2025 | 30 | 10 | 2 | 6 | 3 | █████████ |
| Jan 2026 | 36 | 22 | 4 | 0 | 0 | ███████████ |
| Feb 2026 | 31 | 9 | 12 | 0 | 4 | █████████ |
| Mar 2026 | 9 | 2 | 3 | 1 | 1 | ███ |
| Apr 2026 | 32 | 10 | 11 | 0 | 2 | ██████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 7 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Contracts | The total cost of those 12 aircraft was around Tk19,020 crore. | [Biman strikes Boeing deal to buy 14 aircraft at $3.7b](https://www.tbsnews.net/economy/aviation/biman-signs-landmark-deal-boeing-buy-14-aircraft-1426441) · tbsnews.net |
| 30 Apr 2026 | Contracts | Boeing has secured 20,000 tonnes of permanent carbon dioxide removal through a structured procurement with Supercritical | [Boeing Secures 20,000 Tonnes of High-Quality Carbon Removal to…](https://esgnews.com/boeing-secures-20000-tonnes-of-high-quality-carbon-removal-to-tackle-aviation-emissions/) · esgnews.com |
| 28 Apr 2026 | Contracts | Panama City, April 28, 2026 /PRNewswire/ -- Boeing [NYSE: BA] and Copa Airlines today announced the Panamanian operator has ordered 40 737 MAX… | [Panama's Copa locks in 40 Boeing jets, with room for 20 more](https://www.stocktitan.net/news/BA/boeing-and-copa-airlines-announce-order-for-up-to-60-737-max-vk2cle5wbylv.html) · stocktitan.net |
| 25 Apr 2026 | Announcement | US manufacturer Boeing will have to make expensive and time-consuming modifications to approximately 30 airframes of the upcoming Boeing 777-9 that… | article unavailable |
| 24 Apr 2026 | Announcement | This week has been a good one for Boeing, with the firm publishing its first‑quarter results. This report featured the news that it expects the 737… | article unavailable |
| 23 Apr 2026 | Earnings | Revenue for the unit rose by 13 percent to $9.2bn for the quarter. | article unavailable |
| 23 Apr 2026 | Earnings | Boeing announced its earnings results on Wednesday. The aircraft producer reported ($0.20) EPS for the quarter, beating analysts’ consensus… | article unavailable |
| 22 Apr 2026 | Earnings | The company narrowed its net loss in the first three months of the year to $7 million, or 11 cents a share, down from a loss of $31 million, or 16… | article unavailable |
| 21 Apr 2026 | Earnings | Boeing (BA +1.81%) is scheduled to report first-quarter earnings tomorrow morning | article unavailable |
| 21 Apr 2026 | Contracts | Ethiopian Airlines has converted six Boeing 787-9 options, fully exercising commitments from its 2023 order. | [Ethiopian Airlines Firms Options On Six More 787s \| Aviation Week…](https://aviationweek.com/air-transport/airlines-lessors/ethiopian-airlines-firms-options-six-more-787s) · aviationweek.com |
| 21 Apr 2026 | Asset acquisition | Ethiopian Airlines, on Monday said it is buying six additional Boeing 787-9 Dreamliner jets as it looks to expand its long-haul flights across… | article unavailable |
| 21 Apr 2026 | Asset acquisition | The largest airline in Africa by passenger number and fleet size continues to grow with today's announcement that Ethiopian Airlines has purchased… | [Africa's Largest Boeing 787 Operator Firms Up 6 More Dreamliners](https://simpleflying.com/ethiopian-airlines-boeing-787-dreamliner-firm-order/) · simpleflying.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company boeing.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company boeing.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company boeing.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company boeing.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$PRISM_BUSINESS_API_BASE/v1/business/companies/boeing.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "boeing.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Openai News](openai-news.md)
- [Amazon News](amazon-news.md)
- [Tata Motors News](tata-motors-news.md)
- [Ola Electric News](ola-electric-news.md)
