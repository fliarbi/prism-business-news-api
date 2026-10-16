# Thrive Capital Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “thrive capital portfolio” · 30/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [thrive-capital-portfolio.json](../../examples/scenarios/thrive-capital-portfolio.json).

**Question.** Which rounds did Thrive Capital appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Thrive Capital”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 90 |
| With a usable reported amount | 82 |
| Reported total (usable amounts) | $59.6B |
| Median reported round | $154M |
| Largest reported round | $10B |
| Amounts left out as implausible or unconverted | 7 |
| Busiest month | Oct 2025 (12 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 7 | 7 | $2.1B | $105M | ████████████ |
| Jun 2025 | 9 | 9 | $1.8B | $425M | ███████████████ |
| Jul 2025 | 8 | 8 | $257.9M | $33M | █████████████ |
| Aug 2025 | 11 | 9 | $16.3B | $1B | ██████████████████ |
| Sep 2025 | 4 | 4 | $1.7B | $648M | ███████ |
| Oct 2025 | 12 | 12 | $8.4B | $200M | ████████████████████ |
| Nov 2025 | 8 | 7 | $3.2B | $300M | █████████████ |
| Dec 2025 | 7 | 7 | $5.7B | $162M | ████████████ |
| Jan 2026 | 7 | 7 | $4.5B | $75M | ████████████ |
| Feb 2026 | 7 | 5 | $5.4B | $150M | ████████████ |
| Mar 2026 | 5 | 4 | $15B | $4B | ████████ |
| Apr 2026 | 5 | 3 | $2.2B | $1.1B | ████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 27 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Mar 2026 | Openai (openai.com) | — | $10B | altimeter capital, Andreessen Horowitz, coatue | USA | OpenAI - $10.0B |
| 10 Feb 2026 | Databricks (databricks.com) | Series K | $5B ⚠ check sentence | qatar investment authority, Singapore Temasek, Macquarie… | United States | United States data & artificial intelligence (AI) company Databrick has raised $5 billion funding at $134 billion valuation, and with… |
| 4 Mar 2026 | Anduril Industries (anduril.com) | — | $4B | thrive capital, Andreessen Horowitz | USA | the defense company is seeking to raise about $4 billion from venture capital firms Thrive Capital and Andreessen Horowitz. |
| 13 Nov 2025 | Cursor (cursor.com) | Series D | $2.3B ⚠ check sentence | accel, coatue, Andreessen Horowitz | United States | Cursor has vaulted into the top tier of private AI companies after securing a massive $2.3 billion Series D at a $29.3 billion valuation. |
| 17 Dec 2025 | Trade Republic (traderepublic.com) | secondary transaction | $1.3B | founders fund, sequoia, accel | Germany | Investors have carried out a secondary transaction of 1.2 billion euros that values the company at 12.5 billion euros. |
| 27 Mar 2026 | Physical Intelligence (physicalintelligence.company) | — | $1B ⚠ check sentence | founders fund, lightspeed venture partners, thrive capital | USA | Physical Intelligence, the two-year-old San Francisco robotics startup, is in discussions to raise about $1 billion in new funding at a… |
| 8 Oct 2025 | Base Power (basepower.in) | Series C | $1B | addition, valor equity partners, lightspeed venture partners | USA | Base Power, an Austin-based energy startup modernizing the U.S. power grid, has secured a whopping $1 billion in Series C funding to… |
| 27 Aug 2025 | Anysphere (anysphere.inc) | Series C | $900M | thrive capital, Andreessen Horowitz, accel | — | Anysphere, the AI research lab behind AI coding tool Cursor, raised a sizable $900 million Series C round that values the company at… |
| 2 Jun 2025 | Neuralink (neuralink.com) | Series E | $650M | ARK Invest, dfj growth, founders fund | USA | Neuralink, a brain‑computer interface startup founded by Elon Musk, secured $650 million in a Series E funding round to advance its… |
| 24 Sep 2025 | Isomorphic Labs (isomorphiclabs.com) | — | $648M | thrive capital | UK | Isomorphic Labs from UK. 600 million euros in March 2025 – the round of Thrive Capital from the USA has been led. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Rogo (rogodata.com) | Series D | $160M ⚠ check sentence | sequoia capital, thrive capital, khosla ventures | United States | Rogo closed a 160 million dollar Series D round led by Kleiner Perkins, lifting total funding above 300 million dollars to scale its… |
| 22 Apr 2026 | Cursor (cursor.com) | private funding round | $2B | Andreessen Horowitz, thrive capital, nvidia | — | Cursor was actively finalizing a $2 billion private funding round that would have valued the AI coding software company at $50 billion.… |
| 6 Apr 2026 | Openai (openai.com) | — | — ⚠ implausible size | amazon, nvidia, softbank | — | OpenAI has raised USD $122 billion in committed capital, valuing the company at USD $852 billion after the investment. The round was… |
| 30 Mar 2026 | Openai (openai.com) | — | $10B | altimeter capital, Andreessen Horowitz, coatue | USA | OpenAI - $10.0B |
| 27 Mar 2026 | Physical Intelligence (physicalintelligence.company) | — | $1B ⚠ check sentence | founders fund, lightspeed venture partners, thrive capital | USA | Physical Intelligence, the two-year-old San Francisco robotics startup, is in discussions to raise about $1 billion in new funding at a… |
| 4 Mar 2026 | Anduril Industries (anduril.com) | — | $4B | thrive capital, Andreessen Horowitz | USA | the defense company is seeking to raise about $4 billion from venture capital firms Thrive Capital and Andreessen Horowitz. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "Thrive Capital" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "Thrive Capital" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "Thrive Capital" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Thrive Capital", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Thrive Capital", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Mubadala Investments](mubadala-investments.md)
- [Sequoia Investments](sequoia-investments.md)
- [Accel Investments](accel-investments.md)
- [TPG Portfolio](tpg-portfolio.md)
