# Amazon News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “amazon news” · 6,600/month India · 33,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [amazon-news.json](../../examples/scenarios/amazon-news.json).

**Question.** What has the news reported about Amazon in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `amazon.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `amazon.com` |
| Headlines, Jan – Apr 2026 (estimate) | 3,419 |
| Events, May 2025 – Apr 2026 | 1,397 |
| Most frequent event types | Announcement (501), Job creation (196), New product (136) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 19% · 0.6% · 80% of 3,419 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 5 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Here's Why This Remains My Least Favorite "Magnificent Seven" Stock -- Even After a Strong Earnings Report \|…](https://www.fool.com/investing/2026/04/30/heres-why-this-remains-my-least-favorite-magnifice/) | fool.com | 8 | positive | Earnings |
| 30 Apr 2026 | [Amazon's AWS boosts revenue growth in Q1 milestone](https://www.digitalcommerce360.com/2026/04/30/amazon-aws-revenue-growth-milestone-q1-fy26/) | digitalcommerce360.com | 8 | positive | Earnings |
| 30 Apr 2026 | [One Million Robots In, Amazon’s Automation Ambitions Are Just Heating Up](https://wwd.com/sourcing-journal/logistics/amazon-robotics-fulfillment-center-warehouse-automation-ceo-andy-jassy-1-million-robots-q1-earnings-aws-1238935748/) | wwd.com | 7 | positive | — |
| 30 Apr 2026 | ["Magnificent Seven" Companies Microsoft, Amazon, Alphabet, and Meta Just Reported Earnings. Here Are the…](https://www.fool.com/investing/2026/04/30/magnificent-seven-companies-microsoft-amazon-alpha/) | fool.com | 8 | positive | — |
| 30 Apr 2026 | [Up 27% in 1 Month, Amazon Is Now the Best-Performing "Magnificent Seven" Stock in 2026. 2 Reasons Why It's a…](https://www.fool.com/investing/2026/04/30/amazon-all-time-high-buy-magnificent-seven-stock) | fool.com | 8 | negative | — |
| 30 Apr 2026 | [“We’ve never seen a technology grow this fast”: Andy Jassy says Amazon Web Services AI business hits $15 bn…](https://storyboard18.com/brand-makers/weve-never-seen-a-technology-grow-this-fast-andy-jassy-says-amazon-web-services-ai-business-hits-15-bn-run-rate-96872.htm) | storyboard18.com | 8 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Announcement | 501 |
| Job creation | 196 |
| New product | 136 |
| Lawsuit | 107 |
| Earnings | 95 |
| Contracts | 88 |
| Layoffs | 75 |
| Key people | 65 |
| Regulatory | 56 |
| M&A | 40 |
| Capital infusion | 17 |
| Asset acquisition | 16 |
| Incorporation | 3 |
| Funding round | 2 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Announcement | Job creation | New product | Lawsuit |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 84 | 16 | 14 | 9 | 3 | ████████ |
| Jun 2025 | 92 | 31 | 20 | 4 | 7 | █████████ |
| Jul 2025 | 83 | 43 | 6 | 4 | 11 | ████████ |
| Aug 2025 | 211 | 85 | 72 | 20 | 2 | ████████████████████ |
| Sep 2025 | 117 | 45 | 7 | 19 | 20 | ███████████ |
| Oct 2025 | 110 | 20 | 25 | 16 | 2 | ██████████ |
| Nov 2025 | 84 | 21 | 4 | 8 | 14 | ████████ |
| Dec 2025 | 97 | 29 | 13 | 15 | 14 | █████████ |
| Jan 2026 | 112 | 65 | 2 | 9 | 7 | ███████████ |
| Feb 2026 | 153 | 41 | 11 | 10 | 8 | ███████████████ |
| Mar 2026 | 125 | 65 | 12 | 18 | 6 | ████████████ |
| Apr 2026 | 129 | 40 | 10 | 4 | 13 | ████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 4 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Earnings | Amazon reported $181.5 billion in revenue, or 17% year-over-year growth. | [Amazon's AWS boosts revenue growth in Q1 milestone](https://www.digitalcommerce360.com/2026/04/30/amazon-aws-revenue-growth-milestone-q1-fy26/) · digitalcommerce360.com |
| 30 Apr 2026 | Lawsuit | The class action lawsuit argued that Amazon did not give those mandatory breaks to hourly employees in Washington state, as required by state law. | article unavailable |
| 30 Apr 2026 | Earnings | Revenue climbed 17% year over year to $181.5 billion, beating consensus by more than $4 billion | [Stock Market Today (LIVE): Markets Close Out April With a Bang; Data…](https://www.fool.com/investing/2026/04/30/stock-market-today-live-coverage/) · fool.com |
| 30 Apr 2026 | Announcement | Amazon has also committed to investing more than $35 billion in India by 2030 focusing on business expansion and other measures such as AI-driven… | [Amazon Now’s India orders growing 25% every month: CEO Andy Jassy \|…](https://www.livemint.com/companies/news/amazon-now-amazon-prime-india-ceo-andy-jassy-quick-commerce-11777531511884.html) · livemint.com |
| 30 Apr 2026 | Earnings | Amazon’s AWS touched $37.6 billion, up 28% | [Big Tech Q1 results: AI may be the story, but ads are still the…](https://www.exchange4media.com/digital-news/big-tech-q1-results-ai-may-be-the-story-but-ads-are-still-the-business-154268.html) · exchange4media.com |
| 30 Apr 2026 | Earnings | Amazon posted net sales of $181.5 billion in the first quarter, up 17% from $155.7 billion a year earlier. | article unavailable |
| 30 Apr 2026 | Earnings | Overall, Amazon posted net sales of $181.5 billion in the first quarter, up 17% from $155.7 billion a year earlier. Operating income for the quarter… | article unavailable |
| 29 Apr 2026 | Announcement | Overall, Amazon reported first-quarter revenue of $181.5 billion, up 17 percent year over year. | [Amazon's chips become a $20B business](https://www.theregister.com/software/2026/04/30/amazons-chips-become-a-20b-business/5221236) · theregister.com |
| 29 Apr 2026 | Announcement | Amazon is now among the top three datacenter chip businesses in the world, as its semiconductor business surpassed a $20 billion annual run rate ...… | [Amazon's chips become a $20B business](https://www.theregister.com/2026/04/29/amazon_chips_20b_business/) · theregister.com |
| 29 Apr 2026 | Announcement | Amazon is now among the top three datacenter chip businesses in the world, as its semiconductor business surpassed a $20 billion annual run rate ... | [Amazon's chips become a $20B business](https://theregister.com/2026/04/29/amazon_chips_20b_business/) · theregister.com |
| 29 Apr 2026 | Earnings | Amazon reported adjusted earnings per share of $2.78 on $181.5 billion in revenue | article unavailable |
| 29 Apr 2026 | Earnings | Amazon's net sales during the first quarter of 2026, up 17% year over year. | [Amazon Hits $70 Billion in Ad Revenue Over the Past 12 Months](https://www.adweek.com/commerce/amazon-hits-70-billion-in-ad-revenue-over-the-past-12-months/) · adweek.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company amazon.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company amazon.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company amazon.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company amazon.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/amazon.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "amazon.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Infosys News](infosys-news.md)
- [Openai News](openai-news.md)
- [Boeing News](boeing-news.md)
- [Tata Motors News](tata-motors-news.md)
