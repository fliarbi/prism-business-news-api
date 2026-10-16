# D2C Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “d2c funding” · 30/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [d2c-funding.json](../../examples/scenarios/d2c-funding.json).

**Question.** How many d2c deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “d2c”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 61 |
| With a usable reported amount | 56 |
| Reported total (usable amounts) | $471.1M |
| Median reported round | $4M |
| Largest reported round | $42.6M |
| Busiest month | Apr 2026 (15 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3 | 3 | $7.5M | $720k | ████ |
| Jun 2025 | 2 | 2 | $45.6M | $22.8M | ███ |
| Jul 2025 | 4 | 4 | $20.1M | $980k | █████ |
| Aug 2025 | 3 | 3 | $28M | $540k | ████ |
| Sep 2025 | 5 | 5 | $64.6M | $4M | ███████ |
| Oct 2025 | 3 | 3 | $43.6M | $480k | ████ |
| Nov 2025 | 5 | 5 | $27.6M | $3.3M | ███████ |
| Dec 2025 | 4 | 4 | $54.6M | $13.1M | █████ |
| Jan 2026 | 4 | 3 | $11.6M | $3.9M | █████ |
| Feb 2026 | 6 | 6 | $32.1M | $6M | ████████ |
| Mar 2026 | 7 | 5 | $52.3M | $7.5M | █████████ |
| Apr 2026 | 15 | 13 | $83.4M | $3M | ████████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 6 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 10 Oct 2025 | Fs Life (fslife.co) | Series B | $42.6M | Colossa Ventures, fireside ventures, HirePro Consulting | India | FS Life, the parent company of D2C women’s fashion brand FableStreet, is raising Rs 35.54 crore (around $4 million) led by Colossa… |
| 2 Jun 2025 | Snitch (snitch.co.in) | — | $40.8M | 360 One Asset Management, Ravi modi, SWC Global | India | Snitch, a fast-fashion direct-to-consumer (D2C) menswear brand, has secured ₹340 crore (approximately $40 million) in a combination of… |
| 6 Apr 2026 | Dam Good Fish (damgoodfish.com) | Strategic | $36M ⚠ check sentence | — | India | Dam Good Fish Raises Strategic Funding D2C seafood brand Dam Good Fish raised strategic funding at a valuation of ₹30 crore. |
| 10 Sep 2025 | Asaya (asaya.asia) | pre-Series A | $33.6M | RPSG Capital, OTP Ventures, huddle ventures | India | Asaya raised INR 28 Cr (about $3 Mn) in its pre-Series A round led by RPSG Capital. |
| 19 Aug 2025 | R for Rabbit (rforrabbit.com) | Series B (primary & secondary) | $27M | filter capital, 3one4 capital | India | R for Rabbit, a direct-to-consumer baby products brand, has raised $27 million in a funding round led by Filter Capital and 3one4 Capital. |
| 1 Dec 2025 | Atomberg (atomberg.com) | Series C extension | $25.4M | temasek, co-founders, jungle ventures | India | Atomberg — a consumer‑appliances brand — has raised INR 212 crore (≈ US $24 million) in an extension of its Series C funding round, led by… |
| 4 Sep 2025 | FirstClub | Series A | $23M | — | India | FirstClub raised $23 million in Series A |
| 18 Mar 2026 | Akshayakalpa Organic (akshayakalpa.org) | Series D | $21M | ABC Impact Fund | India | Organic dairy startup Akshayakalpa Organic is raising Rs 175 crore (around $19 million) in its Series D round led by ABC Impact Fund, with… |
| 11 Mar 2026 | Ernesta (ernesta.com) | Series B | $20M | addition | United States | Ernesta – $20M Series B D2C Ernesta, a direct-to-consumer custom rug company, has raised $20M in Series B funding led by Addition. |
| 8 Dec 2025 | Conscious Chemist (consciouschemist.com) | Bridge round | $18M | atomic capital, First Port Capital Fund B, IPV International | India | D2C skincare brand Conscious Chemist has secured INR 15 crore in a bridge round led by Atomic Capital, with participation from First Port… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 28 Apr 2026 | House of Chikankari (houseofchikankari.in) | Series A | $3M | Cap Alpha Ventures | India | House of Chikankari Raises ₹25 Crore Series A |
| 28 Apr 2026 | Hyugalife (hyugalife.com) | Series A | $12M | ivycap ventures, first bridge fund | India | HyugaLife Raises ₹100 Crore Series A |
| 22 Apr 2026 | Chupps (chupps.com) | Pre-Series B | — | Ajinkya Rahane | India | Chupps, India's fast-growing D2C open footwear brand, has announced that Ajinkya Rahane, current captain of Kolkata Knight Riders and… |
| 20 Apr 2026 | Clarity Labs (clarity.cx) | Seed | $480k | Artha Venture Fund II, Angel Investors | India | Clarity Labs Raises INR 4 Cr in Seed Round Outcome-driven functional personal care brand, Clarity Labs, has raised over INR 4 crore in… |
| 17 Apr 2026 | Fifth Sense (fifthsense.org.uk) | Pre-Seed | $756k | OTP Ventures, Sadev Ventures, ISV Capital | India | FIFTH SENSE has secured ₹6.3 crore in a pre-seed funding round led by OTP Ventures, with participation from Sadev Ventures, ISV Capital,… |
| 11 Apr 2026 | Pluckk (pluckk.in) | — | $10.7M | — | India | Pluckk raised $10.74 million. |
| 11 Apr 2026 | Fill & Me | pre‑Seed | $160k | — | India | D2C kids accessories brand Fill & Me raised $160,000 in a pre‑Seed round. |
| 9 Apr 2026 | Pluckk (pluckk.in) | Growth | $12M | Euro Gulf Investment | India | Pluckk Raises ₹100 Crore from Euro Gulf Investment. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector d2c --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector d2c --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector d2c --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "d2c", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "d2c", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Climate Tech Funding](climate-tech-funding.md)
- [Growth Stage Funding](growth-stage-funding.md)
- [Insurtech Funding](insurtech-funding.md)
- [Agritech Funding](agritech-funding.md)
