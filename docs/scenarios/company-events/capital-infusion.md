# Capital Infusion: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “capital infusion” · 260/month India · 1,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [capital-infusion.json](../../examples/scenarios/capital-infusion.json).

**Question.** How many capital infusion events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `capital_infusion`.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 7,958 |
| Companies (with a domain) | 5,544 |
| Source articles | 6,657 |
| Busiest month | Feb 2026 (892 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 4.1% · 0.8% · 95% of 2,541 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 507 | ███████████ |
| Jun 2025 | 569 | █████████████ |
| Jul 2025 | 609 | ██████████████ |
| Aug 2025 | 656 | ███████████████ |
| Sep 2025 | 663 | ███████████████ |
| Oct 2025 | 643 | ██████████████ |
| Nov 2025 | 620 | ██████████████ |
| Dec 2025 | 588 | █████████████ |
| Jan 2026 | 596 | █████████████ |
| Feb 2026 | 892 | ████████████████████ |
| Mar 2026 | 778 | █████████████████ |
| Apr 2026 | 837 | ███████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 5 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | parauco.com | Capital infusion | The company approved an increase in capital of approximately US$ 330 million, intended to finance its robust investment plan from US$ 1,033 million… | [Parque Arauco saca cuentas alegres en el primer trimestre y utilidad…](https://www.df.cl/empresas/retail/parque-arauco-saca-cuentas-alegres-en-el-primer-trimestre-y-utilidad-total) · df.cl |
| 30 Apr 2026 | global.toyota | Capital infusion | with the total investment estimated at around 300 billion yen ($1.91 billion), the report said. | article unavailable |
| 30 Apr 2026 | osaic.com | Capital infusion | Osaic has clinched more than $2 billion in new capital with Bain Capital joining existing investors Ares and Lexington Partners. | [Osaic clinches more than $2 billion in new capital as Bain Capital…](https://www.investmentnews.com/independent-broker-dealers/osaic-clinches-more-than-2-billion-in-new-capital-as-bain-capital-joins-investors/266389) · investmentnews.com |
| 30 Apr 2026 | rivian.com | Capital infusion | DOE will now loan Rivian $4.5 billion, instead of the originally agreed amount of $6.6 billion | [Rivian downsizes new EV factory after Trump’s DOE slashes loan…](https://www.theverge.com/transportation/921585/rivian-georgia-factory-capacity-doe-loan) · theverge.com |
| 30 Apr 2026 | osaic.com | Capital infusion | The deal raises more than $2 billion in fresh capital for Osaic, | [Reverence Capital Partners Closes $2B Osaic Recapitalization](https://www.wealthmanagement.com/ibd-news/reverence-capital-partners-closes-2b-osaic-recapitalization) · wealthmanagement.com |
| 30 Apr 2026 | gm.com | Capital infusion | Toledo Propulsion Systems: This site will see a new $40 million investment to support capacity in 10-speed transmission manufacturing for GM's… | [General Motors announces $830 million investment at Romulus,…](https://www.cbsnews.com/detroit/news/general-motors-830-million-investment-romulus-saginaw-toledo-sites/) · cbsnews.com |
| 30 Apr 2026 | blueowl.com | Capital infusion | $6.1bn raised in the quarter from these investors. | [Blue Owl grows AUM and earnings despite wealth jitters](https://alternativecreditinvestor.com/2026/04/30/blue-owl-grows-aum-and-earnings-despite-wealth-jitters/) · alternativecreditinvestor.com |
| 30 Apr 2026 | viciproperties.com | Capital infusion | This quarter, we announced an expansion of our long-term strategic relationship with Cain and Eldridge Industries by providing a $1.5 billion… | article unavailable |
| 30 Apr 2026 | basf.com | Capital infusion | Continuously at least 1.5 billion euros would be invested annually in the preservation and also new plants in Ludwigshafen, explained the manager. | article unavailable |
| 30 Apr 2026 | arbonis.com | Capital infusion | Arbonis (€50 million from CA, 135 employees) is an entity of the Vinci Group and subsidiary of Vinci Construction (€31.7 billion from CA). | [Le spécialiste de la construction en bois lamellé-collé Arbonis…](https://www.lejournaldesentreprises.com/article/le-specialiste-de-la-construction-en-bois-lamelle-colle-arbonis-construit-une-nouvelle-usine-2142145) · lejournaldesentreprises.com |
| 30 Apr 2026 | ctruh.com | Capital infusion | Ctruh, a Bengaluru-based deep-tech company building the infrastructure layer for the spatial internet, has announced the successful closure of its… | [Ctruh Raises $2.5M to Build Spatial Internet](https://www.passionateinmarketing.com/deep-tech-startup-ctruh-raises-2-5-million-seed-round-to-build-the-infrastructure-layer-of-the-spatial-internet-sets-us-and-uae-launch-for-2026/) · passionateinmarketing.com |
| 30 Apr 2026 | novartis.com | Capital infusion | Novartis to expand in Durham and Wake Counties, adding 700 jobs with a $771 million investment. | [Novartis finalizes new manufacturing facility in Morrisville as part…](https://abc11.com/post/novartis-open-new-drug-manufacturing-facility-morrisville-north-carolina/19005550/) · abc11.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type capital_infusion --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type capital_infusion --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type capital_infusion --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["capital_infusion"], "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["capital_infusion"], "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Bank Results](bank-results.md)
- [SEBI Order](sebi-order.md)
- [Asset Sale](asset-sale.md)
- [CEO Appointment](ceo-appointment.md)
