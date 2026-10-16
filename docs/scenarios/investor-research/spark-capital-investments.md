# Spark Capital Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “spark capital investments” · 10/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [spark-capital-investments.json](../../examples/scenarios/spark-capital-investments.json).

**Question.** Which rounds did Spark Capital appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Spark Capital”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 65 |
| With a usable reported amount | 63 |
| Reported total (usable amounts) | $5.5B |
| Median reported round | $55M |
| Largest reported round | $1.4B |
| Busiest month | Mar 2026 (13 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 6 | 6 | $91.4M | $17.5M | █████████ |
| Jun 2025 | 6 | 6 | $605.1M | $14.2M | █████████ |
| Jul 2025 | 0 | 0 | — | — |  |
| Aug 2025 | 9 | 8 | $263M | $61.5M | ██████████████ |
| Sep 2025 | 4 | 4 | $163M | $81.5M | ██████ |
| Oct 2025 | 7 | 7 | $2B | $250M | ███████████ |
| Nov 2025 | 2 | 2 | $106M | $106M | ███ |
| Dec 2025 | 5 | 5 | $281M | $105M | ████████ |
| Jan 2026 | 2 | 2 | $84M | $42M | ███ |
| Feb 2026 | 3 | 3 | $500M | $500M | █████ |
| Mar 2026 | 13 | 12 | $1.3B | $65M | ████████████████████ |
| Apr 2026 | 8 | 8 | $398.8M | $50.5M | ████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 19 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 24 Oct 2025 | Crusoe (crusoe.ai) | Series E | $1.4B ⚠ check sentence | valor equity partners, Mubadala Capital, 137 ventures | USA | Crusoe, the AI factory company, today announced the initial closing of its anticipated $1.375 billion Series E round, bringing the… |
| 24 Mar 2026 | MatX (matx.com) | Series B | $625M | alchip, Andrej Karpathy, Dwarkesh Patel | USA |  |
| 12 Jun 2025 | Cyera (cyera.io) | Series E | $540M | georgian, greenoaks, lightspeed venture partners | — | Cyera, which helps enterprises protect sensitive information while adopting artificial intelligence, has secured $540m in a Series E… |
| 10 Oct 2025 | Kalshi (kalshi.com) | Series D | $300M ⚠ check sentence | sequoia, Andressen Horowitz, capitalg | United States | Kalshi just raised a $300 million Series D round at a $5 billion valuation. |
| 26 Oct 2025 | Sesame (sesamecare.com) | Series B | $250M | sequoia capital, spark capital, other undisclosed VCs | — | Sesame, led by former Oculus executives, secured a $250 million Series B to build AI‑powered smart glasses with an always‑on personal… |
| 2 Apr 2026 | 9fin (9fin.com) | Series C | $170M ⚠ check sentence | harbourvest partners, cpp investments, redalpine | United States | 9fin, an AI-native data and analytics platform focused on debt capital markets, has raised $170 million in a Series C funding round at a… |
| 28 Mar 2026 | Granola (granola.so) | Series C | $125M | index ventures, kleiner perkins, lightspeed venture partners | UK | The London-based startup announced a $125 million Series C on 25 March, led by Danny Rimer at Index Ventures, with Mamoon Hamid at Kleiner… |
| 18 Dec 2025 | Profluent (profluent.com) | financing | $106M | altimeter capital, bezos expeditions, spark capital | United States | Profluent, a leader in frontier AI for protein design, today announced a $106 million financing co-led by Altimeter Capital and Bezos… |
| 3 Dec 2025 | Antithesis (antithesis.com) | Series A | $105M | jane street, Amplify Venture Partners, spark capital | United States | Antithesis, a Northern Virginia startup pitching itself as infrastructure for never-down software, raised a $105 million Series A led by… |
| 30 Sep 2025 | Eve (evehome.com) | Series B | $103M ⚠ check sentence | spark capital, Andreessen Horowitz, lightspeed venture… | United States | On Tuesday, generative artificial intelligence-powered legal tech startup Eve announced that it completed a $103 million series B funding… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Parallel Web Systems | Series B | $10M ⚠ check sentence | sequoia capital, kleiner perkins, index ventures | — | Former Twitter (now X) CEO Parag Agrawal’s AI agentic platform Parallel Web Systems has raised a $100 million Series B at a $2 billion… |
| 16 Apr 2026 | Gambit Security | Seed and Series A | $61M | spark capital, kleiner perkins, cyberstarts | — | Gambit Security, an AI-native enterprise resilience platform, has emerged from stealth with $61m in seed and Series A funding raised in… |
| 14 Apr 2026 | Synera (synera.io) | Series B | $37.8M | revaia, capgemini, uvc partners | Germany | Synera has raised €35 million ($40 million) in a Series B round led by Revaia. |
| 14 Apr 2026 | Synera (synera.io) | Series B | $40M | revaia, Capgemini through ISAI Cap Venture, uvc partners | Germany | Synera, a Bremen, Germany-based provider of a agentic AI platform orchestrating the full industrial engineering value chain, raised $40m… |
| 9 Apr 2026 | Latent (latenthealth.com) | — | $80M ⚠ check sentence | Transformation Capital, spark capital, mckesson ventures | — | Latent Health secured $80 million in total funding from investors including Transformation Capital, Spark Capital, McKesson Ventures,… |
| 2 Apr 2026 | 9fin (9fin.com) | Series C | $170M ⚠ check sentence | harbourvest partners, cpp investments, redalpine | United States | 9fin, an AI-native data and analytics platform focused on debt capital markets, has raised $170 million in a Series C funding round at a… |
| 31 Mar 2026 | 9fin (9fin.com) | Series C | $17M ⚠ check sentence | HarbourVest, cpp investments, redalpine | — | HarbourVest leads round with participation from CPP Investments and earlier investors; total funding raised now exceeds $250 million 9fin,… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "Spark Capital" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "Spark Capital" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "Spark Capital" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Spark Capital", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Spark Capital", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Index Ventures Portfolio](index-ventures-portfolio.md)
- [Redpoint Investments](redpoint-investments.md)
- [Global Founders Capital Investments](global-founders-capital-investments.md)
- [Techstars Portfolio](techstars-portfolio.md)
