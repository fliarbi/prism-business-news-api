# Antler Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “antler investments” · 30/month India · 90/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [antler-investments.json](../../examples/scenarios/antler-investments.json).

**Question.** Which rounds did Antler appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Antler”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 187 |
| With a usable reported amount | 178 |
| Reported total (usable amounts) | $1.6B |
| Median reported round | $1.9M |
| Largest reported round | $300M |
| Busiest month | Jul 2025 (26 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 5 | 4 | $16.9M | $5.6M | ████ |
| Jun 2025 | 11 | 10 | $193.2M | $6.6M | ████████ |
| Jul 2025 | 26 | 26 | $427.5M | $2M | ████████████████████ |
| Aug 2025 | 23 | 19 | $20.6M | $840k | ██████████████████ |
| Sep 2025 | 15 | 15 | $180.7M | $3.5M | ████████████ |
| Oct 2025 | 20 | 19 | $47.8M | $1.6M | ███████████████ |
| Nov 2025 | 20 | 20 | $142.4M | $3M | ███████████████ |
| Dec 2025 | 6 | 5 | $18.2M | $1.1M | █████ |
| Jan 2026 | 21 | 20 | $231.5M | $160.8k | ████████████████ |
| Feb 2026 | 15 | 15 | $131.5M | $3M | ████████████ |
| Mar 2026 | 15 | 15 | $429.4M | $8M | ████████████ |
| Apr 2026 | 10 | 10 | $23.7M | $2.4M | ████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 23 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 13 Mar 2026 | Pixverse (pixverse.com) | — | $300M ⚠ check sentence | antler, EnvisionX Capital, iglobe partners | — | Alibaba-backed AI video startup PixVerse has raised $300 million in new funding, according to Bloomberg, pushing the company to a… |
| 6 Jan 2026 | Airalo (airalo.com) | Growth | $220M | cvc capital partners, peak xv, Antler Elevate | — | Airalo secured $220M to expand its global eSIM connectivity platform |
| 4 Jul 2025 | Lovable (lovable.it) | Growth round | $150M | accel, creandum, 20VC | — | Lovable Raises $150M Growth Round for AI Web Development |
| 18 Jun 2025 | Salmon (salmon.ph) | Growth (Equity + Debt Financing) | $88M | Spice Expeditions, Antler Elevate, ifc | Philippines | Salmon, a Philippines-based consumer fintech startup operating a digital lending platform and rural bank, secured $88 million in a growth… |
| 28 Feb 2026 | Inamo (inamo.com) | Series A | $60M | Five SB Limited, Shastra VC, antler | India | Quick commerce enablement startup Inamo is raising ₹50 Cr (about $5.4 Mn) in what seems to be its Series A funding round. |
| 17 Sep 2025 | Aisphere (aisphere.tech) | Series B | $60M | Fortune Capital, Shenzhen Capital Group, Beijing… | China | AIsphere, a Chinese startup, has raised more than USD 60 million in a Series B funding round led by Alibaba, with participation from… |
| 2 Mar 2026 | Harper (harperimage.com) | — | $47M | 10x founders, antler, emergence capital | USA | Harper – $47.0M |
| 23 Nov 2025 | Agentio (agentio.com) | — | $40M | alleycorp, antler, benchmark | United States | Agentio has now raised a total of $56.3M in total equity funding and is backed by AlleyCorp, Antler, Benchmark, Craft Ventures,… |
| 21 Nov 2025 | Peec AI (peec.ai) | Series-A | $21M | Singular VC, antler, Identity VC | Germany | The Berlin AI startup Peec AI has completed a 21 million US dollars (around 18 million euros) comprehensive Series-A. |
| 9 Sep 2025 | Teton.ai (teton.ai) | Series A | $20M | plural, bertelsmann investments, Antler Elevate | Denmark | Teton.ai ... secured a $20 million Series A round to expand its AI‑powered predictive care platform for nursing and senior living… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 28 Apr 2026 | Manifest (manifestcommerce.com) | pre-seed | $2M | Brand Fund by Previously Unavailable, antler, icehouse… | — | A trans‑Tasman startup has raised $2 million in pre‑seed funding to help advertising agencies better track and value their work amid the… |
| 15 Apr 2026 | SolvaPay | pre-seeded | $2.6M | redstone, ms&ad ventures, antler | — | SolvaPay announced that it raised €2.4 million in a pre-seeded round to build payment infrastructure oriented to the natural economy, an… |
| 15 Apr 2026 | Stendr | pre-seed | $5.4M | rainfall, acme, skyfall | Norway | Stendr, a Norwegian defence technology company, has raised $5.4 million in an oversubscribed pre-seed funding round to advance its… |
| 14 Apr 2026 | OrtCloud | pre-seed | $1.7M | golden gate ventures, antler | Singapore | OrtCloud, a Singapore-based cloud infrastructure company, has raised $1.7 million in a pre-seed funding round led by Southeast… |
| 13 Apr 2026 | Airmo (airmo.io) | Seed | $5.4M | ananda impact ventures, unconventional ventures, kopa… | Germany, Luxembourg | Airmo, a Munich, Germany- and Luxembourg-based climate-tech and space tech startup, raised €5M in Seed funding. |
| 13 Apr 2026 | Ralio | pre-Seed | $2.3M | Seed X, love ventures, plug and play | United Kingdom | Ralio, a London-based FinTech startup building a payments platform tailored for business AI agents, has announced a €2.1 million ($2.5… |
| 8 Apr 2026 | Onsite (onsiteworkshops.com) | seed | $1.3M | golden gate ventures, antler, other angel investors | Singapore | Singapore-based contech startup Onsite has raised US$1.3 million in seed funding to enhance its digital platform for construction site… |
| 7 Apr 2026 | Chatfood (chatfood.io) | — | $3M | antler, 6G Capital, zinal growth | UAE | UAE-based FoodTech ChatFood raised $3 million led by Antler with a reserved amount for key strategic Saudi partners where 6G Capital and… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Antler --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Antler --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Antler --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Antler", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Antler", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [8vc Portfolio](8vc-portfolio.md)
- [Kleiner Perkins Portfolio](kleiner-perkins-portfolio.md)
- [Greylock Portfolio](greylock-portfolio.md)
- [Iconiq Portfolio](iconiq-portfolio.md)
