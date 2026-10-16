# Deep Tech Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “deep tech funding” · 90/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [deep-tech-funding.json](../../examples/scenarios/deep-tech-funding.json).

**Question.** How many deep tech deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “deep tech”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 44 |
| With a usable reported amount | 38 |
| Reported total (usable amounts) | $2.9B |
| Median reported round | $4.5M |
| Largest reported round | $963.4M |
| Busiest month | Mar 2026 (8 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3 | 3 | $35.2M | $6.6M | ████████ |
| Jun 2025 | 1 | 1 | $8.5M | $8.5M | ██ |
| Jul 2025 | 2 | 2 | $4.7M | $2.3M | █████ |
| Aug 2025 | 0 | 0 | — | — |  |
| Sep 2025 | 2 | 2 | $14M | $7M | █████ |
| Oct 2025 | 5 | 4 | $23.5M | $4.4M | ████████████ |
| Nov 2025 | 7 | 7 | $1.8B | $6M | ██████████████████ |
| Dec 2025 | 3 | 3 | $23.6M | $2.8M | ████████ |
| Jan 2026 | 3 | 3 | $7.1M | $2M | ████████ |
| Feb 2026 | 6 | 6 | $979.6M | $6.3M | ███████████████ |
| Mar 2026 | 8 | 6 | $20.5M | $835k | ████████████████████ |
| Apr 2026 | 4 | 1 | $11.3M | $11.3M | ██████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 4 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 13 Feb 2026 | Mundi Ventures (mundiventures.com) | — | $963.4M | — | UK | European investors powered $892 million close for Mundi Ventures’ deep tech growth fund… |
| 5 Nov 2025 | India Deep Tech Alliance (IDTA) | — | $850M | nvidia, qualcomm ventures | India | The India Deep Tech Alliance (IDTA) has secured fresh commitments of over Rs 7,500 crore ($850 million) and expanded its membership with… |
| 11 Nov 2025 | Delvitech (delvitech.tech) | Series B | $40M | EGS Beteiligungen, CREADD Ventures, several European… | Switzerland | Swiss deep tech startup Delvitech has raised $40 million in Series B funding. |
| 26 May 2025 | Tan90 Thermal Solutions | Series A | $24M | blue ashva capital, Capital-A, 3i partners | India | NABVENTURES led a Series A funding round for deep tech startup Tan90 Thermal Solutions, which raised Rs 20 crore ($2.35 million) with… |
| 3 Dec 2025 | SynaXG Technologies | inaugural | $20M | january capital, vertex ventures, qualgro | Singapore | SynaXG Technologies, a deep tech company building wireless infrastructure for the artificial intelligence era, has raised over USD 20… |
| 2 Oct 2025 | Kiutra (kiutra.com) | equity | $14M | Novacapital, 55 north, High-Tech Gründerfonds | Germany | kiutra, the globally leading provider of magnetic cooling for quantum technologies, today announced the successful closing of a €13… |
| 30 Mar 2026 | Empirical Ventures (empiricalventures.vc) | — | $12.7M | british business bank | UK | Empirical Ventures, a UK-based investment group that backs entrepreneurial scientists, has secured a £10m commitment from the British… |
| 17 Apr 2026 | Atomic Tessellator | seed | $11.3M | crane venture partners, in-q-tel, icehouse ventures | New Zealand | Atomic Tessellator has raised $11.3 million in seed funding. |
| 10 Sep 2025 | LeydenJar | Customer funding | $10.8M | Leading US-based consumer electronics company | Netherlands | In parallel, the company secured €10 million in customer funding from a leading US-based consumer electronics company for the development… |
| 13 Jun 2025 | Colugo Systems (colugo-sys.com) | first round | $8.5M ⚠ check sentence | Ayalon Insurance and Finance | Israel | Colugo Systems, which makes electric drones used by the military and in civil operations, raised $8.5 million in its first round. The deal… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 17 Apr 2026 | Atomic Tessellator | seed | $11.3M | crane venture partners, in-q-tel, icehouse ventures | New Zealand | Atomic Tessellator has raised $11.3 million in seed funding. |
| 2 Apr 2026 | Innovinnprom | — | — | european union | Ukraine | The EU is awarding €20 million in funding to 41 cutting‑edge Ukrainian start‑ups and SMEs, following a European Innovation Council call to… |
| 2 Apr 2026 | Farsight Vision | — | — | european union | Ukraine | The EU is awarding €20 million in funding to 41 cutting‑edge Ukrainian start‑ups and SMEs, following a European Innovation Council call to… |
| 2 Apr 2026 | Anotherland | — | — | european union | Ukraine | The EU is awarding €20 million in funding to 41 cutting‑edge Ukrainian start‑ups and SMEs, following a European Innovation Council call to… |
| 30 Mar 2026 | Empirical Ventures (empiricalventures.vc) | — | $12.7M | british business bank | UK | Empirical Ventures, a UK-based investment group that backs entrepreneurial scientists, has secured a £10m commitment from the British… |
| 27 Mar 2026 | Stratificare (stratificare.com) | — | $370k | TIS Inc. | Singapore | Logice, Sembuh AI and StratifiCare each awarded S$500,000 by major Japan IT company TIS Inc., as part of its S$7.6 million commitment to… |
| 27 Mar 2026 | Logice (logiceindonesia.com) | — | $370k | TIS Inc. | Singapore | Logice, Sembuh AI and StratifiCare each awarded S$500,000 by major Japan IT company TIS Inc., as part of its S$7.6 million commitment to… |
| 27 Mar 2026 | Sembuh AI | — | $370k | TIS Inc. | Singapore | Logice, Sembuh AI and StratifiCare each awarded S$500,000 by major Japan IT company TIS Inc., as part of its S$7.6 million commitment to… |
| 20 Mar 2026 | Upsurgeon (upsurgeon.com) | — | $5.4M | simest, Deep Blue Ventures, Deep Ocean Capital Fund | Italy | UpSurgeOn has announced that it has closed a €5 million investment round. |
| 17 Mar 2026 | Cortical Labs (corticallabs.com) | undisclosed investment | — | horizon ventures, 3C, gobi partners | Australia | Cortical Labs , a Melbourne-based deep tech company developing biological computing systems, secured an undisclosed investment in a round… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector "deep tech" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector "deep tech" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector "deep tech" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "deep tech", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "deep tech", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Robotics Funding](robotics-funding.md)
- [Cybersecurity Funding](cybersecurity-funding.md)
- [Edtech Funding](edtech-funding.md)
- [Web3 Funding](web3-funding.md)
