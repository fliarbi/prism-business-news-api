# Foodtech Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “foodtech funding” · volume below estimate threshold  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [foodtech-funding.json](../../examples/scenarios/foodtech-funding.json).

**Question.** How many foodtech deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “foodtech”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 61 |
| With a usable reported amount | 56 |
| Reported total (usable amounts) | $1.8B |
| Median reported round | $4M |
| Largest reported round | $1.2B |
| Busiest month | Jun 2025 (11 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1 | 1 | $1.4M | $1.4M | ██ |
| Jun 2025 | 11 | 9 | $77.7M | $3.5M | ████████████████████ |
| Jul 2025 | 9 | 8 | $65M | $2.2M | ████████████████ |
| Aug 2025 | 2 | 2 | $1.8M | $908k | ████ |
| Sep 2025 | 2 | 2 | $1.1M | $540k | ████ |
| Oct 2025 | 8 | 8 | $148.5M | $16.3M | ███████████████ |
| Nov 2025 | 6 | 6 | $33.3M | $2.1M | ███████████ |
| Dec 2025 | 8 | 8 | $1.3B | $20.8M | ███████████████ |
| Jan 2026 | 3 | 2 | $4.3M | $2.2M | █████ |
| Feb 2026 | 4 | 3 | $20.5M | $6.7M | ███████ |
| Mar 2026 | 2 | 2 | $72.6M | $36.3M | ████ |
| Apr 2026 | 5 | 5 | $48.1M | $6M | █████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 7 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 8 Dec 2025 | Swiggy (swiggy.com) | Qualified Institutional Placement (QIP) | $1.2B | — | India | Swiggy today said its shareholders approved a proposal to raise up to INR 10,000 Cr via qualified institutional placement (QIP). |
| 28 Dec 2025 | Calo (calo.app) | Series B | $64M | aljazira capital, Nuwa Capital, stv | Saudi Arabia | Calo, a personalised meal subscription startup founded in 2019, has raised $64 million in Series B funding to fuel its global expansion… |
| 11 Jun 2025 | Tastewise (tastewise.io) | Series B | $50M | — | Israel | TASTEWISE \| Announced a $50 million Series B fundraising round to further develop its AI-powered platform for the food and beverage… |
| 21 Oct 2025 | Matr Foods (matrfoods.com) | Series A | $43.2M ⚠ check sentence | novo holdings, Export and Investment Fund of Denmark… | Denmark | The company has completed a €40 million fundraise, comprising €20 million in Series A equity and €20 million in venture debt, the largest… |
| 24 Mar 2026 | Swish (swishanalytics.com) | Series B | $38M | Hara Global, bain capital ventures, accel | — | Swish, a 10-minute food delivery startup, raised $38 million in a Series B round led by Hara Global and Bain Capital Ventures, with… |
| 10 Mar 2026 | Verley | — | $34.6M | alven | France | The Lyon start-up Verley is closing a fund raising of 32 million euros to speed up the marketing of its whey proteins produced by… |
| 15 Oct 2025 | Savor (savor.co) | — | $33M | breakthrough energy ventures, synthesis capital | United States | With financial support from Breakthrough Energy Ventures, a capital fund led by Bill Gates, and Synthesis Capital, Savor, a foodtech… |
| 23 Apr 2026 | Planetary (planetarytech.com) | — | $28M | — | — | Planetary nets $28m to scale fermentation infrastructure and licensing platform |
| 25 Nov 2025 | Revyve (revyve.bio) | — | $25.9M | — | Netherlands | The Netherlands saw a larger round with Revyve closing approximately €24 million to scale yeast-based egg-replacement proteins |
| 3 Oct 2025 | Eternal (eternal.bio) | employee stock option grant | $25.3M | — | India | Zomato’s parent company, Eternal Ltd., has approved a fresh grant of employee stock options (ESOPs) worth approximately INR 211 crore,… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 24 Apr 2026 | Cosaic (cosaic.io) | — | $6M | dsm-firmenich Ventures | — | Planetary has raised USD 28 million and Cosaic USD 6 million. |
| 23 Apr 2026 | Planetary (planetarytech.com) | — | $28M | — | — | Planetary nets $28m to scale fermentation infrastructure and licensing platform |
| 20 Apr 2026 | Adamo Foods (adamofoods.com) | grant | $10.8M | Bühler, tu delft | — | ADAMO FOODS \| Lands a €10M EU grant as part of the MycoStruct consortium to scale the production of its whole-cut mycelium steaks. |
| 17 Apr 2026 | Falaê | seed | $300k | Investidores.vc | Brazil | Brazilian startup Falaê raised about $300,000 (R$1.5 million) in its first funding round led by Investidores.vc. |
| 7 Apr 2026 | Chatfood (chatfood.io) | — | $3M | antler, 6G Capital, zinal growth | UAE | UAE-based FoodTech ChatFood raised $3 million led by Antler with a reserved amount for key strategic Saudi partners where 6G Capital and… |
| 24 Mar 2026 | Swish (swishanalytics.com) | Series B | $38M | Hara Global, bain capital ventures, accel | — | Swish, a 10-minute food delivery startup, raised $38 million in a Series B round led by Hara Global and Bain Capital Ventures, with… |
| 10 Mar 2026 | Verley | — | $34.6M | alven | France | The Lyon start-up Verley is closing a fund raising of 32 million euros to speed up the marketing of its whey proteins produced by… |
| 6 Feb 2026 | Green Rebel Foods (greenrebelfoods.com) | — | $12.5M | Unovis NCAP Fund II, Teja Ventures, Agfunder Alternative… | Indonesia | Indonesia’s first plant-based meat company, Green Rebel Foods, has raised US$12.5 million in its latest funding round, valuing the company… |
| 5 Feb 2026 | Goals Inc. | Debt Financing | $6.7M | mizuho bank, aozora corporate investment, shoko chukin bank | Japan | Funding Details Company: Goals Inc. Raised: ¥1.0B Round: Debt Financing Funding Date: February 2026 Investors: Mizuho Bank, Aozora… |
| 4 Feb 2026 | Barakah (barakah.app) | strategic | — | foodlabs | Saudi Arabia | Barakah, a Saudi Arabia-based foodtech startup, has secured a strategic funding round from German-based VC FoodLabs |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector foodtech --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector foodtech --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector foodtech --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "foodtech", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "foodtech", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Defence Tech Funding](defence-tech-funding.md)
- [E-commerce Funding](e-commerce-funding.md)
- [Hrtech Funding](hrtech-funding.md)
- [Legaltech Funding](legaltech-funding.md)
