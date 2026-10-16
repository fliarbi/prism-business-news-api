# FDA Approval: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “fda approval” · 2,900/month India · 6,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [fda-approval.json](../../examples/scenarios/fda-approval.json).

**Question.** How many fda approval events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `fda_approval`.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 226 |
| Companies (with a domain) | 142 |
| Source articles | 213 |
| Busiest month | Oct 2025 (31 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 11% · 0.0% · 89% of 53 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 16 | ██████████ |
| Jun 2025 | 14 | █████████ |
| Jul 2025 | 16 | ██████████ |
| Aug 2025 | 26 | █████████████████ |
| Sep 2025 | 17 | ███████████ |
| Oct 2025 | 31 | ████████████████████ |
| Nov 2025 | 25 | ████████████████ |
| Dec 2025 | 24 | ███████████████ |
| Jan 2026 | 11 | ███████ |
| Feb 2026 | 18 | ████████████ |
| Mar 2026 | 16 | ██████████ |
| Apr 2026 | 12 | ████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 7 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | lilly.com | FDA approval | What else you need to know: Eli Lilly’s GLP‑1 business got another tailwind during the quarter with the FDA’s approval of Foundayo, the pill version… | article unavailable |
| 23 Apr 2026 | ciplausa.com | FDA approval | Cipla’s wholly owned subsidiary — Cipla USA Inc (Cipla) has received final approval from the United States Food and Drug Administration (USFDA) for… | [Cipla shines as its arm gets USFDA’s final nod for Albuterol Sulfate…](https://udaipurkiran.com/cipla-shines-as-its-arm-gets-usfdas-final-nod-for-albuterol-sulfate-inhalation-aerosol/) · udaipurkiran.com |
| 17 Apr 2026 | aurobindo.com | FDA approval | Aurobindo Pharma has received final approval from the US Food & Drug Administration (USFDA) to manufacture and market Glycerol Phenylbutyrate Oral… | [Aurobindo Pharma inches up on getting USFDA’s final nod for Glycerol…](https://udaipurkiran.com/aurobindo-pharma-inches-up-on-getting-usfdas-final-nod-for-glycerol-phenylbutyrate-oral-liquid/) · udaipurkiran.com |
| 16 Apr 2026 | bluetree.ai | FDA approval | received “self-affirmed FDA food safe status” from the US Food and Drug Administration | [Reduced-sugar tech for beverages gets FDA approval](https://www.dairyprocessing.com/articles/2470-reduced-sugar-tech-for-beverages-gets-fda-approval) · dairyprocessing.com |
| 14 Apr 2026 | travere.com | FDA approval | the company announced that the FDA approved FILSPARI to reduce proteinuria in adult and pediatric patients aged 8 years and older with focal… | [Crude Oil Falls Sharply; Wells Fargo Earnings Miss Views - Avanos…](https://benzinga.com/markets/market-summary/26/04/51811493/crude-oil-falls-sharply-wells-fargo-earnings-miss-views) · benzinga.com |
| 10 Apr 2026 | telixpharma.com | FDA approval | The move was triggered by Telix's announcement that the U.S. Food and Drug Administration accepted its resubmitted New Drug Application for… | [Telix Pharmaceuticals Shares Jump 7% on FDA Nod for Brain Cancer…](https://www.ibtimes.com.au/telix-pharmaceuticals-shares-jump-7-fda-nod-brain-cancer-imaging-agent-amid-strong-revenue-1866078) · ibtimes.com.au |
| 10 Apr 2026 | telixpharma.com | FDA approval | Telix Pharmaceuticals Ltd (ASX: TLX) led the S&P/ASX 200 gainers Friday with a 3.23 percent surge to $14.08 after the U.S. Food and Drug… | article unavailable |
| 8 Apr 2026 | biocon.com | FDA approval | Biocon: The company launched Bosaya and Aukelso (denosumab-kyqq) in the United States after receiving approval and interchangeable designation from… | article unavailable |
| 8 Apr 2026 | aurobindo.com | FDA approval | The company secured final approval from the US Food and Drug Administration to manufacture and market Dapagliflozin and Metformin hydrochloride… | article unavailable |
| 8 Apr 2026 | bauschsurgical.eu | FDA approval | Today announced that the U.S. Food and Drug Administration has granted 510(k) clearance for the Bi-Blade+ advanced dual-port vitrectomy cutter and… | article unavailable |
| 7 Apr 2026 | alembicpharmaceuticals.com | FDA approval | Alembic Pharmaceuticals has secured final approval from the US Food & Drug Administration (USFDA) for its Abbreviated New Drug Application (ANDA)… | article unavailable |
| 31 Mar 2026 | biogen.co.uk | FDA approval | FDA approves a higher‑dose SPINRAZA regimen, broadening Biogen’s commercial opportunity in spinal muscular atrophy and supporting longer‑term… | [Biogen (NASDAQ:BIIB) Shares Gap Down – Here’s Why](https://www.watchlistnews.com/biogen-nasdaqbiib-shares-gap-down-heres-why/11037781.html) · watchlistnews.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type fda_approval --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type fda_approval --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type fda_approval --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["fda_approval"], "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["fda_approval"], "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Restructuring](restructuring.md)
- [Quarterly Results](quarterly-results.md)
- [Rights Issue](rights-issue.md)
- [AI Layoffs](ai-layoffs.md)
