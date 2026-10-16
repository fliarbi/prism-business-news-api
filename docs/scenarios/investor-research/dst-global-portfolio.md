# Dst Global Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “dst global portfolio” · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [dst-global-portfolio.json](../../examples/scenarios/dst-global-portfolio.json).

**Question.** Which rounds did Dst Global appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Dst Global”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 85 |
| With a usable reported amount | 81 |
| Reported total (usable amounts) | $44.6B |
| Median reported round | $100M |
| Largest reported round | $16B |
| Amounts left out as implausible or unconverted | 2 |
| Busiest month | Jan 2026 (15 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 4 | 4 | $996M | $225M | █████ |
| Jun 2025 | 9 | 8 | $1.7B | $140M | ████████████ |
| Jul 2025 | 0 | 0 | — | — |  |
| Aug 2025 | 5 | 5 | $1.2B | $271M | ███████ |
| Sep 2025 | 6 | 6 | $4B | $175M | ████████ |
| Oct 2025 | 6 | 6 | $2.6B | $200M | ████████ |
| Nov 2025 | 4 | 3 | $117.4M | $46.4M | █████ |
| Dec 2025 | 5 | 5 | $578.8M | $64.8M | ███████ |
| Jan 2026 | 15 | 15 | $17.3B | $144.5M | ████████████████████ |
| Feb 2026 | 13 | 13 | $22.1B | $176M | █████████████████ |
| Mar 2026 | 10 | 8 | $17.4B | $500M | █████████████ |
| Apr 2026 | 8 | 8 | $10.1B | $28.5M | ███████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 18 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 27 Mar 2026 | Waymo (waymo.com) | Series D | $16B | alphabet, Andreessen Horowitz, bdt & msd partners | — | Mountain View-based Waymo is a mobility technology company that improves transportation by developing self‑driving solutions for travelers… |
| 24 Apr 2026 | Protect Prometheus | — | $10B | jpmorgan chase, blackrock, dst global | — | Protect Prometheus, AI lab co-led by Jeff Bezos, has reportedly raised $10 billion in fresh funding. |
| 10 Feb 2026 | Databricks (databricks.com) | Series K | $5B ⚠ check sentence | qatar investment authority, Singapore Temasek, Macquarie… | United States | United States data & artificial intelligence (AI) company Databrick has raised $5 billion funding at $134 billion valuation, and with… |
| 9 Oct 2025 | Reflection AI (reflectionai.ca) | Series B | $2B ⚠ check sentence | nvidia, disruptive, b capital | USA | Reflection AI raised a colossal $2 billion in a Series B funding round at an $8 billion valuation. |
| 16 Sep 2025 | Mistral AI (mistral.ai) | Series C | $2B ⚠ check sentence | ASML Holding NV, dst global, Andreessen Horowitz | — | French startup Mistral AI has secured USD 2bn (EUR 1.7bn) in a Series C round, bringing its valuation to USD 13.8bn, the company announced… |
| 27 Aug 2025 | Anysphere (anysphere.inc) | Series C | $900M | thrive capital, Andreessen Horowitz, accel | — | Anysphere, the AI research lab behind AI coding tool Cursor, raised a sizable $900 million Series C round that values the company at… |
| 20 Mar 2026 | Earendil Labs | — | $787M | Dimension Capital, dst global, ince capital | USA | Earendil Labs, an AI-driven biotechnology company advancing next-generation biologics, announced that it has raised $787 million in… |
| 16 Mar 2026 | Quince (quince.com) | — | $500M | iconiq capital, wellington management, dst global | United States | Online retailer Quince has raised $500 million in funding, valuing the company at $10.1 billion. |
| 22 May 2025 | Airwallex (airwallex.com) | Series F | $466M ⚠ check sentence | square peg, blackbird, airtree | Australia | Cross-border payments company Airwallex has completed an enormous $466 million Series F round, bringing its valuation to $9.6 billion… |
| 18 Dec 2025 | Lovable (lovable.it) | Series B | $330M ⚠ check sentence | capitalg, Menlo Ventures' Anthology fund, nventures | Sweden | Lovable has raised $330 million in Series B funding at a $6.6 billion valuation, led by CapitalG and Menlo Ventures' Anthology fund. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 24 Apr 2026 | Protect Prometheus | — | $10B | jpmorgan chase, blackrock, dst global | — | Protect Prometheus, AI lab co-led by Jeff Bezos, has reportedly raised $10 billion in fresh funding. |
| 18 Apr 2026 | Resolve.ai | — | $40M | dst global, salesforce ventures | United States | Resolve.ai has now raised a total of $200M in total equity funding and is backed by DST Global and Salesforce Ventures. |
| 17 Apr 2026 | Haast (haast.io) | Series A | $12M | peak xv partners, DST Global Partners, airtree | United States | Today, Haast, the leading AI-powered enterprise compliance engine, announced it has raised $12 million in Series A funding led by Peak XV… |
| 16 Apr 2026 | Resolve AI (resolve.ai) | Series A Extension | $40M | dst global, salesforce ventures | — | Resolve AI Raises $40M in Series A Extension for Production AI Operations. |
| 10 Apr 2026 | Haast (haast.io) | Series A | $17M | peak xv partners, DST Global Partners, airtree | Australia | Haast has raised $17 million (US$12 million) in a Series A round led by Peak XV Partners, with participation from DST Global Partners,… |
| 27 Mar 2026 | Waymo (waymo.com) | Series D | $16B | alphabet, Andreessen Horowitz, bdt & msd partners | — | Mountain View-based Waymo is a mobility technology company that improves transportation by developing self‑driving solutions for travelers… |
| 24 Mar 2026 | Waymo (waymo.com) | Series D | — ⚠ implausible size | alphabet, Andreessen Horowitz, bdt & msd partners | USA |  |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "Dst Global" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "Dst Global" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "Dst Global" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Dst Global", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Dst Global", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [GIC Portfolio](gic-portfolio.md)
- [Atomico Investments](atomico-investments.md)
- [Lux Capital Portfolio](lux-capital-portfolio.md)
- [Y Combinator Portfolio](y-combinator-portfolio.md)
