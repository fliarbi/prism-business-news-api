# Drone Startup Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “drone startup funding” · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [drone-startup-funding.json](../../examples/scenarios/drone-startup-funding.json).

**Question.** How many drone startup deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “drone”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 65 |
| With a usable reported amount | 59 |
| Reported total (usable amounts) | $3.7B |
| Median reported round | $11.8M |
| Largest reported round | $800M |
| Busiest month | Feb 2026 (14 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 4 | 4 | $203.6M | $40M | ██████ |
| Jun 2025 | 7 | 6 | $178.3M | $13.4M | ██████████ |
| Jul 2025 | 6 | 5 | $26.7M | $1.5M | █████████ |
| Aug 2025 | 3 | 3 | $38.8M | $8.8M | ████ |
| Sep 2025 | 4 | 3 | $154.2M | $15M | ██████ |
| Oct 2025 | 3 | 3 | $16.7M | $4.6M | ████ |
| Nov 2025 | 3 | 3 | $111M | $55.5M | ████ |
| Dec 2025 | 1 | 1 | $75M | $75M | █ |
| Jan 2026 | 4 | 4 | $1.2B | $305.9M | ██████ |
| Feb 2026 | 14 | 12 | $515M | $12.4M | ████████████████████ |
| Mar 2026 | 9 | 9 | $1.1B | $31.9M | █████████████ |
| Apr 2026 | 7 | 6 | $86.6M | $10.8M | ██████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 14 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 23 Mar 2026 | Zipline (zipline.io) | Series H | $800M | paradigm, Fidelity Management & Research Company, baillie… | United States | The additional funds, which included participation from crypto investment firm Paradigm, has pushed Zipline’s recent Series H round to… |
| 12 May 2025 | Quantum Systems (quantum-systems.com) | Series-C | $160M | balderton capital, hensoldt, airbus defence and space | Germany | The drone startup Quantum Systems (Munich) has a series-C financing round of more than 160 million. The financing round was led by… |
| 23 Sep 2025 | Auterion (auterion.com) | — | $130M | bessemer venture partners, lakestar, mosaic | — | Drone software company Auterion has collected 130 million dollars in a round of financing. |
| 6 Nov 2025 | Ageagle Aerial Systems (ageagle.com) | Series G Convertible Preferred Stock | $100M | — | — | AgEagle Aerial Systems Inc. has entered into a Securities Purchase Agreement to issue and sell up to 100,000 shares of its Series G… |
| 27 Jun 2025 | Raphe MPhibr (mphibr.com) | Series B | $100M | — | India | Back in India, Raphe mPhibr, a drone technology startup, closed a substantial $100 million Series B round to increase local production… |
| 18 Dec 2025 | Neros (neros.tech) | Series B | $75M | Vy Capital US, interlagos | USA | El Segundo-based Neros closed a $75 million Series B round led by Sequoia Capital with participation from Vy Capital US and Interlagos. |
| 9 Apr 2026 | Manna (manna.aero) | Series B | $50M | ARK Invest, ireland strategic investment fund, schooner… | Ireland | That pitch just landed him $50 million. Manna, the Irish drone delivery startup, closed a Series B this month backed by ARK Invest—Cathie… |
| 26 Feb 2026 | Draganfly (draganfly.com) | registered direct offering | $50M | — | Canada | Draganfly Inc. (NASDAQ: DPRO) announced the pricing of a registered direct offering to purchase 7,150,000 common shares at a price of US… |
| 18 Jun 2025 | Red Cat Holdings (redcatholdings.com) | registered direct offering | $46.8M | institutional investors | — | On June 17, 2025, Red Cat Holdings entered into a securities purchase agreement with institutional investors for a registered direct… |
| 9 May 2025 | Unusual Machines (unusualmachines.com) | — | $40M | Dominari Securities | — | Dominari Securities LLC, a subsidiary of Dominari Holdings Inc., successfully facilitated the introduction of Unusual Machines, Inc. into… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 24 Apr 2026 | Dronamics (dronamics.com) | Strategic Investment | — | asia air survey | Bulgaria | Bulgarian Dronamics has announced its entry into Japan, alongside a strategic investment from Asia Air Survey (TSE: 9233). |
| 14 Apr 2026 | Donecle (donecle.com) | — | $10.8M | irdi capital investissement, swen capital partners, gso… | France | Drone-based aircraft inspection specialist Donecle has received €10 million ($11.7 million) in new capital investment to drive… |
| 14 Apr 2026 | Thirdeye Systems (thirdeye-systems.com) | strategic investment | $10M | EagleNXT | Israel | today announced a key move aligned with its comprehensive growth strategy – a $10.0 million strategic investment in ThirdEye Systems Ltd.,… |
| 9 Apr 2026 | Manna (manna.aero) | Series B | $50M | ARK Invest, ireland strategic investment fund, schooner… | Ireland | That pitch just landed him $50 million. Manna, the Irish drone delivery startup, closed a Series B this month backed by ARK Invest—Cathie… |
| 8 Apr 2026 | Airhub (airhub.app) | series-A | $4.8M | keen venture partners, Runway FBU, Lumaux | — | The European software startup AirHub has completed a series-A financing of EUR 4.4 million. |
| 1 Apr 2026 | Manna Air Delivery | Series B | $11M | ARK Invest, ireland strategic investment fund, schooner… | Ireland | Manna Air Delivery, a Dublin, Ireland-based consumer drone delivery company, raised $50M in Series B funding. |
| 24 Mar 2026 | Zipline (zipline.io) | Series H | $200M | fidelity, baillie gifford, valor equity partners | United States | US-based drone logistics company Zipline has raised an additional $200 million, bringing its recent Series H funding round to $800 million. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector drone --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector drone --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector drone --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "drone", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "drone", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Mental Health Startup Funding](mental-health-startup-funding.md)
- [Travel Startup Funding](travel-startup-funding.md)
- [EV Startup Funding](ev-startup-funding.md)
- [Logistics Startup Funding](logistics-startup-funding.md)
