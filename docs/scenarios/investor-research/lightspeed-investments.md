# Lightspeed Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “lightspeed investments” · 30/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [lightspeed-investments.json](../../examples/scenarios/lightspeed-investments.json).

**Question.** Which rounds did Lightspeed appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Lightspeed”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 350 |
| With a usable reported amount | 333 |
| Reported total (usable amounts) | $71.9B |
| Median reported round | $55M |
| Largest reported round | $20B |
| Amounts left out as implausible or unconverted | 3 |
| Busiest month | Jan 2026 (47 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 17 | 17 | $805.7M | $22.4M | ███████ |
| Jun 2025 | 24 | 23 | $3B | $114M | ██████████ |
| Jul 2025 | 10 | 10 | $721.7M | $50M | ████ |
| Aug 2025 | 22 | 21 | $4.4B | $58M | █████████ |
| Sep 2025 | 41 | 39 | $17.8B | $47M | █████████████████ |
| Oct 2025 | 38 | 37 | $9.6B | $68M | ████████████████ |
| Nov 2025 | 21 | 20 | $1.6B | $51.5M | █████████ |
| Dec 2025 | 21 | 17 | $2.1B | $130M | █████████ |
| Jan 2026 | 47 | 46 | $26.4B | $85M | ████████████████████ |
| Feb 2026 | 46 | 43 | $23B | $45M | ████████████████████ |
| Mar 2026 | 42 | 39 | $3.9B | $65M | ██████████████████ |
| Apr 2026 | 21 | 21 | $1.8B | $27M | █████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 26 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 9 Feb 2026 | Anthropic (anthropic.com) | Late-stage mega-round | $20B ⚠ check sentence | nvidia, microsoft, altimeter capital | USA | The company is reportedly raising $20 billion in new capital at a staggering $350 billion valuation. |
| 10 Oct 2025 | Reflection AI (reflectionai.ca) | — | $2B ⚠ check sentence | nvidia, disruptive, dst | United States | Reflection AI on Friday raised $2 billion at an $8 billion valuation, surpassing its previous valuation just seven months ago by 15x from… |
| 16 Sep 2025 | Mistral AI (mistral.ai) | Series C | $2B ⚠ check sentence | ASML Holding NV, dst global, Andreessen Horowitz | — | French startup Mistral AI has secured USD 2bn (EUR 1.7bn) in a Series C round, bringing its valuation to USD 13.8bn, the company announced… |
| 14 Jan 2026 | Skild AI | Series C | $1.4B | softbank group, nventures, bezos expeditions | US | Skild AI, a Pittsburgh-based robotics AI startup, secured a mammoth $1.4 billion funding round to accelerate development of its… |
| 27 Apr 2026 | Ineffable Intelligence | — | $1.1B ⚠ check sentence | sequoia capital, lightspeed venture partners, nvidia | United Kingdom | David Silver has raised $1.1bn (£880m) for his London-based startup Ineffable Intelligence at a valuation of $5.1bn, in a round led by… |
| 27 Mar 2026 | Physical Intelligence (physicalintelligence.company) | — | $1B ⚠ check sentence | founders fund, lightspeed venture partners, thrive capital | USA | Physical Intelligence, the two-year-old San Francisco robotics startup, is in discussions to raise about $1 billion in new funding at a… |
| 8 Oct 2025 | Base Power (basepower.in) | Series C | $1B | addition, valor equity partners, lightspeed venture partners | USA | Base Power, an Austin-based energy startup modernizing the U.S. power grid, has secured a whopping $1 billion in Series C funding to… |
| 3 Oct 2025 | Unconventional (unconventional.com) | — | $1B ⚠ check sentence | Andreessen Horowitz, lightspeed, lux capital | — | Naveen Rao, who was formerly the head of artificial intelligence at Databricks, is in talks to raise $1 billion at a $5 billion valuation… |
| 2 Jun 2025 | Neuralink (neuralink.com) | — | $650M | ARK Invest, founders fund, sequoia capital | U.S. | Elon Musk's brain tech startup Neuralink has closed a $650 million funding round. |
| 24 Mar 2026 | Temporal Technologies (temporal.io) | Series D | $649.5M | amplify partners, Andreessen Horowitz, gic | USA |  |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Coral (getcoral.app) | investment | $12.5M | lightspeed, Z47 | — | The company announced a $12.5 million investment led by Lightspeed and Z47. |
| 30 Apr 2026 | Oolka (oolka.in) | Series A | $14M | accel, lightspeed, Z47 | India | Oolka has raised $14 million in a Series A funding round led by Accel, with participation from existing investors Lightspeed and Z47. |
| 28 Apr 2026 | Zocks Communications | Series B | $45M | rfg advisory, lightspeed venture partners, qed investors | USA | Zocks announced its Series B funding in January, raising $45 million... |
| 28 Apr 2026 | Snabbit | Series D | $56M | Susquehanna Venture Capital, Mirae Asset Venture… | India | Snabbit, an Indian on-demand home services startup, has closed a $56 million funding round, confirming TechCrunch’s earlier report. |
| 27 Apr 2026 | Ineffable Intelligence | — | $1.1B ⚠ check sentence | sequoia capital, lightspeed venture partners, nvidia | United Kingdom | David Silver has raised $1.1bn (£880m) for his London-based startup Ineffable Intelligence at a valuation of $5.1bn, in a round led by… |
| 25 Apr 2026 | Snabbit | — | $50M | Susquehanna Venture Capital, mirae asset, fj labs | India | The Bengaluru-based startup is in talks to raise around $50 million in the round, according to three people with knowledge of the deal. |
| 24 Apr 2026 | Oolka (oolka.in) | Series A | $15.6M | lightspeed, Z47, Meesho founders | India | Oolka Raises ₹130 Cr Series A Oolka, an AI-powered credit management platform, has raised INR 130 crore (~$14 million) in a Series A round… |
| 23 Apr 2026 | Reliable Robotics (reliable.co) | — | $160M | nimble partners, eclipse, lightspeed | United States | today announced $160M in new funding to accelerate deployment and scale production of the Reliable Autonomy System (RAS) – the first… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Lightspeed --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Lightspeed --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Lightspeed --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Lightspeed", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Lightspeed", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [NEA Investments](nea-investments.md)
- [Insight Partners Portfolio](insight-partners-portfolio.md)
- [Khosla Ventures Portfolio](khosla-ventures-portfolio.md)
- [Coatue Investments](coatue-investments.md)
