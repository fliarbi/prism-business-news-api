# Global Founders Capital Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “global founders capital investments” · 10/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [global-founders-capital-investments.json](../../examples/scenarios/global-founders-capital-investments.json).

**Question.** Which rounds did Global Founders Capital appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Global Founders Capital”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 8 |
| With a usable reported amount | 8 |
| Reported total (usable amounts) | $219.4M |
| Median reported round | $16M |
| Largest reported round | $93M |
| Busiest month | Oct 2025 (4 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1 | 1 | $17.3M | $17.3M | █████ |
| Jun 2025 | 1 | 1 | $93M | $93M | █████ |
| Jul 2025 | 0 | 0 | — | — |  |
| Aug 2025 | 0 | 0 | — | — |  |
| Sep 2025 | 0 | 0 | — | — |  |
| Oct 2025 | 4 | 4 | $49.1M | $13.6M | ████████████████████ |
| Nov 2025 | 0 | 0 | — | — |  |
| Dec 2025 | 0 | 0 | — | — |  |
| Jan 2026 | 0 | 0 | — | — |  |
| Feb 2026 | 2 | 2 | $60M | $60M | ██████████ |
| Mar 2026 | 0 | 0 | — | — |  |
| Apr 2026 | 0 | 0 | — | — |  |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 2 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 16 Jun 2025 | Aspora | — | $93M | sequoia capital, Greylock Partners, hummingbird ventures | United Kingdom | Aspora has announced a $93 million fundraise spread across three funding rounds. |
| 16 Feb 2026 | Entire (entire-directmarketing.com) | total equity funding | $60M | basis set ventures, cherry ventures, felicis | — | Entire has now raised a total of $60.0M in total equity funding and is backed by Basis Set Ventures, Cherry Ventures, Felicis, Garry Tan,… |
| 15 May 2025 | Orasio | — | $17.3M | frst, global founders capital, expeditions fund | — | Orasio, a start-up created in early 2025 and specialized in the processing of video feeds thanks to artificial intelligence, announces… |
| 23 Oct 2025 | Riff (321riff.com) | Series A | $16M | northzone, Skyfall Ventures, Maki.vc | Norway | Oslo-based Riff (formerly Databutton), the platform operators use to build and launch high-impact applications, has raised $16 million in… |
| 15 Oct 2025 | Chari (chari.com) | Series A | $12M | spe capital, Orange Ventures, Verod-Kepple | Morocco | Chari, the Moroccan startup supported by Y Combinator and founded in 2020 by the couple Ismael Belkhayat and Sophia Alj, announces a… |
| 24 Oct 2025 | Shuttle (shuttlebd.com) | Seed | $6M | y combinator, global founders capital, Thomas Dohmke | United Kingdom | Shuttle, a London, UK-based cloud infrastructure platform for developers, has raised $6 million in Seed funding. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 16 Feb 2026 | Entire (entire-directmarketing.com) | total equity funding | $60M | basis set ventures, cherry ventures, felicis | — | Entire has now raised a total of $60.0M in total equity funding and is backed by Basis Set Ventures, Cherry Ventures, Felicis, Garry Tan,… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "Global Founders Capital" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "Global Founders Capital" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "Global Founders Capital" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Global Founders Capital", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Global Founders Capital", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Redpoint Investments](redpoint-investments.md)
- [Spark Capital Investments](spark-capital-investments.md)
- [Techstars Portfolio](techstars-portfolio.md)
