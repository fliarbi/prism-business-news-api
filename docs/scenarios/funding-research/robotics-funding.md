# Robotics Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “robotics funding” · 10/month India · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [robotics-funding.json](../../examples/scenarios/robotics-funding.json).

**Question.** How many robotics deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “robotics”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 538 |
| With a usable reported amount | 454 |
| Reported total (usable amounts) | $46B |
| Median reported round | $20.8M |
| Largest reported round | $7B |
| Busiest month | Mar 2026 (63 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 12 | 12 | $119M | $7.2M | ████ |
| Jun 2025 | 37 | 31 | $1.5B | $23M | ████████████ |
| Jul 2025 | 49 | 36 | $1.3B | $24M | ████████████████ |
| Aug 2025 | 38 | 28 | $2B | $20M | ████████████ |
| Sep 2025 | 58 | 47 | $5.1B | $16.5M | ██████████████████ |
| Oct 2025 | 35 | 28 | $1.4B | $40M | ███████████ |
| Nov 2025 | 56 | 51 | $5.4B | $14M | ██████████████████ |
| Dec 2025 | 35 | 27 | $1.2B | $20.1M | ███████████ |
| Jan 2026 | 44 | 42 | $4.8B | $10M | ██████████████ |
| Feb 2026 | 58 | 51 | $4.5B | $21.3M | ██████████████████ |
| Mar 2026 | 63 | 55 | $8.1B | $35M | ████████████████████ |
| Apr 2026 | 53 | 46 | $13.7B | $82M | █████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 29 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 13 Apr 2026 | Brils | — | $7B | POSCO Group | — | POSCO Group invested W7bn in robot solutions provider Brils to advance automation and AI in manufacturing. |
| 26 Mar 2026 | SkildAI | — | $1.4B | — | — | SkildAI's $1.4B round |
| 14 Jan 2026 | Skild AI | Series C | $1.4B | softbank group, nventures, bezos expeditions | US | Skild AI, a Pittsburgh-based robotics AI startup, secured a mammoth $1.4 billion funding round to accelerate development of its… |
| 5 Apr 2026 | Neura Robotics (neura-robotics.com) | — | $1.2B | Sheikh Hamad bin Jassim Al Thani, amazon, qualcomm ventures | Germany | Metzingen-based robotics startup Neura Robotics has secured approximately $1.2 billion in funding, with participation from Sheikh Hamad… |
| 14 Apr 2026 | Figure AI | — | $1B | — | — | Companies such as Figure AI, a humanoid robotics startup, and Agility Robotics have raised as much as $1 billion and $641 million,… |
| 27 Mar 2026 | Physical Intelligence (physicalintelligence.company) | — | $1B ⚠ check sentence | founders fund, lightspeed venture partners, thrive capital | USA | Physical Intelligence, the two-year-old San Francisco robotics startup, is in discussions to raise about $1 billion in new funding at a… |
| 2 Sep 2025 | Ubtech (ubtrobot.com) | credit line | $1B | infini capital | China | Humanoid robotics developer UBTECH Robotics Corp. has reportedly secured a credit line of up to $1 billion from Infini Capital to expand… |
| 24 Mar 2026 | Apptronik (apptronik.com) | Series A | $963.6M | AT&T Ventures, b capital, Datapower Ventures | USA |  |
| 12 Jan 2026 | Ondas Holdings Inc. | direct offering | $959.2M | an institutional investor | United States | Ondas estimates net proceeds from the offering to be approximately $959.2 million, after deducting placement agent fees and estimated… |
| 14 Apr 2026 | Agility Robotics (agilityrobotics.com) | — | $641M | — | — | Companies such as Figure AI, a humanoid robotics startup, and Agility Robotics have raised as much as $1 billion and $641 million,… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Apera AI (apera.ai) | Strategic Investment | — | Zebra Ventures | — | Zebra Ventures, the corporate venture capital arm of Zebra Technologies Corporation (NASDAQ: ZBRA ), today announced a strategic… |
| 29 Apr 2026 | Monumental (monumental.co) | seed | $25M | — | — | As we previously covered, Monumental, a Dutch startup, has built a working bricklaying robot that has already completed commercial… |
| 29 Apr 2026 | All3 | seed | $25M | rtp global, SuperSeed, begin capital | — | All3, a construction robotics company, has raised $25 million in seed funding to bring its robotic construction platform to market. |
| 28 Apr 2026 | Skydio (skydio.com) | Series F | $110M ⚠ check sentence | — | USA | Skydio has raised $110 million in Series F financing, led by existing investors, bringing the company’s valuation to $4.4 billion. |
| 28 Apr 2026 | Kemaro (kemaro.ch) | Series B | $4.5M | Spicehaus Partner AG | Switzerland | Swiss robotics innovator KEMARO has secured €4.2 million ($5 million) in an initial pre-closing of its Series B financing round to… |
| 27 Apr 2026 | Sereact (sereact.ai) | Series B | $11M | headline, Bullhound Capital, felix capital | Germany | German robotics software company Sereact has secured $110 million in a Series B funding round. |
| 27 Apr 2026 | Squaremind (squaremind.io) | pre-Series A | $18M | sonder capital, Deeptech 2030 Fund, Adamed Technology | France | SquareMind, an AI and robotics company developing solutions for dermatology, has announced $18 million in funding, including previously… |
| 27 Apr 2026 | Sereact (sereact.ai) | Series B | $110M | headline, Bullhound Capital, felix capital | Germany | Sereact, the Stuttgart-based AI robotics software company, has raised $110 million in a Series B round led by Headline, the international… |
| 27 Apr 2026 | Linkerbot | Series B+ | — | ant group, HongShan Group, Zhongguancun Science Park Fund | China | Beijing-based Linkerbot completed what it called a “series B+” funding round last week that valued it at $3 billion. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector robotics --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector robotics --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector robotics --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "robotics", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "robotics", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Unicorn Funding](unicorn-funding.md)
- [Venture Debt Funding](venture-debt-funding.md)
- [Cybersecurity Funding](cybersecurity-funding.md)
- [Deep Tech Funding](deep-tech-funding.md)
