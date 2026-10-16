# SAAS Funding News: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “saas funding news” · 10/month India · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [saas-funding-news.json](../../examples/scenarios/saas-funding-news.json).

**Question.** How many saas deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “saas”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 381 |
| With a usable reported amount | 326 |
| Reported total (usable amounts) | $5.7B |
| Median reported round | $5.5M |
| Largest reported round | $290M |
| Busiest month | Oct 2025 (45 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 31 | 28 | $391.1M | $4.7M | ██████████████ |
| Jun 2025 | 40 | 36 | $444.1M | $7.2M | ██████████████████ |
| Jul 2025 | 36 | 25 | $290.4M | $7.8M | ████████████████ |
| Aug 2025 | 36 | 31 | $555.5M | $5.5M | ████████████████ |
| Sep 2025 | 44 | 39 | $1B | $10M | ████████████████████ |
| Oct 2025 | 45 | 41 | $445.7M | $3M | ████████████████████ |
| Nov 2025 | 33 | 29 | $690.9M | $8.2M | ███████████████ |
| Dec 2025 | 35 | 30 | $720.2M | $4.1M | ████████████████ |
| Jan 2026 | 36 | 26 | $329.7M | $2.2M | ████████████████ |
| Feb 2026 | 23 | 19 | $302.7M | $7.6M | ██████████ |
| Mar 2026 | 12 | 12 | $181.3M | $7M | █████ |
| Apr 2026 | 10 | 10 | $336.9M | $5.7M | ████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 12 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 9 Sep 2025 | Earnix (earnix.com) | Continuation Vehicle | $290M | TPG GP Solutions, JVP | Israel | Earnix, a leading provider of dynamic AI for insurance and banking, has raised $290m in a Continuation Vehicle led by TPG GP Solutions… |
| 26 Dec 2025 | Moengage (moengage.com) | — | $280M | chryscapital, Dragon Fund, mitsubishi ufj financial group | — | MoEngage: Enterprise software-as-a-service (SaaS) startup MoEngage closed an additional $180 million as part of its ongoing funding round,… |
| 11 Dec 2025 | Harness (harnessdata.ai) | Series E | $200M | goldman sachs | United States | The firm’s Series E, announced Thursday (Dec. 11), was led by Goldman Sachs and brought in $200 million. |
| 1 Sep 2025 | Layerx (layerxsecurity.com) | Series B | $192.2M ⚠ check sentence | tcv, mufg bank, Mitsubishi UFJ Innovation Partners | Japan | LayerX, a Japanese AI SaaS startup that enables businesses to cut back-office workload, has raised $100 million in a Series B round led by… |
| 20 Jan 2026 | Pennylane (pennylane.com) | Series E | $189M | tcv, Blackstone Growth, sequoia capital | France |  |
| 2 Feb 2026 | Datarails (datarails.com) | Series C | $173.5M | ClalTech, innovation endeavors, Joey Low | — |  |
| 6 Apr 2026 | Wingify (wingify.com) | — | $165.7M | everstone capital, Vyom Mankekar, Other Investors | India | SaaS major Wingify is raising ₹1,381 Cr (nearly $149 Mn) in a strategic round led by majority shareholder and private equity (PE) firm… |
| 22 Aug 2025 | Starian | strategic investment | $128M | general atlantic | Brazil | Starian, a newly launched company that has managed all the solutions for the private sector of Softplan, has just raised R$ 640 million in… |
| 4 Nov 2025 | Quo (quocard.com) | Growth Investment | $105M | general catalyst | — | Quo Raises $105M |
| 12 May 2025 | Ascendx Cloud | growth-stage | $104.8M | Osprey Investors, columbia lake partners, Charles Delingpole | United Kingdom | Ascendx Cloud, a London-based provider of enterprise-grade CRM SaaS solutions, has announced a €97 million funding round to scale its… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Otto (ottostore.com) | Seed | $500k | Backfuture VC, Quadri Ventures, BAG Collective | India | Otto Raises $500K Seed Round |
| 29 Apr 2026 | Cata (grupocata.com.br) | seed | $5.3M | portage, white star capital, 468 capital | Singapore | The funding round was led by Portage, with participation from White Star Capital, 468 Capital, FoodLabs, FJ Labs, Rally Cap, and Iterative. |
| 24 Apr 2026 | Fanbase (fanbase.app) | Extension | $600k | — | Brazil | The startup raised a $600,000 extension round following a previous seed round. |
| 23 Apr 2026 | Eaship | seed | $1.1M | Hispanic Israeli Foundation Swanlaab Venture Factory | Spain | The Hispanic Israeli Foundation Swanlaab Venture Factory has led a seed funding round of EUR 1 million in Eaship, a SaaS platform that… |
| 8 Apr 2026 | Atlas (atlasroofing.com) | Seed | $6M | accel, stellaris venture partners | India | Atlas has raised $6 million in a seed round co‑led by Accel and Stellaris Venture Partners. |
| 8 Apr 2026 | Cloud Capital (cloudcap.in) | pre-seed and seed | $7.7M | connect ventures, Backed Ventures, middlegame ventures | — | Cloud Capital Raises $7.7 mn Cloud Capital, a SaaS-based cloud financial management platform, raised $7.7 million in combined pre-seed and… |
| 6 Apr 2026 | Wingify (wingify.com) | — | $165.7M | everstone capital, Vyom Mankekar, Other Investors | India | SaaS major Wingify is raising ₹1,381 Cr (nearly $149 Mn) in a strategic round led by majority shareholder and private equity (PE) firm… |
| 6 Apr 2026 | Wingify (wingify.com) | Growth | $150M | everstone capital | India | Wingify Receives $150 Million Growth Investment Delhi-based SaaS company Wingify, known for its conversion optimisation platform VWO,… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector saas --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector saas --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector saas --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "saas", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "saas", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Gaming Funding](gaming-funding.md)
- [Fintech Funding](fintech-funding.md)
- [Unicorn Funding](unicorn-funding.md)
- [Venture Debt Funding](venture-debt-funding.md)
