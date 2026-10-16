# Andreessen Horowitz Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “andreessen horowitz portfolio” · 30/month India · 110/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [andreessen-horowitz-portfolio.json](../../examples/scenarios/andreessen-horowitz-portfolio.json).

**Question.** Which rounds did Andreessen Horowitz appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Andreessen Horowitz”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 362 |
| With a usable reported amount | 339 |
| Reported total (usable amounts) | $94.7B |
| Median reported round | $50M |
| Largest reported round | $16B |
| Amounts left out as implausible or unconverted | 5 |
| Busiest month | Mar 2026 (52 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 18 | 17 | $2.7B | $100M | ███████ |
| Jun 2025 | 25 | 25 | $3.9B | $60M | ██████████ |
| Jul 2025 | 18 | 18 | $5B | $38M | ███████ |
| Aug 2025 | 41 | 40 | $15.6B | $40M | ████████████████ |
| Sep 2025 | 27 | 25 | $8.2B | $44M | ██████████ |
| Oct 2025 | 25 | 24 | $3.3B | $50M | ██████████ |
| Nov 2025 | 35 | 32 | $6.6B | $68M | █████████████ |
| Dec 2025 | 34 | 33 | $7.1B | $41M | █████████████ |
| Jan 2026 | 28 | 28 | $5.8B | $92M | ███████████ |
| Feb 2026 | 34 | 33 | $24.6B | $140M | █████████████ |
| Mar 2026 | 52 | 46 | $38B | $102.7M | ████████████████████ |
| Apr 2026 | 25 | 18 | $5.3B | $28M | ██████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 27 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 27 Mar 2026 | Waymo (waymo.com) | Series D | $16B | alphabet, Andreessen Horowitz, bdt & msd partners | — | Mountain View-based Waymo is a mobility technology company that improves transportation by developing self‑driving solutions for travelers… |
| 30 Mar 2026 | Openai (openai.com) | — | $10B | altimeter capital, Andreessen Horowitz, coatue | USA | OpenAI - $10.0B |
| 10 Feb 2026 | Databricks (databricks.com) | Series K | $5B ⚠ check sentence | qatar investment authority, Singapore Temasek, Macquarie… | United States | United States data & artificial intelligence (AI) company Databrick has raised $5 billion funding at $134 billion valuation, and with… |
| 4 Mar 2026 | Anduril Industries (anduril.com) | — | $4B | thrive capital, Andreessen Horowitz | USA | the defense company is seeking to raise about $4 billion from venture capital firms Thrive Capital and Andreessen Horowitz. |
| 6 Apr 2026 | Saronic (saronic.com) | total equity | $2.6B | 8vc, advent international, Andreessen Horowitz | United States | Saronic has now raised a total of $2.6B in total equity funding and is backed by 8VC, Advent International, Andreessen Horowitz, BAM… |
| 13 Nov 2025 | Cursor (cursor.com) | Series D | $2.3B ⚠ check sentence | accel, coatue, Andreessen Horowitz | United States | Cursor has vaulted into the top tier of private AI companies after securing a massive $2.3 billion Series D at a $29.3 billion valuation. |
| 4 Sep 2025 | Mistral AI (mistral.ai) | Late‑stage (unconfirmed) | $2.2B | Andreessen Horowitz, general catalyst, (New investors not… | France | Paris‑based Mistral AI is reportedly in the final stages of securing a colossal €2 billion (~$2.2 billion) funding round that would value… |
| 7 Aug 2025 | Thinking Machines Lab | — | $2B | Andreessen Horowitz | — | Thinking Machines Lab Jul 2025 $2 B $12 B Led by Andreessen Horowitz, major ex‑OpenAI team |
| 24 Mar 2026 | World Labs (worldlabs.vdtrxn) | Venture | $1.2B | amd, Andreessen Horowitz, autodesk | USA |  |
| 3 Dec 2025 | Kalshi (kalshi.com) | Series E | $1B | paradigm, sequoia, Andreessen Horowitz | United States | Kalshi, a New York-based financial exchange and prediction market, has closed a $1 billion Series E round valuing the company at $11… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 27 Apr 2026 | Signull Labs | seed | $8M | Andreessen Horowitz, sequoia capital | — | Signull Labs raised $8 million in a seed round led by prominent venture firms including Andreessen Horowitz and Sequoia Capital. |
| 27 Apr 2026 | Segura (segura-moto.fr) | seed | $8M | Andreessen Horowitz, kaszek, big_bets | Brazil | Brazilian startup Segura has raised an $8 million in a seed round to build what it calls the operating layer between insurers and brokers… |
| 27 Apr 2026 | Atech (atech.cloud) | Pre-Seed | — | nordic makers, emblem, lovable | Denmark | AI hardware startup Atech has raised a Pre-Seed round with participation from Nordic Makers, Emblem, Lovable, Sequoia Scout Fund… |
| 24 Apr 2026 | Petual | Funding | $20M | Andreessen Horowitz, first round capital, cowboy ventures | — | Petual raises $20m for AI-powered SOX compliance Petual, an AI-powered audit and compliance platform, has secured $20m in funding to… |
| 23 Apr 2026 | Petual | — | — | Andreessen Horowitz (a16z) | — | Andreessen Horowitz (a16z) has invested in Petual, a startup building an AI-powered platform designed to streamline audit and compliance… |
| 22 Apr 2026 | Cursor (cursor.com) | private funding round | $2B | Andreessen Horowitz, thrive capital, nvidia | — | Cursor was actively finalizing a $2 billion private funding round that would have valued the AI coding software company at $50 billion.… |
| 22 Apr 2026 | Ulysses (ulysses-ltd.com) | Series A | — | Booz Allen Ventures, Andreessen Horowitz's American… | USA | The investment is part of Ulysses’ Series A funding round, led by Andreessen Horowitz’s American Dynamism fund. |
| 17 Apr 2026 | Flock Safety (flocksafety.com) | — | — ⚠ check sentence | Andreessen Horowitz | USA | Flock Safety, which sells cameras, drones and AI software to police departments, was valued at $8.4 billion in a new round of funding… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "Andreessen Horowitz" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "Andreessen Horowitz" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "Andreessen Horowitz" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Andreessen Horowitz", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Andreessen Horowitz", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Coatue Investments](coatue-investments.md)
- [General Catalyst Portfolio](general-catalyst-portfolio.md)
- [Temasek Portfolio](temasek-portfolio.md)
- [8vc Portfolio](8vc-portfolio.md)
