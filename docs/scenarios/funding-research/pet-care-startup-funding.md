# Pet Care Startup Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “pet care startup funding” · volume below estimate threshold  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [pet-care-startup-funding.json](../../examples/scenarios/pet-care-startup-funding.json).

**Question.** How many pet care startup deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “pet”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 79 |
| With a usable reported amount | 72 |
| Reported total (usable amounts) | $1.5B |
| Median reported round | $8.6M |
| Largest reported round | $175M |
| Busiest month | May 2025 (14 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 14 | 12 | $335.3M | $24M | ████████████████████ |
| Jun 2025 | 6 | 6 | $17.8M | $3M | █████████ |
| Jul 2025 | 3 | 1 | $2.1M | $2.1M | ████ |
| Aug 2025 | 10 | 10 | $137.2M | $2.7M | ██████████████ |
| Sep 2025 | 0 | 0 | — | — |  |
| Oct 2025 | 4 | 3 | $3.6M | $1.8M | ██████ |
| Nov 2025 | 3 | 3 | $8.4M | $4.2M | ████ |
| Dec 2025 | 7 | 6 | $113.7M | $16.2M | ██████████ |
| Jan 2026 | 1 | 1 | $90k | $90k | █ |
| Feb 2026 | 13 | 12 | $296.7M | $16.8M | ███████████████████ |
| Mar 2026 | 10 | 10 | $446.4M | $52M | ██████████████ |
| Apr 2026 | 8 | 8 | $347M | $30M | ███████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 19 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 15 Apr 2026 | Phillips Pet Food | Unitranche asset-based lending revolver | $175M | gordon brothers | — | Gordon Brothers, the global asset experts, provided $175 million in strategic financing to support Phillips Pet Food’s acquisition of… |
| 15 Apr 2026 | Nasta Pet Food | — | $140M | H.I.G. Whitehorse | — | H.I.G. Whitehorse arranged a $140 million financing package for the manufacturer. |
| 22 May 2025 | Butternut Box (butternutbox.com) | Growth / Debt Financing | $100M | liquidity group | United Kingdom | Butternut Box Fetches $100 M in Debt Financing for Fresh Pet Food Service |
| 12 Feb 2026 | Lassie (lassie.co) | Series C | $75M | balderton capital, felix capital, inventure | Sweden | Stockholm-based Lassie, a prevention-focused pet insurer, has raised $75 million in Series C funding to support its expansion across… |
| 20 Aug 2025 | Enviroo (enviroo.com) | — | $73.7M | — | UK | Enviroo, a UK-based PET recycling company, has confirmed it has secured £58 million ($78.2m) in funding for its planned facility in… |
| 2 Mar 2026 | Lyka (lyka.com.au) | Series C | $67M | LGVP | Australia | Lyka has raised $67 million in a Series C led by US investors to fund global expansion and clinical research into dog health and longevity. |
| 3 Mar 2026 | Cirklo (cirklo.mx) | — | $52M | — | Brazil | Cirklo, one of Brazil's largest PET waste pickers, announces the capture of R$ 260 million through the issuance of green debentures, in… |
| 16 Dec 2025 | Katkin (katkin.com) | Series C | $50M | Unnamed group of investors | UK | UK-based fresh cat food producer KatKin has raised $50m in equity and debt funding to help the company expand across the country. |
| 11 Aug 2025 | Jinx (thinkjinx.com) | — | $46M | — | United States | previous funding rounds raised $46 million to support Jinx’s brick-and-mortar retail launch and expand its product portfolio. |
| 5 May 2025 | Heads Up for Tails (headsupfortails.com) | Undisclosed | $40M | peak xv, verlinvest | India | Earlier this year, Mint reported that Heads Up For Tails has begun fresh talks to raise $40 million from new and existing investors such… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 28 Apr 2026 | Sportpet Designs (sportpetdesign.com) | revolving credit facility | $30M | wingspire capital | — | Wingspire Capital announced the closing of a $30 million revolving credit facility to SportPet Designs LLC, a designer, manufacturer and… |
| 23 Apr 2026 | OurPetsLife | — | $342.9k | gc angels | UK | It made a £270k investment into Manchester’s OurPetsLife. |
| 15 Apr 2026 | Nasta Pet Food | — | $140M | H.I.G. Whitehorse | — | H.I.G. Whitehorse arranged a $140 million financing package for the manufacturer. |
| 15 Apr 2026 | Phillips Pet Food | Unitranche asset-based lending revolver | $175M | gordon brothers | — | Gordon Brothers, the global asset experts, provided $175 million in strategic financing to support Phillips Pet Food’s acquisition of… |
| 11 Apr 2026 | Petwealth | — | $1.7M | — | USA | Petwealth, a Miami-based pet health diagnostics company, announced its emergence from stealth with $1.7 million in funding as it looks to… |
| 17 Mar 2026 | Zoomies (gozoomies.in) | pre-seed | $600k | D2C Insider Super Angels, Pallavi Mohadikar, Unacademy… | India | Pet food startup Zoomies has raised â¹5 crore in a pre-seed funding round led by D2C Insider Super Angels |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector pet --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector pet --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector pet --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "pet", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "pet", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Martech Funding](martech-funding.md)
- [Payments Startup Funding](payments-startup-funding.md)
