# ITC News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “itc news” · 9,900/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [itc-news.json](../../examples/scenarios/itc-news.json).

**Question.** What has the news reported about ITC in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `itcportal.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `itcportal.com` |
| Headlines, Jan – Apr 2026 (estimate) | 1,542 |
| Events, May 2025 – Apr 2026 | 80 |
| Most frequent event types | Earnings (54), Announcement (12), M&A (7) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 28% · 1.0% · 71% of 1,542 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 3 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [How investment trends in US residential solar compare to Europe](https://www.pv-tech.org/how-investment-trends-us-residential-solar-compare-europe/) | pv-tech.org | 6 | positive | — |
| 30 Apr 2026 | [Congress should fix the nuclear investment tax credit](https://www.utilitydive.com/news/congress-should-pass-legislation-to-fix-the-nuclear-investment-tax-credit/818911/) | utilitydive.com | 7 | positive | — |
| 30 Apr 2026 | [LG ES says manufacturing spend puts company on track for 50GWh+ US ESS production target](https://www.energy-storage.news/lg-es-says-manufacturing-spend-puts-company-on-track-for-50gwh-us-ess-production-target/) | energy-storage.news | 8 | positive | — |
| 30 Apr 2026 | [India’s Solar Superpower Moment: Cheap, Scalable, Unstoppable](https://www.saurenergy.com/solar-energy-blog/indias-solar-superpower-moment-cheap-scalable-unstoppable-11780566) | saurenergy.com | 8 | positive | — |
| 30 Apr 2026 | [Breakout stocks to buy or sell: Sumeet Bagadia recommends five shares to buy today — 30 April 2026 \| Stock…](https://www.livemint.com/market/stock-market-news/breakout-stocks-to-buy-or-sell-sumeet-bagadia-recommends-five-shares-to-buy-today-30-april-2026-11777509728462.html) | livemint.com | 6 | positive | — |
| 29 Apr 2026 | [सिगरेट 17% तक महंगी हो सकती है: सोना एक दिन में ₹809 और चांदी ₹241 सस्ती हुई, मई में 12 दिन बंद रहेंगे बैंक](https://www.bhaskar.com/business/news/gold-silver-prices-fall-banks-to-close-may-cigarette-costlier-137818471.html) | bhaskar.com | 6 | negative | — |
| 29 Apr 2026 | [मई में फिर बढ़ेंगे सिगरेट के दाम? खबर आते ही इन 2 शेयरों में तूफानी तेजी](https://www.aajtak.in/business/news/story/cigarette-prices-hike-in-may-itc-godfrey-phillips-share-rise-tutd-dskc-2536814-2026-04-29) | aajtak.in | 6 | negative | — |
| 29 Apr 2026 | [Indian Markets Close Higher Despite Surge In Crude Oil Prices](https://www.newsmobile.in/business/indian-markets-close-higher-despite-surge-in-crude-oil-prices/) | newsmobile.in | 6 | positive | — |
| 29 Apr 2026 | [Sensex rises 609 points as UAE’s OPEC exit spurs crude hopes; rupee hits record low](https://www.thehindubusinessline.com/markets/sensex-rises-609-points-as-uaes-opec-exit-spurs-crude-hopes-rupee-hits-record-low/article70920331.ece) | thehindubusinessline.com | 8 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 54 |
| Announcement | 12 |
| M&A | 7 |
| Key people | 3 |
| Regulatory | 3 |
| Contracts | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Announcement | M&A | Key people |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 17 | 16 | 0 | 1 | 0 | ███████████████████ |
| Jun 2025 | 2 | 0 | 1 | 1 | 0 | ██ |
| Jul 2025 | 0 | 0 | 0 | 0 | 0 |  |
| Aug 2025 | 18 | 16 | 1 | 0 | 0 | ████████████████████ |
| Sep 2025 | 9 | 2 | 2 | 2 | 3 | ██████████ |
| Oct 2025 | 4 | 4 | 0 | 0 | 0 | ████ |
| Nov 2025 | 13 | 5 | 6 | 0 | 0 | ██████████████ |
| Dec 2025 | 1 | 0 | 0 | 0 | 0 | █ |
| Jan 2026 | 10 | 9 | 1 | 0 | 0 | ███████████ |
| Feb 2026 | 5 | 2 | 1 | 2 | 0 | ██████ |
| Mar 2026 | 0 | 0 | 0 | 0 | 0 |  |
| Apr 2026 | 1 | 0 | 0 | 1 | 0 | █ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 6 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 2 Apr 2026 | M&A | ITC announced that the company with effect from today i.e., 1 April 2026 has acquired the right to nominate the majority of the Directors on the… | article unavailable |
| 18 Feb 2026 | Announcement | ITCMAARS, the “phygital” platform floated by ITC, has benefitted 2.2 million farmers and over 2,100 Farmer Producer Organisations (FPOs) across 11… | article unavailable |
| 12 Feb 2026 | M&A | ITC acquired Yogabar for Rs 255 crore | article unavailable |
| 6 Feb 2026 | M&A | ITC has bought into Yoga Bar and acquired 24 Mantra through an earn-out structure. | [From ITC, HUL to Marico: Why big FMCG is paying billions for brands…](https://www.financialexpress.com/business/news/from-itc-hul-to-marico-why-big-fmcg-is-paying-billions-for-brands-youve-only-seen-on-instagram/4133698/) · financialexpress.com |
| 6 Feb 2026 | Earnings | The company posted a net profit of 4,931.19 Crores in its last quarter. | [ITC Share Price Today 6 Feb 2026: Live NSE/BSE Rates, Technical…](https://www.livemint.com/market/market-stats/stocks-itc-share-price-nse-bse-s0003028) · livemint.com |
| 2 Feb 2026 | Earnings | posted a consolidated net profit of ₹5,018 crore, largely unchanged from ₹5,013 crore in the same period last year. Its consolidated revenue from… | article unavailable |
| 30 Jan 2026 | Announcement | ITC is set to debut a collection of premium, freshness-focused packaged foods – ranging from cookies and cakes to chutneys and namkeens – to bridge… | article unavailable |
| 30 Jan 2026 | Earnings | Consolidated gross revenue grew 7.1% YoY to ₹19,200 crore | article unavailable |
| 30 Jan 2026 | Earnings | ITC on Thursday reported a consolidated net profit attributable to owners of ₹4,931.19 crore for the October–December quarter (Q3FY26), marginally… | [Q3 results today: Nestle India, NTPC, SAIL, Ambuja Cements, 153…](https://www.business-standard.com/companies/quarterly-results/q3-results-nestle-india-ntpc-sail-ambuja-cements-153-others-on-jan-30-126013000103_1.html) · business-standard.com |
| 30 Jan 2026 | Earnings | ITC’s revenue from operations rose 7.1 per cent year on year to Rs 21,577.58 crore, compared with Rs 20,140.15 crore in the same quarter last year. | [ITC’s Q3 smoke signals mixed as profit flattens, costs rise](https://indiantelevision.com/mam/itcs-q3-smoke-signals-mixed-as-profit-flattens-costs-rise/) · indiantelevision.com |
| 29 Jan 2026 | Earnings | The company revenue is expected to stand at Rs 18,286 crore in the reporting quarter against Rs 17,053 crore, registering a growth of 7.2 per cent… | [ITC Shares Fall Ahead of Q3 Results, Likely Dividend Announcement;…](https://www.lokmattimes.com/business/itc-shares-fall-ahead-of-q3-results-likely-dividend-announcement-stock-down-22-in-6-months-a475/) · lokmattimes.com |
| 29 Jan 2026 | Earnings | Revenue will probably grow about 6%, but profit might drop by 5–6% because last year's income was high. | [ITC Share Price Falls to Rs. 319 as Q3 Results Loom, Profit Likely…](https://www.analyticsinsight.net/stocks/itc-share-price-falls-to-rs-319-as-q3-results-loom-profit-likely-under-pressure) · analyticsinsight.net |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company itcportal.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company itcportal.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company itcportal.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company itcportal.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/itcportal.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "itcportal.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.
- Zero-count periods are included; partial_period marks buckets only partly covered by the window.
- shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)

## Related demonstrations

- [Samsung News](samsung-news.md)
- [Reliance Industries News](reliance-industries-news.md)
- [Tata Steel News](tata-steel-news.md)
- [Paytm News](paytm-news.md)
