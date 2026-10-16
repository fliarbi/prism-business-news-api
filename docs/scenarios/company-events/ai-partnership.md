# AI Partnership: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “ai partnership” · 390/month India · 1,300/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [ai-partnership.json](../../examples/scenarios/ai-partnership.json).

**Question.** How many ai partnership events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `company_announcement`, `contracts` and the word “AI” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 4,074 |
| Companies (with a domain) | 1,443 |
| Source articles | 3,397 |
| Busiest month | Aug 2025 (1,008 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 12% · 0.7% · 87% of 6,002 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Announcement | Contracts |  |
| --- | ---: | ---: | ---: | --- |
| May 2025 | 174 | 93 | 81 | ███ |
| Jun 2025 | 160 | 107 | 53 | ███ |
| Jul 2025 | 200 | 131 | 69 | ████ |
| Aug 2025 | 1,008 | 907 | 101 | ████████████████████ |
| Sep 2025 | 305 | 149 | 156 | ██████ |
| Oct 2025 | 277 | 123 | 154 | █████ |
| Nov 2025 | 342 | 150 | 192 | ███████ |
| Dec 2025 | 280 | 147 | 133 | ██████ |
| Jan 2026 | 310 | 199 | 111 | ██████ |
| Feb 2026 | 361 | 242 | 119 | ███████ |
| Mar 2026 | 280 | 143 | 137 | ██████ |
| Apr 2026 | 377 | 217 | 160 | ███████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 3 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | isg-one.com | Announcement | new research report published today by Information Services Group ( ISG ) (Nasdaq: III ), a global AI-centered technology research and advisory firm. | [Asia Pacific companies speed SAP overhauls as 2027 deadline nears](https://www.stocktitan.net/news/III/companies-in-asia-pacific-accelerate-sap-y2n8rqa4xzs3.html) · stocktitan.net |
| 30 Apr 2026 | metavision.com ⚠ check link: not Meta's domain | Announcement | This week, Meta launched the open beta of Meta Ads AI Connectors. | article unavailable |
| 30 Apr 2026 | airproducts.com | Announcement | Industrial gas major Air Products expects its helium supply to electronics customers in Asia to more than double by 2030, as new assets come online… | article unavailable |
| 30 Apr 2026 | datavault.com | Contracts | Datavault AI plans to receive a 5% equity interest in King Mining Capital at the closing of the transactions contemplated by the agreement, together… | article unavailable |
| 30 Apr 2026 | luxinnovation.lu | Announcement | Minister of Economics Lex Delles and CEO Mario Grotz presented the Annual Report 2025 on Thursday, and also provided an update to the Luxembourg AI… | [Luxinnovation schließt strategische Neuausrichtung ab](https://www.wort.lu/wirtschaft/luxinnovation-schliesst-strategische-neuausrichtung-ab/150465278.html) · wort.lu |
| 30 Apr 2026 | options-it.com | Contracts | PrivateMind solution has been selected by a Tier 1 bank for major AI deployment in its Iceland data center. | [Options Technology expands Financial Services Footprint with Major…](https://www.cityam.com/options-technology-expands-financial-services-footprint-with-major-tier-1-bank-ai-deployment-in-iceland/) · cityam.com |
| 30 Apr 2026 | amazon.com | Announcement | Amazon has also committed to investing more than $35 billion in India by 2030 focusing on business expansion and other measures such as AI-driven… | [Amazon Now’s India orders growing 25% every month: CEO Andy Jassy \|…](https://www.livemint.com/companies/news/amazon-now-amazon-prime-india-ceo-andy-jassy-quick-commerce-11777531511884.html) · livemint.com |
| 30 Apr 2026 | qualcomm.com | Announcement | Qualcomm recently partnered with OpenAI to develop an AI chip for a future device. | [Why Qualcomm shares jumped after CEO Cristiano Amon's comments -…](https://www.businesstoday.in/markets/stocks/story/why-qualcomm-shares-jumped-after-ceo-cristiano-amons-comments-key-details-528176-2026-04-30) · businesstoday.in |
| 30 Apr 2026 | msheireb.com | Contracts | Msheireb Properties, a Qatari real estate development company, has signed a Memorandum of Understanding (MoU) with MEEZA, an IT services and… | [Msheireb Properties and MEEZA unveil AI Digital Companion in Doha](https://www.gccbusinessnews.com/msheireb-properties-meeza-ai-companion/) · gccbusinessnews.com |
| 30 Apr 2026 | meeza.net | Contracts | Msheireb Properties, a Qatari real estate development company, has signed a Memorandum of Understanding (MoU) with MEEZA, an IT services and… | [Msheireb Properties and MEEZA unveil AI Digital Companion in Doha](https://www.gccbusinessnews.com/msheireb-properties-meeza-ai-companion/) · gccbusinessnews.com |
| 29 Apr 2026 | amazon.com | Announcement | Amazon also launched Bedrock AgentCore, a set of infra tools for building and deploying AI agents, which Amazon said is now used to deploy an agent… | [Amazon's chips become a $20B business](https://www.theregister.com/software/2026/04/30/amazons-chips-become-a-20b-business/5221236) · theregister.com |
| 29 Apr 2026 | amazon.com | Announcement | Amazon's rapidly expanding custom silicon business includes its Graviton processors, Trainium AI training chips, and Nitro security chips, and is… | [Amazon's chips become a $20B business](https://www.theregister.com/2026/04/29/amazon_chips_20b_business/) · theregister.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type company_announcement --event-type contracts --q AI --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type company_announcement --event-type contracts --q AI --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type company_announcement --event-type contracts --q AI --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["company_announcement", "contracts"], "q": "AI", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["company_announcement", "contracts"], "q": "AI", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [New Product Launch](new-product-launch.md)
- [Dividend Announcement](dividend-announcement.md)
- [Bank Results](bank-results.md)
- [SEBI Order](sebi-order.md)
