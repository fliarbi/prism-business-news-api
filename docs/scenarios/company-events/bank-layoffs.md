# Bank Layoffs: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “bank layoffs” · 90/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [bank-layoffs.json](../../examples/scenarios/bank-layoffs.json).

**Question.** How many bank layoffs events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `layoffs` and the word “bank” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 82 |
| Companies (with a domain) | 56 |
| Source articles | 77 |
| Busiest month | Sep 2025 (16 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 76% · 0.0% · 24% of 46 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 10 | ████████████ |
| Jun 2025 | 3 | ████ |
| Jul 2025 | 6 | ████████ |
| Aug 2025 | 5 | ██████ |
| Sep 2025 | 16 | ████████████████████ |
| Oct 2025 | 2 | ██ |
| Nov 2025 | 8 | ██████████ |
| Dec 2025 | 3 | ████ |
| Jan 2026 | 6 | ████████ |
| Feb 2026 | 5 | ██████ |
| Mar 2026 | 7 | █████████ |
| Apr 2026 | 11 | ██████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 2 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 27 Apr 2026 | axisbank.com | Layoffs | Axis Bank's total employee strength fell from 1,04,400 at the end of FY25 to 1,01,300 by the close of March 2026, a reduction of over 3,100 people… | [Axis Bank Cuts Over 3,100 Jobs In FY26 As Technology Investments…](https://techstory.in/axis-bank-cuts-over-3100-jobs-in-fy26-as-technology-investments-drive-productivity-gains-across-operations/) · techstory.in |
| 27 Apr 2026 | axisbank.com | Layoffs | Axis Bank has seen a decline in employee headcount for FY26, with its total workforce falling by around 3,000 employees' year-on-year. | [Axis Bank Layoffs: Cuts 3,000 Jobs In FY26 Amid Productivity Gains…](https://www.newsx.com/business/axis-bank-layoffs-cuts-3000-jobs-in-fy26-amid-productivity-gains-from-tech-investments-expands-branch-network-despite-reduced-workforce-206074/) · newsx.com |
| 27 Apr 2026 | axisbank.com | Layoffs | Axis Bank Ltd. has reported a reduction in its total workforce by approximately 3,000 employees for the financial year ended March 31, 2026. | [Axis Bank Layoffs: 3,000 Employees Affected in FY26 Amid Bank’s…](https://www.latestly.com/business/axis-bank-layoffs-3000-employees-affected-in-fy26-amid-banks-digital-transformation-tech-driven-product-gains-7408770.html) · latestly.com |
| 25 Apr 2026 | axisbank.com | Layoffs | Axis Bank's headcount fell to 1.01 lakh in FY26, a reduction of 3,000 roles attributed to technology-driven productivity gains. | [⚡Axis Bank Workforce Optimisation: Tech-Led Strategy Trims Headcount…](https://www.latestly.com/quickly/business/axis-bank-layoffs-axis-banks-employee-headcount-drops-by-3000-in-fy26-as-tech-investments-boost-productivity-7407389.html) · latestly.com |
| 24 Apr 2026 | bank.co.jp | Layoffs | The Bank announced the dismantling of 3900 jobs at the beginning of 2025. | [Medienbericht: Noch mehr Stellenabbau bei der Commerzbank?](https://www.bild.de/politik/medienbericht-noch-ein-stellenabbau-bei-der-commerzbank-69eb2e3826442256f6b586ab) · bild.de |
| 20 Apr 2026 | efirstbank.com | Layoffs | Less than five months after PNC Financial Services Group Inc. (NYSE: PNC) closed its $4.1 billion acquisition of FirstBank Holding Co., the… | article unavailable |
| 15 Apr 2026 | bankofamerica.com | Layoffs | Citigroup with 2,000 and Bank of America with 1,073. | [Wall Street banks cut more than 5,000 jobs even as they notch record…](https://www.businesstimes.com.sg/companies-markets/banking-finance/wall-street-banks-cut-more-5000-jobs-even-they-notch-record-profits) · businesstimes.com.sg |
| 15 Apr 2026 | danskebank.fi | Layoffs | The bank recently announced plans to cut 114 positions while reorganizing teams. | [AI or deindustrialisation? Layoffs surge in Lithuania](https://www.lrt.lt/en/news-in-english/19/2898364/ai-or-deindustrialisation-layoffs-surge-in-lithuania) · lrt.lt |
| 13 Apr 2026 | gocardless.com | Layoffs | The London-based firm, which specialises in bank-to-bank payment solutions, said it had made a redundancy provision for around 90 roles. | [Gocardless to axe 90 jobs as UK fintech eyes profitability](https://www.cityam.com/gocardless-to-axe-90-jobs-as-uk-fintech-eyes-profitability/) · cityam.com |
| 9 Apr 2026 | bendigoadelaide.com.au | Layoffs | In 2025, the bank joined NAB, Bank of Queensland and ANZ in announcing staff redundancies, with it axing 145 technology jobs impacting 637 workers. | [Bank to cut workforce after outsourcing deal](https://www.ntnews.com.au/business/work/leaders-companies/bank-axes-jobs-after-striking-new-multimilliondollar-partnership-deals/news-story/a02a1f7c128b617a7f85b8a789de772d) · ntnews.com.au |
| 3 Apr 2026 | monzo.com | Layoffs | Monzo announced on March 31 that it is closing its US operations. The digital bank will stop onboarding new US customers, lay off approximately 50… | [Monzo Exited the US Three Months After Getting Its European Banking…](https://www.fintechweekly.com/news/digital-bank-european-licence-us-exit-strategy-2026) · fintechweekly.com |
| 30 Mar 2026 | unibiz.com | Layoffs | Additionally, as detailed in the WARN notice, Swiss bank UBS will be laying off 103 employees in Weehawken around June 22 through 24. | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type layoffs --q bank --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type layoffs --q bank --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type layoffs --q bank --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["layoffs"], "q": "bank", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["layoffs"], "q": "bank", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Article filters require a matching source article in the same window; records without a matching article are excluded. Each deal still counts once.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.
- Zero-count periods are included; partial_period marks buckets only partly covered by the window.
- shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)

## Related demonstrations

- [Pharma Layoffs](pharma-layoffs.md)
- [Antitrust Lawsuit](antitrust-lawsuit.md)
- [Tech IPO](tech-ipo.md)
- [Media Layoffs](media-layoffs.md)
