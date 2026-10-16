# Founders Fund Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “founders fund portfolio” · 20/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [founders-fund-portfolio.json](../../examples/scenarios/founders-fund-portfolio.json).

**Question.** Which rounds did Founders Fund appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Founders Fund”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 200 |
| With a usable reported amount | 183 |
| Reported total (usable amounts) | $29.7B |
| Median reported round | $46M |
| Largest reported round | $8.3B |
| Amounts left out as implausible or unconverted | 6 |
| Busiest month | Jun 2025 (25 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 15 | 14 | $438.2M | $25.6M | ████████████ |
| Jun 2025 | 25 | 24 | $5.2B | $200M | ████████████████████ |
| Jul 2025 | 21 | 21 | $1.8B | $19M | █████████████████ |
| Aug 2025 | 17 | 15 | $9.7B | $115.5M | ██████████████ |
| Sep 2025 | 16 | 16 | $1.1B | $40.5M | █████████████ |
| Oct 2025 | 15 | 15 | $5.8B | $125M | ████████████ |
| Nov 2025 | 15 | 12 | $783.3M | $26.5M | ████████████ |
| Dec 2025 | 15 | 15 | $3.3B | $300M | ████████████ |
| Jan 2026 | 8 | 8 | $820.7M | $27.5M | ██████ |
| Feb 2026 | 21 | 16 | $627.2M | $36.6M | █████████████████ |
| Mar 2026 | 17 | 12 | $1.6B | $75M | ██████████████ |
| Apr 2026 | 15 | 15 | $677.3M | $42.5M | ████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 26 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 1 Aug 2025 | Openai (openai.com) | — | $8.3B | dragoneer investment group, blackstone, tpg | United States | OpenAI, maker of ChatGPT, has raised $8.3 billion in a new funding round that values the artificial intelligence company at $300 billion,… |
| 5 Jun 2025 | Anduril Industries (anduril.com) | Series G | $2.5B | founders fund, existing investors | USA | Anduril Industries, a U.S. defense technology company, raised $2.5 billion in its latest funding round. |
| 24 Oct 2025 | Crusoe (crusoe.ai) | — | $1.4B ⚠ check sentence | valor equity partners, Mubadala Capital, nvidia | USA | Crusoe, which calls itself 'the AI Factory Company,' is valued at over $10 billion in this latest $1.4 billion funding round. |
| 18 Dec 2025 | Trade Republic (traderepublic.com) | secondary | $1.3B ⚠ check sentence | founders fund, wellington management, gic | Germany | Berlin, 17. December 2025 (PM) – YPOG has provided comprehensive legal advice to Trade Republic Bank GmbH in the context of a secondary… |
| 27 Mar 2026 | Physical Intelligence (physicalintelligence.company) | — | $1B ⚠ check sentence | founders fund, lightspeed venture partners, thrive capital | USA | Physical Intelligence, the two-year-old San Francisco robotics startup, is in discussions to raise about $1 billion in new funding at a… |
| 22 Oct 2025 | Polymarket (polymarket.com) | — | $1B ⚠ check sentence | founders fund | United States | a massive jump from its $1 billion market cap earlier this year in a Founders Fund-led round. |
| 2 Jun 2025 | Neuralink (neuralink.com) | Series E | $650M | ARK Invest, dfj growth, founders fund | USA | Neuralink, a brain‑computer interface startup founded by Elon Musk, secured $650 million in a Series E funding round to advance its… |
| 19 Aug 2025 | Cognition (cognition.ai) | Series C | $500M | founders fund | — | Cognition has secured nearly $500 million in Series C funding, valuing the company at $9.8 billion, according to reports. The round was… |
| 1 Aug 2025 | Ramp (ramp.network) | Series E-2 | $500M | iconiq capital, founders fund, D1 Capital | USA | Ramp, a New York-based expense management fintech startup, raised a hefty $500 million in a Series E-2 round to accelerate its AI-driven… |
| 4 Jul 2025 | Rippling (rippling.com) | Collection G spherical | $450M ⚠ check sentence | sands capital, gic, Goldman Sachs Development | US | Rippling, a San Francisco-based HR tech startup, has raised $450 million in a Collection G funding spherical, valuing the corporate at… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Scout AI (withscout.com) | Series A | $100M | align ventures, draper associates, Decisive Point Ventures | — | Scout AI Raises $100M Series A to Advance Defense AI |
| 20 Apr 2026 | Logicc | Seed | $2.7M | 10x Founders Fund, redstone, ms&ad ventures | — | Logicc raised €2.5M seed round for secure AI in regulated industries. |
| 20 Apr 2026 | Sona (getsona.com) | Series B | $45M | N47, felicis, northzone | USA | Sona has raised $45 million in Series B funding led by N47, with participation from existing investors Felicis, Northzone, Gradient, and… |
| 20 Apr 2026 | Loop (loopstore.com) | Series C | $95M | valor equity partners, Valor Atreides AI Fund, 8vc | United States | Loop, a San Francisco, CA–based full-stack, verticalized AI platform for logistics and supply chains, has raised $95 million in Series C… |
| 15 Apr 2026 | Alloy Therapeutics (alloytx.com) | Series E | $40M | 8vc, jic venture growth investments, echo capital | USA | Alloy Therapeutics, a biotechnology ecosystem company, announced a $40 million Series E financing round. |
| 9 Apr 2026 | Nava (navacenter.com) | Seed | $9.6M | rtp global, unicorn india ventures, Blume Founders Fund | Singapore | Nava previously raised a $9.6 million seed round led by RTP Global, with participation from Unicorn India Ventures, Blume Founders Fund,… |
| 7 Apr 2026 | Hermeus (hermeus.com) | Series D | $350M | khosla ventures, founders fund, canaan | United States | Hermeus, an Atlanta‑area defense startup developing autonomous hypersonic aircraft, closed a $350 million funding round. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "Founders Fund" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "Founders Fund" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "Founders Fund" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Founders Fund", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Founders Fund", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [General Atlantic Portfolio](general-atlantic-portfolio.md)
- [Tiger Global Portfolio](tiger-global-portfolio.md)
- [NEA Investments](nea-investments.md)
- [Insight Partners Portfolio](insight-partners-portfolio.md)
