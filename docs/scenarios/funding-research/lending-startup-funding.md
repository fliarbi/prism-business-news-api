# Lending Startup Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “lending startup funding” · volume below estimate threshold  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [lending-startup-funding.json](../../examples/scenarios/lending-startup-funding.json).

**Question.** How many lending startup deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “lending”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 113 |
| With a usable reported amount | 101 |
| Reported total (usable amounts) | $9.2B |
| Median reported round | $26.8M |
| Largest reported round | $1.9B |
| Amounts left out as implausible or unconverted | 1 |
| Busiest month | Oct 2025 (15 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 4 | 4 | $255.3M | $61M | █████ |
| Jun 2025 | 7 | 7 | $813.8M | $76.5M | █████████ |
| Jul 2025 | 3 | 3 | $1.9B | $23.3M | ████ |
| Aug 2025 | 12 | 12 | $329.3M | $10.8M | ████████████████ |
| Sep 2025 | 7 | 7 | $560.2M | $64M | █████████ |
| Oct 2025 | 15 | 9 | $562.1M | $18.5M | ████████████████████ |
| Nov 2025 | 7 | 4 | $732.6M | $165M | █████████ |
| Dec 2025 | 12 | 11 | $287.6M | $18M | ████████████████ |
| Jan 2026 | 10 | 10 | $376.1M | $26.4M | █████████████ |
| Feb 2026 | 14 | 13 | $688.7M | $23M | ███████████████████ |
| Mar 2026 | 14 | 14 | $1.5B | $21M | ███████████████████ |
| Apr 2026 | 8 | 7 | $1.2B | $140M | ███████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 6 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 3 Jul 2025 | Propel Finance (propelfinance.co.uk) | Series | $1.9B | barclays, bank of america, citi | United Kingdom | Propel Finance has secured a £1.5 billion funding round to expand its support for small and medium-sized enterprises (SMEs) across the UK. |
| 17 Mar 2026 | Upstart (upstart.com) | forward-flow commitment | $1B | Eltura Capital Management, aperture investors | — | Artificial intelligence (AI) lending marketplace Upstart has secured a $1bn (£0.74bn) forward-flow commitment with alternative asset… |
| 8 Apr 2026 | Poonawalla Fincorp (poonawallafincorp.com) | QIP | $600M | — | India | Poonawalla Fincorp is likely to launch a qualified institutional placement (QIP) to raise up to ₹5,000 crore, according to CNBC-TV18… |
| 5 Jun 2025 | Crebrid | credit facility | $500M | barings | — | Barings has announced a new credit facility with real estate lending platform Crebrid, with Barings’ investors taking a minority equity… |
| 18 Nov 2025 | Quantum Lending Solutions | — | $400M | global asset-based private credit firm, atlas sp partners,… | USA | Quantum Lending Solutions (“Quantum”), an AI-based enterprise platform that enables banks, marketplaces, and technology platforms to make… |
| 6 Oct 2025 | Pagaya (pagaya.com) | ABS transaction | $400M | One William Street Capital Management, L.P. (OWS) | — | Pagaya Technologies LTD. (“Pagaya” or “the Company”), a global technology company delivering AI-driven product solutions for the financial… |
| 19 Feb 2026 | Kiavi (kiavi.com) | rated securitization | $350M | Nomura Securities International, Inc., barclays, deutsche… | United States | Kiavi, a leading AI-powered non-bank lending platform to residential real estate investors, today announced the closing of a $350 million… |
| 5 Nov 2025 | Bmg Money (bmgmoney.com) | Financing Facility | $300M | webbank, Waterfall Asset Management | USA | BMG Money announced today that it has secured a $300 million financing facility with Utah-based WebBank, a leading national issuer of… |
| 8 Apr 2026 | Kreditbee (kreditbee.in) | Series E | $280M ⚠ check sentence | — | India | KreditBee has raised $280 million in a Series E round, achieving a valuation of $1.5 billion and entering the unicorn club. |
| 4 Mar 2026 | Youlend (youlend.com) | forward-flow financing facility | $225M | Värde Partners | United States | YouLend has secured a multi-year forward-flow financing facility from Värde Partners, in a move aimed at expanding its capital base and… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 22 Apr 2026 | Revltek (revltek.com) | revolving line of credit | — | Texas Capital | United States | RevlTek, a credit union service organization (CUSO) leveraging financial technology to originate, administer and purchase purpose-driven… |
| 15 Apr 2026 | JPalmer Collective | Credit Facility | $135M | Texas Capital, dime community bank, Forbright Bank | United States | JPalmer Collective (JPC), an asset-based lending firm supporting fast-growing, women-led and natural products companies, today announced… |
| 8 Apr 2026 | Paywatch (paywatch.co.kr) | — | $20M | — | Malaysia | Fintech firms like Paywatch and Funding Societies underscore the sector's appeal, with recent rounds exceeding $20 million each to expand… |
| 8 Apr 2026 | Funding Societies (fundingsocieties.com) | — | $20M | — | Malaysia | Fintech firms like Paywatch and Funding Societies underscore the sector's appeal, with recent rounds exceeding $20 million each to expand… |
| 8 Apr 2026 | Braviant Holdings (braviantholdings.com) | Revolving asset-backed credit facility | $145M | — | USA | Braviant Holdings, a Chicago-based technology-driven consumer lending platform has secured approximately $145m in committed capacity… |
| 8 Apr 2026 | Kreditbee (kreditbee.in) | Series E | $280M ⚠ check sentence | — | India | KreditBee has raised $280 million in a Series E round, achieving a valuation of $1.5 billion and entering the unicorn club. |
| 8 Apr 2026 | Poonawalla Fincorp (poonawallafincorp.com) | QIP | $600M | — | India | Poonawalla Fincorp is likely to launch a qualified institutional placement (QIP) to raise up to ₹5,000 crore, according to CNBC-TV18… |
| 30 Mar 2026 | Metafin (metafin.in) | — | $10M | — | India | "Metafin raised $10 million in debt," |
| 30 Mar 2026 | Finfinity (finfinity.co.in) | — | $2.4M | — | India | "Finfinity raised $2.4 million," |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector lending --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector lending --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector lending --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "lending", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "lending", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Hrtech Funding](hrtech-funding.md)
- [Legaltech Funding](legaltech-funding.md)
- [Martech Funding](martech-funding.md)
- [Payments Startup Funding](payments-startup-funding.md)
