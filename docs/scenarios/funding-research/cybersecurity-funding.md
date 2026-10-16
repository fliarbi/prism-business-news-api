# Cybersecurity Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “cybersecurity funding” · 20/month India · 110/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [cybersecurity-funding.json](../../examples/scenarios/cybersecurity-funding.json).

**Question.** How many cybersecurity deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “cybersecurity”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 516 |
| With a usable reported amount | 455 |
| Reported total (usable amounts) | $24.4B |
| Median reported round | $16.2M |
| Largest reported round | $7.3B |
| Amounts left out as implausible or unconverted | 1 |
| Busiest month | Mar 2026 (55 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 27 | 23 | $558.3M | $14.2M | ██████████ |
| Jun 2025 | 46 | 41 | $2.5B | $20M | █████████████████ |
| Jul 2025 | 45 | 38 | $7.9B | $11M | ████████████████ |
| Aug 2025 | 32 | 30 | $511.2M | $9.2M | ████████████ |
| Sep 2025 | 49 | 47 | $1.8B | $10.5M | ██████████████████ |
| Oct 2025 | 40 | 36 | $542.4M | $8.6M | ███████████████ |
| Nov 2025 | 44 | 38 | $2.6B | $22M | ████████████████ |
| Dec 2025 | 48 | 44 | $2.5B | $16.5M | █████████████████ |
| Jan 2026 | 40 | 37 | $1.2B | $19M | ███████████████ |
| Feb 2026 | 54 | 45 | $2.3B | $24M | ████████████████████ |
| Mar 2026 | 55 | 50 | $2.2B | $35M | ████████████████████ |
| Apr 2026 | 36 | 26 | $1.1B | $28.5M | █████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 19 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 11 Jul 2025 | Island (island.co) | Total funding | $7.3B | — | — | Island, a late-stage startup selling a security-themed enterprise browser, has raised more than $730 million in funding and has partnered… |
| 10 Jun 2025 | Cyberark Software (cyberark.com) | Convertible Senior Notes | $1.2B | — | — | On June 10, 2025, CyberArk Software Ltd. successfully closed a private offering of $1.25 billion in 0.00% Convertible Senior Notes due… |
| 22 Sep 2025 | Netskope (netskope.com) | IPO | $908M | — | USA | The well-received offering brought in $908 million for Netskope, which has posted significant and growing revenue in recent quarters. |
| 22 Feb 2026 | Saviynt (saviynt.com) | growth equity | $700M | kkr, Sixth Street Growth, TenEleven | United States | El Segundo-based cybersecurity firm Saviynt had one of the longest stretches between venture rounds, as it raised $700 million of growth… |
| 17 Dec 2025 | Cyera (cyera.io) | — | $540M ⚠ check sentence | — | Israel | This investment also follows a $540 million funding round in June, which pushed Cyera’s valuation to $6 billion. |
| 7 Feb 2026 | Kiteworks (kiteworks.com) | growth-equity | $450M | insight partners, Sixth Street Growth | — | Kiteworks announced a $450 million growth-equity investment from global software investors Insight Partners and Sixth Street Growth. |
| 5 Dec 2025 | Armis (armis.tech) | late-stage | $435M | — | USA | Armis’s $435M late-stage round reflected strong demand for enterprise security platforms... |
| 30 Jun 2025 | Cato Networks (catonetworks.com) | Series G | $359M | vitruvian partners, ion crossover partners, multiple… | Israel | Israeli cybersecurity startup Cato Networks has raised $359 million in late‑stage funding to expand its global presence. |
| 23 Jan 2026 | Torq (torqlogistics.com) | — | $332M | Merlin Ventures, insight partners, bessemer venture partners | Israel | The round raised $332 million and included participation from Insight Partners, Bessemer Venture Partners, Greenfield Partners, Evolution… |
| 4 Nov 2025 | Chainguard (chainguard.dev) | Venture Round | $280M | general catalyst | USA | Chainguard Raises A $280M Venture Round |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Bug Bounty Switzerland | — | — | deutsche beteiligungs ag | Switzerland | Deutsche Beteiligungs AG invests in Bug Bounty Switzerland and strengthens platform for cybersecurity testing |
| 29 Apr 2026 | Bug Bounty (bugbounty.sa) | Long-Term Investment | — | deutsche beteiligungs ag, Direttissima Growth Partners | Switzerland | Deutsche Beteiligungs AG (DBAG) has acquired a minority stake in Big Bounty Switzerland (BBS) in the form of a Long-Term Investment. |
| 28 Apr 2026 | Escape (escape.tech) | — | $18M | — | — | The startup based in Biarritz has just completed a fundraising exercise of $18 million. |
| 27 Apr 2026 | Daintta (daintta.com) | — | — | ldc | United Kingdom | Daintta is to expand further following a “significant” investment from private equity investor LDC. |
| 27 Apr 2026 | Quointelligence (quointelligence.eu) | Series-A | $7.9M | elevator ventures, BMH Beteiligungs-Managementgesellschaft… | Germany | The Frankfurt-based cybersecurity company QuoIntelligence has completed a Series-A financing round of 7.3 million euros. |
| 24 Apr 2026 | Spectrum Security (spectrum-security.com.ua) | Seed | $19M | techoperators, WhiteRabbit Ventures, Skinos Ventures | — | Spectrum Security raises $19m in seed funding round Spectrum Security, a cybersecurity firm specialising in automated threat detection,… |
| 24 Apr 2026 | Copperhelm | seed | $7M | tlv partners, ToDay Ventures, icon | Israel | Copperhelm, $7 million, Cybersecurity, Israel |
| 24 Apr 2026 | SpartanX | seed | — | — | — | SpartanX announced it has raised seed funding to support development of its AI-native cybersecurity platform. |
| 23 Apr 2026 | Deep Algorithm | Pre-Series A | $19.2M | unicorn india ventures, sb investment | India | Deep Algorithm Raises ₹16 Cr in Pre-Series A Round AI-driven cybersecurity and digital trust company, Deep Algorithms, has raised ₹16… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector cybersecurity --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector cybersecurity --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector cybersecurity --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "cybersecurity", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "cybersecurity", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Venture Debt Funding](venture-debt-funding.md)
- [Robotics Funding](robotics-funding.md)
- [Deep Tech Funding](deep-tech-funding.md)
- [Edtech Funding](edtech-funding.md)
