# Breakthrough Energy Ventures Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “breakthrough energy ventures portfolio” · 10/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [breakthrough-energy-ventures-portfolio.json](../../examples/scenarios/breakthrough-energy-ventures-portfolio.json).

**Question.** Which rounds did Breakthrough Energy Ventures appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Breakthrough Energy Ventures”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 19 |
| With a usable reported amount | 19 |
| Reported total (usable amounts) | $5.6B |
| Median reported round | $122M |
| Largest reported round | $3B |
| Busiest month | Apr 2026 (5 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1 | 1 | $38M | $38M | ████ |
| Jun 2025 | 0 | 0 | — | — |  |
| Jul 2025 | 1 | 1 | $44M | $44M | ████ |
| Aug 2025 | 2 | 2 | $875M | $437.5M | ████████ |
| Sep 2025 | 2 | 2 | $3B | $1.5B | ████████ |
| Oct 2025 | 2 | 2 | $543M | $271.5M | ████████ |
| Nov 2025 | 0 | 0 | — | — |  |
| Dec 2025 | 4 | 4 | $612M | $306M | ████████████████ |
| Jan 2026 | 0 | 0 | — | — |  |
| Feb 2026 | 2 | 2 | $140M | $140M | ████████ |
| Mar 2026 | 0 | 0 | — | — |  |
| Apr 2026 | 5 | 5 | $349M | $105M | ████████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 9 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 10 Sep 2025 | Commonwealth Fusion Systems (cfs.energy) | — | $3B | Bill Gates, breakthrough energy ventures | USA | CFS has raised nearly $3 billion, including an $863 million round that closed in August. Gates and Breakthrough Energy Ventures lead an… |
| 8 Oct 2025 | Stoke Space Technologies (stoke-space.com) | Series D | $510M | US Innovative Technology Fund, washington harbour… | USA | Stoke Space landed $510M Series D to accelerate reusable rockets. |
| 15 Dec 2025 | Fervo Energy (fervoenergy.com) | total equity funding | $462M | alliancebernstein, atacama ventures, b capital | USA | Fervo Energy has now raised a total of $1.1B in total equity funding and is backed by AllianceBernstein, Atacama Ventures, B Capital,… |
| 23 Dec 2025 | Zeroavia (zeroavia.com) | Series D | $150M | Barclays Climate Ventures, breakthrough energy ventures,… | — | ZeroAvia, an electric aviation startup developing hydrogen fuel‑cell engines, announced additional funding led by climate‑focused… |
| 18 Feb 2026 | Heron Power | Series B | $140M | Andreessen Horowitz’s American Dynamism Fund, breakthrough… | United States | On Wednesday, solid‑state transformer startup Heron Power closed a $140 million Series B round from investors including Andreessen… |
| 23 Apr 2026 | Sygaldry Technologies | Series A and Seed | $139M | earth venture capital, initialized capital, breakthrough… | US | Earth Venture Capital, a decarbonization-focused climate tech venture capital firm based in Singapore, has announced its involvement in… |
| 17 Jul 2025 | Geologicai (geologicai.com) | Series B | $44M | blue earth capital, BHP Ventures, rio tinto | Canada | Calgary-based mining tech startup GeologicAI has secured $44 million USD ($60.5 million CAD) in Series B funding as the intense demand for… |
| 15 Oct 2025 | Savor (savor.co) | — | $33M | breakthrough energy ventures, synthesis capital | United States | With financial support from Breakthrough Energy Ventures, a capital fund led by Bill Gates, and Synthesis Capital, Savor, a foodtech… |
| 17 Sep 2025 | Na | — | $15M | breakthrough energy ventures, british airways, american… | — | Breakthrough Energy Ventures and about 10 carriers are committing $150 million to support early-stage SAF startups moving through the… |
| 18 Aug 2025 | Planted Solar (plantedsolar.com) | — | $12M | piva capital, breakthrough energy ventures, khosla ventures | United States | Planted Solar, the solar deployment platform helping project developers build faster, smarter, and more profitably, today announced a $12… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 23 Apr 2026 | Sygaldry Technologies | Series A and Seed | $139M | earth venture capital, initialized capital, breakthrough… | US | Earth Venture Capital, a decarbonization-focused climate tech venture capital firm based in Singapore, has announced its involvement in… |
| 16 Apr 2026 | Sygaldry Technologies | Series A | $105M | breakthrough energy ventures, y combinator, Rock Yard… | United States | Sygaldry Technologies has raised $105M in a Series A led by Breakthrough Energy Ventures, following a $34M seed from Initialized Capital. |
| 14 Apr 2026 | Sygaldry Technologies, Inc. | Series A | $105M | breakthrough energy ventures, y combinator, Rock Yard… | USA | Sygaldry Technologies, Inc., an Ann Arbor, MI provider of quantum-accelerated AI servers raised $105M in Series A funding. |
| 18 Feb 2026 | Heron Power | Series B | $140M | Andreessen Horowitz’s American Dynamism Fund, breakthrough… | United States | On Wednesday, solid‑state transformer startup Heron Power closed a $140 million Series B round from investors including Andreessen… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "Breakthrough Energy Ventures" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "Breakthrough Energy Ventures" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "Breakthrough Energy Ventures" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Breakthrough Energy Ventures", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Breakthrough Energy Ventures", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Intel Capital Portfolio](intel-capital-portfolio.md)
- [Prosus Investments](prosus-investments.md)
- [Index Ventures Portfolio](index-ventures-portfolio.md)
- [Redpoint Investments](redpoint-investments.md)
