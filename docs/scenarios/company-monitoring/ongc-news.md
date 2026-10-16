# Ongc News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “ongc news” · 8,100/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [ongc-news.json](../../examples/scenarios/ongc-news.json).

**Question.** What has the news reported about Ongc in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `ongcindia.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `ongcindia.com` |
| Headlines, Jan – Apr 2026 (estimate) | 9 |
| Events, May 2025 – Apr 2026 | 47 |
| Most frequent event types | Earnings (25), Contracts (10), Announcement (7) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 22% · 0.0% · 78% of 9 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 1 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [ONGC Director HR Manish Patil gets additional charge of Director Finance](https://psuwatch.com/psu-appointments/ongc-director-hr-manish-patil-gets-additional-charge-of-director-finance) | psuwatch.com | 7 | positive | Key people |
| 9 Apr 2026 | [Inventory gains, GRMs to boost EBITDA of OMCs in Q4; Down on a quarterly basis](https://www.financialexpress.com/business/news/inventory-gains-grms-to-boost-ebitda-of-omcs-in-q4nbspdown-on-a-quarterly-basis/4201596/) | financialexpress.com | 7 | negative | Earnings |
| 6 Mar 2026 | [ONGC's Highest Ever CapEx & Multi-Billion Dollar Deep-Water Pivot - Nimish Maheshwari](https://www.smartkarma.com/insights/ongc-s-highest-ever-capex-multi-billion-dollar-deep-water-pivot) | smartkarma.com | 7 | positive | Announcement |
| 9 Feb 2026 | [Seamec secures ONGC charter extension for diving support vessel - Splash247](https://splash247.com/seamec-secures-ongc-charter-extension-for-diving-support-vessel/) | splash247.com | 5 | positive | Contracts |
| 30 Jan 2026 | [Energy pivot: India explores US liquefaction investments, Japan upstream tie-ups, says Hardeep Puri \| Today…](https://www.livemint.com/news/natural-gas-liquefication-us-lng-projects-energy-partnerships-japan-hardeep-singh-puri-11769701370255.html) | livemint.com | 8 | positive | Announcement |
| 16 Jan 2026 | [ONGC to board Shipping Corp, oil companies JV as equity partner](https://energy.economictimes.indiatimes.com/news/oil-and-gas/ongc-to-board-shipping-corp-oil-companies-jv-as-equity-partner/126555681) | energy.economictimes.indiatimes.com | 7 | positive | M&A |
| 9 Jan 2026 | [3QFY26 earnings preview: OMCs set to report a strong quarter; upstream and gas to remain under pressure](https://www.fortuneindia.com/markets/3qfy26-earnings-preview-omcs-set-to-report-a-strong-quarter-upstream-and-gas-to-remain-under-pressure/129321) | fortuneindia.com | 7 | positive | Earnings |
| 6 Jan 2026 | [ONGC Partners Mitsui to Expands Ethane Shipping Business](https://startuptalky.com/news/ongc-partners-mitsui-in-joint-venture/) | startuptalky.com | 7 | positive | M&A |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 25 |
| Contracts | 10 |
| Announcement | 7 |
| M&A | 3 |
| Key people | 2 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Contracts | Announcement | M&A |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 10 | 8 | 1 | 0 | 1 | ████████████████████ |
| Jun 2025 | 4 | 2 | 1 | 1 | 0 | ████████ |
| Jul 2025 | 6 | 3 | 2 | 1 | 0 | ████████████ |
| Aug 2025 | 3 | 3 | 0 | 0 | 0 | ██████ |
| Sep 2025 | 3 | 0 | 3 | 0 | 0 | ██████ |
| Oct 2025 | 3 | 2 | 0 | 1 | 0 | ██████ |
| Nov 2025 | 4 | 2 | 0 | 2 | 0 | ████████ |
| Dec 2025 | 2 | 1 | 0 | 0 | 0 | ████ |
| Jan 2026 | 5 | 2 | 0 | 1 | 2 | ██████████ |
| Feb 2026 | 4 | 1 | 3 | 0 | 0 | ████████ |
| Mar 2026 | 1 | 0 | 0 | 1 | 0 | ██ |
| Apr 2026 | 2 | 1 | 0 | 0 | 0 | ████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 3 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Key people | ONGC Director HR Manish Patil has been given additional responsibility of the Director Finance as Vivek Tongaonkar superannuated from the company… | [ONGC Director HR Manish Patil gets additional charge of Director…](https://psuwatch.com/psu-appointments/ongc-director-hr-manish-patil-gets-additional-charge-of-director-finance) · psuwatch.com |
| 9 Apr 2026 | Earnings | ONGC’s standalone EBITDA is expected to raise 36% and Oil India’s EBITDA is set to increase 16%. | [Inventory gains, GRMs to boost EBITDA of OMCs in Q4; Down on a…](https://www.financialexpress.com/business/news/inventory-gains-grms-to-boost-ebitda-of-omcs-in-q4nbspdown-on-a-quarterly-basis/4201596/) · financialexpress.com |
| 6 Mar 2026 | Announcement | ONGC's record high drilling and exploration CapEx in FY25 signals a shift towards frontier exploration to combat production declines, but risks of… | [ONGC's Highest Ever CapEx & Multi-Billion Dollar Deep-Water Pivot -…](https://www.smartkarma.com/insights/ongc-s-highest-ever-capex-multi-billion-dollar-deep-water-pivot) · smartkarma.com |
| 18 Feb 2026 | Contracts | the vessel “SEAMEC DIAMOND” has gone off-hire from its contract with ONGC with effect from February 18, 2026 at 01:30 hrs. | article unavailable |
| 13 Feb 2026 | Earnings | In Q3 FY26, ONGC's revenue from operations declined 6.4 percent YoY to Rupees 31,546.51 crore from Rupees 33,716.80 crore in Q3 FY25. Profit,… | article unavailable |
| 10 Feb 2026 | Contracts | "Vantage Drilling International Ltd. (the \"Company\") announces that it has received a binding Notification of Award (NOA) from ONGC for the… | article unavailable |
| 9 Feb 2026 | Contracts | Indian offshore vessel operator Seamec has secured a charter extension from compatriot government-owned oil and gas company ONGC. | [Seamec secures ONGC charter extension for diving support vessel -…](https://splash247.com/seamec-secures-ongc-charter-extension-for-diving-support-vessel/) · splash247.com |
| 30 Jan 2026 | Announcement | Also Read \| ONGC to offload stake in petchem arm OPal, eyes global investors | [Energy pivot: India explores US liquefaction investments, Japan…](https://www.livemint.com/news/natural-gas-liquefication-us-lng-projects-energy-partnerships-japan-hardeep-singh-puri-11769701370255.html) · livemint.com |
| 16 Jan 2026 | M&A | Earlier this month, ONGC formed an equal JV with Japan's Mitsui O.S.K. Lines, Ltd (MOL), the world's second largest fleet owner, to own and operate… | [ONGC to board Shipping Corp, oil companies JV as equity partner](https://energy.economictimes.indiatimes.com/news/oil-and-gas/ongc-to-board-shipping-corp-oil-companies-jv-as-equity-partner/126555681) · energy.economictimes.indiatimes.com |
| 9 Jan 2026 | Earnings | ONGC and Oil India are expected to report a QoQ decline in EBITDA to ₹17,460 crore, down 8.2% QoQ, according to PL Capital. | [RIL, ONGC to OMCs: What to expect from the oil and gas sector in…](https://www.livemint.com/market/stock-market-news/ril-ongc-to-omcs-what-to-expect-from-the-oil-and-gas-sector-in-q3fy26-results-11767958855534.html) · livemint.com |
| 9 Jan 2026 | Earnings | ONGC’s EBITDA is expected to decline around 10% YoY, hurt by lower oil and gas price realizations. | [3QFY26 earnings preview: OMCs set to report a strong quarter;…](https://www.fortuneindia.com/markets/3qfy26-earnings-preview-omcs-set-to-report-a-strong-quarter-upstream-and-gas-to-remain-under-pressure/129321) · fortuneindia.com |
| 6 Jan 2026 | M&A | In order to enter the specialised ethane shipping market, ONGC would acquire a 50% share in two joint ventures with Mitsui OSK Lines (MOL) of Japan. | [ONGC Partners Mitsui to Expands Ethane Shipping Business](https://startuptalky.com/news/ongc-partners-mitsui-in-joint-venture/) · startuptalky.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company ongcindia.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company ongcindia.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company ongcindia.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company ongcindia.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/ongcindia.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "ongcindia.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Qualcomm News](qualcomm-news.md)
- [Wipro News](wipro-news.md)
- [Toyota News](toyota-news.md)
- [Lucid News](lucid-news.md)
