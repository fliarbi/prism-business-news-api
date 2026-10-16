# Media Startup Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “media startup funding” · 10/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [media-startup-funding.json](../../examples/scenarios/media-startup-funding.json).

**Question.** How many media startup deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “media”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 138 |
| With a usable reported amount | 119 |
| Reported total (usable amounts) | $50.7B |
| Median reported round | $19M |
| Largest reported round | $24B |
| Amounts left out as implausible or unconverted | 1 |
| Busiest month | Jan 2026 (18 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 12 | 10 | $92.5M | $13.5M | █████████████ |
| Jun 2025 | 14 | 14 | $2.1B | $172.5M | ████████████████ |
| Jul 2025 | 9 | 9 | $839.6M | $14M | ██████████ |
| Aug 2025 | 10 | 10 | $933M | $30.2M | ███████████ |
| Sep 2025 | 6 | 4 | $64.2M | $7.6M | ███████ |
| Oct 2025 | 12 | 9 | $886.4M | $18M | █████████████ |
| Nov 2025 | 9 | 8 | $132.6M | $5M | ██████████ |
| Dec 2025 | 13 | 12 | $532.2M | $30M | ██████████████ |
| Jan 2026 | 18 | 17 | $5.4B | $50M | ████████████████████ |
| Feb 2026 | 11 | 10 | $285.1M | $26.7M | ████████████ |
| Mar 2026 | 17 | 12 | $15.5B | $50M | ███████████████████ |
| Apr 2026 | 7 | 4 | $24B | $5.5M | ████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 16 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 6 Apr 2026 | Paramount (paramount.com) | Equity commitments | $24B | Saudi Arabia's Public Investment Fund, qatar investment… | Saudi Arabia | Paramount Skydance Corp. (NASDAQ:PSKY) is in talks to secure a massive $24 billion in equity commitments from three Gulf sovereign-wealth… |
| 14 Mar 2026 | TikTok USDS | — | $10B | — | US | Investors behind the future joint venture TikTok USDS will pay $10 billion (€8.72 billion) to the US government for its role as mediator… |
| 7 Jan 2026 | Versant Media Group | Debt Financing | $3.8B | JPMorgan, morgan stanley | United States | The financing consisted of a $1 billion term loan A facility and a $750 million revolving credit facility agented by JPMorgan, a $1… |
| 23 Mar 2026 | Nexstar Media Group (nexstardigital.com) | Senior Secured Notes | $3.4B | — | United States | Nexstar Media Group, Inc. (NASDAQ: NXST) (“Nexstar” or the “Company”) announced today that Nexstar Media Inc. (“Nexstar Media”), its… |
| 9 Jan 2026 | Bruin Capital (bruincapital.com) | — | $1B | Apollo co-founder, Josh Harris | United States | United States sports, entertainment, media & tech private equity firm Bruin Capital has raised $1 billion from investors including Apollo… |
| 20 Oct 2025 | NEP Group (nepgroup.com) | equity | $700M | 26North, carlyle | — | NEP Group, a media technology provider working across most major global sporting events, has secured a $700M equity investment led by… |
| 14 Aug 2025 | Bending Spoons (bendingspoons.com) | debt financing | $540M | J.P. Morgan, bnp paribas, Crédit Agricole CIB | Italy | Bending Spoons, the Milan-based technology company behind a roster of globally recognised digital products, has locked in over €500… |
| 10 Jun 2025 | Harbourview Equity Partners (harbourviewequity.com) | debt | $500M | kkr | — | HarbourView Equity Partners, an alternative asset management company focused on investment opportunities in the entertainment, media and… |
| 27 Jun 2025 | Inter Media and Communication S.p.A. | senior secured notes offering | $378M | U.S. institutional investors | Italy | The team supported both the Italian and U.S. law aspects of a €350 million senior secured notes offering, set to mature in 2030. |
| 10 Jun 2025 | Runway (runway.com) | Series D | $308M | general atlantic | — | Runway, a startup at the forefront of generative AI for media production, has raised $308 million in a Series D funding round led by… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 23 Apr 2026 | Identityy | Early-stage VC funding | — | Swishin Ventures | India | Identityy, a homegrown social media platform developed by Treefe Technology, has secured early-stage venture capital funding from Swishin… |
| 12 Apr 2026 | Tantv (tantvstudios.com) | pre-seed | $250k | Pharrell Williams' Black Ambition | — | "The funds will be utilized for product development (AI/ML) and team expansion," said Fashanu. |
| 7 Apr 2026 | WAYA Media | — | — | Foras.ai | — | Founders Media, the parent company of WAYA Media, has announced a strategic investment from Foras.ai, a move that accelerates the… |
| 6 Apr 2026 | Runway (runway.com) | venture fund launch | $10M | — | USA | Runway has launched a $10 million venture fund to back early-stage startups, according to a report by TechCrunch on Tuesday. |
| 6 Apr 2026 | Paramount (paramount.com) | Equity commitments | $24B | Saudi Arabia's Public Investment Fund, qatar investment… | Saudi Arabia | Paramount Skydance Corp. (NASDAQ:PSKY) is in talks to secure a massive $24 billion in equity commitments from three Gulf sovereign-wealth… |
| 4 Apr 2026 | Fanon Media & Entertainment | Pre-Seed | $1M | kalaari capital, Gruhas | — |  |
| 4 Apr 2026 | Kuku Fm (kukufm.com) | — | — | MS Dhoni | — |  |
| 30 Mar 2026 | Burt Intelligence (burt.ai) | — | — | riverside acceleration capital | United States | Riverside Acceleration Capital (RAC) is pleased to announce our recent investment in Burt Intelligence (Burt) |
| 25 Mar 2026 | DGTOOHL | Strategic investment | — | tribes | India | New Delhi: Tribes, an integrated communications agency, has announced a strategic investment in DGTOOHL, a data-driven out-of-home (OOH)… |
| 25 Mar 2026 | DGTOOHL- A Mobiyoung Product | Strategic Investment | — | tribes | India | Tribes, India’s most awarded integrated communications agency, today announced a strategic investment in DGTOOHL- a Mobiyoung Product, a… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector media --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector media --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector media --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "media", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "media", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Healthtech Funding](healthtech-funding.md)
- [Manufacturing Startup Funding](manufacturing-startup-funding.md)
- [Medtech Funding](medtech-funding.md)
- [Mental Health Startup Funding](mental-health-startup-funding.md)
