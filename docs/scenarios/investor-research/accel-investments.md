# Accel Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “accel investments” · 260/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [accel-investments.json](../../examples/scenarios/accel-investments.json).

**Question.** Which rounds did Accel appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Accel”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 506 |
| With a usable reported amount | 460 |
| Reported total (usable amounts) | $33.1B |
| Median reported round | $17M |
| Largest reported round | $2.3B |
| Amounts left out as implausible or unconverted | 2 |
| Busiest month | Mar 2026 (63 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 35 | 33 | $3.8B | $26.5M | ███████████ |
| Jun 2025 | 37 | 36 | $3.1B | $18.6M | ████████████ |
| Jul 2025 | 32 | 28 | $4.9B | $10M | ██████████ |
| Aug 2025 | 30 | 25 | $1.6B | $11M | ██████████ |
| Sep 2025 | 62 | 59 | $2.3B | $17.6M | ████████████████████ |
| Oct 2025 | 57 | 55 | $2.2B | $16M | ██████████████████ |
| Nov 2025 | 33 | 31 | $6B | $12.5M | ██████████ |
| Dec 2025 | 26 | 22 | $2.8B | $58.9M | ████████ |
| Jan 2026 | 45 | 41 | $1.1B | $14M | ██████████████ |
| Feb 2026 | 52 | 46 | $1.6B | $11M | █████████████████ |
| Mar 2026 | 63 | 54 | $3.4B | $34M | ████████████████████ |
| Apr 2026 | 34 | 30 | $3.4B | $14.5M | ███████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 23 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 14 Nov 2025 | Anysphere (anysphere.inc) | Series D | $2.3B | accel, coatue, nvidia | United States | AI coding startup Anysphere completed a $2.3 billion Series D funding round on Thursday, valuing the company at $29.3 billion. Accel and… |
| 13 Nov 2025 | Cursor (cursor.com) | Series D | $2.3B ⚠ check sentence | accel, coatue, Andreessen Horowitz | United States | Cursor has vaulted into the top tier of private AI companies after securing a massive $2.3 billion Series D at a $29.3 billion valuation. |
| 15 Jul 2025 | Thinking Machines Lab | Series A | $2B | Andreessen Horowitz, nvidia, accel | — | Thinking Machines Lab has raised an unprecedented $2 billion early-stage funding round led by Andreessen Horowitz. |
| 6 Apr 2026 | Helsing (helsing.ai) | — | $1.5B ⚠ check sentence | general catalyst, accel, saab | Germany | Helsing has raised over €1.4 billion, achieving unicorn-plus status with a valuation around €3-4 billion in recent rounds backed by… |
| 18 Dec 2025 | Trade Republic (traderepublic.com) | secondary | $1.3B ⚠ check sentence | founders fund, wellington management, gic | Germany | Berlin, 17. December 2025 (PM) – YPOG has provided comprehensive legal advice to Trade Republic Bank GmbH in the context of a secondary… |
| 28 Apr 2026 | True Anomaly (trueanomaly.space) | Series D | $650M | eclipse, riot ventures, paradigm | USA | True Anomaly today announced its $650 million Series D funding round. |
| 7 May 2025 | Wonder (wonder.com) | Series (?) | $600M | new enterprise associates, accel, google ventures | USA | Lore in a LinkedIn post Tuesday said there was participation from major existing shareholders, led by New Enterprise Associates, Accel,… |
| 10 Mar 2026 | Legora | Series D | $550M | accel, benchmark, bessemer venture partners | Sweden | Legora Raises $550M in Series D Funding to Expand AI in Legal Operations |
| 12 Jun 2025 | Cyera (cyera.io) | Series E | $540M | georgian, greenoaks, lightspeed venture partners | — | Cyera, which helps enterprises protect sensitive information while adopting artificial intelligence, has secured $540m in a Series E… |
| 14 Nov 2025 | Chaos Industries (getchaos.com) | — | $510M | valor equity partners, 8vc, accel | USA | CHAOS Industries has raised $510 million in new funding to expand development and manufacturing of its sensing and timing technologies for… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Dreamteam (dreamteam.gg) | Series A | $40M | accel, Together Fund | India | Chennai-based AI startup Dreamteam is in advanced discussions to raise around $40 million in its Series A funding round, with Accel and… |
| 30 Apr 2026 | Ctruh (ctruh.com) | Seed | $2.5M | inflection point ventures, Avinya Ventures, india… | India | Ctruh, the deep-tech company building the infrastructure layer for the spatial internet, has raised $2.5 Million in a Seed funding round… |
| 30 Apr 2026 | Oolka (oolka.in) | Series A | $14M | accel, lightspeed, Z47 | India | Oolka has raised $14 million in a Series A funding round led by Accel, with participation from existing investors Lightspeed and Z47. |
| 29 Apr 2026 | Sahi (sahi.com.tr) | Series B | $33M | accel, elevation capital, others | India | Sahi Raises $33 Mn Series B |
| 28 Apr 2026 | True Anomaly (trueanomaly.space) | Series D | $650M | eclipse, riot ventures, paradigm | USA | True Anomaly today announced its $650 million Series D funding round. |
| 24 Apr 2026 | PvX Partners | Series A | $10.5M | T-Accelerate Capital, Z Venture Capital, drive by draftkings | — | PvX Partners has raised $10.5 million in a Series A round as the firm scales its cohort-based financing model for consumer apps. |
| 23 Apr 2026 | Astor (astorim.com) | seed | $5M | monashees, goodwater, Y Combinator accelerator | US | Astor, a startup founded by two Brazilians in the United States, has just lifted a $5 million seed round led by Monashees. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Accel --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Accel --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Accel --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Accel", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Accel", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Sequoia Investments](sequoia-investments.md)
- [Thrive Capital Portfolio](thrive-capital-portfolio.md)
- [TPG Portfolio](tpg-portfolio.md)
- [A16Z Portfolio](a16z-portfolio.md)
