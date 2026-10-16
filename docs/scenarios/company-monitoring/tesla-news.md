# Tesla News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “tesla news” · 2,400/month India · 74,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [tesla-news.json](../../examples/scenarios/tesla-news.json).

**Question.** What has the news reported about Tesla in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `tesla.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `tesla.com` |
| Headlines, Jan – Apr 2026 (estimate) | 120 |
| Events, May 2025 – Apr 2026 | 369 |
| Most frequent event types | Announcement (108), Earnings (64), Key people (55) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 21% · 0.8% · 78% of 120 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 5 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [First Tesla Semi Rolls Off High-Volume Production Line - TT](https://www.transporttopics.com/articles/first-tesla-semi-production) | transporttopics.com | 7 | positive | Announcement |
| 29 Apr 2026 | [Tesla Semi vs Diesel: Electric Truck Costs and Production in 2026](https://www.inboundlogistics.com/articles/tesla-semi-enters-production-as-diesels-cost-advantage-collapses/) | inboundlogistics.com | 7 | negative | Announcement |
| 24 Apr 2026 | [Shanghai factory powers robust Q1 for Tesla](https://global.chinadaily.com.cn/a/202604/24/WS69eac75ca310d6866eb45473.html) | global.chinadaily.com.cn | 8 | positive | Earnings |
| 23 Apr 2026 | [Tesla Reveals Mysterious $2 Billion AI Hardware Deal in SEC Filing](https://gizmodo.com/tesla-reveals-mysterious-2-billion-ai-hardware-deal-in-sec-filing-2000750025) | gizmodo.com | 8 | positive | M&A |
| 23 Apr 2026 | [Tesla Expanding Giga Berlin Workforce by 1,000 to Boost Model Y Production](https://driveteslacanada.ca/model-y/tesla-expanding-giga-berlin-workforce-by-1000-to-boost-model-y-production/) | driveteslacanada.ca | 7 | positive | Job creation |
| 23 Apr 2026 | [US-Autobauer Tesla will 1.000 neue Jobs in Brandenburg schaffen](https://www.tagesschau.de/inland/regional/brandenburg/tesla-brandenburg-arbeitsplaetze-100.html) | tagesschau.de | 7 | negative | Job creation |
| 23 Apr 2026 | [Tesla will Produktion in Grünheide erhöhen und 1.000 neue Jobs schaffen](https://www.rbb24.de/wirtschaft/beitrag/2026/04/tesla-gruenheide-ausbau-produktion-1000-arbeitsplaetze.html) | rbb24.de | 6 | positive | Job creation |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Announcement | 108 |
| Earnings | 64 |
| Key people | 55 |
| Contracts | 44 |
| Lawsuit | 28 |
| Regulatory | 21 |
| Job creation | 15 |
| M&A | 13 |
| Asset acquisition | 6 |
| New product | 6 |
| Layoffs | 3 |
| Board | 3 |
| Capital infusion | 2 |
| Buyback | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Announcement | Earnings | Key people | Contracts |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 16 | 4 | 1 | 7 | 0 | ████ |
| Jun 2025 | 19 | 3 | 0 | 7 | 2 | █████ |
| Jul 2025 | 72 | 22 | 20 | 8 | 14 | ████████████████████ |
| Aug 2025 | 53 | 20 | 2 | 7 | 2 | ███████████████ |
| Sep 2025 | 9 | 3 | 0 | 1 | 2 | ██ |
| Oct 2025 | 29 | 3 | 16 | 0 | 1 | ████████ |
| Nov 2025 | 28 | 9 | 1 | 8 | 7 | ████████ |
| Dec 2025 | 14 | 2 | 1 | 2 | 6 | ████ |
| Jan 2026 | 27 | 11 | 10 | 1 | 0 | ████████ |
| Feb 2026 | 28 | 9 | 1 | 8 | 4 | ████████ |
| Mar 2026 | 23 | 5 | 0 | 4 | 3 | ██████ |
| Apr 2026 | 51 | 17 | 12 | 2 | 3 | ██████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 4 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Announcement | Tesla said its first Semi rolled off the company’s high-volume production line in Reno, Nev., on April 29. | [First Tesla Semi Rolls Off High-Volume Production Line - TT](https://www.transporttopics.com/articles/first-tesla-semi-production) · transporttopics.com |
| 30 Apr 2026 | Announcement | The first Tesla Semi rolled off the company’s high-volume production line in Reno, Nev., on April 29, the company announced in a social media post. | article unavailable |
| 29 Apr 2026 | Announcement | In its Q1 2026 shareholder filing with the SEC, Tesla flipped the narrative. Tesla confirmed that the Semi has entered pilot production at a… | [Tesla Semi vs Diesel: Electric Truck Costs and Production in 2026](https://www.inboundlogistics.com/articles/tesla-semi-enters-production-as-diesels-cost-advantage-collapses/) · inboundlogistics.com |
| 24 Apr 2026 | Announcement | Elon Musk, CEO of Tesla, has officially announced through X's account that Cybercab, the company's ambitious autonomous robotaxi, is already on the… | article unavailable |
| 24 Apr 2026 | Regulatory | Tesla first foreign automaker to pass data security requirements from the country’s auto industry body in April 2024. | article unavailable |
| 24 Apr 2026 | Earnings | The company released its first‑quarter financial results on Thursday, reporting total revenue of $22.4 billion, benefiting from increased vehicle… | [Shanghai factory powers robust Q1 for Tesla](https://global.chinadaily.com.cn/a/202604/24/WS69eac75ca310d6866eb45473.html) · global.chinadaily.com.cn |
| 23 Apr 2026 | M&A | In April 2026, the Company entered into an agreement to acquire an AI hardware company for up to $2.00 billion in Tesla common stock and equity… | [Tesla Reveals Mysterious $2 Billion AI Hardware Deal in SEC Filing](https://gizmodo.com/tesla-reveals-mysterious-2-billion-ai-hardware-deal-in-sec-filing-2000750025) · gizmodo.com |
| 23 Apr 2026 | M&A | Tesla is quietly buying a mystery AI hardware company. In a brief one-sentence mention in its 10-Q filing, released alongside its Wednesday earnings… | article unavailable |
| 23 Apr 2026 | Job creation | Tesla also plans to transition approximately 500 temporary workers into permanent positions over the course of the year. | [Tesla Expanding Giga Berlin Workforce by 1,000 to Boost Model Y…](https://driveteslacanada.ca/model-y/tesla-expanding-giga-berlin-workforce-by-1000-to-boost-model-y-production/) · driveteslacanada.ca |
| 23 Apr 2026 | Job creation | The US electric car manufacturer Tesla wants to create 1,000 new jobs in the short term at his plant in Brandenburg. | [US-Autobauer Tesla will 1.000 neue Jobs in Brandenburg schaffen](https://www.tagesschau.de/inland/regional/brandenburg/tesla-brandenburg-arbeitsplaetze-100.html) · tagesschau.de |
| 23 Apr 2026 | Job creation | Tesla also wants to take over up to 500 temporary workers in permanent employment in the coming months. | [Tesla will Produktion in Grünheide erhöhen und 1.000 neue Jobs…](https://www.rbb24.de/wirtschaft/beitrag/2026/04/tesla-gruenheide-ausbau-produktion-1000-arbeitsplaetze.html) · rbb24.de |
| 23 Apr 2026 | Announcement | Tesla wants to increase the number of employees in his plant in Grünheide. | [Tesla will Gas geben: 1.000 neue Mitarbeiter in Grünheide](https://www.giessener-allgemeine.de/netzwelt/tesla-will-gas-geben-000-neue-mitarbeiter-in-gruenheide-zr-94274517.html) · giessener-allgemeine.de |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company tesla.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company tesla.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company tesla.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company tesla.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/tesla.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "tesla.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Vodafone Idea News](vodafone-idea-news.md)
- [Adani News](adani-news.md)
- [Nintendo News](nintendo-news.md)
- [Nvidia News](nvidia-news.md)
