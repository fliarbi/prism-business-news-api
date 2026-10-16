# Agritech Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “agritech funding” · 20/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [agritech-funding.json](../../examples/scenarios/agritech-funding.json).

**Question.** How many agritech deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “agritech”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 88 |
| With a usable reported amount | 78 |
| Reported total (usable amounts) | $626.5M |
| Median reported round | $4.6M |
| Largest reported round | $87M |
| Amounts left out as implausible or unconverted | 1 |
| Busiest month | Sep 2025 (11 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 7 | 5 | $16.5M | $3M | █████████████ |
| Jun 2025 | 9 | 8 | $47.5M | $2.4M | ████████████████ |
| Jul 2025 | 5 | 4 | $19.2M | $4M | █████████ |
| Aug 2025 | 6 | 6 | $57.9M | $9.1M | ███████████ |
| Sep 2025 | 11 | 9 | $64.6M | $4.6M | ████████████████████ |
| Oct 2025 | 3 | 3 | $11.5M | $2M | █████ |
| Nov 2025 | 11 | 9 | $91M | $9.6M | ████████████████████ |
| Dec 2025 | 7 | 6 | $57.6M | $9.2M | █████████████ |
| Jan 2026 | 6 | 6 | $104.8M | $5M | ███████████ |
| Feb 2026 | 7 | 6 | $64.3M | $1.4M | █████████████ |
| Mar 2026 | 7 | 7 | $68.1M | $7.5M | █████████████ |
| Apr 2026 | 9 | 9 | $35.3M | $2.7M | ████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 10 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 2 Jan 2026 | Arya.ag | Series D | $87M | gef capital partners | India | New Delhi-based agritech firm Arya.ag has raised Rs 725 crore (around $80.3 million) in its Series D round from GEF Capital Partners. |
| 4 Feb 2026 | Pure Harvest Smart Farms (pureharvest.ae) | growth funding | $50M | SHUAA Capital | UAE | UAE-based agritech startup, Pure Harvest Smart Farms, has secured $50 million in growth funding through a Sharia-compliant finance… |
| 22 Sep 2025 | Nofence (nofence.no) | — | $35M | — | — | Nofence : A virtual fencing company for livestock management raised $35 million. |
| 20 Nov 2025 | Agrostar (agrostar.in) | — | $30M | — | India | AgroStar secured $30 million to accelerate digital agriculture adoption across India. |
| 15 Mar 2026 | Waycool (waycool.in) | — | $22.7M | — | — | WayCool raised $22.7 million. |
| 9 Dec 2025 | Nextprotein (nextprotein.co) | — | $21M | — | Tunisia | nextProtein, specializing in sustainable agritech and the production of animal protein from insects, secured $21 million. |
| 29 Aug 2025 | Maalexi (maalexi.com) | Debt | $20M | amwal capital partners | UAE | This time, Maalexi has secured a shariah-compliant credit facility of up to $20 million (around Rs 176 crore) from Amwal Capital Partners,… |
| 30 Jun 2025 | Eggoz Nutrition (eggoz.in) | Series C | $20M | omnivore, NABVENTURES, Avaana Capital | India | Brand offering farm-fresh eggs with a tech-integrated supply chain, Eggoz Nutrition raised $20 million in its Series C round. |
| 28 Nov 2025 | Aerobotics (aerobotics.com) | — | $17M | naspers | South Africa | In 2020, the Cape Town-founded company famously raised R100m from Naspers in a $17m (R253m at the time) funding around. |
| 15 Apr 2026 | Agriodor (agriodor.com) | Series A | $16.2M | Environmental and Solidarity Revolution Fund, région sud… | France | Agriodor, a Rennes-based AgriTech startup using natural scents to protect crops, has raised €15 million in Series A funding to accelerate… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 17 Apr 2026 | Culta (culta.io) | Pre-Series A | $4.5M | archetype ventures, UntroD Capital | Japan | Japan-based agritech startup Culta secured $4.5 million (700 million yen) in a Pre-Series A round co-led by Archetype Ventures and UntroD… |
| 15 Apr 2026 | Agriodor (agriodor.com) | Series A | $16.2M | Environmental and Solidarity Revolution Fund, région sud… | France | Agriodor, a Rennes-based AgriTech startup using natural scents to protect crops, has raised €15 million in Series A funding to accelerate… |
| 14 Apr 2026 | Culta (culta.io) | pre-Series A | $4.7M | archetype ventures, UntroD Capital, nissay capital | Japan | With the fresh capital, Culta plans to scale operations and accelerate entry into markets in Southeast Asia and Australia. |
| 8 Apr 2026 | Kilimo Fresh (kilimofresh.co.tz) | pre-seed | $200k ⚠ check sentence | madica | Tanzania | Madica, a pre‑seed investment programme focused on African startups, has added three new companies to its portfolio, committing up to… |
| 6 Apr 2026 | Cropcoin | pre-Series A | $1.3M | — | India | Emerging startups Agritech startup Cropcoin raised $1.29 million in a pre-Series A round. |
| 4 Apr 2026 | Cropcoin | Pre-Series A | $1.3M | unicorn india ventures, Climate Angels | — |  |
| 4 Apr 2026 | Aquapulse (aquapulse.vn) | Series A | $2.7M | NABVENTURES | — |  |
| 3 Apr 2026 | Cropcoin Technologies | pre-Series A | $1.4M | unicorn india ventures, Climate Angels | India | AgriTech startup Cropcoin Technologies raised INR 12 crore ($1.27 million) in pre-Series A funding led by Unicorn India Ventures, with… |
| 2 Apr 2026 | Aquapulse (aquapulse.vn) | Series A | $3M | NABVENTURES | India | Aquaculture-focused agritech startup Aquapulse has netted ₹25 Cr (about $2.7 Mn) in its ongoing Series A round led by NABVENTURES via its… |
| 30 Mar 2026 | Cropcoin Technologies | Pre-Series A | $14.4M | unicorn india ventures, Climate Angels | India | Cropcoin Technologies, a Mumbai, India-based agritech startup, raised RS 12 Crore ($1.27M) in Pre-Series A funding. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector agritech --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector agritech --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector agritech --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "agritech", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "agritech", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [D2C Funding](d2c-funding.md)
- [Insurtech Funding](insurtech-funding.md)
- [Proptech Funding](proptech-funding.md)
- [Creator Economy Funding](creator-economy-funding.md)
