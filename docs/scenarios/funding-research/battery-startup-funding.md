# Battery Startup Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “battery startup funding” · volume below estimate threshold  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [battery-startup-funding.json](../../examples/scenarios/battery-startup-funding.json).

**Question.** How many battery startup deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “battery”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 403 |
| With a usable reported amount | 362 |
| Reported total (usable amounts) | $57.3B |
| Median reported round | $15.8M |
| Largest reported round | $15B |
| Busiest month | Apr 2026 (59 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 29 | 27 | $5.9B | $15.6M | ██████████ |
| Jun 2025 | 15 | 14 | $15.3B | $4.5M | █████ |
| Jul 2025 | 14 | 10 | $1.8B | $108.8M | █████ |
| Aug 2025 | 20 | 19 | $1.7B | $7.4M | ███████ |
| Sep 2025 | 47 | 47 | $1.8B | $11.1M | ████████████████ |
| Oct 2025 | 44 | 42 | $2.2B | $10M | ███████████████ |
| Nov 2025 | 41 | 35 | $1.3B | $7.4M | ██████████████ |
| Dec 2025 | 35 | 35 | $4.6B | $38.6M | ████████████ |
| Jan 2026 | 27 | 23 | $1.9B | $5M | █████████ |
| Feb 2026 | 40 | 33 | $3.5B | $32.4M | ██████████████ |
| Mar 2026 | 32 | 29 | $2.6B | $21.9M | ███████████ |
| Apr 2026 | 59 | 48 | $15.6B | $48.2M | ████████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 19 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 6 Jun 2025 | Northvolt (northvolt.com) | — | $15B | volkswagen, goldman sachs, pension funds | Sweden | It collected over $15 billion in a single financing round, as much as no other start-up until then. |
| 28 Apr 2026 | Contemporary Amperex Technology (catl.com) | Share Sale | $5B | — | Hong Kong | has raised $5 billion through a share sale in Hong Kong |
| 28 Apr 2026 | CATL | share placement | $5B | — | — | From ESS News The world’s leading battery maker, CATL, completed a share placement in Hong Kong on Tuesday, raising about $5 billion in a… |
| 3 Dec 2025 | Vulcan Energy (v-er.eu) | debt financing | $1.3B | export development canada, export finance australia,… | Germany | Vulcan Energy has closed a €1.2bn financing package with a range of export credit agencies (ECAs) and banks to fund the first phase of a… |
| 31 Mar 2026 | StarPlus Energy | loan | $1.2B | samsung sdi | — | South Korea's Samsung SDI said it plans to lend 1.6 trillion won ($1.05 billion) to StarPlus Energy, its battery joint venture with… |
| 10 Apr 2026 | Ascend Elements (ascendelements.com) | — | $1.1B ⚠ check sentence | — | USA | Westborough, Massachusetts-based Ascend, which specializes in reprocessing old batteries into cathode material at a factory in Georgia,… |
| 6 Feb 2026 | Ardea Resources (ardearesources.com.au) | Non-binding Funding Support | $1B | export finance australia, Export-Import Bank of the United… | Australia | Ardea Resources has secured up to $1 billion in non-binding funding support from US and Australian government agencies for its Goongarrie… |
| 8 Oct 2025 | Base Power (basepower.in) | Series C | $1B | addition, capitalg, Elad Gil | USA | The Austin-based startup, which had raised $200 million in April, is back with another $1 billion in funding. |
| 13 May 2025 | POSCO Future M (poscofuturem.com) | Rights Offering | $825M | POSCO Holdings | South Korea | Posco Future M, the group’s core battery materials subsidiary, had earlier announced a rights offering worth 1.1 trillion won to secure… |
| 8 Apr 2026 | Agratas Energy Storage Solutions Pvt. Ltd | Bank financing | $730M | axis bank, dbs bank, Hong Kong and Shanghai Banking Corp. | India | has raised more than $730 million from a group of banks in 2025, as the company moves closer to starting commercial operations |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Nouveau Monde Graphite (nmg.com) | Equity Financing | $297M | Canada Growth Fund, Investissement Québec, eni | Canada | Canadian graphite mine developer Nouveau Monde Graphite (NMG) has received a commitment of $297 million in financing to support its Phase… |
| 29 Apr 2026 | Matrix Renewables (matrixrenewables.com) | non-recourse financing | $311.1M | cibc, mufg bank, natwest | United Kingdom | Matrix Renewables has reached financial close on a £245 million non-recourse financing package to support the construction of a 500MW /… |
| 29 Apr 2026 | Battery Smart (batterysmart.in) | Series B (extended) | $29M | tiger global, blume ventures, ecosystem integrity fund | — | With its $65 million Series B round and $29 million extended Series B round, Battery Smart has raised about $192 million in funding thus… |
| 29 Apr 2026 | Nexamp (nexamp.com) | credit facility | $200M | Nuveen Energy Infrastructure Credit | US | Nexamp, a developer of solar and battery storage projects, secured a $200 million credit facility from Nuveen Energy Infrastructure… |
| 29 Apr 2026 | Battery Smart (batterysmart.in) | Debt financing | $15M | mirova | India | Battery Smart, India's leading EV battery swapping provider, has raised $15 million in debt financing. The funding round was led by… |
| 28 Apr 2026 | Renewable Metals (renewable-metals.com) | Series A | $12M | CEFC/Virescent Ventures, emr, Neglected Climate… | Australia | Renewable Metals Raises $12M Series A for Battery Recycling. |
| 28 Apr 2026 | Contemporary Amperex Technology (catl.com) | Share Sale | $5B | — | Hong Kong | has raised $5 billion through a share sale in Hong Kong |
| 28 Apr 2026 | CATL | share placement | $5B | — | — | From ESS News The world’s leading battery maker, CATL, completed a share placement in Hong Kong on Tuesday, raising about $5 billion in a… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector battery --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector battery --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector battery --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "battery", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "battery", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Quick Commerce Funding](quick-commerce-funding.md)
- [B2b Marketplace Funding](b2b-marketplace-funding.md)
- [Construction Tech Funding](construction-tech-funding.md)
- [Defence Tech Funding](defence-tech-funding.md)
