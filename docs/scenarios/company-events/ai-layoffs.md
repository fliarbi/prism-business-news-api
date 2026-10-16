# AI Layoffs: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “ai layoffs” · 2,900/month India · 4,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [ai-layoffs.json](../../examples/scenarios/ai-layoffs.json).

**Question.** How many ai layoffs events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `layoffs` and the word “AI” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 110 |
| Companies (with a domain) | 74 |
| Source articles | 106 |
| Busiest month | Mar 2026 (15 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 82% · 0.2% · 18% of 397 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 5 | ███████ |
| Jun 2025 | 4 | █████ |
| Jul 2025 | 10 | █████████████ |
| Aug 2025 | 9 | ████████████ |
| Sep 2025 | 14 | ███████████████████ |
| Oct 2025 | 12 | ████████████████ |
| Nov 2025 | 7 | █████████ |
| Dec 2025 | 2 | ███ |
| Jan 2026 | 11 | ███████████████ |
| Feb 2026 | 11 | ███████████████ |
| Mar 2026 | 15 | ████████████████████ |
| Apr 2026 | 10 | █████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 4 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 24 Apr 2026 | superops.com | Layoffs | Enterprise tech startup SuperOps has laid off around 60 employees as part of a restructuring exercise aimed at improving efficiency and accelerating… | [SuperOps Lays Off 30% Staff In AI-Led Restructuring Push](https://inc42.com/buzz/superops-lays-off-30-staff-in-ai-led-restructuring-push/) · inc42.com |
| 23 Apr 2026 | target.com | Layoffs | Target eliminates posts while accelerating its shift towards AI The decision was communicated internally and responds to the need to “manage the… | [Meta despedirá a 8.000 empleados en plena apuesta por la…](https://www.perfil.com/noticias/economia/meta-despedira-a-8000-empleados-en-plena-apuesta-por-la-inteligencia-artificial-segun-afp-a40.phtml) · perfil.com |
| 20 Apr 2026 | acko.com | Layoffs | Digital insuretech firm Acko has let go of around 60 employees, or roughly 5 per cent of its workforce, as part of a broader structural realignment… | article unavailable |
| 20 Apr 2026 | binance.com | Layoffs | Binance fired an employee for 'holding multiple jobs' after using AI to improve development efficiency. | [A top influencer reveals: Binance employee doubled coding efficiency…](https://www.panewslab.com/en/articles/019da9d1-3077-761a-b9ec-fbca0bb20946) · panewslab.com |
| 18 Apr 2026 | sama.com | Layoffs | Sama officially announced the mass layoffs, confirming that over 1,000 individuals would lose their positions following Meta’s decision to end their… | article unavailable |
| 17 Apr 2026 | oracle.com | Layoffs | Oracle has reported the highest number of layoffs globally in 2026, cutting more than 25,000 roles as part of a major restructuring tied to its AI… | [Global tech layoffs hit 80,000 in Q1, tally may cross 3 lakh this…](https://www.lokmattimes.com/technology/global-tech-layoffs-hit-80000-in-q1-tally-may-cross-3-lakh-this-year-report-1/) · lokmattimes.com |
| 9 Apr 2026 | x.ai | Layoffs | February 11: xAI layoffs affect co-founders AI company xAI has reduced its workforce during a reorganization initiative, confirmed by founder Elon… | [2026 tech company layoffs](https://informationweek.com/it-staffing-careers/2026-tech-company-layoffs) · informationweek.com |
| 9 Apr 2026 | hsbc.com | Layoffs | Meanwhile, another report said that global banking major HSBC is also considering job cuts over the coming years, as Chief Executive Officer Georges… | article unavailable |
| 3 Apr 2026 | metavision.com ⚠ check link: not Meta's domain | Layoffs | Meta, which laid off 700 staff from its Reality Labs division in March, and Oracle, which this week notified thousands of workers they were being… | article unavailable |
| 30 Mar 2026 | chrobinson.com | Layoffs | The Eden Prairie-based logistics company has reduced its total employment by 31% as it deploys hundreds of AI agents. | [C.H. Robinson trims high-level managers as part of AI-driven cuts](https://www.startribune.com/ch-robinson-trims-high-level-managers-as-part-of-ai-cuts/601638317) · startribune.com |
| 25 Mar 2026 | metavision.com ⚠ check link: not Meta's domain | Layoffs | Meta is replacing its human moderators with artificial intelligence systems to identify harmful content that goes against their policies. The… | [Meta sustituye a sus moderadores de contenido por IA pese a sus…](https://www.publico.es/sociedad/meta-sustituye-moderadores-contenido-ia-pese-riesgos-humanos-entienden-mejor-contexto.html) · publico.es |
| 25 Mar 2026 | meetblock.com ⚠ check link: not Block's domain | Layoffs | Block CEO Jack Dorsey recently reduced his workforce by 40%, citing AI’s capacity to reshape corporate operations. | [Perplexity CEO Aravind Srinivas Suggests AI Layoffs Could Fuel New…](https://www.latestly.com/technology/perplexity-ceo-aravind-srinivas-suggests-ai-layoffs-could-fuel-new-era-of-entrepreneurship-7366751.html) · latestly.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type layoffs --q AI --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type layoffs --q AI --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type layoffs --q AI --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["layoffs"], "q": "AI", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["layoffs"], "q": "AI", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [FDA Approval](fda-approval.md)
- [Rights Issue](rights-issue.md)
- [Demerger](demerger.md)
- [IPO India](ipo-india.md)
