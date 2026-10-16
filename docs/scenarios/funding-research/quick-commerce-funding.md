# Quick Commerce Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “quick commerce funding” · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [quick-commerce-funding.json](../../examples/scenarios/quick-commerce-funding.json).

**Question.** How many quick commerce deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “quick commerce”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 81 |
| With a usable reported amount | 72 |
| Reported total (usable amounts) | $5.1B |
| Median reported round | $12M |
| Largest reported round | $1.2B |
| Busiest month | Mar 2026 (18 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 4 | 4 | $356M | $100M | ████ |
| Jun 2025 | 1 | 0 | — | — | █ |
| Jul 2025 | 5 | 4 | $4.2M | $900k | ██████ |
| Aug 2025 | 16 | 15 | $486M | $6.1M | ██████████████████ |
| Sep 2025 | 4 | 4 | $49M | $23M | ████ |
| Oct 2025 | 7 | 6 | $456.5M | $3.3M | ████████ |
| Nov 2025 | 8 | 7 | $2.1B | $465M | █████████ |
| Dec 2025 | 5 | 4 | $2.3B | $1.1B | ██████ |
| Jan 2026 | 0 | 0 | — | — |  |
| Feb 2026 | 10 | 8 | $115.7M | $8M | ███████████ |
| Mar 2026 | 18 | 17 | $274.7M | $9M | ████████████████████ |
| Apr 2026 | 3 | 3 | $601M | $300M | ███ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 25 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 22 Dec 2025 | Swiggy (swiggy.com) | Qualified institutional placement | $1.2B | capital group, gic, blackrock | India | Swiggy, the Indian food delivery and quick-commerce company, has raised ₹10,000 crore through a qualified institutions placement, arming… |
| 28 Nov 2025 | Zepto (zepto.com.au) | Confidential filing | $480M | — | India | Zepto is preparing a confidential filing to raise around ₹4,000 crore. |
| 27 Apr 2026 | Amazon Now | — | $300M | Amazon India | India | Amazon India has announced a ₹2,800 crore (approximately $300 million) investment to dramatically scale its quick commerce vertical,… |
| 3 Mar 2026 | Flink (miflink.com) | growth funding | $100M | prosus, btomorrow ventures, existing investors | Germany | Today, the company raised $100 million in growth funding led by Prosus, along with existing investors and new backer Btomorrow Ventures,… |
| 28 Feb 2026 | Inamo (inamo.com) | Series A | $60M | Five SB Limited, Shastra VC, antler | India | Quick commerce enablement startup Inamo is raising ₹50 Cr (about $5.4 Mn) in what seems to be its Series A funding round. |
| 12 Mar 2026 | Blinkit (blinkit.com) | Rights Issue | $54M | eternal | India | Eternal, the parent entity of quick-commerce platform Blinkit, has infused ₹450 crore through a rights issue |
| 30 Mar 2026 | Munchmart Technologies Private Limited (Swish) | Series B | $38M | Hara Global Capital, bain capital ventures, accel india | — | Munchmart Technologies Private Limited, dba Swish, has raised $38 million from a Series B fundraise led by Hara Global Capital with… |
| 24 Mar 2026 | Swish (swishanalytics.com) | Series B | $38M | Hara Global, bain capital ventures, accel | — | Swish, a 10-minute food delivery startup, raised $38 million in a Series B round led by Hara Global and Bain Capital Ventures, with… |
| 4 Sep 2025 | FirstClub Technology Pvt. Ltd. | Series A | $23M | accel, rtp global, Blume Founders Fund | India | India’s only quality-first quick commerce platform FirstClub Technology Pvt. Ltd., today announced it has raised $23 million in Series A… |
| 5 Feb 2026 | ShopZilo | Series A | $15.3M | peak xv partners, info edge ventures, chiratae ventures | India | Mumbai: Fashion quick commerce startup ShopZilo has closed a $15.3 million Series A funding round, roughly Rs 140 crore, as it steps up… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 27 Apr 2026 | Amazon Now | — | $300M | Amazon India | India | Amazon India has announced a ₹2,800 crore (approximately $300 million) investment to dramatically scale its quick commerce vertical,… |
| 23 Apr 2026 | Amazon India | Investment | $300M | Amazon India | India | Amazon India will invest over INR 2,800 crore (USD 300 million) to scale its logistics and "Amazon Now" quick commerce network while… |
| 6 Apr 2026 | Try and Buy | pre-Seed | $1M | — | India | Try and Buy quick commerce startup raised $1 million in a pre-Seed round. |
| 31 Mar 2026 | Epik (epik.com) | pre-seed | $1M | InfoEdge Ventures, Raghu Pavan T S, Anirudh Prasad | India | Epik, a Try and Buy quick commerce startup focused on consumer electronics and home appliances, has announced that it has raised $1… |
| 30 Mar 2026 | Munchmart Technologies Private Limited (Swish) | Series B | $38M | Hara Global Capital, bain capital ventures, accel india | — | Munchmart Technologies Private Limited, dba Swish, has raised $38 million from a Series B fundraise led by Hara Global Capital with… |
| 24 Mar 2026 | Swish (swishanalytics.com) | Series B | $38M | Hara Global, bain capital ventures, accel | — | Swish, a 10-minute food delivery startup, raised $38 million in a Series B round led by Hara Global and Bain Capital Ventures, with… |
| 24 Mar 2026 | Ozi (ozi.ng) | Seed | $6.2M | rtp global | — | Ozi Raises $6.2 Mn Led by RTP Global. |
| 24 Mar 2026 | Zilo (zilo.co.uk) | Series A | — | — | India | Fashion-focused quick commerce startup ZILO has raised a larger Series A round of over $15 million led by institutional investors. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector "quick commerce" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector "quick commerce" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector "quick commerce" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "quick commerce", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "quick commerce", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [EV Startup Funding](ev-startup-funding.md)
- [Logistics Startup Funding](logistics-startup-funding.md)
- [B2b Marketplace Funding](b2b-marketplace-funding.md)
- [Battery Startup Funding](battery-startup-funding.md)
