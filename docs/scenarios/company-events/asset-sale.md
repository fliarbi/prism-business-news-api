# Asset Sale: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “asset sale” · 260/month India · 880/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [asset-sale.json](../../examples/scenarios/asset-sale.json).

**Question.** How many asset sale events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `asset_acquisition`, `ma` and the word “sale” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 4,902 |
| Companies (with a domain) | 3,272 |
| Source articles | 3,456 |
| Busiest month | Dec 2025 (547 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 9.0% · 4.7% · 86% of 1,718 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | M&A | Asset acquisition |  |
| --- | ---: | ---: | ---: | --- |
| May 2025 | 286 | 139 | 147 | ██████████ |
| Jun 2025 | 332 | 219 | 113 | ████████████ |
| Jul 2025 | 375 | 196 | 179 | ██████████████ |
| Aug 2025 | 369 | 178 | 191 | █████████████ |
| Sep 2025 | 387 | 183 | 204 | ██████████████ |
| Oct 2025 | 424 | 238 | 186 | ████████████████ |
| Nov 2025 | 393 | 229 | 164 | ██████████████ |
| Dec 2025 | 547 | 301 | 246 | ████████████████████ |
| Jan 2026 | 401 | 211 | 190 | ███████████████ |
| Feb 2026 | 501 | 248 | 253 | ██████████████████ |
| Mar 2026 | 432 | 244 | 188 | ████████████████ |
| Apr 2026 | 455 | 219 | 236 | █████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 5 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | perrigo.com | Asset acquisition | Perrigo Company plc ... today announced that it has completed the previously announced sale of its branded Dermacosmetics business to Karo… | [Perrigo gets €306M upfront as it exits ACO, Biodermal, Emolium,…](https://www.stocktitan.net/news/PRGO/perrigo-completes-divestiture-of-dermacosmetics-3bosj7csz1zb.html) · stocktitan.net |
| 30 Apr 2026 | karopharma.com | Asset acquisition | Perrigo Company plc ... today announced that it has completed the previously announced sale of its branded Dermacosmetics business to Karo… | [Perrigo gets €306M upfront as it exits ACO, Biodermal, Emolium,…](https://www.stocktitan.net/news/PRGO/perrigo-completes-divestiture-of-dermacosmetics-3bosj7csz1zb.html) · stocktitan.net |
| 30 Apr 2026 | ruckusnetworks.com | M&A | Vistance Networks Inc. shares surged more than 22% Thursday, climbing to $12.84 in morning trading after the networking technology company reported… | [Vistance Networks Stock Soars 22% on Q1 Beat, $1.85B RUCKUS Sale to…](https://ibtimes.com.au/vistance-networks-stock-soars-22-q1-beat-185b-ruckus-sale-belden-100m-buyback-plan-1867876) · ibtimes.com.au |
| 30 Apr 2026 | belden.com | M&A | Vistance Networks Inc. shares surged more than 22% Thursday, climbing to $12.84 in morning trading after the networking technology company reported… | [Vistance Networks Stock Soars 22% on Q1 Beat, $1.85B RUCKUS Sale to…](https://ibtimes.com.au/vistance-networks-stock-soars-22-q1-beat-185b-ruckus-sale-belden-100m-buyback-plan-1867876) · ibtimes.com.au |
| 30 Apr 2026 | trepp.com | M&A | Daily Mail and General Trust plc (DMGT) announced the sale of its American real estate information subsidiary, Trepp, to the Fitch Group for… | [Daily Mail And General Trust Plc \|](https://www.webdisclosure.com/article/dmgt-vend-trepp-a-fitch-group-pour-1-milliard-de-dollars-cVzVrFRgaFQ) · webdisclosure.com |
| 30 Apr 2026 | fitch.group | M&A | Daily Mail and General Trust plc (DMGT) announced the sale of its American real estate information subsidiary, Trepp, to the Fitch Group for… | [Daily Mail And General Trust Plc \|](https://www.webdisclosure.com/article/dmgt-vend-trepp-a-fitch-group-pour-1-milliard-de-dollars-cVzVrFRgaFQ) · webdisclosure.com |
| 30 Apr 2026 | tandg.global | Asset acquisition | Meanwhile, the sale to Bidfood is proposed to include T&G’s Fijian business and its Pacific Island Exports business. | [T&G Global is in advanced discussions to sell two key parts of its…](https://www.freshfruitportal.com/news/2026/04/30/tg-global-divestment/) · freshfruitportal.com |
| 30 Apr 2026 | bidfood.co.uk | Asset acquisition | Meanwhile, the sale to Bidfood is proposed to include T&G’s Fijian business and its Pacific Island Exports business. | [T&G Global is in advanced discussions to sell two key parts of its…](https://www.freshfruitportal.com/news/2026/04/30/tg-global-divestment/) · freshfruitportal.com |
| 30 Apr 2026 | tandg.global | Asset acquisition | The proposed sale to Bidfood includes T&G's Fijian business and T&G Fresh's Pacific Island Exports business. | article unavailable |
| 30 Apr 2026 | bidfood.co.uk | Asset acquisition | The proposed sale to Bidfood includes T&G's Fijian business and T&G Fresh's Pacific Island Exports business. | article unavailable |
| 30 Apr 2026 | ccpgames.com | M&A | It has announced that it is selling the studio back to its management. EVE Online In a report to the South Korean regulator, Pearl Abyss stated that… | [Pearl Abyss sold the creators of EVE Online for much less than it…](https://gameworldobserver.com/2026/04/30/pearl-abyss-sold-the-creators-of-eve-online-for-much-less-than-it-purchased-them-for) · gameworldobserver.com |
| 30 Apr 2026 | novobanco.pt | M&A | Today announced it has successfully completed the sale of its majority stake in Novo Banco, S.A. (“novobanco” or “the bank”), Portugal’s… | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type asset_acquisition --event-type ma --q sale --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type asset_acquisition --event-type ma --q sale --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type asset_acquisition --event-type ma --q sale --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["asset_acquisition", "ma"], "q": "sale", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["asset_acquisition", "ma"], "q": "sale", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [SEBI Order](sebi-order.md)
- [Capital Infusion](capital-infusion.md)
- [CEO Appointment](ceo-appointment.md)
- [Battery Plant](battery-plant.md)
