# AI Startup Funding News: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “ai startup funding news” · 10/month India · 880/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [ai-startup-funding-news.json](../../examples/scenarios/ai-startup-funding-news.json).

**Question.** How many ai startup deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “ai”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 4,641 |
| With a usable reported amount | 4,154 |
| Reported total (usable amounts) | $912.1B |
| Median reported round | $12M |
| Largest reported round | $22.5B |
| Amounts left out as implausible or unconverted | 35 |
| Busiest month | Sep 2025 (465 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 259 | 233 | $36.8B | $10.2M | ███████████ |
| Jun 2025 | 315 | 290 | $38.9B | $13M | ██████████████ |
| Jul 2025 | 345 | 311 | $82.5B | $9.6M | ███████████████ |
| Aug 2025 | 370 | 311 | $42.7B | $12M | ████████████████ |
| Sep 2025 | 465 | 424 | $132.6B | $14M | ████████████████████ |
| Oct 2025 | 465 | 427 | $53.3B | $10M | ████████████████████ |
| Nov 2025 | 420 | 384 | $120.4B | $14M | ██████████████████ |
| Dec 2025 | 334 | 290 | $78.3B | $11.9M | ██████████████ |
| Jan 2026 | 396 | 348 | $101B | $10.8M | █████████████████ |
| Feb 2026 | 449 | 399 | $146.2B | $18.4M | ███████████████████ |
| Mar 2026 | 401 | 352 | $125.6B | $30M | █████████████████ |
| Apr 2026 | 422 | 385 | $87.1B | $14M | ██████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 24 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 24 Dec 2025 | Openai (openai.com) | investment | $22.5B | softbank | — | SoftBank rushed to meet its $22.5 billion pledge to OpenAI, selling stakes and pausing other deals to prioritize the investment. |
| 18 Feb 2026 | Xai (x.ai) | Series E | $20B | humain, fidelity, cisco | USA | Elon Musk’s artificial intelligence startup xAI announced it received a $3 billion investment from Humain |
| 28 Jan 2026 | Anthropic (anthropic.com) | — | $20B | gic, coatue, sequoia capital | United States | Anthropic, one of the fastest‑growing AI start‑ups, is preparing to raise around $20 billion from venture capital firms and other major… |
| 9 Dec 2025 | Microsoft (microsoft.com) | investment | $19.2B | microsoft | India | MICROSOFT WILL INVEST ₹1.6 LAKH CRORE IN INDIA: AI AND CLOUD INFRASTRUCTURE WILL COST; CEO SATYA NADELA HAS BEEN GOING TO INVEST $17.5… |
| 2 Apr 2026 | Related Digital (relateddigital.com) | Financing | $16B | blackstone, bank of america | United States | Related Digital – Related Cos.’ new data center arm – has lined up a $16B financing deal for a massive data center in Saline Township,… |
| 27 Mar 2026 | Waymo (waymo.com) | Series D | $16B | alphabet, Andreessen Horowitz, bdt & msd partners | — | Mountain View-based Waymo is a mobility technology company that improves transportation by developing self‑driving solutions for travelers… |
| 17 Sep 2025 | Nscale (nscale.com) | Investment | $15.5B | microsoft | United Kingdom | Microsoft headlined the U.K. announcements, committing $15.5 billion of new investment to computing equipment. The software giant said it… |
| 1 Jul 2025 | ScaleAI | — | $15B | meta | — | Meta has made major investments in AI firms such as ScaleAI, reportedly investing $15 billion |
| 9 May 2025 | TWG Global | Equity raise | $15B | Mubadala Capital | Hong Kong | Under this strategic investment alliance and as part of TWG’s $15 billion equity raise, Mubadala Capital will anchor and lead a $10… |
| 3 Jul 2025 | Scale (scale.com) | — | $14.8B | meta | — | Meta invested a massive $14.8B in Scale , whose CEO is also joining the tech giant. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Featherless.ai | Series A | $20M | AMD Ventures, airbus ventures, bmw i ventures | — | Featherless.ai, a Singapore co-founded artificial intelligence (AI) firm, has secured $20 million in Series A funding co-led by AMD… |
| 30 Apr 2026 | Parallel Web Systems | Series B | $10M ⚠ check sentence | sequoia capital, kleiner perkins, index ventures | — | Former Twitter (now X) CEO Parag Agrawal’s AI agentic platform Parallel Web Systems has raised a $100 million Series B at a $2 billion… |
| 30 Apr 2026 | Netomi (netomi.com) | — | — | accenture ventures | United States | Accenture has made an investment, through Accenture Ventures, in Netomi, a leading customer experience AI platform company. |
| 30 Apr 2026 | Netomi (netomi.com) | — | $110M | accenture ventures, adobe ventures, wndrco | USA | Netomi, the San Francisco-based startup building AI systems for enterprise customer service, said Thursday that it has raised $110 million… |
| 30 Apr 2026 | Dreamteam (dreamteam.gg) | Series A | $40M | accel, Together Fund | India | Chennai-based AI startup Dreamteam is in advanced discussions to raise around $40 million in its Series A funding round, with Accel and… |
| 30 Apr 2026 | Synaps (synaps.io) | pre-seed | $3.6M | plug and play, Fil Rouge Capital | Austria | Five months later, Synaps is announcing a $3.6 million pre‑seed funding round from US‑based accelerator and VC Plug and Play, and… |
| 30 Apr 2026 | Tryll (tryll.co) | pre-seed | $600k | Early Game Ventures | Romania | Venture capital fund Early Game Ventures announced a USD 600,000 pre-seed investment in Tryll, a startup that integrates AI into video… |
| 29 Apr 2026 | Parallel Web Systems | Series B | $100M | sequoia capital | — | Parallel Web Systems Raises $100M Series B for AI Agents’ Web Infrastructure |
| 29 Apr 2026 | Aidoc (aidoc.com) | Series E | $150M ⚠ check sentence | Growth Equity at Goldman Sachs Alternatives, general… | Israel | Aidoc has raised $150M in Series E funding, led by Growth Equity at Goldman Sachs Alternatives, bringing its total funding to over $500M.… |
| 29 Apr 2026 | Apera AI (apera.ai) | — | — | Zebra Ventures | Canada | Our investment in Apera AI is a strategic step toward a more intelligent, responsive automation future |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector ai --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector ai --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector ai --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "ai", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "ai", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Series A Funding](series-a-funding.md)
- [Series B Funding](series-b-funding.md)
- [Series C Funding](series-c-funding.md)
- [Biotech Funding News](biotech-funding-news.md)
