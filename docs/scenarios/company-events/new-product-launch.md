# New Product Launch: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “new product launch” · 1,900/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [new-product-launch.json](../../examples/scenarios/new-product-launch.json).

**Question.** How many new product launch events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `new_product`.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 11,446 |
| Companies (with a domain) | 5,872 |
| Source articles | 10,475 |
| Busiest month | Apr 2026 (1,258 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 1.2% · 0.2% · 99% of 3,828 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 841 | █████████████ |
| Jun 2025 | 727 | ████████████ |
| Jul 2025 | 771 | ████████████ |
| Aug 2025 | 873 | ██████████████ |
| Sep 2025 | 1,038 | █████████████████ |
| Oct 2025 | 1,145 | ██████████████████ |
| Nov 2025 | 984 | ████████████████ |
| Dec 2025 | 742 | ████████████ |
| Jan 2026 | 838 | █████████████ |
| Feb 2026 | 1,112 | ██████████████████ |
| Mar 2026 | 1,117 | ██████████████████ |
| Apr 2026 | 1,258 | ████████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 7 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | vocus.com | New product | Vocus' newly launched partner program offers technology solution providers access to its legacy and TPG networks along with a range of benefits. | [Vocus partner program to tap into legacy networks](https://www.arnnet.com.au/article/4165288/vocus-partner-program-to-tap-into-legacy-networks.html) · arnnet.com.au |
| 30 Apr 2026 | innovmetric.com | New product | InnovMetric, an independent software development company, has launched PolyWorks® 2026. | article unavailable |
| 30 Apr 2026 | antintl.com | New product | Ant International CEO Peng Yang shares the company’s global strategy for the era of AI commerce and launches its open-sourced Agentic Mobile… | [Expanding infrastructure for the age of AI commerce: Ant…](https://www.fintechnews.org/expanding-infrastructure-for-the-age-of-ai-commerce-ant-international-connects-over-150-million-merchants-with-more-than-2-billion-consumers/) · fintechnews.org |
| 30 Apr 2026 | microsoft.com | New product | Microsoft packages AI, identity, and security together Microsoft appears to be focused on building an all-in-one platform for AI services, recently… | article unavailable |
| 30 Apr 2026 | cloud.google.com | New product | Google Cloud is taking a more partner-led approach, expanding partner capacity and reducing regional barriers so customers can scale AI deployments… | article unavailable |
| 30 Apr 2026 | apollo-oe.com | New product | Apollo Launches Int’l Casualty Reinsurance Business, Led by Berkley Re’s Mackenzie Apollo, the London-based subsidiary of Skyward Group, announced… | [People Moves: Apollo Launches Int'l Casualty Reinsurance Business,…](https://www.insurancejournal.com/news/international/2026/04/30/867927.htm) · insurancejournal.com |
| 30 Apr 2026 | hyundaimotorgroup.com | New product | SEOUL, April 29, 2026 – Hyundai Motor Group (the Group) today unveiled Pleos Connect, a next‑generation in‑vehicle infotainment system designed to… | [Hyundai Motor Group redefines in-vehicle experience with ‘Pleos…](https://www.cbtnews.com/hmg-redefines-experience-with-pleos-connect/) · cbtnews.com |
| 30 Apr 2026 | bi.go.id | New product | Prior to China, BI had also launched QRIS usage in South Korea on April 1. | article unavailable |
| 30 Apr 2026 | superagent.com | New product | SUPERAGENT AI, Inc. today announced the general availability of SUPERAGENT 2.0, a comprehensive platform update that transitions the software from… | [SUPERAGENT AI Unveils Platform 2.0, Delivering a Unified Autonomous…](https://globalfintechseries.com/insurtech/superagent-ai-unveils-platform-2-0-delivering-a-unified-autonomous-workforce-for-independent-insurance-agencies/) · globalfintechseries.com |
| 30 Apr 2026 | hyperionmt.com | New product | Hyperion Intelligence Inc. (“Hyperion”) today debuted FairMarketValue, an A.I. enabled financial intelligence platform that streamlines how… | article unavailable |
| 30 Apr 2026 | international-motors.de | New product | International Motors is rolling out a new connected digital ecosystem designed to bring fleet operations, vehicle health, and dealer communication… | [International Debuts ‘My International’ Connected Platform to…](http://www.truckinginfo.com/news/international-debuts-my-international-connected-platform-to-centralize-fleet-data-service-and-dealer-communication) · truckinginfo.com |
| 30 Apr 2026 | medcaretechinc.com | New product | MESA, AZ / ACCESS Newswire / April 30, 2026 / Medical Care Technologies Inc. (OTCID:MDCE) ("the Company") today announced the launch of its newly… | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type new_product --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type new_product --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type new_product --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["new_product"], "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["new_product"], "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Strategic Partnership](strategic-partnership.md)
- [It Layoffs](it-layoffs.md)
- [Dividend Announcement](dividend-announcement.md)
- [AI Partnership](ai-partnership.md)
