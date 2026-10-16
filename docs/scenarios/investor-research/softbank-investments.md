# Softbank Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “softbank investments” · 260/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [softbank-investments.json](../../examples/scenarios/softbank-investments.json).

**Question.** Which rounds did Softbank appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Softbank”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 139 |
| With a usable reported amount | 83 |
| Reported total (usable amounts) | $131.1B |
| Median reported round | $360.5M |
| Largest reported round | $22.5B |
| Amounts left out as implausible or unconverted | 46 |
| Busiest month | Mar 2026 (24 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3 | 3 | $512.3M | $10.8M | ██ |
| Jun 2025 | 8 | 4 | $711.5M | $98.2M | ███████ |
| Jul 2025 | 4 | 3 | $3.9B | $750M | ███ |
| Aug 2025 | 23 | 19 | $19.7B | $170.5M | ███████████████████ |
| Sep 2025 | 5 | 4 | $20.4B | $185.5M | ████ |
| Oct 2025 | 8 | 6 | $11.4B | $1.8B | ███████ |
| Nov 2025 | 4 | 3 | $2.1B | $500M | ███ |
| Dec 2025 | 12 | 8 | $51.1B | $4.8B | ██████████ |
| Jan 2026 | 20 | 15 | $34.4B | $480M | █████████████████ |
| Feb 2026 | 18 | 4 | $14.9B | $1.8B | ███████████████ |
| Mar 2026 | 24 | 11 | $3.2B | $225M | ████████████████████ |
| Apr 2026 | 10 | 3 | $600M | $300M | ████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 26 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Jan 2026 | Openai (openai.com) | Series E | $22.5B | SoftBank Vision Fund 2 | USA | SoftBank has a 11 per cent stake in OpenAI after making a $22.5 billion investment through its SoftBank Vision Fund 2 at the end of 2025. |
| 27 Sep 2025 | Tether (tether.to) | — | $20B | softbank group, ark investment management | United States | According to Bloomberg, venture capital giants SoftBank Group and ARK Investment Management are among potential investors considering a… |
| 19 Aug 2025 | Ampere (ampere.cars) | acquisition | $6.5B | softbank group | United States | SoftBank also acquired Ampere, a U.S.-based semiconductor design company focused on high-performance, energy efficient, sustainable AI… |
| 19 Jul 2025 | Perplexity AI (perplexity.ai) | — | $3B | SoftBank Group Vision Fund 2 | US | In 2024 June, Perplexity AI raised additional funding at $3 billion with investment from SoftBank Group Vision Fund 2. |
| 5 Dec 2025 | DayOne Data Centers | Series C | $2B | boyu capital, Coatue Management, Hillhouse Investment | Singapore | – DayOne Data Centers is in advanced talks to raise more than US$2 billion (S$2.6 billion) in an upsized Series C funding round to help… |
| 13 Oct 2025 | Wayve (wayve.ai) | — | $2B | microsoft, softbank | UK | British autonomous driving technology group Wayve is in talks with Microsoft and SoftBank to raise up to $2 billion in funding. |
| 19 Aug 2025 | Intel Corporation (intel.co.uk) | equity investment | $2B | softbank group | United States | SoftBank is buying $2 billion worth of stock in Intel Corporation’s common stock to drive the current AI revolution. |
| 2 Mar 2026 | Rapidus (rapidus.se) | — | $1.8B | Information-Technology Promotion Agency (IPA), Canon Inc.,… | Japan | Rapidus Corporation today announced that it has completed a funding round totaling 267.6 billion yen (equivalent to $1.7 billion USD) from… |
| 7 Nov 2025 | Metropolis (metropolis.vdtrxn) | Term Loan B & Series D | $1.6B | JPMorgan Chase Bank, N.A., liontree, bdt & msd partners | United States | Metropolis, a Los Angeles, CA-based company that applies artificial intelligence to real-world environments, has secured $1.6 billion in… |
| 14 Jan 2026 | Skild AI | Series C | $1.4B | softbank group, nventures, bezos expeditions | US | Skild AI, a Pittsburgh-based robotics AI startup, secured a mammoth $1.4 billion funding round to accelerate development of its… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Aidoc (aidoc.com) | Series E | $150M | Goldman Sachs Growth Equity, general catalyst, softbank… | — | Aidoc Raises $150M Series E for Clinical AI Scaling |
| 6 Apr 2026 | Openai (openai.com) | — | — ⚠ implausible size | amazon, nvidia, softbank | — | OpenAI has raised USD $122 billion in committed capital, valuing the company at USD $852 billion after the investment. The round was… |
| 2 Apr 2026 | Whoop (whoop.com) | Series G | $450M ⚠ check sentence | SoftBank Vision Fund 2, ivp, qatar investment authority | — | On April 1, 2026, WHOOP, the human performance company, announced the successful closing of a $450 million Series G funding round. Led by… |
| 1 Apr 2026 | OpenAI Group PBC | — | — ⚠ implausible size | Amazon.com Inc., nvidia, softbank group | — | OpenAI Group PBC has closed its largest funding round to date, raising $122 billion in committed capital at a post-money valuation of $852… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Softbank --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Softbank --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Softbank --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Softbank", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Softbank", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [A16Z Portfolio](a16z-portfolio.md)
- [Bessemer Investments](bessemer-investments.md)
- [Hillhouse Investments](hillhouse-investments.md)
- [Carlyle Investments](carlyle-investments.md)
