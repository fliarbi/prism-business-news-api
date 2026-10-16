# Strategic Partnership: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “strategic partnership” · 1,600/month India · 2,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [strategic-partnership.json](../../examples/scenarios/strategic-partnership.json).

**Question.** How many strategic partnership events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `company_announcement`, `contracts` and the word “partnership” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 1,290 |
| Companies (with a domain) | 989 |
| Source articles | 1,027 |
| Busiest month | Feb 2026 (150 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 1.9% · 0.1% · 98% of 693 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Contracts | Announcement |  |
| --- | ---: | ---: | ---: | --- |
| May 2025 | 71 | 44 | 27 | █████████ |
| Jun 2025 | 75 | 41 | 34 | ██████████ |
| Jul 2025 | 70 | 45 | 25 | █████████ |
| Aug 2025 | 134 | 79 | 55 | ██████████████████ |
| Sep 2025 | 119 | 59 | 60 | ████████████████ |
| Oct 2025 | 99 | 53 | 46 | █████████████ |
| Nov 2025 | 149 | 84 | 65 | ████████████████████ |
| Dec 2025 | 134 | 87 | 47 | ██████████████████ |
| Jan 2026 | 79 | 40 | 39 | ███████████ |
| Feb 2026 | 150 | 78 | 72 | ████████████████████ |
| Mar 2026 | 114 | 65 | 49 | ███████████████ |
| Apr 2026 | 96 | 56 | 40 | █████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 4 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 29 Apr 2026 | sambanova.ai | Announcement | Harry Ault, Chief Revenue Officer at SambaNova, visited Sydney to advance the strategic partnership between SambaNova and SCX, meeting with… | [SCX Brings Sovereign AI to Equinix’s AI Ecosystem and Confirms…](https://www.businessupturn.com/brand-post/scx-brings-sovereign-ai-to-equinixs-ai-ecosystem-and-confirms-national-expansion-with-sambanova-sn50/) · businessupturn.com |
| 28 Apr 2026 | doordash.com | Announcement | DoorDash reports one of its largest grocery expansions in Canada through a new partnership with Empire Company, bringing more than 1,000 stores… | article unavailable |
| 28 Apr 2026 | stengg.com | Contracts | ST Engineering’s freighter conversion business, in partnership with EFW, secured contracts for Airbus A330-300 passenger-to-freighter conversions… | [ST Engineering Reports Strong Aftermarket Growth \| Aviation Week…](https://aviationweek.com/mro/aircraft-propulsion/st-engineering-reports-strong-aftermarket-growth) · aviationweek.com |
| 28 Apr 2026 | stengg.com | Contracts | Meanwhile, ST Engineering’s freighter conversion business, in partnership with EFW, secured contracts for Airbus A330-300 passenger-to-freighter… | [ST Engineering Reports Strong Aftermarket Growth \| Aviation Week…](https://www.aviationweek.com/mro/aircraft-propulsion/st-engineering-reports-strong-aftermarket-growth) · aviationweek.com |
| 28 Apr 2026 | aldar.com | Announcement | and the acquisition of The Link at Masdar City for Dh654 million in partnership with Mubadala Investment Company | article unavailable |
| 28 Apr 2026 | aldar.com | Announcement | The company also aims to unveil a new mega development in Dubai this year after buying two plots of land near Nad Al Sheba and Palm Jebel Ali in… | article unavailable |
| 27 Apr 2026 | riotinto.com | Announcement | Rio Tinto has a strong first quarter of 2026 — and is sending a clear signal towards sustainability with a new industrial partnership. | [Rio Tinto: Prysmian-Partnerschaft für Low-Carbon-Kabel](https://www.boerse-express.com/news/articles/rio-tinto-prysmian-partnerschaft-fuer-low-carbon-kabel-898506) · boerse-express.com |
| 27 Apr 2026 | cph2.com | Contracts | The companies have agreed to develop a partnership seeking the supply, installation, commissioning and maintenance of 175MW of electrolysers over… | [CPH2 inks MoU with BKW’s ABE Gruppe for 175MW rollout of…](https://newsnreleases.com/2026/04/27/cph2-mou-bkw-abe-gruppe-175mw-membrane-free-electrolyser/) · newsnreleases.com |
| 27 Apr 2026 | abe-gruppe.de | Contracts | The companies have agreed to develop a partnership seeking the supply, installation, commissioning and maintenance of 175MW of electrolysers over… | [CPH2 inks MoU with BKW’s ABE Gruppe for 175MW rollout of…](https://newsnreleases.com/2026/04/27/cph2-mou-bkw-abe-gruppe-175mw-membrane-free-electrolyser/) · newsnreleases.com |
| 26 Apr 2026 | bloomenergy.com | Announcement | The main driver of this rally is an extended partnership with Oracle. | [Bloom Energy: EPS $0,45 schlägt Konsens](https://www.boerse-express.com/news/articles/bloom-energy-eps-045-schlaegt-konsens-897756) · boerse-express.com |
| 24 Apr 2026 | airliquide.com | Contracts | To support this partnership, Air Liquide will invest over 350 million U.S. dollars to expand its production with an additional Air Separation Unit… | [Air Liquide enters agreement to supply gases for…](https://www.chemengonline.com/air-liquide-enters-agreement-to-supply-gases-for-low-carbon-emissions-steel-facility/) · chemengonline.com |
| 23 Apr 2026 | intelligence-airbusds.com | Contracts | Airbus and more closely its Defence and Space division, one of the three main members of the group that has been selected as a technical partner for… | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type company_announcement --event-type contracts --q partnership --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type company_announcement --event-type contracts --q partnership --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type company_announcement --event-type contracts --q partnership --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["company_announcement", "contracts"], "q": "partnership", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["company_announcement", "contracts"], "q": "partnership", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Q4 Results](q4-results.md)
- [Job Cuts](job-cuts.md)
- [It Layoffs](it-layoffs.md)
- [New Product Launch](new-product-launch.md)
