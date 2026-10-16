# Proptech Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “proptech funding” · 20/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [proptech-funding.json](../../examples/scenarios/proptech-funding.json).

**Question.** How many proptech deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “proptech”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 149 |
| With a usable reported amount | 141 |
| Reported total (usable amounts) | $4.6B |
| Median reported round | $7.4M |
| Largest reported round | $1B |
| Busiest month | Jan 2026 (22 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 19 | 19 | $219.5M | $5M | █████████████████ |
| Jun 2025 | 7 | 6 | $98.1M | $10.8M | ██████ |
| Jul 2025 | 10 | 10 | $480.4M | $52.9M | █████████ |
| Aug 2025 | 9 | 8 | $31.3M | $2M | ████████ |
| Sep 2025 | 10 | 9 | $96.7M | $10.6M | █████████ |
| Oct 2025 | 10 | 10 | $114.3M | $7M | █████████ |
| Nov 2025 | 15 | 15 | $2.1B | $17M | ██████████████ |
| Dec 2025 | 14 | 12 | $113.7M | $3.4M | █████████████ |
| Jan 2026 | 22 | 22 | $353.6M | $9M | ████████████████████ |
| Feb 2026 | 19 | 16 | $606.6M | $15M | █████████████████ |
| Mar 2026 | 5 | 5 | $408.7M | $57.9M | █████ |
| Apr 2026 | 9 | 9 | $121.6M | $1.6M | ████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 17 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 14 Nov 2025 | La Rosa Holdings (larosaholdings.com) | equity purchase facility | $1B | — | USA | Press Release – New York, NY – November 13, 2025 – Sichenzia Ross Ference Carmel LLP announced that it represented La Rosa Holdings Corp… |
| 15 Nov 2025 | Entrata (entrata.com) | — | $507M | silver lake, others | USA | Within a year of him taking over its helm, Edmunds engineered a $507 million fundraise from private equity firm Silver Lake and others. |
| 4 Feb 2026 | Bedrock Robotics | — | $300M | capitalg, Nvidia’s venture arm, Valor Equity Partners’… | — | Proptech startup Bedrock Robotics has nailed down nearly $300M to accelerate the construction process, especially for data centers. |
| 27 Mar 2026 | Sunday PropTech | Financing | $286M | Citigroup, access point | USA | Sunday PropTech has secured $286 million in financing to support the acquisition and repositioning of a 38-hotel U.S. hospitality… |
| 11 Jul 2025 | Bilt (biltapp.com) | new primary funding | $250M | general catalyst, gid, united wholesale mortgage | — | Bilt has secured $250m in new primary funding, valuing it at $10.75bn. |
| 11 Mar 2026 | Gropyus (gropyus.com) | venture capital | $108M | vonovia, semapa next | Austria | Business chancellor Schönherr advised Gropyus, a Vienna-based PropTech, on its recent financing round of 100 million euros. |
| 30 Jan 2026 | Propy (propy.com) | credit facility | $100M | metropolitan partners group | USA | Propy has obtained a $100 million credit facility from Metropolitan Partners Group to fuel its AI driven acquisition strategy in the title… |
| 27 Feb 2026 | Dwelly (dwelly.ca) | — | $87.6M | — | United Kingdom | Dwelly has raised £69m in new funding as part of its ambitious plans to acquire more letting agencies and expand its AI-powered operating… |
| 11 Jun 2025 | Nawy (nawy.com) | — | $75M | — | Egypt | Leading the way was Egypt’s Nawy, which closed a $75 million round ($52 million equity + $23 million debt), marking Africa’s biggest-ever… |
| 22 Jan 2026 | Cubby Storage (cubbystorage.com) | Series A | $63M | Goldman Sachs Alternatives | — | Cubby Storage – $63M Series A PROPTECH Cubby Storage, a property management platform for storage operators, has raised $63M in Series A… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 22 Apr 2026 | Breezemove (breezemove.co.uk) | seed | $952.5k | gc angels | UK | GC Angels has made a “six-figure” investment into Breezemove as part of their £750,000 seed round. |
| 21 Apr 2026 | Habi (habi.co) | credit facility | $60M | — | Mexico | The financing follows a $60M credit facility in Mexico, bringing its total credit lines to $100M. |
| 21 Apr 2026 | Habi (habi.co) | credit line | $40M | BBVA Spark | Colombia | Colombian proptech Habi secured a $40M credit line from BBVA Spark. |
| 16 Apr 2026 | Openmoove | equity | $889k | development bank of wales, haatch, Welsh angel investors | UK | Cardiff-based proptech firm Openmoove has secured £700,000 in equity funding to expand its platform, grow its team and accelerate its… |
| 15 Apr 2026 | Helium (helium.com) | — | $600k | Kunal Shah | India | Proptech startup Helium raise Rs 5 crore from Kunal Shah, others. |
| 15 Apr 2026 | Houseeazy (houseeazy.com) | Series B | $16M | accel | India | For instance, HouseEazy raised $16 million (₹148 crore) in a Series B round led by Accel in October 2025. |
| 3 Apr 2026 | Proho | pre‑seed | $1M | Bharath Vivek Chandhok | India | AI‑powered property platform Proho raised $1 million in pre‑seed funding, with participation from investors including Bharath Vivek… |
| 2 Apr 2026 | Jozo | Seed | $2.2M | Sheikh Hamad Bin Saedan Real Estate Co. | Saudi Arabia | Saudi proptech startup Jozo has raised $2.2 million in a seed round led by real estate giant, Sheikh Hamad Bin Saedan Real Estate Co. to… |
| 27 Mar 2026 | Sunday PropTech | Financing | $286M | Citigroup, access point | USA | Sunday PropTech has secured $286 million in financing to support the acquisition and repositioning of a 38-hotel U.S. hospitality… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector proptech --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector proptech --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector proptech --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "proptech", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "proptech", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Insurtech Funding](insurtech-funding.md)
- [Agritech Funding](agritech-funding.md)
- [Creator Economy Funding](creator-economy-funding.md)
- [Femtech Funding](femtech-funding.md)
