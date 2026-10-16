# Bonus Issue: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “bonus issue” · 110,000/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [bonus-issue.json](../../examples/scenarios/bonus-issue.json).

**Question.** How many bonus issue events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `company_announcement` and the word “bonus” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 47 |
| Companies (with a domain) | 45 |
| Source articles | 44 |
| Busiest month | Apr 2026 (10 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 3.1% · 3.1% · 94% of 32 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 0 |  |
| Jun 2025 | 2 | ████ |
| Jul 2025 | 5 | ██████████ |
| Aug 2025 | 9 | ██████████████████ |
| Sep 2025 | 5 | ██████████ |
| Oct 2025 | 2 | ████ |
| Nov 2025 | 1 | ██ |
| Dec 2025 | 2 | ████ |
| Jan 2026 | 4 | ████████ |
| Feb 2026 | 3 | ██████ |
| Mar 2026 | 4 | ████████ |
| Apr 2026 | 10 | ████████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 5 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | intesasanpaolo.com | Announcement | According to a calculation by First Cisl, there was an increase in the bonus pool made available by the company, amounting to EUR 177 million, which… | article unavailable |
| 27 Apr 2026 | pearlabyss.com | Announcement | Apparently it doesn’t stop here, either, with another bonus due at the beginning of 2027 based on 2026 financial performance. | [Crimson Desert Has Sold So Well Developer Pearl Abyss Has Reportedly…](https://nordic.ign.com/crimson-desert/106833/crimson-desert-has-sold-so-well-developer-pearl-abyss-has-reportedly-given-every-employee-a-3400-bon) · nordic.ign.com |
| 22 Apr 2026 | samsung.com | Announcement | Samsung Electronics Co. faces an escalating labor battle after its unions raised their bonus demand to 15% of this year’s operating profit, a sum… | [Samsung’s $203 billion question: Who gets what? - KED Global](https://www.kedglobal.com/labor-union/newsView/ked202604220007) · kedglobal.com |
| 21 Apr 2026 | savills.com | Announcement | Post navigation Savills has reported further progress in narrowing its gender pay gap, even as disparities in bonus and ethnicity pay metrics… | [Savills narrows gender pay gap as female representation edges up -…](https://propertyindustryeye.com/savills-narrows-gender-pay-gap-as-female-representation-edges-up/) · propertyindustryeye.com |
| 17 Apr 2026 | vpl.visagar.com | Announcement | 2011 -Visagar Polytex has given the Bonus in the Ratio of 1:1 | article unavailable |
| 17 Apr 2026 | company.co | Announcement | 2015 -The Company has allotted the Bonus Shares to its shareholders in the Ratio of 10:1. | article unavailable |
| 15 Apr 2026 | estithmarholding.com | Announcement | 2025 board report, presented before shareholders at the general assembly meeting, which approved 20% bonus shares. | [Estithmar Holding to expand global presence and build sustainable…](https://www.zawya.com/en/business/investment/estithmar-holding-to-expand-global-presence-and-build-sustainable-institutional-value-rlx3j89f) · zawya.com |
| 7 Apr 2026 | starbucks.in | Announcement | When combined with the new bonus structure, Starbucks estimates that some baristas could see their total pay increase by as much as 8%. | [Starbucks Announces Barista Bonuses and Weekly Pay in Turnaround…](https://time.news/starbucks-announces-barista-bonuses-and-weekly-pay-in-turnaround-effort/) · time.news |
| 2 Apr 2026 | starbucks.com | Announcement | Scheduled for rollout in July 2026, the program introduces a new store performance-based bonus structure. Baristas and shift supervisors can now… | [Starbucks launching new employee rewards program](https://chainstoreage.com/starbucks-launching-new-employee-rewards-program) · chainstoreage.com |
| 2 Apr 2026 | bydglobal.com | Announcement | The Chinese are now launching the next round and extending their 'E-Bonus' until the end of June 2026. | [BYD verlängert „E-Bonus“-Aktion in Deutschland bis Ende Juni -…](https://www.electrive.net/2026/04/02/byd-verlaengert-e-bonus-aktion-in-deutschland-bis-ende-juni/) · electrive.net |
| 26 Mar 2026 | britishairways.com | Announcement | The airline's pilots would have to cut their aircraft's carbon dioxide emissions by 60,000 tons more than their 2025 levels to receive a bonus worth… | article unavailable |
| 23 Mar 2026 | timesgreenenergy.com | Announcement | Times Green Energy (India) Ltd Bonus Issue1:1 | [Dividends, Bonus, Stock Splits and Rights Issues This Week (March…](https://www.angelone.in/news/market-updates/dividends-bonus-stock-splits-and-rights-issues-this-week-march-23-27-2026-castrol-india-vedanta-and-more) · angelone.in |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type company_announcement --q bonus --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type company_announcement --q bonus --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type company_announcement --q bonus --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["company_announcement"], "q": "bonus", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["company_announcement"], "q": "bonus", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Lawsuit](lawsuit.md)
- [Stock Split](stock-split.md)
- [Class Action Lawsuit](class-action-lawsuit.md)
- [Fundraise](fundraise.md)
