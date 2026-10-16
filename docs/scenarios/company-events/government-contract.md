# Government Contract: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “government contract” · 2,900/month India · 22,200/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [government-contract.json](../../examples/scenarios/government-contract.json).

**Question.** How many government contract events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `contracts` and the word “government” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 683 |
| Companies (with a domain) | 452 |
| Source articles | 520 |
| Busiest month | Sep 2025 (87 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 6.6% · 0.8% · 93% of 256 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 33 | ████████ |
| Jun 2025 | 30 | ███████ |
| Jul 2025 | 60 | ██████████████ |
| Aug 2025 | 77 | ██████████████████ |
| Sep 2025 | 87 | ████████████████████ |
| Oct 2025 | 60 | ██████████████ |
| Nov 2025 | 49 | ███████████ |
| Dec 2025 | 42 | ██████████ |
| Jan 2026 | 49 | ███████████ |
| Feb 2026 | 71 | ████████████████ |
| Mar 2026 | 57 | █████████████ |
| Apr 2026 | 68 | ████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 6 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 27 Apr 2026 | stengg.com | Contracts | ground‑segment infrastructure contracts from government integrators in Asia and Europe. | [ST Engineering bags S$4.8 billion in Q1 contracts on Middle East…](https://www.businesstimes.com.sg/companies-markets/st-engineering-bags-s4-8-billion-q1-contracts-middle-east-defence-aerospace-demand) · businesstimes.com.sg |
| 24 Apr 2026 | skgroup.co | Contracts | Through subsidiaries SK Telekom and SK Innovation, the conglomerate struck memorandums of understanding (MOUs) with the Vietnam’s National… | article unavailable |
| 24 Apr 2026 | stackitgroup.com | Contracts | The Dutch government has signed a framework agreement with the German cloud platform Stackit. | [Dutch government selects Stackit, Lidl's sister company, as its…](https://www.techzine.eu/news/infrastructure/140768/dutch-government-selects-stackit-lidls-sister-company-as-its-cloud-alternative/) · techzine.eu |
| 23 Apr 2026 | loomsolar.com | Contracts | Loom Solar has secured a second land allotment from the Uttar Pradesh government to scale its solar and Battery Energy Storage Systems (BESS)… | article unavailable |
| 19 Apr 2026 | samsungcnt.com | Contracts | The Finocchiaro CLP Government and Samsung C&T have signed a Memorandum of Understanding (MoU) to unlock new projects and investment across energy,… | [Strengthening Investment Cooperation With South Korea](https://www.nationaltribune.com.au/strengthening-investment-cooperation-with-south-korea/) · nationaltribune.com.au |
| 19 Apr 2026 | gov.au | Contracts | The federal government is contributing $240 million towards the precinct and stadium, which was conditional on the master plan being approved. | [The Tasmanian government has selected Constructure Joint Venture and…](https://www.yarrawongachronicle.com.au/aap-entertainment/chinese-state-firm-among-top-afl-stadium-build-bidders/) · yarrawongachronicle.com.au |
| 18 Apr 2026 | hrrl.in | Contracts | Tripartite Agreement to Ensure Feedstock Supply The proposed agreement will bring together HPCL Rajasthan Refinery Limited (HRRL), the state… | [Rajasthan Fast-Tracks Tripartite Pact for Petro Zone Development \|…](https://chemindigest.com/rajasthan-fast-tracks-tripartite-pact-for-petro-zone-development/) · chemindigest.com |
| 17 Apr 2026 | india.gov.in | Contracts | APOLLO MICRO SYSTEMS HAS POINTED OUT IN EXCHANGE FILING THAT THE COMPANY FOR MANUFACTURING A VARIETY OF DIFFERENT DEFENCE SYSTEMS AND AMMUNITION OF… | [सरकार से मिला मिसाइल और रॉकेट बनाने का लाइसेंस, डिफेंस शेयर में…](https://www.livehindustan.com/business/defence-stock-apollo-micro-systems-jumped-over-16-percent-today-company-bagged-license-for-manufacture-of-ammunitions-201776435369843.html) · livehindustan.com |
| 17 Apr 2026 | apollo-micro.com | Contracts | APOLLO MICRO SYSTEMS HAS POINTED OUT IN EXCHANGE FILING THAT THE COMPANY FOR MANUFACTURING A VARIETY OF DIFFERENT DEFENCE SYSTEMS AND AMMUNITION OF… | [सरकार से मिला मिसाइल और रॉकेट बनाने का लाइसेंस, डिफेंस शेयर में…](https://www.livehindustan.com/business/defence-stock-apollo-micro-systems-jumped-over-16-percent-today-company-bagged-license-for-manufacture-of-ammunitions-201776435369843.html) · livehindustan.com |
| 17 Apr 2026 | fusionmedialtd.com | Contracts | Government agency Active Travel England has appointed communications firm Fusion Media to support the delivery of its Making Active Places… | article unavailable |
| 17 Apr 2026 | totalenergies.eg | Contracts | French energy giant TotalEnergies will no longer pursue offshore wind projects in the US after securing a US$1bn deal with the government to focus… | article unavailable |
| 16 Apr 2026 | repsol.com | Contracts | Spanish Repsol announced on Thursday (16) an agreement with the government of Venezuela and the state PDVSA to resume operational control of assets… | [Espanhola Repsol retoma controle na Venezuela e planeja triplicar…](https://www.moneytimes.com.br/repsol-retoma-controle-na-venezuela-e-planeja-triplicar-producao-de-petroleo-em-3-anos-2/) · moneytimes.com.br |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type contracts --q government --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type contracts --q government --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type contracts --q government --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["contracts"], "q": "government", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["contracts"], "q": "government", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Joint Venture](joint-venture.md)
- [Mergers and Acquisitions](mergers-and-acquisitions.md)
- [Earnings](earnings.md)
- [SME IPO](sme-ipo.md)
