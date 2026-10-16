# Zomato News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “zomato news” · 27,100/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [zomato-news.json](../../examples/scenarios/zomato-news.json).

**Question.** What has the news reported about Zomato in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `zomato.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `zomato.com` |
| Headlines, Jan – Apr 2026 (estimate) | 892 |
| Events, May 2025 – Apr 2026 | 67 |
| Most frequent event types | Announcement (28), Earnings (22), New product (7) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 24% · 1.1% · 75% of 892 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 5 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Eternal Reports Robust Q4 Revenue Growth](https://www.franchiseindia.com/insights/en/news/eternal-reports-robust-q4-revenue-growth.58811) | franchiseindia.com | 7 | positive | Earnings |
| 30 Apr 2026 | [D-Street pare early losses: Nifty closes below 24,000, Sensex swings 1,000 points intraday](https://www.financialexpress.com/market/sensex-nifty-50-stock-market-today-live-updates-india-us-iran-isreal-war-asia-nikkei-gold-silver-rate-crude-oil-30april2026-4222682/) | financialexpress.com | 8 | negative | — |
| 29 Apr 2026 | [West Asia conflict threatens India’s growth outlook, inflation at risk: Finance Ministry](https://www.financialexpress.com/shorts/business/news/west-asia-conflict-threatens-indias-growth-outlook-inflation-at-risk-finance-ministrynbsp-4222261/) | financialexpress.com | 7 | negative | — |
| 29 Apr 2026 | [Playing to keep playoff hopes alive: Can Hardik Pandya’s Mumbai beat SRH?](https://www.financialexpress.com/shorts/sports/mi-vs-srh-mumbai-indians-playoff-qualification-scenarios-ipl-2026-4222022/) | financialexpress.com | 7 | negative | — |
| 29 Apr 2026 | [Eternal strengthens support for delivery partners as summer sets in](https://businessnewsthisweek.com/business/eternal-strengthens-support-for-delivery-partners-as-summer-sets-in/) | businessnewsthisweek.com | 7 | positive | Announcement |
| 29 Apr 2026 | [Aviation losses to persist in FY27 as outlook turns negative](https://www.financialexpress.com/shorts/airlines-aviation/aviation-losses-to-persist-in-fy27-as-outlook-turns-negative-4222002/) | financialexpress.com | 8 | positive | — |
| 29 Apr 2026 | [PIB fact check labels viral fuel price hike report as fake, urges citizens to verify](https://www.financialexpress.com/shorts/india-news/pib-fact-check-labels-viral-fuel-price-hike-report-as-fake-urges-citizens-to-verify-through-official-sources-4221905/) | financialexpress.com | 8 | negative | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Announcement | 28 |
| Earnings | 22 |
| New product | 7 |
| Key people | 5 |
| Contracts | 3 |
| M&A | 1 |
| Layoffs | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Announcement | Earnings | New product | Key people |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 9 | 4 | 5 | 0 | 0 | ███████████ |
| Jun 2025 | 4 | 1 | 1 | 2 | 0 | █████ |
| Jul 2025 | 7 | 1 | 5 | 0 | 1 | █████████ |
| Aug 2025 | 4 | 3 | 1 | 0 | 0 | █████ |
| Sep 2025 | 1 | 1 | 0 | 0 | 0 | █ |
| Oct 2025 | 3 | 0 | 3 | 0 | 0 | ████ |
| Nov 2025 | 2 | 0 | 1 | 0 | 1 | ██ |
| Dec 2025 | 16 | 15 | 0 | 1 | 0 | ████████████████████ |
| Jan 2026 | 9 | 1 | 2 | 0 | 2 | ███████████ |
| Feb 2026 | 3 | 0 | 1 | 2 | 0 | ████ |
| Mar 2026 | 4 | 2 | 0 | 1 | 1 | █████ |
| Apr 2026 | 5 | 0 | 3 | 1 | 0 | ██████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 5 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 29 Apr 2026 | New product | Zomato has introduced a new worker-focused initiative aimed at protecting its delivery partners from extreme weather conditions. | [Zomato Launches Cooling Vests For Delivery Partners To Combat…](https://www.newsmobile.in/nation/zomato-launches-cooling-vests-for-delivery-partners-to-combat-extreme-heat/) · newsmobile.in |
| 28 Apr 2026 | Earnings | food delivery business, Zomato, delivered an adjusted Ebitda margin of 5.5% of net order value, translating to an absolute profit of Rs 532 crore… | article unavailable |
| 28 Apr 2026 | Earnings | The Italian has been a profit of Rs 174 crore in the fourth quarter (March 2026 quarter). | [Zomato वाली कंपनी का मुनाफा 346% बढ़ा, 292% चढ़ गए हैं कंपनी के शेयर](https://www.livehindustan.com/business/zomato-parent-company-eternal-profit-soared-346-percent-company-share-jumped-292-percent-in-3-year-201777375528886.html) · livehindustan.com |
| 28 Apr 2026 | Earnings | Zomato’s operating revenue grew 33% YoY and 2% QoQ to ₹2,737 Cr. | [Eternal Q4: Profit Surges 4.5X YoY To ₹174 Cr](https://inc42.com/buzz/eternal-q4-profit-surges-4-5x-yoy-to-%e2%82%b9174-cr/) · inc42.com |
| 7 Apr 2026 | M&A | On June 24, Zomato announced a plan to buy Blinkit for $568 million. | article unavailable |
| 25 Mar 2026 | Announcement | First used in-house for Zomato’s own customer service needs, Nugget was scaled into a centralized platform and launched as an enterprise offering in… | [Zomato Cuts $11M in Support Costs With MongoDB-Powered AI Platform](https://www.analyticsinsight.net/press-release/zomato-cuts-11m-in-support-costs-with-mongodb-powered-ai-platform) · analyticsinsight.net |
| 23 Mar 2026 | Key people | Zomato Appoints Aditya Mangla as CEO of Its Food Ordering and Delivery Business | [Shamik Basu Appointed as Adobe India VP \| LatestLY](https://www.latestly.com/business/shamik-basu-appointed-as-adobe-india-vp-7364533.html) · latestly.com |
| 20 Mar 2026 | New product | Zomato Healthy Mode: CEO Deepinder Goyal Announces New Feature With Healthy Score for Every Dish. | [Zomato Hikes Platform Fee Again to INR 14.90 as Rapido’s Zero-Fee…](https://www.latestly.com/technology/zomato-hikes-platform-fee-again-to-inr-14-90-as-rapidos-zero-fee-entry-heats-up-food-delivery-war-7361791.html) · latestly.com |
| 8 Mar 2026 | Announcement | The company posted 16.6 per cent year-on-year net order value (NOV) growth at Rs 9,846 crore in the December quarter translating into 21.3 per cent… | [Swiggy, magicpin, Zomato see food delivery regain growth momentum in…](https://www.dailyexcelsior.com/swiggy-magicpin-zomato-see-food-delivery-regain-growth-momentum-in-dec-qtr/) · dailyexcelsior.com |
| 11 Feb 2026 | Earnings | Revenue: In the fiscal year 2023, Zomato's revenue was ₹2,056.00 crore (US$261.4 million). Net loss: In the fiscal year 2023, Zomato's net loss was… | article unavailable |
| 10 Feb 2026 | New product | Zomato has announced a dedicated AI-powered hotline (89200 89200) that makes onboarding as a delivery partner as simple as making a phone call. | article unavailable |
| 10 Feb 2026 | New product | Zomato, India’s food ordering and delivery platform, has announced a dedicated AI-powered hotline (89200 89200) that makes onboarding as a delivery… | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company zomato.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company zomato.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company zomato.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company zomato.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/zomato.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "zomato.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Tata Motors News](tata-motors-news.md)
- [Ola Electric News](ola-electric-news.md)
- [Hdfc Bank News](hdfc-bank-news.md)
- [Oracle News](oracle-news.md)
