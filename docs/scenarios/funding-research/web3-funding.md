# Web3 Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “web3 funding” · 10/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [web3-funding.json](../../examples/scenarios/web3-funding.json).

**Question.** How many web3 deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “web3”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 52 |
| With a usable reported amount | 48 |
| Reported total (usable amounts) | $3.8B |
| Median reported round | $4.2M |
| Largest reported round | $2.5B |
| Busiest month | Jun 2025 (10 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 6 | 6 | $52.5M | $2.4M | ████████████ |
| Jun 2025 | 10 | 10 | $569.5M | $3.2M | ████████████████████ |
| Jul 2025 | 5 | 4 | $535.1M | $17.5M | ██████████ |
| Aug 2025 | 0 | 0 | — | — |  |
| Sep 2025 | 3 | 3 | $7.5M | $2.3M | ██████ |
| Oct 2025 | 7 | 5 | $98.8M | $13.5M | ██████████████ |
| Nov 2025 | 2 | 2 | $2.5B | $1.3B | ████ |
| Dec 2025 | 3 | 3 | $8.2M | $3.1M | ██████ |
| Jan 2026 | 6 | 6 | $99M | $3.5M | ████████████ |
| Feb 2026 | 5 | 5 | $355.9M | $7.5M | ██████████ |
| Mar 2026 | 1 | 1 | $2M | $2M | ██ |
| Apr 2026 | 4 | 3 | $30.5M | $7.5M | ████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 7 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 19 Nov 2025 | Obex (obex.es) | — | $2.5B | sky | — | Sky, which recently approved a governance vote to inject up to $2.5B of USDS stablecoins into Obex. |
| 30 Jul 2025 | Nano Labs (nano.cn) | Convertible promissory notes | $500M | — | — | Back on June 24, Nano Labs raised $500 million through convertible promissory notes. |
| 2 Feb 2026 | Rain (rain.agency) | Series C | $332.5M | bessemer venture partners, dragonfly, endeavor catalyst | — |  |
| 27 Jan 2026 | Jiuzi Holdings, Inc. | Non-binding MOU for strategic investment | $90M | morgan international | United States | Morgan International Finance Ltd under which Morgan International Finance intends to invest up to $90 million at a price of $3.00 per share. |
| 18 Oct 2025 | Astra Nova | — | $48.3M | outlier ventures, Investors from Saudi Arabia, Investors… | — | On October 18, Astra Nova raised $48.3 million to enhance its AI-powered Web3 content tools, with funding led by Outlier Ventures and… |
| 10 Jun 2025 | Hypernative (hypernative.io) | — | $40M | — | — | Hypernative raised $40 million to protect over $100 billion in crypto assets from real-time threats. |
| 2 May 2025 | Azen (azengroup.com) | equity | $40M | Royal Front LLC | UAE | In addition, aZen’s holding company has secured a $40 million equity investment from UAE-based Royal Front LLC to drive long-term… |
| 3 Jul 2025 | The Open Platform (top.co) | Series A | $28.5M | ribbit capital, pantera capital | United Arab Emirates | The Open Platform raised $28.5 million in an extended Series A funding round, led by Ribbit Capital, with Pantera Capital also… |
| 15 Oct 2025 | Yueda Digital Holding | — | $28M | — | USA | Yueda Digital Holding (Nasdaq: YDKG) (the 'Company'), a Web3 and digital-economy company with a focus on the long-term accumulation of… |
| 21 Apr 2026 | QLink World | Strategic Investment | $20M | foresight ventures | United Arab Emirates | Leading the Web3 super gateways: QLink World received $20 million strategic investment led by Foresight Ventures, aiming to jointly build… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 21 Apr 2026 | QLink World | Strategic Investment | $20M | foresight ventures | United Arab Emirates | Leading the Web3 super gateways: QLink World received $20 million strategic investment led by Foresight Ventures, aiming to jointly build… |
| 15 Apr 2026 | Claw Intelligence | seed | $3M | Castrum Istanbul, titans ventures, super labs | — | Claw Intelligence, a Web3 intelligent layer project, announced the completion of a $3 million seed round of financing. |
| 9 Apr 2026 | Oh | Series A | $7.5M | L1D, Auros Global, hashed | — | Web3 AI project Oh has completed a $7.5 million Series A funding round, led by Maven11 Capital, with participation from L1D, Auros Global,… |
| 8 Apr 2026 | Libeara (libeara.com) | — | — | gsr, sc ventures | — | market maker GSR led a funding round for Libeara, a tokenization platform backed by SC Ventures, to support its strategy of building a… |
| 26 Mar 2026 | PeakAI | seed | $2M | cogitent ventures, Covey Network, catchervc | — | PeakAI, an AI-powered Web3 marketing analytics platform, has closed a $2 million seed funding round backed by seven investors including… |
| 24 Feb 2026 | Based (getbased.com) | Series A | $11.5M | pantera capital, coinbase ventures, Wintermute Ventures | Singapore | Based, a Singapore‑based crypto/Web3 startup, has raised $11.5 million in a Series A round ... |
| 13 Feb 2026 | YOAKE | — | $3.2M | sony innovation fund | — | PANews reported on February 13th that YOAKE, a Web3 entertainment ecosystem project, announced an additional investment of approximately… |
| 13 Feb 2026 | YOAKE | Extended Seed | $1.2M ⚠ check sentence | — | — | YOAKE has raised approximately $4.45 million in total funding to date, including $1.25 million in the Extended Seed round completed in… |
| 12 Feb 2026 | Bullshot | — | $7.5M | animoca brands, TBV Ventures, OneAM Capital | — | $7.5 Million Raised from Top-Tier Investors |
| 2 Feb 2026 | Rain (rain.agency) | Series C | $332.5M | bessemer venture partners, dragonfly, endeavor catalyst | — |  |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector web3 --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector web3 --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector web3 --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "web3", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "web3", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Deep Tech Funding](deep-tech-funding.md)
- [Edtech Funding](edtech-funding.md)
- [Mobility Funding](mobility-funding.md)
- [Bridge Round Funding](bridge-round-funding.md)
