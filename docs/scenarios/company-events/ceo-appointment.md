# CEO Appointment: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “ceo appointment” · 110/month India · 1,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [ceo-appointment.json](../../examples/scenarios/ceo-appointment.json).

**Question.** How many ceo appointment events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `key_people` and the word “CEO” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 9,852 |
| Companies (with a domain) | 5,484 |
| Source articles | 9,261 |
| Busiest month | Feb 2026 (1,018 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 8.2% · 2.9% · 89% of 4,567 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 682 | █████████████ |
| Jun 2025 | 662 | █████████████ |
| Jul 2025 | 813 | ████████████████ |
| Aug 2025 | 729 | ██████████████ |
| Sep 2025 | 902 | ██████████████████ |
| Oct 2025 | 756 | ███████████████ |
| Nov 2025 | 610 | ████████████ |
| Dec 2025 | 765 | ███████████████ |
| Jan 2026 | 1,013 | ████████████████████ |
| Feb 2026 | 1,018 | ████████████████████ |
| Mar 2026 | 888 | █████████████████ |
| Apr 2026 | 1,014 | ████████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 8 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | contentbureau.com | Key people | Toups assumed the role of global chief executive this January, replacing Heather Kernahan, who left the agency in May after nine years in the… | article unavailable |
| 30 Apr 2026 | hotwire.com | Key people | Macdonald takes over for Heather Craft, following her departure from Hotwire as its North American CEO in December 2025. | [Hotwire names Americas president](https://www.prweek.com/article/1956690/hotwire-names-americas-president) · prweek.com |
| 30 Apr 2026 | contentbureau.com | Key people | Kernahan acquired agency The Content Bureau in July, taking over the 25-year-old firm as CEO. | [Hotwire names Americas president](https://www.prweek.com/article/1956690/hotwire-names-americas-president) · prweek.com |
| 30 Apr 2026 | colonialwilliamsburg.org | Key people | Cliff Fleet, president and CEO of the Colonial Williamsburg Foundation, announced his retirement after serving in the role since 2020. | article unavailable |
| 30 Apr 2026 | alvotech.com | Key people | I'm very happy to see Lisa Graver taking over the CEO role, thus joining my other wonderful colleagues in the executive team. | article unavailable |
| 30 Apr 2026 | alvotech.com | Key people | Lisa Graver taking over the CEO role | article unavailable |
| 30 Apr 2026 | unigel.com.br | Key people | Gabriel, son of the petrochemical company's founder, Henri Slezynger, previously held no position within the company and will assume the role of… | [Slezynger family takes over Unigel amid reorganization](https://valorinternational.globo.com/business/news/2026/04/30/slezynger-family-takes-over-unigel-amid-reorganization.ghtml) · valorinternational.globo.com |
| 30 Apr 2026 | oxfordproperties.com | Key people | Queen is taking over the role from Randy Hoffman, a 20-year Oxford vet who served in the position for seven months before taking the role of CEO at… | article unavailable |
| 30 Apr 2026 | ihse.com | Key people | Brockhaus Technologies AG has realigned the management of its subsidiary IHSE, announcing Dr. Thomas Niessen as the new CEO, effective May 2026. | [Brockhaus Capital Management AG \|](https://www.webdisclosure.com/article/brockhaus-technologies-ag-announces-new-ceo-for-ihse-9XRujmcvv35) · webdisclosure.com |
| 30 Apr 2026 | lucidmotors.com | Key people | Winterhoff, who had served as interim CEO since February 2025, transitioned into the role of Chief Operating Officer once Napoli took over. | article unavailable |
| 30 Apr 2026 | sportmanitoba.ca | Key people | Sport Manitoba President & CEO JANET MCMAHON “is retiring” on May 1 (WINNIPEG FREE PRESS, 4/29). | [Sports Business Daily: Executive Transactions - April 30, 2026](https://www.sportsbusinessjournal.com/Articles/2026/04/30/sports-business-daily-executive-transactions-april-30-2026/) · sportsbusinessjournal.com |
| 30 Apr 2026 | hawkeyeinnovations.com | Key people | Hawk-Eye Innovations named Managing Dir BEN CROSSING CEO (Hawk-Eye Innovations). | [Sports Business Daily: Executive Transactions - April 30, 2026](https://www.sportsbusinessjournal.com/Articles/2026/04/30/sports-business-daily-executive-transactions-april-30-2026/) · sportsbusinessjournal.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type key_people --q CEO --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type key_people --q CEO --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type key_people --q CEO --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["key_people"], "q": "CEO", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["key_people"], "q": "CEO", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Capital Infusion](capital-infusion.md)
- [Asset Sale](asset-sale.md)
- [Battery Plant](battery-plant.md)
- [Bankruptcy News](bankruptcy-news.md)
