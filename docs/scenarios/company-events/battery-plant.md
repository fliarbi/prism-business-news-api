# Battery Plant: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “battery plant” · 170/month India · 880/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [battery-plant.json](../../examples/scenarios/battery-plant.json).

**Question.** How many battery plant events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `asset_acquisition`, `company_announcement` and the word “battery” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 784 |
| Companies (with a domain) | 364 |
| Source articles | 674 |
| Busiest month | Aug 2025 (119 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 3.0% · 0.4% · 97% of 263 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Announcement | Asset acquisition |  |
| --- | ---: | ---: | ---: | --- |
| May 2025 | 48 | 38 | 10 | ████████ |
| Jun 2025 | 35 | 32 | 3 | ██████ |
| Jul 2025 | 50 | 29 | 21 | ████████ |
| Aug 2025 | 119 | 63 | 56 | ████████████████████ |
| Sep 2025 | 70 | 52 | 18 | ████████████ |
| Oct 2025 | 56 | 40 | 16 | █████████ |
| Nov 2025 | 43 | 31 | 12 | ███████ |
| Dec 2025 | 44 | 30 | 14 | ███████ |
| Jan 2026 | 53 | 39 | 14 | █████████ |
| Feb 2026 | 85 | 48 | 37 | ██████████████ |
| Mar 2026 | 73 | 47 | 26 | ████████████ |
| Apr 2026 | 108 | 81 | 27 | ██████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 6 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | menarini.com | Announcement | Menarini confirms that a Class II battery-electric vehicle is under development, extending its product range beyond urban applications toward… | [Menarini focuses on Europe-wide presence, upcoming e-bus debut and…](https://www.sustainable-bus.com/news/menarini-new-electric-bus-model-and-intercity-project/) · sustainable-bus.com |
| 30 Apr 2026 | drax.com | Announcement | With our first battery storage projects and the commissioning of our first OCGT unit progressing, we are growing our UK FlexGen portfolio. | [Drax hails good performance as it 'supports UK energy at a critical…](https://www.business-live.co.uk/economic-development/drax-hails-good-performance-supports-33866317) · business-live.co.uk |
| 29 Apr 2026 | adstec-energy.com | Announcement | Large-scale storage as a strategic next step With the SKM project (1 GW / 4 GWh), ADS-TEC Energy is developing one of Europe’s largest battery… | [Where flexibility becomes a business model: ADS-TEC Energy releases…](https://ads-tec-com.mynewsdesk.com/pressreleases/where-flexibility-becomes-a-business-model-ads-tec-energy-releases-updated-investor-presentation-3445668) · ads-tec-com.mynewsdesk.com |
| 28 Apr 2026 | keliber.fi | Announcement | The €783 million project is operated by Keliber Oy, a Finnish mining and battery-materials company. | [Finland launches Europe's first full lithium mine-to-refinery product](http://www.euronews.com/business/2026/04/28/finland-becomes-first-in-europe-to-run-full-lithium-mine-to-refinery-cycle) · euronews.com |
| 28 Apr 2026 | southstarbatterymetals.com | Announcement | South Star Battery Metals Corp. (" South Star " or the " Company ") (TSXV: STS) (OTCQB: STSBF ) is pleased to report that the first week of… | article unavailable |
| 26 Apr 2026 | adanigreenenergy.com | Announcement | The company plans to invest about Rs 15,000 crore to add battery energy storage capacity over 10 gigawat-hour (GWH) in the current fiscal year. | [अडानी की इस कंपनी ने ₹15000 करोड़ निवेश का किया ऐलान, शेयर पर रहेगी…](https://www.livehindustan.com/business/adani-group-company-adani-green-to-invest-15000-crore-rs-to-add-10-gigawatt-battery-storage-in-fy27-now-share-in-focus-201777205336624.html) · livehindustan.com |
| 26 Apr 2026 | zgh.com | Announcement | Geely also revealed major progress in solid-state battery technology, with testing of its first internally developed battery pack set to begin in… | article unavailable |
| 24 Apr 2026 | masdar.ae | Announcement | Among its upcoming projects is a large 5.2GW solar development in Abu Dhabi, which will be combined with 19GWh of battery energy storage. | article unavailable |
| 23 Apr 2026 | allianzgi.com | Asset acquisition | Through the deal, Allianz further expands its exposure to the large-scale battery storage sector. | article unavailable |
| 23 Apr 2026 | totalenergies.eg | Asset acquisition | the transaction represents the company's second investment in battery storage in Germany after it agreed in March to buy a 50% stake in a project… | article unavailable |
| 23 Apr 2026 | allianzgi.com | Asset acquisition | the transaction represents the company's second investment in battery storage in Germany after it agreed in March to buy a 50% stake in a project… | article unavailable |
| 23 Apr 2026 | ntt-ae.co.jp | Asset acquisition | Eku Energy acquired the battery system from NTT Anode Energy Corp, a wholly owned subsidiary of NTT Inc (TYO:9432), the company announced on… | [Eku Energy Japan starts up 2-MW battery in Fukuoka](https://renewablesnow.com/news/eku-energy-japan-starts-up-2-mw-battery-in-fukuoka-1293591/) · renewablesnow.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type asset_acquisition --event-type company_announcement --q battery --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type asset_acquisition --event-type company_announcement --q battery --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type asset_acquisition --event-type company_announcement --q battery --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["asset_acquisition", "company_announcement"], "q": "battery", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["asset_acquisition", "company_announcement"], "q": "battery", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Article filters require a matching source article in the same window; records without a matching article are excluded. Each deal still counts once.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.
- Zero-count periods are included; partial_period marks buckets only partly covered by the window.
- shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)

## Related demonstrations

- [Asset Sale](asset-sale.md)
- [CEO Appointment](ceo-appointment.md)
- [Bankruptcy News](bankruptcy-news.md)
- [Data Center Investment](data-center-investment.md)
