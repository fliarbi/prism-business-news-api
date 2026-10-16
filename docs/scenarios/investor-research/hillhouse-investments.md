# Hillhouse Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “hillhouse investments” · 210/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [hillhouse-investments.json](../../examples/scenarios/hillhouse-investments.json).

**Question.** Which rounds did Hillhouse appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Hillhouse”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 17 |
| With a usable reported amount | 12 |
| Reported total (usable amounts) | $5.8B |
| Median reported round | $217.5M |
| Largest reported round | $2B |
| Busiest month | Apr 2026 (5 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 0 | 0 | — | — |  |
| Jun 2025 | 0 | 0 | — | — |  |
| Jul 2025 | 0 | 0 | — | — |  |
| Aug 2025 | 1 | 1 | $36.8M | $36.8M | ████ |
| Sep 2025 | 1 | 1 | $140M | $140M | ████ |
| Oct 2025 | 1 | 1 | $1.8B | $1.8B | ████ |
| Nov 2025 | 0 | 0 | — | — |  |
| Dec 2025 | 2 | 1 | $2B | $2B | ████████ |
| Jan 2026 | 1 | 1 | $235M | $235M | ████ |
| Feb 2026 | 2 | 1 | $235M | $235M | ████████ |
| Mar 2026 | 4 | 3 | $987M | $493.5M | ████████████████ |
| Apr 2026 | 5 | 3 | $630M | $120M | ████████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 3 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 5 Dec 2025 | DayOne Data Centers | Series C | $2B | boyu capital, Coatue Management, Hillhouse Investment | Singapore | – DayOne Data Centers is in advanced talks to raise more than US$2 billion (S$2.6 billion) in an upsized Series C funding round to help… |
| 20 Mar 2026 | Earendil Labs | — | $787M | Dimension Capital, dst global, ince capital | USA | Earendil Labs, an AI-driven biotechnology company advancing next-generation biologics, announced that it has raised $787 million in… |
| 16 Apr 2026 | Tars (hellotars.com) | Pre-A | $455M | Hillhouse Ventures, Sequoia China, Meituan Longzhu | China | Gasgoo Munich- Gasgoo has learned that TARS has officially closed a $455 million (roughly 3.1 billion yuan) Pre-A funding round. |
| 5 Feb 2026 | Tenpoint Therapeutics (tenpointtherapeutics.com) | Series B | $235M | Hillhouse Family Office | — | Innovative eye treatment firm, Tenpoint Therapeutics, has raised $235M in a Series B round with support from Hillhouse Family Office |
| 24 Mar 2026 | Aridge | equity | $200M | Gaorong Ventures, Fortune Capital, hillhouse capital | — | Aridge, the flying car subsidiary of Xpeng, raised nearly USD 200 million in an equity round from Gaorong Ventures, Fortune Capital,… |
| 25 Sep 2025 | Beatbot (beatbot.tech) | — | $140M | DragonBall Capital, hillhouse capital, shunwei capital | China | Beatbot , a consumer robotics developer, has raised around RMB 1 billion (USD 140 million) in a new round led by DragonBall Capital, the… |
| 17 Apr 2026 | D-Robotics | Series B1 | $120M | Synstellation Capital, didi, Meituan Longzhu | — | Chinese robot technology startup D-Robotics, a unit spun off from autonomous-driving startup Horizon Robotics, has raised $120 million in… |
| 29 Apr 2026 | Axoft (axoft.us) | Series A | $55M | C.P. Group Innovation, alumni ventures, Stanford… | — | Axoft Raises $55M Series A for Implantable Brain-Computer Interfaces |
| 5 Aug 2025 | CarDekho.com | — | $36.8M | hillhouse capital, Tyborn Capital | — | Auto Classified Portal CarDekho.com has raised Rs 307 crore in the Leadership of Chinese Funds Hillhouse Capital and Tyborn Capital and $… |
| 28 Apr 2026 | Elegoo (elegoo.com) | Series B+ | — | Meituan’s DragonBall Capital, Shenzhen Capital Group,… | — | Elegoo, one of China’s leading 3D printing companies, has raised a nine-figure RMB sum in a Series B+ round. The round was jointly backed… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Axoft (axoft.us) | Series A | $55M | C.P. Group Innovation, alumni ventures, Stanford… | — | Axoft Raises $55M Series A for Implantable Brain-Computer Interfaces |
| 28 Apr 2026 | Elegoo (elegoo.com) | Series B+ | — | Meituan’s DragonBall Capital, Shenzhen Capital Group,… | — | Elegoo, one of China’s leading 3D printing companies, has raised a nine-figure RMB sum in a Series B+ round. The round was jointly backed… |
| 17 Apr 2026 | D-Robotics | Series B1 | $120M | Synstellation Capital, didi, Meituan Longzhu | — | Chinese robot technology startup D-Robotics, a unit spun off from autonomous-driving startup Horizon Robotics, has raised $120 million in… |
| 16 Apr 2026 | Tars (hellotars.com) | Pre-A | $455M | Hillhouse Ventures, Sequoia China, Meituan Longzhu | China | Gasgoo Munich- Gasgoo has learned that TARS has officially closed a $455 million (roughly 3.1 billion yuan) Pre-A funding round. |
| 13 Apr 2026 | Quest Global (quest-global.com) | Minority equity investment | — | Hillhouse Investment | — | Quest Global, a leading engineering services company, has entered into definitive agreements with global investment firm Hillhouse… |
| 24 Mar 2026 | Aridge | equity | $200M | Gaorong Ventures, Fortune Capital, hillhouse capital | — | Aridge, the flying car subsidiary of Xpeng, raised nearly USD 200 million in an equity round from Gaorong Ventures, Fortune Capital,… |
| 20 Mar 2026 | Earendil Labs | — | $787M | Dimension Capital, dst global, ince capital | USA | Earendil Labs, an AI-driven biotechnology company advancing next-generation biologics, announced that it has raised $787 million in… |
| 10 Mar 2026 | Metanovas (metanovas.com) | Series A+ | — | GRC SinoGreen Capital, hillhouse capital, Kangaroo Mommy… | — | MetaNovas, an AI‑driven drug discovery company, has completed its Series A+ and Series A++ rounds with backing from GRC SinoGreen Capital,… |
| 11 Feb 2026 | AGILINK | — | — | BV Baidu Ventures, YF Capital, Synstellation Capital | — | Gasgoo Munich-AGILINK recently announced the completion of a new financing round worth hundreds of millions of yuan. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Hillhouse --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Hillhouse --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Hillhouse --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Hillhouse", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Hillhouse", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Bessemer Investments](bessemer-investments.md)
- [Softbank Investments](softbank-investments.md)
- [Carlyle Investments](carlyle-investments.md)
- [Warburg Pincus Portfolio](warburg-pincus-portfolio.md)
