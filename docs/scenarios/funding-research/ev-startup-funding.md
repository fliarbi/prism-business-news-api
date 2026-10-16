# EV Startup Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “ev startup funding” · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [ev-startup-funding.json](../../examples/scenarios/ev-startup-funding.json).

**Question.** How many ev startup deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “electric vehicle”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 109 |
| With a usable reported amount | 104 |
| Reported total (usable amounts) | $16B |
| Median reported round | $30M |
| Largest reported round | $1.5B |
| Busiest month | Dec 2025 (13 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 7 | 5 | $198.5M | $18M | ███████████ |
| Jun 2025 | 9 | 8 | $640.7M | $12.5M | ██████████████ |
| Jul 2025 | 11 | 11 | $1.9B | $121.5M | █████████████████ |
| Aug 2025 | 8 | 7 | $2.5B | $262.5M | ████████████ |
| Sep 2025 | 12 | 11 | $3.6B | $125M | ██████████████████ |
| Oct 2025 | 8 | 8 | $496.5M | $35M | ████████████ |
| Nov 2025 | 7 | 7 | $2.9B | $428.5M | ███████████ |
| Dec 2025 | 13 | 13 | $182.8M | $9.4M | ████████████████████ |
| Jan 2026 | 5 | 5 | $153.2M | $3M | ████████ |
| Feb 2026 | 13 | 13 | $1.2B | $30M | ████████████████████ |
| Mar 2026 | 7 | 7 | $1.3B | $17.3M | ███████████ |
| Apr 2026 | 9 | 9 | $1.4B | $44.8M | ██████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 12 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 15 Aug 2025 | VinFast Auto (vinfastauto.com) | Sale of assets and shares | $1.5B | Pham Nhat Vuong | Vietnam | VinFast Auto Ltd is poised to raise about US$1.5 billion by selling certain research and development assets to its founder. |
| 17 Sep 2025 | NIO Inc. | Equity Offering | $1.2B | morgan stanley asia, UBS Securities LLC, UBS AG Hong Kong… | United States | NIO Inc. (NYSE: NIO; HKEX: 9866; SGX: NIO) (“NIO” or the “Company”), a pioneer and a leading company in the global smart electric vehicle… |
| 6 Feb 2026 | Ardea Resources (ardearesources.com.au) | Non-binding Funding Support | $1B | export finance australia, Export-Import Bank of the United… | Australia | Ardea Resources has secured up to $1 billion in non-binding funding support from US and Australian government agencies for its Goongarrie… |
| 25 Nov 2025 | Erisha E Mobility (erishaev.com) | investment | $1B | UAE-based investor | — | The $1-billion investment in Erisha E Mobility, the electric vehicle arm of Rana Group, by a UAE-based investor, was the biggest driver of… |
| 12 Sep 2025 | Nio (nio.com) | discounted new share placement | $1B | — | China | China $12 Billion Electric Vehicle Company Nio Raised $1 Billion via Discounted New Share Placement (HKD 43.36 / $5.57), Current market… |
| 18 Nov 2025 | Lucid Group (wearelucidgroup.com) | Convertible Senior Notes | $975M | — | USA | Simpson Thacher represented the initial purchasers in connection with the offering by Lucid Group, Inc. ("Lucid") of $975 million… |
| 16 Mar 2026 | Ola Electric Mobility (olaelectric.com) | Initial Public Offering | $660M | — | India | In August 2024, Ola Electric Mobility raised Rs 5,500 crore through its initial public offering (IPO). |
| 13 Apr 2026 | Slate Auto | Series C | $650M | TWG Global | United States | Slate Auto has closed its $650 million Series C round led by TWG Global. |
| 14 Nov 2025 | Octopus Electric Vehicles (octopusev.com) | Credit facility | $635M | morgan stanley, lloyds banking group, crédit agricole | UK | UK-based Octopus Electric Vehicles (Octopus EV) has obtained a £500m ($657.8m) funding from a group of lenders, increasing its total… |
| 25 Jul 2025 | Electra (electrainfo.com) | green loan | $467.6M ⚠ check sentence | — | France | 🇫🇷 EV charge point operator Electra secures €433M green loan, surpasses €1B in total funding |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Battery Smart (batterysmart.in) | Series B (extended) | $29M | tiger global, blume ventures, ecosystem integrity fund | — | With its $65 million Series B round and $29 million extended Series B round, Battery Smart has raised about $192 million in funding thus… |
| 23 Apr 2026 | Mufin Green Finance (mufingreenfinance.com) | preferential allotment | $388.8M | hindon mercantile, Sageone Capital, Sandeep Kapadia | India | Mufin Green Finance has completed a preferential allotment, raising about ₹324 crore through the issuance of equity shares and warrants. |
| 23 Apr 2026 | Mufin Green Finance (mufingreenfinance.com) | equity stake acquisition | $44.8M | tata mutual fund | India | Tata Mutual Fund acquired a stake worth around ₹37.37 crore in Mufin Green Finance |
| 23 Apr 2026 | Trevel (trevelapp.com) | — | $1M | — | India | TREVEL, a premium all-electric cab-hailing startup focused on safety and reliability, has initiated a $1 million fundraising round, with… |
| 15 Apr 2026 | Glydways (glydways.com) | — | $170M | suzuki motor corporation, acs group, khosla ventures | — | Glydways, a creator of autonomous electric pods that can move 10,000 people per hour through lanes that are even narrower than a parking… |
| 13 Apr 2026 | Slate Auto | Series C | $650M | TWG Global | United States | Slate Auto has closed its $650 million Series C round led by TWG Global. |
| 11 Apr 2026 | Astranova Mobility | Series A | $72M | ivycap ventures, asian development bank, advantedge founders | India | Astranova Mobility, a Gurgaon electric vehicle (EV) startup, has successfully raised Rs. 60 crore. The money was raised in a Series A… |
| 10 Apr 2026 | Astronova Mobility | — | $7.2M | IvyCap Ventures Advisors | India | Astronova Mobility: Gurugram-based electric vehicle (EV) financing platform Astranova Mobility has raised Rs 60 crore in a fresh funding… |
| 8 Apr 2026 | Wallbox (wallbox.com) | interim financing | $11.9M | banco santander, banco bilbao vizcaya argentaria, caixabank | Spain | In connection with the signing of the restructuring plan, the Group has also secured €11 million in interim financing, comprising (i) a… |
| 30 Mar 2026 | Charge+ (chargeplus.com) | Series A | $8M | — | Singapore | In 2024, Charge+ raised US$8 million in a Series A round. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector "electric vehicle" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector "electric vehicle" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector "electric vehicle" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "electric vehicle", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "electric vehicle", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Travel Startup Funding](travel-startup-funding.md)
- [Drone Startup Funding](drone-startup-funding.md)
- [Logistics Startup Funding](logistics-startup-funding.md)
- [Quick Commerce Funding](quick-commerce-funding.md)
