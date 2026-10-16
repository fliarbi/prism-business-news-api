# Series A Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “series a funding” · 880/month India · 3,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [series-a-funding.json](../../examples/scenarios/series-a-funding.json).

**Question.** How many series a deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** round type “series a”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 3,824 |
| With a usable reported amount | 3,547 |
| Reported total (usable amounts) | $104.6B |
| Median reported round | $15M |
| Largest reported round | $20B |
| Amounts left out as implausible or unconverted | 5 |
| Busiest month | Feb 2026 (444 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 247 | 235 | $4.3B | $13M | ███████████ |
| Jun 2025 | 272 | 249 | $5.6B | $15.4M | ████████████ |
| Jul 2025 | 287 | 259 | $7.4B | $13M | █████████████ |
| Aug 2025 | 276 | 255 | $4.3B | $12M | ████████████ |
| Sep 2025 | 352 | 326 | $5.7B | $14M | ████████████████ |
| Oct 2025 | 347 | 325 | $28B | $15M | ████████████████ |
| Nov 2025 | 297 | 278 | $7B | $15.6M | █████████████ |
| Dec 2025 | 286 | 268 | $6.4B | $18.4M | █████████████ |
| Jan 2026 | 308 | 279 | $8.3B | $15M | ██████████████ |
| Feb 2026 | 444 | 417 | $14.9B | $16.7M | ████████████████████ |
| Mar 2026 | 341 | 315 | $10.1B | $19.9M | ███████████████ |
| Apr 2026 | 367 | 341 | $6.8B | $15M | █████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 21 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 9 Oct 2025 | Xai (x.ai) | Series A/Series B/etc. (undetermined) | $20B | nvidia, apollo global management, diameter capital partners | USA | Elon Musk’s AI startup xAI is raising more financing than initially planned, tapping backers including Nvidia Corp. to lift its ongoing… |
| 23 Jul 2025 | Thinking Machines Lab | Series A | $2B ⚠ check sentence | — | — | Thinking Machines Lab Co‑Founded by former OpenAI CTO Mira Murati, the startup secured a $2 billion Series A round at a $12 billion… |
| 28 Jan 2026 | Cloover (cloover.co) | Series A equity financing | $1.2B | — | Germany | Berlin-based climate fintech company Cloover has secured over $1.2 billion in funding commitments, comprising equity and debt facilities… |
| 26 Feb 2026 | Zyphra (zyphra.com) | Series A | $1B ⚠ check sentence | — | US | Zyphra is a full‑stack AI startup developing both foundation models and its Inference Cloud, a scalable platform for deploying generative… |
| 6 Jun 2025 | Strategy (strategygbd.com) | Series A Perpetual Preferred Stock | $979.7M | barclays | — | On June 5, 2025, Strategy announced an underwriting agreement with Barclays Capital Inc. for the issuance and sale of 11,764,700 shares of… |
| 24 Mar 2026 | Apptronik (apptronik.com) | Series A | $963.6M | AT&T Ventures, b capital, Datapower Ventures | USA |  |
| 28 Jan 2026 | Waabi (waabi.ai) | Series A/B (latest raise) | $750M | uber, G2 Venture Partners, khosla ventures | Canada | Uber will invest $250mn as part of a $750mn raise that values the company at $3bn, according to people familiar with the matter. |
| 8 May 2025 | Slate Auto | Series A and B | $700M | bezos expeditions, general catalyst, TWG Global | United States | Slate Auto, the startup electric vehicle manufacturer, today confirmed to Newsweek that the company raised $700 million total through… |
| 10 Feb 2026 | YASC | Series A | $532M | — | — | It follows a Series A round of over 3.8 billion yuan in 2023. |
| 11 Mar 2026 | Mind Robotics | Series A | $500M | accel, Andreessen Horowitz | United States | Mind Robotics raises $500M Series A to automate industrial manufacturing. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Featherless.ai | Series A | $20M | AMD Ventures, airbus ventures, bmw i ventures | — | Featherless.ai, a Singapore co-founded artificial intelligence (AI) firm, has secured $20 million in Series A funding co-led by AMD… |
| 30 Apr 2026 | Koda Health (kodahealthcare.com) | Series A | $14M | evidenced, Mudita Venture Partners, techstars | USA | Its series A round was led by Evidenced, with participation from Mudita Venture Partners, Techstars and the Texas Medical Center last… |
| 30 Apr 2026 | Moleculent (moleculent.com) | Extended Series A | $20M | Rubicon Healthcare Partners, arch venture partners, eir… | Sweden | NEW YORK – Swedish startup Moleculent said on Thursday that it has raised $20 million in extended Series A financing to help drive the… |
| 30 Apr 2026 | Dreamteam (dreamteam.gg) | Series A | $40M | accel, Together Fund | India | Chennai-based AI startup Dreamteam is in advanced discussions to raise around $40 million in its Series A funding round, with Accel and… |
| 30 Apr 2026 | Axoft (axoft.us) | Series A | $55M | C.P. Group Innovation, alumni ventures, Stanford… | USA | With the completion of a $55m fundraise, Axoft is planning to advance the development of its implantable brain-computer interfaces (iBCI). |
| 30 Apr 2026 | Rocsys (rocsys.com) | Series A | $13M | capricorn partners, Scania Invest, Forward.One | Netherlands | The Dutch startup announced the Rocsys M1, which it describes as the world’s first hands-free charging system capable of serving multiple… |
| 30 Apr 2026 | Rogo (rogodata.com) | Series A | — | Khosla | USA |  |
| 30 Apr 2026 | Studentcrowd (studentcrowd.com) | Series A | $8.9M | yfm equity partners, Midlands Engine Investment Fund II… | UK | StudentCrowd has secured £7m in Series A funding as it looks to expand its data platform into international markets. |
| 30 Apr 2026 | Pratech Brands (pratechbrands.com) | Series A | $10.6M | IvyCap Ventures Fund III, First Bridge India Growth Fund | India | Pratech Brands Private Limited, the parent company of Hyugalife, has raised $10.6 million (~₹100 crore) from a Series A fundraise led by… |
| 30 Apr 2026 | Performativ (performativ.com) | Series A | $14M | Deutsche Börse Group, rabo investments, fintech collective | Denmark | Performativ has raised $14 million in a Series A funding round led by Deutsche Börse Group, with participation from Rabo Investments, as… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --round-type "series a" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --round-type "series a" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --round-type "series a" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"round_type": "series a", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"round_type": "series a", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Seed Funding](seed-funding.md)
- [Series B Funding](series-b-funding.md)
- [AI Startup Funding News](ai-startup-funding-news.md)
