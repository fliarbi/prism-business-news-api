# NEA Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “nea investments” · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [nea-investments.json](../../examples/scenarios/nea-investments.json).

**Question.** Which rounds did New Enterprise Associates appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “New Enterprise Associates”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 55 |
| With a usable reported amount | 53 |
| Reported total (usable amounts) | $9.3B |
| Median reported round | $77.5M |
| Largest reported round | $4B |
| Busiest month | Sep 2025 (9 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 6 | 6 | $811.5M | $84M | █████████████ |
| Jun 2025 | 4 | 4 | $343M | $93M | █████████ |
| Jul 2025 | 3 | 3 | $173.5M | $47M | ███████ |
| Aug 2025 | 4 | 3 | $335M | $115M | █████████ |
| Sep 2025 | 9 | 9 | $966.8M | $80M | ████████████████████ |
| Oct 2025 | 4 | 4 | $77.6M | $15M | █████████ |
| Nov 2025 | 7 | 7 | $1.6B | $317M | ████████████████ |
| Dec 2025 | 0 | 0 | — | — |  |
| Jan 2026 | 4 | 3 | $4.2B | $2.1B | █████████ |
| Feb 2026 | 4 | 4 | $181.2M | $40M | █████████ |
| Mar 2026 | 6 | 6 | $156.5M | $19M | █████████████ |
| Apr 2026 | 4 | 4 | $430M | $100M | █████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 17 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 16 Jan 2026 | Databricks (databricks.com) | Venture | $4B | Andreessen Horowitz, blackrock, blackstone group | United States | Round: Venture |
| 10 Nov 2025 | Clio (clio.com) | equity | $900M | new enterprise associates, tcv, goldman sachs asset… | Canada | Clio’s equity financing was led by U.S.-based private equity firm New Enterprise Associates, which also led a US$900-million deal in 2024… |
| 7 May 2025 | Wonder (wonder.com) | Series (?) | $600M | new enterprise associates, accel, google ventures | USA | Lore in a LinkedIn post Tuesday said there was participation from major existing shareholders, led by New Enterprise Associates, Accel,… |
| 9 Sep 2025 | Strive Health (strivehealth.com) | Series D | $550M | new enterprise associates, hercules capital, cvs health… | — | Strive Health, which offers an AI-driven kidney care model, has raised $550 million in a Series D funding round, with $300 million secured… |
| 26 Jan 2026 | Synthesia (synthesia.io) | Series E | $200M ⚠ check sentence | google ventures, kleiner perkins, accel | United Kingdom | has raised a $200 million Series E round of funding that brings its valuation to $4 billion — up from $2.1 billion just a year ago. |
| 3 Apr 2026 | Nitra (nitra.com) | — | $187M | Actions Capital, comma capital, hyphen capital | USA | Nitra snags $187 million in funding New York-based Nitra aims to make administrative work easier for healthcare practices. |
| 11 Aug 2025 | Setpoint Medical (setpointmedical.com) | Series D | $140M | elevage medical technologies, ally bridge group, northwell… | USA | SetPoint Medical has secured $140 million in private financing to propel the U.S. launch of its novel neuroimmune therapy for rheumatoid… |
| 11 Jun 2025 | SpliceBio | Series B | $135M | EQT Life Sciences, sanofi ventures, Roche Venture Fund | Spain | Spanish biotechnology startup SpliceBio has raised $135 million in a Series B financing. |
| 17 Nov 2025 | Sakana AI | Series B | $134M | mitsubishi ufj financial group, khosla ventures, new… | Japan | Sakana AI, a Tokyo, Japan–based AI startup, has raised approximately ¥20 billion (USD 135 million) in a Series B funding round. |
| 30 Mar 2026 | Qualified Health | — | $125M | Anthology Fund, cathay innovation, flare capital partners | USA | Qualified Health - $125.0M |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 18 Apr 2026 | Bluefish (bluefishoffice.co.uk) | — | $43M | Amex Ventures, bloomberg beta, crane venture partners | United States | Bluefish has now raised a total of $63M in total equity funding and is backed by Amex Ventures, Bloomberg Beta, Crane Venture Partners,… |
| 18 Apr 2026 | Slash (joinslash.com) | — | $100M | goodwater capital, khosla ventures, new enterprise… | United States | Slash has now raised a total of $160M in total equity funding and is backed by Goodwater Capital, Khosla Ventures, New Enterprise… |
| 17 Apr 2026 | Slash Financial | Series C | $100M | ribbit capital, khosla ventures, goodwater capital | USA | Slash Financial, a US-based business banking platform, has raised USD 100 million in a Series C funding round led by Ribbit Capital, with… |
| 3 Apr 2026 | Nitra (nitra.com) | — | $187M | Actions Capital, comma capital, hyphen capital | USA | Nitra snags $187 million in funding New York-based Nitra aims to make administrative work easier for healthcare practices. |
| 31 Mar 2026 | Qualified Health | Series B | $12.5M | new enterprise associates, Transformation Capital,… | USA | Qualified Health, a public benefit corporation providing a secure enterprise AI platform built for health systems, today announced a $125… |
| 30 Mar 2026 | Qualified Health | — | $125M | Anthology Fund, cathay innovation, flare capital partners | USA | Qualified Health - $125.0M |
| 2 Mar 2026 | Union.ai | — | $19M | Mozilla Ventures, nava ventures, new enterprise associates | USA | Union.ai – $19.0M |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "New Enterprise Associates" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "New Enterprise Associates" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "New Enterprise Associates" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "New Enterprise Associates", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "New Enterprise Associates", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Tiger Global Portfolio](tiger-global-portfolio.md)
- [Founders Fund Portfolio](founders-fund-portfolio.md)
- [Insight Partners Portfolio](insight-partners-portfolio.md)
- [Lightspeed Investments](lightspeed-investments.md)
