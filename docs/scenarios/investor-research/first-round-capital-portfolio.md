# First Round Capital Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “first round capital portfolio” · 10/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [first-round-capital-portfolio.json](../../examples/scenarios/first-round-capital-portfolio.json).

**Question.** Which rounds did First Round Capital appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “First Round Capital”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 69 |
| With a usable reported amount | 66 |
| Reported total (usable amounts) | $2B |
| Median reported round | $44.5M |
| Largest reported round | $200M |
| Busiest month | Apr 2026 (24 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 5 | 4 | $250M | $25M | ████ |
| Jun 2025 | 7 | 6 | $96.5M | $10M | ██████ |
| Jul 2025 | 2 | 2 | $50M | $50M | ██ |
| Aug 2025 | 8 | 7 | $273.6M | $30M | ███████ |
| Sep 2025 | 6 | 6 | $336M | $75M | █████ |
| Oct 2025 | 7 | 7 | $265M | $50M | ██████ |
| Nov 2025 | 0 | 0 | — | — |  |
| Dec 2025 | 0 | 0 | — | — |  |
| Jan 2026 | 0 | 0 | — | — |  |
| Feb 2026 | 4 | 4 | $89M | $29M | ███ |
| Mar 2026 | 6 | 6 | $71M | $35.5M | █████ |
| Apr 2026 | 24 | 24 | $656.7M | $44M | ████████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 21 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 2 May 2025 | Persona (withpersona.com) | Series D | $200M ⚠ check sentence | founders fund, ribbit capital, bond | USA | Persona, a verified identity platform based in San Francisco, has raised $200m in Series D funding, pushing its valuation to $2bn. |
| 1 Aug 2025 | Fal (fal.ai) | Series C | $125M ⚠ check sentence | meritech capital partners, salesforce ventures, Shopify… | United States | fal, a San Francisco, CA-based AI infrastructure company, has raised $125 million in Series C funding, bringing its valuation to $1.5… |
| 27 Apr 2026 | Omni (exploreomni.com) | — | $120M | first round capital, google ventures, iconiq growth | US | San Francisco-based Omni provides a data collaboration and analytics platform that allows teams to explore, model, and share business data… |
| 15 Sep 2025 | Dyna Robotics | Series A | $120M | Robostrategy, crv, first round capital | United States | Dyna Robotics today announced it has closed a $120 million Series A funding round, led by Robostrategy, CRV, and First Round Capital, with… |
| 5 Aug 2025 | Clay (clay.com) | Series C | $100M ⚠ check sentence | capitalg, Meritech Capital, sequoia capital | USA | Clay, a New York-based startup building an AI-powered sales automation platform, has raised $100 million in a Series C round at a $3.1… |
| 10 Jun 2025 | Prepared (prepared911.com) | Series C | $80M | general catalyst, Andreessen Horowitz, first round capital | USA | Prepared, a provider of an assistive AI platform for emergency response, has secured $80 million in a Series C funding round. |
| 2 Oct 2025 | Assort Health (assorthealth.com) | Series B | $76M | lightspeed venture partners, felicis, first round capital | United States | Assort Health, a Palo Alto startup automating healthcare call centers with voice AI, has raised $76 million in a Series B financing |
| 15 Oct 2025 | Reducto | Series B | $75M ⚠ check sentence | Andreessen Horowitz, benchmark, first round capital | USA | Reducto, a San Francisco, CA-based AI document intelligence platform, has raised $75 million in Series B funding, bringing its total… |
| 17 Sep 2025 | Omnea (omnea.co) | Series B | $75M ⚠ check sentence | insight partners, khosla ventures, accel | UK | Omnea, a leading AI-native procurement intake and orchestration platform, has raised $50M in Series B funding to accelerate its shift to a… |
| 15 Apr 2026 | Artemis (artemislp.com) | Series A | $70M | felicis, first round capital, brightmind | — | Artemis Raises $70M in Series A Funding for AI-native security operations and automated response |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Parallel Web Systems | Series B | $10M ⚠ check sentence | sequoia capital, kleiner perkins, index ventures | — | Former Twitter (now X) CEO Parag Agrawal’s AI agentic platform Parallel Web Systems has raised a $100 million Series B at a $2 billion… |
| 29 Apr 2026 | Actively AI | Series B | $45M | tcv, First Harmonic, bain capital ventures | — | Actively AI Raises $45M Series B to Expand AI Go-To-Market Platform |
| 28 Apr 2026 | Manifest OS | Series A | $60M ⚠ check sentence | menlo ventures, kleiner perkins, first round capital | United States | Manifest OS has secured a $60 million Series A round (at a $750 million valuation) to further develop its AI-driven software for the legal… |
| 28 Apr 2026 | Actively (actively.ai) | Series B | $45M ⚠ check sentence | tcv, First Harmonic, bain capital ventures | United States | The round, co-led by TCV and First Harmonic, with backing from Bain Capital Ventures, First Round Capital, and Alkeon, brings total… |
| 27 Apr 2026 | Omni (exploreomni.com) | — | $120M | first round capital, google ventures, iconiq growth | US | San Francisco-based Omni provides a data collaboration and analytics platform that allows teams to explore, model, and share business data… |
| 24 Apr 2026 | Petual | Funding | $20M | Andreessen Horowitz, first round capital, cowboy ventures | — | Petual raises $20m for AI-powered SOX compliance Petual, an AI-powered audit and compliance platform, has secured $20m in funding to… |
| 24 Apr 2026 | Omni Analytics, Inc. | Series C | $120M ⚠ check sentence | iconiq, Theory Ventures, first round capital | United States | Omni, a San Francisco, CA–based AI analytics platform, has raised $120 million in Series C funding at a $1.5 billion valuation. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "First Round Capital" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "First Round Capital" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "First Round Capital" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "First Round Capital", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "First Round Capital", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Lux Capital Portfolio](lux-capital-portfolio.md)
- [Y Combinator Portfolio](y-combinator-portfolio.md)
- [GV Investments](gv-investments.md)
- [Intel Capital Portfolio](intel-capital-portfolio.md)
