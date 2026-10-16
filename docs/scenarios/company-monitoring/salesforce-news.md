# Salesforce News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “salesforce news” · 1,300/month India · 5,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [salesforce-news.json](../../examples/scenarios/salesforce-news.json).

**Question.** What has the news reported about Salesforce in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `salesforce.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `salesforce.com` |
| Headlines, Jan – Apr 2026 (estimate) | 2,403 |
| Events, May 2025 – Apr 2026 | 200 |
| Most frequent event types | Earnings (55), New product (39), M&A (23) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 20% · 0.4% · 79% of 2,403 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 4 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Eli Lilly (LLY) Q1 2026 Earnings Transcript \| The Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/04/30/eli-lilly-lly-q1-2026-earnings-transcript/) | fool.com | 7 | positive | Earnings |
| 30 Apr 2026 | [Marketplace Briefing: Amazon joins Google-backed shopping effort, suggesting a shift in AI strategy](https://www.modernretail.co/technology/marketplace-briefing-amazon-joins-google-backed-shopping-effort-suggesting-a-shift-in-ai-strategy/) | modernretail.co | 7 | positive | — |
| 30 Apr 2026 | [Call Center AI Market is expected to Hit US$ 12.7 billion by 2033 \| Major Companies - IBM, Microsoft, AWS,…](https://www.openpr.com/news/4496954/call-center-ai-market-is-expected-to-hit-us-12-7-billion-by-2033) | openpr.com | 8 | positive | — |
| 30 Apr 2026 | [Dreamteam AI CRM startup eyes $40 Mn in Series A funding, targets disruption in global SaaS market \|…](https://businessreviewlive.com/dreamteam-ai-crm-startup-eyes-40-mn-in-series-a-funding-targets-disruption-in-global-saas-market/) | businessreviewlive.com | 8 | positive | Funding round |
| 30 Apr 2026 | [Amazon Web Service Does an Agentic Shift into the Application Layer](https://cxotoday.com/research/amazon-web-service-does-an-agentic-shift-into-the-application-layer/) | cxotoday.com | 8 | positive | — |
| 30 Apr 2026 | [LinkedIn's New CEO Just Disclosed a Number Microsoft Never Has. Here's Why That's the Real Story.](https://startupnews.fyi/ai-deeptech/linkedin-s-new-ceo-just-disclosed-a-number-microsoft-never) | startupnews.fyi | 8 | negative | Earnings |
| 30 Apr 2026 | [Gentrack’s Veovo to acquire Dubai Technology Partners for $10mn - NewsnReleases](https://newsnreleases.com/2026/04/30/gentracks-veovo-acquire-dubai-technology-partners/) | newsnreleases.com | 7 | positive | M&A |
| 29 Apr 2026 | [Amazon’s OpenAI gambit signals a new phase in the cloud wars — one where exclusivity no longer applies](https://www.venturebeat.com/technology/amazons-openai-gambit-signals-a-new-phase-in-the-cloud-wars-one-where-exclusivity-no-longer-applies) | venturebeat.com | 8 | positive | New product |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 55 |
| New product | 39 |
| M&A | 23 |
| Key people | 22 |
| Announcement | 19 |
| Contracts | 13 |
| Layoffs | 13 |
| Buyback | 7 |
| Job creation | 5 |
| Asset acquisition | 2 |
| Regulatory | 1 |
| Capital infusion | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | New product | M&A | Key people |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 21 | 6 | 1 | 10 | 0 | █████████████ |
| Jun 2025 | 12 | 1 | 6 | 3 | 0 | ████████ |
| Jul 2025 | 6 | 0 | 4 | 0 | 0 | ████ |
| Aug 2025 | 14 | 0 | 3 | 3 | 4 | █████████ |
| Sep 2025 | 24 | 13 | 2 | 0 | 0 | ███████████████ |
| Oct 2025 | 20 | 2 | 7 | 2 | 1 | ████████████ |
| Nov 2025 | 13 | 2 | 2 | 3 | 0 | ████████ |
| Dec 2025 | 27 | 13 | 7 | 1 | 3 | █████████████████ |
| Jan 2026 | 9 | 0 | 1 | 0 | 4 | ██████ |
| Feb 2026 | 32 | 15 | 2 | 1 | 6 | ████████████████████ |
| Mar 2026 | 13 | 1 | 2 | 0 | 2 | ████████ |
| Apr 2026 | 9 | 2 | 2 | 0 | 2 | ██████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 6 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 28 Apr 2026 | Contracts | Salesforce today announced that Moderna has selected Salesforce’s Agentforce Life Sciences for Customer Engagement to unify the biotechnology… | [Salesforce Agentforce Life Sciences to Unify Moderna’s Global…](https://www.salesforce.com/au/news/press-releases/2026/04/28/salesforce-agentforce-life-sciences-unify-moderna-global-commercial-operations/) · salesforce.com |
| 23 Apr 2026 | Earnings | During the fourth quarter of 2026, Salesforce delivered $11.2 billion in top-line results, marking 12% annual expansion. | article unavailable |
| 21 Apr 2026 | Key people | Nadia Bischof, former head of Matrix42 Switzerland and last of servicenow, has taken over a new position at Salesforce. | article unavailable |
| 20 Apr 2026 | Contracts | Chiesi Group, an international biopharmaceutical group, has selected Salesforce’s Agentforce Life Sciences for Customer Engagement to transform its… | [Chiesi Group Selects Salesforce Agentforce Life Sciences to…](https://www.salesforce.com/news/press-releases/2026/04/20/chiesi-group-agentforce-life-sciences-transforms-customer-engagement/) · salesforce.com |
| 15 Apr 2026 | Key people | Collins runs Salesforce’s Government Cloud, which is the company’s portfolio of products for governments around the world. He was previously the… | article unavailable |
| 15 Apr 2026 | New product | Salesforce has added a new LLM Governance capability in AI Gateway, the control layer within Agent Fabric that provides centralized visibility of… | [MuleSoft Agent Fabric adds new ways to keep AI agents in line](https://www.cio.com/article/4159235/mulesoft-agent-fabric-adds-new-ways-to-keep-ai-agents-in-line-2.html) · cio.com |
| 15 Apr 2026 | New product | Salesforce is also adding new Model Control Protocol features, including MCP Bridge to make it easier to access legacy APIs. | article unavailable |
| 7 Apr 2026 | Earnings | The CRM provider reported $3.81 earnings per share (EPS) for the quarter, topping the consensus estimate of $3.05 by $0.76. | [Salesforce Inc. (CRM) to Issue Quarterly Dividend of $0.44 on April…](https://www.themarketsdaily.com/2026/04/07/salesforce-inc-crm-to-issue-quarterly-dividend-of-0-44-on-april-23rd.html) · themarketsdaily.com |
| 7 Apr 2026 | Layoffs | Epic Games, a video game and software company, and Salesforce, a cloud-based software company, announced layoffs of 1,000 and 1,500 respectively,… | [Oracle, Amazon, Dell lead global job cuts amid AI push](https://telanganatoday.com/oracle-amazon-dell-lead-global-job-cuts-amid-ai-push) · telanganatoday.com |
| 29 Mar 2026 | Buyback | Of the approved volume, USD 25 billion is immediately being invested in an accelerated buyback, which was launched at the end of March. | [Salesforce Aktie: Milliarden für Aktionäre](https://www.boerse-express.com/news/articles/salesforce-aktie-milliarden-fuer-aktionaere-885198) · boerse-express.com |
| 26 Mar 2026 | Buyback | Over the past three fiscal years, Salesforce repurchased $7.6 billion, $7.8 billion, and $12.6 billion of stock, respectively. | article unavailable |
| 24 Mar 2026 | Key people | Mike Wolff – GTM and revenue leader with deep expertise in scaling global sales organizations, technology partnerships, and customer success.… | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company salesforce.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company salesforce.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company salesforce.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company salesforce.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$PRISM_BUSINESS_API_BASE/v1/business/companies/salesforce.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "salesforce.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.
- Zero-count periods are included; partial_period marks buckets only partly covered by the window.
- shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)

## Related demonstrations

- [Airtel News](airtel-news.md)
- [Larsen and Toubro News](larsen-and-toubro-news.md)
- [Coal India News](coal-india-news.md)
- [Paypal News](paypal-news.md)
