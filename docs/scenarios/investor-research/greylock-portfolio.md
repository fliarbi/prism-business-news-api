# Greylock Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “greylock portfolio” · 10/month India · 90/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [greylock-portfolio.json](../../examples/scenarios/greylock-portfolio.json).

**Question.** Which rounds did Greylock appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Greylock”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 64 |
| With a usable reported amount | 61 |
| Reported total (usable amounts) | $4.2B |
| Median reported round | $50M |
| Largest reported round | $750M |
| Busiest month | Jun 2025 (13 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 4 | 4 | $121M | $15M | ██████ |
| Jun 2025 | 13 | 13 | $460.4M | $49.4M | ████████████████████ |
| Jul 2025 | 4 | 4 | $95M | $31M | ██████ |
| Aug 2025 | 7 | 7 | $559.5M | $50M | ███████████ |
| Sep 2025 | 2 | 2 | $275M | $137.5M | ███ |
| Oct 2025 | 5 | 5 | $1.3B | $555M | ████████ |
| Nov 2025 | 11 | 8 | $275M | $60M | █████████████████ |
| Dec 2025 | 2 | 2 | $155M | $77.5M | ███ |
| Jan 2026 | 2 | 2 | $250M | $250M | ███ |
| Feb 2026 | 8 | 8 | $521.8M | $65M | ████████████ |
| Mar 2026 | 3 | 3 | $139M | $45M | █████ |
| Apr 2026 | 3 | 3 | $253.1M | $70M | █████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 20 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 27 Oct 2025 | Wealthsimple (wealthsimple.com) | equity | $750M ⚠ check sentence | dragoneer investment group, gic, canada pension plan… | Canada | Wealthsimple has unveiled an equity round of up to $750 million at a post-money valuation of $10 billion to accelerate the company’s… |
| 26 Jan 2026 | Upwind (upwind.io) | Series B | $250M | bessemer venture partners, salesforce ventures, Picture… | USA | Upwind, a San Francisco startup building a runtime-first cloud security platform, announced a $250 million Series B round. |
| 24 Sep 2025 | Modular (modular.com) | — | $250M | U.S. Innovative Technology Fund, dfj growth, GV | United States | AI startup Modular said on Wednesday it raised $250 million in a funding round valuing it at $1.6 billion. |
| 21 Aug 2025 | Nuro, Inc. | Series E | $203M ⚠ check sentence | uber, baillie gifford, icehouse ventures | — | Nuro, Inc. (“Nuro”), a leader in autonomous driving technology, today announced the closing of a $203M Series E funding round at a $6B… |
| 10 Aug 2025 | Baseten (baseten.co) | Series D | $150M ⚠ check sentence | bond, capitalg, Premji | United States | Baseten, the company powering inference for the world’s fastest-growing AI products, has secured a $150 million Series D fundraise at a… |
| 6 Apr 2026 | Censys (censys.com) | total equity | $143.1M | decibel partners, google ventures, greylock | United States | Censys has now raised a total of $143.1M in total equity funding and is backed by Decibel Partners, Google Ventures, Greylock, Intel… |
| 5 Dec 2025 | 7AI | Series A | $130M | index ventures, blackstone innovations investments, greylock | USA | 7AI, the company whose customers trust dynamic AI agents to get security work done at scale, has announced a US$130 million Series A… |
| 4 Feb 2026 | Resolve AI (resolve.ai) | Series A | $125M ⚠ check sentence | lightspeed venture partners, Greylock Partners, unusual… | United States | Resolve AI, a company developing AI for running and operating software in production, has raised $125 million in a non-blended Series A… |
| 5 Jun 2025 | Snorkel AI (snorkel.ai) | Series D | $100M ⚠ check sentence | addition, Prosperity7 Ventures, Greylock Partners | USA | Snorkel AI, a Redwood City, CA–based AI software startup, raised $100 million in a Series D round at a $1.3 billion valuation. |
| 16 Feb 2026 | Bretton AI | total equity funding | $95.3M | Canvas Prime, greylock, sapphire ventures | — | Bretton AI has now raised a total of $95.3M in total equity funding and is backed by Canvas Prime, Greylock, Sapphire Ventures, Thomson… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 7 Apr 2026 | Censys (censys.com) | Series D | $70M | morgan stanley expansion capital, decibel partners,… | — | Censys, the internet intelligence and insights platform, has raised $70m in a combined funding round to accelerate the development of its… |
| 6 Apr 2026 | Censys (censys.com) | total equity | $143.1M | decibel partners, google ventures, greylock | United States | Censys has now raised a total of $143.1M in total equity funding and is backed by Decibel Partners, Google Ventures, Greylock, Intel… |
| 1 Apr 2026 | Censys (censys.com) | Series D equity | $40M | morgan stanley expansion capital, decibel partners,… | — | The financing includes a $40 million Series D equity round alongside $30 million in debt financing. |
| 13 Mar 2026 | Axiamatic (axiamatic.com) | — | $54M | Greylock Partners, bessemer venture partners | USA | Consequently, the company has emerged from stealth with $54 million in funding from Greylock Partners and Bessemer Venture Partners. |
| 6 Mar 2026 | Cylake | seed | $45M | greylock | USA | Cybersecurity startup Cylake has raised $45 million in seed funding to develop a security platform that runs entirely within customers’… |
| 20 Feb 2026 | Cogent (cogentco.com) | Series A | $42M | bain capital ventures, Greylock Partners, definition | USA | Cogent Security, a cybersecurity company building autonomous AI agents for enterprise vulnerability remediation, has raised new capital… |
| 20 Feb 2026 | Pepper (pepper.me) | Series C | $50M | lead edge capital, iconiq, index ventures | USA | Pepper, the end-to-end technology platform for independent food distributors, announced it has raised $50 million in Series C funding. |
| 19 Feb 2026 | Cogent Security | Series A | $42M ⚠ check sentence | bain capital ventures, greylock, definition | United States | Cogent Security, a San Francisco, CA–based AI-driven vulnerability remediation company, has raised $42 million in a Series A funding… |
| 19 Feb 2026 | Braintrust (usebraintrust.com) | Series B | $80M | iconiq capital, Andreessen Horowitz, greylock | United States | Braintrust, a San Francisco, CA–based technology company focused on AI observability, has raised $80 million in a Series B round. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Greylock --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Greylock --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Greylock --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Greylock", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Greylock", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Kleiner Perkins Portfolio](kleiner-perkins-portfolio.md)
- [Antler Investments](antler-investments.md)
- [Iconiq Portfolio](iconiq-portfolio.md)
- [Blume Ventures Portfolio](blume-ventures-portfolio.md)
