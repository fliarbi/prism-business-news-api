# Benchmark Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “benchmark investments” · 70/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [benchmark-investments.json](../../examples/scenarios/benchmark-investments.json).

**Question.** Which rounds did Benchmark appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Benchmark”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 61 |
| With a usable reported amount | 58 |
| Reported total (usable amounts) | $10.4B |
| Median reported round | $80M |
| Largest reported round | $2.8B |
| Busiest month | Oct 2025 (11 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 5 | 5 | $581.2M | $78.1M | █████████ |
| Jun 2025 | 2 | 2 | $80M | $40M | ████ |
| Jul 2025 | 5 | 3 | $105M | $30M | █████████ |
| Aug 2025 | 3 | 3 | $210M | $100M | █████ |
| Sep 2025 | 9 | 8 | $1.3B | $30M | ████████████████ |
| Oct 2025 | 11 | 11 | $2B | $150M | ████████████████████ |
| Nov 2025 | 6 | 6 | $540.6M | $40M | ███████████ |
| Dec 2025 | 0 | 0 | — | — |  |
| Jan 2026 | 2 | 2 | $100M | $50M | ████ |
| Feb 2026 | 3 | 3 | $1B | $1B | █████ |
| Mar 2026 | 9 | 9 | $4.3B | $360M | ████████████████ |
| Apr 2026 | 6 | 6 | $299.7M | $47.5M | ███████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 26 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 24 Mar 2026 | Cerebras Systems (cerebras.net) | Series H | $2.8B | 1789 Capital, alpha wave global, altimeter capital | USA |  |
| 10 Mar 2026 | Legora | Series D | $550M | accel, benchmark, bessemer venture partners | Sweden | Legora Raises $550M in Series D Funding to Expand AI in Legal Operations |
| 2 Nov 2025 | Mercor (mercor.com) | total equity funding | $483.6M | benchmark, felicis, general catalyst | United States | Mercor has now raised a total of $483.6M in total equity funding and is backed by Benchmark, Felicis, General Catalyst, and Robinhood… |
| 30 May 2025 | Clickhouse (clickhouse.com) | Series C | $350M | khosla ventures, bond, ivp | USA | ClickHouse, Inc., a leader in real-time analytics, data warehousing, observability, and AI/ML, today announced it has raised $350 million… |
| 6 Apr 2026 | Starcloud (starcloud.ee) | total equity | $193.9M | 3C AGI Partners, adjacent, benchmark | United States | Starcloud has now raised a total of $193.9M in total equity funding and is backed by 3C AGI Partners, Adjacent, Benchmark, Carya Venture… |
| 16 Mar 2026 | Sunday (sundayapp.com) | — | $165M | bain capital ventures, benchmark, coatue | USA | Sunday – $165.0M |
| 22 Oct 2025 | Langchain (langchain.com) | Series B | $125M ⚠ check sentence | ivp, capitalg, sapphire ventures | — | LangChain has raised $125 million, boosting its valuation to $1.25 billion, the company announced on Monday. |
| 9 Aug 2025 | Applied Compute | — | $100M | benchmark | — | Benchmark’s investment valued Applied Compute at $100 million, Upstarts Media reported. |
| 9 Aug 2025 | Decart (decart.bg) | Series B | $100M | sequoia capital, benchmark, zeev ventures | USA | Decart … raised $100 million in Series B funding… |
| 4 Sep 2025 | Exa (exa.ai) | Series B | $85M ⚠ check sentence | benchmark, lightspeed, y combinator | USA | San Francisco-based AI search infrastructure startup, Exa (formerly Metaphor), has raised $85 million in a Series B round at a $700… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 27 Apr 2026 | Acuitymd (acuitymd.com) | — | $80M | atreides management, benchmark, iconiq growth | US | Boston-based AcuityMD a medtech intelligence platform that leverages AI and precise data to support commercial decision-making. |
| 16 Apr 2026 | Eigen (eigen.io) | seed | $15M | benchmark, Ben Silbermann, David Singleton | — | The stealth AI startup has raised a $15 million seed round from Benchmark with Pinterest founder Ben Silbermann and Dreamer founder David… |
| 6 Apr 2026 | Starcloud (starcloud.ee) | total equity | $193.9M | 3C AGI Partners, adjacent, benchmark | United States | Starcloud has now raised a total of $193.9M in total equity funding and is backed by 3C AGI Partners, Adjacent, Benchmark, Carya Venture… |
| 1 Apr 2026 | Voltalia (voltalia.com) | regulated agreement | $10.8M | benchmark shareholder | — | Voltalia announces the signing of a regulated agreement for a financing of EUR 100 million, granted by its benchmark shareholder, in the… |
| 30 Mar 2026 | Starcloud (starcloud.ee) | Series A | $170M | benchmark, eqt ventures | United States | Starcloud Raises $170M in Series A Funding for Space Data Centers |
| 24 Mar 2026 | Cerebras Systems (cerebras.net) | Series H | $2.8B | 1789 Capital, alpha wave global, altimeter capital | USA |  |
| 16 Mar 2026 | Sunday (sundayapp.com) | — | $165M | bain capital ventures, benchmark, coatue | USA | Sunday – $165.0M |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Benchmark --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Benchmark --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Benchmark --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Benchmark", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Benchmark", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Carlyle Investments](carlyle-investments.md)
- [Warburg Pincus Portfolio](warburg-pincus-portfolio.md)
- [General Atlantic Portfolio](general-atlantic-portfolio.md)
- [Tiger Global Portfolio](tiger-global-portfolio.md)
