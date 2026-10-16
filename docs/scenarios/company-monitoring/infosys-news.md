# Infosys News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “infosys news” · 40,500/month India · 1,300/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [infosys-news.json](../../examples/scenarios/infosys-news.json).

**Question.** What has the news reported about Infosys in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `infosys.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `infosys.com` |
| Headlines, Jan – Apr 2026 (estimate) | 3,000 |
| Events, May 2025 – Apr 2026 | 322 |
| Most frequent event types | Earnings (174), M&A (30), New product (26) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 37% · 0.4% · 63% of 3,000 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 4 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Infosys appoints Nitin Paranjpe as Vice Chairman; Nandan Nilekani to continue as Chairman](https://www.financialexpress.com/business/news-infosys-appoints-nitin-paranjpe-as-vice-chairman-nandan-nilekani-to-continue-as-chairman-4223617/) | financialexpress.com | 7 | positive | — |
| 30 Apr 2026 | [Infosys appoints Nitin Paranjpe as vice chairman](https://www.thehindubusinessline.com/info-tech/infosys-appoints-nitin-paranjpe-as-vice-chairman/article70925811.ece) | thehindubusinessline.com | 7 | positive | Key people |
| 30 Apr 2026 | [Nitin Paranjpe: Infosys names Nitin Paranjpe vice chairman; Nilekani says no chairman transition planned -…](https://timesofindia.indiatimes.com/business/india-business/infosys-names-nitin-paranjpe-vice-chairman-nilekani-says-no-chairman-transition-planned/articleshow/130640026.cms) | timesofindia.indiatimes.com | 7 | positive | Key people |
| 30 Apr 2026 | [Infosys appoints Nitin Paranjpe as vice chairman - The Economic Times](https://economictimes.indiatimes.com/tech/information-tech/infosys-appoints-nitin-paranjpe-as-vice-chairman/articleshow/130639122.cms) | economictimes.indiatimes.com | 7 | positive | Key people |
| 30 Apr 2026 | [Infosys loses spot in top 10 companies by market cap; this PSU replaces IT giant - BusinessToday](https://www.businesstoday.in/markets/stocks/story/infosys-loses-spot-in-top-10-companies-by-market-cap-this-psu-replaces-it-giant-528340-2026-04-30) | businesstoday.in | 6 | positive | — |
| 30 Apr 2026 | [Crude Shock, Global Jitters Pull Markets Lower Despite Strong April Rally – Outlook Business](https://www.outlookbusiness.com/markets/crude-shock-global-jitters-pull-markets-lower-despite-strong-april-rally) | outlookbusiness.com | 7 | negative | — |
| 30 Apr 2026 | [Meta CTO Andrew Bosworth Issues Strict Performance Ultimatum to Staff Following Layoffs, Declares…](https://www.latestly.com/technology/meta-cto-andrew-bosworth-issues-strict-performance-ultimatum-to-staff-following-layoffs-declares-underperformance-not-an-option-7413432.html) | latestly.com | 7 | positive | — |
| 30 Apr 2026 | [BT Closing Bell \| Sensex settles 582 pts lower, Nifty below 24,000; Eternal, HUL lead index losers -…](https://www.businesstoday.in/markets/stocks/story/bt-closing-bell-sensex-settles-582-pts-lower-nifty-below-24000-eternal-hul-lead-index-losers-528248-2026-04-30) | businesstoday.in | 7 | negative | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 174 |
| M&A | 30 |
| New product | 26 |
| Announcement | 24 |
| Contracts | 16 |
| Job creation | 12 |
| Buyback | 12 |
| Key people | 7 |
| Regulatory | 7 |
| Layoffs | 7 |
| Lawsuit | 5 |
| Asset acquisition | 2 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | M&A | New product | Announcement |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 9 | 4 | 0 | 2 | 0 | ███ |
| Jun 2025 | 15 | 0 | 0 | 0 | 3 | █████ |
| Jul 2025 | 49 | 37 | 2 | 1 | 2 | █████████████████ |
| Aug 2025 | 31 | 10 | 9 | 4 | 1 | ███████████ |
| Sep 2025 | 18 | 7 | 1 | 0 | 3 | ██████ |
| Oct 2025 | 38 | 26 | 0 | 2 | 2 | █████████████ |
| Nov 2025 | 15 | 2 | 0 | 9 | 0 | █████ |
| Dec 2025 | 10 | 1 | 2 | 2 | 0 | ███ |
| Jan 2026 | 47 | 38 | 1 | 1 | 5 | ████████████████ |
| Feb 2026 | 10 | 2 | 0 | 3 | 4 | ███ |
| Mar 2026 | 21 | 3 | 13 | 2 | 2 | ███████ |
| Apr 2026 | 59 | 44 | 2 | 0 | 2 | ████████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 4 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Key people | IT company Infosys has appointed HUL's non-executive chairman Nitin Paranjpe as non-executive vice chairman of its board with immediate effect, the… | [Infosys appoints Nitin Paranjpe as vice chairman](https://www.thehindubusinessline.com/info-tech/infosys-appoints-nitin-paranjpe-as-vice-chairman/article70925811.ece) · thehindubusinessline.com |
| 30 Apr 2026 | Key people | Infosys has appointed Hindustan Unilever Ltd’s non-executive chairman Nitin Paranjpe as non-executive vice chairman of its board with immediate… | [Nitin Paranjpe: Infosys names Nitin Paranjpe vice chairman; Nilekani…](https://timesofindia.indiatimes.com/business/india-business/infosys-names-nitin-paranjpe-vice-chairman-nilekani-says-no-chairman-transition-planned/articleshow/130640026.cms) · timesofindia.indiatimes.com |
| 29 Apr 2026 | Contracts | Truist Financial Corp. of the United States has awarded Infosys Ltd a contract to establish and operate a global capabilities centre (GCC) in… | [Infosys Wins $500M GCC Deal with Truist](https://startuptalky.com/news/infosys-lands-largest-gcc-contract/) · startuptalky.com |
| 29 Apr 2026 | Job creation |  | [Infosys Lands Landmark $500M GCC Contract with Truist Financial](https://www.indianweb2.com/2026/05/infosys-lands-landmark-500m-gcc.html) · indianweb2.com |
| 26 Apr 2026 | M&A | Infosys MD & CEO Salil Parekh, post the company’s recent acquisition, commented that by bringing together Optimum’s provider experience with Infosys… | article unavailable |
| 25 Apr 2026 | Announcement | Infosys in Q4 reduced the number of around 8,440 employees. | article unavailable |
| 25 Apr 2026 | Earnings | Infosys delivered constant-currency revenue growth of 3.1% for FY2026, the strongest performance of the four. | [Why record large deal wins at TCS, Infosys, HCLTech, and Wipro are not](https://business-news-today.com/why-record-large-deal-wins-at-tcs-infosys-hcltech-and-wipro-are-not-showing-up-in-constant-currency-revenue-growth/) · business-news-today.com |
| 24 Apr 2026 | Earnings | Infosys posted a sequential constant currency decline of 1.3–1.35% to $5,040 million in the March quarter | article unavailable |
| 24 Apr 2026 | Earnings | Infosys reported Q4FY26 revenue at $5.04 billion, down 1.2% QoQ from $5.10 billion while increasing 4.1% YoY. | article unavailable |
| 24 Apr 2026 | Regulatory | Infosys has approved performance-linked stock incentives worth approximately INR 52 crore for its Chief Executive Officer and Managing Director,… | [Infosys CEO Salil Parekh Gets INR 52 Crore Stock Incentives From…](https://www.latestly.com/business/infosys-ceo-salil-parekh-gets-inr-52-crore-stock-incentives-from-company-amid-wage-hike-delays-7405794.html) · latestly.com |
| 24 Apr 2026 | Earnings | Infosys has reported FY26 revenue of $20,158 million, registering growth of 3.1 percent, supported by strong enterprise demand for AI-led… | [Infosys FY26 Revenue Hits $20.16 bn as AI Strategy Drives $14.9 bn…](https://infotechlead.com/software/infosys-fy26-revenue-hits-20-16-bn-as-ai-strategy-drives-14-9-bn-deal-wins-95361) · infotechlead.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company infosys.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company infosys.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company infosys.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company infosys.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/infosys.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "infosys.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Jio News](jio-news.md)
- [Intel News](intel-news.md)
- [Openai News](openai-news.md)
- [Amazon News](amazon-news.md)
