# Series D Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “series d funding” · 90/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [series-d-funding.json](../../examples/scenarios/series-d-funding.json).

**Question.** How many series d deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** round type “series d”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 384 |
| With a usable reported amount | 370 |
| Reported total (usable amounts) | $97.3B |
| Median reported round | $100M |
| Largest reported round | $16B |
| Amounts left out as implausible or unconverted | 2 |
| Busiest month | Jan 2026 (51 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 25 | 23 | $1.9B | $93M | ██████████ |
| Jun 2025 | 35 | 35 | $3.3B | $75M | ██████████████ |
| Jul 2025 | 15 | 14 | $999M | $57.5M | ██████ |
| Aug 2025 | 47 | 46 | $3.8B | $60.3M | ██████████████████ |
| Sep 2025 | 37 | 37 | $24.4B | $150M | ███████████████ |
| Oct 2025 | 23 | 22 | $3.5B | $105M | █████████ |
| Nov 2025 | 23 | 22 | $12.4B | $500M | █████████ |
| Dec 2025 | 26 | 25 | $3.2B | $104M | ██████████ |
| Jan 2026 | 51 | 51 | $10.9B | $128M | ████████████████████ |
| Feb 2026 | 47 | 47 | $24.9B | $117M | ██████████████████ |
| Mar 2026 | 37 | 32 | $21.7B | $101.5M | ███████████████ |
| Apr 2026 | 18 | 16 | $4.9B | $155M | ███████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 19 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 27 Mar 2026 | Waymo (waymo.com) | Series D | $16B | alphabet, Andreessen Horowitz, bdt & msd partners | — | Mountain View-based Waymo is a mobility technology company that improves transportation by developing self‑driving solutions for travelers… |
| 3 Sep 2025 | Anthropic (anthropic.com) | Series D | $13B | iconiq, Fidelity Management & Research, lightspeed venture… | — | The funding round was led by Iconiq, Fidelity Management & Research, and Lightspeed Venture Partners. Heavyweights like Altimeter, General… |
| 24 Jan 2026 | Xai (x.ai) | Series D | $5.3B | — | — | This was followed by $5.3 billion in equity and debt in 2025. |
| 15 Sep 2025 | Tamara (tamara.co) | Series D (facility) | $2.4B | goldman sachs, citi, Apollo-managed funds | Saudi Arabia | Tamara has secured up to $2.4 billion in fresh funding backed by Goldman Sachs, Citi, and Apollo-managed funds. |
| 14 Nov 2025 | Anysphere (anysphere.inc) | Series D | $2.3B | accel, coatue, nvidia | United States | AI coding startup Anysphere completed a $2.3 billion Series D funding round on Thursday, valuing the company at $29.3 billion. Accel and… |
| 13 Nov 2025 | Cursor (cursor.com) | Series D | $2.3B ⚠ check sentence | accel, coatue, Andreessen Horowitz | United States | Cursor has vaulted into the top tier of private AI companies after securing a massive $2.3 billion Series D at a $29.3 billion valuation. |
| 3 Apr 2026 | Saronic (saronic.com) | Series D | $1.8B | kleiner perkins | United States | Leading the pack was Saronic's monumental $1.75 billion Series D funding round, the largest ever for an Austin-based startup and a boon… |
| 7 Nov 2025 | Metropolis (metropolis.vdtrxn) | Term Loan B & Series D | $1.6B | JPMorgan Chase Bank, N.A., liontree, bdt & msd partners | United States | Metropolis, a Los Angeles, CA-based company that applies artificial intelligence to real-world environments, has secured $1.6 billion in… |
| 25 Feb 2026 | Wayve (wayve.ai) | Series D | $1.5B ⚠ check sentence | uber, nvidia, microsoft | United Kingdom | Wayve said including “additional milestone-based” investments from Uber, it has secured $1.5bn (R23,887,442,400) in funding with this… |
| 10 Nov 2025 | PT Garuda Indonesia | Series D | $1.5B | state asset fund Danantara | Indonesia | National airline PT Garuda Indonesia plans to issue 315.6 billion series D shares to raise Rp 23.67 trillion (US$1.4 billion), comprising… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Rogo (rogodata.com) | Series D | $160M | kleiner perkins, sequoia capital, thrive | USA | Rogo Raises $160M in Series D Funding for Finance AI Platform |
| 29 Apr 2026 | Hightouch (hightouch.com) | Series D | $150M | iconiq capital, sapphire ventures, amplify partners | United States | Hightouch , the leader in data and AI for marketing, today announced a $150 million Series D financing led by Growth Equity at Goldman… |
| 28 Apr 2026 | Snabbit | Series D | $56M | Susquehanna Venture Capital, Mirae Asset Venture… | India | Snabbit, an Indian on-demand home services startup, has closed a $56 million funding round, confirming TechCrunch’s earlier report. |
| 28 Apr 2026 | True Anomaly (trueanomaly.space) | Series D | $650M | eclipse, riot ventures, paradigm | USA | True Anomaly today announced its $650 million Series D funding round. |
| 26 Apr 2026 | Snabbit | Series D | — | Mirae Asset Venture Investments, bertelsmann india… | India | Bengaluru-based startup Snabbit is in advanced talks to secure $50-60 million in fresh funding. |
| 17 Apr 2026 | Wayve (wayve.ai) | Series D extension | $60M | qualcomm, amd, arm | UK | The extension totals $60 million and adds three household names in automotive computing to a shareholder register that already spans cloud… |
| 16 Apr 2026 | Wayve (wayve.ai) | Series D | $1.3B | amd, arm, qualcomm ventures | UK | Wayve, a company specialized in autonomous driving, has expanded its Series D financing round by $60 million. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --round-type "series d" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --round-type "series d" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --round-type "series d" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"round_type": "series d", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"round_type": "series d", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Biotech Funding News](biotech-funding-news.md)
- [Crypto Funding](crypto-funding.md)
- [Gaming Funding](gaming-funding.md)
- [Fintech Funding](fintech-funding.md)
