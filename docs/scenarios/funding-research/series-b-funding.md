# Series B Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “series b funding” · 320/month India · 1,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [series-b-funding.json](../../examples/scenarios/series-b-funding.json).

**Question.** How many series b deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** round type “series b”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 1,775 |
| With a usable reported amount | 1,673 |
| Reported total (usable amounts) | $118B |
| Median reported round | $35M |
| Largest reported round | $20B |
| Busiest month | Mar 2026 (177 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 107 | 103 | $4.9B | $33.6M | ████████████ |
| Jun 2025 | 132 | 127 | $5.2B | $32.5M | ███████████████ |
| Jul 2025 | 140 | 135 | $5.9B | $31M | ████████████████ |
| Aug 2025 | 155 | 149 | $5.6B | $30M | ██████████████████ |
| Sep 2025 | 169 | 163 | $21.5B | $37.5M | ███████████████████ |
| Oct 2025 | 169 | 163 | $32.9B | $35M | ███████████████████ |
| Nov 2025 | 130 | 123 | $5.4B | $34.8M | ███████████████ |
| Dec 2025 | 160 | 148 | $10.6B | $40M | ██████████████████ |
| Jan 2026 | 138 | 126 | $6.9B | $50M | ████████████████ |
| Feb 2026 | 170 | 161 | $8.3B | $37.5M | ███████████████████ |
| Mar 2026 | 177 | 161 | $9.1B | $35.5M | ████████████████████ |
| Apr 2026 | 128 | 114 | $6.5B | $41M | ██████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 15 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 9 Oct 2025 | Xai (x.ai) | Series A/Series B/etc. (undetermined) | $20B | nvidia, apollo global management, diameter capital partners | USA | Elon Musk’s AI startup xAI is raising more financing than initially planned, tapping backers including Nvidia Corp. to lift its ongoing… |
| 9 Sep 2025 | Anthropic (anthropic.com) | Series B | $13B | iconiq capital, amazon | — | Anthropic raised $13 billion in a round led by Iconiq Capital. |
| 30 Oct 2025 | Poolside (poolside.ai) | Series B | $2B ⚠ check sentence | nvidia, Existing investors (~$700m prior) | — | Poolside, an AI-coding assistant startup, is in discussions to raise up to $2 billion at a pre-money valuation near $12 billion, with… |
| 20 Oct 2025 | Reflection AI (reflectionai.ca) | Series B | $2B ⚠ check sentence | — | USA | Reflection AI closed a $2 billion Series B round at an $8 billion valuation, fueling advances in its artificial intelligence models and… |
| 17 Oct 2025 | Dayone (dayoneny.org) | Series B | $1.2B | — | Singapore | GDS founder, chairman, and CEO William Huang also serves as DayOne’s chairman, but GDS’s influence has waned as its stake dropped from… |
| 25 Sep 2025 | Nscale (nscale.com) | Series B | $1.1B | aker asa, nokia, Sandton Capital | United Kingdom | British artificial intelligence group Nscale has raised $1.1 billion from investors, including Norway's Aker ASA and Finland's Nokia, to… |
| 3 Oct 2025 | Domyn | Series B (planned) | $1.1B | — | Italy | The company is seeking to raise €1 billion over the next six months, a bold step to accelerate its AI gigafactory projects and expand its… |
| 2 Dec 2025 | Kalshi (kalshi.com) | Series B | $1B ⚠ check sentence | paradigm, sequoia capital, Andreessen Horowitz | — | Kalshi, which allows people to bet on future events, announced on Tuesday that it raised a $1 billion funding round at an $11 billion… |
| 14 Jul 2025 | Commonwealth Fusion Systems (cfs.energy) | Series B | $1B | Bill Gates | US | Major rounds include a whopping $1bn Series B for Bill Gates-backed Commonwealth Fusion Systems |
| 20 May 2025 | QXO | Series B Mandatory Convertible Preferred Stock | $1B | — | — | The aggregate gross proceeds from the offerings are expected to be $1.0B. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Parallel Web Systems | Series B | $10M ⚠ check sentence | sequoia capital, kleiner perkins, index ventures | — | Former Twitter (now X) CEO Parag Agrawal’s AI agentic platform Parallel Web Systems has raised a $100 million Series B at a $2 billion… |
| 30 Apr 2026 | Kimbal (kimbal.io) | Series B | $22M | gef capital partners, Niveshaay | India | Energy engineering company Kimbal Pvt Ltd on Thursday raised $22 million in a Series B funding round, led by sustainability-focused… |
| 29 Apr 2026 | Actively AI | Series B | $45M | tcv, First Harmonic, bain capital ventures | — | Actively AI Raises $45M Series B to Expand AI Go-To-Market Platform |
| 29 Apr 2026 | Firestorm Labs | Series B | $82M | washington harbour partners, nea, Ondas Holdings | — | Firestorm Labs Raises $82M Series B Funding for Deployable Drone Factories |
| 29 Apr 2026 | SPREAD AI | Series B | $30M | OTB Ventures, DTCP Growth, IQT | — | SPREAD AI Raises $30M in Series B Funding for Industrial Manufacturing AI |
| 29 Apr 2026 | Parallel Web Systems | Series B | $100M | sequoia capital | — | Parallel Web Systems Raises $100M Series B for AI Agents’ Web Infrastructure |
| 29 Apr 2026 | Sahi (sahi.com.tr) | Series B | $33M | accel, elevation capital, others | India | Sahi Raises $33 Mn Series B |
| 29 Apr 2026 | Rosi (rosi-solar.com) | Series B | $21.6M | InnoEnergy, cma cgm, european innovation council | Spain | From pv magazine Spain Rosi, a French cleantech company specializing in the recycling of end-of-life PV modules, has secured more than €20… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --round-type "series b" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --round-type "series b" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --round-type "series b" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"round_type": "series b", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"round_type": "series b", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Seed Funding](seed-funding.md)
- [Series A Funding](series-a-funding.md)
- [AI Startup Funding News](ai-startup-funding-news.md)
- [Series C Funding](series-c-funding.md)
