# General Catalyst Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “general catalyst portfolio” · 40/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [general-catalyst-portfolio.json](../../examples/scenarios/general-catalyst-portfolio.json).

**Question.** Which rounds did General Catalyst appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “General Catalyst”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 372 |
| With a usable reported amount | 353 |
| Reported total (usable amounts) | $48.4B |
| Median reported round | $47M |
| Largest reported round | $13B |
| Amounts left out as implausible or unconverted | 2 |
| Busiest month | Mar 2026 (46 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 37 | 37 | $5.2B | $99.9M | ████████████████ |
| Jun 2025 | 43 | 40 | $4B | $90M | ███████████████████ |
| Jul 2025 | 23 | 21 | $2.2B | $90.7M | ██████████ |
| Aug 2025 | 30 | 27 | $382.5M | $20M | █████████████ |
| Sep 2025 | 30 | 29 | $20.7B | $55M | █████████████ |
| Oct 2025 | 40 | 40 | $7.1B | $80M | █████████████████ |
| Nov 2025 | 22 | 22 | $1.6B | $25M | ██████████ |
| Dec 2025 | 32 | 29 | $1.7B | $40M | ██████████████ |
| Jan 2026 | 17 | 17 | $2.1B | $78M | ███████ |
| Feb 2026 | 31 | 29 | $781.6M | $34M | █████████████ |
| Mar 2026 | 46 | 43 | $2.6B | $40M | ████████████████████ |
| Apr 2026 | 21 | 19 | $2.8B | $38M | █████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 25 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 3 Sep 2025 | Anthropic (anthropic.com) | Series | $13B | iconiq, Fidelity Management & Research, lightspeed venture… | — | The funding round was led by Iconiq, Fidelity Management & Research, and Lightspeed Venture Partners. Heavyweights like Altimeter, General… |
| 4 Sep 2025 | Mistral AI (mistral.ai) | Late‑stage (unconfirmed) | $2.2B | Andreessen Horowitz, general catalyst, (New investors not… | France | Paris‑based Mistral AI is reportedly in the final stages of securing a colossal €2 billion (~$2.2 billion) funding round that would value… |
| 6 Apr 2026 | Helsing (helsing.ai) | — | $1.5B ⚠ check sentence | general catalyst, accel, saab | Germany | Helsing has raised over €1.4 billion, achieving unicorn-plus status with a valuation around €3-4 billion in recent rounds backed by… |
| 29 May 2025 | Grammarly (grammarly.com) | Funding round (non-dilutive) | $1.4B | general catalyst | USA | San Francisco-based Grammarly (AI writing assistant) secured $1.0 billion in funding from its long-time investor General Catalyst. |
| 20 May 2025 | Slate Auto | — | $700M | bezos expeditions, general catalyst, TWG Global | USA | Slate has already raised $700 million in financing. |
| 18 Jun 2025 | Applied Intuition (appliedintuition.com) | Series F | $600M ⚠ check sentence | BlackRock-managed funds and accounts, kleiner perkins,… | United States | Applied Intuition, Inc., the leading vehicle intelligence company for automotive, trucking, construction, mining, agriculture, and… |
| 10 Mar 2026 | Legora | Series D | $550M | accel, benchmark, bessemer venture partners | Sweden | Legora Raises $550M in Series D Funding to Expand AI in Legal Operations |
| 29 Jul 2025 | Zepto (zepto.com.au) | — | $500M | general catalyst, Avenir Growth | India | The 4-year-old startup is also in the process of raising $500 million round in a mix of primary and secondary transactions. The round will… |
| 2 Nov 2025 | Mercor (mercor.com) | total equity funding | $483.6M | benchmark, felicis, general catalyst | United States | Mercor has now raised a total of $483.6M in total equity funding and is backed by Benchmark, Felicis, General Catalyst, and Robinhood… |
| 22 Jan 2026 | Humans (humans.uz) | — | $480M ⚠ check sentence | sequoia capital, general catalyst, softbank vision fund | — | AI startup Humans raised $480 million in a funding round at a $4.5 billion valuation led by Andreessen Horowitz and co‑led by Sequoia… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Aidoc (aidoc.com) | Series E | $150M | Goldman Sachs Growth Equity, general catalyst, softbank… | — | Aidoc Raises $150M Series E for Clinical AI Scaling |
| 27 Apr 2026 | Avoca (avoca.com) | Series B | — | meritech, general catalyst | — | The Series B funding was led by Meritech and General Catalyst. |
| 24 Apr 2026 | PvX Partners | Series A | $10.5M | T-Accelerate Capital, Z Venture Capital, drive by draftkings | — | PvX Partners has raised $10.5 million in a Series A round as the firm scales its cohort-based financing model for consumer apps. |
| 23 Apr 2026 | Shade (wearshade.com) | Venture Round | $14M | khosla ventures, construct capital, bling capital | — | Shade Raises $14M Venture Round for AI Media Search |
| 23 Apr 2026 | Almanac Health | seed | $10M | general catalyst, lightspeed venture partners | USA | Almanac Health has raised $10 million in a seed round led by F-Prime, with participation from General Catalyst and Lightspeed Venture… |
| 16 Apr 2026 | Native (native.io) | Series A | $42M | Ballistic Ventures, general catalyst, yl ventures | USA | Native emerges from stealth with $42m ... The company’s $31m Series A was led by Ballistic Ventures, with continued participation from… |
| 14 Apr 2026 | Slate Auto | Series B | $590M | TWG Global, Jeff Bezos’s family office, general catalyst | — | They also led the company’s earlier $590 million Series B round, reports Bloomberg. |
| 10 Apr 2026 | Louden Richason | Series A | $35M | general catalyst, chemistry | United States | New York based health insurance administration platform raised $35m in Series A funding led by General Catalyst and Chemistry. |
| 9 Apr 2026 | Luminai (luminai.com) | Series B | $38M | peak xv partners, define ventures, general catalyst | United States | Luminai, an AI-native automation platform tailored for the healthcare sector, has secured $38 million in a Series B funding round to scale… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "General Catalyst" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "General Catalyst" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "General Catalyst" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "General Catalyst", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "General Catalyst", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Khosla Ventures Portfolio](khosla-ventures-portfolio.md)
- [Coatue Investments](coatue-investments.md)
- [Andreessen Horowitz Portfolio](andreessen-horowitz-portfolio.md)
- [Temasek Portfolio](temasek-portfolio.md)
