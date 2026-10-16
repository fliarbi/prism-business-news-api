# Ola Electric News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “ola electric news” · 27,100/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [ola-electric-news.json](../../examples/scenarios/ola-electric-news.json).

**Question.** What has the news reported about Ola Electric in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `olaelectric.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `olaelectric.com` |
| Headlines, Jan – Apr 2026 (estimate) | 532 |
| Events, May 2025 – Apr 2026 | 193 |
| Most frequent event types | Earnings (75), Announcement (54), New product (17) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 38% · 0.0% · 62% of 532 articles |
| Funding records, Jan – Apr 2026 | 1 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 3 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [E2W registrations rise 52% in April despite price hikes, supply constraints](https://www.financialexpress.com/business/news/e2w-registrations-rise-52-in-april-despite-price-hikes-supply-constraints/4223765/) | financialexpress.com | 6 | positive | — |
| 30 Apr 2026 | [ICRA Downgrades Ola Electric’s Rating Amid Rising Competition, Declining Sales](https://startupnews.fyi/ev-mobility/icra-downgrades-ola-electric-s-rating) | startupnews.fyi | 8 | negative | — |
| 29 Apr 2026 | [Ola Electric shares in focus as ICRA downgrades ratings](https://www.businessupturn.com/finance/stock-market/ola-electric-shares-in-focus-today-icra-downgrades-credit-rating-to-bbb-negative/) | businessupturn.com | 7 | negative | — |
| 27 Apr 2026 | [Markets rebound strongly after three-day losing streak; Sensex gains over 600 points - The Statesman](https://www.thestatesman.com/business/markets-rebound-strongly-after-three-day-losing-streak-sensex-gains-over-600-points-1503586762.html) | thestatesman.com | 6 | positive | — |
| 27 Apr 2026 | [Sensex, Nifty 50 snap 3-day losing run, end over 0.8% higher — 10 key highlights from the Indian stock…](https://www.livemint.com/market/stock-market-news/sensex-nifty-50-snap-3-day-losing-run-end-over-0-8-higher-10-key-highlights-from-the-indian-stock-market-today-11777283924149.html) | livemint.com | 6 | positive | — |
| 24 Apr 2026 | [Top Gainers & Losers on April 24: Anant Raj, Infosys, Cyient, Ceat, HCL Tech, Coforge among top losers \|…](https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-april-24-anant-raj-infosys-cyient-ceat-hcl-tech-coforge-among-top-losers-11777025840580.html) | livemint.com | 8 | negative | — |
| 24 Apr 2026 | [Auto sector stocks today, April 24: Force Motors down 3%, Hyundai Motor India falls 3.10%, Ola Electric…](https://www.businessupturn.com/finance/stock-market/auto-sector-stocks-today-april-24-force-motors-down-3-hyundai-motor-india-falls-3-10-ola-electric-drops-3/) | businessupturn.com | 6 | negative | — |
| 22 Apr 2026 | [Ola Electric Mobility share price rallies 65% this month. Is the worst behind? \| Stock Market News](https://www.livemint.com/market/stock-market-news/ola-electric-mobility-share-price-rallies-65-this-month-is-the-worst-behind-11776830554853.html) | livemint.com | 6 | positive | — |
| 21 Apr 2026 | [Amara Raja plans to begin bulk production of EV cells in 2027](https://economictimes.indiatimes.com/industry/renewables/amara-raja-plans-to-begin-bulk-production-of-ev-cells-in-2027/articleshow/130426634.cms) | economictimes.indiatimes.com | 8 | positive | Announcement |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 75 |
| Announcement | 54 |
| New product | 17 |
| Regulatory | 14 |
| Key people | 13 |
| Funding round | 6 |
| IPO | 5 |
| Lawsuit | 4 |
| Layoffs | 4 |
| Job creation | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Announcement | New product | Regulatory |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 19 | 13 | 2 | 1 | 0 | ██████████████ |
| Jun 2025 | 4 | 3 | 0 | 1 | 0 | ███ |
| Jul 2025 | 25 | 19 | 3 | 1 | 1 | ███████████████████ |
| Aug 2025 | 12 | 1 | 3 | 4 | 0 | █████████ |
| Sep 2025 | 12 | 2 | 8 | 1 | 1 | █████████ |
| Oct 2025 | 11 | 0 | 4 | 4 | 1 | ████████ |
| Nov 2025 | 17 | 14 | 1 | 0 | 0 | █████████████ |
| Dec 2025 | 22 | 3 | 6 | 0 | 7 | ████████████████ |
| Jan 2026 | 20 | 0 | 8 | 3 | 0 | ███████████████ |
| Feb 2026 | 27 | 19 | 4 | 0 | 2 | ████████████████████ |
| Mar 2026 | 6 | 1 | 3 | 1 | 0 | ████ |
| Apr 2026 | 18 | 0 | 12 | 1 | 2 | █████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 1 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 16 Apr 2026 | Regulatory | Bourses BSE and NSE have put the securities of Ola Electric under the short-term ASM (Additional Surveillance Measure) framework. | [Ola Electric shares: Up 59% in a month, still nursing a 30% six…](https://www.businesstoday.in/markets/stocks/story/ola-electric-shares-up-59-in-a-month-still-nursing-a-30-six-month-decline-should-you-buy-525874-2026-04-16) · businesstoday.in |
| 15 Apr 2026 | Announcement | Ola Electric Mobility Limited announced today that its vehicle registration numbers on the VAHAN portal will temporarily decrease during February… | [Ola Electric Warns of Temporary Dip in Vahan Portal Registrations \|…](https://www.autocarpro.in/news/ola-electric-warns-of-temporary-dip-in-vahan-portal-registrations-125024) · autocarpro.in |
| 15 Apr 2026 | IPO | Shares of OIa Electric touched 20% upper circuit on the exchange on today's listing. The company's share price closed at Rs 91.18 per share on the… | [Ola Electric surges 20% to hit upper circuit on listing day \|…](https://www.autocarpro.in/news/ola-electric-surges-20-to-hit-upper-circuit-on-listing-day--121977) · autocarpro.in |
| 15 Apr 2026 | Announcement | India's largest electric two-wheeler maker Ola Electric is planning to roll out its first electric motorcycle Roadster this month. | [Ultraviolette Targets 12 New Models in 3 Years, Annual Sales of 1…](https://www.autocarpro.in/news/ultraviolette-targets-12-new-models-in-3-years-annual-sales-of-1-lakh-units-in-3-4-years-125266) · autocarpro.in |
| 15 Apr 2026 | Key people | Ola Electric Mobility (Ola Electric) today announced the appointment of BVR Subbu as a member of its Board of Directors. | [BVR Subbu joins Ola Electric board of directors \| Autocar Professional](https://www.autocarpro.in/news-national/bvr-subbu-joins-ola-electric-board-of-directors-44645) · autocarpro.in |
| 14 Apr 2026 | Regulatory | Share this News: New Delhi, 13th April 2026: Ola Electric has received a major relief from the Bombay High Court as it quashed earlier orders passed… | [Ola Electric CEO Spared Court Appearance - Punekar News](https://www.punekarnews.in/ola-electric-ceo-spared-court-appearance/) · punekarnews.in |
| 14 Apr 2026 | Announcement | Ola Electric has announced the readiness of its in-house developed 46100 format Lithium Iron Phosphate (LFP) battery cell, marking a major step… | article unavailable |
| 9 Apr 2026 | Announcement | The Gigafactory currently has a capacity of 2.5 GWh, which is being scaled up to 6 GWh. | [Ola Electric Mobility shares surge 17% on in-house LFP cell…](https://www.auto.economictimes.indiatimes.com/news/two-wheelers/ola-electric-mobility-shares-surge-17-on-in-house-lfp-cell-breakthrough-extend-two-day-rally-to-22/130136221) · auto.economictimes.indiatimes.com |
| 8 Apr 2026 | Announcement | Ola Electric has announced the readiness of its in-house developed Lithium Iron Phosphate (LFP) battery cell, marking a significant milestone in its… | [Ola Electric Unveils Indigenous LFP 46100 Battery Cell as…](https://emobilityplus.com/2026/04/08/ola-electric-unveils-indigenous-lfp-46100-battery-cell-as-gigafactory-expansion-accelerates-and-ev-adoption-gains-momentum/) · emobilityplus.com |
| 8 Apr 2026 | Announcement | Ola Electric on Tuesday announced readiness of its in-house developed lithium iron phosphate (LFP) cell, marking a key milestone in its mission to… | [Indigenous 46100 LFP cell is ready: Ola Electric](https://www.bizzbuzz.news/industry/auto/indigenous-46100-lfp-cell-is-ready-ola-electric-1388575) · bizzbuzz.news |
| 7 Apr 2026 | Announcement | Ola Electric on Tuesday announced that its in-house developed Lithium Iron Phosphate (LFP) battery cell is now ready for the market and will enter… | [Ola Electric 'ready' with in-house LFP battery cell, 46100 format to…](https://www.auto.economictimes.indiatimes.com/news/auto-components/ola-electric-launches-in-house-developed-lfp-battery-cells-for-next-gen-evs/130082817) · auto.economictimes.indiatimes.com |
| 7 Apr 2026 | Announcement | New Delhi: Ola Electric on Tuesday announced readiness of its in-house developed lithium iron phosphate (LFP) cell, marking a key milestone in its… | [Ola Electric announces readiness of indigenous 46100 LFP cell](https://economictimes.indiatimes.com/industry/renewables/ola-electric-announces-readiness-of-indigenous-46100-lfp-cell/articleshow/130084712.cms) · economictimes.indiatimes.com |

## Funding records, Jan – Apr 2026

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 16 Mar 2026 | Ola Electric Mobility (olaelectric.com) | Initial Public Offering | $660M | — | India | In August 2024, Ola Electric Mobility raised Rs 5,500 crore through its initial public offering (IPO). |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company olaelectric.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company olaelectric.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company olaelectric.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company olaelectric.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/olaelectric.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "olaelectric.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Boeing News](boeing-news.md)
- [Tata Motors News](tata-motors-news.md)
- [Zomato News](zomato-news.md)
- [Hdfc Bank News](hdfc-bank-news.md)
