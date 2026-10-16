# Sequoia Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “sequoia investments” · 90/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [sequoia-investments.json](../../examples/scenarios/sequoia-investments.json).

**Question.** Which rounds did Sequoia appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Sequoia”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 366 |
| With a usable reported amount | 336 |
| Reported total (usable amounts) | $107.8B |
| Median reported round | $62.6M |
| Largest reported round | $25B |
| Amounts left out as implausible or unconverted | 11 |
| Busiest month | Feb 2026 (44 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 14 | 13 | $516M | $52.5M | ██████ |
| Jun 2025 | 40 | 39 | $3.3B | $70M | ██████████████████ |
| Jul 2025 | 23 | 23 | $886.8M | $29.1M | ██████████ |
| Aug 2025 | 36 | 35 | $9.4B | $35M | ████████████████ |
| Sep 2025 | 20 | 19 | $576.9M | $30M | █████████ |
| Oct 2025 | 35 | 33 | $11.8B | $180M | ████████████████ |
| Nov 2025 | 20 | 18 | $2.6B | $57.5M | █████████ |
| Dec 2025 | 36 | 35 | $3.7B | $75M | ████████████████ |
| Jan 2026 | 39 | 36 | $67.2B | $125M | ██████████████████ |
| Feb 2026 | 44 | 37 | $39.6B | $96M | ████████████████████ |
| Mar 2026 | 36 | 30 | $19B | $75M | ████████████████ |
| Apr 2026 | 23 | 18 | $4.4B | $155M | ██████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 25 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 19 Jan 2026 | Anthropic (anthropic.com) | — | $25B | gic, coatue, sequoia capital | United States | the venture capital giant is participating in a round led by Singapore sovereign wealth fund GIC and US investor Coatue, each of which is… |
| 27 Mar 2026 | Waymo (waymo.com) | Series D | $16B | alphabet, Andreessen Horowitz, bdt & msd partners | — | Mountain View-based Waymo is a mobility technology company that improves transportation by developing self‑driving solutions for travelers… |
| 4 Aug 2025 | Openai (openai.com) | Private Funding Round (Late-stage) | $8.3B ⚠ check sentence | dragoneer investment group, blackstone, tpg | USA | OpenAI has raised a massive $8.3 billion in new funding at a staggering $300 billion valuation. |
| 10 Oct 2025 | Reflection AI (reflectionai.ca) | — | $2B ⚠ check sentence | nvidia, disruptive, dst | United States | Reflection AI on Friday raised $2 billion at an $8 billion valuation, surpassing its previous valuation just seven months ago by 15x from… |
| 22 Apr 2026 | Factory (factory.com) | Series C | $1.5B ⚠ check sentence | khosla ventures, sequoia capital, blackstone | — | Factory announced it has raised $150 million in a Series C funding round led by Khosla Ventures, with participation from Sequoia Capital,… |
| 14 Jan 2026 | Skild AI | Series C | $1.4B | softbank group, nventures, bezos expeditions | US | Skild AI, a Pittsburgh-based robotics AI startup, secured a mammoth $1.4 billion funding round to accelerate development of its… |
| 18 Dec 2025 | Trade Republic (traderepublic.com) | secondary | $1.3B ⚠ check sentence | founders fund, wellington management, gic | Germany | Berlin, 17. December 2025 (PM) – YPOG has provided comprehensive legal advice to Trade Republic Bank GmbH in the context of a secondary… |
| 27 Apr 2026 | Ineffable Intelligence | — | $1.1B ⚠ check sentence | sequoia capital, lightspeed venture partners, nvidia | United Kingdom | David Silver has raised $1.1bn (£880m) for his London-based startup Ineffable Intelligence at a valuation of $5.1bn, in a round led by… |
| 3 Dec 2025 | Kalshi (kalshi.com) | Series E | $1B | paradigm, sequoia, Andreessen Horowitz | United States | Kalshi, a New York-based financial exchange and prediction market, has closed a $1 billion Series E round valuing the company at $11… |
| 24 Mar 2026 | Ayar Labs (ayarlabs.com) | Series E | $871.5M | 1789 Capital, alchip, AMD Ventures | USA |  |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Parallel Web Systems | Series B | $10M ⚠ check sentence | sequoia capital, kleiner perkins, index ventures | — | Former Twitter (now X) CEO Parag Agrawal’s AI agentic platform Parallel Web Systems has raised a $100 million Series B at a $2 billion… |
| 29 Apr 2026 | Rogo (rogodata.com) | Series D | $160M | kleiner perkins, sequoia capital, thrive | USA | Rogo Raises $160M in Series D Funding for Finance AI Platform |
| 29 Apr 2026 | Parallel Web Systems | Series B | $100M | sequoia capital | — | Parallel Web Systems Raises $100M Series B for AI Agents’ Web Infrastructure |
| 27 Apr 2026 | Volant (volant.aero) | Series C | $300M | stone, Sequoia China, Fortera Capital | China | Gasgoo Munich- VOLANT has recently closed a Series C funding round exceeding $300 million. |
| 27 Apr 2026 | Signull Labs | seed | $8M | Andreessen Horowitz, sequoia capital | — | Signull Labs raised $8 million in a seed round led by prominent venture firms including Andreessen Horowitz and Sequoia Capital. |
| 27 Apr 2026 | Ineffable Intelligence | — | $1.1B ⚠ check sentence | sequoia capital, lightspeed venture partners, nvidia | United Kingdom | David Silver has raised $1.1bn (£880m) for his London-based startup Ineffable Intelligence at a valuation of $5.1bn, in a round led by… |
| 27 Apr 2026 | Atech (atech.cloud) | Pre-Seed | — | nordic makers, emblem, lovable | Denmark | AI hardware startup Atech has raised a Pre-Seed round with participation from Nordic Makers, Emblem, Lovable, Sequoia Scout Fund… |
| 22 Apr 2026 | Factory (factory.com) | Series C | $1.5B ⚠ check sentence | khosla ventures, sequoia capital, blackstone | — | Factory announced it has raised $150 million in a Series C funding round led by Khosla Ventures, with participation from Sequoia Capital,… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Sequoia --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Sequoia --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Sequoia --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Sequoia", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Sequoia", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Blackstone Investments](blackstone-investments.md)
- [Mubadala Investments](mubadala-investments.md)
- [Thrive Capital Portfolio](thrive-capital-portfolio.md)
- [Accel Investments](accel-investments.md)
