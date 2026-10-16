# Lawsuit: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “lawsuit” · 9,900/month India · 165,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [lawsuit.json](../../examples/scenarios/lawsuit.json).

**Question.** How many lawsuit events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `lawsuit`.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 9,866 |
| Companies (with a domain) | 3,868 |
| Source articles | 5,563 |
| Busiest month | Feb 2026 (1,165 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 85% · 2.6% · 12% of 2,106 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 602 | ██████████ |
| Jun 2025 | 510 | █████████ |
| Jul 2025 | 845 | ███████████████ |
| Aug 2025 | 959 | ████████████████ |
| Sep 2025 | 889 | ███████████████ |
| Oct 2025 | 700 | ████████████ |
| Nov 2025 | 753 | █████████████ |
| Dec 2025 | 735 | █████████████ |
| Jan 2026 | 606 | ██████████ |
| Feb 2026 | 1,165 | ████████████████████ |
| Mar 2026 | 1,037 | ██████████████████ |
| Apr 2026 | 1,065 | ██████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 5 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | stgusa.com | Lawsuit | Minority lenders, including Axos Financial and Siemens Financial Services, challenged the LMT in New York state court. | article unavailable |
| 30 Apr 2026 | investors.axosfinancial.com | Lawsuit | Minority lenders, including Axos Financial and Siemens Financial Services, challenged the LMT in New York state court. | article unavailable |
| 30 Apr 2026 | finance.siemens.com | Lawsuit | Minority lenders, including Axos Financial and Siemens Financial Services, challenged the LMT in New York state court. | article unavailable |
| 30 Apr 2026 | oocl.com | Lawsuit | While the $45.6 million award is substantial, it is significantly lower than the $165 million initially sought by Bed Bath & Beyond. | [OOCL Ordered to Pay Record $45.6m in FMC Ruling Over Pandemic…](https://indiaseatradenews.com/oocl-ordered-to-pay-record-45-6m-in-fmc-ruling-over-pandemic-contract-breaches/) · indiaseatradenews.com |
| 30 Apr 2026 | bedbathandbeyond.com | Lawsuit | While the $45.6 million award is substantial, it is significantly lower than the $165 million initially sought by Bed Bath & Beyond. | [OOCL Ordered to Pay Record $45.6m in FMC Ruling Over Pandemic…](https://indiaseatradenews.com/oocl-ordered-to-pay-record-45-6m-in-fmc-ruling-over-pandemic-contract-breaches/) · indiaseatradenews.com |
| 30 Apr 2026 | gregbrockman.com | Lawsuit | With the trial underway for Elon Musk’s lawsuit against OpenAI CEO Sam Altman and president Greg Brockman, judges and jurors are weighing a central… | [The Real Stakes Behind Elon Musk’s Showdown with Sam Altman](https://observer.com/2026/04/elon-musk-openai-sam-altman-lawsuit-trial/) · observer.com |
| 30 Apr 2026 | jindalpoly.com | Lawsuit | The National Company Law Tribunal’s (NCLT) special bench on Thursday directed listing the class action lawsuit against Jindal Poly Films before the… | [NCLT to hear class action suit against Jindal Poly on May 7](https://www.financialexpress.com/business/news/nclt-to-hear-class-action-suit-against-jindal-poly-on-may-7/4223512/) · financialexpress.com |
| 30 Apr 2026 | continentalserves.com | Lawsuit | Continental shareholders had to decide whether they would agree to a million-dollar settlement in the dispute with ex-managers. | [Dieselskandal abgeschlossen? So haben die Continental-Aktionäre…](https://www.dieharke.de/der-norden/continental-dieselskandal-vergleich-ueber-43-7-millionen-euro-beschlossen-VGV22S3X7JCG5NABSE5UH5YPRM.html) · dieharke.de |
| 30 Apr 2026 | renaultgroup.com | Lawsuit | Renault Group has asked India’s National Company Law Tribunal to approve a reorganization of its local operations | [Renault seeks NCLT approval for India overhaul as it bets on scale…](https://www.storyboard18.com/brand-marketing/renault-seeks-nclt-approval-for-india-overhaul-as-it-bets-on-scale-and-exports-96888.htm) · storyboard18.com |
| 30 Apr 2026 | amazon.com | Lawsuit | The class action lawsuit argued that Amazon did not give those mandatory breaks to hourly employees in Washington state, as required by state law. | article unavailable |
| 30 Apr 2026 | soluxtec.de | Lawsuit | From pv magazine Germany German solar module manufacturer Soluxtec has filed for insolvency proceedings with the Bitburg District Court on Wednesday. | [German solar module maker Soluxtec files for insolvency](https://www.pv-magazine.com/2026/04/30/german-solar-module-maker-soluxtec-files-for-insolvency/) · pv-magazine.com |
| 30 Apr 2026 | vertumotors.com | Lawsuit | Vertu Motors has been notified by its insurers of a successful settlement of the Group’s business interruption insurance claim relating to the… | [Vertu reveals success of its JLR cyber attack insurance claim](https://www.motortrader.com/motor-trader-news/automotive-news/vertu-reveals-success-of-its-jlr-cyber-attack-insurance-claim-30-04-2026) · motortrader.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type lawsuit --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type lawsuit --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type lawsuit --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["lawsuit"], "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["lawsuit"], "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Product Recall](product-recall.md)
- [Layoffs](layoffs.md)
- [Stock Split](stock-split.md)
- [Bonus Issue](bonus-issue.md)
