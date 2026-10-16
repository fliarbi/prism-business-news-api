# Bankruptcy News: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “bankruptcy news” · 30/month India · 1,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [bankruptcy-news.json](../../examples/scenarios/bankruptcy-news.json).

**Question.** How many bankruptcy events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `company_announcement`, `lawsuit` and the word “bankruptcy” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 325 |
| Companies (with a domain) | 190 |
| Source articles | 268 |
| Busiest month | Aug 2025 (50 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 86% · 1.3% · 13% of 157 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Lawsuit | Announcement |  |
| --- | ---: | ---: | ---: | --- |
| May 2025 | 15 | 15 | 0 | ██████ |
| Jun 2025 | 19 | 16 | 3 | ████████ |
| Jul 2025 | 24 | 20 | 4 | ██████████ |
| Aug 2025 | 50 | 39 | 11 | ████████████████████ |
| Sep 2025 | 31 | 22 | 9 | ████████████ |
| Oct 2025 | 20 | 11 | 9 | ████████ |
| Nov 2025 | 27 | 20 | 7 | ███████████ |
| Dec 2025 | 27 | 18 | 9 | ███████████ |
| Jan 2026 | 28 | 23 | 5 | ███████████ |
| Feb 2026 | 39 | 36 | 3 | ████████████████ |
| Mar 2026 | 17 | 6 | 11 | ███████ |
| Apr 2026 | 28 | 26 | 2 | ███████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 5 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 29 Apr 2026 | fatbrands.com | Announcement | FAT Brands Inc., which oversees the franchise-based chain, filed for Chapter 11 bankruptcy in January to restructure more than $1 billion in debt. | [Longtime Restaurant Chain Closes All MA Locations](https://patch.com/massachusetts/across-ma/longtime-restaurant-chain-closes-all-ma-locations) · patch.com |
| 28 Apr 2026 | firstbrandsgroup.com | Lawsuit | First Brands Group LLC doled out bonuses to employees who booked accounting adjustments that inflated its profit margins and picked its outside… | [Bankruptcy Report Details First Brands Accounting, Audits (1)](https://news.bloomberglaw.com/financial-accounting/bankruptcy-report-sheds-light-on-first-brands-accounting-audits) · news.bloomberglaw.com |
| 23 Apr 2026 | qvcgroup.com | Lawsuit | The QVC Group, which operates the HSN and QVC shopping channels, filed for bankruptcy protection in April. | article unavailable |
| 23 Apr 2026 | ffcorp.org | Lawsuit | Friendly Franchisees Corporation, a large Carl’s Jr. franchisee, filed for bankruptcy protection in early April. | article unavailable |
| 23 Apr 2026 | 801restaurantgroup.com | Lawsuit | The parent company of 801 Chophouse, a small chain of upscale steakhouses primarily in the Midwest, filed for bankruptcy in April. | article unavailable |
| 22 Apr 2026 | proxicom.com | Lawsuit | The bankruptcy court judge, Judith K. Fitzgerald, also approved a settlement between Armstrong and its Web site developer, ending a three-year pay… | [Armstrong gets another extension](https://lancasteronline.com/business/armstrong-gets-another-extension/article_38f5568f-3cfe-529c-9f36-e9c0f0882b5a.html) · lancasteronline.com |
| 22 Apr 2026 | armstrongceilings.com | Lawsuit | The bankruptcy court judge, Judith K. Fitzgerald, also approved a settlement between Armstrong and its Web site developer, ending a three-year pay… | [Armstrong gets another extension](https://lancasteronline.com/business/armstrong-gets-another-extension/article_38f5568f-3cfe-529c-9f36-e9c0f0882b5a.html) · lancasteronline.com |
| 17 Apr 2026 | 801restaurantgroup.com | Lawsuit | 801 Restaurant Group LLC filed for Chapter 11 reorganization last Friday in U.S. Bankruptcy Court in Kansas | article unavailable |
| 17 Apr 2026 | qvcgroup.com | Lawsuit | QVC Group jointly filed 70 bankruptcy cases on behalf of itself and its subsidiaries, which include popular QVC brands such as Cornerstone, Ballard… | [QVC officially filed for bankruptcy. Here's what to know.](https://www.inquirer.com/business/retail/qvc-bankruptcy-debt-financial-restructuring-20260417.html) · inquirer.com |
| 17 Apr 2026 | qvcgroup.com | Lawsuit | Online retailer QVC Group has initiated voluntary Chapter 11 bankruptcy proceedings in the US after reaching a restructuring support agreement with… | [Multimedia retailer QVC Group begins Chapter 11 process](https://www.retail-insight-network.com/news/qvc-group-begins-chapter-11-process/) · retail-insight-network.com |
| 17 Apr 2026 | supernova.io | Lawsuit | In the filing in the U.S. Bankruptcy Court for the Southern District of Texas, under SuperNova Management Inc., the Humble, Texas-based retailer… | [SuperNova Furniture owner: ‘We’ll come back stronger’ - Furniture…](https://www.furnituretoday.com/financial/supernova-furniture-owner-well-come-back-stronger/) · furnituretoday.com |
| 17 Apr 2026 | qvcgroup.com | Lawsuit | Home shopping network QVC Group Inc. has filed for Chapter 11 bankruptcy court protection in Texas to cut $5.3 billion off its debt load. | [Clarks, Skechers Among Shoe Brands Hit by QVC Bankruptcy](https://wwd.com/footwear-news/shoe-industry-news/qvc-bankruptcy-clarks-skechers-home-shopping-1238919519/) · wwd.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type company_announcement --event-type lawsuit --q bankruptcy --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type company_announcement --event-type lawsuit --q bankruptcy --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type company_announcement --event-type lawsuit --q bankruptcy --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["company_announcement", "lawsuit"], "q": "bankruptcy", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["company_announcement", "lawsuit"], "q": "bankruptcy", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [CEO Appointment](ceo-appointment.md)
- [Battery Plant](battery-plant.md)
- [Data Center Investment](data-center-investment.md)
- [Media Mergers](media-mergers.md)
