# IPO India: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “ipo india” · 3,600/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [ipo-india.json](../../examples/scenarios/ipo-india.json).

**Question.** How many ipo india events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `ipo` and the word “India” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 406 |
| Companies (with a domain) | 205 |
| Source articles | 392 |
| Busiest month | Sep 2025 (53 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 6.5% · 0.6% · 93% of 477 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 28 | ███████████ |
| Jun 2025 | 41 | ███████████████ |
| Jul 2025 | 39 | ███████████████ |
| Aug 2025 | 18 | ███████ |
| Sep 2025 | 53 | ████████████████████ |
| Oct 2025 | 46 | █████████████████ |
| Nov 2025 | 19 | ███████ |
| Dec 2025 | 37 | ██████████████ |
| Jan 2026 | 41 | ███████████████ |
| Feb 2026 | 29 | ███████████ |
| Mar 2026 | 35 | █████████████ |
| Apr 2026 | 20 | ████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 9 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 28 Apr 2026 | playsimple.in | IPO | Modern Times Group (MTG) has confirmed that its India-based subsidiary PlaySimple has filed for an initial public offering in Mumbai valued at up to… | [Modern Times Group confirms PlaySimple IPO filing targeting up to…](https://www.pocketgamer.biz/modern-times-group-confirms-playsimple-ipo-filing-targeting-up-to-335m-in-mumbai/) · pocketgamer.biz |
| 28 Apr 2026 | virtusa.com | IPO | Virtusa Corp, a global information technology services firm owned by Swedish private equity giant EQT, is exploring an initial public offering in… | [IT firm Virtusa eyes India IPO, could raise over $1 billion](https://www.thehindubusinessline.com/markets/it-firm-virtusa-eyes-india-ipo-could-raise-over-1-billion/article70915980.ece) · thehindubusinessline.com |
| 23 Apr 2026 | playsimple.in | IPO | PlaySimple has today, on Thursday, April 23, 2026, filed its Draft Red Herring Prospectus (“DRHP”) containing the information related to the… | article unavailable |
| 20 Apr 2026 | imarticus.org | IPO | The Mumbai-based start-up is preparing for an initial public offering of around ₹1,000 crore in FY27 and plans to file its draft red herring… | article unavailable |
| 17 Apr 2026 | cyberscope.fr | IPO | Tac Infosec shares surged following its U.S. subsidiary, CyberScope's, announcement of a planned Nasdaq IPO, a first for an India-listed… | article unavailable |
| 14 Apr 2026 | nodwingaming.com | IPO | Nodwin Gaming, a subsidiary of India's only listed mobile gaming firm Nazara Technologies Ltd, is looking to raise over $100 million and has… | [Nodwin Gaming eyes IPO momentum, inducts Manish Agarwal to board \|…](https://www.livemint.com/companies/nodwin-gaming-eyes-ipo-momentum-inducts-manish-agarwal-board-11776066788697.html) · livemint.com |
| 13 Apr 2026 | nseindia.com | IPO | The proposed maiden issue of the stock exchange could reportedly raise over Rs 20,000 crore from India’s primary markets... | article unavailable |
| 12 Apr 2026 | bonbloc.com | IPO | Bonbloc Technologies Limited, an AI-native enterprise technology and SaaS solutions provider, has issued an Addendum cum Corrigendum to its Draft… | article unavailable |
| 12 Apr 2026 | powericaltd.com | IPO | Linklaters has advised ICICI Securities Limited, IIFL Capital Services Limited and Nuvama Wealth Management Limited as lead underwriters on Powerica… | [Linklaters advises underwriters on Powerica Limited’s INR 11bn IPO](https://legaldesire.com/linklaters-advises-underwriters-on-powerica-limiteds-inr-11bn-ipo/) · legaldesire.com |
| 9 Apr 2026 | powericaltd.com | IPO | Powerica Limited’s INR 11 billion IPO on the National Stock Exchange of India Limited and BSE Limited. | [India - Linklaters Advises Underwriters On Powerica Limited’s INR…](https://conventuslaw.com/press-releases/india-linklaters-advises-underwriters-on-powerica-limiteds-inr-11bn-ipo/) · conventuslaw.com |
| 9 Apr 2026 | sbifunds.com | IPO | seeing with a good eye the SBI Funds Management Limited (SBI AMC) public offering project (IPO) in India. | article unavailable |
| 8 Apr 2026 | ompowertransmission.com | IPO | Om Power Transmission Limited (the “Company”), a power transmission infrastructure engineering, procurement, and construction (“EPC”) company… | [Om Power Transmission Limited IPO Opens on April 09, 2026 - Up18 News](https://up18news.com/om-power-transmission-limited-ipo-opens-on-april-09-2026/) · up18news.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type ipo --q India --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type ipo --q India --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type ipo --q India --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["ipo"], "q": "India", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["ipo"], "q": "India", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Article filters require a matching source article in the same window; records without a matching article are excluded. Each deal still counts once.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.
- Zero-count periods are included; partial_period marks buckets only partly covered by the window.
- shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)

## Related demonstrations

- [AI Layoffs](ai-layoffs.md)
- [Demerger](demerger.md)
- [Q4 Results](q4-results.md)
- [Job Cuts](job-cuts.md)
