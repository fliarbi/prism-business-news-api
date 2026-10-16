# 8vc Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “8vc portfolio” · 10/month India · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [8vc-portfolio.json](../../examples/scenarios/8vc-portfolio.json).

**Question.** Which rounds did 8VC appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “8VC”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 121 |
| With a usable reported amount | 116 |
| Reported total (usable amounts) | $10.5B |
| Median reported round | $40M |
| Largest reported round | $2.6B |
| Busiest month | Sep 2025 (18 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2 | 2 | $230M | $230M | ██ |
| Jun 2025 | 13 | 13 | $585M | $30M | ██████████████ |
| Jul 2025 | 7 | 4 | $90M | $45M | ████████ |
| Aug 2025 | 4 | 4 | $667M | $68.5M | ████ |
| Sep 2025 | 18 | 18 | $1.2B | $40M | ████████████████████ |
| Oct 2025 | 5 | 5 | $173M | $45M | ██████ |
| Nov 2025 | 7 | 7 | $596M | $38M | ████████ |
| Dec 2025 | 8 | 8 | $1.1B | $192.5M | █████████ |
| Jan 2026 | 13 | 13 | $583.3M | $21M | ██████████████ |
| Feb 2026 | 17 | 17 | $1.3B | $77.5M | ███████████████████ |
| Mar 2026 | 17 | 15 | $1.5B | $65M | ███████████████████ |
| Apr 2026 | 10 | 10 | $3B | $65M | ███████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 21 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 6 Apr 2026 | Saronic (saronic.com) | total equity | $2.6B | 8vc, advent international, Andreessen Horowitz | United States | Saronic has now raised a total of $2.6B in total equity funding and is backed by 8VC, Advent International, Andreessen Horowitz, BAM… |
| 14 Nov 2025 | Chaos Industries (getchaos.com) | — | $510M | valor equity partners, 8vc, accel | USA | CHAOS Industries has raised $510 million in new funding to expand development and manufacturing of its sensing and timing technologies for… |
| 16 Mar 2026 | Quince (quince.com) | — | $500M | 8vc, baillie gifford, basis set ventures | USA | Quince – $500.0M |
| 15 Aug 2025 | Cognition (cognition.ai) | — | $500M | Peter Thiel’s Founders Fund, khosla ventures, pear vc | — | Now the Wall Street Journal (WSJ) is reporting that a new round led by Founders Fund sees Cognition raise $500m toward that goal. |
| 24 Mar 2026 | Bedrock Robotics | Series B | $350M | 8vc, C4 Ventures, capitalg | USA |  |
| 16 Jan 2026 | Erebor (erebor.capital) | Venture | $350M | 8vc, founders fund, Haun Ventures | United States | Round: Venture |
| 31 Dec 2025 | Tech and Digital Asset Banking Startup Co-founded By Anduril CEO Palmer Luckey | — | $350M ⚠ check sentence | lux capital, founders fund, Haun Ventures | — | Round: $350 million funding at a $4.35 billion valuation. Investors: Led by Lux Capital with participation from Founders Fund, Haun… |
| 13 May 2025 | Addepar (addepar.com) | Series G | $230M | vitruvian partners, westcap, 8vc | — | Addepar, a leading global technology and data platform that investment professionals rely on to make the most informed, data-driven… |
| 26 Mar 2026 | Emed (emed.com) | — | $200M ⚠ check sentence | AON Consulting, Inc., NFL legend and eMed Founding Chief… | USA | eMed today announced it has raised $200 million in funding at a $2 billion plus valuation. |
| 17 Jun 2025 | Ramp (ramp.network) | Series E | $200M ⚠ check sentence | thrive capital, D1 Capital Partners, general catalyst | USA | Ramp, the leading financial operations platform, announced its Series E financing, bringing its valuation to $16 billion. For the fifth… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 23 Apr 2026 | Rilian | seed | $17.5M | 8vc, first in, tamarack global | United States | Rilian, a McLean, Virginia-based startup building agentic AI systems integration for defence and national security customers, has raised… |
| 20 Apr 2026 | Loop (loopstore.com) | Series C | $95M | valor equity partners, Valor Atreides AI Fund, 8vc | United States | Loop, a San Francisco, CA–based full-stack, verticalized AI platform for logistics and supply chains, has raised $95 million in Series C… |
| 15 Apr 2026 | Alloy Therapeutics (alloytx.com) | Series E | $40M | 8vc, jic venture growth investments, echo capital | USA | Alloy Therapeutics, a biotechnology ecosystem company, announced a $40 million Series E financing round. |
| 9 Apr 2026 | Chapter (askchapter.org) | Series E | $100M | fifth down capital, 8vc, stripes | United States | Chapter Raises $100M Series E Round Back to Home NEW YORK, NY, Chapter, the leading AI company focused on retirement, announced today that… |
| 6 Apr 2026 | Saronic (saronic.com) | total equity | $2.6B | 8vc, advent international, Andreessen Horowitz | United States | Saronic has now raised a total of $2.6B in total equity funding and is backed by 8VC, Advent International, Andreessen Horowitz, BAM… |
| 6 Apr 2026 | Sycamore (sycamore.world) | total equity | $65M | 8vc, Abhinav Gupta, abstract ventures | United States | Sycamore has now raised a total of $65M in total equity funding and is backed by 8VC, Abhinav Gupta, Abstract Ventures, Ali Ghodsi, and… |
| 3 Apr 2026 | Glimpse (tryglimpse.com) | Series A | $35M | Andreessen Horowitz, 8vc, y combinator | — | Glimpse, a NYC-based provider of an AI platform to automate CPG and retail operations, raised $35m in Series A funding. The round, which… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor 8VC --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor 8VC --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor 8VC --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "8VC", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "8VC", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Investor names match broadly (a name can match several firms or funds); use a domain for a narrower match.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Andreessen Horowitz Portfolio](andreessen-horowitz-portfolio.md)
- [Temasek Portfolio](temasek-portfolio.md)
- [Kleiner Perkins Portfolio](kleiner-perkins-portfolio.md)
- [Antler Investments](antler-investments.md)
