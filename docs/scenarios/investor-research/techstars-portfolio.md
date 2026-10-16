# Techstars Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “techstars portfolio” · 20/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [techstars-portfolio.json](../../examples/scenarios/techstars-portfolio.json).

**Question.** Which rounds did Techstars appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Techstars”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 60 |
| With a usable reported amount | 60 |
| Reported total (usable amounts) | $424.6M |
| Median reported round | $3.9M |
| Largest reported round | $150M |
| Busiest month | Nov 2025 (11 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 8 | 8 | $42M | $2.1M | ███████████████ |
| Jun 2025 | 2 | 2 | $1.2M | $591.3k | ████ |
| Jul 2025 | 4 | 4 | $25.9M | $5.1M | ███████ |
| Aug 2025 | 1 | 1 | $1.5M | $1.5M | ██ |
| Sep 2025 | 7 | 7 | $26.3M | $2.9M | █████████████ |
| Oct 2025 | 9 | 9 | $61.2M | $5.4M | ████████████████ |
| Nov 2025 | 11 | 11 | $41.4M | $3.2M | ████████████████████ |
| Dec 2025 | 5 | 5 | $22.7M | $6.5M | █████████ |
| Jan 2026 | 3 | 3 | $152.5M | $2M | █████ |
| Feb 2026 | 5 | 5 | $21.7M | $969k | █████████ |
| Mar 2026 | 2 | 2 | $14.6M | $7.3M | ████ |
| Apr 2026 | 3 | 3 | $22M | $6M | █████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 12 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 21 Jan 2026 | Preply (preply.com) | Series D | $150M ⚠ check sentence | horizon capital, hoxton ventures, owl ventures | USA | Language learning marketplace Preply is now valued at $1.2 billion after raising a $150 million Series D round that marks a new chapter… |
| 14 Oct 2025 | Sensei (sensei.tech) | Series A | $22.7M | metro ag, techstars ventures, bluecrow capital | Portugal | Last year, Sensei secured €15 million in a Series A funding round. Taking the total raised to €21 million, this is enabling the… |
| 17 Feb 2026 | Seasats (seasats.com) | Series A | $20M | Konvoy Ventures, shield capital, dns capital | United States | Seasats, a San Diego, CA-based company which specializes in small uncrewed surface vehicles (sUSVs), raised $20M in Series A funding. |
| 15 May 2025 | Solestial (solestial.com) | Series A | $17M | ae ventures, crosscut ventures, Zeon Ventures | United States | Solestial, Inc. (“Solestial”), the solar energy company for space, today announced a significant milestone with the closing of its $17M… |
| 8 Oct 2025 | Transcrypts (transcrypts.com) | Seed | $15M | pantera capital, Lightspeed Faction, alpha edison | USA |  |
| 30 Apr 2026 | Koda Health (kodahealthcare.com) | Series A | $14M | evidenced, Mudita Venture Partners, techstars | USA | Its series A round was led by Evidenced, with participation from Mudita Venture Partners, Techstars and the Texas Medical Center last… |
| 30 Sep 2025 | Qovery (qovery.com) | Series A | $13M | iris, speedinvest, crane venture partners | France | Qovery, a Paris-born SaaS platform that promises to cut through that bottleneck by automating application deployment, just raised $13… |
| 2 Jul 2025 | Yaspa (yaspa.com) | — | $12M | discerning capital, techstars ventures | United Kingdom | Yaspa, a hyper-growth financial technology company based in London, confirmed that it has received $12 million in its latest funding round. |
| 13 May 2025 | Flexpoint (getflexpoint.com) | Series A | $12M | foundry group, Haymaker Ventures, garuda ventures | USA | FlexPoint, a payments automation platform for managed service providers (MSPs), secured a $12 million Series A round led by Foundry Group… |
| 22 Dec 2025 | Automotus (automotus.co) | — | $9M | Santa Barbara Venture Partners, weatherford capital,… | USA | Automotus, a Los Angeles-based software company that sells curb management, traffic and associated payment technology, has raised $9… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Koda Health (kodahealthcare.com) | Series A | $14M | evidenced, Mudita Venture Partners, techstars | USA | Its series A round was led by Evidenced, with participation from Mudita Venture Partners, Techstars and the Texas Medical Center last… |
| 28 Apr 2026 | Manifest (manifestcommerce.com) | pre-seed | $2M | Brand Fund by Previously Unavailable, antler, icehouse… | — | A trans‑Tasman startup has raised $2 million in pre‑seed funding to help advertising agencies better track and value their work amid the… |
| 10 Apr 2026 | Peakmetrics (peakmetrics.com) | Series A | $6M | moneta ventures, techstars, Parameter Ventures | — | PeakMetrics, the leading AI-driven narrative intelligence company, announced the close of its $6M Series A funding round led by Moneta… |
| 30 Mar 2026 | Ateios (ateios.com) | — | $7.3M | Carat Venture Partners, E8 Angels, elevate ventures | USA | Ateios - $7.3M |
| 26 Mar 2026 | Ateios Systems (ateios.com) | Series A | $7.2M | elevate ventures, visiontech partners, good growth capital | — | One year after winning a million-dollar investment at the inaugural TitletownTech Start-up Draft, Ateios Systems has closed a $7.25M… |
| 17 Feb 2026 | Seasats (seasats.com) | Series A | $20M | Konvoy Ventures, shield capital, dns capital | United States | Seasats, a San Diego, CA-based company which specializes in small uncrewed surface vehicles (sUSVs), raised $20M in Series A funding. |
| 16 Feb 2026 | Intuos (intuos.it) | — | $777.6k | argo, Techstars Transformative World Torino, ventive | Italy | The startup, based at L’Aquila’s Aeroporto dei Parchi, has successfully raised €720k. |
| 4 Feb 2026 | Kumulus Water (kumuluswater.com) | pre-Seed | $969k | Paris Techstars Accelerator, flat6labs, wilco | Tunisia | Kumulus Water, a water service startup based in Tunisia, has raised a $969k pre-Seed funding round from Paris Techstars Accelerator,… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Techstars --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Techstars --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Techstars --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Techstars", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Techstars", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Investor names match broadly (a name can match several firms or funds); use a domain for a narrower match.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Spark Capital Investments](spark-capital-investments.md)
- [Global Founders Capital Investments](global-founders-capital-investments.md)
