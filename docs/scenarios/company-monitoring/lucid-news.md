# Lucid News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “lucid news” · 90/month India · 8,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [lucid-news.json](../../examples/scenarios/lucid-news.json).

**Question.** What has the news reported about Lucid in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `lucidmotors.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `lucidmotors.com` |
| Headlines, Jan – Apr 2026 (estimate) | 17 |
| Events, May 2025 – Apr 2026 | 35 |
| Most frequent event types | Key people (18), Announcement (6), Asset acquisition (3) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 29% · 0.0% · 71% of 17 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 6 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 19 Apr 2026 | [15 Reasons Why Motorcycle Tyre Review 2024 Worth Knowing](https://www.thedetroitbureau.com/www-news/15-reasons-why-motorcycle-tyre-review-2024-worth-knowing-dhxahakz8ld5) | thedetroitbureau.com | 6 | positive | Announcement |
| 16 Apr 2026 | [Lucid: Neuer CEO und frisches Kapital - Drehmoment](https://drehmoment.net/lucid-neuer-ceo-und-frisches-kapital/) | drehmoment.net | 6 | positive | Key people |
| 15 Apr 2026 | [Who Is Lucid's New CEO? Silvio Napoli Leaves a Swiss Elevator Company to Lead the American EV Maker](http://www.caranddriver.com/news/a71027527/silvio-napoli-named-lucid-ceo/) | caranddriver.com | 6 | positive | Key people |
| 14 Apr 2026 | [Lucid Motors Has A New CEO And A Bunch More Funding](https://www.insideevs.com/news/792958/lucid-new-ceo-named-funding/) | insideevs.com | 6 | positive | Key people |
| 23 Mar 2026 | [SEC drops four-year long investigation into EV startup Faraday Future](https://americanbazaaronline.com/2026/03/23/sec-drops-four-year-long-investigation-into-ev-startup-faraday-future-477403/) | americanbazaaronline.com | 8 | negative | Regulatory |
| 22 Mar 2026 | [Exclusive: The SEC drops its four-year-old investigation into EV startup Faraday Future](https://techcrunch.com/2026/03/22/the-sec-drops-its-four-year-old-investigation-into-ev-startup-faraday-future/) | techcrunch.com | 8 | negative | Regulatory |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Key people | 18 |
| Announcement | 6 |
| Asset acquisition | 3 |
| Regulatory | 2 |
| Earnings | 1 |
| M&A | 1 |
| Contracts | 1 |
| Lawsuit | 1 |
| Job creation | 1 |
| Layoffs | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Key people | Announcement | Asset acquisition | Regulatory |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 8 | 4 | 2 | 1 | 0 | ████████████████ |
| Jun 2025 | 0 | 0 | 0 | 0 | 0 |  |
| Jul 2025 | 1 | 0 | 0 | 0 | 0 | ██ |
| Aug 2025 | 3 | 0 | 0 | 2 | 0 | ██████ |
| Sep 2025 | 0 | 0 | 0 | 0 | 0 |  |
| Oct 2025 | 0 | 0 | 0 | 0 | 0 |  |
| Nov 2025 | 3 | 2 | 0 | 0 | 0 | ██████ |
| Dec 2025 | 3 | 0 | 2 | 0 | 0 | ██████ |
| Jan 2026 | 1 | 0 | 1 | 0 | 0 | ██ |
| Feb 2026 | 4 | 3 | 0 | 0 | 0 | ████████ |
| Mar 2026 | 2 | 0 | 0 | 0 | 2 | ████ |
| Apr 2026 | 10 | 9 | 1 | 0 | 0 | ████████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 5 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Key people | Winterhoff, who had served as interim CEO since February 2025, transitioned into the role of Chief Operating Officer once Napoli took over. | article unavailable |
| 19 Apr 2026 | Announcement | Lucid Motors is working hard to ramp up production and expand its market reach. | [15 Reasons Why Motorcycle Tyre Review 2024 Worth Knowing](https://www.thedetroitbureau.com/www-news/15-reasons-why-motorcycle-tyre-review-2024-worth-knowing-dhxahakz8ld5) · thedetroitbureau.com |
| 16 Apr 2026 | Key people | Marc Winterhoff hands over after 14 months. | [Lucid: Neuer CEO und frisches Kapital - Drehmoment](https://drehmoment.net/lucid-neuer-ceo-und-frisches-kapital/) · drehmoment.net |
| 15 Apr 2026 | Key people | Marc Winteroff, Lucid's current interim chief executive, will return to his former job as the brand's COO. | [Who Is Lucid's New CEO? Silvio Napoli Leaves a Swiss Elevator…](http://www.caranddriver.com/news/a71027527/silvio-napoli-named-lucid-ceo/) · caranddriver.com |
| 15 Apr 2026 | Key people | The news also means that Marc Winteroff, Lucid's current interim chief executive, will return to his former job as the brand's COO. | [Who Is Lucid's New CEO? Silvio Napoli Leaves a Swiss Elevator…](https://www.caranddriver.com/news/a71027527/silvio-napoli-named-lucid-ceo/) · caranddriver.com |
| 15 Apr 2026 | Key people | The newly appointed chief executive, who spent nearly 31 years at Switzerland's Schindler Group, will begin as Executive Director based in… | article unavailable |
| 15 Apr 2026 | Key people | Napoli brings extensive global leadership experience, having previously served as CEO of Schindler Group, where he led large-scale operations and… | article unavailable |
| 14 Apr 2026 | Key people | Napoli will replace Lucid's interim CEO Marc Winterhoff, who will return to his role as COO. | article unavailable |
| 14 Apr 2026 | Key people | Lucid Motors has finally found a new CEO in long-time industrial executive, Silvio Napoli, marking the end of a more than year-long search following… | article unavailable |
| 23 Mar 2026 | Regulatory | The SEC had earlier dismissed an investigation into Lucid Motors in 2023 and ended a probe into Fisker in 2025. | [SEC drops four-year long investigation into EV startup Faraday Future](https://americanbazaaronline.com/2026/03/23/sec-drops-four-year-long-investigation-into-ev-startup-faraday-future-477403/) · americanbazaaronline.com |
| 22 Mar 2026 | Regulatory | It dismissed an investigation into Lucid Motors in 2023 | [Exclusive: The SEC drops its four-year-old investigation into EV…](https://techcrunch.com/2026/03/22/the-sec-drops-its-four-year-old-investigation-into-ev-startup-faraday-future/) · techcrunch.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company lucidmotors.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company lucidmotors.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company lucidmotors.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company lucidmotors.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/lucidmotors.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "lucidmotors.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Ongc News](ongc-news.md)
- [Toyota News](toyota-news.md)
- [Uber News](uber-news.md)
- [IBM News](ibm-news.md)
