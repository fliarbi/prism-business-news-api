# TCS News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “tcs news” · 40,500/month India · 3,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [tcs-news.json](../../examples/scenarios/tcs-news.json).

**Question.** What has the news reported about TCS in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `tcs.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `tcs.com` |
| Headlines, Jan – Apr 2026 (estimate) | 154 |
| Events, May 2025 – Apr 2026 | 419 |
| Most frequent event types | Earnings (163), Contracts (65), Announcement (51) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 27% · 0.0% · 73% of 154 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 8 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 18 Apr 2026 | [TCS clarifies Nida Khan 'not HR manager' in Nashik case, launches probe and oversight panel](https://www.storyboard18.com/trending/tcs-clarifies-nida-khan-not-hr-manager-in-nashik-case-launches-probe-and-oversight-panel-ws-l-95565.htm) | storyboard18.com | 8 | negative | Lawsuit |
| 17 Apr 2026 | [No POSH complaints from employees who filed FIRs: TCS statement after Nashik case](https://www.indiatoday.in/india/story/tcs-denies-receiving-complaints-in-nashik-sexual-harassment-probe-2897975-2026-04-17) | indiatoday.in | 8 | negative | Regulatory |
| 15 Apr 2026 | [Tata Group plans hydrogen bus production in Lucknow](https://www.hindustantimes.com/cities/lucknow-news/tata-group-plans-hydrogen-bus-production-in-lucknow-101776266343916.html) | hindustantimes.com | 8 | positive | Announcement |
| 15 Apr 2026 | [TCS headcount fell by 23,460 in FY26; but no more layoffs for now: Sudeep Kunnummal, CHRO - The Economic Times](https://economictimes.indiatimes.com/tech/information-tech/tcs-headcount-fell-by-23460-in-fy26-but-no-more-layoffs-for-now-sudeep-kunnummal-chro/articleshow/130286784.cms) | economictimes.indiatimes.com | 7 | negative | Layoffs |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 163 |
| Contracts | 65 |
| Announcement | 51 |
| Layoffs | 43 |
| Key people | 21 |
| New product | 19 |
| M&A | 15 |
| Lawsuit | 14 |
| Job creation | 14 |
| Capital infusion | 6 |
| Regulatory | 5 |
| Funding round | 1 |
| Asset acquisition | 1 |
| Incorporation | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Contracts | Announcement | Layoffs |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 13 | 0 | 6 | 2 | 0 | ███ |
| Jun 2025 | 8 | 0 | 1 | 6 | 0 | ██ |
| Jul 2025 | 67 | 46 | 1 | 4 | 9 | █████████████████ |
| Aug 2025 | 41 | 8 | 12 | 9 | 3 | ██████████ |
| Sep 2025 | 27 | 3 | 9 | 6 | 3 | ███████ |
| Oct 2025 | 65 | 31 | 6 | 4 | 8 | ████████████████ |
| Nov 2025 | 23 | 0 | 7 | 2 | 3 | ██████ |
| Dec 2025 | 21 | 3 | 4 | 3 | 2 | █████ |
| Jan 2026 | 44 | 26 | 2 | 1 | 7 | ███████████ |
| Feb 2026 | 11 | 0 | 6 | 4 | 1 | ███ |
| Mar 2026 | 19 | 3 | 8 | 1 | 0 | █████ |
| Apr 2026 | 80 | 43 | 3 | 9 | 7 | ████████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 8 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Layoffs | Tata Consultancy Services had earlier planned to let go of 12,500 employees | article unavailable |
| 26 Apr 2026 | M&A | Tata Consultancy Services (TCS) acquired the US-based Coastal Cloud for about $700 million | article unavailable |
| 24 Apr 2026 | Earnings | TCS reported a 0.5% decline in FY26 revenue to $30,017 million | article unavailable |
| 24 Apr 2026 | Earnings | TCS reported Q4FY26 revenue at Rs 70,698 crore, up 9.6% YoY from Rs 64,479 crore in Q4FY25 and 5.4% QoQ. | article unavailable |
| 21 Apr 2026 | Lawsuit | Police have formed a Special Investigation Team (SIT) to probe nine FIRs linked to the case and have arrested eight employees so far, including a… | article unavailable |
| 21 Apr 2026 | Contracts | Seoul, April 21, 2026 Internet giant Naver said it has signed a memorandum of understanding (MOU) with the information technology (IT) arm of Tata… | article unavailable |
| 18 Apr 2026 | Lawsuit | Following the emergence of the case last week, Nashik Police constituted a Special Investigation Team to probe complaints filed by eight women… | [TCS clarifies Nida Khan 'not HR manager' in Nashik case, launches…](https://www.storyboard18.com/trending/tcs-clarifies-nida-khan-not-hr-manager-in-nashik-case-launches-probe-and-oversight-panel-ws-l-95565.htm) · storyboard18.com |
| 17 Apr 2026 | Regulatory | The company also said it is cooperating fully with law enforcement agencies to ensure a thorough and transparent probe. | [No POSH complaints from employees who filed FIRs: TCS statement…](https://www.indiatoday.in/india/story/tcs-denies-receiving-complaints-in-nashik-sexual-harassment-probe-2897975-2026-04-17) · indiatoday.in |
| 17 Apr 2026 | Lawsuit | After more workers came forward, a total of 8 FIRs were registered with the city police under charges of religious conversion and sexual harassment. | article unavailable |
| 16 Apr 2026 | Announcement | Tata Consultancy Services currently employs around 20,000 professionals in Lucknow, Noida, and Varanasi, with plans to double the workforce to… | article unavailable |
| 15 Apr 2026 | Announcement | It could reach 40,000 in the next five years. | [Tata Group plans hydrogen bus production in Lucknow](https://www.hindustantimes.com/cities/lucknow-news/tata-group-plans-hydrogen-bus-production-in-lucknow-101776266343916.html) · hindustantimes.com |
| 15 Apr 2026 | Layoffs | In 2025, the company had indicated plans to reduce approximately 2% of its workforce, alongside implementing stricter bench policies, which… | [TCS headcount fell by 23,460 in FY26; but no more layoffs for now:…](https://economictimes.indiatimes.com/tech/information-tech/tcs-headcount-fell-by-23460-in-fy26-but-no-more-layoffs-for-now-sudeep-kunnummal-chro/articleshow/130286784.cms) · economictimes.indiatimes.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company tcs.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company tcs.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company tcs.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company tcs.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$PRISM_BUSINESS_API_BASE/v1/business/companies/tcs.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "tcs.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Nintendo News](nintendo-news.md)
- [Nvidia News](nvidia-news.md)
- [Jio News](jio-news.md)
- [Intel News](intel-news.md)
