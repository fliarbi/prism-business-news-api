# Insolvency: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “insolvency” · 14,800/month India · 27,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [insolvency.json](../../examples/scenarios/insolvency.json).

**Question.** How many insolvency events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `company_announcement`, `lawsuit` and the word “insolvency” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 204 |
| Companies (with a domain) | 124 |
| Source articles | 153 |
| Busiest month | Jun 2025 (32 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 85% · 2.4% · 13% of 85 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Lawsuit | Announcement |  |
| --- | ---: | ---: | ---: | --- |
| May 2025 | 24 | 24 | 0 | ███████████████ |
| Jun 2025 | 32 | 32 | 0 | ████████████████████ |
| Jul 2025 | 27 | 27 | 0 | █████████████████ |
| Aug 2025 | 19 | 18 | 1 | ████████████ |
| Sep 2025 | 15 | 14 | 1 | █████████ |
| Oct 2025 | 7 | 7 | 0 | ████ |
| Nov 2025 | 10 | 10 | 0 | ██████ |
| Dec 2025 | 10 | 9 | 1 | ██████ |
| Jan 2026 | 7 | 7 | 0 | ████ |
| Feb 2026 | 14 | 14 | 0 | █████████ |
| Mar 2026 | 18 | 18 | 0 | ███████████ |
| Apr 2026 | 21 | 19 | 2 | █████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 7 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | soluxtec.de | Lawsuit | From pv magazine Germany German solar module manufacturer Soluxtec has filed for insolvency proceedings with the Bitburg District Court on Wednesday. | [German solar module maker Soluxtec files for insolvency](https://www.pv-magazine.com/2026/04/30/german-solar-module-maker-soluxtec-files-for-insolvency/) · pv-magazine.com |
| 30 Apr 2026 | reliancepower.co.in | Lawsuit | "Export Import Bank of the United States (US Exim) filed an insolvency application against the company, alleging a “debt default”" | article unavailable |
| 29 Apr 2026 | dictum.com | Lawsuit | Dictum GmbH from Plattling in the district of Deggendorf has applied to the insolvency court Deggendorf for self-insolvency. | [Nach 170 Jahren: Traditions-Unternehmen aus Bayern stellt…](https://www.t-online.de/finanzen/aktuelles/wirtschaft/id_101234180/werkzeughersteller-dictum-aus-plattling-meldet-insolvenz-an.html) · t-online.de |
| 29 Apr 2026 | papresa.es | Announcement | Spanish newsprint and recycled containerboard producer Papresa has filed for insolvency. According to a notice from the Spanish insolvency register,… | [Papresa files for insolvency](https://euwid-paper.com/news/companies/papresa-files-for-insolvency-and-will-be-liquidated-280426/) · euwid-paper.com |
| 27 Apr 2026 | sbi.co.in | Lawsuit | In 2018, ICICI Bank filed the first insolvency petition against JAL, followed by SBI in 2022. | article unavailable |
| 27 Apr 2026 | jalindia.com | Lawsuit | In 2018, ICICI Bank filed the first insolvency petition against JAL, followed by SBI in 2022. | article unavailable |
| 27 Apr 2026 | icicibank.com | Lawsuit | In 2018, ICICI Bank filed the first insolvency petition against JAL, followed by SBI in 2022. | article unavailable |
| 23 Apr 2026 | commissionbureau.com | Lawsuit | The Commission has also requested the opening of insolvency proceedings in its own administration on April 1, 2026. | article unavailable |
| 20 Apr 2026 | tvsscs.com | Lawsuit | Following the settlement, TVS Supply Chain withdrew its appeal related to insolvency proceedings, confirming that both companies have mutually… | [TVS Supply Chain Settles Debt Dispute with ZTE Telecom India](https://www.electronicsforyou.biz/industry-buzz/tvs-supply-chain-settles-debt-dispute-with-zte-telecom-indiatelecomtvs-supply-chain-settles-debt-dispute-with-zte-telecom-india/) · electronicsforyou.biz |
| 19 Apr 2026 | tvsscs.com | Lawsuit | TVS Supply Chain Solutions has settled its debt dispute with ZTE Telecom India and withdrawn its appeal in NCLAT against an order that rejected… | [TVS Supply settles dispute with ZTE, withdraws insolvency plea in…](https://www.cnbctv18.com/market/tvs-supply-settles-dispute-with-zte-withdraws-insolvency-plea-in-nclat-ws-l-19889199.htm) · cnbctv18.com |
| 18 Apr 2026 | qvcgroup.com | Lawsuit | "The teleshopping station has filed for insolvency in the USA." | article unavailable |
| 16 Apr 2026 | kelheim-fibres.com | Lawsuit | German viscose fibre producer Kelheim Fibres announced that it would cease operations as of 31 March. The company filed for insolvency in October… | [Fibre Excellence files for insolvency, but remains hopeful of a rescue](https://www.euwid-paper.com/news/companies/fibre-excellence-files-for-insolvency-but-remains-hopeful-of-a-rescue-160426/) · euwid-paper.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type company_announcement --event-type lawsuit --q insolvency --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type company_announcement --event-type lawsuit --q insolvency --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type company_announcement --event-type lawsuit --q insolvency --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["company_announcement", "lawsuit"], "q": "insolvency", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["company_announcement", "lawsuit"], "q": "insolvency", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Article filters require a matching source article in the same window; records without a matching article are excluded. Each deal still counts once.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.
- Zero-count periods are included; partial_period marks buckets only partly covered by the window.
- shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)

## Related demonstrations

- [Fundraise](fundraise.md)
- [Bank Mergers News](bank-mergers-news.md)
- [Joint Venture](joint-venture.md)
- [Mergers and Acquisitions](mergers-and-acquisitions.md)
