# Fintech Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “fintech funding” · 110/month India · 110/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [fintech-funding.json](../../examples/scenarios/fintech-funding.json).

**Question.** How many fintech deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “fintech”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 2,062 |
| With a usable reported amount | 1,872 |
| Reported total (usable amounts) | $152.7B |
| Median reported round | $15M |
| Largest reported round | $10B |
| Amounts left out as implausible or unconverted | 2 |
| Busiest month | Oct 2025 (210 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 175 | 164 | $11B | $15M | █████████████████ |
| Jun 2025 | 178 | 163 | $11.5B | $22M | █████████████████ |
| Jul 2025 | 175 | 157 | $13.5B | $21.6M | █████████████████ |
| Aug 2025 | 171 | 154 | $12.2B | $18.1M | ████████████████ |
| Sep 2025 | 206 | 183 | $13.7B | $10M | ████████████████████ |
| Oct 2025 | 210 | 185 | $16.6B | $18M | ████████████████████ |
| Nov 2025 | 171 | 153 | $10.2B | $19M | ████████████████ |
| Dec 2025 | 167 | 157 | $12.1B | $17.5M | ████████████████ |
| Jan 2026 | 142 | 136 | $9.6B | $19.2M | ██████████████ |
| Feb 2026 | 178 | 154 | $18B | $12.5M | █████████████████ |
| Mar 2026 | 149 | 141 | $14.3B | $12M | ██████████████ |
| Apr 2026 | 140 | 125 | $21.2B | $15.6M | █████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 17 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 11 Feb 2026 | Grab (getgrab.com) | — | $10B ⚠ check sentence | — | Singapore | Grab, the pioneering superapp for ride-hailing, food delivery, and fintech, tops the list with over $10 billion in total funding since its… |
| 27 Apr 2026 | Nubank (nubank.com.br) | — | $9B | — | Brazil | Nubank, one of the largest digital financial services platforms in the world, announces investments of approximately BRL 45 billion… |
| 19 Mar 2026 | Nuvei (nuvei.com) | — | $6.3B | — | Canada | Not only did the $6.3 billion take-private of Nuvei affect markets, but it also altered the discourse. |
| 12 Jun 2025 | DeFi Development Corp. | — | $5B | RK Capital Management LLC | United States | On June 11, 2025, DeFi Development Corp. entered into a Share Purchase Agreement with RK Capital Management LLC, allowing the company to… |
| 17 Sep 2025 | Forward Industries (forwardindustries.com) | ATM Equity Offering | $4B | — | US | Forward Industries has announced plans to establish an at-the-market (ATM) equity offering program, potentially raising up to $4 billion. |
| 20 Oct 2025 | Revolut (revolut.com) | — | $3B | — | United Kingdom | Revolut, the London‑based digital banking giant, has closed a record‑breaking $3 billion funding round, valuing the company at about $75… |
| 2 Feb 2026 | Tamara (tamara.co) | debt | $2.4B | — | Saudi Arabia | Saudi fintech firms, including Tamara, which secured a $2.4 billion debt facility, and Hala, which closed a $157 million Series B round. |
| 23 May 2025 | Acrisure (acrisure.com) | New issuance of convertible senior preferred stock | $2.1B | bain capital, Fidelity Management & Research Company,… | — | Acrisure, a global FinTech company delivering tech-powered financial services to businesses and individuals, has raised $2.1bn through a… |
| 2 Apr 2026 | Klarna (klarna.com) | Forward-Flow Facility | $2B | elliott investment management | USA | The $2 billion forward-flow facility with funds managed by Elliott Investment Management announced in March, which is structured to… |
| 2 Dec 2025 | Blanco (blanco.com) | — | $2B | broota | Chile | A $2 billion amount is what the Chilean Fintech Blanco hopes to raise, through Broota. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Performativ (performativ.com) | Series A | $14M | Deutsche Börse Group, rabo investments, fintech collective | Denmark | Performativ has raised $14 million in a Series A funding round led by Deutsche Börse Group, with participation from Rabo Investments, as… |
| 29 Apr 2026 | Ebury (ebury.com) | — | $698.5M | santander, centerbridge partners, vitruvian partners | — | "Santander has agreed to participate in c.£550 million funding rounds for Ebury, its global fintech platform focused on cross-border… |
| 29 Apr 2026 | Payjoy (payjoy.com) | credit line | $140M | neuberger berman | Peru | On March 17, and gradually around that date in other countries, Peru closed the operation whereby private investment manager Neuberger… |
| 29 Apr 2026 | Upstart (upstart.com) | forward-flow commitment | $1.2B | fortress investment group | United States | Fortress has agreed to purchase up to $1.25 billion of consumer loans originated through the Upstart platform over the course of 15 months. |
| 29 Apr 2026 | Sahi (sahi.com.tr) | Series B | $33M | accel, elevation capital, others | India | Sahi Raises $33 Mn Series B |
| 29 Apr 2026 | Lemfi (lemfi.com) | — | $127M | — | UK | LemFi has committed GBP £100 million to the UK economy over the next five years |
| 29 Apr 2026 | Chazm | Series A | — | stonebridge, Shorooq, kb investment | South Korea | Shorooq, a leading multi-strategy investment firm, today announced its investment in the Series A funding round of Chazm, a South… |
| 29 Apr 2026 | Novio (novio.com) | Series A | $12M | cornerstone ventures, Shepherd’s Hill Private Equity,… | India | Indian FinTech startup Novio has raised ₹100 crore (approximately $10.5 million) in a Series A funding round led by Cornerstone Ventures,… |
| 28 Apr 2026 | HiSofi (hisofi.com) | seed | $1M | Sororitê, saasholic, other investors | Brazil | HiSofi, Fintech of São Paulo, has just raised R$ 5 million in a seed round (initial phase of investments in startups) with participation… |
| 28 Apr 2026 | Onsetto | Seed II | $9M | canapi ventures, EJF Ventures, Idea Fund of La Crosse | — | Onsetto, a fintech platform focused on helping financial institutions win and activate business banking relationships, announced today… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector fintech --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector fintech --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector fintech --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "fintech", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "fintech", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Series D Funding](series-d-funding.md)
- [Gaming Funding](gaming-funding.md)
- [SAAS Funding News](saas-funding-news.md)
- [Unicorn Funding](unicorn-funding.md)
