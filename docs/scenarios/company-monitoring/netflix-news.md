# Netflix News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “netflix news” · 2,900/month India · 14,800/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [netflix-news.json](../../examples/scenarios/netflix-news.json).

**Question.** What has the news reported about Netflix in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `netflix.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `netflix.com` |
| Headlines, Jan – Apr 2026 (estimate) | 7,830 |
| Events, May 2025 – Apr 2026 | 360 |
| Most frequent event types | M&A (153), Earnings (56), Regulatory (30) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 28% · 0.8% · 72% of 7,830 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 2 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Netflix, Inc. $NFLX Position Raised by New York State Teachers Retirement System](https://baseballnewssource.com/2026/04/30/netflix-inc-nflx-position-raised-by-new-york-state-teachers-retirement-system/11105093.html) | baseballnewssource.com | 4 | positive | — |
| 30 Apr 2026 | [Chess.com Passes 250 Million Users, Launches Its Ads Gambit](https://www.adweek.com/media/chess-makes-new-advertising-gambit/) | adweek.com | 5 | positive | — |
| 30 Apr 2026 | [Warner Bros. Discovery CEO David Zaslavâs Pay More Than Tripled in 2025 to a Staggering $165 MillionÂ](https://au.variety.com/2026/biz/news/david-zaslav-warner-bros-discovery-compensation-2025-36094/) | au.variety.com | 8 | negative | — |
| 30 Apr 2026 | [Check Point (CHKP) Q1 2026 Earnings Transcript](https://theglobeandmail.com/investing/markets/stocks/CHKP/pressreleases/1632262/check-point-chkp-q1-2026-earnings-transcript/) | theglobeandmail.com | 7 | positive | Earnings |
| 30 Apr 2026 | [David Zaslav's Warner Bros. Discovery Pay Package Skyrocketed In 2025 - SlashFilm](https://www.slashfilm.com/2161269/david-zaslav-2025-warner-bros-discovery-pay-package/) | slashfilm.com | 8 | negative | — |
| 30 Apr 2026 | [Warner Bros. Discovery CEO David Zaslav’s pay package tripled to $165 million in 2025 \| Company Business News](https://www.livemint.com/companies/news/warner-bros-discovery-ceo-david-zaslav-s-pay-package-tripled-to-165-million-in-2025-11777559760988.html) | livemint.com | 8 | positive | — |
| 30 Apr 2026 | [Stock Market Today (LIVE): Markets Close Out April With a Bang; Data Center Surprise Sends QCOM Up 15% \| The…](https://www.fool.com/investing/2026/04/30/stock-market-today-live-coverage/) | fool.com | 7 | negative | Earnings |
| 30 Apr 2026 | [TIME100 Most Influential Companies 2026: Netflix](https://time.com/collection/time100-most-influential-companies/2026/netflix/) | time.com | 8 | positive | — |
| 30 Apr 2026 | [Should You Buy Adobe Stock After the Company's $25 Billion Share Repurchase Announcement?](https://theglobeandmail.com/investing/markets/stocks/ADBE/pressreleases/1610976/should-you-buy-adobe-stock-after-the-companys-25-billion-share-repurchase-announcement/) | theglobeandmail.com | 8 | negative | Buyback |
| 30 Apr 2026 | [Aditya Huria likely to join Netflix India as marketing manager for films & series](https://indiantelevision.com/mam/aditya-huria-likely-to-join-netflix-india-as-marketing-manager-for-films-series/) | indiantelevision.com | 5 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| M&A | 153 |
| Earnings | 56 |
| Regulatory | 30 |
| Asset acquisition | 28 |
| Key people | 22 |
| Lawsuit | 17 |
| Contracts | 16 |
| Announcement | 8 |
| New product | 6 |
| Job creation | 6 |
| Board | 6 |
| Buyback | 6 |
| Capital infusion | 3 |
| Funding round | 2 |
| IPO | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | M&A | Earnings | Regulatory | Asset acquisition |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3 | 0 | 0 | 0 | 0 | █ |
| Jun 2025 | 9 | 0 | 1 | 0 | 0 | █ |
| Jul 2025 | 18 | 0 | 13 | 0 | 0 | ███ |
| Aug 2025 | 4 | 0 | 1 | 0 | 0 | █ |
| Sep 2025 | 6 | 1 | 0 | 0 | 0 | █ |
| Oct 2025 | 21 | 5 | 9 | 1 | 0 | ███ |
| Nov 2025 | 6 | 2 | 0 | 0 | 1 | █ |
| Dec 2025 | 143 | 93 | 0 | 9 | 21 | ████████████████████ |
| Jan 2026 | 39 | 14 | 13 | 4 | 1 | █████ |
| Feb 2026 | 64 | 29 | 2 | 15 | 1 | █████████ |
| Mar 2026 | 10 | 3 | 2 | 0 | 0 | █ |
| Apr 2026 | 37 | 6 | 15 | 1 | 4 | █████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 7 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 27 Apr 2026 | Asset acquisition | Netflix Inc. is in final talks to buy Radford Studio Center in Studio City. | article unavailable |
| 23 Apr 2026 | Asset acquisition | Netflix is in advanced talks to buy the historic Radford Studio Center in Los Angeles, signaling plans to turn the nearly 100‑year‑old lot into its… | [Netflix Eyes Historic Radford Studio Center In Los Angeles As Its…](https://www.ibtimes.com/netflix-eyes-historic-radford-studio-center-los-angeles-its-next-major-production-hub-3801869) · ibtimes.com |
| 23 Apr 2026 | Buyback | The company unveiled the stock buyback program Thursday morning. | [Netflix Sets Big $25 Billion Stock Buyback Amid Lagging Share Price](https://www.hollywoodreporter.com/business/business-news/netflix-sets-new-stock-buyback-program-low-share-price-1236572828/) · hollywoodreporter.com |
| 23 Apr 2026 | Buyback | Netflix announces $25 billion share buyback boost Netflix is ticking up in premarket trading on Thursday after the streaming giant announced plans… | article unavailable |
| 23 Apr 2026 | M&A | Late last year, Warner rebuffed Paramount's overtures to instead strike a $72 billion studio and streaming deal with Netflix. | article unavailable |
| 23 Apr 2026 | Buyback | On April 22, Netflix’s board of directors authorized the repurchase of an additional $25 billion of common stock, without an expiration date | article unavailable |
| 22 Apr 2026 | Earnings | The company reported first-quarter revenue of $12.25 billion last week, beating analyst estimates of $12.18 billion. | [Netflix Eyes TikTok-Style Feed To Capture 'Snackable' Viewing -…](https://benzinga.com/analyst-stock-ratings/analyst-color/26/04/51982094/netflix-eyes-tiktok-style-feed-to-capture-snackable-viewing) · benzinga.com |
| 22 Apr 2026 | Asset acquisition | Netflix is adding to its Los Angeles real estate portfolio with the historic Radford Studio Center lot in Studio City. The streaming giant is in… | article unavailable |
| 22 Apr 2026 | Asset acquisition | Netflix is in talks to buy a Los Angeles-area studio production property at a hefty discount. | article unavailable |
| 21 Apr 2026 | Earnings | For Q2 2026, it projects revenue of $12.5 billion, while analysts were looking for $12.6 billion. The forecast for earnings per share of $0.78 was… | article unavailable |
| 18 Apr 2026 | Earnings | Netflix has set its Q2 2026 guidance at 0.780-0.780 EPS. As a group, analysts predict that Netflix will post 24.58 earnings per share for the… | [Netflix (NASDAQ:NFLX) Issues Q2 2026 Earnings Guidance](https://www.themarketsdaily.com/2026/04/18/netflix-nasdaqnflx-issues-q2-2026-earnings-guidance.html) · themarketsdaily.com |
| 17 Apr 2026 | Earnings | The company’s first-quarter results, released after the close of Thursday trading, beat expectations for revenue and earnings, but its financial… | [Netflix Stock Walloped As Wall Street Questions Its Post-Warner Path](https://deadline.com/2026/04/netflix-stock-drops-wall-street-warner-bros-paramount-1236864310/) · deadline.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company netflix.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company netflix.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company netflix.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company netflix.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/netflix.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "netflix.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Walmart News](walmart-news.md)
- [Rivian News](rivian-news.md)
- [Meta News](meta-news.md)
- [Jpmorgan News](jpmorgan-news.md)
