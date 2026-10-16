# Drug Approval: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “drug approval” · 90/month India · 110/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [drug-approval.json](../../examples/scenarios/drug-approval.json).

**Question.** How many drug approval events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `fda_approval`, `regulatory` and the word “approval” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 2,347 |
| Companies (with a domain) | 1,614 |
| Source articles | 2,282 |
| Busiest month | Sep 2025 (245 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 12% · 3.9% · 84% of 644 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Regulatory | FDA approval |  |
| --- | ---: | ---: | ---: | --- |
| May 2025 | 161 | 154 | 7 | █████████████ |
| Jun 2025 | 126 | 124 | 2 | ██████████ |
| Jul 2025 | 159 | 152 | 7 | █████████████ |
| Aug 2025 | 217 | 206 | 11 | ██████████████████ |
| Sep 2025 | 245 | 244 | 1 | ████████████████████ |
| Oct 2025 | 193 | 187 | 6 | ████████████████ |
| Nov 2025 | 217 | 208 | 9 | ██████████████████ |
| Dec 2025 | 242 | 235 | 7 | ████████████████████ |
| Jan 2026 | 172 | 165 | 7 | ██████████████ |
| Feb 2026 | 220 | 212 | 8 | ██████████████████ |
| Mar 2026 | 199 | 194 | 5 | ████████████████ |
| Apr 2026 | 196 | 190 | 6 | ████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 8 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | lilly.com | FDA approval | What else you need to know: Eli Lilly’s GLP‑1 business got another tailwind during the quarter with the FDA’s approval of Foundayo, the pill version… | article unavailable |
| 30 Apr 2026 | infiniteitsolutions.net | Regulatory | Infinite IT Solutions, a leading provider of enterprise e-invoicing and automation solutions in the Gulf region, today announced that it has… | article unavailable |
| 29 Apr 2026 | amgen.com | Regulatory | First up, the agency has requested—again—that Amgen remove the autoimmune therapy Tavneos from the market. Specifically, the FDA says that unblinded… | article unavailable |
| 29 Apr 2026 | gbbank.co.uk | Regulatory | Eddie Trahearn, currently Chief Strategy & Financial Officer, subject to regulatory approval. | [GB Bank CEO Mike Says to step down as Eddie Trahearn named successor](https://bridgingloandirectory.co.uk/people/gb-bank-ceo-mike-says-to-step-down-as-eddie-trahearn-named-successor/) · bridgingloandirectory.co.uk |
| 29 Apr 2026 | gbbank.co.uk | Regulatory | He will be succeeded by Eddie Trahearn, currently chief strategy & financial officer – subject to regulatory approval – at the end of April 2026. | article unavailable |
| 29 Apr 2026 | interpolitanmoney.com | Regulatory | Interpolitan Money has received regulatory approval to operate within GIFT City, India, extending its international footprint and adding another… | article unavailable |
| 29 Apr 2026 | alaskaenergymetals.com | Regulatory | The Company announces that, subject to approval of the TSX Venture Exchange, it has further extended the term of its marketing agreement (the… | article unavailable |
| 29 Apr 2026 | jadegas.com.au | Regulatory | Jade Gas Holdings Limited (ASX:JGH) has secured approval from Mongolia’s Mineral Resources and Petroleum Authority for the appraisal report covering… | [Jade Gas (ASX:JGH) advances Mongolia gas licence pathway as TTCBM…](https://business-news-today.com/jade-gas-asxjgh-advances-mongolia-gas-licence-pathway-as-ttcbm-appraisal-wins-regulator-approval/) · business-news-today.com |
| 29 Apr 2026 | fairchildgold.com | Regulatory | Fairchild Gold Corp. (TSXV: FAIR) (FSE: Y4Y) (OTCQB: FCHDF) (“Fairchild” or the “Company“) is pleased to announce, further to its news releases… | article unavailable |
| 29 Apr 2026 | rumble.com | Regulatory | BaFin's approval only confirms that the EU Prospectus meets the standards of completeness, comprehensibility and consistency required by law. | [Rumble, Inc.: Rumble Announces Receipt of all Regulatory Approvals…](https://www.finanznachrichten.de/nachrichten-2026-05/68397175-rumble-inc-rumble-announces-receipt-of-all-regulatory-approvals-for-business-combination-with-northern-data-399.htm) · finanznachrichten.de |
| 29 Apr 2026 | biotalys.com | Regulatory | In April 2026, the company obtained state registration in Florida, marking the first approval of an AGROBODY biocontrol by a US state. | [Biotalys Reports Full-Year 2025 Financial Results and Business…](https://agrigateglobal.com/press-release/biotalys-reports-full-year-2025-financial-results-and-business-highlights/) · agrigateglobal.com |
| 28 Apr 2026 | gotspare.com | Regulatory | Spare has received In-Principle Approval (IPA) from the Central Bank of the UAE (CBUAE) to operate under the country’s Open Finance Regulatory… | [Spare Unveils First Seamless Al Tareq (Open Banking) Powered…](https://ffnews.com/newsarticle/paytech/spare-unveils-first-seamless-al-tareq-open-banking-powered-cross-border-transactions-in-the-gcc/) · ffnews.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type fda_approval --event-type regulatory --q approval --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type fda_approval --event-type regulatory --q approval --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type fda_approval --event-type regulatory --q approval --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["fda_approval", "regulatory"], "q": "approval", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["fda_approval", "regulatory"], "q": "approval", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Media Layoffs](media-layoffs.md)
- [CEO Resigns](ceo-resigns.md)
