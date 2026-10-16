# Kleiner Perkins Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “kleiner perkins portfolio” · 20/month India · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [kleiner-perkins-portfolio.json](../../examples/scenarios/kleiner-perkins-portfolio.json).

**Question.** Which rounds did Kleiner Perkins appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Kleiner Perkins”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 128 |
| With a usable reported amount | 123 |
| Reported total (usable amounts) | $27.3B |
| Median reported round | $100M |
| Largest reported round | $16B |
| Amounts left out as implausible or unconverted | 1 |
| Busiest month | Mar 2026 (20 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 7 | 6 | $273M | $23M | ███████ |
| Jun 2025 | 10 | 10 | $1.5B | $150M | ██████████ |
| Jul 2025 | 11 | 11 | $1.5B | $180M | ███████████ |
| Aug 2025 | 9 | 8 | $807.6M | $150M | █████████ |
| Sep 2025 | 2 | 1 | $8M | $8M | ██ |
| Oct 2025 | 8 | 8 | $576.7M | $100M | ████████ |
| Nov 2025 | 18 | 18 | $527M | $80M | ██████████████████ |
| Dec 2025 | 15 | 15 | $832M | $120M | ███████████████ |
| Jan 2026 | 9 | 9 | $520M | $70M | █████████ |
| Feb 2026 | 8 | 8 | $504M | $65.5M | ████████ |
| Mar 2026 | 20 | 19 | $19.3B | $182.4M | ████████████████████ |
| Apr 2026 | 11 | 10 | $2.4B | $61M | ███████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 25 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 27 Mar 2026 | Waymo (waymo.com) | Series D | $16B | alphabet, Andreessen Horowitz, bdt & msd partners | — | Mountain View-based Waymo is a mobility technology company that improves transportation by developing self‑driving solutions for travelers… |
| 3 Apr 2026 | Saronic (saronic.com) | Series D | $1.8B | kleiner perkins | United States | Leading the pack was Saronic's monumental $1.75 billion Series D funding round, the largest ever for an Austin-based startup and a boon… |
| 18 Jun 2025 | Applied Intuition (appliedintuition.com) | Series F | $600M ⚠ check sentence | BlackRock-managed funds and accounts, kleiner perkins,… | United States | Applied Intuition, Inc., the leading vehicle intelligence company for automotive, trucking, construction, mining, agriculture, and… |
| 16 Mar 2026 | Nexthop AI | — | $500M | altimeter capital, Andreessen Horowitz, battery ventures | USA | Nexthop AI – $500.0M |
| 4 Jul 2025 | Rippling (rippling.com) | Collection G spherical | $450M ⚠ check sentence | sands capital, gic, Goldman Sachs Development | US | Rippling, a San Francisco-based HR tech startup, has raised $450 million in a Collection G funding spherical, valuing the corporate at… |
| 25 Jun 2025 | Harvey (harvey.ai) | Series E | $300M ⚠ check sentence | kleiner perkins, coatue, sequoia | USA | Harvey, the legal AI platform used by law firms and corporate legal teams worldwide, has raised $300 million in a Series E funding round,… |
| 21 Oct 2025 | Fal.ai | Series D | $250M | kleiner perkins, sequoia capital, Meritech Capital | USA | Redwood City‑based firm secured roughly $250 million in new funding led by Kleiner Perkins and Sequoia Capital. |
| 5 Aug 2025 | Ambience Healthcare (ambiencehealthcare.com) | Series C | $243M | oak hc/ft, Andreessen Horowitz (a16z), openai startup fund | USA | Ambience Healthcare, a San Francisco, CA-based ambient AI platform for documentation, coding, and clinical documentation integrity (CDI),… |
| 4 Aug 2025 | Openevidence (openevidence.com) | Series B | $210M ⚠ check sentence | google ventures, kleiner perkins, sequoia capital | United States | OpenEvidence, the most widely used medical search and AI application among verified U.S. clinicians, today announced a $210 million Series… |
| 26 Jan 2026 | Synthesia (synthesia.io) | Series E | $200M ⚠ check sentence | google ventures, kleiner perkins, accel | United Kingdom | has raised a $200 million Series E round of funding that brings its valuation to $4 billion — up from $2.1 billion just a year ago. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Parallel Web Systems | Series B | $10M ⚠ check sentence | sequoia capital, kleiner perkins, index ventures | — | Former Twitter (now X) CEO Parag Agrawal’s AI agentic platform Parallel Web Systems has raised a $100 million Series B at a $2 billion… |
| 29 Apr 2026 | Rogo (rogodata.com) | Series D | $160M | kleiner perkins, sequoia capital, thrive | USA | Rogo Raises $160M in Series D Funding for Finance AI Platform |
| 29 Apr 2026 | Parallel Web Systems | Series B | $100M ⚠ check sentence | sequoia capital, kleiner perkins, index ventures | United States | Parallel Web Systems, a startup founded by former Twitter CEO Parag Agrawal, has raised $100 million in a Series B funding round led by… |
| 28 Apr 2026 | Manifest OS | Series A | $60M ⚠ check sentence | menlo ventures, kleiner perkins, first round capital | United States | Manifest OS has secured a $60 million Series A round (at a $750 million valuation) to further develop its AI-driven software for the legal… |
| 27 Apr 2026 | Avoca (avoca.com) | Series A | — | kleiner perkins | — | the Series A was led by Kleiner Perkins. |
| 17 Apr 2026 | Sage Haven | Pre-Seed | $3M | hustle fund, how women invest, LaunchTN | — | Sage Haven announces the official launch of its safer messaging and voice calling app for kids, following a successful beta period,… |
| 17 Apr 2026 | Balerion AI | Seed | $6M | kleiner perkins, formation, boxgroup | US | Balerion AI Use of Funds The company will use the funds to enhance its AI capabilities, expand its enterprise customer base, and grow its… |
| 16 Apr 2026 | Gambit Security | Seed and Series A | $61M | spark capital, kleiner perkins, cyberstarts | — | Gambit Security, an AI-native enterprise resilience platform, has emerged from stealth with $61m in seed and Series A funding raised in… |
| 7 Apr 2026 | Harvey (harvey.ai) | Series | $200M ⚠ check sentence | gic, sequoia, Andreessen Horowitz | — | Harvey, a legal infrastructure company, raised USD 200 million in a funding round co-led by returning investors GIC and Sequoia, at a… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "Kleiner Perkins" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "Kleiner Perkins" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "Kleiner Perkins" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Kleiner Perkins", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Kleiner Perkins", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Investor names match broadly (a name can match several firms or funds); use a domain for a narrower match.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Temasek Portfolio](temasek-portfolio.md)
- [8vc Portfolio](8vc-portfolio.md)
- [Antler Investments](antler-investments.md)
- [Greylock Portfolio](greylock-portfolio.md)
