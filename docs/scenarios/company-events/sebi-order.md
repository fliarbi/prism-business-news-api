# SEBI Order: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “sebi order” · 1,300/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [sebi-order.json](../../examples/scenarios/sebi-order.json).

**Question.** How many sebi order events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `regulatory` and the word “SEBI” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 202 |
| Companies (with a domain) | 142 |
| Source articles | 177 |
| Busiest month | Sep 2025 (41 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 47% · 3.5% · 50% of 58 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 17 | ████████ |
| Jun 2025 | 8 | ████ |
| Jul 2025 | 15 | ███████ |
| Aug 2025 | 22 | ███████████ |
| Sep 2025 | 41 | ████████████████████ |
| Oct 2025 | 25 | ████████████ |
| Nov 2025 | 12 | ██████ |
| Dec 2025 | 12 | ██████ |
| Jan 2026 | 13 | ██████ |
| Feb 2026 | 11 | █████ |
| Mar 2026 | 12 | ██████ |
| Apr 2026 | 14 | ███████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 6 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 28 Apr 2026 | cupidltd.in | Regulatory | Cupid Limited has been issued an administrative warning letter by the Securities and Exchange Board of India (SEBI) dated April 23, 2026. | [Cupid receives administrative warning from SEBI for non-compliance -…](https://www.businessupturn.com/business/cupid-receives-administrative-warning-from-sebi-for-non-compliance/) · businessupturn.com |
| 25 Apr 2026 | manappuram.com | Regulatory | Manappuram Finance's Chairman and Managing Director, V.P. Nandakumar, has received an administrative warning from the Securities and Exchange Board… | article unavailable |
| 20 Apr 2026 | mcxindia.com | Regulatory | The Multi Commodity Exchange of India Limited (MCX) on Monday said it has received approval from market regulator the Securities and Exchange Board… | article unavailable |
| 20 Apr 2026 | mcxindia.com | Regulatory | Multi Commodity Exchange of India Ltd (MCX) on Monday said it has received approval from the Securities and Exchange Board of India (Sebi) to invest… | article unavailable |
| 16 Apr 2026 | sunpharma.com | Regulatory | Sun Pharma's April 10 regulatory filing to BSE and NSE, issued by Company Secretary Anoop Deshpande, stated explicitly that the information… | [Sun Pharma Organon acquisition bid 2026: Bloomberg report, $12…](https://www.businessupturn.com/business/sun-pharma-places-aggressive-bid-for-organon-contradicting-companys-own-earlier-clarification-of-speculative-reports/) · businessupturn.com |
| 15 Apr 2026 | stringbio.com | Regulatory | In a separate development last month, the company informed exchanges about violations of its Code of Conduct under Sebi’s Insider Trading… | [Upcoming stock split: Check record date, ratio, pre and post split…](https://www.businesstoday.in/markets/stocks/story/upcoming-stock-split-check-record-date-ratio-pre-and-post-split-face-value-525741-2026-04-15) · businesstoday.in |
| 15 Apr 2026 | allcargoterminals.com | Regulatory | Allcargo Terminals Limited has submitted Compliance certificate under Reg 74(5) of SEBI (DP) Regulation 2018 for the quarter ended March 2026 | [Allcargo Terminals News - Allcargo Terminals Announcement, Latest…](https://economictimes.indiatimes.com/allcargo-terminals-ltd/stocksupdate/companyid-2116783.cms) · economictimes.indiatimes.com |
| 10 Apr 2026 | poonawallafincorp.com | Regulatory | The floor price of ₹390.26 per share has been determined in line with the pricing formula prescribed under SEBI ICDR Regulations. | [Poonawalla Fincorp launches QIP at a floor price of ₹390.26 per…](https://www.livemint.com/market/stock-market-news/poonawalla-fincorp-launches-qip-at-a-floor-price-of-rs-390-26-per-share-down-2-6-from-previous-close-11775793977004.html) · livemint.com |
| 8 Apr 2026 | gmdcltd.com | Regulatory | The Securities and Exchange Board of India (SEBI) has issued an Administrative Warning to Gujarat Mineral Development Corporation (GMDC) following… | [Gujarat Mineral Development Corporation receives SEBI administrative…](https://www.businessupturn.com/business/gujarat-mineral-development-corporation-receives-sebi-administrative-warning/) · businessupturn.com |
| 8 Apr 2026 | ashianahousing.com | Regulatory | Ashiana Housing has submitted a regulatory intimation to the National Stock Exchange of India and BSE confirming that it does not fall under the… | article unavailable |
| 7 Apr 2026 | shreecement.com | Regulatory | Shree Cement has submitted a confirmation certificate from its Registrar and Share Transfer Agent (RTA), MUFG Intime India Private Limited, pursuant… | article unavailable |
| 6 Apr 2026 | reliancerent.com | Regulatory | After the deal was eventually announced and confirmed to be true, Sebi issued a show-cause notice to Reliance in December 2021, alleging violation… | [Reliance, stock exchange silence on Trump's claims test limits of…](https://www.livemint.com/companies/news/reliance-stock-exchange-silence-on-trumps-claims-test-limits-of-sebis-disclosure-norms-11775379759499.html) · livemint.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type regulatory --q SEBI --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type regulatory --q SEBI --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type regulatory --q SEBI --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["regulatory"], "q": "SEBI", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["regulatory"], "q": "SEBI", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [AI Partnership](ai-partnership.md)
- [Bank Results](bank-results.md)
- [Capital Infusion](capital-infusion.md)
- [Asset Sale](asset-sale.md)
