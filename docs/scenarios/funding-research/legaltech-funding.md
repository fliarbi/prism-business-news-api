# Legaltech Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “legaltech funding” · volume below estimate threshold  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [legaltech-funding.json](../../examples/scenarios/legaltech-funding.json).

**Question.** How many legaltech deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “legaltech”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 78 |
| With a usable reported amount | 76 |
| Reported total (usable amounts) | $2.3B |
| Median reported round | $5.8M |
| Largest reported round | $500M |
| Busiest month | Oct 2025 (17 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3 | 3 | $157.5M | $76.2M | ████ |
| Jun 2025 | 9 | 9 | $362.6M | $3.4M | ███████████ |
| Jul 2025 | 3 | 3 | $17.2M | $4M | ████ |
| Aug 2025 | 4 | 3 | $23.1M | $7.5M | █████ |
| Sep 2025 | 9 | 9 | $484.4M | $5.3M | ███████████ |
| Oct 2025 | 17 | 17 | $415.3M | $7.4M | ████████████████████ |
| Nov 2025 | 4 | 3 | $19M | $6M | █████ |
| Dec 2025 | 2 | 2 | $2.6M | $1.3M | ██ |
| Jan 2026 | 13 | 13 | $213.4M | $8M | ███████████████ |
| Feb 2026 | 6 | 6 | $141.4M | $22M | ███████ |
| Mar 2026 | 4 | 4 | $21M | $2.5M | █████ |
| Apr 2026 | 4 | 4 | $508.8M | $3.2M | █████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 12 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 14 Apr 2026 | Legora | — | $500M | — | — | Legora, an AI-powered legaltech firm, attracted over $500 million amid rising demand for intelligent applications. |
| 23 Sep 2025 | Filevine (filevine.com) | Series E | $400M | insight partners, accel, Halo Fund | USA |  |
| 25 Jun 2025 | Harvey AI | Series E | $300M ⚠ check sentence | kleiner perkins, coatue, conviction | United States | Harvey AI, a San Francisco-based generative AI platform for the legal and professional services industries, has raised $300 million in… |
| 5 Feb 2026 | Lawhive (lawhive.co.uk) | Series B | $60M | Mitch Rales, tq ventures, google ventures | UK | Lawhive is a UK-based startup reinventing the general‑practice law firm by combining human lawyers with AI‑powered workflows. … The round… |
| 26 Jan 2026 | Orbital (getorbital.com) | Series B | $60M | brighton park capital, rev, The LegalTech Fund | United Kingdom | Orbital, a London, UK–based AI-native platform for real estate law and property due diligence, has raised $60 million in Series B funding. |
| 27 Jan 2026 | Spotdraft (spotdraft.com) | Series B | $56M | — | — | The investment follows SpotDraft’s $56 million Series B raise in February 2025 and reflects accelerating enterprise demand for secure,… |
| 27 Jan 2026 | Summize (summize.com) | — | $50.8M | maven capital partners, kennet partners, Federated Hermes… | United Kingdom | LegalTech Summize has completed a £40 million funding and reinvestment round to accelerate global expansion. |
| 9 Oct 2025 | Spellbook (spellbook.legal) | Series B | $50M | threshold, inovia, bling | Canada | Spellbook, co-founded and led by Scott Stevenson, announced a $50 million Series B led by Keith Rabois of Khosla Ventures, valuing the… |
| 9 Oct 2025 | Enter (enter.de) | Series A | $37.5M | founders fund, sequoia capital | Brazil | São Paulo-based legaltech company Enter has successfully raised $37.5 million in a Series A funding round led by Founders Fund and Sequoia… |
| 29 Oct 2025 | Syllo (syllo.ai) | Growth Funding | $30M | venrock, Two Seas Capital, Strategic individual investors | — | Syllo, a New York–based company that provides AI-powered litigation platform, has secured $30 million in growth funding. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 21 Apr 2026 | Lawyered (lawyered.in) | Pre-Series A | $2.5M | Rainmatter, Turbostart, finvolve | India | Lawyered has raised $2.5 million in a pre-Series A funding round co-led by Rainmatter by Zerodha and Turbostart, with participation from… |
| 20 Apr 2026 | Beleuert.de | seed | $3M | Jawed Karim, moonfire ventures, zeno ventures | — | The platform is backed by the Legaltech Openlaw, which has completed a seed financing round of 2.8 million euros (3.3 million dollars).… |
| 16 Apr 2026 | Openlaw (openlaw.io) | seed | $3.3M | Jawed Karim, moonfire ventures, other international VCs… | Germany | The Munich-based LegalTech-Startup Openlaw has completed a seed financing of 3.3 million US dollars. |
| 14 Apr 2026 | Legora | — | $500M | — | — | Legora, an AI-powered legaltech firm, attracted over $500 million amid rising demand for intelligent applications. |
| 27 Mar 2026 | Keith (keithcompany.com) | seed | $2.5M | backed vc, breega, Angel Investors | UK | Keith, a new UK-based AI-native law firm, has raised €2.3 million (£2 million) in seed funding ahead of its launch this summer. |
| 24 Mar 2026 | Avvoka (avvoka.com) | Growth | $17.8M | Valhalla Ventures | UK | Legaltech platform Avvoka announced that it has secured £14 million of growth investment, in a funding round led by Mark and Lindy… |
| 11 Mar 2026 | Avvoka (avvoka.com) | Angel | $762k | — | — | Bootstrapped from launch in 2016, with just £600k raised from angel investors, the investment is the first institutional capital raised by… |
| 26 Feb 2026 | Firmpilot (firmpilot.com) | Series A-1 | $22M | deepwork capital, data point capital, blumberg capital | United States | FirmPilot Raises $22M Series A-1 Round Back to Home MIAMI, FL, FirmPilot, the AI-powered legal marketing platform, today announced the… |
| 9 Feb 2026 | HAQQ Legal AI | seed | $3M | — | Lebanon | Lebanon’s HAQQ Legal AI has secured USD 3 million in fresh funding, a notable vote of confidence for a young legaltech company trying to… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector legaltech --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector legaltech --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector legaltech --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "legaltech", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "legaltech", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Foodtech Funding](foodtech-funding.md)
- [Hrtech Funding](hrtech-funding.md)
- [Lending Startup Funding](lending-startup-funding.md)
- [Martech Funding](martech-funding.md)
