# Khosla Ventures Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “khosla ventures portfolio” · 50/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [khosla-ventures-portfolio.json](../../examples/scenarios/khosla-ventures-portfolio.json).

**Question.** Which rounds did Khosla Ventures appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Khosla Ventures”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 233 |
| With a usable reported amount | 222 |
| Reported total (usable amounts) | $17.6B |
| Median reported round | $42M |
| Largest reported round | $1.5B |
| Amounts left out as implausible or unconverted | 1 |
| Busiest month | Apr 2026 (30 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 18 | 18 | $864M | $33M | ████████████ |
| Jun 2025 | 18 | 15 | $860.4M | $40M | ████████████ |
| Jul 2025 | 11 | 10 | $750.9M | $105M | ███████ |
| Aug 2025 | 24 | 22 | $2.7B | $35.5M | ████████████████ |
| Sep 2025 | 22 | 22 | $842M | $60M | ███████████████ |
| Oct 2025 | 18 | 18 | $907.9M | $25.2M | ████████████ |
| Nov 2025 | 20 | 20 | $779.5M | $35M | █████████████ |
| Dec 2025 | 20 | 19 | $2.3B | $70M | █████████████ |
| Jan 2026 | 21 | 21 | $3.6B | $70M | ██████████████ |
| Feb 2026 | 14 | 13 | $1.2B | $35M | █████████ |
| Mar 2026 | 17 | 16 | $1.3B | $40.5M | ███████████ |
| Apr 2026 | 30 | 28 | $2.8B | $100M | ████████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 25 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 22 Apr 2026 | Factory (factory.com) | Series C | $1.5B ⚠ check sentence | khosla ventures, sequoia capital, blackstone | — | Factory announced it has raised $150 million in a Series C funding round led by Khosla Ventures, with participation from Sequoia Capital,… |
| 18 Dec 2025 | Trade Republic (traderepublic.com) | secondary | $1.3B ⚠ check sentence | founders fund, wellington management, gic | Germany | Berlin, 17. December 2025 (PM) – YPOG has provided comprehensive legal advice to Trade Republic Bank GmbH in the context of a secondary… |
| 28 Jan 2026 | Waabi Innovation Inc. | Series C | $1B | khosla ventures, G2 Venture Partners, uber | Canada | Waabi Innovation Inc., a Canadian startup that develops self-driving technology for trucks, has secured $1 billion in funding for its… |
| 28 Aug 2025 | Commonwealth Fusion Systems (cfs.energy) | Funding Round (private) | $863M | nvidia, google, breakthrough energy ventures | USA | Commonwealth Fusion Systems (CFS), a Massachusetts-based nuclear fusion startup, closed an $863 million funding round. |
| 15 Aug 2025 | Cognition (cognition.ai) | — | $500M | Peter Thiel’s Founders Fund, khosla ventures, pear vc | — | Now the Wall Street Journal (WSJ) is reporting that a new round led by Founders Fund sees Cognition raise $500m toward that goal. |
| 11 Mar 2026 | Rhoda AI | Series A | $450M | khosla ventures, temasek, mayfield | United States | Rhoda AI raises $450M Series A to advance real-world robotics intelligence. |
| 27 Aug 2025 | FieldAI | Series C | $405M | nventures, bezos expeditions, khosla ventures | — | FieldAI, a robotics software startup backed by Nvidia, Bezos Expeditions, and Bill Gates’s foundation, announced a massive $405 million… |
| 21 Aug 2025 | Field AI (fieldai.com) | — | $405M | nventures, bezos expeditions, khosla ventures | USA | Field AI, a robotics startup backed by Bill Gates, has raised $405 million across two funding rounds, attracting investments from Nvidia’s… |
| 17 Jan 2026 | Clickhouse (clickhouse.com) | Series D | $400M | bessemer venture partners, gic, index ventures | United States | ClickHouse Inc. has raised $400 million in a Series D round led by Dragoneer Investment Group, marking one of the largest funding rounds… |
| 7 Apr 2026 | Hermeus (hermeus.com) | Series D | $350M | khosla ventures, founders fund, canaan | United States | Hermeus, an Atlanta‑area defense startup developing autonomous hypersonic aircraft, closed a $350 million funding round. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Parallel Web Systems | Series B | $10M ⚠ check sentence | sequoia capital, kleiner perkins, index ventures | — | Former Twitter (now X) CEO Parag Agrawal’s AI agentic platform Parallel Web Systems has raised a $100 million Series B at a $2 billion… |
| 29 Apr 2026 | Rogo (rogodata.com) | Series D | $160M | kleiner perkins, sequoia capital, thrive | USA | Rogo Raises $160M in Series D Funding for Finance AI Platform |
| 29 Apr 2026 | Parallel Web Systems | Series B | $100M ⚠ check sentence | sequoia capital, kleiner perkins, index ventures | United States | Parallel Web Systems, a startup founded by former Twitter CEO Parag Agrawal, has raised $100 million in a Series B funding round led by… |
| 27 Apr 2026 | Shade (wearshade.com) | — | $14M | bling capital, construct capital, khosla ventures | US | New York-based Shade develops a private AI-driven file explorer that visually searches and previews terabytes of files. |
| 24 Apr 2026 | Grai (grai.io) | Seed | $9M | khosla ventures, Polish Inovo VC, Tensor Ventures | Poland | Polish-based GRAI has secured $9 (€7.65) million in seed funding in a round co-led by Khosla Ventures and Polish Inovo VC, as the startup… |
| 22 Apr 2026 | Factory (factory.com) | Series C | $1.5B ⚠ check sentence | khosla ventures, sequoia capital, blackstone | — | Factory announced it has raised $150 million in a Series C funding round led by Khosla Ventures, with participation from Sequoia Capital,… |
| 20 Apr 2026 | Factory (factory.com) | Series C | $150M | khosla ventures, sequoia capital, blackstone | — | Factory, an autonomous software engineering platform used by enterprises including Nvidia, Adobe and Adyen, raised $150 million in a… |
| 18 Apr 2026 | Slash (joinslash.com) | — | $100M | goodwater capital, khosla ventures, new enterprise… | United States | Slash has now raised a total of $160M in total equity funding and is backed by Goodwater Capital, Khosla Ventures, New Enterprise… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "Khosla Ventures" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "Khosla Ventures" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "Khosla Ventures" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Khosla Ventures", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Khosla Ventures", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Insight Partners Portfolio](insight-partners-portfolio.md)
- [Lightspeed Investments](lightspeed-investments.md)
- [Coatue Investments](coatue-investments.md)
- [General Catalyst Portfolio](general-catalyst-portfolio.md)
