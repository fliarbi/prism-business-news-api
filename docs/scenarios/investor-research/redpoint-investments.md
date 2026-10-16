# Redpoint Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “redpoint investments” · 10/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [redpoint-investments.json](../../examples/scenarios/redpoint-investments.json).

**Question.** Which rounds did Redpoint appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Redpoint”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 108 |
| With a usable reported amount | 104 |
| Reported total (usable amounts) | $7.1B |
| Median reported round | $67.5M |
| Largest reported round | $550M |
| Busiest month | Oct 2025 (12 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 5 | 5 | $306.2M | $70M | ████████ |
| Jun 2025 | 9 | 9 | $915M | $70M | ███████████████ |
| Jul 2025 | 8 | 7 | $160M | $22M | █████████████ |
| Aug 2025 | 10 | 10 | $299M | $36M | █████████████████ |
| Sep 2025 | 9 | 9 | $1B | $85M | ███████████████ |
| Oct 2025 | 12 | 12 | $837M | $150M | ████████████████████ |
| Nov 2025 | 12 | 11 | $536M | $61M | ████████████████████ |
| Dec 2025 | 12 | 11 | $392M | $30M | ████████████████████ |
| Jan 2026 | 8 | 8 | $1.1B | $100M | █████████████ |
| Feb 2026 | 6 | 6 | $450.5M | $120M | ██████████ |
| Mar 2026 | 9 | 8 | $1.2B | $292M | ███████████████ |
| Apr 2026 | 8 | 8 | $400M | $100M | █████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 22 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 10 Mar 2026 | Legora | Series D | $550M | accel, benchmark, bessemer venture partners | Sweden | Legora Raises $550M in Series D Funding to Expand AI in Legal Operations |
| 10 Sep 2025 | Strive Health (strivehealth.com) | Series D | $550M | nea, cvs health ventures, capitalg | USA | Strive Health has secured a massive $550 million in Series D funding. |
| 12 Jun 2025 | Cyera (cyera.io) | Series E | $540M | georgian, greenoaks, lightspeed venture partners | — | Cyera, which helps enterprises protect sensitive information while adopting artificial intelligence, has secured $540m in a Series E… |
| 20 Nov 2025 | Function Health (functionhealth.com) | Series B | $298M | redpoint ventures, Andreessen Horowitz, aglaé ventures | — | Function Health raised $298 million in Series B funding. |
| 16 Jan 2026 | K2 Space (k2space.com) | Series C | $250M | alpine space ventures, altimeter capital, hedosophia | United States | Round: Series C |
| 14 Oct 2025 | Berliner (berliner.hr) | Series-C | $180M | firstminute capital, accel, meritech | Germany | Only six months after the completion of the Series-B financing round in March 2025, n8n has raised another USD 180 million in a… |
| 10 Oct 2025 | N8n (n8n.io) | Series-C | $180M ⚠ check sentence | accel, meritech, redpoint | Germany | The Berlin-based start-up n8n has accumulated 180 million US dollars in a Series-C financing round, which increases the total financing to… |
| 22 Sep 2025 | Appzen (appzen.com) | Series D | $180M | riverwood capital, 500 global, lightspeed | United States | AppZen, an AI platform for enterprise finance teams, announced a $180 million Series D round on Monday. The growth financing was led… |
| 26 Feb 2026 | Revel (revel-health.com) | Series B | $150M | index ventures, redpoint ventures, thrive capital | USA | Revel today announced $150 million in Series B funding to accelerate its expansion across aerospace, defense, robotics, and industrial… |
| 23 Jan 2026 | Inferact | Seed | $150M ⚠ check sentence | Andreessen Horowitz, lightspeed venture partners, sequoia… | United States | Inferact, a San Francisco, CA-based AI infrastructure startup, has secured $150 million in Seed funding at an $800 million valuation. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 27 Apr 2026 | Omni (exploreomni.com) | — | $120M | first round capital, google ventures, iconiq growth | US | San Francisco-based Omni provides a data collaboration and analytics platform that allows teams to explore, model, and share business data… |
| 27 Apr 2026 | Acuitymd (acuitymd.com) | — | $80M | atreides management, benchmark, iconiq growth | US | Boston-based AcuityMD a medtech intelligence platform that leverages AI and precise data to support commercial decision-making. |
| 24 Apr 2026 | Omni Analytics, Inc. | Series C | $120M ⚠ check sentence | iconiq, Theory Ventures, first round capital | United States | Omni, a San Francisco, CA–based AI analytics platform, has raised $120 million in Series C funding at a $1.5 billion valuation. |
| 23 Apr 2026 | AARU (aarurobot.com) | Series A | $80M | redpoint ventures | — | Aaru Raises $80M Series A for Synthetic Consumer and Political Research |
| 23 Mar 2026 | Chainguard (chainguard.dev) | Funding | — | sequoia capital, redpoint ventures, spark capital | — | Chainguard announced funding support from leading investors including Sequoia Capital, Redpoint Ventures, Spark Capital, and Mantis VC. |
| 10 Mar 2026 | Legora | Series D | $550M | accel, benchmark, bessemer venture partners | Sweden | Legora Raises $550M in Series D Funding to Expand AI in Legal Operations |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Redpoint --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Redpoint --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Redpoint --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Redpoint", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Redpoint", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Breakthrough Energy Ventures Portfolio](breakthrough-energy-ventures-portfolio.md)
- [Index Ventures Portfolio](index-ventures-portfolio.md)
- [Spark Capital Investments](spark-capital-investments.md)
- [Global Founders Capital Investments](global-founders-capital-investments.md)
