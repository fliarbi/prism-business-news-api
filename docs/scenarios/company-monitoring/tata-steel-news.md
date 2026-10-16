# Tata Steel News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “tata steel news” · 9,900/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [tata-steel-news.json](../../examples/scenarios/tata-steel-news.json).

**Question.** What has the news reported about Tata Steel in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `tatasteel.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `tatasteel.com` |
| Headlines, Jan – Apr 2026 (estimate) | 1,329 |
| Events, May 2025 – Apr 2026 | 247 |
| Most frequent event types | Earnings (78), M&A (47), Contracts (33) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 27% · 0.5% · 72% of 1,329 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 7 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [BT Closing Bell \| Sensex settles 582 pts lower, Nifty below 24,000; Eternal, HUL lead index losers -…](https://www.businesstoday.in/markets/stocks/story/bt-closing-bell-sensex-settles-582-pts-lower-nifty-below-24000-eternal-hul-lead-index-losers-528248-2026-04-30) | businesstoday.in | 7 | negative | — |
| 30 Apr 2026 | [Top Gainers and Losers on April 30: Vedanta, Waaree Energies, Eternal, Adani Energy, Ceat, among top losers…](https://www.livemint.com/market/stock-market-news/top-gainers-and-losers-on-april-30-vedanta-waaree-energies-eternal-adani-energy-ceat-among-top-losers-11777542888922.html) | livemint.com | 6 | negative | — |
| 30 Apr 2026 | [Sensex falls 600 points, investors lose ₹5 lakh crore: What drove the market down? Explained \| Stock Market…](https://www.livemint.com/market/stock-market-news/sensex-plunges-1-000-points-investors-lose-5-lakh-crore-nifty-50-5-key-factors-behind-stock-market-crash-explained-11777521833697.html) | livemint.com | 6 | negative | — |
| 29 Apr 2026 | [Global steelmakers can do much more to green their processes](https://www.eco-business.com/news/global-steelmakers-can-do-much-more-to-green-their-processes/) | eco-business.com | 7 | negative | — |
| 29 Apr 2026 | [India's Quality Leap: IFQM Leads CXO Study Mission to Japan with JUSE](https://www.aninews.in/news/business/indias-quality-leap-ifqm-leads-cxo-study-mission-to-japan-with-juse20260429160355) | aninews.in | 7 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 78 |
| M&A | 47 |
| Contracts | 33 |
| Announcement | 28 |
| Asset acquisition | 20 |
| Lawsuit | 15 |
| Regulatory | 10 |
| Key people | 6 |
| New product | 3 |
| Capital infusion | 3 |
| Job creation | 3 |
| Funding round | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | M&A | Contracts | Announcement |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 21 | 15 | 2 | 3 | 1 | ████████████ |
| Jun 2025 | 9 | 2 | 1 | 1 | 1 | █████ |
| Jul 2025 | 35 | 14 | 4 | 4 | 7 | ████████████████████ |
| Aug 2025 | 24 | 11 | 4 | 3 | 4 | ██████████████ |
| Sep 2025 | 16 | 1 | 1 | 11 | 2 | █████████ |
| Oct 2025 | 12 | 1 | 1 | 2 | 4 | ███████ |
| Nov 2025 | 25 | 13 | 1 | 0 | 2 | ██████████████ |
| Dec 2025 | 30 | 0 | 7 | 3 | 3 | █████████████████ |
| Jan 2026 | 7 | 2 | 2 | 1 | 0 | ████ |
| Feb 2026 | 29 | 18 | 1 | 2 | 0 | █████████████████ |
| Mar 2026 | 20 | 0 | 16 | 0 | 0 | ███████████ |
| Apr 2026 | 19 | 1 | 7 | 3 | 4 | ███████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 3 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 28 Apr 2026 | Key people | Chairman of the Board, Manager, Corporate Sustainability, Rohn Chaudhary has been appointed. | [टाटा स्टील ने मैग्नेट इंडिया बोर्ड का किया गठन](https://www.livehindustan.com/jharkhand/jamshedpur/story-tata-steel-forms-new-magnet-india-board-to-enhance-community-engagement-201777377836128.html) · livehindustan.com |
| 28 Apr 2026 | Lawsuit | the Odisha High Court has effectively quashed demand notices worth nearly ₹4,313 crore related to the company’s Sukinda Chromite Block. | [Tata Steel Share Price Today: Stock Jumps Over 2% To Fresh 52-Week…](https://www.newsx.com/business/tata-steel-share-price-today-stock-jumps-over-2-to-fresh-52-week-high-of-218-as-court-extends-relief-in-4313-cr-mining-dispute-206407/) · newsx.com |
| 28 Apr 2026 | Lawsuit | Tata Steel Ltd scored a legal victory on Tuesday after the Orissa High Court quashed demand notices totalling over ₹4,313 crore raised against the… | article unavailable |
| 28 Apr 2026 | M&A | In 2007, Tata Steel had acquired Anglo-Dutch Steel Manufacturer Company Corus Group PLC in USD 12 billion. | [सन फार्मा ने अमेरिकी कंपनी पर लगाया 11.75 अरब डॉलर का बड़ा दांव](https://www.inextlive.com/sun-pharma-places-a-massive-11-75-billion-bet-on-a-us-company-1777299981) · inextlive.com |
| 22 Apr 2026 | M&A | Tata Steel has executed the share subscription and shareholders’ agreement (SSSA) with Tata Power Renewable Energy (TPREL) and TP Adarsh (TPAL) and… | [Tata Steel inches up on executing share subscription, shareholders’…](https://udaipurkiran.com/tata-steel-inches-up-on-executing-share-subscription-shareholders-pact-with-tprel-tpal/) · udaipurkiran.com |
| 22 Apr 2026 | M&A | Tata Steel has formally completed the acquisition of a 26 percent stake in TP Adarsh Limited by subscribing to 59,00,000 equity shares of face value… | article unavailable |
| 21 Apr 2026 | M&A | Tata Steel has successfully completed the acquisition of a 26% equity stake in TP Adarsh Limited on April 21, 2026, following the execution of a… | [Tata Steel Completes 26% Stake Acquisition in TP Adarsh Limited on…](https://scanx.trade/stock-market-news/companies/tata-steel-completes-acquisition-of-26-stake-in-tp-adarsh-limited-for-5-90-crore/38328211) · scanx.trade |
| 21 Apr 2026 | Contracts | Tata Steel and SMS Group signed a memorandum of understanding to decarbonize the ironmaking process in June 2023. | [Tata Steel partners with SMS Group to deploy world ‘s first EASyMelt…](https://newsriveting.com/tata-steel-partners-with-sms-group-to-deploy-world-s-first-easymelt-technology/) · newsriveting.com |
| 21 Apr 2026 | Contracts | India’s leading steel manufacturer, Tata Steel, has entered into definitive agreements with Paul Wurth, S.A (Luxembourg), part of the SMS Group… | article unavailable |
| 21 Apr 2026 | Announcement | New Delhi: Tata Steel is looking to decarbonize its ironmaking operations in Jamshedpur with a path-breaking technology that hasn’t been used… | [Tata Steel to decarbonize its ironmaking by deploying EASyMelt…](https://helloentrepreneurs.com/business/tata-steel-to-decarbonize-its-ironmaking-by-deploying-easymelt-technology-at-its-jamshedpur-plant-82450/) · helloentrepreneurs.com |
| 13 Apr 2026 | Announcement | At its UK operations, the company is working a £1.25 billion (nearly Rs 16,000 crore) electric arc furnace (EAF) at Port Talbot, and it would have a… | [Tata Steel hits ‘best-ever’ quarterly volumes: Key data points for…](https://www.financialexpress.com/market/stock-insights/tata-steel-hits-best-ever-quarterly-volumes-key-data-points-for-investors/4206256/) · financialexpress.com |
| 13 Apr 2026 | Contracts | The estimated Contract Price under the agreement is Rs. 60 crore net of GST. | [Two dozen stocks including, L&T, NTPC, HUDCO, NBCC, Zaggle,…](https://www.thehindubusinessline.com/markets/two-dozen-stocks-including-lt-ntpc-hudco-nbcc-zaggle-astrazeneca-apollo-hospitals-shalby-tgv-saraf-will-be-in-focus-on-monday/article70854347.ece) · thehindubusinessline.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company tatasteel.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company tatasteel.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company tatasteel.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company tatasteel.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/tatasteel.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "tatasteel.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Reliance Industries News](reliance-industries-news.md)
- [ITC News](itc-news.md)
- [Paytm News](paytm-news.md)
- [General Motors News](general-motors-news.md)
