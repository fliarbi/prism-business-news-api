# B2b Marketplace Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “b2b marketplace funding” · volume below estimate threshold  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [b2b-marketplace-funding.json](../../examples/scenarios/b2b-marketplace-funding.json).

**Question.** How many b2b marketplace deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “marketplace”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 136 |
| With a usable reported amount | 118 |
| Reported total (usable amounts) | $7.7B |
| Median reported round | $8.3M |
| Largest reported round | $1B |
| Amounts left out as implausible or unconverted | 1 |
| Busiest month | Oct 2025 (20 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 7 | 6 | $30.2M | $3.2M | ███████ |
| Jun 2025 | 10 | 7 | $746.7M | $30M | ██████████ |
| Jul 2025 | 10 | 9 | $452.1M | $9M | ██████████ |
| Aug 2025 | 12 | 9 | $159.8M | $2.7M | ████████████ |
| Sep 2025 | 7 | 7 | $927.6M | $7M | ███████ |
| Oct 2025 | 20 | 18 | $1.3B | $6.5M | ████████████████████ |
| Nov 2025 | 13 | 13 | $155M | $3.2M | █████████████ |
| Dec 2025 | 7 | 7 | $200.3M | $8.2M | ███████ |
| Jan 2026 | 5 | 5 | $192.9M | $21.3M | █████ |
| Feb 2026 | 11 | 11 | $443.1M | $18.4M | ███████████ |
| Mar 2026 | 19 | 13 | $1.5B | $4.8M | ███████████████████ |
| Apr 2026 | 15 | 13 | $1.7B | $7.7M | ███████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 12 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 17 Mar 2026 | Upstart (upstart.com) | forward-flow commitment | $1B | Eltura Capital Management, aperture investors | — | Artificial intelligence (AI) lending marketplace Upstart has secured a $1bn (£0.74bn) forward-flow commitment with alternative asset… |
| 28 Apr 2026 | Vinted (vinted.com) | secondary funding | $950.4M ⚠ check sentence | — | Lithuania | Following an investment round of 880 million euros, the secondhand platform Vinted is now valued at 8 billion euros. |
| 22 Sep 2025 | Stubhub (stubhub.com) | IPO | $800M | — | USA | StubHub raised $800 million via its entrance onto the New York Stock Exchange. |
| 8 Apr 2026 | Carsome (carsome.my) | — | $600M | — | Malaysia | Carsome, the pioneering used car e-marketplace, leads with over $600 million raised, revolutionizing automotive sales since 2015. |
| 19 Oct 2025 | Meesho (meesho.com) | equity | $510M | elevation capital, peak xv partners, Highway Series 1 | India | Bengaluru-based online marketplace Meesho has filed its updated draft red herring prospectus (UDRHP) with the SEBI to raise up to ₹4,250… |
| 24 Jun 2025 | Moglix (moglix.com) | — | $370M ⚠ check sentence | tiger global, accel, alpha wave global | India | Moglix has raised over $370 million to date. |
| 27 Oct 2025 | Mercor (mercor.com) | Series C | $350M ⚠ check sentence | felicis ventures, benchmark, general catalyst | USA | Mercor, which connects AI labs with domain experts for training their foundational AI models, has raised $350 million at a $10 billion… |
| 18 Feb 2026 | Kavak (kavak.com) | Series E | $300M | Andreessen Horowitz, wcm investment management, Foxhaven… | Mexico | Kavak raises $300M in Series E funding led by Andreessen Horowitz to expand its used car platform |
| 24 Mar 2026 | Whop (whop.com) | Venture | $273M | Tether Ventures | USA |  |
| 29 Oct 2025 | Whatnot (whatnot.com) | Series F | $225M | dst global, capitalg, sequoia capital | USA | Whatnot, one of the live shopping platforms across the U.S., UK, and Europe, has landed $225 million in Series F funding. The round was… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Udora | — | $9.9M | — | UAE | The marketplace specializing in gifts Flowwow has closed an investment round of 9.2 million euros with which a new stage begins under a… |
| 29 Apr 2026 | Sprect (sprect.com) | — | $240k | Subhkam Ventures | India | Sprect (Super Connect) has raised Rs. 2 crore in funding from Subhkam Ventures (I) Private Limited, a registered NBFC firm that invests… |
| 28 Apr 2026 | Vinted (vinted.com) | Secondary transaction | — | eqt, schroders capital, Teachers’ Venture Growth (TVG) | — | The transaction was led by EQT, Schroders Capital, and Teachers’ Venture Growth (TVG), Ontario Teachers’ Pension Plan’s late-stage venture… |
| 28 Apr 2026 | Hyugalife (hyugalife.com) | Series A | $120M | ivycap ventures, first bridge fund | India | HyugaLife, founded by Sachin Parikh, Anvi Shah, and Neehar Modi, has raised ₹100 Cr in its Series A funding round, led by IvyCap Ventures.… |
| 28 Apr 2026 | Vinted (vinted.com) | secondary funding | $950.4M ⚠ check sentence | — | Lithuania | Following an investment round of 880 million euros, the secondhand platform Vinted is now valued at 8 billion euros. |
| 15 Apr 2026 | SparesHub.com | Second round | $240k | Anthill Scale Ventures, esvee technologies, Chennai Angels | India | Online autoparts marketplace SparesHub.com has raised Rs 2 crore from Singapore-based Anthill Scale Ventures, US-based Esvee Technologies,… |
| 15 Apr 2026 | CredR (Incredible Technologies Private) | — | $5.8M | Yamaha Motors, omidyar network india, eight roads ventures | India | Bangalore-based CredR (Incredible Technologies Private) used two-wheeler platform has raised Rs 48.1 crore ($ 6.5 million) in its latest… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector marketplace --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector marketplace --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector marketplace --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "marketplace", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "marketplace", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Logistics Startup Funding](logistics-startup-funding.md)
- [Quick Commerce Funding](quick-commerce-funding.md)
- [Battery Startup Funding](battery-startup-funding.md)
- [Construction Tech Funding](construction-tech-funding.md)
