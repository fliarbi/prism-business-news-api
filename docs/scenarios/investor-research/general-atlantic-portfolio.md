# General Atlantic Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “general atlantic portfolio” · 50/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [general-atlantic-portfolio.json](../../examples/scenarios/general-atlantic-portfolio.json).

**Question.** Which rounds did General Atlantic appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “General Atlantic”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 49 |
| With a usable reported amount | 42 |
| Reported total (usable amounts) | $6.7B |
| Median reported round | $144M |
| Largest reported round | $859.5M |
| Busiest month | Jul 2025 (9 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2 | 1 | $358.6M | $358.6M | ████ |
| Jun 2025 | 1 | 1 | $308M | $308M | ██ |
| Jul 2025 | 9 | 7 | $815.8M | $144M | ████████████████████ |
| Aug 2025 | 5 | 5 | $386M | $97.5M | ███████████ |
| Sep 2025 | 2 | 1 | $525M | $525M | ████ |
| Oct 2025 | 6 | 6 | $1B | $187.5M | █████████████ |
| Nov 2025 | 5 | 5 | $1B | $210M | ███████████ |
| Dec 2025 | 6 | 5 | $660M | $100M | █████████████ |
| Jan 2026 | 1 | 0 | — | — | ██ |
| Feb 2026 | 6 | 6 | $1.7B | $207.5M | █████████████ |
| Mar 2026 | 5 | 5 | $1.4B | $704.8M | ███████████ |
| Apr 2026 | 1 | 0 | — | — | ██ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 19 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 24 Mar 2026 | Runway (runway.com) | Series E | $859.5M | adobe ventures, alliancebernstein, AMD Ventures | USA |  |
| 30 Oct 2025 | Phonepe (phonepe.com) | secondary transaction | $600M | general atlantic | India | General Atlantic has invested about $600 million in PhonePe through a secondary transaction |
| 9 Mar 2026 | Sierra Space (sierraspace.com) | — | $550M | andalusian private capital, coatue, general atlantic | USA | Sierra Space – $550.0M |
| 15 Dec 2025 | Brevo (brevo.com) | Liquidity event | $540M | general atlantic, oakley, partech | France | Brevo just joined France’s unicorn club with a splashy €500 million announcement, resetting the cap table. |
| 4 Nov 2025 | Property Finder (propertyfinder.com) | Debt Round | $525M | permira, blackstone, general atlantic | UAE | Property Finder Raises A $525M Debt Round |
| 20 May 2025 | Butternut Box (butternutbox.com) | investment | $358.6M | general atlantic, l catterton | UK | Having most recently received a €332 million investment from General Atlantic and L Catterton. |
| 11 Nov 2025 | Balaji Wafers (balajiwafers.com) | — | $300M | general atlantic | India | US-based private equity firm General Atlantic is close to finalizing a ₹2,500 crore investment for a 7% stake in Balaji Wafers, valuing… |
| 27 Oct 2025 | Nurix Therapeutics (nurixtx.com) | underwritten registered offering | $250M | general atlantic, redmile group, Braidwell | USA | the closing of its previously announced underwritten registered offering of 24,485,799 shares of its common stock at a purchase price of… |
| 2 Jul 2025 | Klar (klar.mx) | — | $190M | general atlantic, Grupo Santander, sdg | Mexico | Klar, a Mexican neobank, recently announced the raising of $190 million in a new round of financing, consisting of $170 million in capital… |
| 1 Jul 2025 | Kfin Technologies (kfintech.com) | Secondary Share Sale | $145.2M | General Atlantic Singapore | India | In another block deal, General Atlantic Singapore, KFin Technologies' biggest shareholder, is selling about 6.9% in the company for about… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 16 Apr 2026 | Joe & the Juice (joejuice.com) | — | — | general atlantic | Denmark | Joe & The Juice has made significant strides since selling a majority stake to New York investment firm General Atlantic in November 2023. |
| 24 Mar 2026 | Runway (runway.com) | Series E | $859.5M | adobe ventures, alliancebernstein, AMD Ventures | USA |  |
| 9 Mar 2026 | Sierra Space (sierraspace.com) | — | $550M | andalusian private capital, coatue, general atlantic | USA | Sierra Space – $550.0M |
| 12 Feb 2026 | Bold (boldstrategies.com) | — | $40M | general atlantic, Cóndor Inverlink, inqlab | Colombia | Bold, a Colombia-based SME-focused payments and financial services FinTech providing digital payments and business management tools,… |
| 11 Feb 2026 | Runway AI (runway-ai.ai) | Series E | $315M | general atlantic, nvidia, fidelity | USA | The company raised $315 million in its Series E funding round, led by General Atlantic. |
| 10 Feb 2026 | Runway (runway.com) | Series E | $31.5M ⚠ check sentence | general atlantic, nvidia, Fidelity Management & Research | — | Runway has closed a $315 million Series E led by General Atlantic, with notable participation from Nvidia, Fidelity Management & Research,… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "General Atlantic" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "General Atlantic" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "General Atlantic" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "General Atlantic", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "General Atlantic", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Warburg Pincus Portfolio](warburg-pincus-portfolio.md)
- [Benchmark Investments](benchmark-investments.md)
- [Tiger Global Portfolio](tiger-global-portfolio.md)
- [Founders Fund Portfolio](founders-fund-portfolio.md)
