# Adani News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “adani news” · 90,500/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [adani-news.json](../../examples/scenarios/adani-news.json).

**Question.** What has the news reported about Adani in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `adani.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `adani.com` |
| Headlines, Jan – Apr 2026 (estimate) | 9 |
| Events, May 2025 – Apr 2026 | 37 |
| Most frequent event types | Lawsuit (27), Regulatory (3), Earnings (2) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 100% · 0.0% · 0.0% of 9 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 4 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 8 Apr 2026 | [Adani Group Stocks Rally; Adani Total, Adani Green Jump Over 13 Pc – Outlook Business](https://www.outlookbusiness.com/markets/adani-group-stocks-rally-adani-total-adani-green-jump-over-13-pc) | outlookbusiness.com | 7 | negative | Lawsuit |
| 8 Apr 2026 | [Adani Group Stocks: Adani Ent, Adani Ports, Adani Green, ATGL rally 13%](https://www.thehindubusinessline.com/markets/stock-markets/adani-enterprises-adani-ports-rally-up-to-10-group-stocks-jump-amid-legal-developments/article70837138.ece) | thehindubusinessline.com | 8 | negative | Lawsuit |
| 31 Mar 2026 | [Inde : bataille judiciaire à 4 milliards de dollars autour d’actifs clés et du seul circuit de F1 du pays –…](https://entrevue.fr/monde/inde-bataille-judiciaire-a-4-milliards-de-dollars-autour-dactifs-cles-et-du-seul-circuit-de-f1-du-pays/) | entrevue.fr | 7 | negative | Lawsuit |
| 31 Mar 2026 | [Indian billionaire challenges Adani’s winning bid for $4 bln in assets, F1 track](https://gulfbusiness.com/en/2026/news/indian-billionaire-challenges-adanis-winning-bid-for-4-bln-in-assets-f1-track/) | gulfbusiness.com | 8 | negative | Lawsuit |
| 27 Jan 2026 | [Adani Group stocks rebound 6% after clarifying US regulatory dispute](https://www.fortuneindia.com/markets/adani-group-stocks-rebound-6-after-clarifying-us-regulatory-dispute/129763) | fortuneindia.com | 8 | negative | Lawsuit |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Lawsuit | 27 |
| Regulatory | 3 |
| Earnings | 2 |
| Announcement | 2 |
| M&A | 1 |
| Contracts | 1 |
| Asset acquisition | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Lawsuit | Regulatory | Earnings | Announcement |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 6 | 5 | 0 | 1 | 0 | ███████████████ |
| Jun 2025 | 4 | 2 | 0 | 0 | 1 | ██████████ |
| Jul 2025 | 4 | 2 | 0 | 1 | 0 | ██████████ |
| Aug 2025 | 3 | 2 | 0 | 0 | 0 | ████████ |
| Sep 2025 | 8 | 6 | 2 | 0 | 0 | ████████████████████ |
| Oct 2025 | 0 | 0 | 0 | 0 | 0 |  |
| Nov 2025 | 0 | 0 | 0 | 0 | 0 |  |
| Dec 2025 | 1 | 0 | 0 | 0 | 1 | ██ |
| Jan 2026 | 4 | 3 | 1 | 0 | 0 | ██████████ |
| Feb 2026 | 0 | 0 | 0 | 0 | 0 |  |
| Mar 2026 | 2 | 2 | 0 | 0 | 0 | █████ |
| Apr 2026 | 5 | 5 | 0 | 0 | 0 | ████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 5 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 8 Apr 2026 | Lawsuit | A US judge granted a request from billionaire Gautam Adani to schedule a hearing in efforts to dismiss a US Securities and Exchange Commission fraud… | [Adani Group Stocks Rally; Adani Total, Adani Green Jump Over 13 Pc –…](https://www.outlookbusiness.com/markets/adani-group-stocks-rally-adani-total-adani-green-jump-over-13-pc) · outlookbusiness.com |
| 8 Apr 2026 | Lawsuit | The stocks of various Adani Group companies surged on the bourses on Wednesday after a United States court accepted its petition to dismiss the US… | article unavailable |
| 8 Apr 2026 | Lawsuit | Adani Group stocks, including flagship Adani Enterprises, Adani Green Energy and Adani Ports, rallied up to 13% on Wednesday after billionaire… | article unavailable |
| 8 Apr 2026 | Lawsuit | after a US court accepted the plea filed by the counsels of Guatam and Sagar Adani for a pre-motion conference to dismiss a securities fraud case… | [Adani group stocks surge up to 13% after this US court order in…](https://www.livemint.com/market/stock-market-news/adani-group-stocks-surge-up-to-12-after-this-us-court-order-in-bribery-case-against-gautam-adani-nephew-11775628454114.html) · livemint.com |
| 8 Apr 2026 | Lawsuit | Gautam Adani moved a US court seeking dismissal of a securities fraud lawsuit filed by the US Securities and Exchange Commission. | [Adani Group Stocks: Adani Ent, Adani Ports, Adani Green, ATGL rally…](https://www.thehindubusinessline.com/markets/stock-markets/adani-enterprises-adani-ports-rally-up-to-10-group-stocks-jump-amid-legal-developments/article70837138.ece) · thehindubusinessline.com |
| 31 Mar 2026 | Lawsuit | Indian billionaire Anil Agarwal challenges in the Supreme Court the winning offer of his compatriot Gautam Adani for the takeover of a bankrupt… | [Inde : bataille judiciaire à 4 milliards de dollars autour d’actifs…](https://entrevue.fr/monde/inde-bataille-judiciaire-a-4-milliards-de-dollars-autour-dactifs-cles-et-du-seul-circuit-de-f1-du-pays/) · entrevue.fr |
| 31 Mar 2026 | Lawsuit | Agarwal’s Vedanta has mounted a legal challenge over a creditor committee’s decision to award the assets of Jaiprakash Associates to Adani | [Indian billionaire challenges Adani’s winning bid for $4 bln in…](https://gulfbusiness.com/en/2026/news/indian-billionaire-challenges-adanis-winning-bid-for-4-bln-in-assets-f1-track/) · gulfbusiness.com |
| 27 Jan 2026 | Lawsuit | The SEC’s civil lawsuit, filed in November 2024, alleges that Gautam Adani and Sagar Adani violated U.S. securities laws by making false and… | [Adani Group stocks rebound 6% after clarifying US regulatory dispute](https://www.fortuneindia.com/markets/adani-group-stocks-rebound-6-after-clarifying-us-regulatory-dispute/129763) · fortuneindia.com |
| 25 Jan 2026 | Lawsuit | The SEC has since filed a civil lawsuit against Gautam and Sagar Adani, that is separate from a criminal case initiated by the US Department of… | article unavailable |
| 25 Jan 2026 | Regulatory | United states SEC had issued direct summons in 2025 but India law ministry declined to serve the summons. | article unavailable |
| 24 Jan 2026 | Lawsuit | The SEC has filed a civil lawsuit against Gautam Adani and Sagar Adani, separate from a criminal case initiated by the US Department of Justice… | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company adani.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company adani.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company adani.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company adani.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$PRISM_BUSINESS_API_BASE/v1/business/companies/adani.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "adani.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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
- [Tesla News](tesla-news.md)
- [Nintendo News](nintendo-news.md)
