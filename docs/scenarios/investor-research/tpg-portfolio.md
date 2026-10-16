# TPG Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “tpg portfolio” · 90/month India · 390/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [tpg-portfolio.json](../../examples/scenarios/tpg-portfolio.json).

**Question.** Which rounds did TPG appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “TPG”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 78 |
| With a usable reported amount | 61 |
| Reported total (usable amounts) | $71.2B |
| Median reported round | $375M |
| Largest reported round | $13B |
| Amounts left out as implausible or unconverted | 8 |
| Busiest month | Sep 2025 (17 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2 | 2 | $64.6M | $64.6M | ██ |
| Jun 2025 | 3 | 2 | $415M | $207.5M | ████ |
| Jul 2025 | 3 | 3 | $531.5M | $127M | ████ |
| Aug 2025 | 7 | 6 | $9.8B | $222.2M | ████████ |
| Sep 2025 | 17 | 16 | $14.4B | $150M | ████████████████████ |
| Oct 2025 | 2 | 0 | — | — | ██ |
| Nov 2025 | 8 | 7 | $6.7B | $1B | █████████ |
| Dec 2025 | 1 | 1 | $266M | $266M | █ |
| Jan 2026 | 6 | 4 | $12.8B | $328M | ███████ |
| Feb 2026 | 6 | 5 | $2.5B | $450M | ███████ |
| Mar 2026 | 9 | 8 | $14.8B | $350M | ███████████ |
| Apr 2026 | 14 | 7 | $13B | $2.1B | ████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 15 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 3 Sep 2025 | Anthropic (anthropic.com) | F-series | $13B | iconiq, Fidelity Management & Research Company, lightspeed… | — | It finally attracted $13 billion. |
| 6 Jan 2026 | Jackson Financial | credit line | $12B | tpg | — | The asset manager's TPG credit line will initially invest at least $12 billion on behalf of life insurer Jackson Financial, with a… |
| 30 Mar 2026 | Openai (openai.com) | — | $10B | altimeter capital, Andreessen Horowitz, coatue | USA | OpenAI - $10.0B |
| 22 Apr 2026 | DeployCo | equity | $4.5B ⚠ check sentence | openai, tpg, bain capital | USA | OpenAI will initially invest $500 million of equity into the joint venture, known internally as DeployCo, which is expected to be valued… |
| 20 Nov 2025 | Hypervault (hypervault.com) | Equity and debt | $2.2B | tcs, TPG Terabyte | India | Tata Consultancy Services (TCS) and private equity group TPG will invest up to ₹18,000 crore in a data centre venture, HyperVault,… |
| 17 Feb 2026 | Connected Infra Group | — | $1B | TPG Peppertree | USA | TPG Peppertree has committed up to $1 billion to Connected Infra Group |
| 28 Nov 2025 | Tata Consultancy Services (tcs.com) | — | $1B | TPG Inc. | India | Tata Consultancy Services secured $1 billion in backing from TPG Inc. to fast-track its data infrastructure goals. |
| 21 Nov 2025 | TCS (tcs-plc.co.uk) | — | $1B | tpg | India | The company has secured $1 billion funding from private equity firm TPG. |
| 11 Sep 2025 | Eruditus (eruditus.com) | Equity | $741M ⚠ check sentence | prosus, TPG Rise Fund, peak xv partners | — | Eruditus, which has raised a total of $741 million in equity funding from 27 investors including Prosus, TPG Rise Fund, Peak XV Partners… |
| 23 Feb 2026 | Everest Infrastructure Partners (everestinfrastructure.com) | Equity | $500M | TPG Peppertree | United States | © Shutterstock Ohio-based TPG Peppertree, an investment firm specializing in digital infrastructure, recently committed $500 million in… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 27 Apr 2026 | Vinted (vinted.com) | primary funding round | — | tpg | Lithuania | In 2024 it brought in fresh investors in a round led by US investment group TPG, valuing it at $5bn. |
| 26 Apr 2026 | Armstrong World Industries (armstrongceilings.com) | Equity Investment | $179M | TPG Capital | USA | But those criteria were canceled when TPG Capital last month bought 12 percent of Armstrong's common stock and the economic interests in… |
| 22 Apr 2026 | DeployCo | — | $4B | tpg, bain capital, advent international | — | additional support from names such as TPG, Bain Capital, Advent International, Brookfield and Goanna Capital, which together should direct… |
| 22 Apr 2026 | DeployCo | — | — ⚠ check sentence | openai, tpg, bain capital | United States | The ChatGPT maker will initially invest $500 million of equity into the joint venture, known internally as DeployCo, which is expected to… |
| 22 Apr 2026 | DeployCo | equity | $4.5B ⚠ check sentence | openai, tpg, bain capital | USA | OpenAI will initially invest $500 million of equity into the joint venture, known internally as DeployCo, which is expected to be valued… |
| 17 Apr 2026 | Zum (ridezum.com) | — | $100M | tpg | USA | Since its 2015 founding, student logistics platform Zum has now raised about $500 million, including a fresh $100 million led by TPG to… |
| 13 Apr 2026 | Allogene Therapeutics (allogene.com) | public offering | $175M | goldman sachs, jefferies, td cowen | United States | Allogene Therapeutics, Inc. (Nasdaq: ALLO ) today announced that it intends to offer and sell, in an underwritten public offering and… |
| 6 Apr 2026 | Openai (openai.com) | — | — ⚠ implausible size | amazon, nvidia, softbank | — | OpenAI has raised USD $122 billion in committed capital, valuing the company at USD $852 billion after the investment. The round was… |
| 6 Apr 2026 | Openai (openai.com) | Private Equity Joint Venture | $4B ⚠ check sentence | tpg, advent international, bain capital | USA | A separate PE joint venture with TPG, Advent International, Bain Capital, and Brookfield Asset Management, valued at roughly $10 billion… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor TPG --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor TPG --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor TPG --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "TPG", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "TPG", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Thrive Capital Portfolio](thrive-capital-portfolio.md)
- [Accel Investments](accel-investments.md)
- [A16Z Portfolio](a16z-portfolio.md)
- [Bessemer Investments](bessemer-investments.md)
