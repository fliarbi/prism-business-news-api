# IBM News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “ibm news” · 1,600/month India · 5,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [ibm-news.json](../../examples/scenarios/ibm-news.json).

**Question.** What has the news reported about IBM in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `ibm.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `ibm.com` |
| Headlines, Jan – Apr 2026 (estimate) | 3,670 |
| Events, May 2025 – Apr 2026 | 162 |
| Most frequent event types | Earnings (32), Announcement (24), Lawsuit (23) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 19% · 1.1% · 80% of 3,670 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 3 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Sabre Annual Meeting: Shareholders Elect Directors, Approve Pay Plans, Ratify Ernst & Young](https://www.thelincolnianonline.com/2026/04/30/sabre-annual-meeting-shareholders-elect-directors-approve-pay-plans-ratify-ernst-young.html) | thelincolnianonline.com | 7 | positive | Board |
| 30 Apr 2026 | [Definedge Securities Appoints Hemant Luthra as Chairman; Ajay Srivastava, D. Prasad Join Board - Punekar News](https://www.punekarnews.in/definedge-securities-appoints-hemant-luthra-as-chairman-ajay-srivastava-d-prasad-join-board/) | punekarnews.in | 5 | positive | Key people |
| 30 Apr 2026 | [Pharma Cloud Services Market is expected to Hit US$ 55.78 Billion by 2033 \| Major Companies - IBM…](https://www.openpr.com/news/4497042/pharma-cloud-services-market-is-expected-to-hit-us-55-78-billion) | openpr.com | 7 | positive | — |
| 30 Apr 2026 | [Definedge Securities appoints Hemant Luthra as Chairman; Ajay Srivastava, D. Prasad join Board](https://www.medianews4u.com/definedge-securities-appoints-hemant-luthra-as-chairman-ajay-srivastava-d-prasad-join-board/) | medianews4u.com | 5 | positive | Key people |
| 30 Apr 2026 | [Airline Flight Operations Software Market is Going to Boom \| Major Giants SITA, Jeppesen, Airbus](https://www.openpr.com/news/4496932/airline-flight-operations-software-market-is-going-to-boom) | openpr.com | 6 | positive | — |
| 30 Apr 2026 | [Why CrowdStrike's Consolidation Bet Is the Only One That Matters](https://theglobeandmail.com/investing/markets/stocks/PANW/pressreleases/1651606/why-crowdstrikes-consolidation-bet-is-the-only-one-that-matters/) | theglobeandmail.com | 7 | positive | — |
| 30 Apr 2026 | [S&P 500 Rally: Earnings Heat Up Ahead of the Fed](https://fintech.tv/sp-500-surges-10-in-april-big-tech-earnings-fed-decision-in-focus/) | fintech.tv | 4 | positive | — |
| 30 Apr 2026 | [Healthcare Asset Management Market to Skyrocket 26.5% Annually, Reaching $284.7 Billion by 2034 as RFID and…](https://www.openpr.com/news/4496473/healthcare-asset-management-market-to-skyrocket-26-5) | openpr.com | 7 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 32 |
| Announcement | 24 |
| Lawsuit | 23 |
| Key people | 21 |
| M&A | 16 |
| Contracts | 16 |
| New product | 11 |
| Layoffs | 7 |
| Regulatory | 4 |
| Asset acquisition | 3 |
| Job creation | 3 |
| Capital infusion | 2 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Announcement | Lawsuit | Key people |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 4 | 0 | 0 | 0 | 0 | ██ |
| Jun 2025 | 5 | 0 | 1 | 0 | 1 | ███ |
| Jul 2025 | 9 | 4 | 2 | 0 | 0 | █████ |
| Aug 2025 | 21 | 6 | 8 | 0 | 2 | ████████████ |
| Sep 2025 | 7 | 0 | 1 | 0 | 1 | ████ |
| Oct 2025 | 19 | 9 | 0 | 0 | 5 | ███████████ |
| Nov 2025 | 6 | 0 | 0 | 0 | 0 | ███ |
| Dec 2025 | 20 | 0 | 2 | 0 | 5 | ███████████ |
| Jan 2026 | 16 | 9 | 0 | 0 | 2 | █████████ |
| Feb 2026 | 15 | 0 | 5 | 0 | 4 | █████████ |
| Mar 2026 | 5 | 0 | 2 | 0 | 0 | ███ |
| Apr 2026 | 35 | 4 | 3 | 23 | 1 | ████████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 4 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 29 Apr 2026 | Job creation | IBM said it will hire one-third of the qualified program graduates from a new City Colleges apprenticeship program. | [IBM plans to hire hundreds on Far South Side for new delivery center](https://www.cbsnews.com/chicago/news/ibm-hiring-jobs-far-south-side-new-delivery-center/) · cbsnews.com |
| 29 Apr 2026 | New product | GA status coincides with the launch of an IBM Bob Premium Package for Z, "which integrates and enhances the capabilities of IBM watsonx Code… | [IBM's AI coding 'partner' Bob hits general availability](https://www.theregister.com/development/2026/04/29/ibms-ai-coding-partner-bob-hits-general-availability/5219012) · theregister.com |
| 28 Apr 2026 | New product | the GA status coincides with the launch of an IBM Bob Premium Package for Z | article unavailable |
| 23 Apr 2026 | Earnings | CFO Jim Kavanaugh reported 6% revenue growth, 140 basis points of operating pre-tax margin expansion, 17% adjusted EBITDA growth, and 19% growth in… | [International Business Machines Q1 Earnings Call Highlights](https://www.dailypolitical.com/2026/04/23/international-business-machines-q1-earnings-call-highlights.html) · dailypolitical.com |
| 23 Apr 2026 | Earnings | IBM has reported 9 percent increase in revenue to $15.9 billion in Q1 2026 | [AI drives revenue growth at IBM through hybrid cloud, automation,…](https://infotechlead.com/networking/ai-drives-revenue-growth-at-ibm-through-hybrid-cloud-automation-and-enterprise-platforms-95316) · infotechlead.com |
| 22 Apr 2026 | Earnings | The tech company made $15.9 billion in revenue during the quarter, which beats the expectation of $15.65 billion. | article unavailable |
| 22 Apr 2026 | Lawsuit | Tying executive compensation to diversity metrics, walling off affinity-based groups and programs, and setting diversity targets for hiring pools… | [Federal Targets, First Settlement Underscore Corporate DEI Risks](https://news.bloomberglaw.com/esg/federal-targets-first-settlement-underscore-corporate-dei-risks-26) · news.bloomberglaw.com |
| 16 Apr 2026 | Announcement | According to COMvergence estimates, IBM's overall expenditure on media increased to 190 million d&oacute;lars in 2025, a considerable ca&iacute;dece… | [Omnicom gana la cuenta global de medios de IBM](https://periodicopublicidad.com/articulo/fusiones-y-adquisiciones/omnicom-gana-cuenta-global-medios-ibm/20260416101855171973.html) · periodicopublicidad.com |
| 16 Apr 2026 | Announcement | IBM has granted its global media account to Omnicom after a competitive review. | article unavailable |
| 16 Apr 2026 | Earnings | Revenue of $15.9 billion, up 9 percent, up 6 percent at constant currency | [IBM RELEASES FIRST-QUARTER RESULTS](https://newsroom.ibm.com/2026-04-22-IBM-RELEASES-FIRST-QUARTER-RESULTS) · newsroom.ibm.com |
| 15 Apr 2026 | Lawsuit | Tech giant IBM agreed to pay $17 million to settle allegations that its DE&I initiatives failed to comply with anti-discrimination requirements in… | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company ibm.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company ibm.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company ibm.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company ibm.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/ibm.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "ibm.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Lucid News](lucid-news.md)
- [Uber News](uber-news.md)
- [Airtel News](airtel-news.md)
- [Larsen and Toubro News](larsen-and-toubro-news.md)
