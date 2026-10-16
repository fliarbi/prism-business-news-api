# Medtech Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “medtech funding” · 10/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [medtech-funding.json](../../examples/scenarios/medtech-funding.json).

**Question.** How many medtech deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “medtech”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 122 |
| With a usable reported amount | 103 |
| Reported total (usable amounts) | $1.8B |
| Median reported round | $7.1M |
| Largest reported round | $150M |
| Busiest month | Jan 2026 (15 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 10 | 9 | $117.3M | $1.4M | █████████████ |
| Jun 2025 | 9 | 8 | $151.8M | $6.7M | ████████████ |
| Jul 2025 | 13 | 10 | $120.7M | $8.1M | █████████████████ |
| Aug 2025 | 6 | 6 | $78.2M | $2.7M | ████████ |
| Sep 2025 | 9 | 4 | $69.6M | $17.8M | ████████████ |
| Oct 2025 | 11 | 11 | $278.6M | $11.2M | ███████████████ |
| Nov 2025 | 13 | 9 | $263.3M | $4.3M | █████████████████ |
| Dec 2025 | 8 | 7 | $199.7M | $6.1M | ███████████ |
| Jan 2026 | 15 | 14 | $246.5M | $16.2M | ████████████████████ |
| Feb 2026 | 12 | 11 | $56.4M | $4.7M | ████████████████ |
| Mar 2026 | 8 | 6 | $71.7M | $9.4M | ███████████ |
| Apr 2026 | 8 | 8 | $121.6M | $7.9M | ███████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 11 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 21 Nov 2025 | Distalmotion (distalmotion.com) | Series G | $150M | Revival Healthcare Capital, inside investor | Switzerland | Walder Wyss advised Distalmotion, a globally active MedTech company based in Lausanne, throughout closing of its USD 150 million series G… |
| 27 Jun 2025 | Forsight Robotics (forsightrobotics.com) | Series B | $125M | eclipse | Israel | This week, Israeli medtech startup ForSight Robotics raised a massive $125 million in a Series B round led by Eclipse. |
| 3 Dec 2025 | Fire1 (fire1foundry.com) | late-stage deal | $124.2M | — | Ireland | Ireland’s maturing ecosystem continued into 2025 with a €115 million (£101m) late-stage deal for Dublin-based medical device firm FIRE1,… |
| 21 Oct 2025 | Comind (comind.io) | — | $102.5M | plural, angelini ventures, localglobe | UK | London-based MedTech CoMind has raised $102.5 million (£76.7m) to advance its non-invasive brain monitoring technology aimed at… |
| 6 Nov 2025 | Trogenix | Series A | $88.9M | iq capital, 4bio capital, cancer research horizons | Scotland | Edinburgh Uni spinout Trogenix has completed Series A financing of £70 million in a round led by IQ Capital, alongside returning investors… |
| 22 Apr 2026 | Acuitymd (acuitymd.com) | Series C | $80M | stepstone group, benchmark, redpoint ventures | USA | Funding Details Company: AcuityMD, Inc. Raised: $80.0M Round: Series C Funding Date: April 2026 Lead Investor: StepStone Group Additional… |
| 28 Jan 2026 | ProVerum (proverummedical.com) | — | $74.1M | — | Ireland | ProVerum secured €68.6 million to advance a minimally invasive urology treatment |
| 29 Oct 2025 | Allergy Therapeutics (allergytherapeutics.com) | Warrants exercise | $69.8M | — | UK | Allergy Therapeutics has strengthened its finances after raising £55 million from the exercise of 1.38 billion lender warrants, using the… |
| 14 Aug 2025 | Reprieve Cardiovascular (reprievecardio.com) | Series B | $61M | deerfield management, Rex Health Ventures, arboretum… | USA | Reprieve Cardiovascular, a Milford, MA-based medical device startup, has secured $61 million in Series B financing |
| 31 May 2025 | Salvia Bioelectronics (salviabioelectronics.com) | Series B | $60M | — | Netherlands | Dutch medtech company Salvia BioElectronics has raised $60 million in a Series B funding round to develop its MySalvia Therapy. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 28 Apr 2026 | Luminate Medical (luminatemed.com) | — | $21M | — | Ireland | Galway-based medtech company Luminate Medical, which raised $21m. |
| 28 Apr 2026 | Plaquetec (plaquetec.com) | — | $5M | — | — | PlaqueTec, a medtech company pioneering intracoronary liquid biopsy to identify inflammatory drivers of cardiovascular disease, has raised… |
| 22 Apr 2026 | Acuitymd (acuitymd.com) | Series C | $80M | stepstone group, benchmark, redpoint ventures | USA | Funding Details Company: AcuityMD, Inc. Raised: $80.0M Round: Series C Funding Date: April 2026 Lead Investor: StepStone Group Additional… |
| 16 Apr 2026 | AI DIAGNOSTICS (ai-diagnostics.net) | pre-Series A | $4.6M | steele foundation for hope, iFSP Group, global innovation… | South Africa | A South African medtech company has obtained R85m in funding to develop its AI-driven tool, enhancing the accessibility of TB screening. |
| 15 Apr 2026 | Zelemiq Life Science Limited | seed | $254k | foundercatalyst | United Kingdom | Zelemiq Life Science Limited, the innovator behind the myRipple® metabolic monitoring platform, today announced the successful completion… |
| 8 Apr 2026 | Neuroclues (neuroclues.com) | Series A | $10.8M ⚠ check sentence | InvestBW, LeanSquare, Wallonie Entreprendre | France, Belgium | neuroClues, a French-Belgian MedTech startup, has raised €10 million in a Series A round, along with additional non-dilutive funding,… |
| 31 Mar 2026 | Hepta Medical (heptamed.com) | A-series | $5.4M | ui investissement, supernova invest, bpifrance | France | The French Medtech is closing a second part of its A-series raising, for an additional €5 million, bringing the total envelope to almost… |
| 30 Mar 2026 | Lifebloom (lifebloomcandles.com) | — | $8.6M | private investors, France 2030 | — | The medtech will be in the middle of Lifebloom, and will be financing €8 million to change the scale. Founded in 2019, the company… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector medtech --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector medtech --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector medtech --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "medtech", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "medtech", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Manufacturing Startup Funding](manufacturing-startup-funding.md)
- [Media Startup Funding](media-startup-funding.md)
- [Mental Health Startup Funding](mental-health-startup-funding.md)
- [Travel Startup Funding](travel-startup-funding.md)
