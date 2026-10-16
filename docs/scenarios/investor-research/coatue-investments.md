# Coatue Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “coatue investments” · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [coatue-investments.json](../../examples/scenarios/coatue-investments.json).

**Question.** Which rounds did Coatue appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Coatue”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 145 |
| With a usable reported amount | 124 |
| Reported total (usable amounts) | $159.3B |
| Median reported round | $300M |
| Largest reported round | $25B |
| Amounts left out as implausible or unconverted | 12 |
| Busiest month | Mar 2026 (24 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 8 | 8 | $676M | $80M | ███████ |
| Jun 2025 | 10 | 10 | $1.7B | $200M | ████████ |
| Jul 2025 | 3 | 1 | $210M | $210M | ██ |
| Aug 2025 | 5 | 4 | $8.8B | $230M | ████ |
| Sep 2025 | 14 | 13 | $13.7B | $180M | ████████████ |
| Oct 2025 | 11 | 11 | $2.9B | $187.5M | █████████ |
| Nov 2025 | 11 | 8 | $6.1B | $300M | █████████ |
| Dec 2025 | 3 | 3 | $6B | $3B | ██ |
| Jan 2026 | 18 | 13 | $66.2B | $2B | ███████████████ |
| Feb 2026 | 18 | 14 | $60B | $1B | ███████████████ |
| Mar 2026 | 24 | 23 | $18B | $200M | ████████████████████ |
| Apr 2026 | 20 | 16 | $3.5B | $265M | █████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 30 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 19 Jan 2026 | Anthropic (anthropic.com) | — | $25B | gic, coatue, sequoia capital | United States | the venture capital giant is participating in a round led by Singapore sovereign wealth fund GIC and US investor Coatue, each of which is… |
| 30 Mar 2026 | Openai (openai.com) | — | $10B | altimeter capital, Andreessen Horowitz, coatue | USA | OpenAI - $10.0B |
| 9 Feb 2026 | Firmus Technologies | debt financing | $10B | blackstone, coatue | Australia | Australian artificial intelligence infrastructure company Firmus Technologies has secured a February 9, 2026 commitment for $10 billion in… |
| 16 Jan 2026 | Databricks (databricks.com) | Venture | $4B | Andreessen Horowitz, blackrock, blackstone group | United States | Round: Venture |
| 24 Mar 2026 | Cerebras Systems (cerebras.net) | Series H | $2.8B | 1789 Capital, alpha wave global, altimeter capital | USA |  |
| 23 Mar 2026 | Kalshi (kalshi.com) | — | $2.6B | coatue | USA | Kalshi has now raised a total of $2.6B in total equity funding and is backed by Coatue. |
| 14 Nov 2025 | Anysphere (anysphere.inc) | Series D | $2.3B | accel, coatue, nvidia | United States | AI coding startup Anysphere completed a $2.3 billion Series D funding round on Thursday, valuing the company at $29.3 billion. Accel and… |
| 13 Nov 2025 | Cursor (cursor.com) | Series D | $2.3B ⚠ check sentence | accel, coatue, Andreessen Horowitz | United States | Cursor has vaulted into the top tier of private AI companies after securing a massive $2.3 billion Series D at a $29.3 billion valuation. |
| 6 Jan 2026 | Dayone (dayoneny.org) | Series C | $2B | Coatue Management, Indonesia Investment Authority | Singapore | DayOne, the overseas arm of Shanghai-based GDS Holdings, has won the backing of Indonesia’s sovereign wealth fund as part of a Series C… |
| 14 Jan 2026 | Skild AI | Series C | $1.4B | softbank group, nventures, bezos expeditions | US | Skild AI, a Pittsburgh-based robotics AI startup, secured a mammoth $1.4 billion funding round to accelerate development of its… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 23 Apr 2026 | Reliable Robotics (reliable.co) | — | $160M | nimble partners, eclipse, lightspeed | United States | today announced $160M in new funding to accelerate deployment and scale production of the Reliable Autonomy System (RAS) – the first… |
| 14 Apr 2026 | Firmus (firmus.ai) | private debt financing | $330M | blackstone, coatue | Australia | In November last year, the neocloud said it had raised AU$500m ($351 million) for Project Southgate. |
| 12 Apr 2026 | Firmus (firmus.ai) | equity injection | $505M | coatue, nvidia | — | Firmus, an Asia-based AI infrastructure provider, is lining up a $505 million equity injection led by Coatue, with NVIDIA expected to… |
| 11 Apr 2026 | Sifive (sifive.com) | — | $175M ⚠ check sentence | Coatue Management, intel capital, qualcomm ventures | — | SiFive hasn’t raised since March 2022, Pitchbook estimates, when it brought in $175 million led by Coatue Management at a pre-money… |
| 10 Apr 2026 | Kalshi (kalshi.com) | — | $1B ⚠ check sentence | coatue | — | Kalshi raised $1 billion in March, doubling its valuation to $22 billion led by Coatue. |
| 7 Apr 2026 | Tamara (tamara.co) | — | $100M | Sanabil Investments, coatue, Shoorooq Partners | Saudi Arabia | Saudi Arabia’s buy now, pay later (BNPL) platform Tamara raised $100 million in funds led by Riyadh-based Sanabil Investments where other… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Coatue --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Coatue --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Coatue --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Coatue", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Coatue", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Lightspeed Investments](lightspeed-investments.md)
- [Khosla Ventures Portfolio](khosla-ventures-portfolio.md)
- [General Catalyst Portfolio](general-catalyst-portfolio.md)
- [Andreessen Horowitz Portfolio](andreessen-horowitz-portfolio.md)
