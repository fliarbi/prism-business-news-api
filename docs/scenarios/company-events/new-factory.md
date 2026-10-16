# New Factory: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “new factory” · 590/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [new-factory.json](../../examples/scenarios/new-factory.json).

**Question.** How many new factory events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `company_announcement`, `asset_acquisition` and the word “factory” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 542 |
| Companies (with a domain) | 324 |
| Source articles | 488 |
| Busiest month | Aug 2025 (111 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 23% · 1.2% · 76% of 167 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Announcement | Asset acquisition |  |
| --- | ---: | ---: | ---: | --- |
| May 2025 | 38 | 26 | 12 | ███████ |
| Jun 2025 | 11 | 11 | 0 | ██ |
| Jul 2025 | 49 | 39 | 10 | █████████ |
| Aug 2025 | 111 | 66 | 45 | ████████████████████ |
| Sep 2025 | 55 | 48 | 7 | ██████████ |
| Oct 2025 | 37 | 34 | 3 | ███████ |
| Nov 2025 | 37 | 28 | 9 | ███████ |
| Dec 2025 | 34 | 30 | 4 | ██████ |
| Jan 2026 | 41 | 29 | 12 | ███████ |
| Feb 2026 | 43 | 33 | 10 | ████████ |
| Mar 2026 | 39 | 35 | 4 | ███████ |
| Apr 2026 | 47 | 41 | 6 | ████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 5 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | luxinnovation.lu | Announcement | Minister of Economics Lex Delles and CEO Mario Grotz presented the Annual Report 2025 on Thursday, and also provided an update to the Luxembourg AI… | [Luxinnovation schließt strategische Neuausrichtung ab](https://www.wort.lu/wirtschaft/luxinnovation-schliesst-strategische-neuausrichtung-ab/150465278.html) · wort.lu |
| 30 Apr 2026 | talleys.co.nz | Announcement | Talley's is closing its Westport fish processing factory, the company has confirmed. | [Talley's confirms Westport factory closure](https://www.odt.co.nz/regions/west-coast/talleys-confirms-westport-factory-closure-rnz) · odt.co.nz |
| 29 Apr 2026 | corning.com | Announcement | In March, Corning broke ground on a brand-new factory where it will manufacture cables specifically for Meta, which highlights the scale of the deal. | [This Super Semiconductor Stock Is Obliterating Nvidia, AMD, and…](https://www.theglobeandmail.com/investing/markets/stocks/GLW/pressreleases/1594991/this-super-semiconductor-stock-is-obliterating-nvidia-amd-and-broadcom-in-2026/) · theglobeandmail.com |
| 29 Apr 2026 | singer.lk | Asset acquisition | Singer (Sri Lanka) PLC has officially entered into a Sale Purchase Agreement to acquire the factory premises of ACME Printing and Packaging PLC. | [Singer to Acquire ACME Printing Factory for Rs. 630 Million -…](http://bizenglish.adaderana.lk/singer-to-acquire-acme-printing-factory-for-rs-630-million/) · bizenglish.adaderana.lk |
| 29 Apr 2026 | acmelk.com | Asset acquisition | Singer (Sri Lanka) PLC has officially entered into a Sale Purchase Agreement to acquire the factory premises of ACME Printing and Packaging PLC. | [Singer to Acquire ACME Printing Factory for Rs. 630 Million -…](http://bizenglish.adaderana.lk/singer-to-acquire-acme-printing-factory-for-rs-630-million/) · bizenglish.adaderana.lk |
| 28 Apr 2026 | forvia.com | Asset acquisition | The Forvia automotive manufacturer, which has a factory in Bains-sur-Oust (Ille-et-Vilaine), announces that he has entered into an agreement with… | [L'usine Forvia de Bains-sur-Oust va passer aux mains du fonds…](https://www.lejournaldesentreprises.com/breve/lusine-forvia-de-bains-sur-oust-va-passer-aux-mains-du-fonds-americain-apollo-2141931) · lejournaldesentreprises.com |
| 28 Apr 2026 | apollo-oe.com | Asset acquisition | The Forvia automotive manufacturer, which has a factory in Bains-sur-Oust (Ille-et-Vilaine), announces that he has entered into an agreement with… | [L'usine Forvia de Bains-sur-Oust va passer aux mains du fonds…](https://www.lejournaldesentreprises.com/breve/lusine-forvia-de-bains-sur-oust-va-passer-aux-mains-du-fonds-americain-apollo-2141931) · lejournaldesentreprises.com |
| 22 Apr 2026 | nomadfoods.com | Announcement | Nomad Foods has announced the intention to close the factory by the end of 2026. | article unavailable |
| 22 Apr 2026 | changanqatar.com | Announcement | The automaker certainly appears to think so, and is reportedly considering a factory in northern Spain, with the Aragon region cited as a leading… | [Changan aims to crack top ten global OEMs by 2030 \| Automotive World](https://www.automotiveworld.com/news/changan-aims-to-crack-top-ten-global-oems-by-2030/) · automotiveworld.com |
| 22 Apr 2026 | suse.com | Announcement | SUSE AI Factory, a joint solution combining SUSE’s open-source AI stack with Nvidia’s enterprise AI infrastructure, was launched on Tuesday. | article unavailable |
| 22 Apr 2026 | rivian.com | Announcement | A tornado struck Rivian’s electric vehicle factory in Normal, Illinois, last Friday, temporarily halting operations at a newer section of the… | article unavailable |
| 22 Apr 2026 | nvidia.com | Announcement | On March 31 local time, NVIDIA and Marvell announced a strategic partnership to connect Marvell with NVIDIA's AI factory and AI-RAN ecosystem… | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type company_announcement --event-type asset_acquisition --q factory --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type company_announcement --event-type asset_acquisition --q factory --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type company_announcement --event-type asset_acquisition --q factory --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["company_announcement", "asset_acquisition"], "q": "factory", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["company_announcement", "asset_acquisition"], "q": "factory", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Data Center Investment](data-center-investment.md)
- [Media Mergers](media-mergers.md)
- [Semiconductor Plant](semiconductor-plant.md)
- [Pharma Layoffs](pharma-layoffs.md)
