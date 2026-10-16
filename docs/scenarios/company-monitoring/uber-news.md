# Uber News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “uber news” · 880/month India · 6,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [uber-news.json](../../examples/scenarios/uber-news.json).

**Question.** What has the news reported about Uber in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `uber.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `uber.com` |
| Headlines, Jan – Apr 2026 (estimate) | 811 |
| Events, May 2025 – Apr 2026 | 165 |
| Most frequent event types | Key people (31), New product (29), Announcement (28) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 16% · 1.5% · 82% of 811 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 5 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Rivian Posts Narrower First-Quarter Loss Ahead of R2 Launch - TT](https://www.transporttopics.com/articles/rivian-earnings-q1-2026) | transporttopics.com | 7 | negative | — |
| 30 Apr 2026 | [Kazakhstan at the heart of inDrive’s global push toward a user-driven super-app](https://gulfnews.com/gn-focus/kazakhstan-at-the-heart-of-indrives-global-push-toward-a-user-driven-super-app-1.500524603) | gulfnews.com | 7 | positive | — |
| 29 Apr 2026 | [Chipotle (CMG) Q1 2026 Earnings Transcript \| The Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/04/29/chipotle-cmg-q1-2026-earnings-transcript/) | fool.com | 7 | positive | Earnings |
| 29 Apr 2026 | [The eVTOL Era is Beginning With Uber and Joby Aviation: What Investors Need to Know \| The Motley Fool](https://www.fool.com/investing/2026/04/29/the-evtol-era-is-beginning-with-uber-and-joby-avia/) | fool.com | 7 | positive | — |
| 28 Apr 2026 | [Bill Ackman's Pershing Square USA Fund IPOs Today. What Stocks Will It Hold? \| The Motley Fool](https://www.fool.com/investing/2026/04/28/bill-ackmans-pershing-square-usa-fund-ipos-today-w/) | fool.com | 7 | positive | — |
| 28 Apr 2026 | [Uber Technologies, Inc. $UBER Shares Sold by D.A. Davidson & CO.](https://www.defenseworld.net/2026/04/28/uber-technologies-inc-uber-shares-sold-by-d-a-davidson-co.html) | defenseworld.net | 4 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Key people | 31 |
| New product | 29 |
| Announcement | 28 |
| M&A | 26 |
| Earnings | 17 |
| Contracts | 13 |
| Lawsuit | 7 |
| Regulatory | 7 |
| Capital infusion | 3 |
| IPO | 2 |
| Buyback | 2 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Key people | New product | Announcement | M&A |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 23 | 2 | 5 | 2 | 5 | █████████████ |
| Jun 2025 | 12 | 6 | 1 | 3 | 1 | ███████ |
| Jul 2025 | 11 | 0 | 3 | 2 | 2 | ██████ |
| Aug 2025 | 11 | 1 | 2 | 2 | 0 | ██████ |
| Sep 2025 | 6 | 1 | 2 | 0 | 0 | ███ |
| Oct 2025 | 8 | 2 | 0 | 4 | 1 | █████ |
| Nov 2025 | 11 | 3 | 1 | 2 | 2 | ██████ |
| Dec 2025 | 11 | 0 | 8 | 2 | 0 | ██████ |
| Jan 2026 | 4 | 0 | 1 | 1 | 1 | ██ |
| Feb 2026 | 35 | 10 | 3 | 6 | 5 | ████████████████████ |
| Mar 2026 | 12 | 0 | 1 | 4 | 2 | ███████ |
| Apr 2026 | 21 | 6 | 2 | 0 | 7 | ████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 5 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 28 Apr 2026 | M&A | Uber announced an investment in the French company HysetCo, specializing in taxis and hydrogenated VTC. This is the first acquisition of U.S.… | article unavailable |
| 27 Apr 2026 | Contracts | Ras Al Khaimah Transport Authority (RAKTA) has signed an agreement with Uber to introduce the Uber app in the emirate, strengthening the transport… | [Ras Al Khaimah rides go digital with Uber](https://gulfnews.com/uae/transport/rakta-uber-launch-smart-taxi-booking-in-ras-al-khaimah-1.500521193) · gulfnews.com |
| 17 Apr 2026 | New product | Uber has launched a service that sends a gig worker to your door to collect items you want to return to a retailer, for $5 a pickup. | [Uber will now send a courier to your door to return your shopping…](https://thenextweb.com/news/uber-return-package-doorstep-courier-pickup-eats) · thenextweb.com |
| 17 Apr 2026 | M&A | The US Group has acquired another share package, which corresponds to around 4.5 percent of Delivery Hero, and thus holds a significant share in… | [Uber baut Beteiligung an Delivery Hero aus und setzt auf Kooperation](https://retail-news.de/uber-beteiligung-delivery-hero-strategie/) · retail-news.de |
| 17 Apr 2026 | New product | Uber launched a new feature on Friday that lets customers return purchased items without leaving their home. | [Uber will now pick up your returns from your doorstep \| TechCrunch](https://techcrunch.com/2026/04/17/uber-will-now-pick-up-your-returns-from-your-doorstep/) · techcrunch.com |
| 17 Apr 2026 | M&A | Naspers, through its international investment arm Prosus, has sold a major stake in food delivery giant Delivery Hero to Uber in a deal worth around… | [Naspers Sells R5.2 Billion Delivery Hero Stake to Uber in Major…](https://www.joburgetc.com/business/naspers-sells-delivery-hero-stake-to-uber-r5-2-billion/) · joburgetc.com |
| 17 Apr 2026 | M&A | Prosus has sold a 4.5% stake in its German delivery platform, Delivery Hero, to Uber for R5.2 billion. | article unavailable |
| 17 Apr 2026 | M&A | Dutch technology investor Prosus has agreed to sell a 4.5% stake in Delivery Hero to Uber for about €270 million. | [Prosus To Sell 4.5% Stake In Delivery Hero To Uber \| ESM Magazine](https://www.esmmagazine.com/technology/prosus-to-sell-4-5-stake-in-delivery-hero-to-uber-309886) · esmmagazine.com |
| 17 Apr 2026 | M&A | Uber has acquired 13,582,342 additional shares in Delivery Hero from Prosus, representing approximately 4.5% of the issued capital of Delivery Hero. | article unavailable |
| 17 Apr 2026 | M&A | Uber acquires a share of 4.5 percent of the large action Prosus for around 270 million euros. | [Lieferdienste: Uber kauft offenbar weitere Anteile an Delivery Hero](http://www.handelsblatt.com/unternehmen/dienstleister/lieferdienste-uber-kauft-offenbar-weitere-anteile-an-delivery-hero/100217729.html) · handelsblatt.com |
| 16 Apr 2026 | Lawsuit | Uber filed a petition with the Administrative Council for Economic Defence (Cade) requesting that the body keep the filing of an open investigation… | article unavailable |
| 13 Apr 2026 | Key people | Uber has named Arjun Kalra as head of marketing for India and South Asia. | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company uber.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company uber.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company uber.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company uber.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/uber.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "uber.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Toyota News](toyota-news.md)
- [Lucid News](lucid-news.md)
- [IBM News](ibm-news.md)
- [Airtel News](airtel-news.md)
