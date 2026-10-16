# Media Layoffs: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “media layoffs” · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [media-layoffs.json](../../examples/scenarios/media-layoffs.json).

**Question.** How many media layoffs events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `layoffs` and the word “media” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 66 |
| Companies (with a domain) | 55 |
| Source articles | 64 |
| Busiest month | May 2025 (11 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 83% · 0.0% · 17% of 69 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 11 | ████████████████████ |
| Jun 2025 | 5 | █████████ |
| Jul 2025 | 7 | █████████████ |
| Aug 2025 | 7 | █████████████ |
| Sep 2025 | 6 | ███████████ |
| Oct 2025 | 5 | █████████ |
| Nov 2025 | 5 | █████████ |
| Dec 2025 | 2 | ████ |
| Jan 2026 | 2 | ████ |
| Feb 2026 | 3 | █████ |
| Mar 2026 | 6 | ███████████ |
| Apr 2026 | 7 | █████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 5 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 24 Apr 2026 | nestle.com | Layoffs | In Germany and Spain, media reports suggested the cuts in those countries amount to around 300 each, with a further 185 in Italy. | [Nestlé job cull begins in Europe under plan to eliminate 16,000…](https://www.just-food.com/news/nestle-job-cuts-begin-in-europe-under-plan-to-eliminate-16000-positions/) · just-food.com |
| 24 Apr 2026 | microsoft.com | Layoffs | Also on Thursday, US media reported that tech giant Microsoft was planning to offer voluntary early retirement buyouts for around 8.700 workers, or… | article unavailable |
| 17 Apr 2026 | metavision.com ⚠ check link: not Meta's domain | Layoffs | The parent of major social media platforms, Meta, eliminated approximately 2,400 roles. | [Tech Layoffs Surge Globally: Job Cuts Across Sector Cross Over…](https://www.latestly.com/technology/tech-layoffs-surge-globally-job-cuts-across-sector-cross-over-80000-in-q1-as-tech-giants-shift-toward-ai-infrastructure-7396737.html) · latestly.com |
| 17 Apr 2026 | olakrutrim.com | Layoffs | This followed earlier cuts of about 100 employees, taking the total number of layoffs this year to nearly 200, according to media reports. | article unavailable |
| 16 Apr 2026 | saxoniaguesthouse.co.uk | Layoffs | According to a recent media report, the precious metal manufacturer and recycler Saxonia, based in Dresden (Saxony), has now decided to take this… | [Deutsches Traditionsunternehmen soll aufgelöst werden – was wird aus…](https://www.merkur.de/wirtschaft/traditionsunternehmen-soll-aufgeloest-werden-was-wird-aus-den-mitarbeitern-94264497.html) · merkur.de |
| 9 Apr 2026 | snapacc.com | Layoffs | April 15: Snap lays off 16% of workforce Snap, parent company of social media platform Snapchat, is reducing its headcount by 1,000 jobs, according… | [2026 tech company layoffs](https://informationweek.com/it-staffing-careers/2026-tech-company-layoffs) · informationweek.com |
| 18 Mar 2026 | unfi.com | Layoffs | United Natural Foods Inc. (UNFI) plans to close a distribution facility in Racine, Wis., according to multiple media reports. The move will lay off… | article unavailable |
| 17 Mar 2026 | multichoiceafrica.com | Layoffs | CANAL+, the French media giant, plans to cut staff at its African pay-TV subsidiary MultiChoice Group through a voluntary severance package to… | article unavailable |
| 11 Mar 2026 | antolin.com | Layoffs | About 50 workers are expected to lose their jobs, according to Slovak media reports. | [Spanish automotive supplier to shut Trnava plant](https://spectator.sme.sk/business/c/spanish-automotive-supplier-to-shut-one-of-its-plants-in-slovakia) · spectator.sme.sk |
| 11 Mar 2026 | hndpx.com | Layoffs | Horizon Media, among the world’s largest independent ad agencies, underwent a round of layoffs this week, cutting 50 roles out of a headcount of… | [EXCLUSIVE: Horizon Media Cuts 50 Roles in AI-Focused Agency…](https://www.adweek.com/agencies/horizon-media-layoffs-march-2026/) · adweek.com |
| 11 Mar 2026 | multichoice.com | Layoffs | French media group Canal+ plans to cut the workforce at MultiChoice through voluntary severance offers targeted at support functions. | article unavailable |
| 5 Mar 2026 | paceind.com | Layoffs | and in Jackson. Tenn., where 59 workers will lose their jobs, according to media reports in both markets. | [Pace Industries to close pair of Muskegon plants, cut 145 jobs](https://www.crainsgrandrapids.com/news/manufacturing/pace-industries-to-close-pair-of-muskegon-plants-cut-145-jobs/) · crainsgrandrapids.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type layoffs --q media --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type layoffs --q media --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type layoffs --q media --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["layoffs"], "q": "media", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["layoffs"], "q": "media", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Bank Layoffs](bank-layoffs.md)
- [Tech IPO](tech-ipo.md)
- [CEO Resigns](ceo-resigns.md)
- [Drug Approval](drug-approval.md)
