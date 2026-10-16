# Spotify News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “spotify news” · 480/month India · 5,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [spotify-news.json](../../examples/scenarios/spotify-news.json).

**Question.** What has the news reported about Spotify in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `spotify.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `spotify.com` |
| Headlines, Jan – Apr 2026 (estimate) | 1,888 |
| Events, May 2025 – Apr 2026 | 73 |
| Most frequent event types | Key people (34), Earnings (29), Lawsuit (3) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 20% · 0.4% · 80% of 1,888 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 3 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Mineral Resources and POSCO execute key formal agreements](https://themarketonline.com.au/mineral-resources-and-posco-execute-key-formal-agreements-2026-05-01/) | themarketonline.com.au | 7 | positive | — |
| 30 Apr 2026 | [Five things to watch as ASX banks enter earnings season](https://themarketonline.com.au/five-things-to-watch-as-asx-banks-enter-earnings-season-2026-05-01/) | themarketonline.com.au | 6 | positive | — |
| 30 Apr 2026 | [Trader or driller? Iran war exposes Big Oil’s transatlantic divide: Bousso - Oil & Gas 360](https://www.oilandgas360.com/trader-or-driller-iran-war-exposes-big-oils-transatlantic-divide-bousso/) | oilandgas360.com | 7 | positive | — |
| 30 Apr 2026 | [Hyundai Motor Group redefines in-vehicle experience with ‘Pleos Connect’ next-generation infotainment system](https://www.cbtnews.com/hmg-redefines-experience-with-pleos-connect/) | cbtnews.com | 6 | positive | New product |
| 30 Apr 2026 | [YCM unveils world-first floating solar canopy on main dock - Monaco Life](https://monacolife.net/ycm-unveils-world-first-floating-solar-canopy-on-main-dock/) | monacolife.net | 7 | positive | — |
| 30 Apr 2026 | [UMG revenues up 8.1% as it prepares to sell 50% of Spotify stake](https://musically.com/2026/04/30/umg-revenues-up-8-1-as-it-prepares-to-sell-50-of-spotify-stake/) | musically.com | 7 | negative | — |
| 30 Apr 2026 | [Amazon beats expectations thanks to strong cloud growth - TechCentral.ie](https://www.techcentral.ie/amazon-beats-expectations-thanks-to-strong-cloud-growth/) | techcentral.ie | 8 | positive | — |
| 30 Apr 2026 | [Iran war stasis brings US inflation expectations back to the boil: Mike Dolan](https://www.zawya.com/en/news/insights/iran-war-stasis-brings-us-inflation-expectations-back-to-the-boil-mike-dolan-imgpwwt3) | zawya.com | 8 | negative | — |
| 30 Apr 2026 | [Why Taylor Swift's groundbreaking record contract is the gift that keeps on giving for other artists](https://www.musicweek.com/talent/read/why-taylor-swift-s-groundbreaking-record-contract-is-the-gift-that-keeps-on-giving-for-other-artists/094041) | musicweek.com | 7 | negative | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Key people | 34 |
| Earnings | 29 |
| Lawsuit | 3 |
| New product | 3 |
| M&A | 1 |
| Contracts | 1 |
| IPO | 1 |
| Buyback | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Key people | Earnings | Lawsuit | New product |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2 | 2 | 0 | 0 | 0 | ██ |
| Jun 2025 | 3 | 0 | 0 | 2 | 1 | ███ |
| Jul 2025 | 9 | 0 | 6 | 1 | 0 | ██████████ |
| Aug 2025 | 3 | 0 | 2 | 0 | 0 | ███ |
| Sep 2025 | 18 | 17 | 0 | 0 | 1 | ████████████████████ |
| Oct 2025 | 9 | 6 | 2 | 0 | 0 | ██████████ |
| Nov 2025 | 2 | 0 | 2 | 0 | 0 | ██ |
| Dec 2025 | 3 | 0 | 2 | 0 | 1 | ███ |
| Jan 2026 | 5 | 4 | 1 | 0 | 0 | ██████ |
| Feb 2026 | 13 | 2 | 11 | 0 | 0 | ██████████████ |
| Mar 2026 | 0 | 0 | 0 | 0 | 0 |  |
| Apr 2026 | 6 | 3 | 3 | 0 | 0 | ███████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 5 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 29 Apr 2026 | Earnings | Spotify is forecasting lower profit and slower growth in paying subscribers for the second quarter of 2026 than analysts had expected. | article unavailable |
| 28 Apr 2026 | Earnings | Revenue guidance of €4.8 billion remains broadly in line with forecasts | [Spotify Shares Slide on Weak Q2 Outlook and Slower Subscriber Growth…](https://techeconomy.ng/spotify-q2-2026-forecast-premium-subscriber-slowdown/) · techeconomy.ng |
| 28 Apr 2026 | Earnings | Revenue growth for the quarter accelerated to 8 percent, or 14 percent on a constant currency basis, to get the company to €4.5 billion. Operating… | [Spotify Hits 293 Million Premium Subs and a Profit Record, But Stock…](https://www.hollywoodreporter.com/business/business-news/spotify-q1-earnings-report-subs-stock-drops-outlook-1236578858/) · hollywoodreporter.com |
| 28 Apr 2026 | Key people | Spotify promotes Shipra Srivastava to Head of Marketing | [Deepanjan Roy appointed to senior marketing and sales position at…](http://storyboard18.com/brand-makers/deepanjan-roy-appointed-to-senior-marketing-and-sales-position-at-tata-motors-commercial-vehicles-96495.htm) · storyboard18.com |
| 9 Apr 2026 | Key people | I’m thrilled to share that I’ve been promoted to Head of Marketing (MENA, Türkiye, Pakistan & CIS) at Spotify! Looking forward to this next chapter! | [Spotify elevates Dinesh Kumar Srinivasan to head of marketing](https://www.afaqs.com/people-spotting/spotify-elevates-dinesh-kumar-srinivasan-to-head-of-marketing-11704229) · afaqs.com |
| 9 Apr 2026 | Key people | Dinesh Kumar Srinivasan announced on LinkedIn that he has been promoted to Head of Marketing for MENA, Türkiye, Pakistan, and the CIS at Spotify. | article unavailable |
| 13 Feb 2026 | Earnings | Based on Spotify’s latest earnings release for the quarter ending December 31, the company reported a quarterly revenue of $4.49 billion and a net… | [Barclays Sticks to Their Buy Rating for Spotify (SPOT)](https://markets.businessinsider.com/news/stocks/barclays-sticks-to-their-buy-rating-for-spotify-spot-1035824945) · markets.businessinsider.com |
| 12 Feb 2026 | Earnings | The subscriber growth is coupled with a significant financial performance, with Spotify achieving €2.2 billion (approximately $2.5 billion USD) in… | [Spotify Hits 290M Subscribers & Records Annual Profit in 2025 - News…](https://www.newsdirectory3.com/spotify-hits-290m-subscribers-records-annual-profit-in-2025/) · newsdirectory3.com |
| 11 Feb 2026 | Earnings | The popular music platform closed 2025 with a little over €2.2bn in net profits which represents a 94% increase. | article unavailable |
| 11 Feb 2026 | Earnings | Spotify’s R&D expenses have been falling sharply - down to €290 million in Q4, a 23% decline year-on-year. | article unavailable |
| 11 Feb 2026 | Earnings | Spotify’s earnings call highlighted that for 2025 as a whole, Spotify was a €17.19bn business – $20.5bn at current exchange rates – while reporting… | [Spotify's AI promise: ‘We will not do deals that aren’t good for…](https://musically.com/2026/02/11/spotifys-ai-promise-we-will-not-do-deals-that-arent-good-for-artists/) · musically.com |
| 11 Feb 2026 | Key people | Following Daniel Ek's transition from the CEO role, Spotify Technology S.A. (NYSE:SPOT) says the company hasn't changed direction | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company spotify.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company spotify.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company spotify.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company spotify.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/spotify.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "spotify.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Icici Bank News](icici-bank-news.md)
- [Coinbase News](coinbase-news.md)
- [Bajaj Finance News](bajaj-finance-news.md)
- [Stripe News](stripe-news.md)
