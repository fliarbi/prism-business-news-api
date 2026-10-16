# Construction Tech Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “construction tech funding” · volume below estimate threshold  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [construction-tech-funding.json](../../examples/scenarios/construction-tech-funding.json).

**Question.** How many construction tech deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “construction”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 288 |
| With a usable reported amount | 249 |
| Reported total (usable amounts) | $5.8B |
| Median reported round | $8.5M |
| Largest reported round | $415M |
| Amounts left out as implausible or unconverted | 1 |
| Busiest month | Sep 2025 (39 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 38 | 32 | $457.1M | $6.5M | ███████████████████ |
| Jun 2025 | 18 | 17 | $440.7M | $10.5M | █████████ |
| Jul 2025 | 19 | 15 | $681.4M | $8M | ██████████ |
| Aug 2025 | 10 | 8 | $141.9M | $13.9M | █████ |
| Sep 2025 | 39 | 29 | $441.4M | $6.5M | ████████████████████ |
| Oct 2025 | 26 | 25 | $716.6M | $10M | █████████████ |
| Nov 2025 | 28 | 24 | $727M | $10M | ██████████████ |
| Dec 2025 | 28 | 24 | $510.7M | $12.5M | ██████████████ |
| Jan 2026 | 16 | 13 | $291.2M | $4.4M | ████████ |
| Feb 2026 | 28 | 27 | $1.1B | $4.6M | ██████████████ |
| Mar 2026 | 18 | 18 | $279.5M | $10.5M | █████████ |
| Apr 2026 | 20 | 17 | $146.3M | $5.4M | ██████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 16 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 25 Nov 2025 | Companycam (companycam.com) | late-stage equity investment | $415M | b capital | USA | Leaders at CompanyCam declined to disclose the amount raised during the round. However, data from private capital market research platform… |
| 4 Feb 2026 | Bedrock Robotics | — | $300M | capitalg, Nvidia’s venture arm, Valor Equity Partners’… | — | Proptech startup Bedrock Robotics has nailed down nearly $300M to accelerate the construction process, especially for data centers. |
| 30 Oct 2025 | Dexco (dexcoinc.com) | public issuance of unsecured, non-convertible debentures | $300M | — | Brazil | Dexco’s third public issuance of unsecured, non-convertible debentures, totaling BRL 1.5 billion (approx. USD 279 million) |
| 4 Jul 2025 | Shapoorji Pallonji (shapoorji.in) | loan | $300M | — | India | Shapoorji Pallonji & Co., the construction arm of the Shapoorji Pallonji Group, is in talks with banks to borrow about USD 300 million… |
| 11 Jun 2025 | Corporate Strategies | debt financing | $200M | bank, private lender | — | Corporate Strategies completed a $200 million debt financing and $65 million recapitalization for one of the nation’s oldest full-service,… |
| 26 Jan 2026 | Ramery (ramery.fr) | structured financing plan | $172.8M | septentrion | — | Ramery (3,000 employees, 700 million euros from CA 2025) signed a structured financing plan of 160 million euros at the end of January… |
| 29 May 2025 | Buildots (buildots.com) | Series D | $166M | qumra capital, OG Venture Partners, tlv partners | USA | Buildots, a Chicago-based AI-driven construction tech startup, raised $45 million in a Series D round. |
| 7 Jul 2025 | Infra.market (infra.market) | Debt | $150M | Mars Growth Capital | India | Infra.Market has raised $150 million in structured debt financing from Mars Growth Capital, a joint venture between MUFG and Liquidity… |
| 8 Jul 2025 | Morgan Construction (morganconstruction.org) | Credit Facility | $148M | gordon brothers | Canada | On July 8, 2025, Gordon Brothers announced that they have agented C$200 million in financing, consisting of a five-year C$150 million… |
| 22 Oct 2025 | North American Construction Group (nacg.ca) | private placement | $125M | National Bank Capital Markets, ATB Securities Inc., scotia… | Canada | North American Construction Group Ltd. (“NACG”) announced the closure of its private placement offering of an additional $125 million… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Highway Data Systems (highwaydata.co.uk) | — | $1.6M | Investment Fund for Scotland, maven capital partners,… | UK | Growth support Rob Stevenson of Maven and Joe Charlesworth Highway Data Systems, which provides quality assurance technology to the road… |
| 29 Apr 2026 | Monumental (monumental.co) | seed | $25M | — | — | As we previously covered, Monumental, a Dutch startup, has built a working bricklaying robot that has already completed commercial… |
| 29 Apr 2026 | All3 | seed | $25M | rtp global, SuperSeed, begin capital | — | All3, a construction robotics company, has raised $25 million in seed funding to bring its robotic construction platform to market. |
| 28 Apr 2026 | TimberHP (timberhp.com) | Strategic investment | — | FTAI Infrastructure, blackrock, finance authority of maine | United States | TimberHP, the first U.S.-based manufacturer of wood fiber insulation, today announced a strategic investment from FTAI Infrastructure Inc. |
| 17 Apr 2026 | Ballas (ballas.biz) | Series B | $15M | SMBC Edge, Z Venture Capital | Japan | Japanese construction technology company BALLAS Inc. raised $15 million (¥2.4 billion) in a Series B round co-led by SMBC Edge and Z… |
| 15 Apr 2026 | Ballas (ballas.biz) | Series B | — | persol venture partners | Japan | Persol Holdings has invested in the Series B round of Tokyo-based Ballas, a company that designs, develops, manufactures and sells… |
| 14 Apr 2026 | Conxai (conxai.com) | Series A | $5.8M | baybg venture capital, capricorn partners, pi labs | Germany | Conxai, a Munich, Germany-based provider of a construction tech platform, raised $5.8m in Series A funding. |
| 14 Apr 2026 | Alliance Tool Hire | investment | $381k | Alliance Tool Hire | United Kingdom | A Poole-based construction rental supplier has invested £300,000 in launching a dedicated lifting division |
| 14 Apr 2026 | Primepoint (primepoint.com) | seed | $10M | penny jar capital, nextview ventures, navitas capital | United States | Primepoint, a San Mateo, CA-based provider of a construction intelligence platform for workflows project teams, raised $10M in seed funding. |
| 9 Apr 2026 | Goldfields Testing Laboratory | grant | $43k | — | Australia | Kalgoorlie-Boulder-based Goldfields Testing Laboratory has secured $43,000 to establish a local round determinate panel testing service, a… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector construction --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector construction --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector construction --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "construction", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "construction", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [B2b Marketplace Funding](b2b-marketplace-funding.md)
- [Battery Startup Funding](battery-startup-funding.md)
- [Defence Tech Funding](defence-tech-funding.md)
- [E-commerce Funding](e-commerce-funding.md)
