# Index Ventures Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “index ventures portfolio” · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [index-ventures-portfolio.json](../../examples/scenarios/index-ventures-portfolio.json).

**Question.** Which rounds did Index Ventures appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Index Ventures”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 134 |
| With a usable reported amount | 132 |
| Reported total (usable amounts) | $12.8B |
| Median reported round | $50M |
| Largest reported round | $2B |
| Busiest month | May 2025 (18 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 18 | 18 | $1B | $45M | ████████████████████ |
| Jun 2025 | 11 | 10 | $300.9M | $25M | ████████████ |
| Jul 2025 | 15 | 15 | $398.4M | $22M | █████████████████ |
| Aug 2025 | 4 | 4 | $393.8M | $65M | ████ |
| Sep 2025 | 3 | 3 | $3.8B | $1.8B | ███ |
| Oct 2025 | 12 | 12 | $999.8M | $100M | █████████████ |
| Nov 2025 | 14 | 14 | $1.7B | $100M | ████████████████ |
| Dec 2025 | 11 | 11 | $374.8M | $28.3M | ████████████ |
| Jan 2026 | 7 | 7 | $790M | $100M | ████████ |
| Feb 2026 | 13 | 13 | $1.4B | $92.5M | ██████████████ |
| Mar 2026 | 15 | 14 | $1.1B | $35M | █████████████████ |
| Apr 2026 | 11 | 11 | $1.7B | $85.8M | ████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 20 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 16 Sep 2025 | Mistral AI (mistral.ai) | Series C | $2B ⚠ check sentence | ASML Holding NV, dst global, Andreessen Horowitz | — | French startup Mistral AI has secured USD 2bn (EUR 1.7bn) in a Series C round, bringing its valuation to USD 13.8bn, the company announced… |
| 27 Apr 2026 | Ineffable Intelligence | — | $1.1B ⚠ check sentence | sequoia capital, lightspeed venture partners, nvidia | United Kingdom | David Silver has raised $1.1bn (£880m) for his London-based startup Ineffable Intelligence at a valuation of $5.1bn, in a round led by… |
| 24 Mar 2026 | Temporal Technologies (temporal.io) | Series D | $649.5M | amplify partners, Andreessen Horowitz, gic | USA |  |
| 23 Nov 2025 | Physical Intelligence (physicalintelligence.company) | — | $600M | capitalg, index ventures, Jeff Bezos | United States | Physical Intelligence has now raised a total of $1.1B in total equity funding and is backed by CapitalG, Index Ventures, Jeff Bezos, Lux… |
| 17 Jan 2026 | Clickhouse (clickhouse.com) | Series D | $400M | bessemer venture partners, gic, index ventures | United States | ClickHouse Inc. has raised $400 million in a Series D round led by Dragoneer Investment Group, marking one of the largest funding rounds… |
| 2 Nov 2025 | Fireworks AI | total equity funding | $307M | Evantic Capital, index ventures, lightspeed venture partners | United States | Fireworks AI has now raised a total of $307.0M in total equity funding and is backed by Evantic Capital, Index Ventures, Lightspeed… |
| 2 Feb 2026 | Decagon (decagon.ai) | — | $250M | accel, Andreessen Horowitz, avra | — | Decagon – $250.0M |
| 2 Nov 2025 | Sublime Security (sublime.security) | total equity funding | $239.8M | 01 Advisors, avenir, citi ventures | United States | Sublime Security has now raised a total of $239.8M in total equity funding and is backed by 01 Advisors, Avenir, Citi Ventures, Georgian,… |
| 18 Jun 2025 | Persona (withpersona.com) | Series D | $200M | founders fund, ribbit capital, bond | USA | U.S.-based identity verification start-up Persona announced in mid-June 2025 that it had raised $200 million in a Series D funding round… |
| 10 Feb 2026 | Flapping Airplanes | seed | $180M | sequoia, google ventures, index ventures | — | A revolutionary AI lab called Flapping Airplanes has raised $180 million in seed funding from top investors including Sequoia, Google… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Parallel Web Systems | Series B | $10M ⚠ check sentence | sequoia capital, kleiner perkins, index ventures | — | Former Twitter (now X) CEO Parag Agrawal’s AI agentic platform Parallel Web Systems has raised a $100 million Series B at a $2 billion… |
| 29 Apr 2026 | Parallel Web Systems | Series B | $100M ⚠ check sentence | sequoia capital, kleiner perkins, index ventures | United States | Parallel Web Systems, a startup founded by former Twitter CEO Parag Agrawal, has raised $100 million in a Series B funding round led by… |
| 27 Apr 2026 | Ineffable Intelligence | — | $1.1B ⚠ check sentence | sequoia capital, lightspeed venture partners, nvidia | United Kingdom | David Silver has raised $1.1bn (£880m) for his London-based startup Ineffable Intelligence at a valuation of $5.1bn, in a round led by… |
| 20 Apr 2026 | Loop (loopstore.com) | Series C | $95M | valor equity partners, Valor Atreides AI Fund, 8vc | United States | Loop, a San Francisco, CA–based full-stack, verticalized AI platform for logistics and supply chains, has raised $95 million in Series C… |
| 13 Apr 2026 | Crosby (crosbytech.io) | Series B | $60M | 01 Advisors, bain capital ventures, Elad Gil | — |  |
| 13 Apr 2026 | Alan (alan.com) | — | $116M | index ventures, greenoaks, Kaaf | — | The round was led by existing investor Index Ventures, with new investors Greenoaks, Kaaf, and SH also participating, alongside business… |
| 6 Apr 2026 | Linx Security (linx.security) | total equity | $83M | cyberstarts, index ventures, insight partners | United States | Linx Security has now raised a total of $83M in total equity funding and is backed by Cyberstarts, Index Ventures, and Insight Partners. |
| 6 Apr 2026 | Crosby (crosbytech.io) | total equity | $85.8M | 01 Advisors, bain capital ventures, Elad Gil | United States | Crosby has now raised a total of $85.8M in total equity funding and is backed by 01 Advisors, Bain Capital Ventures, Elad Gil, Index… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "Index Ventures" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "Index Ventures" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "Index Ventures" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Index Ventures", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Index Ventures", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Prosus Investments](prosus-investments.md)
- [Breakthrough Energy Ventures Portfolio](breakthrough-energy-ventures-portfolio.md)
- [Redpoint Investments](redpoint-investments.md)
- [Spark Capital Investments](spark-capital-investments.md)
