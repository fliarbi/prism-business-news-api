# Biotech Funding News: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “biotech funding news” · 390/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [biotech-funding-news.json](../../examples/scenarios/biotech-funding-news.json).

**Question.** How many biotech deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “biotech”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 318 |
| With a usable reported amount | 298 |
| Reported total (usable amounts) | $20.6B |
| Median reported round | $19.7M |
| Largest reported round | $2B |
| Amounts left out as implausible or unconverted | 1 |
| Busiest month | Nov 2025 (39 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 24 | 21 | $1.1B | $25M | ████████████ |
| Jun 2025 | 20 | 18 | $604.9M | $14M | ██████████ |
| Jul 2025 | 15 | 15 | $523.4M | $9.6M | ████████ |
| Aug 2025 | 35 | 33 | $6.3B | $50M | ██████████████████ |
| Sep 2025 | 20 | 18 | $533M | $8.2M | ██████████ |
| Oct 2025 | 36 | 30 | $1.9B | $18.5M | ██████████████████ |
| Nov 2025 | 39 | 37 | $3.5B | $20.8M | ████████████████████ |
| Dec 2025 | 34 | 33 | $1.7B | $14.5M | █████████████████ |
| Jan 2026 | 28 | 28 | $2.1B | $62.2M | ██████████████ |
| Feb 2026 | 18 | 18 | $760.7M | $20.8M | █████████ |
| Mar 2026 | 26 | 25 | $626.6M | $11.3M | █████████████ |
| Apr 2026 | 23 | 22 | $1.2B | $22.2M | ████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 6 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Aug 2025 | Royalty Pharma (royaltypharma.com) | Funding partnership | $2B | revolution medicines | United States | Royalty Pharma plc (NASDAQ:RPRX) entered a $2 billion funding partnership with Revolution Medicines for the development of daraxonrasib, a… |
| 8 Nov 2025 | Halozyme Therapeutics (halozyme.com) | convertible_debt | $1.3B | — | USA | Halozyme Therapeutics, Inc. has priced two new tranches of convertible senior notes totaling $1.3 billion, a move that blends capital… |
| 28 Aug 2025 | Gerresheimer Ag (gerresheimer.de) | revolving credit facility | $729M | — | Germany | Gerresheimer has improved the flexibility of its revolving credit facility of EUR 675 million |
| 10 Nov 2025 | Canton Strategic Holdings | — | $540M | — | — | US biotech firm Canton Strategic Holdings is raising $540m in capital to launch a digital asset treasury in Canton Coin. |
| 7 Oct 2025 | Valneva (valneva.com) | loan agreement | $500M | pharmakon advisors | — | Valneva has secured a new loan agreement that will provide up to $500 million in non-dilutive financing from investment funds managed by… |
| 1 Aug 2025 | Maplight Therapeutics (alvaradotherapeutics.com) | Series D | $372.5M | Forbion, Goldman Sachs Alternatives, sanofi | USA | MapLight Therapeutics, a California-based biotech startup targeting brain and central nervous system disorders, landed a colossal $372.5… |
| 3 Nov 2025 | Tubulis (tubulis.com) | Series C | $371.5M | Fidelity Management & Research Company, janus henderson… | — | Biotech is adding another 36 million euros to its Series C in the second closing to a total volume of 344 million euros. |
| 19 May 2025 | Pathos AI | Series D | $365M ⚠ check sentence | — | — | Pathos AI, a leading AI-driven biotech company, raised $365 million in Series D financing, bringing its post-money valuation to… |
| 15 Apr 2026 | Beeline Medicines | Series A | $300M | bain capital | USA | Beeline Medicines raises $300M Series A for precision autoimmune and inflammatory drug development |
| 23 Jan 2026 | Corxel Pharmaceuticals | Series D1 | $287M | sr one, TCGX Holdings, RA Capital | USA | Corxel Pharmaceuticals, a biotech startup developing an oral GLP‑1 obesity drug, announced a $287 million Series D1 on Jan. 22, 2026. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Mbiomics (mbiomics.com) | Series A | $32.4M | mig fonds, bayern kapital | Germany | The round includes existing investors like MIG Fonds and Bayern Kapital. |
| 24 Apr 2026 | Carmot Therapeutics (carmot.us) | Series E | $150M | — | — | Carmot Therapeutics secured $150 million in Series E for therapies combating obesity and diabetes, underscoring biotech's momentum. |
| 22 Apr 2026 | 10x Science | seed | $4.8M | initialized capital, y combinator, civilization ventures | US | The company announced a $4.8 million seed round led by Initialized Capital, with participation from Y Combinator, Civilization Ventures,… |
| 21 Apr 2026 | Clean Food Group (cleanfood.group) | — | $889k | innovate uk | United Kingdom | The company has also received a £700,000 non-dilutive grant from Innovate UK. |
| 18 Apr 2026 | Biolamina (biolamina.com) | — | $21.6M | european investment bank | Sweden | BioLamina, a Stockholm-based biotech scale-up focused on matrix biology and cell culture has secured a €20 million financing commitment… |
| 18 Apr 2026 | Storm Therapeutics (stormtherapeutics.com) | Series C | $56M | — | United Kingdom | STORM Therapeutics, a Cambridge-based clinical-stage biotech company focused on RNA-targeted cancer therapies, has raised $56 million in… |
| 17 Apr 2026 | ProtierBiotech | Pre-Series A | $2.5M | Hana Ventures, IBK Venture Investment, T Investment | South Korea | South Korean biotech startup ProtierBiotech raised $2.45 million in Pre-Series A funding led by Hana Ventures, IBK Venture Investment, and… |
| 15 Apr 2026 | Terremoto Biosciences (terremotobio.com) | Series C | $108M | ra capital management, deep track capital, Osage… | USA | Terremoto Biosciences Raises $108M Series C for selective AKT1 therapies in oncology and rare disease |
| 15 Apr 2026 | Beeline Medicines | Series A | $300M | bain capital | USA | Beeline Medicines raises $300M Series A for precision autoimmune and inflammatory drug development |
| 15 Apr 2026 | Uluu (uluu.com.au) | grant | $2.1M | Industry Growth Program | Australia | Perth startup Uluu has secured $2.1 million through the Industry Growth Program to supercharge its mission to replace plastic with seaweed. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector biotech --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector biotech --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector biotech --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "biotech", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "biotech", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [AI Startup Funding News](ai-startup-funding-news.md)
- [Series C Funding](series-c-funding.md)
- [Crypto Funding](crypto-funding.md)
- [Series D Funding](series-d-funding.md)
