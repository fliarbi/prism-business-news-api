# Nintendo News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “nintendo news” · 90/month India · 60,500/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [nintendo-news.json](../../examples/scenarios/nintendo-news.json).

**Question.** What has the news reported about Nintendo in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `nintendo.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `nintendo.com` |
| Headlines, Jan – Apr 2026 (estimate) | 326 |
| Events, May 2025 – Apr 2026 | 88 |
| Most frequent event types | Announcement (38), Earnings (37), M&A (4) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 38% · 1.2% · 60% of 326 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 6 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 29 Apr 2026 | [Locals battling 11 years of roadworks are told to wait ANOTHER 12 months](https://www.thescottishsun.co.uk/motors/16210228/britains-longest-roadworks-drag-on/) | thescottishsun.co.uk | 7 | negative | — |
| 29 Apr 2026 | [Peacock in a Pickle: As the Streamer Lags Behind, What Happens Next? \| Analysis](https://dnyuz.com/2026/04/29/peacock-in-a-pickle-as-the-streamer-lags-behind-what-happens-next-analysis/) | dnyuz.com | 7 | positive | — |
| 25 Apr 2026 | [Comcast Q1 Earnings Call Highlights](https://www.defenseworld.net/2026/04/25/comcast-q1-earnings-call-highlights.html) | defenseworld.net | 7 | positive | Announcement |
| 24 Apr 2026 | [US companies welcome start of tariff refund](https://global.chinadaily.com.cn/a/202604/24/WS69eac4bda310d6866eb45400.html) | global.chinadaily.com.cn | 8 | negative | — |
| 23 Apr 2026 | [Gamers Sue Nintendo to Get a Cut of Trump's Tariff Refunds](https://gizmodo.com/gamers-sue-nintendo-to-get-a-cut-of-trumps-tariff-refunds-2000750151) | gizmodo.com | 8 | negative | — |
| 23 Apr 2026 | [Daiwa Securities Group Forecasts Strong Price Appreciation for Netflix (NASDAQ:NFLX) Stock](https://baseballnewssource.com/2026/04/23/daiwa-securities-group-forecasts-strong-price-appreciation-for-netflix-nasdaqnflx-stock/11097443.html) | baseballnewssource.com | 7 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Announcement | 38 |
| Earnings | 37 |
| M&A | 4 |
| Lawsuit | 4 |
| Incorporation | 2 |
| Key people | 1 |
| Contracts | 1 |
| New product | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Announcement | Earnings | M&A | Lawsuit |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 19 | 2 | 15 | 0 | 2 | ████████████████████ |
| Jun 2025 | 4 | 3 | 0 | 0 | 1 | ████ |
| Jul 2025 | 1 | 1 | 0 | 0 | 0 | █ |
| Aug 2025 | 6 | 3 | 3 | 0 | 0 | ██████ |
| Sep 2025 | 3 | 0 | 0 | 1 | 0 | ███ |
| Oct 2025 | 7 | 6 | 0 | 0 | 0 | ███████ |
| Nov 2025 | 18 | 3 | 11 | 3 | 0 | ███████████████████ |
| Dec 2025 | 0 | 0 | 0 | 0 | 0 |  |
| Jan 2026 | 3 | 3 | 0 | 0 | 0 | ███ |
| Feb 2026 | 9 | 0 | 8 | 0 | 0 | █████████ |
| Mar 2026 | 17 | 17 | 0 | 0 | 0 | ██████████████████ |
| Apr 2026 | 1 | 0 | 0 | 0 | 1 | █ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 3 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 23 Apr 2026 | Lawsuit | Nintendo fans in the US have filed a class action lawsuit against the Switch manufacturer. | [Nintendo under pressure: Switch players want their money back -…](https://www.gamingdeputy.com/nintendo-under-pressure-switch-players-want-their-money-back/) · gamingdeputy.com |
| 26 Mar 2026 | Announcement | This Thursday, Japanese company Nintendo would have decided to cut significantly the production of its Nintendo Switch 2 console after sales did not… | [Nintendo habrÃ­a decidido reducir en mÃ¡s de 30% la producciÃ³n de…](https://www.biobiochile.cl/noticias/ciencia-y-tecnologia/videojuegos/2026/03/26/nintendo-habria-decidido-reducir-en-mas-de-30-la-produccion-de-switch-2-segun-bloomberg.shtml) · biobiochile.cl |
| 25 Mar 2026 | Announcement | Nintendo reduces switch 2 production by a third. | [Nintendo drosselt Switch-2-Produktion drastisch \| Heute.at](https://www.heute.at/s/nintendo-drosselt-switch-2-produktion-drastisch-120174262) · heute.at |
| 25 Mar 2026 | Announcement | The company plans to make 4 million units of its flagship device this quarter, a third less than the 6 million it had originally planned to produce,… | [Nintendo cuts Switch 2 output by over 30% on weak holiday sales](https://www.japantimes.co.jp/business/2026/03/25/tech/nintendo-switch-2-output-cut/) · japantimes.co.jp |
| 25 Mar 2026 | Announcement | Nintendo Co is cutting back the production of Switch 2 after demand for the US$450 gaming console trailed the company’s expectations during the… | [Switch 2 stumbles on weak US demand](https://www.thestar.com.my/business/business-news/2026/03/25/switch-2-stumbleson-weak-us-demand) · thestar.com.my |
| 24 Mar 2026 | Announcement | Nintendo will reduce Switch 2 production by one third. ... with this the production of the console will go from 6 to 4 million. | [Nintendo reducirá la producción de Nintendo Switch 2](https://flipr.com.ar/nacionales/tecnologia/culturageek/nintendo-reducira-la-produccion-de-nintendo-switch-2/) · flipr.com.ar |
| 24 Mar 2026 | Announcement | The Japanese firm would have reduced the production expected for this quarter by around 30% after Christmas sales below what was expected in one of… | article unavailable |
| 24 Mar 2026 | Announcement | According to Bloomberg, sources told the outlet that Nintendo has cut its production down by 33% and is now aiming to produce 4 million Switch 2… | [Nintendo Switch 2 production has reportedly been cut by 33%…](https://www.techradar.com/gaming/nintendo-has-reportedly-cut-switch-2-production-significantly-due-to-weak-holiday-sales-and-now-aims-to-produce-4-million-units-instead-of-6-million-this-quarter) · techradar.com |
| 24 Mar 2026 | Announcement | Nintendo decided to reduce the production of Switch 2 after the island's sales were below expectations, especially in the United States. | [Nintendo reduz produção do Switch 2 após vendas perderem força](https://exame.com/tecnologia/nintendo-reduz-producao-do-switch-2-apos-vendas-perderem-forca/) · exame.com |
| 24 Mar 2026 | Announcement | Nintendo now expects to make 4 million Switch 2 units this quarter, down 33% on the 6 million it previously planned to manufacture. | article unavailable |
| 24 Mar 2026 | Announcement | Yesterday, reports suggested Nintendo plans to release a revised Switch 2 model in the EU with a replaceable battery. | article unavailable |
| 24 Mar 2026 | Announcement | Nintendo is planning to cut Switch 2 production by about 30% this fiscal quarter, from 6 million to 4 million. | [Rumor: Nintendo Reportedly Cutting Switch 2 Production By 30% Due To…](https://nintendosoup.com/rumor-nintendo-reportedly-cutting-switch-2-production-by-30-due-to-lower-than-expected-sales/) · nintendosoup.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company nintendo.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company nintendo.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company nintendo.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company nintendo.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/nintendo.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "nintendo.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Adani News](adani-news.md)
- [Tesla News](tesla-news.md)
- [Nvidia News](nvidia-news.md)
- [TCS News](tcs-news.md)
