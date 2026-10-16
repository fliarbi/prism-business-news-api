# Bessemer Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “bessemer investments” · 30/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [bessemer-investments.json](../../examples/scenarios/bessemer-investments.json).

**Question.** Which rounds did Bessemer appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Bessemer”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 216 |
| With a usable reported amount | 196 |
| Reported total (usable amounts) | $36.9B |
| Median reported round | $33.5M |
| Largest reported round | $16B |
| Amounts left out as implausible or unconverted | 3 |
| Busiest month | Feb 2026 (32 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 22 | 20 | $744.9M | $25.4M | ██████████████ |
| Jun 2025 | 9 | 6 | $186M | $40M | ██████ |
| Jul 2025 | 13 | 12 | $402M | $26M | ████████ |
| Aug 2025 | 17 | 16 | $867.8M | $25M | ███████████ |
| Sep 2025 | 14 | 13 | $399.5M | $31M | █████████ |
| Oct 2025 | 23 | 21 | $4.6B | $70M | ██████████████ |
| Nov 2025 | 10 | 9 | $475M | $40M | ██████ |
| Dec 2025 | 16 | 14 | $1.1B | $100M | ██████████ |
| Jan 2026 | 26 | 25 | $1.9B | $32M | ████████████████ |
| Feb 2026 | 32 | 30 | $2.3B | $50.8M | ████████████████████ |
| Mar 2026 | 19 | 17 | $22.4B | $97.5M | ████████████ |
| Apr 2026 | 15 | 13 | $3.1B | $16M | █████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 24 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 27 Mar 2026 | Waymo (waymo.com) | Series D | $16B | alphabet, Andreessen Horowitz, bdt & msd partners | — | Mountain View-based Waymo is a mobility technology company that improves transportation by developing self‑driving solutions for travelers… |
| 4 Oct 2025 | Anthropic PBC | — | $3.8B | lightspeed, bessemer venture partners, cisco investments | — | It was followed by Anthropic PBC's $3.75 billion series E round of funding led by Lightspeed Ventures LLC. |
| 9 Mar 2026 | Easebuzz (easebuzz.in) | — | $2.9B | bessemer venture partners | India | In April 2025, Bessemer led the Rs 240 crore infusion into the company. |
| 6 Apr 2026 | Saronic (saronic.com) | total equity | $2.6B | 8vc, advent international, Andreessen Horowitz | United States | Saronic has now raised a total of $2.6B in total equity funding and is backed by 8VC, Advent International, Andreessen Horowitz, BAM… |
| 10 Mar 2026 | Legora | Series D | $550M | accel, benchmark, bessemer venture partners | Sweden | Legora Raises $550M in Series D Funding to Expand AI in Legal Operations |
| 18 Feb 2026 | Inertia (inertialab.com) | Series A | $450M | bessemer venture partners, google ventures, modern capital | United States | Inertia raises $450M in Series A funding to build fusion energy laser system |
| 17 Jan 2026 | Clickhouse (clickhouse.com) | Series D | $400M | bessemer venture partners, gic, index ventures | United States | ClickHouse Inc. has raised $400 million in a Series D round led by Dragoneer Investment Group, marking one of the largest funding rounds… |
| 2 Feb 2026 | Rain (rain.agency) | Series C | $332.5M | bessemer venture partners, dragonfly, endeavor catalyst | — |  |
| 23 Jan 2026 | Torq (torqlogistics.com) | — | $332M | Merlin Ventures, insight partners, bessemer venture partners | Israel | The round raised $332 million and included participation from Insight Partners, Bessemer Venture Partners, Greenfield Partners, Evolution… |
| 3 Apr 2026 | Sarvam AI (sarvam.ai) | — | $300M | bessemer venture partners, nvidia, Amazon.com Inc | India | India’s homegrown artificial intelligence start-up, Sarvam AI, is close to raising $300 million to $350 million as it seeks to build a… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 27 Apr 2026 | Amperos | — | $16M | bessemer venture partners, neo, uncork capital | US | New York-based Amperos an AI-powered revenue recovery and denial management platform that reduces claim rejections and optimize collections. |
| 24 Apr 2026 | Amperos Health | Series A | $16M | bessemer venture partners, uncork capital, neo | — | It announced on Wednesday that it secured $16 million in Series A funding. |
| 17 Apr 2026 | Zenskar (zenskar.com) | Series A | $15M | Susquehanna, bessemer venture partners, shine capital | United States | New York City based billing and revenue automation platform raised $15m in Series A funding led by Susquehanna, Bessemer Venture Partners,… |
| 16 Apr 2026 | Bold (boldstrategies.com) | Series A | $40M | bessemer venture partners, Picture Capital, red dot… | USA | Bold bags $40m funding round Bold, an enterprise cybersecurity company... The funding round brought in $40m from investors including… |
| 15 Apr 2026 | Hockeystack (hockeystack.com) | — | — ⚠ check sentence | bessemer venture partners, y combinator, uncorrelated… | — | new round of funding with contributions from Bessemer Venture Partners, Y Combinator and Uncorrelated Ventures, bringing the company’s… |
| 15 Apr 2026 | Hockeystack (hockeystack.com) | — | $50M ⚠ check sentence | bessemer venture partners, y combinator, uncorrelated… | USA | HockeyStack, the enterprise Revenue Agent platform, announced the launch of Revenue Agents for the Enterprise alongside a new round of… |
| 7 Apr 2026 | OFF/BEAT | — | $12M | bessemer venture partners | India | boAt co-founder Aman Gupta has raised Rs 100 crore in funding for his new startup OFF/BEAT. |
| 7 Apr 2026 | Offbeat Studios | — | $12M ⚠ check sentence | bessemer venture partners | India | Aman Gupta, cofounder of consumer electronics brand Boat, on Tuesday said that his new venture Offbeat Studios has raised Rs 100 crore.… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Bessemer --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Bessemer --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Bessemer --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Bessemer", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Bessemer", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [TPG Portfolio](tpg-portfolio.md)
- [A16Z Portfolio](a16z-portfolio.md)
- [Softbank Investments](softbank-investments.md)
- [Hillhouse Investments](hillhouse-investments.md)
