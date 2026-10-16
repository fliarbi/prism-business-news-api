# Paypal News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “paypal news” · 880/month India · 5,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [paypal-news.json](../../examples/scenarios/paypal-news.json).

**Question.** What has the news reported about Paypal in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `paypal.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `paypal.com` |
| Headlines, Jan – Apr 2026 (estimate) | 5,083 |
| Events, May 2025 – Apr 2026 | 115 |
| Most frequent event types | Key people (39), Earnings (23), Lawsuit (18) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 43% · 0.8% · 57% of 5,083 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 7 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Antonio Lucio Joins PayPal as CMO Amid Massive Restructure](https://www.adweek.com/commerce/antonio-lucio-joins-paypal-as-cmo-amid-company-wide-restructure/) | adweek.com | 5 | positive | Key people |
| 30 Apr 2026 | [PayPal Creates Dedicated Crypto Division in Major Reorganization Shake-Up](https://www.cryptotimes.io/2026/04/30/paypal-creates-dedicated-crypto-division-in-major-reorganization-shake-up/) | cryptotimes.io | 7 | positive | — |
| 30 Apr 2026 | [The crypto industry is experiencing a K-shaped divergence: VCs reap the benefits, while token holders not…](https://panewslab.com/en/articles/019ddd8e-0654-7718-9290-5f5b602875de) | panewslab.com | 7 | positive | — |
| 30 Apr 2026 | [PayPal Reorganises Leadership and Business Structure, Appoints Frank Keller as President of Checkout…](https://liquidityfinder.com/news/paypal-reorganises-leadership-and-business-structure-appoints-frank-keller-as-president-of-checkout-solutions-a94b8) | liquidityfinder.com | 7 | positive | Key people |
| 30 Apr 2026 | [People Moves: Alyssa Henry, Member of the Board at PayPal](https://www.fintechmagazine.com/news/people-moves-alyssa-henry) | fintechmagazine.com | 5 | positive | Key people |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Key people | 39 |
| Earnings | 23 |
| Lawsuit | 18 |
| New product | 9 |
| M&A | 8 |
| Contracts | 6 |
| Regulatory | 5 |
| Asset acquisition | 2 |
| Job creation | 2 |
| Funding round | 1 |
| Board | 1 |
| Fundraising | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Key people | Earnings | Lawsuit | New product |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2 | 0 | 0 | 0 | 0 | █ |
| Jun 2025 | 3 | 2 | 0 | 0 | 1 | ██ |
| Jul 2025 | 9 | 1 | 4 | 0 | 2 | ██████ |
| Aug 2025 | 1 | 0 | 1 | 0 | 0 | █ |
| Sep 2025 | 6 | 4 | 0 | 0 | 0 | ████ |
| Oct 2025 | 15 | 2 | 8 | 0 | 2 | █████████ |
| Nov 2025 | 10 | 1 | 0 | 0 | 3 | ██████ |
| Dec 2025 | 2 | 0 | 0 | 0 | 0 | █ |
| Jan 2026 | 4 | 0 | 1 | 0 | 0 | ██ |
| Feb 2026 | 32 | 18 | 9 | 0 | 0 | ████████████████████ |
| Mar 2026 | 20 | 7 | 0 | 11 | 1 | ████████████ |
| Apr 2026 | 11 | 4 | 0 | 7 | 0 | ███████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 3 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Key people | PayPal has hired veteran marketing executive Antonio Lucio as chief marketing and corporate affairs officer. | [Antonio Lucio Joins PayPal as CMO Amid Massive Restructure](https://www.adweek.com/commerce/antonio-lucio-joins-paypal-as-cmo-amid-company-wide-restructure/) · adweek.com |
| 30 Apr 2026 | Key people | Anshu Bhardwaj has been appointed Chief AI Transformation & Simplification Officer. | [PayPal Reorganises Leadership and Business Structure, Appoints Frank…](https://liquidityfinder.com/news/paypal-reorganises-leadership-and-business-structure-appoints-frank-keller-as-president-of-checkout-solutions-a94b8) · liquidityfinder.com |
| 30 Apr 2026 | Key people | PayPal has confirmed a significant change to its Board of Directors with the appointment of Alyssa Henry. | [People Moves: Alyssa Henry, Member of the Board at PayPal](https://www.fintechmagazine.com/news/people-moves-alyssa-henry) · fintechmagazine.com |
| 29 Apr 2026 | Key people | Two executives will depart PayPal: Diego Scotti, who served as executive vice president and general manager of the consumer group, and Michelle… | [PayPal Reorganizes in Bid to Revive Growth \| PYMNTS.com](https://www.pymnts.com/personnel/2026/paypal-reorganizes-around-3-business-units/) · pymnts.com |
| 17 Apr 2026 | Lawsuit | An expiry date for a securities collector's suit and the forthcoming quarterly figures force the payment service provider to the defensive. | [PayPal Aktie: Sammelklage und Zahlenfokus](https://www.boerse-express.com/news/articles/paypal-aktie-sammelklage-und-zahlenfokus-893790) · boerse-express.com |
| 14 Apr 2026 | Lawsuit | Bernstein Liebhard LLP announces that a shareholder has filed a securities class action lawsuit on behalf of investors (the “Class”) who purchased… | article unavailable |
| 12 Apr 2026 | Lawsuit | Kessler Topaz Meltzer & Check, LLP informs investors that securities fraud class action lawsuits have been filed against PayPal Holdings, Inc. | [PayPal Holdings, Inc. (PYPL) Class Action Lawsuit Seeks Recovery for…](https://www.prnewswire.com/news-releases/paypal-holdings-inc-pypl-class-action-lawsuit-seeks-recovery-for-investors-april-20-2026-deadline---contact-kessler-topaz-meltzer--check-llp-302739581.html) · prnewswire.com |
| 9 Apr 2026 | Lawsuit | The core of allegations: Management should provide investors with false statements about sales development and growth prospects | [PayPal Aktie: Klagedruck vor Fristablauf](https://www.boerse-express.com/news/articles/paypal-aktie-klagedruck-vor-fristablauf-889835) · boerse-express.com |
| 6 Apr 2026 | Lawsuit | two large law firms recalled an approaching deadline for a class action for alleged securities fraud. | article unavailable |
| 5 Apr 2026 | Lawsuit | plaintiffs accuse PayPal and several executives of having provided false or misleading information on the development of sales and growth prospects… | article unavailable |
| 4 Apr 2026 | Lawsuit | the complaint alleges that the Company and its executives violated federal securities laws by making false and/or misleading statements and/or… | [PYPL SHAREHOLDER ALERT: Faruqi & Faruqi, LLP Reminds PayPal (PYPL)…](http://www.prnewswire.com/news-releases/pypl-shareholder-alert-faruqi--faruqi-llp-reminds-paypal-pypl-investors-of-securities-class-action-deadline-on-april-20-2026-302733414.html) · prnewswire.com |
| 25 Mar 2026 | Key people | Independent Director Ann Sarnoff will succeed McGovern as chair of the Corporate Governance and Nominating Committee of PayPal’s Board following the… | [Alyssa Henry to Join PayPal's Board of Directors; Gail J. McGovern…](https://globalfintechseries.com/banking/digital-payments/alyssa-henry-to-join-paypals-board-of-directors-gail-j-mcgovern-to-retire-from-board/) · globalfintechseries.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company paypal.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company paypal.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company paypal.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company paypal.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/paypal.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "paypal.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.
- Zero-count periods are included; partial_period marks buckets only partly covered by the window.
- shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)

## Related demonstrations

- [Salesforce News](salesforce-news.md)
- [Coal India News](coal-india-news.md)
- [Icici Bank News](icici-bank-news.md)
- [Coinbase News](coinbase-news.md)
