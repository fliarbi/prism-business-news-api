# Travel Startup Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “travel startup funding” · 10/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [travel-startup-funding.json](../../examples/scenarios/travel-startup-funding.json).

**Question.** How many travel startup deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “travel”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 104 |
| With a usable reported amount | 84 |
| Reported total (usable amounts) | $11B |
| Median reported round | $10.2M |
| Largest reported round | $4.2B |
| Amounts left out as implausible or unconverted | 5 |
| Busiest month | Jan 2026 (17 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 10 | 7 | $1.4B | $5.9M | ████████████ |
| Jun 2025 | 10 | 8 | $158.6M | $7.3M | ████████████ |
| Jul 2025 | 3 | 3 | $225M | $112.5M | ████ |
| Aug 2025 | 14 | 12 | $5B | $10.2M | ████████████████ |
| Sep 2025 | 5 | 5 | $189.9M | $13M | ██████ |
| Oct 2025 | 9 | 8 | $1.2B | $155.5M | ███████████ |
| Nov 2025 | 2 | 1 | $1.4M | $1.4M | ██ |
| Dec 2025 | 9 | 4 | $28M | $5.5M | ███████████ |
| Jan 2026 | 17 | 15 | $399.3M | $6.5M | ████████████████████ |
| Feb 2026 | 13 | 9 | $324.5M | $6M | ███████████████ |
| Mar 2026 | 9 | 9 | $2B | $155M | ███████████ |
| Apr 2026 | 3 | 3 | $17.2M | $600k | ████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 13 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 23 Aug 2025 | Hertz Global Holdings (hertz.com) | equity capital sponsorship | $4.2B | Centerbridge Partners L.P., warburg pincus, dundon capital… | USA | The sponsorship group, made up of a trio of companies — Centerbridge Partners L.P., Warburg Pincus LLC and Dundon Capital Partners LLC —… |
| 27 May 2025 | Sabre GLBL Inc. | senior secured notes | $1.3B | — | United States | On May 20, 2025, Sabre Corporation announced that its subsidiary, Sabre GLBL Inc., has increased and priced a $1,325,000,000 offering of… |
| 24 Mar 2026 | Axiom Space (axiomspace.com) | Venture | $850M | 1789 Capital, 4ig, Kam Ghaffarian | USA |  |
| 5 Aug 2025 | Lindblad Expeditions (expeditions.com) | senior secured notes | $650M | — | United States | Lindblad Expeditions, LLC (the "Issuer"), intends to offer $650 million aggregate principal amount of senior secured notes due 2030 (the… |
| 24 Mar 2026 | Cesiumastro (cesiumastro.com) | Series C | $441.2M | airbus ventures, alumni ventures, development bank of japan | USA |  |
| 13 Oct 2025 | Navan (navan.com) | Series G | $300M ⚠ check sentence | coatue | USA | Palo Alto-based Navan, the all-in-one travel, corporate card, and expense management platform, has raised $300 million in Series G funding… |
| 16 Jan 2026 | K2 Space (k2space.com) | Series C | $250M | alpine space ventures, altimeter capital, hedosophia | United States | Round: Series C |
| 18 Jul 2025 | Airalo (airalo.com) | Growth funding | $220M | cvc capital partners, peak xv, Antler Elevate | Singapore | The $220 million funding round was led by new investor CVC through its CVC Asia Fund VI, with CVC contributing $185 million of the total… |
| 10 Oct 2025 | Le Travenues Technologies | — | $156M | prosus | India | Gurugram-based Le Travenues Technologies, the parent company of Ixigo, said it will use part of its ₹1,300 crore fundraise to expand its… |
| 10 Oct 2025 | Ixigo (ixigo.com) | INVESTMENT | $156M | prosus | — | Dutch investment group Prosus will invest INR 13 billion (around $146 million) in Indian online travel company Ixigo for a 10.1% stake. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 25 Apr 2026 | CureMeAbroad | — | $600k | — | India | CureMeAbroad raised a modest $600K in travel tech. |
| 14 Apr 2026 | The Hosteller (thehosteller.com) | Series B | $16.1M | — | — | The Hosteller - raised a funding of $16.1M in Series B round held on Apr 16, 2026. |
| 7 Apr 2026 | Cocopool (cocopool.es) | — | $469.8k | National Innovation Company (Enisa), CEO of Nextret,… | Spain | BARCELONA, 7 The Cocopool private pool rental platform has closed a funding round of 435,000 euros, with the aim of accelerating its… |
| 27 Mar 2026 | Axiom Space (axiomspace.com) | Venture | $350M | 1789 Capital, 4ig, Kam Ghaffarian | — | Houston-based Axiom Space is a space infrastructure company that develops commercial human spaceflight services and orbital platforms. |
| 27 Mar 2026 | ISpace China | Series D | $33.5M | cdh investments, Chengdu Airport Science and Technology… | — | Beijing-based iSpace designs and develops commercial space shuttle. |
| 27 Mar 2026 | Cesiumastro (cesiumastro.com) | Series C | $270M | airbus ventures, alumni ventures, development bank of japan | — | Austin-based CesiumAstro provides out-of-the-box communication systems for satellites, UAVs, launch vehicles, and other space or airborne… |
| 25 Mar 2026 | Lobby (lobby.so) | — | $2.2M | Founderful | Switzerland | Group booking specialist Lobby has raised $2.2 million in funding as it looks to expand beyond hospitality to other segments within travel. |
| 24 Mar 2026 | Axiom Space (axiomspace.com) | Venture | $850M | 1789 Capital, 4ig, Kam Ghaffarian | USA |  |
| 24 Mar 2026 | Cesiumastro (cesiumastro.com) | Series C | $441.2M | airbus ventures, alumni ventures, development bank of japan | USA |  |
| 21 Mar 2026 | Workflex (workflex.com.tr) | Strategic Growth | $40M | spectrum equity | Netherlands | WorkFlex , an Amsterdam-based platform for international travel compliance management, has secured a €37 million strategic growth… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector travel --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector travel --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector travel --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "travel", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "travel", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Medtech Funding](medtech-funding.md)
- [Mental Health Startup Funding](mental-health-startup-funding.md)
- [Drone Startup Funding](drone-startup-funding.md)
- [EV Startup Funding](ev-startup-funding.md)
