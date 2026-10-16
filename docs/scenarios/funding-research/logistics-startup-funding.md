# Logistics Startup Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “logistics startup funding” · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [logistics-startup-funding.json](../../examples/scenarios/logistics-startup-funding.json).

**Question.** How many logistics startup deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “logistics”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 431 |
| With a usable reported amount | 344 |
| Reported total (usable amounts) | $58.7B |
| Median reported round | $19M |
| Largest reported round | $8.4B |
| Amounts left out as implausible or unconverted | 5 |
| Busiest month | Nov 2025 (44 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 29 | 25 | $841.2M | $13.6M | █████████████ |
| Jun 2025 | 33 | 25 | $2.3B | $9.3M | ███████████████ |
| Jul 2025 | 33 | 26 | $7.5B | $14.5M | ███████████████ |
| Aug 2025 | 34 | 25 | $6.3B | $30M | ███████████████ |
| Sep 2025 | 37 | 31 | $3.9B | $28.2M | █████████████████ |
| Oct 2025 | 35 | 24 | $1.8B | $12.4M | ████████████████ |
| Nov 2025 | 44 | 41 | $2.7B | $14.4M | ████████████████████ |
| Dec 2025 | 37 | 23 | $3.2B | $23.8M | █████████████████ |
| Jan 2026 | 36 | 32 | $13.6B | $19M | ████████████████ |
| Feb 2026 | 39 | 31 | $10.2B | $16M | ██████████████████ |
| Mar 2026 | 33 | 26 | $3.3B | $55M | ███████████████ |
| Apr 2026 | 41 | 35 | $6.1B | $64.1M | ███████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 15 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 9 Feb 2026 | Inpost (inpost.pl) | acquisition | $8.4B | fedex, advent, A&R | Poland | Parcel locker group InPost has agreed to be bought by a consortium led by delivery giant FedEx and private equity firm Advent for 7.8… |
| 21 Jan 2026 | Adani Ports and Special Economic Zone (adaniports.com) | Bond Issuance | $6B | life insurance corporation of india | India | Earlier this financial year, another group company, Adani Ports and Special Economic Zone, raised ₹5,000 crore by placing 15-year bonds… |
| 28 Jul 2025 | Transnet (transnet.com) | Guarantee | $5.3B | South African Government | South Africa | The South African Government will grant Transnet an additional guarantee of R94.8 billion (5.34 billion dollars) to support the recovery… |
| 8 Apr 2026 | Ad Ports Group (adportsgroup.com) | Debt refinancing | $2.5B | first abu dhabi bank, Emirates NBD Capital | UAE | AD Ports Group has signed a refinancing agreement worth AED9.175bn with First Abu Dhabi Bank and Emirates NBD Capital, replacing an… |
| 14 Jan 2026 | Cma Cgm (cma-cgm.com) | — | $2.4B | stonepeak | France | CMA CGM today raised $2.4 billion to accelerate investments in its maritime port terminals, which span 10 global properties including the… |
| 28 Aug 2025 | Glp (glp.com) | — | $2B | abu dhabi investment authority, adia | Singapore | Abu Dhabi Investment Authority, one of the world’s biggest sovereign wealth funds, is investing up to $1.5 billion in Singapore-based GLP… |
| 28 Aug 2025 | GLP Pte Ltd | — | $1.5B | abu dhabi investment authority | Singapore | A wholly owned subsidiary of the Abu Dhabi Investment Authority (ADIA) will invest up to $1.5 billion in GLP Pte Ltd to support its next… |
| 5 Jan 2026 | QXO | Convertible preferred equity | $1.2B | apollo global management, franklin templeton, two pension… | — | QXO, founded by former XPO CEO Jacobs (NYSE: XPO) who is both chairman and CEO at QXO, said Monday it had secured about $1.2 billion in… |
| 12 Apr 2026 | Intersport Slovenia Group | — | $1.1B | Intersport Austria | — | Intersport Austria acquires Intersport Slovenia group in €1bn expansion |
| 15 Jan 2026 | S.F. Holding Co., Ltd. | Strategic investment | $1.1B | J&T Global Express | — | S.F. Holding Co., Ltd. and J&T Global Express jointly announced today that they have entered into a strategic cross-shareholding agreement… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Shiprazor (shiprazor.com) | seed | $2.6M | norrsken22, aaic, e4e | South Africa | Shiprazor, the Cape Town-based e-commerce merchant technology and smart logistics platform, has raised $2.65 million (R44m) in seed… |
| 29 Apr 2026 | Aramex (aramex.co.nz) | Debt Refinancing | $220.1M | — | UAE | Aramex has completed a debt refinancing of AED 815 million |
| 28 Apr 2026 | Mojro Technologies (mojro.com) | Series A | $5.5M | IAN Alpha Fund, dallas venture capital, 1crowd | India | Mojro Technologies Pvt. Ltd., a logistics technology company focused on AI-driven supply chain optimization, has closed its Series A… |
| 27 Apr 2026 | Alma Meco | — | $43.2M | maslow capital | Spain | Dunas Capital Real Estate has closed a financing agreement of approximately 40 million euros with Maslow Capital to advance in Alma Meco,… |
| 26 Apr 2026 | Citibox (citibox.com) | — | $108M | Ithaka Infrastructure Partners, Pedro Tortosa | Spain | Citibox has closed a financing round of 100 million euros, the largest investment operation recently registered in the last mile logistics… |
| 23 Apr 2026 | UBM ParentCo, LLC | follow-on investment | $15.6M | main street capital, MSC Income Fund | — | Main Street Capital announced a $15.6 million follow-on investment in its portfolio company UBM ParentCo, LLC, supporting the company’s… |
| 23 Apr 2026 | Eaship | seed | $1.1M | Hispanic Israeli Foundation Swanlaab Venture Factory | Spain | The Hispanic Israeli Foundation Swanlaab Venture Factory has led a seed funding round of EUR 1 million in Eaship, a SaaS platform that… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector logistics --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector logistics --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector logistics --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "logistics", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "logistics", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Drone Startup Funding](drone-startup-funding.md)
- [EV Startup Funding](ev-startup-funding.md)
- [Quick Commerce Funding](quick-commerce-funding.md)
- [B2b Marketplace Funding](b2b-marketplace-funding.md)
