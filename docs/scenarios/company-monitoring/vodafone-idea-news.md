# Vodafone Idea News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “vodafone idea news” · 110,000/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [vodafone-idea-news.json](../../examples/scenarios/vodafone-idea-news.json).

**Question.** What has the news reported about Vodafone Idea in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `myvi.in`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `myvi.in` |
| Headlines, Jan – Apr 2026 (estimate) | 39 |
| Events, May 2025 – Apr 2026 | 193 |
| Most frequent event types | Earnings (75), Regulatory (40), Lawsuit (30) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 66% · 5.3% · 29% of 39 articles |
| Funding records, Jan – Apr 2026 | 1 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 3 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 23 Apr 2026 | [Vodafone Idea Rolls Out 5G in Panipat, Ambala; Haryana Expansion to Cover Seven Cities by May](https://telecomtalk.info/vodafone-idea-5g-expansion-haryana-panipat-ambala/1006670/) | telecomtalk.info | 7 | positive | Announcement |
| 8 Apr 2026 | [Vi’s TN reboot: 5G rollout, subscriber push and CSK connect](https://www.dtnext.in/news/business/vis-tn-reboot-5g-rollout-subscriber-push-and-csk-connect) | dtnext.in | 7 | positive | Announcement |
| 2 Apr 2026 | [Vodafone Idea adds 21,927 new wireless subscribers in February 2026; shares in focus](https://upstox.com/news/market-news/stocks/vodafone-idea-adds-21-927-new-wireless-subscribers-in-february-2026-shares-in-focus/article-191576/) | upstox.com | 7 | positive | Announcement |
| 14 Mar 2026 | [JSW, ST Telemedia among firms eyeing stake in Vodafone Idea \| M&A Critique](https://mnacritique.mergersindia.com/news/jsw-st-telemedia-among-firms-eyeing-stake-in-vodafone-idea/) | mnacritique.mergersindia.com | 7 | positive | M&A |
| 3 Mar 2026 | [Telcos gross revenue crosses Rs 1 lakh cr in Dec quarter, AGR up 8.13% to Rs 84,270 cr](https://economictimes.indiatimes.com/industry/telecom/telecom-news/telcos-gross-revenue-crosses-rs-1-lakh-cr-in-dec-quarter-agr-up-8-13-to-rs-84270-cr/articleshow/128979059.cms) | economictimes.indiatimes.com | 7 | positive | Earnings |
| 27 Feb 2026 | [Jio Maintains Leadership in Revenue Market Share in Q3 FY26](https://startupnews.fyi/2026/02/27/jio-maintains-leadership-in-revenue-market-share-in-q3-fy26/) | startupnews.fyi | 7 | positive | Earnings |
| 29 Jan 2026 | [Vi plans ₹45,000-crore debt-funded CapEx, to follow rivals on tariffs \| Communications Today](https://www.communicationstoday.co.in/vi-plans-%e2%82%b945000-crore-debt-funded-capex-to-follow-rivals-on-tariffs/) | communicationstoday.co.in | 7 | positive | Announcement |
| 28 Jan 2026 | [Vodafone Idea rules out fresh equity as AGR relief, bank funding back 3-year turnaround - CNBC TV18](https://www.cnbctv18.com/business/companies/vodafone-idea-rules-out-fresh-equity-as-agr-relief-bank-funding-back-3-year-turnaround-ws-l-19835160.htm) | cnbctv18.com | 8 | negative | Funding round |
| 28 Jan 2026 | [Vodafone Idea finally looks ‘beyond survival’ after AGR ruling - Total Telecom](https://totaltele.com/vodafone-idea-finally-looks-beyond-survival-after-agr-ruling/) | totaltele.com | 8 | negative | Regulatory |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 75 |
| Regulatory | 40 |
| Lawsuit | 30 |
| Announcement | 13 |
| Key people | 10 |
| Funding round | 10 |
| M&A | 4 |
| Contracts | 4 |
| Capital infusion | 3 |
| Asset acquisition | 1 |
| New product | 1 |
| IPO | 1 |
| Board | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Regulatory | Lawsuit | Announcement |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 17 | 7 | 0 | 2 | 4 | ██████████ |
| Jun 2025 | 5 | 2 | 1 | 2 | 0 | ███ |
| Jul 2025 | 4 | 2 | 0 | 0 | 2 | ██ |
| Aug 2025 | 33 | 23 | 0 | 1 | 0 | ████████████████████ |
| Sep 2025 | 22 | 5 | 3 | 10 | 1 | █████████████ |
| Oct 2025 | 20 | 1 | 5 | 10 | 0 | ████████████ |
| Nov 2025 | 33 | 18 | 6 | 4 | 0 | ████████████████████ |
| Dec 2025 | 17 | 1 | 7 | 1 | 2 | ██████████ |
| Jan 2026 | 31 | 11 | 16 | 0 | 1 | ███████████████████ |
| Feb 2026 | 5 | 4 | 1 | 0 | 0 | ███ |
| Mar 2026 | 2 | 1 | 0 | 0 | 0 | █ |
| Apr 2026 | 4 | 0 | 1 | 0 | 3 | ██ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 3 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Regulatory | The government has cut its adjusted gross revenue (AGR) balance by about 27% or Rs 23,649 crore. | article unavailable |
| 23 Apr 2026 | Announcement | Indian telecom operator Vodafone Idea (Vi) has announced an accelerated expansion of its 5G services across Haryana, beginning with launches in… | [Vodafone Idea Rolls Out 5G in Panipat, Ambala; Haryana Expansion to…](https://telecomtalk.info/vodafone-idea-5g-expansion-haryana-panipat-ambala/1006670/) · telecomtalk.info |
| 8 Apr 2026 | Announcement | It is targeting 50,000 additions over the next quarter and one lakh within six months, alongside a push for double‑digit revenue growth. | [Vi’s TN reboot: 5G rollout, subscriber push and CSK connect](https://www.dtnext.in/news/business/vis-tn-reboot-5g-rollout-subscriber-push-and-csk-connect) · dtnext.in |
| 2 Apr 2026 | Announcement | Vodafone Idea is planning to invest ₹45,000 crore over the next three years to come back on a growth trajectory, a senior official of the company… | [Vodafone Idea adds 21,927 new wireless subscribers in February 2026;…](https://upstox.com/news/market-news/stocks/vodafone-idea-adds-21-927-new-wireless-subscribers-in-february-2026-shares-in-focus/article-191576/) · upstox.com |
| 14 Mar 2026 | M&A | ET reported last September that the government was scouting for a strategic investor to invest $1 billion in Vi for a 11-13% stake. | [JSW, ST Telemedia among firms eyeing stake in Vodafone Idea \| M&A…](https://mnacritique.mergersindia.com/news/jsw-st-telemedia-among-firms-eyeing-stake-in-vodafone-idea/) · mnacritique.mergersindia.com |
| 3 Mar 2026 | Earnings | Vodafone Idea with Rs 8,176.62 crore. | [Telcos gross revenue crosses Rs 1 lakh cr in Dec quarter, AGR up…](https://economictimes.indiatimes.com/industry/telecom/telecom-news/telcos-gross-revenue-crosses-rs-1-lakh-cr-in-dec-quarter-agr-up-8-13-to-rs-84270-cr/articleshow/128979059.cms) · economictimes.indiatimes.com |
| 27 Feb 2026 | Earnings | During the same quarter, Vodafone Idea’s AGR was Rs 99… | [Jio Maintains Leadership in Revenue Market Share in Q3 FY26](https://startupnews.fyi/2026/02/27/jio-maintains-leadership-in-revenue-market-share-in-q3-fy26/) · startupnews.fyi |
| 12 Feb 2026 | Earnings | The revenue for Vodafone Idea has shown a slight increase from Rs 11,117.30 crore in December 2024 to Rs 11,323.00 crore in December 2025. | article unavailable |
| 10 Feb 2026 | Earnings | Vodafone Idea’s consolidated net loss narrowed to ₹5,286 crore in the third quarter ended December 2025 as compared to ₹6,609 crore in the same… | article unavailable |
| 6 Feb 2026 | Regulatory | The government has frozen Vi’s AGR dues for FY2006-07 to FY2018-19 at ₹87,695 crore as of December 31, 2025, in line with Supreme Court directions. | [India’s telecom AGR dues hit ₹1.77 lakh crore, Vodafone Idea…](https://upstox.com/news/business-news/latest-updates/india-s-telecom-agr-dues-hit-1-77-lakh-crore-vodafone-idea-accounts-for-over-half-who-owes-how-much/article-189041/) · upstox.com |
| 29 Jan 2026 | Announcement | Vodafone Idea has unveiled an aggressive three-year turnaround blueprint anchored by a ₹45,000‑crore CapEx plan | [Vi plans ₹45,000-crore debt-funded CapEx, to follow rivals on…](https://www.communicationstoday.co.in/vi-plans-%e2%82%b945000-crore-debt-funded-capex-to-follow-rivals-on-tariffs/) · communicationstoday.co.in |

## Funding records, Jan – Apr 2026

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 28 Jan 2026 | Vodafone Idea (myvi.in) | bank funding | $4.2B | — | India | Vi is targeting ₹25,000 crore in bank funding and ₹10,000 crore in non-funded facilities to support its planned ₹45,000 crore capital… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company myvi.in --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company myvi.in --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company myvi.in --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company myvi.in --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/myvi.in/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "myvi.in", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Adani News](adani-news.md)
- [Tesla News](tesla-news.md)
