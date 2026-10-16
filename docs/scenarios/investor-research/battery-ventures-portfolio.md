# Battery Ventures Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “battery ventures portfolio” · 90/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [battery-ventures-portfolio.json](../../examples/scenarios/battery-ventures-portfolio.json).

**Question.** Which rounds did Battery Ventures appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Battery Ventures”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 84 |
| With a usable reported amount | 83 |
| Reported total (usable amounts) | $8.6B |
| Median reported round | $60M |
| Largest reported round | $2B |
| Busiest month | Feb 2026 (17 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3 | 3 | $410M | $205M | ████ |
| Jun 2025 | 3 | 2 | $75M | $37.5M | ████ |
| Jul 2025 | 4 | 4 | $445M | $55M | █████ |
| Aug 2025 | 5 | 5 | $59.8M | $24.5M | ██████ |
| Sep 2025 | 10 | 10 | $458.9M | $45M | ████████████ |
| Oct 2025 | 2 | 2 | $60M | $30M | ██ |
| Nov 2025 | 13 | 13 | $598M | $40M | ███████████████ |
| Dec 2025 | 8 | 8 | $208M | $51.5M | █████████ |
| Jan 2026 | 7 | 7 | $830M | $250M | ████████ |
| Feb 2026 | 17 | 17 | $1.4B | $90M | ████████████████████ |
| Mar 2026 | 7 | 7 | $2.4B | $255M | ████████ |
| Apr 2026 | 5 | 5 | $2.4B | $300M | ██████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 25 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 22 Apr 2026 | Cursor (cursor.com) | private funding round | $2B | Andreessen Horowitz, thrive capital, nvidia | — | Cursor was actively finalizing a $2 billion private funding round that would have valued the AI coding software company at $50 billion.… |
| 24 Mar 2026 | SambaNova | Series E | $1.5B | battery ventures, cambium capital partners, first data | USA |  |
| 16 Mar 2026 | Nexthop AI | — | $500M | altimeter capital, Andreessen Horowitz, battery ventures | USA | Nexthop AI – $500.0M |
| 4 Jul 2025 | Castelion (castelion.com) | Series B | $350M | lightspeed venture partners, altimeter capital, battery… | — | Castelion Raises $350M Series B for Hypersonics |
| 30 May 2025 | Clickhouse (clickhouse.com) | Series C | $350M | khosla ventures, bond, ivp | USA | ClickHouse, Inc., a leader in real-time analytics, data warehousing, observability, and AI/ML, today announced it has raised $350 million… |
| 9 Apr 2026 | Baseten (baseten.co) | Series E | $300M ⚠ check sentence | capitalg, ivp, nvidia | — | Baseten announced a $300 million Series E at a $5 billion valuation to expand its AI inference infrastructure platform. |
| 22 Jan 2026 | Mews (mews.com) | Series D | $300M ⚠ check sentence | eqt growth, atomico, harbourvest partners | Czech Republic | Czech-founded Mews, a hospitality technology company, has secured a $300 million (€255.17 million) in fresh investment, pushing its… |
| 23 Nov 2025 | Function Health (functionhealth.com) | — | $298M | Aglae Ventures, Allen Crabbe, alumni ventures | United States | Function Health has now raised a total of $354.0M in total equity funding and is backed by Aglae Ventures, Allen Crabbe, Alumni Ventures,… |
| 24 Mar 2026 | Fundamental (fundamental.com) | Series A | $255M | Aravind Srinivas, Assaf Rappaport, battery ventures | USA |  |
| 20 Jan 2026 | Onebrief (onebrief.com) | Series D | $200M | Battery Ventures, sapphire ventures | USA | Onebrief raised $200 million in Series D funding led by Battery Ventures and Sapphire Ventures and acquired Battle Road Digital. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 27 Apr 2026 | Orkes (orkes.io) | — | $60M | avp, battery ventures, nexus venture partners | US | Cupertino-based Orkes offers a platform for modern workflow orchestration, allowing businesses to build and scale complex software… |
| 22 Apr 2026 | Cursor (cursor.com) | private funding round | $2B | Andreessen Horowitz, thrive capital, nvidia | — | Cursor was actively finalizing a $2 billion private funding round that would have valued the AI coding software company at $50 billion.… |
| 9 Apr 2026 | Baseten (baseten.co) | Series E | $300M ⚠ check sentence | capitalg, ivp, nvidia | — | Baseten announced a $300 million Series E at a $5 billion valuation to expand its AI inference infrastructure platform. |
| 24 Mar 2026 | SambaNova | Series E | $1.5B | battery ventures, cambium capital partners, first data | USA |  |
| 24 Mar 2026 | Fundamental (fundamental.com) | Series A | $255M | Aravind Srinivas, Assaf Rappaport, battery ventures | USA |  |
| 16 Mar 2026 | Nexthop AI | — | $500M | altimeter capital, Andreessen Horowitz, battery ventures | USA | Nexthop AI – $500.0M |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "Battery Ventures" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "Battery Ventures" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "Battery Ventures" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Battery Ventures", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Battery Ventures", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Iconiq Portfolio](iconiq-portfolio.md)
- [Blume Ventures Portfolio](blume-ventures-portfolio.md)
- [Elevation Capital Portfolio](elevation-capital-portfolio.md)
- [Google Ventures Portfolio](google-ventures-portfolio.md)
