# Q4 Results: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “q4 results” · 4,400/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [q4-results.json](../../examples/scenarios/q4-results.json).

**Question.** How many q4 results events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `earnings` and the word “Q4” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 3,135 |
| Companies (with a domain) | 2,176 |
| Source articles | 2,912 |
| Busiest month | Feb 2026 (753 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 16% · 0.7% · 83% of 4,778 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 698 | ███████████████████ |
| Jun 2025 | 160 | ████ |
| Jul 2025 | 111 | ███ |
| Aug 2025 | 148 | ████ |
| Sep 2025 | 53 | █ |
| Oct 2025 | 41 | █ |
| Nov 2025 | 54 | █ |
| Dec 2025 | 59 | ██ |
| Jan 2026 | 336 | █████████ |
| Feb 2026 | 753 | ████████████████████ |
| Mar 2026 | 281 | ███████ |
| Apr 2026 | 441 | ████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 3 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | fatpipeinc.com | Earnings | Based on currently available information, FatPipe expects for the fourth quarter: 4th Quarter revenue in the range of $6.6 million to $7.0 million ,… | [FatPipe puts quarterly EBITDA at $3M-$3.2M before May 18 report](https://www.stocktitan.net/news/FATN/fat-pipe-inc-provides-preliminary-fourth-quarter-fiscal-2026-results-4jpq1by1jyw9.html) · stocktitan.net |
| 30 Apr 2026 | eternal.bio | Earnings | Revenue from operations rose 196 percent year on year to Rs 17,292 crore in Q4 from Rs 5,833 crore a year ago while also increasing sequentially… | [Eternal Reports Robust Q4 Revenue Growth](https://www.franchiseindia.com/insights/en/news/eternal-reports-robust-q4-revenue-growth.58811) · franchiseindia.com |
| 30 Apr 2026 | southernenergycorp.com | Earnings | Petroleum and natural gas sales of CA$4.6 million during Q4 2025 and CA$18.0 million for the year ended December 31, 2025, an increase of 17% and… | [Energy Co. Delivers Massive Debt-Free Gulf Coast Turnaround \| Energy…](https://beforeitsnews.com/energy/2026/04/energy-co-delivers-massive-debt-free-gulf-coast-turnaround-2473710.html) · beforeitsnews.com |
| 30 Apr 2026 | evereadyindustries.com | Earnings | Consolidated revenue from operations stood at INR 327.2 crore (Q4 FY25: INR 299.0 crore), driven by favourable momentum in batteries (Alkaline grew… | article unavailable |
| 30 Apr 2026 | indiamart.com | Earnings | IndiaMART Ltd reported a sharp decline in its Q4 net profit, which fell 72.2% year-on-year to ₹50.2 crore from ₹180.6 crore a year earlier. However,… | [IndiaMART Q4 results: Profit plunges 72%, margins contract; ₹60…](https://www.cnbctv18.com/market/indiamart-share-price-q4fy26-results-net-profit-revenue-ebitda-margins-dividend-record-date-ws-l-19896807.htm) · cnbctv18.com |
| 30 Apr 2026 | hul.co.in | Earnings | HUL Q4 adex up by 6% at Rs 1,509 crore; 'Well positioned to navigate volatility' says CEO Priya Nair Hindustan Unilever on Thursday reported a 20%… | [HUL Q4 adex up by 6% at Rs 1,509 crore \| YouTube powers Alphabet’s…](https://www.storyboard18.com/special-coverage/hul-q4-adex-up-by-6-at-rs-1509-crore-youtube-powers-alphabets-ai-push-96814.htm) · storyboard18.com |
| 30 Apr 2026 | ndtv.com | Earnings | NDTV reported a net loss of Rs 98.57 crore in Q4 FY26, significantly higher than the Rs 61.97 crore loss recorded a year ago, reflecting a widening… | article unavailable |
| 30 Apr 2026 | adaniports.com | Earnings | Adani Ports and Special Economic Zone on Thursday reported a 9% rise in consolidated Q4 net profit. Profit came at Rs 3,308 crore in last quarter… | article unavailable |
| 30 Apr 2026 | lalpathlabs.com | Earnings | Dr Lal PathLabs reported a mixed set of Q4 results on Thursday, April 30, with strong revenue growth offset by pressure on profitability margins. | [Dr Lal PathLabs Q4 Results: Profit slips 15% despite strong revenue…](https://www.cnbctv18.com/market/dr-lal-pathlabs-share-price-q4-results-profit-falls-15-pc-revenue-jumps-17-pc-announces-rs-4-dividend-ws-l-19896713.htm) · cnbctv18.com |
| 30 Apr 2026 | bajajfinserv.in | Earnings | The company reported a consolidated net profit of Rs 2,539 crore in Q4 FY26. | [Bajaj Finserv Q4 FY26 results: Net profit up 5% to Rs 2,539 crore,…](https://www.financialexpress.com/business/industry-bajaj-finserv-q4-fy26-results-net-profit-up-5-to-rs-2539-crore-net-income-jumps-to-rs-14209-crorenbsp-4223194/) · financialexpress.com |
| 30 Apr 2026 | adanienterprises.com | Earnings | Adani Enterprises reported a profit before tax of Rs 730 crore for Q4 FY26, against Rs 1,310 crore in the same quarter last year — a 44.3%… | [Adani Enterprises Q4 FY26: PBT down 44% to Rs 730 crore — but here…](https://www.businessupturn.com/business/corporates/adani-enterprises-q4-fy26-pbt-falls-44-to-rs-730-crore-but-a-rs-3940-crore-exceptional-item-last-year-is-distorting-the-entire-comparison/) · businessupturn.com |
| 30 Apr 2026 | adaniports.com | Earnings | For Q4 FY26, the company posted consolidated revenue of ₹10,738 crore, up 26 per cent year-on-year, while EBITDA rose 20 per cent to ₹6,020 crore.… | [Amid global uncertainties, strong cargo volumes steer Adani Ports Q4…](https://www.thehindubusinessline.com/companies/adani-ports-quarterly-profit-rises-as-cargo-volumes-grow/article70923941.ece) · thehindubusinessline.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type earnings --q Q4 --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type earnings --q Q4 --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type earnings --q Q4 --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["earnings"], "q": "Q4", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["earnings"], "q": "Q4", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Demerger](demerger.md)
- [IPO India](ipo-india.md)
- [Job Cuts](job-cuts.md)
- [Strategic Partnership](strategic-partnership.md)
