# Y Combinator Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “y combinator portfolio” · 50/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [y-combinator-portfolio.json](../../examples/scenarios/y-combinator-portfolio.json).

**Question.** Which rounds did Y Combinator appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Y Combinator”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 476 |
| With a usable reported amount | 457 |
| Reported total (usable amounts) | $12.7B |
| Median reported round | $15M |
| Largest reported round | $1B |
| Busiest month | Mar 2026 (52 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 33 | 32 | $859M | $14.5M | █████████████ |
| Jun 2025 | 28 | 27 | $713.6M | $22M | ███████████ |
| Jul 2025 | 23 | 23 | $907.9M | $13M | █████████ |
| Aug 2025 | 50 | 45 | $672.6M | $15.3M | ███████████████████ |
| Sep 2025 | 51 | 49 | $1.4B | $20M | ████████████████████ |
| Oct 2025 | 51 | 47 | $1.5B | $12.4M | ████████████████████ |
| Nov 2025 | 46 | 45 | $869.9M | $11M | ██████████████████ |
| Dec 2025 | 31 | 30 | $1.6B | $15M | ████████████ |
| Jan 2026 | 25 | 25 | $756.9M | $13M | ██████████ |
| Feb 2026 | 38 | 38 | $819.7M | $13.7M | ███████████████ |
| Mar 2026 | 52 | 51 | $2.3B | $20.8M | ████████████████████ |
| Apr 2026 | 48 | 45 | $1.6B | $16.2M | ██████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 25 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 3 Dec 2025 | Kalshi (kalshi.com) | Series E | $1B | paradigm, sequoia, Andreessen Horowitz | United States | Kalshi, a New York-based financial exchange and prediction market, has closed a $1 billion Series E round valuing the company at $11… |
| 10 Mar 2026 | Legora | Series D | $550M | accel, benchmark, bessemer venture partners | Sweden | Legora Raises $550M in Series D Funding to Expand AI in Legal Operations |
| 19 Oct 2025 | Meesho (meesho.com) | equity | $510M | elevation capital, peak xv partners, Highway Series 1 | India | Bengaluru-based online marketplace Meesho has filed its updated draft red herring prospectus (UDRHP) with the SEBI to raise up to ₹4,250… |
| 3 Apr 2026 | Supabase (supabase.com) | — | $500M | accel, felicis, Coatue Management | — | Supabase is seeking to raise about $500 million in the fundraising round, although the amount could change. |
| 4 Jul 2025 | Rippling (rippling.com) | Collection G spherical | $450M ⚠ check sentence | sands capital, gic, Goldman Sachs Development | US | Rippling, a San Francisco-based HR tech startup, has raised $450 million in a Collection G funding spherical, valuing the corporate at… |
| 11 Mar 2026 | Replit (replit.com) | Series D | $400M | georgian, g squared, Andreessen Horowitz | United States | Replit raises $400M in Series D funding to scale its AI-powered coding platform. |
| 16 Jan 2026 | Boom Supersonic (boomsupersonic.com) | Series B | $300M | altimeter capital, ark investment management, bessemer… | United States | Round: Series B |
| 6 Mar 2026 | Science Corporation (sciencecorporation.vdtrxn) | Series C | $230M | lightspeed venture partners, khosla ventures, y combinator | — | Neurotechnology company Science Corporation, founded by Max Hodak, announced an oversubscribed $230 million Series C financing round. |
| 24 Jul 2025 | Vanta (vanta.com) | Series D | $150M | wellington management, goldman sachs, sequoia capital | USA |  |
| 23 Apr 2026 | Sygaldry Technologies | Series A and Seed | $139M | earth venture capital, initialized capital, breakthrough… | US | Earth Venture Capital, a decarbonization-focused climate tech venture capital firm based in Singapore, has announced its involvement in… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | General Analysis | Seed | $10M | altos ventures, 645 ventures, menlo ventures | — | General Analysis, a San Francisco-based startup focused on AI security, has raised $10 million in seed funding to tackle a growing risk:… |
| 27 Apr 2026 | Archil | — | $11M | Andrew Jefferson, Anurag Goel, felicis | US | San Francisco-based Archil a software company that develops cloud storage software that enables organizations to access and manage large… |
| 24 Apr 2026 | Totalis (totalis.uk) | seed | $500k | y combinator | — | Earlier this month, Totalis — a prediction‑market startup working with USDC on Solana — disclosed that it received Y Combinator’s standard… |
| 23 Apr 2026 | Astor (astorim.com) | Seed | $5M | monashees, y combinator, goodwater | — | Astor Raises $5M Seed for AI-Based Financial Advice |
| 23 Apr 2026 | Sygaldry Technologies | Series A and Seed | $139M | earth venture capital, initialized capital, breakthrough… | US | Earth Venture Capital, a decarbonization-focused climate tech venture capital firm based in Singapore, has announced its involvement in… |
| 22 Apr 2026 | 10x Science | seed | $4.8M | initialized capital, y combinator, civilization ventures | US | The company announced a $4.8 million seed round led by Initialized Capital, with participation from Y Combinator, Civilization Ventures,… |
| 20 Apr 2026 | Firecrawl | Series A | $16.2M | Nexus VP, y combinator | Brazil | Seven months ago, Firecrawl raised an R$ 81 million contribution in a Series A round led by Nexus VP, with Y Combinator's follow-on, with… |
| 20 Apr 2026 | Beleuert.de | seed | $3M | Jawed Karim, moonfire ventures, zeno ventures | — | The platform is backed by the Legaltech Openlaw, which has completed a seed financing round of 2.8 million euros (3.3 million dollars).… |
| 20 Apr 2026 | Lua Global Inc. | Unknown | $5.8M | norrsken22, flourish ventures, 20VC | UK | Lua, a London, UK–based operating system for human agent collaboration in the workspace, has raised $5.8 million in funding. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "Y Combinator" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "Y Combinator" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "Y Combinator" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Y Combinator", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Y Combinator", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Investor names match broadly (a name can match several firms or funds); use a domain for a narrower match.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Dst Global Portfolio](dst-global-portfolio.md)
- [Lux Capital Portfolio](lux-capital-portfolio.md)
- [First Round Capital Portfolio](first-round-capital-portfolio.md)
- [GV Investments](gv-investments.md)
