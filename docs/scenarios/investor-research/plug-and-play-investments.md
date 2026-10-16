# Plug and Play Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “plug and play investments” · 10/month India · 70/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [plug-and-play-investments.json](../../examples/scenarios/plug-and-play-investments.json).

**Question.** Which rounds did Plug and Play appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Plug and Play”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 87 |
| With a usable reported amount | 73 |
| Reported total (usable amounts) | $438.2M |
| Median reported round | $4M |
| Largest reported round | $75M |
| Busiest month | May 2025 (12 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 12 | 11 | $253M | $12M | ████████████████████ |
| Jun 2025 | 4 | 4 | $10.8M | $1.7M | ███████ |
| Jul 2025 | 7 | 4 | $13M | $4.4M | ████████████ |
| Aug 2025 | 9 | 7 | $22.6M | $3.5M | ███████████████ |
| Sep 2025 | 10 | 8 | $32M | $4.2M | █████████████████ |
| Oct 2025 | 11 | 10 | $29.7M | $2.2M | ██████████████████ |
| Nov 2025 | 2 | 1 | $8M | $8M | ███ |
| Dec 2025 | 8 | 8 | $36.4M | $4M | █████████████ |
| Jan 2026 | 1 | 1 | $4M | $4M | ██ |
| Feb 2026 | 9 | 7 | $15.2M | $1.4M | ███████████████ |
| Mar 2026 | 6 | 5 | $9.9M | $1.8M | ██████████ |
| Apr 2026 | 8 | 7 | $20.2M | $3.7M | █████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 16 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 13 May 2025 | Nawy Real Estate | Series A | $75M | Partech Africa, e& Capital, march capital | Egypt | Transaction Summary Nawy Real Estate (Nawy), an Egyptian property technology platform, raised $75 million through Series A equity and debt… |
| 15 Dec 2025 | Bitstack (bitstack-app.com) | Series A | $16.2M | 13books Capital, ag2r la mondiale, plug and play ventures | France | Bitstack raises €15M to accelerate its European expansion and launches its first Visa debit card. |
| 22 May 2025 | Kota (kota.com) | Series A | $14.5M | eurazeo, eqt ventures, northzone | Ireland | Irish insurance and employee benefits platform Kota has announced a raised of $14.5m in a Series A funding round, bringing its total raise… |
| 12 Aug 2025 | Certivity (certivity.io) | Series A | $14.4M | almaz capital, uvc partners, Earlybird X | Germany | Certivity, a Munich, Germany-based RegTech software solutions provider, has raised €13.3 million in Series A funding. |
| 15 Oct 2025 | Chari (chari.com) | Series A | $12M | spe capital, Orange Ventures, Verod-Kepple | Morocco | Chari, the Moroccan startup supported by Y Combinator and founded in 2020 by the couple Ismael Belkhayat and Sophia Alj, announces a… |
| 19 May 2025 | Vuz (vuz.com) | Pre-Series C | $12M | international finance corporation, Al Jazira Capital,… | Saudi Arabia | Vuz, the immersive media platform, has announced a strategic investment from the International Finance Corporation (IFC), a member of the… |
| 6 May 2025 | Queens Carbon (queenscarbon.com) | seed | $10M | plug and play, clean energy venture group, Buzzi Unicem USA | USA | Queens Carbon, a developer of next‑generation cement technology, announced it has secured $10 million in seed funding to scale its… |
| 6 Nov 2025 | Lyzr (lyzr.ai) | Series A | $8M | accenture, firstsource, GFT Ventures | United States | Lyzr, the enterprise agentic AI infrastructure company, announced that it has raised an $8 million Series A round led by Rocketship.vc. |
| 13 Jun 2025 | Hirundo (hirundo.es) | seed | $8M | maverick ventures israel, SuperSeed, alpha intelligence… | Israel | Hirundo, which closed an $8 million seed round led by Maverick Ventures Israel, with participation from SuperSeed, Alpha Intelligence… |
| 18 Sep 2025 | Myriad AI | Seed | $7.8M | Category Ventures, long journey ventures, 10vc | — | Myriad AI, a San Francisco- and Prague-based startup specializing in automating regulatory compliance for enterprises, has raised $7.8… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Synaps (synaps.io) | pre-seed | $3.6M | plug and play, Fil Rouge Capital | Austria | Five months later, Synaps is announcing a $3.6 million pre‑seed funding round from US‑based accelerator and VC Plug and Play, and… |
| 27 Apr 2026 | OGold | Strategic Investment | — | plug and play ventures | United Arab Emirates | OGold has secured a strategic investment from Plug and Play Ventures |
| 27 Apr 2026 | Fermeate | seed | $2M | Newfund Capital, sosv, Ajinomoto Group Ventures | USA | Fermeate—a California-based startup using light to turbocharge cell productivity in biomanufacturing—has closed a $2 million seed round… |
| 13 Apr 2026 | Ralio | pre-Seed | $2.3M | Seed X, love ventures, plug and play | United Kingdom | Ralio, a London-based FinTech startup building a payments platform tailored for business AI agents, has announced a €2.1 million ($2.5… |
| 5 Apr 2026 | Omniscient (o8t.com) | pre‑seed | $4.1M | seedcamp, plug and play, MS&AD | France | Omniscient, the Paris‑based decision intelligence platform built for boards and senior executives, has raised $4.1 million in a pre‑seed… |
| 3 Apr 2026 | UnblockPay | Seed | $4.5M | prelude, plug and play, wintermute | Brazil | UnblockPay raised $4.5 million in a seed round led by Prelude, with participation from Plug and Play, Wintermute, Signature Ventures, and… |
| 2 Apr 2026 | Omniscient (o8t.com) | pre-seed | $3.8M | seedcamp, Drysdale, plug and play | France | Omniscient, a Paris-based decision intelligence platform for boards and senior executives, has raised €3.5 million ($4.1 million) in… |
| 30 Mar 2026 | Skillsvest | pre-seed | $660k | plug and play ventures, Sascha Mornell | India | Skillsvest has announced the closure of its ₹5.5 crore pre-seed funding round, comprising a mix of equity and debt, to expand its mission… |
| 16 Mar 2026 | WhiteBridge AI | seed | $3M | FIRSTPICK VC, First Degree, NGL.VC | Lithuania | WhiteBridge AI, the Vilnius-based people-search and digital identity platform, has raised a $3 million seed round, equivalent to roughly… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "Plug and Play" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "Plug and Play" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "Plug and Play" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Plug and Play", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Plug and Play", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Elevation Capital Portfolio](elevation-capital-portfolio.md)
- [Google Ventures Portfolio](google-ventures-portfolio.md)
- [GIC Portfolio](gic-portfolio.md)
- [Atomico Investments](atomico-investments.md)
