# GV Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “gv investments” · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [gv-investments.json](../../examples/scenarios/gv-investments.json).

**Question.** Which rounds did GV appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “GV”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 129 |
| With a usable reported amount | 123 |
| Reported total (usable amounts) | $7.7B |
| Median reported round | $28M |
| Largest reported round | $1.5B |
| Busiest month | Aug 2025 (17 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 16 | 16 | $342.6M | $20.6M | ███████████████████ |
| Jun 2025 | 7 | 7 | $526.6M | $52.5M | ████████ |
| Jul 2025 | 16 | 13 | $223.9M | $4M | ███████████████████ |
| Aug 2025 | 17 | 16 | $406.9M | $12M | ████████████████████ |
| Sep 2025 | 7 | 7 | $675.5M | $112.5M | ████████ |
| Oct 2025 | 12 | 12 | $396.3M | $23.9M | ██████████████ |
| Nov 2025 | 11 | 10 | $139.7M | $7M | █████████████ |
| Dec 2025 | 6 | 6 | $159.6M | $8M | ███████ |
| Jan 2026 | 7 | 6 | $732M | $107M | ████████ |
| Feb 2026 | 15 | 15 | $1.6B | $50M | ██████████████████ |
| Mar 2026 | 7 | 7 | $1.8B | $53.5M | ████████ |
| Apr 2026 | 8 | 8 | $915.2M | $70M | █████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 12 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 24 Mar 2026 | SambaNova | Series E | $1.5B | battery ventures, cambium capital partners, first data | USA |  |
| 20 Apr 2026 | Recursive Superintelligence | Private round | $500M | GV, nvidia | — | Recursive Superintelligence raised $500M+ private round for self‑improving AI systems. |
| 20 Jan 2026 | Humans& | Seed | $480M ⚠ check sentence | nvidia, Jeff Bezos, SV Angel | USA | "Humans&, a startup with a philosophy that AI should empower people rather than replace them, has raised $480 million in seed funding at a… |
| 13 Feb 2026 | Inertia (inertialab.com) | Series A | $450M | bessemer venture partners, GV, modern capital | USA | Fusion startup Inertia has secured $450 million in Series A funding to accelerate commercialization of inertial confinement fusion,… |
| 25 Jun 2025 | Harvey (harvey.ai) | Series E | $300M ⚠ check sentence | kleiner perkins, coatue, sequoia | USA | Harvey, the legal AI platform used by law firms and corporate legal teams worldwide, has raised $300 million in a Series E funding round,… |
| 24 Sep 2025 | Modular (modular.com) | — | $250M | U.S. Innovative Technology Fund, dfj growth, GV | United States | AI startup Modular said on Wednesday it raised $250 million in a funding round valuing it at $1.6 billion. |
| 16 Sep 2025 | Nothing (nothing.tech) | — | $200M | tiger global, GV, highland europe | UK | Nothing has recently secured $200 million in a funding round led by Tiger Global, valuing the company at $1.3 billion, according to a… |
| 3 Sep 2025 | Treeline Biosciences (treeline.bio) | Growth | $200M | arch venture partners, orbimed, GV | USA | Treeline Biosciences, a secretive biotech startup co‑founded by Loxo Oncology’s Josh Bilenker and former Novartis oncology head Jeff… |
| 11 Mar 2026 | Armadin | Combined Seed and Series A | $189.9M | accel, GV, kleiner perkins | — | Kevin Mandia has launched a new cybersecurity company, Armadin, with $189.9 million in combined seed and Series A funding. |
| 24 Apr 2026 | Omni Analytics, Inc. | Series C | $120M ⚠ check sentence | iconiq, Theory Ventures, first round capital | United States | Omni, a San Francisco, CA–based AI analytics platform, has raised $120 million in Series C funding at a $1.5 billion valuation. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 24 Apr 2026 | Omni Analytics, Inc. | Series C | $120M ⚠ check sentence | iconiq, Theory Ventures, first round capital | United States | Omni, a San Francisco, CA–based AI analytics platform, has raised $120 million in Series C funding at a $1.5 billion valuation. |
| 23 Apr 2026 | Omni (exploreomni.com) | Series C | $120M | iconiq, Theory Ventures, first round capital | — | Omni raises $120M Series C for enterprise AI analytics |
| 20 Apr 2026 | Recursive Superintelligence | Private round | $500M | GV, nvidia | — | Recursive Superintelligence raised $500M+ private round for self‑improving AI systems. |
| 16 Apr 2026 | Wealth.com | Series B | $65M | charles schwab, titanium ventures, pruven capital | — | Wealth.com Raises $65M Series B for AI-Powered Estate and Tax Planning. |
| 7 Apr 2026 | Censys (censys.com) | Series D | $70M | morgan stanley expansion capital, decibel partners,… | — | Censys, the internet intelligence and insights platform, has raised $70m in a combined funding round to accelerate the development of its… |
| 6 Apr 2026 | BeastLife (beastlife.in) | pre-Series A | $240k ⚠ check sentence | GVFL, Equentis | India | D2C nutrition company BeastLife has raised Rs 20 crore from GVFL and Equentis in a pre-Series A funding round valued at Rs 320 crore. |
| 1 Apr 2026 | Censys (censys.com) | Series D equity | $40M | morgan stanley expansion capital, decibel partners,… | — | The financing includes a $40 million Series D equity round alongside $30 million in debt financing. |
| 24 Mar 2026 | SambaNova | Series E | $1.5B | battery ventures, cambium capital partners, first data | USA |  |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor GV --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor GV --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor GV --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "GV", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "GV", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Investor names match broadly (a name can match several firms or funds); use a domain for a narrower match.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Y Combinator Portfolio](y-combinator-portfolio.md)
- [First Round Capital Portfolio](first-round-capital-portfolio.md)
- [Intel Capital Portfolio](intel-capital-portfolio.md)
- [Prosus Investments](prosus-investments.md)
