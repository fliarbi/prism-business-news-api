# Payments Startup Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “payments startup funding” · volume below estimate threshold  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [payments-startup-funding.json](../../examples/scenarios/payments-startup-funding.json).

**Question.** How many payments startup deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “payments”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 245 |
| With a usable reported amount | 220 |
| Reported total (usable amounts) | $40B |
| Median reported round | $17.9M |
| Largest reported round | $20B |
| Amounts left out as implausible or unconverted | 1 |
| Busiest month | Jan 2026 (39 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 15 | 13 | $1.9B | $36M | ████████ |
| Jun 2025 | 22 | 17 | $678.1M | $14.2M | ███████████ |
| Jul 2025 | 14 | 14 | $506.3M | $12M | ███████ |
| Aug 2025 | 18 | 16 | $1.2B | $4.9M | █████████ |
| Sep 2025 | 14 | 14 | $3.1B | $10M | ███████ |
| Oct 2025 | 21 | 16 | $1.3B | $21.5M | ███████████ |
| Nov 2025 | 14 | 12 | $1.2B | $24.8M | ███████ |
| Dec 2025 | 24 | 23 | $21.9B | $48.2M | ████████████ |
| Jan 2026 | 39 | 36 | $1.3B | $46M | ████████████████████ |
| Feb 2026 | 36 | 32 | $1.7B | $15M | ██████████████████ |
| Mar 2026 | 15 | 15 | $3.5B | $25M | ████████ |
| Apr 2026 | 13 | 12 | $1.8B | $4M | ███████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 16 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 21 Dec 2025 | Paypay (paypay.ne.jp) | IPO | $20B | — | Japan | The offering is expected to raise over $20 billion. |
| 9 Mar 2026 | Easebuzz (easebuzz.in) | — | $2.9B | bessemer venture partners | India | In April 2025, Bessemer led the Rs 240 crore infusion into the company. |
| 15 Sep 2025 | Tamara (tamara.co) | Asset-backed facility | $2.4B | goldman sachs, citi, apollo funds | Saudi Arabia | Tamara, the first homegrown Saudi fintech unicorn, has secured the largest asset-backed facility of its kind in the region of up to $2.4… |
| 12 Aug 2025 | Priority Technology Holdings, Inc. | credit facility | $1.1B | — | United States | Priority Technology Holdings, Inc. (“Priority” or the “Company”), the payments and banking solution that streamlines collecting, storing,… |
| 28 Apr 2026 | Cobrar CloudWalk Bela (FIDC) | — | $1.1B | Cloudwalk Institutição de Pagamento e Serviços LTDA.,… | Brazil | Limited Liability Quotas Class A of the Segment of Payments of the Investment Fund in Accounts by Cobrar CloudWalk Bela (FIDC) issued… |
| 8 May 2025 | Shift4 Payments (shift4.com) | Euro Notes | $734.4M | — | United States | Shift4 Payments, Inc. (NYSE: FOUR), a leader in integrated payments and commerce technology, today announced that its subsidiaries, Shift4… |
| 30 Apr 2026 | Ebury (ebury.com) | Financing | $698.5M | centerbridge partners, santander, vitruvian partners | — | Santander will invest 50 million pounds (67.4 million dollars) in its international payment technology company Ebury, as part of a round… |
| 10 Nov 2025 | Worldline (worldline.com) | — | $540M | — | — | Payments processor Worldline is to raise €500m to support its turnaround. |
| 18 Oct 2025 | Tempo (heytempo.com) | Series A | $500M | greenoaks, thrive capital, sequoia capital | — | Tempo, a Layer 1 blockchain project, received $500 million in Series A funding from prominent venture capitalists Greenoaks and Thrive… |
| 27 Oct 2025 | Rapyd Financial | — | $469.9M | — | UK | NScale securing a £1.1bn investment with other major deals including Rapyd Financial, which offers payments, mobile wallets, money… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Ebury (ebury.com) | Financing | $698.5M | centerbridge partners, santander, vitruvian partners | — | Santander will invest 50 million pounds (67.4 million dollars) in its international payment technology company Ebury, as part of a round… |
| 30 Apr 2026 | Oolka (oolka.in) | Series A | $14M | accel, lightspeed, Z47 | India | Oolka has raised $14 million in a Series A funding round led by Accel, with participation from existing investors Lightspeed and Z47. |
| 28 Apr 2026 | Cobrar CloudWalk Bela (FIDC) | — | $1.1B | Cloudwalk Institutição de Pagamento e Serviços LTDA.,… | Brazil | Limited Liability Quotas Class A of the Segment of Payments of the Investment Fund in Accounts by Cobrar CloudWalk Bela (FIDC) issued… |
| 28 Apr 2026 | Tapaya | pre-seed | $1.1M | passion capital, depo ventures, BADideas.fund | Czech Republic | Prague-based payments infrastructure startup Tapaya has raised €1 million in a pre-seed funding round led by Passion Capital, with co-lead… |
| 22 Apr 2026 | Cresora Commerce | initial | $4M | nashville capital network | US | Cresora Commerce, a US-based AI-native commerce infrastructure platform, has announced its official launch alongside the close of an… |
| 15 Apr 2026 | SolvaPay | pre-seed | $2.6M | redstone, ms&ad ventures, antler | Sweden | SolvaPay, a Stockholm, Sweden-based provider of an AI payments platform, raised €2.4m ($2.8M) in pre‑seed funding. The round was led by… |
| 13 Apr 2026 | Ralio | — | $25M | — | — | Ralio has successfully raised $25 million in a recent funding round aimed at enhancing its agentic payments platform. |
| 13 Apr 2026 | Ralio | Pre-seed | $2.5M | — | UK | Fintech startup Ralio has just raised $2.5 million of pre-seed funding to make AI agentic payments safer. |
| 13 Apr 2026 | Ralio | pre-Seed | $2.3M | Seed X, love ventures, plug and play | United Kingdom | Ralio, a London-based FinTech startup building a payments platform tailored for business AI agents, has announced a €2.1 million ($2.5… |
| 10 Apr 2026 | Depay (depay.com) | — | $4M | CMT Global, dcg, verda ventures | Argentina | Depay, Argentina's real-time payment infrastructure startup, announced that it has just raised $4 million to accelerate its network… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector payments --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector payments --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector payments --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "payments", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "payments", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Lending Startup Funding](lending-startup-funding.md)
- [Martech Funding](martech-funding.md)
- [Pet Care Startup Funding](pet-care-startup-funding.md)
