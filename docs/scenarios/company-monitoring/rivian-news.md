# Rivian News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “rivian news” · 260/month India · 18,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [rivian-news.json](../../examples/scenarios/rivian-news.json).

**Question.** What has the news reported about Rivian in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `rivian.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `rivian.com` |
| Headlines, Jan – Apr 2026 (estimate) | 270 |
| Events, May 2025 – Apr 2026 | 97 |
| Most frequent event types | Earnings (27), Announcement (25), Job creation (11) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 23% · 0.4% · 76% of 270 articles |
| Funding records, Jan – Apr 2026 | 3 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 2 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Rivian’s revenue is up as R2 production kicks into gear](https://www.theverge.com/transportation/921295/rivian-q1-2026-earnings-revenue-profit-r2) | theverge.com | 7 | positive | Earnings |
| 30 Apr 2026 | [Rivian downsizes new EV factory after Trump’s DOE slashes loan agreement](https://www.theverge.com/transportation/921585/rivian-georgia-factory-capacity-doe-loan) | theverge.com | 7 | negative | Capital infusion |
| 29 Apr 2026 | [America's Auto CEOs Saw Record Pay In 2025. These Were The Top Earners](https://www.motor1.com/news/794340/highest-paid-automotive-ceos-2025-america/) | motor1.com | 8 | positive | Earnings |
| 28 Apr 2026 | [RJ Scaringe Net Worth \| Celebrity Net Worth](https://www.celebritynetworth.com/richest-businessmen/ceos/rj-scaringe-net-worth/) | celebritynetworth.com | 6 | positive | — |
| 25 Apr 2026 | [Automotive Stocks To Follow Now – April 25th](https://www.watchlistnews.com/automotive-stocks-to-follow-now-april-25th/11059607.html) | watchlistnews.com | 5 | positive | — |
| 25 Apr 2026 | [Top Electric Vehicle Stocks Worth Watching – April 24th](https://www.watchlistnews.com/top-electric-vehicle-stocks-worth-watching-april-24th/11059513.html) | watchlistnews.com | 6 | positive | — |
| 23 Apr 2026 | [Rivian Automotive (NASDAQ:RIVN) Trading Up 1.4% – Here’s Why](https://www.thelincolnianonline.com/2026/04/23/rivian-automotive-nasdaqrivn-trading-up-1-4-heres-why.html) | thelincolnianonline.com | 4 | positive | — |
| 23 Apr 2026 | [Top Automotive Stocks To Follow Now – April 22nd](https://www.dailypolitical.com/2026/04/23/top-automotive-stocks-to-follow-now-april-22nd.html) | dailypolitical.com | 5 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 27 |
| Announcement | 25 |
| Job creation | 11 |
| Key people | 9 |
| Layoffs | 6 |
| Funding round | 5 |
| Contracts | 4 |
| Capital infusion | 4 |
| Lawsuit | 3 |
| Regulatory | 2 |
| M&A | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Announcement | Job creation | Key people |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 9 | 3 | 1 | 3 | 0 | ████████ |
| Jun 2025 | 2 | 0 | 0 | 0 | 0 | ██ |
| Jul 2025 | 6 | 0 | 2 | 2 | 0 | █████ |
| Aug 2025 | 9 | 2 | 2 | 2 | 2 | ████████ |
| Sep 2025 | 9 | 0 | 2 | 4 | 1 | ████████ |
| Oct 2025 | 11 | 1 | 2 | 0 | 0 | ██████████ |
| Nov 2025 | 6 | 4 | 1 | 0 | 0 | █████ |
| Dec 2025 | 2 | 0 | 2 | 0 | 0 | ██ |
| Jan 2026 | 7 | 1 | 1 | 0 | 4 | ██████ |
| Feb 2026 | 22 | 12 | 8 | 0 | 1 | ████████████████████ |
| Mar 2026 | 6 | 0 | 1 | 0 | 1 | █████ |
| Apr 2026 | 8 | 4 | 3 | 0 | 0 | ███████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 5 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Earnings | In terms of earnings, Rivian said it brought in $1.38 billion in revenue, an 11.3 percent increase compared to the $1.24 billion in Q1 2025. | [Rivian’s revenue is up as R2 production kicks into gear](https://www.theverge.com/transportation/921295/rivian-q1-2026-earnings-revenue-profit-r2) · theverge.com |
| 30 Apr 2026 | Capital infusion | DOE will now loan Rivian $4.5 billion, instead of the originally agreed amount of $6.6 billion | [Rivian downsizes new EV factory after Trump’s DOE slashes loan…](https://www.theverge.com/transportation/921585/rivian-georgia-factory-capacity-doe-loan) · theverge.com |
| 29 Apr 2026 | Earnings | Rivian 2025 Revenue: $5.4 Billion | [America's Auto CEOs Saw Record Pay In 2025. These Were The Top Earners](https://www.motor1.com/news/794340/highest-paid-automotive-ceos-2025-america/) · motor1.com |
| 22 Apr 2026 | Announcement | A tornado struck Rivian’s electric vehicle factory in Normal, Illinois, last Friday, temporarily halting operations at a newer section of the… | article unavailable |
| 8 Apr 2026 | Earnings | Rivian still reported a net income margin of approximately -63% for the quarter ended Dec. 31, 2025. | article unavailable |
| 3 Apr 2026 | Announcement | "Rivian is also reaffirming its 2026 delivery range guidance of 62,000 to 67,000 vehicles," the company added. | article unavailable |
| 2 Apr 2026 | Earnings | Rivian has released its first-quarter 2026 production and delivery results, offering a steady start to the year as the company continues to scale… | [Rivian Delivers 10,365 EVs in Q1 2026, Holds Firm on Full-Year Outlook](https://driveteslacanada.ca/news/rivian-delivers-10365-evs-in-q1-2026-holds-firm-on-full-year-outlook/) · driveteslacanada.ca |
| 2 Apr 2026 | Announcement | the electric vehicle startup reiterated its full-year guidance of 62,000-67,000 deliveries. | [Rivian beats Q1 delivery estimates as R2 rollout begins \| Automotive…](https://www.automotiveworld.com/news/rivian-beats-q1-delivery-estimates-as-r2-rollout-begins/) · automotiveworld.com |
| 30 Mar 2026 | Key people | Hensler announced he was rejoining the US EV maker via LinkedIn on Sunday. | [Rivian Rehires Former Engineer as Commercial Van Chief After Eight…](https://eletric-vehicles.com/rivian/rivian-rehires-former-engineer-as-commercial-van-chief-after-eight-months-at-gm/) · eletric-vehicles.com |
| 27 Mar 2026 | Funding round | The German automotive giant has already invested a little more than $3 billion in Rivian as part of the joint venture. | [Rivian gets another $1B from Volkswagen \| TechCrunch](https://techcrunch.com/2026/03/27/rivian-gets-another-1b-from-volkswagen/) · techcrunch.com |
| 19 Mar 2026 | Announcement | Rivian no longer expects to hit its long‑standing profitability target by 2027, and the company now links that delay directly to rising spending on… | article unavailable |
| 19 Mar 2026 | Capital infusion | Uber plans to invest up to $1.25 billion in electric vehicle maker Rivian to deploy as many as 50,000 autonomous robotaxis through 2031, the… | article unavailable |

## Funding records, Jan – Apr 2026

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 27 Mar 2026 | Rivian (rivian.com) | debt financing | $1B | volkswagen group | Germany | Rivian will be able to borrow up to $1 billion from Volkswagen Group starting in October. |
| 27 Mar 2026 | Rivian (rivian.com) | equity investment | $3B | volkswagen group | Germany | The German automotive giant has already invested a little more than $3 billion in Rivian as part of the joint venture. |
| 19 Mar 2026 | Rivian (rivian.com) | — | $300M | uber | — | As part of the partnership, Uber committed to an initial investment of $300 million in Rivian, subject to regulatory approval. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company rivian.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company rivian.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company rivian.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company rivian.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$PRISM_BUSINESS_API_BASE/v1/business/companies/rivian.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "rivian.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Microsoft News](microsoft-news.md)
- [Walmart News](walmart-news.md)
- [Netflix News](netflix-news.md)
- [Meta News](meta-news.md)
