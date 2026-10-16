# Healthtech Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “healthtech funding” · 20/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [healthtech-funding.json](../../examples/scenarios/healthtech-funding.json).

**Question.** How many healthtech deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “healthtech”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 325 |
| With a usable reported amount | 287 |
| Reported total (usable amounts) | $6.4B |
| Median reported round | $6.5M |
| Largest reported round | $400M |
| Busiest month | Oct 2025 (40 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 23 | 19 | $574.6M | $9M | ████████████ |
| Jun 2025 | 24 | 21 | $366.3M | $8.9M | ████████████ |
| Jul 2025 | 24 | 23 | $511.5M | $7.7M | ████████████ |
| Aug 2025 | 32 | 21 | $406.7M | $6M | ████████████████ |
| Sep 2025 | 34 | 31 | $1.8B | $20M | █████████████████ |
| Oct 2025 | 40 | 38 | $794.9M | $7.8M | ████████████████████ |
| Nov 2025 | 23 | 19 | $582.5M | $5M | ████████████ |
| Dec 2025 | 13 | 12 | $116.3M | $3.4M | ██████ |
| Jan 2026 | 23 | 23 | $328.9M | $3.6M | ████████████ |
| Feb 2026 | 38 | 37 | $447.8M | $6.5M | ███████████████████ |
| Mar 2026 | 28 | 24 | $867.7M | $9.3M | ██████████████ |
| Apr 2026 | 23 | 19 | $142.4M | $1.9M | ████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 9 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 23 Sep 2025 | Judi Health (Capital Rx) | Series F | $400M | wellington management, general catalyst, Generation IM | USA |  |
| 20 Nov 2025 | Function Health (functionhealth.com) | Series B | $298M | redpoint ventures, Andreessen Horowitz, aglaé ventures | — | Function Health raised $298 million in Series B funding. |
| 15 Jul 2025 | PB Healthcare | initial round of funding | $218M | general catalyst | India | In May of this year, the vertical raised $218 million in its initial round of funding, which was headed by General Catalyst. |
| 4 Sep 2025 | Ortivity (ortivity.de) | Not disclosed | $216M | apheon, unigestion | Germany | Ortivity, a Munich‑based healthtech startup focused on outpatient orthopedic care, has raised €200 million (approximately $215 million) in… |
| 16 Sep 2025 | Pharmeasy (pharmeasy.in) | Debt Financing | $204M ⚠ check sentence | 360 one, Alkram Ventures, MVS Ventures | India | The funding will be used primarily to repay a loan from Goldman Sachs, as PharmEasy works to restructure its obligations following a… |
| 31 Mar 2026 | Whoop (whoop.com) | Financing round | $200M ⚠ check sentence | softbank, ivp, GP Bullhound Fund V | United States | In September 2021, GP Bullhound announced a new investment into WHOOP. The $200m financing round at a $3.4bn valuation was led by Softbank… |
| 26 Mar 2026 | Emed (emed.com) | — | $200M ⚠ check sentence | AON Consulting, Inc., NFL legend and eMed Founding Chief… | USA | eMed today announced it has raised $200 million in funding at a $2 billion plus valuation. |
| 15 Oct 2025 | Oura (ouraring.com) | — | $200M ⚠ check sentence | — | Finland | The round values Oura at around $11 billion, more than double its valuation of $5 billion when it raised $200 million. |
| 1 Sep 2025 | Craneware (craneware.com) | Credit Facility | $200M | hsbc, barclays, natwest | UK | Craneware said it has renewed its $100 million revolving credit facility (RCF) on improved terms, with the option of extending it for two… |
| 15 Sep 2025 | UltraGreen.ai | — | $188M | 65 Equity Partners, vitruvian partners, August Global… | Singapore | UltraGreen.ai has secured a US$188 million investment round led by 65 Equity Partners and Vitruvian Partners. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Sprect (sprect.com) | Seed | $240k | — | India | Sprect Raises ₹2 Cr Seed Round |
| 29 Apr 2026 | Sprect (sprect.com) | Seed | $2.4M | — | India | Sprect Raises ₹2 Cr Seed Round Sprect, a platform offering expert consultations, raised INR 2 crore in funding. |
| 28 Apr 2026 | Dehaze (dehaze.io) | seed | $3.5M | YZR Capital, dn capital, angel invest | Germany | The Munich-based healthtech start-up Dehaze has completed a seed round of 3.2 million euros. |
| 27 Apr 2026 | TriFetch | pre-seed | $1.9M | nexus venture partners, google, hippocratic ai | USA | TriFetch, a San Francisco-based healthtech startup, has raised $1.9 million in pre-seed funding led by Nexus Venture Partners, with angel… |
| 22 Apr 2026 | Calibre (calibre-ebook.com) | pre-Seed | $3M ⚠ check sentence | Berlin-based Amino Collective, Daybreak Ventures, cocoa… | UK | Calibre, a London-based HealthTech company, exits stealth mode after raising €2.8 million (£2.5 million) in pre-Seed funding to date. |
| 22 Apr 2026 | Acuitymd (acuitymd.com) | Series C | $80M | stepstone group, benchmark, redpoint ventures | USA | Funding Details Company: AcuityMD, Inc. Raised: $80.0M Round: Series C Funding Date: April 2026 Lead Investor: StepStone Group Additional… |
| 20 Apr 2026 | Axten Hospitals | Pre-Seed | $300k | pedalstart, Angel Investors | India | Axten Hospitals Raises INR 2.5 Cr from PedalStart A unit of TAH Global Healthcare Pvt. Ltd., Axten Hospitals, has raised INR 2.5 crore in… |
| 11 Apr 2026 | Na | Seed | $1.7M | Caret Capital, Ev2 Ventures, ThinKuvate | India | In a previous seed funding round, the Kochi-based startup raised about $1.71 million from investors like Caret Capital, Ev2 Ventures, and… |
| 10 Apr 2026 | Surf Therapeutics (surftherapeutics.vdtrxn) | — | — | Jetstream Venture Fund | — | Jetstream Venture Fund announced it has secured positions in two startups, Surf Therapeutics and Hill Research, marking a significant… |
| 10 Apr 2026 | Gabify | — | $30k | GHRTBI | India | Additionally, the startup received Rs 25 lakh from GHRTBI under the Nidhi Seed Support Scheme. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector healthtech --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector healthtech --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector healthtech --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "healthtech", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "healthtech", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Creator Economy Funding](creator-economy-funding.md)
- [Femtech Funding](femtech-funding.md)
- [Manufacturing Startup Funding](manufacturing-startup-funding.md)
- [Media Startup Funding](media-startup-funding.md)
