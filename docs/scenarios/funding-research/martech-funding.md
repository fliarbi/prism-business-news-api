# Martech Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “martech funding” · volume below estimate threshold  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [martech-funding.json](../../examples/scenarios/martech-funding.json).

**Question.** How many martech deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “martech”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 14 |
| With a usable reported amount | 13 |
| Reported total (usable amounts) | $180.7M |
| Median reported round | $5.2M |
| Largest reported round | $123.1M |
| Busiest month | Jul 2025 (4 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 0 | 0 | — | — |  |
| Jun 2025 | 0 | 0 | — | — |  |
| Jul 2025 | 4 | 3 | $124.9M | $1.2M | ████████████████████ |
| Aug 2025 | 0 | 0 | — | — |  |
| Sep 2025 | 2 | 2 | $1.2M | $1.2M | ██████████ |
| Oct 2025 | 1 | 1 | $10M | $10M | █████ |
| Nov 2025 | 0 | 0 | — | — |  |
| Dec 2025 | 1 | 1 | $13.9M | $13.9M | █████ |
| Jan 2026 | 3 | 3 | $24.4M | $5.4M | ███████████████ |
| Feb 2026 | 2 | 2 | $6.3M | $3.2M | ██████████ |
| Mar 2026 | 0 | 0 | — | — |  |
| Apr 2026 | 1 | 1 | $6.7k | $6.7k | █████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 1 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 2 Jul 2025 | Talon.One | Growth | $123.1M | silversmith capital partners, Meritech Capital, crv | Germany | Talon.One, a Germany-based enterprise loyalty and promotion software company, has secured €114 million in growth funding. |
| 16 Jan 2026 | Klearly (klearly.nl) | Series A | $14M | — | USA | Klearly (Raleigh, North Carolina) – MarTech/SaaS: $14 million Series A |
| 8 Dec 2025 | Marketing Evolution (marketingevolution.com) | — | $13.9M | — | — | Marketing Evolution, a marketing measurement and optimization platform, has raised $13.9M in funding according to a recent SEC filing. |
| 1 Oct 2025 | Tie (tie.org) | Series A | $10M | innovating capital, stage 2 capital, hawke ventures | United States | Tie, a Miami, Florida-based AI-powered identity resolution platform for e-commerce brands, has raised $10 million in a Series A round. |
| 4 Feb 2026 | Fibr AI | seed | $5.7M | accel, WillowTree Ventures, MVP Ventures | India | AI-native martech startup Fibr AI has raised $5.7 Mn (about INR 52 Cr) in a seed funding round led by existing investor Accel. |
| 26 Jan 2026 | Playad (playad.co) | Pre-Seed | $5.4M | BRV Capital Management, mirae asset venture investment,… | USA | GIGR (dba Playad), a San Francisco, CA–based AI marketing technology startup, has raised $5.4 million in pre-Seed funding. |
| 8 Jan 2026 | Nitro Commerce (nitrocommerce.ai) | Series A | $5M | cornerstone ventures, India Accelerator & Finvolve,… | India | Nitro Commerce, a Gurugram, India–based AI-driven marketing automation startup, has raised USD $5 million in a Series A funding round. |
| 25 Sep 2025 | Nevam | seed | $1.2M | — | — | Fox has just closed a $1.2 million seed round to scale Nevam |
| 18 Jul 2025 | Streamforge (streamforge.com) | Seed | $1.2M | Anges Québec, Triptyq Capital, telegraph hill capital | Canada | Streamforge, a Montreal, Canada-based AI-driven business intelligence solutions for the creator economy, has raised $1.2 million in a seed… |
| 6 Feb 2026 | Decima2 | Pre-Seed | $609.6k | haatch, Y Combinator Partner Nicolas Dessaigne | United Kingdom | Decima2, an Oxford, UK-based AI startup that provides a platform designed to eliminate wasted marketing spend for SMBs, has raised… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 14 Apr 2026 | Martech Store | Grant | $6.7k | Bet9ja Foundation | Nigeria | At the pitch event, Abraham Babarinde, founder of Martech Store, emerged as the grand prize winner, securing ₦10 million. |
| 6 Feb 2026 | Decima2 | Pre-Seed | $609.6k | haatch, Y Combinator Partner Nicolas Dessaigne | United Kingdom | Decima2, an Oxford, UK-based AI startup that provides a platform designed to eliminate wasted marketing spend for SMBs, has raised… |
| 4 Feb 2026 | Fibr AI | seed | $5.7M | accel, WillowTree Ventures, MVP Ventures | India | AI-native martech startup Fibr AI has raised $5.7 Mn (about INR 52 Cr) in a seed funding round led by existing investor Accel. |
| 26 Jan 2026 | Playad (playad.co) | Pre-Seed | $5.4M | BRV Capital Management, mirae asset venture investment,… | USA | GIGR (dba Playad), a San Francisco, CA–based AI marketing technology startup, has raised $5.4 million in pre-Seed funding. |
| 16 Jan 2026 | Klearly (klearly.nl) | Series A | $14M | — | USA | Klearly (Raleigh, North Carolina) – MarTech/SaaS: $14 million Series A |
| 8 Jan 2026 | Nitro Commerce (nitrocommerce.ai) | Series A | $5M | cornerstone ventures, India Accelerator & Finvolve,… | India | Nitro Commerce, a Gurugram, India–based AI-driven marketing automation startup, has raised USD $5 million in a Series A funding round. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector martech --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector martech --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector martech --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "martech", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "martech", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Legaltech Funding](legaltech-funding.md)
- [Lending Startup Funding](lending-startup-funding.md)
- [Payments Startup Funding](payments-startup-funding.md)
- [Pet Care Startup Funding](pet-care-startup-funding.md)
