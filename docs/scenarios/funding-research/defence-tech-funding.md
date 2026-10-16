# Defence Tech Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “defence tech funding” · volume below estimate threshold  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [defence-tech-funding.json](../../examples/scenarios/defence-tech-funding.json).

**Question.** How many defence tech deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “defense”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 266 |
| With a usable reported amount | 234 |
| Reported total (usable amounts) | $40.2B |
| Median reported round | $28.7M |
| Largest reported round | $8B |
| Busiest month | Feb 2026 (38 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 11 | 10 | $1.6B | $105M | ██████ |
| Jun 2025 | 20 | 19 | $4.9B | $44.4M | ███████████ |
| Jul 2025 | 18 | 14 | $2.4B | $50M | █████████ |
| Aug 2025 | 23 | 23 | $1.4B | $14.5M | ████████████ |
| Sep 2025 | 16 | 14 | $1.4B | $51.3M | ████████ |
| Oct 2025 | 12 | 10 | $466.3M | $9.8M | ██████ |
| Nov 2025 | 18 | 18 | $1.5B | $43.2M | █████████ |
| Dec 2025 | 35 | 25 | $1.4B | $22M | ██████████████████ |
| Jan 2026 | 18 | 18 | $1.5B | $30M | █████████ |
| Feb 2026 | 38 | 33 | $9.7B | $25M | ████████████████████ |
| Mar 2026 | 35 | 28 | $11.7B | $68M | ██████████████████ |
| Apr 2026 | 22 | 22 | $3.4B | $13.4M | ████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 22 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 17 Feb 2026 | Anduril Industries (anduril.com) | — | $8B ⚠ check sentence | — | United States | United States defence weapon company Anduril Industries to Raise $8 Billion Funding at $60 Billion Valuation, Founded in 2017 by Palmer… |
| 26 Mar 2026 | Shield AI (shield.ai) | Series G | $2B | advent international, JPMorgan Chase's Strategic… | United States | The startup said on Thursday the Series G round was led by Advent International and co‑led by JPMorgan Chase's Strategic Investment Group,… |
| 3 Apr 2026 | Saronic (saronic.com) | Series D | $1.8B | kleiner perkins | United States | Leading the pack was Saronic's monumental $1.75 billion Series D funding round, the largest ever for an Austin-based startup and a boon… |
| 23 Apr 2026 | L3Harris Technologies (l3harris.com) | Convertible Preferred | $1B | pentagon | United States | The Pentagon has completed a $1 billion investment in L3Harris Technologies’ missile business, formalizing a deal aimed at expanding U.S.… |
| 2 Jul 2025 | Aerovironment (avinc.com) | Public Offering | $875M | J.P. Morgan, BofA Securities, raymond james | United States | ARLINGTON, Va. / Jul 01, 2025 / Business Wire / AeroVironment, Inc. (NASDAQ: AVAV) (the “Company”) today announced the pricing of its… |
| 1 Dec 2025 | Ducommun Incorporated (ducommun.com) | Credit Facility | $650M | — | USA | Ducommun Incorporated (NYSE: DCO) (“Ducommu” or the “Company”) today announced that effective November 24, 2025, it entered into an… |
| 18 Jun 2025 | Helsing (helsing.ai) | — | $648M | prima materia | Germany | Helsing, a Munich-based startup, has raised €600 million in funding, bringing its total to over €1.3 billion. |
| 23 May 2025 | Elbit Systems (elbitsystems.com) | equity issuance | $588.8M | BofA Securities, Inc. | Israel | On May 21, 2025, Elbit Systems Ltd. entered into an underwriting agreement with BofA Securities, Inc. for the issuance and sale of… |
| 6 Mar 2026 | Sierra Space (sierraspace.com) | Equity investment | $550M ⚠ check sentence | LuminArx Capital Management, general atlantic, coatue | United States | Sierra Space has closed a $550 million equity investment led by LuminArx Capital Management, bringing the defense technology company’s… |
| 14 Nov 2025 | Chaos Industries (getchaos.com) | — | $510M | valor equity partners, 8vc, accel | USA | CHAOS Industries has raised $510 million in new funding to expand development and manufacturing of its sensing and timing technologies for… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Scout AI (withscout.com) | seed | $15M | align ventures, draper associates | — | Scout AI, which is squarely focused on developing a frontier artificial intelligence model for unmanned warfare, on Wednesday said it has… |
| 29 Apr 2026 | Scout AI (withscout.com) | Series A | $10M | align ventures, draper associates | U.S. | Scout AI, which is squarely focused on developing a frontier artificial intelligence model for unmanned warfare, on Wednesday said it has… |
| 29 Apr 2026 | Firestorm Labs | Series B | $82M ⚠ check sentence | washington harbour partners, nea, Ondas | USA | The company announced on Wednesday that it has raised $82 million in Series B funding led by Washington Harbour Partners with… |
| 29 Apr 2026 | Laser Photonics (laserphotonics.com) | — | $4M | — | USA | The gross proceeds to the Company from the exercise of the warrants were approximately $4 million, prior to deducting placement agent fees… |
| 28 Apr 2026 | T3 Defense (DFNS) | debt-for-equity | $2.1M | Shalom Menachem, Esousa Group Holdings LLC | — | These shares were issued in exchange for cancelling $2,138,962 of aggregate outstanding principal and accrued interest on promissory notes… |
| 23 Apr 2026 | Adisyn | institutional placement | $9.2M | regal funds management, meitav, Sandton Capital Advisory | Australia | Adisyn has reportedly secured firm commitments to raise AU$14 million (over US$10 million) through an institutional placement, backed by… |
| 23 Apr 2026 | L3Harris Technologies (l3harris.com) | Convertible Preferred | $1B | pentagon | United States | The Pentagon has completed a $1 billion investment in L3Harris Technologies’ missile business, formalizing a deal aimed at expanding U.S.… |
| 23 Apr 2026 | Rilian | seed and seed extension | $17.5M | 8vc, first in, tamarack global | USA | Rilian Inks $17.5M Seed and Seed Extension Back to Home MCLEAN, VA, Rilian, a provider of AI-native cybersecurity and defense systems… |
| 21 Apr 2026 | Foresight Autonomous Holdings (foresightauto.com) | Strategic investment | $17.5M | Visionwave | USA | VisionWave today announced a non-binding term sheet for a strategic investment in Foresight Autonomous Holdings, under which it would… |
| 19 Apr 2026 | Graham Corporation (graham-mfg.com) | — | $50M | T. Rowe Price Investment Management | — | Graham Corporation announced it has secured a $50 million investment from accounts advised by T. Rowe Price Investment Management,… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector defense --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector defense --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector defense --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "defense", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "defense", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Battery Startup Funding](battery-startup-funding.md)
- [Construction Tech Funding](construction-tech-funding.md)
- [E-commerce Funding](e-commerce-funding.md)
- [Foodtech Funding](foodtech-funding.md)
