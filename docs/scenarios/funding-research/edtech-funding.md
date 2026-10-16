# Edtech Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “edtech funding” · 40/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [edtech-funding.json](../../examples/scenarios/edtech-funding.json).

**Question.** How many edtech deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “edtech”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 160 |
| With a usable reported amount | 146 |
| Reported total (usable amounts) | $2.2B |
| Median reported round | $3.9M |
| Largest reported round | $741M |
| Busiest month | Sep 2025 (23 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 7 | 5 | $33.2M | $7.6M | ██████ |
| Jun 2025 | 22 | 22 | $152.8M | $100k | ███████████████████ |
| Jul 2025 | 11 | 9 | $53.8M | $2.5M | ██████████ |
| Aug 2025 | 12 | 11 | $47.7M | $3.4M | ██████████ |
| Sep 2025 | 23 | 18 | $980.9M | $10.8M | ████████████████████ |
| Oct 2025 | 9 | 8 | $36.4M | $6M | ████████ |
| Nov 2025 | 14 | 13 | $408.2M | $6.5M | ████████████ |
| Dec 2025 | 12 | 12 | $111.7M | $5M | ██████████ |
| Jan 2026 | 16 | 14 | $254.5M | $8M | ██████████████ |
| Feb 2026 | 14 | 14 | $89.7M | $2.5M | ████████████ |
| Mar 2026 | 12 | 12 | $65.7M | $2.4M | ██████████ |
| Apr 2026 | 8 | 8 | $30.5M | $1.4M | ███████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 15 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 11 Sep 2025 | Eruditus (eruditus.com) | Equity | $741M ⚠ check sentence | prosus, TPG Rise Fund, peak xv partners | — | Eruditus, which has raised a total of $741 million in equity funding from 27 investors including Prosus, TPG Rise Fund, Peak XV Partners… |
| 13 Nov 2025 | Aakash Educational Services (aakash.ac.in) | Debt-to-Equity Conversion | $300M | Ranjan Pai’s family office | India | His family office acquired a 39.6% stake after converting a $300 million debt investment into equity in early 2024. |
| 21 Jan 2026 | Preply (preply.com) | Series D | $137.2M | westcap, Índico Capital Partners | Spain | Preply, a US and Spain-based global language learning marketplace, has announced today the closing of its Series D round, securing €127… |
| 13 Jun 2025 | Knowunity (knowunity.com) | Series B | $48.6M | xange, portfolion, isomer capital | Germany | Knowunity, a Berlin-based learning platform built "by and for students", has raised €27 million in a Series B round to further develop its… |
| 9 Dec 2025 | PenPencil Edu Services | Equity | $48M | Physicswallah | India | According to a stock exchange filing, the edtech company’s board approved the following investments: Rs 399.85 crore in PenPencil Edu… |
| 6 Jun 2025 | Principia (principia.net) | Series A | $34M | valor capital group | Brazil | Principia, an edtech and fintech platform in Brazil, secured $34 million to accelerate its AI-powered academic management software and… |
| 4 Feb 2026 | Bcas (bcasapp.com) | debt | $32.4M | myinvestor | Spain | BCAS, a Madrid-based EdTech startup specialised in flexible education financing, today announced the closing of a new €30 million debt… |
| 18 Mar 2026 | Busright (busright.com) | Venture | $30M | volition capital | — | BusRight, a school bus routing, tracking, and safety platform for student transportation operations, has raised $30M in Venture funding… |
| 15 Jan 2026 | Emversity (emversity.com) | Series A | $30M | premji invest, lightspeed, Z47 | India | Edtech startup Emversity has raised $30 Mn (INR 271 Cr) in a Series A funding round led by Premji Invest, with participation from… |
| 4 Feb 2026 | Ula (ulalaunch.com) | Series B | $28M | Growth Visions Fund, Jordan Capital & Investment Fund,… | Saudi Arabia | has raised $28 million in a Series B funding round led by Growth Visions Fund, with participation from Jordan Capital & Investment Fund… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Elevify | seed | $1.4M | newtopia, GP Investimentos, Lotux.VC | — | With just over a year of operation and a team of just seven people, edtech recently lifted a $1.35 million seed round to accelerate its… |
| 23 Apr 2026 | Gaia Learning (gaialearning.co.uk) | — | $508k | nesta, syndicate of angel investors, gc angels | UK | The Manchester company raised a total of £400k alongside NESTA and a syndicate of angel investors. |
| 22 Apr 2026 | Aits (aits.co.jp) | Pre-Series A | $4M | big capital, Redbrook Fund, Sujeet Kumar | India | AITS Raises $4 Mn in Pre-Series A Round |
| 22 Apr 2026 | Sinai.ai | pre-seed | $1.4M | KAUST Innovation Ventures | Egypt | Sinai.ai announced it has closed a $1.45 million pre‑seed funding round to develop its AI‑native books platform. |
| 18 Apr 2026 | KingdomOfChess | — | $177k | BeyondSeed Angel Fund, Arjun Vaidya, Rakesh Amerneni… | — | KingdomOfChess Edtech Digital Learning Platform B2C $177K - BeyondSeed Angel Fund, Arjun Vaidya (V3 Ventures), Rakesh Amerneni (RevOptic),… |
| 15 Apr 2026 | Gizmo (gizmo-experience.com) | Series A | $22M | shine capital, ada ventures, Seek Investments | UK | Gizmo, a London, UK-based provider of an AI-powered learning platform, raised $22M in Series A funding. The round was led by Shine… |
| 10 Apr 2026 | Kaizen Mentoria | — | $970k | Mercurial Atlantic Investments | Brazil | Kaizen Mentoria raised $970,000 from Mercurial Atlantic Investments. |
| 28 Mar 2026 | Qweebi (qweebi.com) | seed | $500k | inflection point ventures, Jeroen Tas, Arpit Jain | Singapore | has raised $500,000 in a seed funding round led by Inflection Point Ventures (IPV). The round also saw participation from global leaders… |
| 25 Mar 2026 | GAGA Inc. | Pre Series A | $2.5M | phoenix venture partners | Saudi Arabia | Phoenix Venture Partners (PVP) has led the $2.5 million Pre Series A priced equity round in GAGA Inc., the Saudi edtech platform… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector edtech --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector edtech --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector edtech --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "edtech", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "edtech", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Cybersecurity Funding](cybersecurity-funding.md)
- [Deep Tech Funding](deep-tech-funding.md)
- [Web3 Funding](web3-funding.md)
- [Mobility Funding](mobility-funding.md)
