# Manufacturing Startup Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “manufacturing startup funding” · 10/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [manufacturing-startup-funding.json](../../examples/scenarios/manufacturing-startup-funding.json).

**Question.** How many manufacturing startup deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “manufacturing”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 671 |
| With a usable reported amount | 599 |
| Reported total (usable amounts) | $87.6B |
| Median reported round | $18M |
| Largest reported round | $14B |
| Amounts left out as implausible or unconverted | 3 |
| Busiest month | Mar 2026 (78 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 29 | 26 | $5B | $31.2M | ███████ |
| Jun 2025 | 64 | 60 | $3.9B | $13.5M | ████████████████ |
| Jul 2025 | 51 | 40 | $3.3B | $17M | █████████████ |
| Aug 2025 | 62 | 56 | $5.1B | $7.3M | ████████████████ |
| Sep 2025 | 60 | 57 | $11.9B | $34.5M | ███████████████ |
| Oct 2025 | 35 | 31 | $2.2B | $15.1M | █████████ |
| Nov 2025 | 52 | 49 | $1.7B | $8.2M | █████████████ |
| Dec 2025 | 48 | 42 | $6.4B | $10.1M | ████████████ |
| Jan 2026 | 70 | 63 | $8.9B | $32.6M | ██████████████████ |
| Feb 2026 | 65 | 54 | $13.4B | $24M | █████████████████ |
| Mar 2026 | 78 | 68 | $7.7B | $28.4M | ████████████████████ |
| Apr 2026 | 57 | 53 | $20.9B | $27.4M | ███████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 10 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 15 Apr 2026 | Tata Electronics (tata.com) | capital investment | $14B | tata group | India | The company is making a major $14 billion investment in semiconductor fabrication and assembly facilities. |
| 27 Feb 2026 | Prometheus (prometeoapi.com) | — | $6.2B ⚠ check sentence | — | United States | It raised $6.2 billion late last year at a valuation of about $30 billion, excluding any new funding now under discussion. |
| 18 Sep 2025 | Intel (intel.com) | investment | $5B | nvidia | USA | Nvidia announced Thursday that it will invest $5 billion in Intel, supporting the US chip manufacturer in difficulty, but did not offer a… |
| 24 Feb 2026 | Global Coffee Co. Pod Manufacturing Joint Venture | equity investment | $4B | apollo, kkr, Goldman Sachs Alternatives | — | That JV includes a $4bn investment co-led by Apollo and KKR, with participation from Goldman Sachs Alternatives, and remains subject to… |
| 8 Apr 2026 | BriHyNergy (brihynergy.com) | Pre-B | $2.8B | Shenzhen Energy Storage Fund | China | The raise saw the state-backed RMB 20bn ($2.9bn) electrochemical energy storage-focused Shenzhen Energy Storage Fund invest in the… |
| 10 Dec 2025 | Celsa (celsa.com.co) | debt refinancing | $1.9B | Strategic Value Partners, LLC and its affiliates (SVP) | UK | Celsa has announced the successful completion of its refinancing. As part of the transaction, Celsa is issuing €600m of HoldCo PIK notes,… |
| 2 Jun 2025 | Nippon Steel (nipponsteel.com) | government grant | $1.8B | Japanese government | Japan | Nippon Steel Corp. (NSC) will receive about $1.75 billion in Japanese government funding to help it expand its recycled-content electric… |
| 24 Dec 2025 | Si Group (siigroup.com) | recapitalization | $1.7B | — | USA | Significant deleveraging transaction resulting in an overall debt reduction of approximately $1.7 billion |
| 2 Aug 2025 | Braidy Industries (braidyindustries.com) | crowdfunding | $1.7B | United Co. Rusal | USA | United Co. Rusal, a Russian aluminum company, plans to invest $200 million in the project. |
| 1 Jul 2025 | Yuzhan Technology (India) Private Limited | investment | $1.5B | foxconn | India | Apple’s key supplier Foxconn has invested $1.48 billion (approximately Rs 12,800 crore) in its India operations over the past five days,… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 28 Apr 2026 | Velo3d (velo3d.com) | direct offering | $50M | — | United States | Velo3D, Inc. announced the closing of its previously announced firm commitment underwritten registered direct offering of 3,571,428 shares… |
| 24 Apr 2026 | Saffron (saffroncooks.com) | equity | $110.7M | POSCO-India Private Limited, POSCO Co., Ltd | India | The transaction involves the issuance of shares of Saffron Resources Private Limited, a wholly owned subsidiary of JSW Steel, to… |
| 23 Apr 2026 | Stch (stchgroup.com) | Pre-Series A | $7M | omnivore, kae capital, WVC | India | STCH, an AI startup focused on fabric development and textile manufacturing, has raised $7 million (around ₹66 crore) in a pre-Series A… |
| 23 Apr 2026 | Powerplus Energy (powerplus-energy.com.au) | — | $2.3M | Australian Renewable Energy Agency (ARENA) | Australia | Under the announcement, PowerPlus Energy will receive $2.32 million to expand and automate parts of its battery pack assembly line in… |
| 22 Apr 2026 | C-Infinity | — | $16M | canaan partners, inventus capital partners, bee partners | United States | C-Infinity announced it has raised $16 million in funding to accelerate development of its AI platform, AutoAssembler, which automates the… |
| 22 Apr 2026 | Atmos Space Cargo (atmos-space-cargo.com) | Series A | $27.8M | Balnord, Expansion Ventures, Keen Defence and Security | Germany | ATMOS Space Cargo has completed a €25.7 million Series A funding round, co-led by Balnord and Expansion Ventures, with support from Keen… |
| 21 Apr 2026 | Steel Exchange India (seil.co.in) | Preferential issue of convertible warrants | $42M | M/s India Coke and Power Private Limited, M/s IMR Steel… | India | Steel Exchange India Limited has received an aggregate amount of ₹75 Crore from M/s India Coke and Power Private Limited and M/s IMR Steel… |
| 17 Apr 2026 | PMGC Holdings Inc. | equity purchase facility | $40M | institutional investor | United States | PMGC Holdings Inc. (Nasdaq: ELAB) (“PMGC” or the “Company”), a diversified holding company executing a targeted roll-up strategy in… |
| 17 Apr 2026 | Evonith Steel | Non-Convertible Debentures | $30M | hdfc mutual fund | India | Furthermore, the Company has raised an additional INR 250 Cr of Non-Convertible Debenture’s (NCDs) from HDFC Mutual Fund further… |
| 16 Apr 2026 | NG Electro Products | — | $18M | JM Financial Private Equity, some family offices | India | Consumer goods-focused NG Electro Products on Thursday said it has raised Rs 150 crore from JM Financial Private Equity and some family… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector manufacturing --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector manufacturing --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector manufacturing --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "manufacturing", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "manufacturing", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Femtech Funding](femtech-funding.md)
- [Healthtech Funding](healthtech-funding.md)
- [Media Startup Funding](media-startup-funding.md)
- [Medtech Funding](medtech-funding.md)
