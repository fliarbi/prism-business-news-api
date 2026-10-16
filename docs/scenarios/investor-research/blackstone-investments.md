# Blackstone Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “blackstone investments” · 390/month India · 4,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [blackstone-investments.json](../../examples/scenarios/blackstone-investments.json).

**Question.** Which rounds did Blackstone appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Blackstone”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 135 |
| With a usable reported amount | 117 |
| Reported total (usable amounts) | $139.2B |
| Median reported round | $371.5M |
| Largest reported round | $18.2B |
| Amounts left out as implausible or unconverted | 7 |
| Busiest month | Mar 2026 (22 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 7 | 5 | $3.9B | $200M | ██████ |
| Jun 2025 | 8 | 7 | $5.9B | $342.7M | ███████ |
| Jul 2025 | 9 | 7 | $245.4M | $25M | ████████ |
| Aug 2025 | 4 | 3 | $9.3B | $4.7B | ████ |
| Sep 2025 | 13 | 11 | $31.1B | $2.5B | ████████████ |
| Oct 2025 | 7 | 7 | $3.2B | $634.3M | ██████ |
| Nov 2025 | 7 | 7 | $1.5B | $275M | ██████ |
| Dec 2025 | 8 | 8 | $4.7B | $119M | ███████ |
| Jan 2026 | 11 | 8 | $5B | $200M | ██████████ |
| Feb 2026 | 20 | 19 | $43.6B | $1B | ██████████████████ |
| Mar 2026 | 22 | 21 | $14.6B | $550M | ████████████████████ |
| Apr 2026 | 19 | 14 | $32.2B | $1B | █████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 23 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 11 Feb 2026 | Anthropic (anthropic.com) | — | $18.2B | blackstone, Coatue Management, Singapore’s GIC | — | The asset manager is planning to invest some $200m in Anthropic’s current round, which values the start-up at $350bn, the news service… |
| 2 Apr 2026 | Related Digital (relateddigital.com) | Financing | $16B | blackstone, bank of america | United States | Related Digital – Related Cos.’ new data center arm – has lined up a $16B financing deal for a massive data center in Saline Township,… |
| 9 Feb 2026 | Firmus Technologies | debt financing | $10B | blackstone, coatue | Australia | Australian artificial intelligence infrastructure company Firmus Technologies has secured a February 9, 2026 commitment for $10 billion in… |
| 10 Apr 2026 | Coreweave (coreweave.com) | Debt facility | $8.5B | mufg, morgan stanley, goldman sachs | United States | CoreWeave today announced it has closed an $8.5 billion delayed draw term loan facility (“DDTL 4.0 Facility”), supporting the continued… |
| 4 Aug 2025 | Openai (openai.com) | Private Funding Round (Late-stage) | $8.3B ⚠ check sentence | dragoneer investment group, blackstone, tpg | USA | OpenAI has raised a massive $8.3 billion in new funding at a staggering $300 billion valuation. |
| 26 Sep 2025 | Sempra Infrastructure Partners | Equity | $7B | Blackstone Credit and Insurance, kkr, Apollo-managed funds | United States | Funding for phase two is supported by an equity investment led by Blackstone Credit and Insurance, together with an investor consortium… |
| 24 Jun 2025 | Rogers Communications (rogers.com) | Equity investment | $5.2B | blackstone, Blackstone Credit & Insurance, cpp investments | Canada | Blackstone has successfully closed its previously announced CDN$7 billion equity investment in Rogers Communications Inc. |
| 16 Jan 2026 | Databricks (databricks.com) | Venture | $4B | Andreessen Horowitz, blackrock, blackstone group | United States | Round: Venture |
| 1 Sep 2025 | New World Development (nwd.com.hk) | — | $2.5B | blackstone, Cheng family | Hong Kong | Octus reported last month that Blackstone and the Cheng family were considering co-investing about US$2.5 billion in NWD. |
| 7 May 2025 | Dream Games (dreamgames.com) | Strategic equity and debt financing | $2.5B | cvc, blackstone, Other investors | Turkey | Turkey-based mobile games developer Dream Games has announced a strategic equity investment from CVC and debt financing from Blackstone… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 22 Apr 2026 | Anthropic JV | — | $1B | blackstone, hellman & friedman, permira | — | Anthropic is pursuing a parallel joint venture with Blackstone, Hellman & Friedman, and Permira at a smaller scale, approximately $1… |
| 22 Apr 2026 | Factory (factory.com) | Series C | $1.5B ⚠ check sentence | khosla ventures, sequoia capital, blackstone | — | Factory announced it has raised $150 million in a Series C funding round led by Khosla Ventures, with participation from Sequoia Capital,… |
| 20 Apr 2026 | Factory (factory.com) | Series C | $150M | khosla ventures, sequoia capital, blackstone | — | Factory, an autonomous software engineering platform used by enterprises including Nvidia, Adobe and Adyen, raised $150 million in a… |
| 14 Apr 2026 | Firmus (firmus.ai) | private debt financing | $330M | blackstone, coatue | Australia | In November last year, the neocloud said it had raised AU$500m ($351 million) for Project Southgate. |
| 13 Apr 2026 | Pennylane (pennylane.com) | — | $205M | tcv, Blackstone Growth | — | The French accounting software business Pennylane, which targets start-ups and SMEs in Europe, raised $205m in a round led by TCV and… |
| 12 Apr 2026 | Sunotec | — | — | Blackstone Tactical Opportunities | Bulgaria | Linklaters has advised Sunotec, a leading European system integrator of large-scale renewable energy infrastructure, on a partnership… |
| 10 Apr 2026 | Coreweave (coreweave.com) | Debt facility | $8.5B | mufg, morgan stanley, goldman sachs | United States | CoreWeave today announced it has closed an $8.5 billion delayed draw term loan facility (“DDTL 4.0 Facility”), supporting the continued… |
| 8 Apr 2026 | Teva Pharmaceuticals (tevapharm.com) | Strategic funding agreement | $400M | Blackstone Life Sciences | — | Teva Pharmaceuticals ... announced a $400 million strategic funding agreement with Blackstone Life Sciences spread across four years to… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Blackstone --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Blackstone --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Blackstone --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Blackstone", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Blackstone", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [KKR Investments](kkr-investments.md)
- [Mubadala Investments](mubadala-investments.md)
- [Sequoia Investments](sequoia-investments.md)
