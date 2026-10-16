# Media Mergers: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “media mergers” · 20/month India · 1,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [media-mergers.json](../../examples/scenarios/media-mergers.json).

**Question.** How many media mergers events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `ma` and the word “media” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 1,183 |
| Companies (with a domain) | 719 |
| Source articles | 771 |
| Busiest month | Sep 2025 (133 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 9.7% · 2.9% · 87% of 598 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 65 | ██████████ |
| Jun 2025 | 74 | ███████████ |
| Jul 2025 | 115 | █████████████████ |
| Aug 2025 | 100 | ███████████████ |
| Sep 2025 | 133 | ████████████████████ |
| Oct 2025 | 85 | █████████████ |
| Nov 2025 | 96 | ██████████████ |
| Dec 2025 | 125 | ███████████████████ |
| Jan 2026 | 68 | ██████████ |
| Feb 2026 | 130 | ████████████████████ |
| Mar 2026 | 118 | ██████████████████ |
| Apr 2026 | 74 | ███████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 3 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | wtwhmedia.com | M&A | announced that it served as the exclusive sell side financial advisor to HealthLeaders, a brand of Simplify Compliance, a Leeds Equity Partners… | [Intrepid Investment Bankers Advises HealthLeaders on Its Sale to…](https://intrepidib.com/intrepid-investment-bankers-advises-healthleaders-on-its-sale-to-wtwh-media/) · intrepidib.com |
| 30 Apr 2026 | healthleadersmedia.com | M&A | announced that it served as the exclusive sell side financial advisor to HealthLeaders, a brand of Simplify Compliance, a Leeds Equity Partners… | [Intrepid Investment Bankers Advises HealthLeaders on Its Sale to…](https://intrepidib.com/intrepid-investment-bankers-advises-healthleaders-on-its-sale-to-wtwh-media/) · intrepidib.com |
| 30 Apr 2026 | ecdinternational.co.uk | M&A | Beyond Capital Partners Fund III, advised by Beyond Capital Partners GmbH (“BCP”), has acquired a majority stake in Munich-based SPCR Media GmbH… | [Beyond Capital acquires majority stake in SPCR Invest - FYB…](https://www.fyb.de/en/beyond-capital-acquires-majority-stake-in-spcr-invest) · fyb.de |
| 30 Apr 2026 | media.sanoma.fi | M&A | The Finnish group Sanoma, owner since 2021 of Santillana Spain, has acquired the Catalan publisher Vicens Vives, one of the main providers of… | [El grupo finlandés Sanoma compra la histórica editorial Vicens Vives](https://www.elperiodico.com/es/ocio-y-cultura/20260430/grupo-finlandes-sanoma-compra-vicens-129708886) · elperiodico.com |
| 30 Apr 2026 | otokar.com.tr | M&A | Otokar has signed an agreement to acquire a majority stake in Automecanica S.A. and its production facility in Mediaș, Romania. The agreement covers… | article unavailable |
| 30 Apr 2026 | judithripka.com | M&A | Xcel Brands, the media and consumer products company, sold the Judith Ripka jewelry brand to Fuzion Creations, a large wholesale manufacturer of… | [EXCLUSIVE: Xcel Brands Sells Judith Ripka](https://wwd.com/business-news/retail/xcel-brands-sells-judith-ripka-jewelry-brand-1238933629/) · wwd.com |
| 29 Apr 2026 | starkwood.com | M&A | Perseus Operating Group announced it has acquired Starkwood, a website design and digital media services provider, in a tech M&A deal. | [Tech M&A Deals: All Things Mobile Analytic, Glass Atlas, Perseus…](https://infotechlead.com/analytics/tech-ma-deals-all-things-mobile-analytic-glass-atlas-perseus-operating-95472) · infotechlead.com |
| 29 Apr 2026 | csiperseus.com | M&A | Perseus Operating Group announced it has acquired Starkwood, a website design and digital media services provider, in a tech M&A deal. | [Tech M&A Deals: All Things Mobile Analytic, Glass Atlas, Perseus…](https://infotechlead.com/analytics/tech-ma-deals-all-things-mobile-analytic-glass-atlas-perseus-operating-95472) · infotechlead.com |
| 29 Apr 2026 | totalenergies.eg | M&A | In this transaction, announced in November, TotalEnergies acquires 50% of a flexible electricity generation activity (gas and biomass power… | article unavailable |
| 29 Apr 2026 | eph-elektronik.de | M&A | In this transaction, announced in November, TotalEnergies acquires 50% of a flexible electricity generation activity (gas and biomass power… | article unavailable |
| 29 Apr 2026 | pep.com.au | M&A | Pacific Equity Partners has reportedly made a $747 million non-binding indicative offer to acquire ASX-listed out-of-home media company oOh!media. | [Private equity firm makes $747m play for oOh!media - Mediaweek](https://www.mediaweek.com.au/private-equity-firm-makes-747m-play-for-oohmedia/) · mediaweek.com.au |
| 29 Apr 2026 | oohmedia.com.au | M&A | Pacific Equity Partners has reportedly made a $747 million non-binding indicative offer to acquire ASX-listed out-of-home media company oOh!media. | [Private equity firm makes $747m play for oOh!media - Mediaweek](https://www.mediaweek.com.au/private-equity-firm-makes-747m-play-for-oohmedia/) · mediaweek.com.au |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type ma --q media --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type ma --q media --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type ma --q media --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["ma"], "q": "media", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["ma"], "q": "media", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Bankruptcy News](bankruptcy-news.md)
- [Data Center Investment](data-center-investment.md)
- [New Factory](new-factory.md)
- [Semiconductor Plant](semiconductor-plant.md)
