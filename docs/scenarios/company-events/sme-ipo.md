# SME IPO: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “sme ipo” · 22,200/month India · 70/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [sme-ipo.json](../../examples/scenarios/sme-ipo.json).

**Question.** How many sme ipo events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `ipo` and the word “SME” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 186 |
| Companies (with a domain) | 111 |
| Source articles | 166 |
| Busiest month | Jul 2025 (29 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 7.4% · 0.0% · 93% of 95 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 16 | ███████████ |
| Jun 2025 | 18 | ████████████ |
| Jul 2025 | 29 | ████████████████████ |
| Aug 2025 | 18 | ████████████ |
| Sep 2025 | 26 | ██████████████████ |
| Oct 2025 | 22 | ███████████████ |
| Nov 2025 | 5 | ███ |
| Dec 2025 | 12 | ████████ |
| Jan 2026 | 17 | ████████████ |
| Feb 2026 | 8 | ██████ |
| Mar 2026 | 12 | ████████ |
| Apr 2026 | 3 | ██ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 4 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 23 Apr 2026 | lesgroup.in | IPO | Leapfrog Engineering Services Limited has announced its plan to raise funds through an Initial Public Offering (IPO) on the BSE SME platform. | article unavailable |
| 17 Apr 2026 | prlindia.com | IPO | Premier Roadlines shares list at 30% premium on the NSE SME platform, debuting at Rs 87. | [Premier Roadlines News - Premier Roadlines Announcement, Latest News…](https://economictimes.indiatimes.com/premier-roadlines-ltd/stocksupdate/companyid-2199024.cms) · economictimes.indiatimes.com |
| 31 Mar 2026 | monomark.co.in | IPO | Monomark Engineering IPO open date is 2026 and the IPO will close on 2026. Monomark Engineering IPO is a Bookbuilding IPO Issue. The company to… | [Monomark Engineering IPO Date, Review, Price, Allotment Details -…](https://ipowatch.in/monomark-engineering-ipo-date-review-price-allotment-details/) · ipowatch.in |
| 27 Mar 2026 | emiactech.com | IPO | The SME initial public offer (IPO) of Emiac Technologies Limited will open for bidding on Friday and close on Wednesday, April 8. | [Rs 32 crore SME IPO of Emiac Technologies opens today - check price…](https://economictimes.indiatimes.com/markets/ipos/fpos/rs-32-crore-sme-ipo-of-emiac-technologies-opens-today-check-price-band-gmp-other-details/articleshow/129837083.cms) · economictimes.indiatimes.com |
| 25 Mar 2026 | vividgroup.in | IPO | The SME initial public offer (IPO) of Vivid Electromech opened for bidding on Wednesday and will close on Monday March 30. | article unavailable |
| 24 Mar 2026 | tipcoengineering.com | IPO | Explore how Tipco Engineering India Ltd.’s IPO performed during its subscription period, including investor participation on Day 1, price band… | [Explore how Tipco Engineering India Ltd.’s IPO performed during its…](https://www.bajajfinservmarkets.in/discover/tipco-engineering-india-ipo-subscription-status) · bajajfinservmarkets.in |
| 23 Mar 2026 | tipcoengineering.com | IPO | Tipco Engineering India Limited, an integrated engineering powerhouse based in Mumbai, is set to launch its Initial Public Offering (IPO) on March… | [Tipco Engineering's Strategic IPO: A New Era of Growth \| Business](https://www.devdiscourse.com/article/business/3847420-tipco-engineerings-strategic-ipo-a-new-era-of-growth) · devdiscourse.com |
| 23 Mar 2026 | liqvd.asia | IPO | Digital advertising agency Liqvd Asia, after submitting its DRHP in late 2025, received regulatory approval in early 2026 for its SME listing. | [IPO wave hits digital ad agencies as indies choose scale over sellouts](http://www.storyboard18.com/advertising/ipo-wave-hits-digital-ad-agencies-as-indies-choose-scale-over-sellouts-92883.htm) · storyboard18.com |
| 17 Mar 2026 | specialitymedicine.com | IPO | Speciality Medicines, engaged in the marketing and distribution of speciality pharmaceutical products across multiple therapeutic areas, plans to… | article unavailable |
| 14 Mar 2026 | novusloyalty.com | IPO | Novus Loyalty Limited will launch its IPO on March 17, with the issue closing on March 20. The SME IPO has a price band of Rs 139 to Rs 146 per… | [IPO Calendar: Coal India subsidiary among 3 IPOs scheduled for next…](https://economictimes.indiatimes.com/markets/ipos/fpos/ipo-calendar-coal-india-subsidiary-among-3-ipos-scheduled-for-next-week/articleshow/129569743.cms) · economictimes.indiatimes.com |
| 13 Mar 2026 | novusloyalty.com | IPO | The ₹60.15 crore SME issue of Novus Loyalty is a mix of a fresh issue worth ₹48.18 crore and an OFS of ₹11.97 crore by Deepak Tomar and Sweta Singh.… | article unavailable |
| 2 Mar 2026 | mobilise.co.in | IPO | Shares of Mobilise App Lab are set to list on the NSE SME platform on March 2, with the grey market premium currently at around 5% over the issue… | [Mobilise App shares to debut on NSE SME today. GMP indicates…](https://economictimes.indiatimes.com/markets/stocks/news/mobilise-app-shares-to-debut-on-nse-sme-today-gmp-indicates-positive-listing/articleshow/128933334.cms) · economictimes.indiatimes.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type ipo --q SME --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type ipo --q SME --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type ipo --q SME --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["ipo"], "q": "SME", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["ipo"], "q": "SME", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Government Contract](government-contract.md)
- [Earnings](earnings.md)
- [Share Buyback](share-buyback.md)
- [Tech Layoffs](tech-layoffs.md)
