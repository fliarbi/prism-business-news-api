# Stock Split: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “stock split” · 90,500/month India · 33,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [stock-split.json](../../examples/scenarios/stock-split.json).

**Question.** How many stock split events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `company_announcement` and the word “split” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 106 |
| Companies (with a domain) | 75 |
| Source articles | 106 |
| Busiest month | Dec 2025 (16 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 9.4% · 0.0% · 91% of 32 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 4 | █████ |
| Jun 2025 | 5 | ██████ |
| Jul 2025 | 5 | ██████ |
| Aug 2025 | 12 | ███████████████ |
| Sep 2025 | 10 | ████████████ |
| Oct 2025 | 7 | █████████ |
| Nov 2025 | 4 | █████ |
| Dec 2025 | 16 | ████████████████████ |
| Jan 2026 | 10 | ████████████ |
| Feb 2026 | 11 | ██████████████ |
| Mar 2026 | 12 | ███████████████ |
| Apr 2026 | 10 | ████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 7 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | internationalpaper.com | Announcement | IP is progressing on its announced plan to split into two geographic regions, one in North America and one in EMEA. IP will retain a 20% ownership… | [​​​​​​​International Paper touts $200M in EMEA cuts ahead of…](https://www.packagingdive.com/news/international-paper-q1-2026-earnings-emea-split-cost-savings/818922/) · packagingdive.com |
| 23 Apr 2026 | directdigitalholdings.com | Announcement | Direct Digital Holdings, Inc. (Nasdaq: DRCT) ('Direct Digital Holdings' or the 'Company'), a leading advertising and marketing technology platform… | [Direct Digital Holdings Announces Reverse Stock Split](https://www.prnewswire.com/news-releases/direct-digital-holdings-announces-reverse-stock-split-302751255.html) · prnewswire.com |
| 22 Apr 2026 | cuebiopharma.com | Announcement | Cue Biopharma, Inc. (Nasdaq: CUE ), a clinical-stage biopharmaceutical company ... today announced that it will implement a 1-for-30 reverse stock… | [Cue Biopharma cuts share count to 3.3M as it seeks Nasdaq compliance](https://www.stocktitan.net/news/CUE/cue-biopharma-announces-1-for-30-reverse-stock-g0zdxxvtxub0.html) · stocktitan.net |
| 21 Apr 2026 | amararajaeandm.com | Announcement | In a significant strategic pivot, Amara Raja has revised its capacity allocation across the planned 16 GWh, moving from a largely mobility-focused… | [Amara Raja plans to begin bulk production of EV cells in 2027](https://economictimes.indiatimes.com/industry/renewables/amara-raja-plans-to-begin-bulk-production-of-ev-cells-in-2027/articleshow/130426634.cms) · economictimes.indiatimes.com |
| 17 Apr 2026 | zspace.com | Announcement | zSpace, Inc. (NASDAQ: ZSPC ) (“zSpace” or the “Company”), a leading provider of augmented and virtual reality (AR/VR) solutions for education and… | article unavailable |
| 16 Apr 2026 | larosaholdings.com | Announcement | La Rosa Holdings Corp. (NASDAQ: LRHC ) (“La Rosa” or the “Company”), a real estate and PropTech enterprise, today announced that it will effect a… | article unavailable |
| 15 Apr 2026 | bharatforge.com | Announcement | The company has secured new business orders worth US$ 120 million during FY2017, split into long-term export orders of US$ 80 million and domestic… | article unavailable |
| 14 Apr 2026 | wheelsup.com | Announcement | Wheels Up Experience Inc. (NYSE: UP ) ("Wheels Up" or the "Company") is announcing that effective immediately after the close of trading on The New… | article unavailable |
| 10 Apr 2026 | bren-energy.com | Announcement | today announced that a reverse share split of its issued and outstanding ordinary shares, no par value per share (the 'Ordinary Shares') at a ratio… | [Brenmiller will cut share count to 515,465 in 5-for-1 reverse split](https://www.stocktitan.net/news/BNRG/brenmiller-energy-ltd-announces-expected-implementation-of-5-for-1-bkkpfa71djw2.html) · stocktitan.net |
| 1 Apr 2026 | greenlane.eu | Announcement | "Greenlane Holdings, Inc. (“Greenlane” or the “Company”) (Nasdaq: GNLN ), ... announced that it will effect a reverse stock split of its outstanding… | article unavailable |
| 26 Mar 2026 | modular-medical.com | Announcement | Modular Medical, Inc. ("Modular Medical" or the "Company") (NASDAQ:MODD), an innovative insulin delivery technology company, today announced that it… | [Modular Medical slashes share count to keep Nasdaq listing](https://www.stocktitan.net/news/MODD/modular-medical-announces-1-for-30-reverse-stock-6kmojjlgbgtx.html) · stocktitan.net |
| 25 Mar 2026 | noodles.com | Announcement | In February, the company announced plans for a reverse stock split that would allow it to continue to trade on the Nasdaq after being warned of… | [Noodles & Company's store closures are boosting the restaurants that…](https://www.restaurantbusinessonline.com/operations/noodles-companys-store-closures-boosting-restaurants-remain) · restaurantbusinessonline.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type company_announcement --q split --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type company_announcement --q split --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type company_announcement --q split --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["company_announcement"], "q": "split", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["company_announcement"], "q": "split", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Layoffs](layoffs.md)
- [Lawsuit](lawsuit.md)
- [Bonus Issue](bonus-issue.md)
- [Class Action Lawsuit](class-action-lawsuit.md)
