# Climate Tech Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “climate tech funding” · 30/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [climate-tech-funding.json](../../examples/scenarios/climate-tech-funding.json).

**Question.** How many climate tech deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “climate”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 170 |
| With a usable reported amount | 152 |
| Reported total (usable amounts) | $5.1B |
| Median reported round | $5.7M |
| Largest reported round | $1.2B |
| Busiest month | Jun 2025 (26 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 9 | 8 | $53.9M | $4.2M | ███████ |
| Jun 2025 | 26 | 20 | $359.8M | $10.8M | ████████████████████ |
| Jul 2025 | 14 | 11 | $115.6M | $8M | ███████████ |
| Aug 2025 | 5 | 5 | $29.8M | $4.8M | ████ |
| Sep 2025 | 17 | 15 | $171.5M | $3.9M | █████████████ |
| Oct 2025 | 21 | 21 | $580.3M | $1.6M | ████████████████ |
| Nov 2025 | 15 | 15 | $670M | $1.8M | ████████████ |
| Dec 2025 | 6 | 5 | $66.5M | $10M | █████ |
| Jan 2026 | 14 | 12 | $1.4B | $20.3M | ███████████ |
| Feb 2026 | 11 | 11 | $136.1M | $12.7M | ████████ |
| Mar 2026 | 18 | 16 | $1.4B | $34.8M | ██████████████ |
| Apr 2026 | 14 | 13 | $115.7M | $5.4M | ███████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 14 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 28 Jan 2026 | Cloover (cloover.co) | Series A equity financing | $1.2B | — | Germany | Berlin-based climate fintech company Cloover has secured over $1.2 billion in funding commitments, comprising equity and debt facilities… |
| 16 Mar 2026 | Climate Fund Managers (climatefundmanagers.com) | Second fund | $1B | — | — | Notable alumni include Climate Fund Managers, which recently closed its second fund at more than $1 billion for climate adaptation… |
| 16 Oct 2025 | Bees & Bears | Debt | $540M | listed European bank | Germany | This comes shortly after securing a landmark €500 million financing framework from a listed European bank, a first for a European climate… |
| 26 Nov 2025 | Just Climate (justclimate.com) | raise | $375M | calstrs, Microsoft’s Climate Innovation Fund, achmea… | — | Just Climate raises $375 million from global institutional investors to scale natural climate solutions across land, water and waste… |
| 5 Nov 2025 | Novastar Ventures (novastarventures.com) | equity investment | $200M | green climate fund | — | The Green Climate Fund approved a USD 200M investment in Novastar Ventures, with USD 50M dedicated to Egypt’s agriculture-focused… |
| 25 Jun 2025 | Paul Tech (paul.tech) | credit facility | $129.6M | meag | Germany | PAUL Tech AG announced a significant financial boost with a EUR 120,000,000 credit facility agreement with MEAG, the asset manager of… |
| 25 Sep 2025 | KawiSafi Fund II | — | $90M | — | Africa | KawiSafi Fund II Secures $90 Million to Accelerate Climate Solutions Across Africa |
| 2 Jan 2026 | Arya.ag | Equity | $87M | gef capital partners | India | today announced that it has raised Rs 725 crore (approximately USD 80.58 million) in equity from GEF Capital Partners. |
| 20 Mar 2026 | Sistema.bio | First tranche | $53M | BNP Paribas Asset Management Alts, British International… | Kenya | The round brings in backing from BNP Paribas Asset Management Alts, British International Investment, and the Shell Foundation, and it… |
| 16 Mar 2026 | Adaptation Asia | — | $50M | — | Philippines | Adaptation Asia and Planetary X’s Panra Fund in the Philippines, for example, is looking to raise $50 million to provide revenue-based… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Prithu | Seed | $12M | Transition Vc | India | Prithu Raises ₹10 Cr Seed Round Prithu, a climate tech startup, raised INR 10 crore in a seed round led by Transition VC. |
| 29 Apr 2026 | Prithu | Seed | $1.2M | Transition Vc | India | Prithu Raises ₹10 Cr Seed Round |
| 24 Apr 2026 | VREY | seed | $3.3M | Rubio Impact Ventures, htgf, kopa ventures | Germany | The Berlin Climate Tech Start-up VREY (RE Joule GmbH) has successfully completed a seed financing round in the height of 3.3 million ¬.… |
| 13 Apr 2026 | Airmo (airmo.io) | Seed | $5.4M | ananda impact ventures, unconventional ventures, kopa… | Germany, Luxembourg | Airmo, a Munich, Germany- and Luxembourg-based climate-tech and space tech startup, raised €5M in Seed funding. |
| 10 Apr 2026 | Satellites On Fire (satellitesonfire.com) | — | $2.7M | dalus capital, draper associates, vitamin c | Argentina | Satellites On Fire raised $2.7 million in a round led by Dalus Capital, with participation from Draper Associates, Vitamin C, Draper… |
| 10 Apr 2026 | Persistent’s Africa Climate Venture Builder Fund | blended finance | $7M | soros economic development fund | — | The Soros Economic Development Fund (SEDF), the impact investment arm of the Open Society Foundations, has committed $7m to Persistent’s… |
| 9 Apr 2026 | Powerlabs (powerlabs.io) | pre-seed | — | breega, Catalyst Fund, Mercy Corps Ventures | Nigeria | PowerLabs, a Nigerian energy and climate-tech startup, has raised a pre-seed round led by Breega, with participation from Catalyst Fund,… |
| 9 Apr 2026 | Sora Fuel (sorafuel.com) | seed | $14.6M | spero ventures, inspired capital, Engine Ventures | USA | Sora Fuel, a Boston, Mass.-based climate technology company, raised $14.6 million in funding. Spero Ventures and Inspired Capital led the… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector climate --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector climate --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector climate --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "climate", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "climate", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Mobility Funding](mobility-funding.md)
- [Bridge Round Funding](bridge-round-funding.md)
- [Growth Stage Funding](growth-stage-funding.md)
- [D2C Funding](d2c-funding.md)
