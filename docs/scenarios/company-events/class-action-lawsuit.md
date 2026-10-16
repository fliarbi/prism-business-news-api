# Class Action Lawsuit: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “class action lawsuit” · 1,600/month India · 90,500/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [class-action-lawsuit.json](../../examples/scenarios/class-action-lawsuit.json).

**Question.** How many class action lawsuit events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `lawsuit` and the word “class action” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 596 |
| Companies (with a domain) | 269 |
| Source articles | 433 |
| Busiest month | Feb 2026 (111 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 91% · 1.3% · 7.8% of 230 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 30 | █████ |
| Jun 2025 | 20 | ████ |
| Jul 2025 | 47 | ████████ |
| Aug 2025 | 15 | ███ |
| Sep 2025 | 31 | ██████ |
| Oct 2025 | 34 | ██████ |
| Nov 2025 | 81 | ███████████████ |
| Dec 2025 | 35 | ██████ |
| Jan 2026 | 26 | █████ |
| Feb 2026 | 111 | ████████████████████ |
| Mar 2026 | 69 | ████████████ |
| Apr 2026 | 97 | █████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 6 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | jindalpoly.com | Lawsuit | The National Company Law Tribunal’s (NCLT) special bench on Thursday directed listing the class action lawsuit against Jindal Poly Films before the… | [NCLT to hear class action suit against Jindal Poly on May 7](https://www.financialexpress.com/business/news/nclt-to-hear-class-action-suit-against-jindal-poly-on-may-7/4223512/) · financialexpress.com |
| 30 Apr 2026 | amazon.com | Lawsuit | The class action lawsuit argued that Amazon did not give those mandatory breaks to hourly employees in Washington state, as required by state law. | article unavailable |
| 28 Apr 2026 | hbsslaw.com | Lawsuit | A securities class action lawsuit has been filed against China’s largest online travel agency, Trip.com Group. | [SAN FRANCISCO, April 28, 2026 (GLOBE NEWSWIRE) -- A securities class…](https://www.advertisingtoday.com/article/908859617-investor-deadline-trip-com-group-tcom-investors-with-substantial-losses-have-opportunity-to-lead-the-trip-com-class-action-lawsuit-hagens-berman) · advertisingtoday.com |
| 26 Apr 2026 | pomerantzlaw.com | Lawsuit | On April 25, 2026, Pomerantz LLP, a prominent law firm known for its work in securities class actions and corporate governance, announced the filing… | article unavailable |
| 26 Apr 2026 | babcock.com | Lawsuit | On April 25, 2026, Pomerantz LLP, a prominent law firm known for its work in securities class actions and corporate governance, announced the filing… | article unavailable |
| 25 Apr 2026 | drivenbrands.com | Lawsuit | Kahn Swick & Foti, LLC announced the initiation of a significant securities fraud class action lawsuit against Driven Brands Holdings Inc. | [Understanding the Driven Brands Holdings Inc. Securities Fraud Class…](https://www.theedadvocate.org/understanding-the-driven-brands-holdings-inc-securities-fraud-class-action-implications-and-investor-insights/) · theedadvocate.org |
| 23 Apr 2026 | nintendo.com | Lawsuit | Nintendo fans in the US have filed a class action lawsuit against the Switch manufacturer. | [Nintendo under pressure: Switch players want their money back -…](https://www.gamingdeputy.com/nintendo-under-pressure-switch-players-want-their-money-back/) · gamingdeputy.com |
| 23 Apr 2026 | stellantis.com | Lawsuit | several US law firms have filed a class action. | [Stellantis: Juni-Deadline für Klage-Anmeldung](https://www.boerse-express.com/news/articles/stellantis-juni-deadline-fuer-klage-anmeldung-896373) · boerse-express.com |
| 23 Apr 2026 | lnw.com | Lawsuit | Gaming supplier Light & Wonder Inc has been served with a class action lawsuit in Australia linked to disclosures regarding its “Dragon Train” game,… | article unavailable |
| 22 Apr 2026 | jameshardie.com | Lawsuit | Slater and Gordon is investigating a potential shareholder class action against James Hardie Industries plc in relation to its 1Q FY26 results and… | [Slater and Gordon announces James Hardie Shareholder Investigation](https://www.nationaltribune.com.au/slater-and-gordon-announces-james-hardie-shareholder-investigation/) · nationaltribune.com.au |
| 21 Apr 2026 | drivenbrands.com | Lawsuit | Driven Brands Holdings Inc. (NASDAQ: DRVN) finds itself embroiled in a class action lawsuit that accuses the company and its senior executives of… | [Driven Brands Faces Securities Fraud Allegations Amidst Financial…](https://www.theedadvocate.org/driven-brands-faces-securities-fraud-allegations-amidst-financial-restatements/) · theedadvocate.org |
| 21 Apr 2026 | taylor.solar | Lawsuit | A separate securities class action, Taylor v. Hercules Capital, Inc., No. 3:26-cv-02465 (N.D. Cal.), is already pending. | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type lawsuit --q "class action" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type lawsuit --q "class action" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type lawsuit --q "class action" --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["lawsuit"], "q": "class action", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["lawsuit"], "q": "class action", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Stock Split](stock-split.md)
- [Bonus Issue](bonus-issue.md)
- [Fundraise](fundraise.md)
- [Bank Mergers News](bank-mergers-news.md)
