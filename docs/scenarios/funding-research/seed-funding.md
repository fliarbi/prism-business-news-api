# Seed Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “seed funding” · 5,400/month India · 1,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [seed-funding.json](../../examples/scenarios/seed-funding.json).

**Question.** How many seed deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** round type “seed”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 5,078 |
| With a usable reported amount | 4,641 |
| Reported total (usable amounts) | $67.8B |
| Median reported round | $3.2M |
| Largest reported round | $12B |
| Amounts left out as implausible or unconverted | 7 |
| Busiest month | Sep 2025 (494 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 361 | 329 | $2.3B | $3.8M | ███████████████ |
| Jun 2025 | 394 | 350 | $3.6B | $3.5M | ████████████████ |
| Jul 2025 | 412 | 362 | $16B | $3.2M | █████████████████ |
| Aug 2025 | 397 | 356 | $5.2B | $2.7M | ████████████████ |
| Sep 2025 | 494 | 459 | $2.5B | $3.3M | ████████████████████ |
| Oct 2025 | 487 | 455 | $5.7B | $3.5M | ████████████████████ |
| Nov 2025 | 452 | 418 | $2.6B | $3.5M | ██████████████████ |
| Dec 2025 | 351 | 321 | $2.4B | $3.8M | ██████████████ |
| Jan 2026 | 399 | 366 | $6B | $3M | ████████████████ |
| Feb 2026 | 477 | 439 | $4B | $3.2M | ███████████████████ |
| Mar 2026 | 405 | 375 | $15.1B | $4M | ████████████████ |
| Apr 2026 | 449 | 411 | $4.5B | $3.1M | ██████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 24 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 21 Jul 2025 | Thinking Machines Lab | Seed | $12B | — | — | 07/15/25 — Thinking Machines Lab — $12B Seed |
| 27 Apr 2026 | Ineffable Intelligence | Seed | $1.1B ⚠ check sentence | — | United Kingdom | Startup Ineffable Intelligence has just come out of stealth.The company, with a mission to make first contact with superintelligence, has… |
| 13 Mar 2026 | Ami Labs (amilabs.xyz) | seed | $1.1B | — | — | The new start-up AMI Labs from AI pioneer Yann LeCun has collected 1.1 billion dollars (890 million euros) â , the largest start-up… |
| 18 Mar 2026 | Advanced Machine Intelligence Labs – AMI | seed | $1B | — | — | Yann LeCun, one of the three Turing winners who founded the field of deep learning, collected $1.03 billion in a seed round with his new… |
| 13 Aug 2025 | Refold AI | seed | $650M | eniac ventures, tidal ventures, better capital | — | A US-headquartered start-up secured $650 million in seed funding it stated would drive its work to employ agentic AI to tackle a hefty… |
| 9 Oct 2025 | Stoke Space Technologies (stoke-space.com) | Seed | $510M | US Innovative Technology Fund, silicon valley bank | USA | Stoke Space, a Kent, Washington-based rocket company building fully reusable launch vehicles, has raised a staggering $510 million in new… |
| 23 Mar 2026 | Humans& | Seed | $480M | SV Angel, nvidia, Jeff Bezos | USA | humans& raises $480M Seed to build a human-centric AI research lab |
| 19 Jan 2026 | Na | seed | $475M | — | — | A two-month-old AI computer company raised a massive $475 million seed round. |
| 19 Jan 2026 | Cursor (cursor.com) | seed | $475M | a16z | — | A two-month-old AI computer company raised a massive $475 million seed round |
| 9 Dec 2025 | Unconventional AI | Seed | $475M ⚠ check sentence | lightspeed venture partners, Andreessen Horowitz, lux… | United States | Unconventional AI has raised $475M in funding from Lightspeed Venture Partners and Andreessen Horowitz , with a current valuation of $4.5B . |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Opalia (opaliafoods.com) | Seed | $3.2M | — | — | Green Queen 🇨🇦 Montreal cell-based dairy company Opalia closes $3.2m seed round with commercial pilots already underway |
| 30 Apr 2026 | Exponent (exponentpe.com) | seed | $5M | multicoin capital | — | Exponent has raised $5 million in a seed round led by Multicoin Capital |
| 30 Apr 2026 | Hyugalife (hyugalife.com) | seed | $6.3M | peak xv, spring marketing capital, stride ventures | India | The raise follows a $6.3 million seed round in February 2024 from Peak XV and Spring Marketing Capital, with additional backing from… |
| 30 Apr 2026 | Ubiqedge (ubiqedge.com) | seed | $1.2M | Piper Serica, Shibam Das, Sumit Chhazed | India | IoT startup Ubiqedge on Thursday raised ₹10 crore in a seed funding round led by Piper Serica, with participation from Atomberg co-founder… |
| 30 Apr 2026 | Spiral Hydrogen | pre-seed | $2.9M | byfounders, Norrsken Evolve, superangel | — | Estonian-Dutch deeptech startup Spiral Hydrogen has raised €2.7 million in pre-seed funding, along with €0.7 million in grants, to develop… |
| 30 Apr 2026 | Misti AI | pre-seed | $336k | fuel ventures | — | Misti AI has secured $336,000 in pre‑seed funding led by Fuel Ventures, with the round still open as the company targets a total of… |
| 30 Apr 2026 | Shiprazor (shiprazor.com) | seed | $2.6M | norrsken22, aaic, e4e | South Africa | Shiprazor, the Cape Town-based e-commerce merchant technology and smart logistics platform, has raised $2.65 million (R44m) in seed… |
| 30 Apr 2026 | Ctruh (ctruh.com) | Seed | $2.5M | inflection point ventures, Avinya Ventures, india… | India | Ctruh, the deep-tech company building the infrastructure layer for the spatial internet, has raised $2.5 Million in a Seed funding round… |
| 30 Apr 2026 | Synaps (synaps.io) | pre-seed | $3.6M | plug and play, Fil Rouge Capital | Austria | Five months later, Synaps is announcing a $3.6 million pre‑seed funding round from US‑based accelerator and VC Plug and Play, and… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --round-type seed --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --round-type seed --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --round-type seed --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"round_type": "seed", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"round_type": "seed", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Series A Funding](series-a-funding.md)
- [Series B Funding](series-b-funding.md)
