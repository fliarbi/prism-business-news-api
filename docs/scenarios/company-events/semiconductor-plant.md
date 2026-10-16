# Semiconductor Plant: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “semiconductor plant” · 590/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [semiconductor-plant.json](../../examples/scenarios/semiconductor-plant.json).

**Question.** How many semiconductor plant events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `asset_acquisition`, `company_announcement` and the word “semiconductor” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 227 |
| Companies (with a domain) | 102 |
| Source articles | 195 |
| Busiest month | Jan 2026 (32 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 4.6% · 0.0% · 95% of 108 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Announcement | Asset acquisition |  |
| --- | ---: | ---: | ---: | --- |
| May 2025 | 10 | 10 | 0 | ██████ |
| Jun 2025 | 12 | 8 | 4 | ████████ |
| Jul 2025 | 18 | 15 | 3 | ███████████ |
| Aug 2025 | 18 | 15 | 3 | ███████████ |
| Sep 2025 | 30 | 25 | 5 | ███████████████████ |
| Oct 2025 | 24 | 20 | 4 | ███████████████ |
| Nov 2025 | 20 | 18 | 2 | ████████████ |
| Dec 2025 | 13 | 11 | 2 | ████████ |
| Jan 2026 | 32 | 19 | 13 | ████████████████████ |
| Feb 2026 | 16 | 16 | 0 | ██████████ |
| Mar 2026 | 13 | 12 | 1 | ████████ |
| Apr 2026 | 21 | 12 | 9 | █████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 6 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | airproducts.com | Announcement | Air Products said it is currently executing around $1bn in air separation and hydrogen projects in Asia tied to multi-phase semiconductor and memory… | article unavailable |
| 29 Apr 2026 | amazon.com | Announcement | Amazon is now among the top three datacenter chip businesses in the world, as its semiconductor business surpassed a $20 billion annual run rate ...… | [Amazon's chips become a $20B business](https://www.theregister.com/software/2026/04/30/amazons-chips-become-a-20b-business/5221236) · theregister.com |
| 29 Apr 2026 | amazon.com | Announcement | Amazon is now among the top three datacenter chip businesses in the world, as its semiconductor business surpassed a $20 billion annual run rate ... | [Amazon's chips become a $20B business](https://theregister.com/2026/04/29/amazon_chips_20b_business/) · theregister.com |
| 28 Apr 2026 | infineon.com | Announcement | Infineon Technologies, Germany’s largest semiconductor manufacturer, has announced a major acceleration of its footprint in India, pivoting toward a… | [Infineon Rapid Expansion into the Indian Semiconductor Ecosystem -…](https://techstory.in/infineons-rapid-expansion-into-the-indian-semiconductor-ecosystem/) · techstory.in |
| 22 Apr 2026 | tsmc.com | Announcement | SANTA CLARA, California -- Taiwan Semiconductor Manufacturing Co. on Wednesday gave a glimpse of its next-generation A13 and A12 chipmaking… | [TSMC teases next-gen A13 and A12 technologies for 2029 production](https://asia.nikkei.com/business/tech/semiconductors/tsmc-teases-next-gen-a13-and-a12-technologies-for-2029-production) · asia.nikkei.com |
| 22 Apr 2026 | samsung.com | Announcement | In 2025, Samsung signed a semiconductor manufacturing agreement with Tesla valued at approximately $16.5 billion. | article unavailable |
| 21 Apr 2026 | samsungsem.co.kr | Announcement | shares of Samsung Electro-Mechanics, the Samsung Electro-Mechanics' FC-BGA substrate for autonomous driving Samsung Electro-Mechanics Co. has… | article unavailable |
| 20 Apr 2026 | bannerhealth.com | Asset acquisition | Banner Health has acquired an 18.8-acre land parcel near the massive Taiwan Semiconductor Manufacturing Company (TSMC) factory in north Phoenix,… | [Banner Health Pays $22M for 18.8 Acres Near TSMC’s $165B Chip Plant…](https://cremarketbeat.com/banner-health-pays-22m-for-18-8-acres-near-tsmcs-165b-chip-plant-in-north-phoenix/) · cremarketbeat.com |
| 16 Apr 2026 | intel.com | Announcement | the semiconductor giant announced its involvement with Musk’s companies—SpaceX, xAI and Tesla—on Terafab. | [Exclusive: Intel Tells Staff It Will Disclose Scope Of Work With…](https://www.crn.com.au/news-network/components-peripherals/2026/exclusive-intel-tells-staff-it-will-disclose-scope-of-work-w) · crn.com.au |
| 13 Apr 2026 | tsmc.com | Announcement | Taiwan Semiconductor Manufacturing Company (TSMC) is accelerating its multibillion dollar expansion in Arizona semiconductor manufacturing site, as… | article unavailable |
| 13 Apr 2026 | tsmc.com | Announcement | Taiwan Semiconductor Manufacturing Co (TSMC) is set to accelerate its multibillion-dollar expansion in Arizona, according to CNBC, deepening its US… | [TSMC Accelerates Arizona Expansion as AI Demand Surges](http://technologymagazine.com/news/tsmc-accelerates-arizona-expansion-as-ai-demand-surges) · technologymagazine.com |
| 7 Apr 2026 | vanguardlogistics.com | Asset acquisition | Vanguard Group Inc. now owns 655,877 shares of the semiconductor company’s stock worth $3,975,000 after acquiring an additional 28,587 shares during… | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type asset_acquisition --event-type company_announcement --q semiconductor --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type asset_acquisition --event-type company_announcement --q semiconductor --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type asset_acquisition --event-type company_announcement --q semiconductor --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["asset_acquisition", "company_announcement"], "q": "semiconductor", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["asset_acquisition", "company_announcement"], "q": "semiconductor", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Media Mergers](media-mergers.md)
- [New Factory](new-factory.md)
- [Pharma Layoffs](pharma-layoffs.md)
- [Antitrust Lawsuit](antitrust-lawsuit.md)
