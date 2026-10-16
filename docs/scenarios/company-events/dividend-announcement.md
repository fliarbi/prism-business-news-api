# Dividend Announcement: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “dividend announcement” · 1,000/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [dividend-announcement.json](../../examples/scenarios/dividend-announcement.json).

**Question.** How many dividend announcement events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `company_announcement` and the word “dividend” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 363 |
| Companies (with a domain) | 259 |
| Source articles | 350 |
| Busiest month | Sep 2025 (40 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 5.9% · 5.9% · 88% of 68 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 25 | ████████████ |
| Jun 2025 | 25 | ████████████ |
| Jul 2025 | 15 | ████████ |
| Aug 2025 | 29 | ██████████████ |
| Sep 2025 | 40 | ████████████████████ |
| Oct 2025 | 33 | ████████████████ |
| Nov 2025 | 26 | █████████████ |
| Dec 2025 | 26 | █████████████ |
| Jan 2026 | 31 | ████████████████ |
| Feb 2026 | 39 | ████████████████████ |
| Mar 2026 | 39 | ████████████████████ |
| Apr 2026 | 35 | ██████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 4 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | lwcc.com | Announcement | LWCC is distributing $28.73 million to nearly 5,000 employers across Southeast Louisiana as part of its 2025 dividend program, reinforcing the… | article unavailable |
| 30 Apr 2026 | danskebank.fi | Announcement | To accelerate the transition towards the new capital target we will pay an extraordinary dividend of DKK 5 billion following the release of our… | [Danske Bank Announces Financial Targets for 2028 and an Updated…](https://globalfintechseries.com/banking/danske-bank-announces-financial-targets-for-2028-and-an-updated-capital-framework/) · globalfintechseries.com |
| 28 Apr 2026 | aep.com | Announcement | The Board of Directors of American Electric Power (Nasdaq: AEP ) has declared a regular quarterly cash dividend of 95 cents per share on the… | article unavailable |
| 27 Apr 2026 | ultratechcement.com | Announcement | UltraTech Cement declares mega dividend: Record Rs 240 payout surpasses last 4 years combined | [Amazon Now targets 1,000 micro-fulfilment centres across 100 cities](https://www.financialexpress.com/business/industry-amazon-now-targets-1000-micro-fulfilment-centres-across-100-cities-4219714/) · financialexpress.com |
| 26 Apr 2026 | pg.com | Announcement | The company raised its dividend for the seventieth consecutive year, continuing a streak that stretches back to its incorporation in 1890. | [P&G’s Tech Bet Starts Showing Up in Sales \| PYMNTS.com](https://www.pymnts.com/news/retail/2026/pgs-tech-bet-starts-showing-up-in-sales/) · pymnts.com |
| 25 Apr 2026 | hzlindia.com | Announcement | The company also declared an interim dividend of ₹11 per share, with April 30 set as the record date. | [Hindustan Zinc Eyes Capacity Doubling by 2030, Demerger Talks May…](https://www.outlookbusiness.com/corporate/hindustan-zinc-eyes-capacity-doubling-by-2030-demerger-talks-may-resume) · outlookbusiness.com |
| 24 Apr 2026 | nbp.com.pk | Announcement | The bank also announced a final dividend of Rs35 per share, translating into an 88% payout ratio, the highest since 2012. | [NBP bets big on digital future](https://mettisglobal.news/NBP-bets-big-on-digital-future-59964) · mettisglobal.news |
| 23 Apr 2026 | tsmc.com | Announcement | The company also recently declared a quarterly dividend, which will be paid on Thursday, July 9th. Investors of record on Thursday, June 11th will… | [Taiwan Semiconductor Manufacturing (NYSE:TSM) Stock Price Down 1.3%…](https://www.themarketsdaily.com/2026/04/23/taiwan-semiconductor-manufacturing-nysetsm-stock-price-down-1-3-whats-next.html) · themarketsdaily.com |
| 22 Apr 2026 | hcltech.com | Announcement | The company has announced an interim dividend of Rs. 24 on every share for FY 2026-27. | [24 रुपये डिविडेंड बांटने का ऐलान, 4488 करोड़ रुपये का हुआ मुनाफा,…](https://www.livehindustan.com/business/hcl-technologies-share-dropped-over-9-percent-after-q4-weak-results-analysts-cuts-share-target-price-201776835097184.html) · livehindustan.com |
| 17 Apr 2026 | vpl.visagar.com | Announcement | 2013 -Visagar Polytex Declared final Dividend @ 10% on Equity Shares. | article unavailable |
| 16 Apr 2026 | kering.com | Announcement | The group has signaled a desire to bring its dividend payout ratio closer to 50% of its profits. | [Kering Unveils Strategic Plan to Double Profitability and Regain…](https://time.news/kering-unveils-strategic-plan-to-double-profitability-and-regain-investor-trust/) · time.news |
| 16 Apr 2026 | kering.com | Announcement | The French luxury group Kering, owner of firms such as Gucci or Balenciaga, presented on Thursday its new strategy 'ReconKering' that seeks to… | [El dueño de Gucci pretende doblar la rentabilidad a medio plazo y…](https://www.pressdigital.es/articulo/economia/2026-04-16/5846729-dueno-gucci-pretende-doblar-rentabilidad-medio-plazo-acercar-payout-50) · pressdigital.es |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type company_announcement --q dividend --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type company_announcement --q dividend --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type company_announcement --q dividend --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["company_announcement"], "q": "dividend", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["company_announcement"], "q": "dividend", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [It Layoffs](it-layoffs.md)
- [New Product Launch](new-product-launch.md)
- [AI Partnership](ai-partnership.md)
- [Bank Results](bank-results.md)
