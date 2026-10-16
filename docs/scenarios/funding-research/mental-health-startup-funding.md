# Mental Health Startup Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “mental health startup funding” · 10/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [mental-health-startup-funding.json](../../examples/scenarios/mental-health-startup-funding.json).

**Question.** How many mental health startup deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “mental health”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 54 |
| With a usable reported amount | 49 |
| Reported total (usable amounts) | $1.6B |
| Median reported round | $12.6M |
| Largest reported round | $452M |
| Busiest month | Nov 2025 (11 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 4 | 4 | $9.9M | $2.1M | ███████ |
| Jun 2025 | 0 | 0 | — | — |  |
| Jul 2025 | 7 | 6 | $243.1M | $35M | █████████████ |
| Aug 2025 | 1 | 1 | $50k | $50k | ██ |
| Sep 2025 | 4 | 2 | $38M | $19M | ███████ |
| Oct 2025 | 5 | 5 | $73.5M | $15.5M | █████████ |
| Nov 2025 | 11 | 11 | $116.4M | $7.3M | ████████████████████ |
| Dec 2025 | 3 | 3 | $50.2M | $25.1M | █████ |
| Jan 2026 | 2 | 2 | $5.2M | $2.6M | ████ |
| Feb 2026 | 5 | 5 | $355.4M | $23.7M | █████████ |
| Mar 2026 | 11 | 9 | $871.5M | $18.5M | ████████████████████ |
| Apr 2026 | 1 | 1 | $40M | $40M | ██ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 11 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 24 Mar 2026 | Talkiatry (talkiatry.com) | Series D | $452M | Andreessen Horowitz, blisce, left lane capital | USA |  |
| 9 Mar 2026 | Grow Therapy (growtherapy.com) | Series D | $150M | signalfire, menlo ventures, goldman sachs asset management | US | Grow Therapy Raises $150M in Series D Funding to Expand Mental Health Platform |
| 12 Feb 2026 | Spring Health (springhealth.com) | — | $100M ⚠ check sentence | — | — | In 2024, Spring Health raised $100 million with a $3.3 billion valuation. |
| 25 Jul 2025 | Slingshot AI (slingshot.xyz) | Series A | $93M ⚠ check sentence | radical ventures, forerunner ventures, Andreessen Horowitz… | — | Slingshot’s flagship product, an AI-powered chatbot named Ash, has officially launched alongside a follow-on Series A funding round.… |
| 31 Jul 2025 | Unmind (unmind.com) | — | $82M ⚠ check sentence | project a, felix capital, sapphire ventures | — | Unmind has raised a total of $82 million to date, with continued support from existing investors Project A, Felix Capital, and Sapphire… |
| 19 Nov 2025 | Diana Health (heydianahealth.com) | — | $55.4M | — | — | In September, Diana Health raised $55.4 million for its integrated women’s health care platform, which includes mental health. |
| 15 Dec 2025 | Radial (radial.com) | Venture | $50M | general catalyst | — | Radial, an interventional advanced mental health care platform, has raised $50M in Venture funding led by General Catalyst. |
| 21 Apr 2026 | Tava Health (tavahealth.com) | Series C | $40M | centana growth partners, catalyst investors, Blue Heron… | United States | Tava Health, a leader in technology-driven mental health services, today announced a $40 million Series C funding round. |
| 3 Oct 2025 | Cartwheel Care | Series unspecified | $35M | — | — | Among pure-play mental health care providers, the largest funding round in recent months went to pediatric-focused companyCartwheel Care… |
| 4 Sep 2025 | Na | senior secured credit facility | $30M | aequum capital | USA | Aequum Capital is pleased to announce the closing of a $30 million senior secured credit facility—consisting of a $25 million term loan… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 21 Apr 2026 | Tava Health (tavahealth.com) | Series C | $40M | centana growth partners, catalyst investors, Blue Heron… | United States | Tava Health, a leader in technology-driven mental health services, today announced a $40 million Series C funding round. |
| 31 Mar 2026 | Jaaq | Series A | $16.2M | Meridian Health Ventures, Bolt Angels, fuel ventures | United Kingdom | British HealthTech JAAQ closes €15 million Series A to grow enterprise partnerships EU-Startups • Mar 23, 2026 • Meridian Health Ventures… |
| 31 Mar 2026 | Jimini Health | seed | $17M | m13, town hall ventures, lionbird | USA | Startup Jimini Health has raised $17 million in seed funding as it seeks to launch its mental health AI platform Sage with large… |
| 30 Mar 2026 | Blossom Health | — | $20M | — | — | Blossom Health raised $20 million across Seed and Series A rounds to expand its AI-powered operating system for psychiatry. |
| 30 Mar 2026 | Amaha (formerly Innerhour) (amahahealth.com) | Series A (extended) | $6M | fireside ventures, Shreyas Shibulal, lightbox | India | Mental health startup Amaha (formerly InnerHour) has raised Rs 50 crore in an extended Series A round led by Fireside Ventures. |
| 24 Mar 2026 | Talkiatry (talkiatry.com) | Series D | $452M | Andreessen Horowitz, blisce, left lane capital | USA |  |
| 12 Mar 2026 | Bliss (blissworld.com) | angel | $270k | keiretsu forum, Finest Love VC, plug and play | Finland | The round, led by Keiretsu Forum, Finest Love VC and Plug and Play, will support the development of AI infrastructure for culturally aware… |
| 10 Mar 2026 | Talkiatry (talkiatry.com) | Late-Stage | $210M | — | USA | Top 10 NYC Venture Capital Deals — February 2026 # Company Amount Round Sector 3 Talkiatry $210M Late-Stage Mental Health / Healthcare |
| 9 Mar 2026 | Grow Therapy (growtherapy.com) | Series D | $150M | signalfire, menlo ventures, goldman sachs asset management | US | Grow Therapy Raises $150M in Series D Funding to Expand Mental Health Platform |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector "mental health" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector "mental health" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector "mental health" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "mental health", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "mental health", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Media Startup Funding](media-startup-funding.md)
- [Medtech Funding](medtech-funding.md)
- [Travel Startup Funding](travel-startup-funding.md)
- [Drone Startup Funding](drone-startup-funding.md)
