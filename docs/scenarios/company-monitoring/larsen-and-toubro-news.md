# Larsen and Toubro News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “larsen and toubro news” · 6,600/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [larsen-and-toubro-news.json](../../examples/scenarios/larsen-and-toubro-news.json).

**Question.** What has the news reported about Larsen and Toubro in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `larsentoubro.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `larsentoubro.com` |
| Headlines, Jan – Apr 2026 (estimate) | 67 |
| Events, May 2025 – Apr 2026 | 205 |
| Most frequent event types | Contracts (70), Earnings (67), Announcement (22) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 9.0% · 1.5% · 90% of 67 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 4 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Hyderabad Metro Rail divestment unlocks capital for core engineering, tech-led businesses: L&T CMD](https://www.thehindu.com/news/cities/Hyderabad/hyderabad-metro-rail-divestment-unlocks-capital-for-core-engineering-tech-led-businesses-lt/article70924463.ece) | thehindu.com | 5 | positive | Asset acquisition |
| 30 Apr 2026 | [Larsen & Toubro Divests 100% Stake In Hyderabad Metro Rail To Unlock Capital](https://www.freepressjournal.in/business/larsen-toubro-divests-100-stake-in-hyderabad-metro-rail-to-unlock-capital) | freepressjournal.in | 7 | positive | Asset acquisition |
| 25 Apr 2026 | [L&T forays into electronics manufacturing](https://www.bizzbuzz.news/manufacturing/lt-forays-into-electronics-manufacturing-1389517) | bizzbuzz.news | 6 | positive | Announcement |
| 24 Apr 2026 | [L&T looks to build India’s next-gen robots and parts with new industrial electronics division](https://www.theweek.in/news/biz-tech/2026/04/24/lnt-industrial-electronics-launch.html) | theweek.in | 7 | positive | New product |
| 24 Apr 2026 | [Larsen & Toubro Wins ₹2,500 Crore Worth Orders For Buildings & Factories Business In India Expansion Push](https://www.freepressjournal.in/business/larsen-toubro-wins-2500-crore-worth-orders-for-buildings-factories-business-in-india-expansion-push) | freepressjournal.in | 7 | positive | Contracts |
| 23 Apr 2026 | [L&T Bags Contract From Oberoi Realty To Construct 7 Residential Towers In Gurugram – Outlook Business](https://www.outlookbusiness.com/corporate/lt-bags-contract-from-oberoi-realty-to-construct-7-residential-towers-in-gurugram) | outlookbusiness.com | 5 | positive | Contracts |
| 13 Apr 2026 | [L&T Eyes Threefold Growth in Nuclear Business Amid Global Clean Energy Push \| Chemical Industry Digest](https://chemindigest.com/lt-eyes-threefold-growth-in-nuclear-business-amid-global-clean-energy-push/) | chemindigest.com | 7 | positive | Announcement |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Contracts | 70 |
| Earnings | 67 |
| Announcement | 22 |
| Asset acquisition | 16 |
| M&A | 10 |
| Key people | 8 |
| Funding round | 4 |
| Regulatory | 3 |
| Capital infusion | 3 |
| New product | 2 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Contracts | Earnings | Announcement | Asset acquisition |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 17 | 2 | 13 | 2 | 0 | ██████████ |
| Jun 2025 | 8 | 5 | 0 | 0 | 1 | █████ |
| Jul 2025 | 22 | 5 | 11 | 1 | 4 | █████████████ |
| Aug 2025 | 22 | 7 | 8 | 2 | 0 | █████████████ |
| Sep 2025 | 18 | 12 | 4 | 0 | 0 | ██████████ |
| Oct 2025 | 35 | 12 | 12 | 4 | 3 | ████████████████████ |
| Nov 2025 | 6 | 3 | 1 | 1 | 0 | ███ |
| Dec 2025 | 5 | 3 | 0 | 1 | 0 | ███ |
| Jan 2026 | 33 | 7 | 18 | 0 | 1 | ███████████████████ |
| Feb 2026 | 11 | 6 | 0 | 2 | 2 | ██████ |
| Mar 2026 | 6 | 2 | 0 | 3 | 1 | ███ |
| Apr 2026 | 22 | 6 | 0 | 6 | 4 | █████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 4 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Asset acquisition | Larsen & Toubro (L&T), which on Wednesday (April 29, 2026), signed an agreement with Telangana government enterprise Hyderabad Metro Rail (HMRL) to… | [Hyderabad Metro Rail divestment unlocks capital for core…](https://www.thehindu.com/news/cities/Hyderabad/hyderabad-metro-rail-divestment-unlocks-capital-for-core-engineering-tech-led-businesses-lt/article70924463.ece) · thehindu.com |
| 30 Apr 2026 | Asset acquisition | Larsen & Toubro has signed an agreement on April 29, 2026, to divest its entire stake in L&T Metro Rail (Hyderabad) Limited to Hyderabad Metro Rail… | [Larsen & Toubro Divests 100% Stake In Hyderabad Metro Rail To Unlock…](https://www.freepressjournal.in/business/larsen-toubro-divests-100-stake-in-hyderabad-metro-rail-to-unlock-capital) · freepressjournal.in |
| 29 Apr 2026 | Asset acquisition | Larsen & Toubro Limited has executed a Share Purchase Agreement with Hyderabad Metro Rail Limited for the sale of its entire shareholding in L&T… | [L&T to sell Hyderabad Metro Rail stake for ₹1,461 crore - CNBC TV18](https://www.cnbctv18.com/market/lt-to-sell-hyderabad-metro-rail-stake-for-rs-1461-crore-ws-l-19896002.htm) · cnbctv18.com |
| 29 Apr 2026 | Asset acquisition | Larsen & Toubro Ltd. (L&T) has finalised the sale of its entire stake in L&T Metro Rail (Hyderabad) Limited for a consideration of Rs 1,461.47 crore. | [Larsen & Toubro to divest entire stake in L&T Metro Rail (Hyderabad)…](https://economictimes.indiatimes.com/industry/transportation/railways/larsen-toubro-sells-entire-stake-in-lt-metro-rail-hyderabad-for-rs-1461-47-crores/articleshow/130606726.cms) · economictimes.indiatimes.com |
| 26 Apr 2026 | New product | Larsen & Toubro (L&T) officially announced on 24 April 2026 its entry into the B2B industrial electronics segment. | article unavailable |
| 25 Apr 2026 | Announcement | New Delhi: Infrastructure major Larsen & Toubro (L&T) on Friday announced its foray into the industrial electronics manufacturing space, with the… | [L&T forays into electronics manufacturing](https://www.bizzbuzz.news/manufacturing/lt-forays-into-electronics-manufacturing-1389517) · bizzbuzz.news |
| 24 Apr 2026 | Regulatory | The Telangana government has formally approved the acquisition of the 100% equity stake held by Larsen & Toubro (L&T) in L&T Metro Rail (Hyderabad)… | article unavailable |
| 24 Apr 2026 | Announcement | Infrastructure major Larsen & Toubro (L&T) on Friday announced its foray into the industrial electronics manufacturing space, with the beginning of… | article unavailable |
| 24 Apr 2026 | New product | On Friday, April 24, 2026, L&T announced that it has formally entered the B2B industrial electronics space with the launch of a brand-new business… | [L&T looks to build India’s next-gen robots and parts with new…](https://www.theweek.in/news/biz-tech/2026/04/24/lnt-industrial-electronics-launch.html) · theweek.in |
| 24 Apr 2026 | Contracts | Alongside residential construction, L&T has secured a contract from an international client to develop a proving ground facility in Haryana. | [Larsen & Toubro Wins ₹2,500 Crore Worth Orders For Buildings &…](https://www.freepressjournal.in/business/larsen-toubro-wins-2500-crore-worth-orders-for-buildings-factories-business-in-india-expansion-push) · freepressjournal.in |
| 23 Apr 2026 | Contracts | The vertical has also bagged many other orders in the domestic market, including for construction of proving ground (testing place) from an… | [L&T Bags Contract From Oberoi Realty To Construct 7 Residential…](https://www.outlookbusiness.com/corporate/lt-bags-contract-from-oberoi-realty-to-construct-7-residential-towers-in-gurugram) · outlookbusiness.com |
| 23 Apr 2026 | Contracts | The business vertical has also secured an order for construction of Proving Ground from a reputed international company in Haryana. | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company larsentoubro.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company larsentoubro.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company larsentoubro.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company larsentoubro.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$PRISM_BUSINESS_API_BASE/v1/business/companies/larsentoubro.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "larsentoubro.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [IBM News](ibm-news.md)
- [Airtel News](airtel-news.md)
- [Salesforce News](salesforce-news.md)
- [Coal India News](coal-india-news.md)
