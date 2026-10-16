# Jio News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “jio news” · 49,500/month India · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [jio-news.json](../../examples/scenarios/jio-news.json).

**Question.** What has the news reported about Jio in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `jio.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `jio.com` |
| Headlines, Jan – Apr 2026 (estimate) | 783 |
| Events, May 2025 – Apr 2026 | 136 |
| Most frequent event types | Earnings (70), Announcement (28), IPO (15) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 16% · 0.3% · 84% of 783 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 3 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [NSE IPO: The India opportunity for Rothschild & Co](https://www.fortuneindia.com/markets/ipo/the-india-opportunity-for-rothschild-co/135308) | fortuneindia.com | 5 | positive | — |
| 30 Apr 2026 | ['Potential of Jio IPO in...' What's the outlook for Reliance Industries - BusinessToday](https://www.businesstoday.in/markets/stocks/story/potential-of-jio-ipo-in-whats-the-outlook-for-reliance-industries-528220-2026-04-30) | businesstoday.in | 7 | positive | — |
| 29 Apr 2026 | [Asia Intelligence Brief for Wednesday, April 29, 2026](https://www.riotimesonline.com/asia-pulse-sk-hynix-softbank-china-india-april-2026/) | riotimesonline.com | 8 | positive | IPO |
| 29 Apr 2026 | [Jio IPO News](https://www.newsdrum.in/business/jio-ipo-may-slip-to-h2-fy27-on-geopolitical-risks-creditsight-11777778) | newsdrum.in | 7 | negative | — |
| 29 Apr 2026 | [📱 WhatsApp Introduces In-App Mobile Recharge for Airtel, Jio & Vi — Explained](https://www.indiaherald.com/Technology/Read/994889203/-WhatsApp-Introduces-InApp-Mobile-Recharge-for-Airtel-Jio-Vi-Explained) | indiaherald.com | 6 | positive | — |
| 28 Apr 2026 | [Reliance to invest ₹1.6 lakh crore in mega Vizag data center cluster - TechStory](https://techstory.in/reliance-to-invest-%e2%82%b91-6-lakh-crore-in-mega-vizag-data-centre-cluster/) | techstory.in | 8 | positive | — |
| 28 Apr 2026 | [Zero IPL trophies: Preity Zinta’s Punjab Kings still value ₹1,200 crore in net worth; check where the money…](https://www.livemint.com/news/trends/zero-ipl-trophies-preity-zinta-s-punjab-kings-still-value-1-200-crore-in-net-worth-check-where-the-money-flows-from-11777360331839.html) | livemint.com | 7 | positive | — |
| 28 Apr 2026 | [Jio's quarterly profit jumps 13%, tops 524 million subscribers in March](https://www.telecompaper.com/news/jios-quarterly-profit-jumps-13-tops-524-million-subscribers-in-march--1569276) | telecompaper.com | 8 | positive | Earnings |
| 27 Apr 2026 | [Jio IPO: Mukesh Ambani Gives an Update](https://telecomtalk.info/jio-ipo-mukesh-ambani-gives-an-update/1006828/) | telecomtalk.info | 8 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 70 |
| Announcement | 28 |
| IPO | 15 |
| Key people | 9 |
| New product | 7 |
| Contracts | 2 |
| Capital infusion | 2 |
| M&A | 1 |
| Asset acquisition | 1 |
| Incorporation | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Announcement | IPO | Key people |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1 | 1 | 0 | 0 | 0 | █ |
| Jun 2025 | 6 | 2 | 3 | 0 | 1 | █████ |
| Jul 2025 | 18 | 15 | 1 | 1 | 0 | ██████████████ |
| Aug 2025 | 26 | 8 | 10 | 3 | 0 | ████████████████████ |
| Sep 2025 | 5 | 1 | 0 | 2 | 0 | ████ |
| Oct 2025 | 18 | 12 | 5 | 0 | 0 | ██████████████ |
| Nov 2025 | 6 | 1 | 2 | 2 | 0 | █████ |
| Dec 2025 | 6 | 1 | 1 | 3 | 0 | █████ |
| Jan 2026 | 17 | 14 | 2 | 1 | 0 | █████████████ |
| Feb 2026 | 9 | 2 | 3 | 0 | 2 | ███████ |
| Mar 2026 | 6 | 1 | 0 | 0 | 5 | █████ |
| Apr 2026 | 18 | 12 | 1 | 3 | 1 | ██████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 3 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 28 Apr 2026 | Earnings | India's Jio Platforms posted operating revenue of INR 449.2 billion for its fourth quarter ended 31 March 2026, which represents an increase of 12.6… | [Jio's quarterly profit jumps 13%, tops 524 million subscribers in…](https://www.telecompaper.com/news/jios-quarterly-profit-jumps-13-tops-524-million-subscribers-in-march--1569276) · telecompaper.com |
| 27 Apr 2026 | Earnings | For the year ended March 31, 2026, the company’s net profit increased to Rs 300.53 billion in FY26, from Rs 261.2 billion in FY25. The revenue from… | [Reliance Jio releases financial results for QE and year ended March…](https://tele.net.in/reliance-jio-releases-financial-results-for-qe-and-year-ended-march-31-2026/) · tele.net.in |
| 25 Apr 2026 | Earnings | Jio Platforms reported a 13% year-on-year rise in net profit for the fourth quarter of FY26, reflecting steady growth in its telecom and digital… | [Jio Platforms Q4 Profit Rises 13%, ARPU Growth Remains Limited…](https://techstory.in/jio-platforms-q4-profit-rises-13-arpu-growth-remains-limited-without-tariff-hike/) · techstory.in |
| 25 Apr 2026 | Earnings | Reliance Jio reported a net profit of Rs 7,935 crore in Q4 FY26. | article unavailable |
| 25 Apr 2026 | Earnings | In the January–March quarter, the group’s digital spearhead reported revenue of Rs 44,929 crore, up 12.7 per cent year on year, while profit after… | [Reliance Jio races ahead in FY26 as profit tops Rs 30,000 crore](https://indiantelevision.com/iworld/reliance-jio-races-ahead-in-fy26-as-profit-tops-rs-30000-crore/) · indiantelevision.com |
| 24 Apr 2026 | Earnings | Jio Platforms Ltd, the group’s telecommunications and digital arm, reported revenues of ₹38,259 crore in Q4, up 13% compared to last year. Ebitda… | [Reliance Q4 profit dips 13% as war-hit O2C drags, retail and Jio…](https://www.livemint.com/companies/company-results/reliance-industries-profit-dips-13-as-war-hit-o2c-drags-retail-and-jio-steady-11777040614137.html) · livemint.com |
| 24 Apr 2026 | Earnings | For the March quarter, the entity’s profit after tax (PAT) rose 13% to Rs 7,935 crore, up from Rs 7,022 crore in the same quarter last year. | [Reliance Industries Q4 results: Net profit falls 12.5%; Jio PAT…](https://timesofindia.indiatimes.com/business/india-business/reliance-industries-q4-results-net-profit-falls-12-5-jio-pat-rises-13/articleshow/130497196.cms) · timesofindia.indiatimes.com |
| 24 Apr 2026 | Earnings | For FY26, the company reported 14.7% increase in revenue from operations to ₹1.72 trillion. Its net profit for the full year was at ₹30,053 crore, a… | [Jio Platforms Q4 profit rises 13%, Arpu flat on no tariff hike \|…](https://www.livemint.com/companies/company-results/jio-platforms-q4fy26-results-reliance-jio-infocomm-arpu-growth-telecom-earnings-5g-spectrum-cost-ipo-subscriber-growth-11776999757398.html) · livemint.com |
| 24 Apr 2026 | Earnings | The company posted quarterly revenue of Rs 44,929 crore, up 12.7% year-on-year, while profit after tax rose 13% to Rs 7,935 crore from Rs 7,022… | article unavailable |
| 24 Apr 2026 | Earnings | Jio Platforms posted a 13% increase in profit to ₹7,935 crore in the March quarter. Its revenue from operations during the quarter increased 12.5%… | [Reliance Industries Q4 results 2026 Highlights: RIL Q4 PAT down…](https://www.livemint.com/market/stock-market-news/reliance-q4-results-2026-live-reliance-share-price-reliance-jio-ipo-reliance-retail-dividend-mukesh-ambani-24-april-2026-11777010727214.html) · livemint.com |
| 23 Apr 2026 | Announcement | Hyderabad: Reliance Jio Infocomm Ltd. has further consolidated its position as the premier digital connectivity provider in the Andhra Pradesh and… | article unavailable |
| 23 Apr 2026 | Earnings | reported 4% sequential and 13% year-on-year growth in net profit to ₹7,935 crore during the quarter. Revenue from operations rose 2.7%… | [Reliance Industries Q4 Results 2026 Preview: From O2C, Jio to Retail…](https://www.livemint.com/market/stock-market-news/reliance-industries-q4-results-2026-preview-from-o2c-jio-to-retail-here-s-what-to-expect-from-mukesh-ambani-led-firm-11776937025641.html) · livemint.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company jio.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company jio.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company jio.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company jio.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$PRISM_BUSINESS_API_BASE/v1/business/companies/jio.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "jio.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Nvidia News](nvidia-news.md)
- [TCS News](tcs-news.md)
- [Intel News](intel-news.md)
- [Infosys News](infosys-news.md)
