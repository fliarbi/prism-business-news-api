# Femtech Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “femtech funding” · 10/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [femtech-funding.json](../../examples/scenarios/femtech-funding.json).

**Question.** How many femtech deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “femtech”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 10 |
| With a usable reported amount | 8 |
| Reported total (usable amounts) | $78.3M |
| Median reported round | $3.2M |
| Largest reported round | $55M |
| Busiest month | Feb 2026 (4 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1 | 1 | $6.3M | $6.3M | █████ |
| Jun 2025 | 0 | 0 | — | — |  |
| Jul 2025 | 3 | 3 | $11.2M | $4M | ███████████████ |
| Aug 2025 | 0 | 0 | — | — |  |
| Sep 2025 | 0 | 0 | — | — |  |
| Oct 2025 | 0 | 0 | — | — |  |
| Nov 2025 | 2 | 2 | $56.7M | $28.4M | ██████████ |
| Dec 2025 | 0 | 0 | — | — |  |
| Jan 2026 | 0 | 0 | — | — |  |
| Feb 2026 | 4 | 2 | $4M | $2M | ████████████████████ |
| Mar 2026 | 0 | 0 | — | — |  |
| Apr 2026 | 0 | 0 | — | — |  |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 3 Nov 2025 | Natural Cycles (naturalcycles.com) | — | $55M | — | — | Natural Cycles, preparing a $55 million-plus round to scale its hormone‑free birth control solution. |
| 27 May 2025 | Hormona (hormona.io) | seed | $6.3M | Voima Ventures, SuperNode Global VC | UK | has raised £5m ($6.7m) in seed funding. |
| 11 Jul 2025 | Plenna (soyplenna.com) | Series A | $6M | Mazapil, dalus capital, new ventures | Mexico | Mexican femtech Plenna secured a $6 million Series A led by Mazapil, Dalus Capital, and New Ventures, with support from angel investor… |
| 3 Jul 2025 | Luma Fertility | Seed | $4M | Peak XV’s Surge, Ameera Shah, B2V Ventures | India | Luma Fertility, a Mumbai‑based femtech provider founded by Neha K. Motwani (founder of Fitternity), has raised $4 million in a seed round… |
| 4 Feb 2026 | Omooma (omooma.com) | — | $2.5M | e20 investment | UAE | Omooma has raised $2.5 million in funding from E20 Investment LTD. |
| 5 Nov 2025 | Solence (solence.care) | — | $1.7M | — | France | Solence in France raised €1.6 million to advance its AI-driven digital therapeutics for PCOS. |
| 4 Feb 2026 | Nabta Health (nabtahealth.com) | — | $1.5M | — | UAE | It raised $1.5 million in funding this year. |
| 17 Jul 2025 | Ovasave (ovasave.com) | pre-seed | $1.2M | PlusVC, annex investments, 25 Madison | UAE | Ovasave, a Hub71 FemTech startup focused on fertility and hormonal health, has successfully completed its pre-seed round, raising $1.2… |
| 25 Feb 2026 | Peripear | angel syndicate investment | — | british business bank, haatch, HERmesa | UK | FemTech business Peripear, creating a wearable device to prevent perineal tears during childbirth. |
| 16 Feb 2026 | Origin (originww.com) | Series B | — | sjf ventures, Blue Venture Fund, gratitude railroad | — | Origin, a femtech company based in Brentwood, announced in late January it raised a series B funding round for an undisclosed amount. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 25 Feb 2026 | Peripear | angel syndicate investment | — | british business bank, haatch, HERmesa | UK | FemTech business Peripear, creating a wearable device to prevent perineal tears during childbirth. |
| 16 Feb 2026 | Origin (originww.com) | Series B | — | sjf ventures, Blue Venture Fund, gratitude railroad | — | Origin, a femtech company based in Brentwood, announced in late January it raised a series B funding round for an undisclosed amount. |
| 4 Feb 2026 | Nabta Health (nabtahealth.com) | — | $1.5M | — | UAE | It raised $1.5 million in funding this year. |
| 4 Feb 2026 | Omooma (omooma.com) | — | $2.5M | e20 investment | UAE | Omooma has raised $2.5 million in funding from E20 Investment LTD. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector femtech --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector femtech --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector femtech --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "femtech", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "femtech", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Proptech Funding](proptech-funding.md)
- [Creator Economy Funding](creator-economy-funding.md)
- [Healthtech Funding](healthtech-funding.md)
- [Manufacturing Startup Funding](manufacturing-startup-funding.md)
