# Iconiq Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “iconiq portfolio” · 10/month India · 70/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [iconiq-portfolio.json](../../examples/scenarios/iconiq-portfolio.json).

**Question.** Which rounds did ICONIQ appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “ICONIQ”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 106 |
| With a usable reported amount | 98 |
| Reported total (usable amounts) | $71.2B |
| Median reported round | $120M |
| Largest reported round | $20B |
| Amounts left out as implausible or unconverted | 6 |
| Busiest month | Feb 2026 (20 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3 | 3 | $256.2M | $80M | ███ |
| Jun 2025 | 7 | 7 | $753.3M | $150M | ███████ |
| Jul 2025 | 7 | 7 | $5.9B | $425M | ███████ |
| Aug 2025 | 7 | 7 | $923M | $85M | ███████ |
| Sep 2025 | 13 | 13 | $13.2B | $100M | █████████████ |
| Oct 2025 | 12 | 12 | $3.5B | $352.5M | ████████████ |
| Nov 2025 | 0 | 0 | — | — |  |
| Dec 2025 | 3 | 3 | $75M | $37.5M | ███ |
| Jan 2026 | 13 | 12 | $20.5B | $100M | █████████████ |
| Feb 2026 | 20 | 14 | $44.6B | $250M | ████████████████████ |
| Mar 2026 | 11 | 10 | $2B | $350M | ███████████ |
| Apr 2026 | 10 | 10 | $648.9M | $120M | ██████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 30 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 9 Feb 2026 | Anthropic (anthropic.com) | Late-stage mega-round | $20B ⚠ check sentence | nvidia, microsoft, altimeter capital | USA | The company is reportedly raising $20 billion in new capital at a staggering $350 billion valuation. |
| 10 Feb 2026 | Databricks (databricks.com) | Series K | $5B ⚠ check sentence | qatar investment authority, Singapore Temasek, Macquarie… | United States | United States data & artificial intelligence (AI) company Databrick has raised $5 billion funding at $134 billion valuation, and with… |
| 15 Oct 2025 | ŌURA | — | $900M | Fidelity Management & Research Company, iconiq, Whale Rock | United States | has announced it has raised over $900M in funding led by Fidelity Management & Research Company with significant participation from new… |
| 14 Oct 2025 | Oura (ouraring.com) | — | $900M | Fidelity Management & Research Company, iconiq, Whale Rock | Finland | Finnish health tech company Oura has raised $900 million in fresh funding led by Fidelity Management & Research Company, with… |
| 27 Oct 2025 | Wealthsimple (wealthsimple.com) | equity | $750M ⚠ check sentence | dragoneer investment group, gic, canada pension plan… | Canada | Wealthsimple has unveiled an equity round of up to $750 million at a post-money valuation of $10 billion to accelerate the company’s… |
| 10 Mar 2026 | Legora | Series D | $550M | accel, benchmark, bessemer venture partners | Sweden | Legora Raises $550M in Series D Funding to Expand AI in Legal Operations |
| 16 Mar 2026 | Quince (quince.com) | — | $500M | iconiq capital, wellington management, dst global | United States | Online retailer Quince has raised $500 million in funding, valuing the company at $10.1 billion. |
| 4 Feb 2026 | Elevenlabs (elevenlabs.io) | Series D | $500M ⚠ check sentence | sequoia capital, Andreessen Horowitz, iconiq | USA | ElevenLabs ... raised $500 million in a Series D round led by Sequoia Capital at an $11 billion valuation. |
| 1 Aug 2025 | Ramp (ramp.network) | Series E-2 | $500M | iconiq capital, founders fund, D1 Capital | USA | Ramp, a New York-based expense management fintech startup, raised a hefty $500 million in a Series E-2 round to accelerate its AI-driven… |
| 2 Feb 2026 | Rain (rain.agency) | Series C | $332.5M | bessemer venture partners, dragonfly, endeavor catalyst | — |  |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Hightouch (hightouch.com) | Series D | $150M | iconiq capital, sapphire ventures, amplify partners | United States | Hightouch , the leader in data and AI for marketing, today announced a $150 million Series D financing led by Growth Equity at Goldman… |
| 27 Apr 2026 | Omni (exploreomni.com) | — | $120M | first round capital, google ventures, iconiq growth | US | San Francisco-based Omni provides a data collaboration and analytics platform that allows teams to explore, model, and share business data… |
| 27 Apr 2026 | Acuitymd (acuitymd.com) | — | $80M | atreides management, benchmark, iconiq growth | US | Boston-based AcuityMD a medtech intelligence platform that leverages AI and precise data to support commercial decision-making. |
| 24 Apr 2026 | Omni Analytics, Inc. | Series C | $120M ⚠ check sentence | iconiq, Theory Ventures, first round capital | United States | Omni, a San Francisco, CA–based AI analytics platform, has raised $120 million in Series C funding at a $1.5 billion valuation. |
| 1 Apr 2026 | Xona (xonasystems.com) | venture | $170M | craft ventures, samsung next, ngp capital | — | Xona raised $170 million in venture funding from Craft Ventures, Samsung NEXT, NGP Capital, ICONIQ Capital, Mohari Ventures, and Woven… |
| 1 Apr 2026 | Whirl AI | seed | $8.9M | iconiq | USA | Whirl AI announced it has emerged from stealth with $8.9 million in seed funding to help enterprise IT teams modernize business processes… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor ICONIQ --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor ICONIQ --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor ICONIQ --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "ICONIQ", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "ICONIQ", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Antler Investments](antler-investments.md)
- [Greylock Portfolio](greylock-portfolio.md)
- [Blume Ventures Portfolio](blume-ventures-portfolio.md)
- [Battery Ventures Portfolio](battery-ventures-portfolio.md)
