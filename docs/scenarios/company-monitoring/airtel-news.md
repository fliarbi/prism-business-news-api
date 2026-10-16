# Airtel News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “airtel news” · 6,600/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [airtel-news.json](../../examples/scenarios/airtel-news.json).

**Question.** What has the news reported about Airtel in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `airtel.in`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `airtel.in` |
| Headlines, Jan – Apr 2026 (estimate) | 57 |
| Events, May 2025 – Apr 2026 | 216 |
| Most frequent event types | Earnings (109), Key people (23), Announcement (20) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 16% · 0.0% · 84% of 57 articles |
| Funding records, Jan – Apr 2026 | 1 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 5 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 7 Apr 2026 | [Bharti Airtel shares: JM Financial sees 37% upside; Q4 preview, target price - BusinessToday](https://www.businesstoday.in/markets/stocks/story/bharti-airtel-shares-jm-financial-sees-up-to-37-upside-q4-preview-target-price-524340-2026-04-07) | businesstoday.in | 7 | positive | Earnings |
| 2 Apr 2026 | [Bharti Airtel hits 650 million users, becomes world’s 2nd-largest telecom operator - Yes Punjab News](https://yespunjab.com/bharti-airtel-hits-650-million-users-becomes-worlds-2nd-largest-telecom-operator/) | yespunjab.com | 8 | positive | Announcement |
| 31 Mar 2026 | [Airtel turnaround: How Gopal Vittal rebuilt the telecom giant](https://www.forbesindia.com/article/leadership/gopal-vittals-network-effect-how-he-rewired-bharti-airtel/2992700/1) | forbesindia.com | 8 | negative | Earnings |
| 28 Mar 2026 | [How Sunil Mittal’s Bharti Enterprises is orchestrating a textbook succession - BusinessToday](https://www.businesstoday.in/latest/corporate/story/how-sunil-mittals-bharti-enterprises-is-orchestrating-a-textbook-succession-522833-2026-03-28) | businesstoday.in | 7 | positive | Key people |
| 27 Mar 2026 | [Sunil Bharti Mittal to step down as Airtel Africa Chairman, Gopal Vittal to take charge](https://www.indiatvnews.com/technology/news/sunil-bharti-mittal-to-step-down-as-airtel-africa-chairman-gopal-vittal-to-take-charge-2026-03-27-1035299) | indiatvnews.com | 8 | positive | Key people |
| 12 Mar 2026 | [Airtel calls Rs 15,800 crore from 2021 rights issue](https://www.financialexpress.com/business/news/airtel-calls-rs-15800-crore-from-2021-rights-issue/4170766/) | financialexpress.com | 7 | positive | Capital infusion |
| 10 Mar 2026 | [Airtel expands connectivity in J&K \| Financial Express Mumbai - newspaper -…](https://www.magzter.com/ja/stories/newspaper/Financial-Express-Mumbai/AIRTEL-EXPANDS-CONNECTIVITY-IN-JK) | magzter.com | 7 | positive | Announcement |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 109 |
| Key people | 23 |
| Announcement | 20 |
| M&A | 16 |
| Lawsuit | 10 |
| New product | 10 |
| Contracts | 9 |
| Regulatory | 7 |
| Asset acquisition | 5 |
| Funding round | 4 |
| Capital infusion | 2 |
| Board | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Key people | Announcement | M&A |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 35 | 20 | 0 | 2 | 8 | ████████████████ |
| Jun 2025 | 7 | 2 | 1 | 0 | 0 | ███ |
| Jul 2025 | 7 | 7 | 0 | 0 | 0 | ███ |
| Aug 2025 | 43 | 25 | 2 | 3 | 2 | ████████████████████ |
| Sep 2025 | 6 | 4 | 0 | 0 | 1 | ███ |
| Oct 2025 | 11 | 0 | 1 | 0 | 0 | █████ |
| Nov 2025 | 32 | 20 | 1 | 2 | 3 | ███████████████ |
| Dec 2025 | 17 | 2 | 13 | 1 | 0 | ████████ |
| Jan 2026 | 4 | 2 | 2 | 0 | 0 | ██ |
| Feb 2026 | 39 | 24 | 1 | 3 | 2 | ██████████████████ |
| Mar 2026 | 8 | 2 | 2 | 3 | 0 | ████ |
| Apr 2026 | 7 | 1 | 0 | 6 | 0 | ███ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 5 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 7 Apr 2026 | Earnings | For the quarter ended March 2026, the telecom giant is expected to register a 1.1% quarter-on-quarter (QoQ) growth in its India wireless revenue,… | [Bharti Airtel shares: JM Financial sees 37% upside; Q4 preview,…](https://www.businesstoday.in/markets/stocks/story/bharti-airtel-shares-jm-financial-sees-up-to-37-upside-q4-preview-target-price-524340-2026-04-07) · businesstoday.in |
| 4 Apr 2026 | Announcement | Airtel is also tackling a critical infrastructure challenge for the Nigerian digital economy: reliance on a single international internet gateway.… | article unavailable |
| 4 Apr 2026 | Announcement | Bharti Airtel has become the world's second-largest telecom operator by customer base, reaching 650 million users across its operations in India and… | article unavailable |
| 3 Apr 2026 | Announcement | "Bharti Airtel has achieved a significant milestone, reaching 650 million subscribers worldwide and becoming the second-largest telecom operator… | article unavailable |
| 2 Apr 2026 | Announcement | Bharti Airtel on Thursday announced that it has reached a major milestone of 650 million customers globally, making it the second-largest telecom… | [Bharti Airtel hits 650 million users, becomes world’s 2nd-largest…](https://yespunjab.com/bharti-airtel-hits-650-million-users-becomes-worlds-2nd-largest-telecom-operator/) · yespunjab.com |
| 2 Apr 2026 | Announcement | Bharti Airtel Thursday said it now has 650 million customers across, a milestone that places the telecom operator as the second largest globally by… | article unavailable |
| 2 Apr 2026 | Announcement | Bharti Airtel on Thursday said it has crossed 650 million customers globally, cementing its position as the world’s second-largest telecom operator… | article unavailable |
| 31 Mar 2026 | Earnings | When looking back to FY16—the year before Reliance Jio entered the fray—when Airtel enjoyed a profit of ₹6,893 crore. | [Airtel turnaround: How Gopal Vittal rebuilt the telecom giant](https://www.forbesindia.com/article/leadership/gopal-vittals-network-effect-how-he-rewired-bharti-airtel/2992700/1) · forbesindia.com |
| 28 Mar 2026 | Key people | It was in early 2014 that Kohli stepped down and Christian de Faria took over. | [How Sunil Mittal’s Bharti Enterprises is orchestrating a textbook…](https://www.businesstoday.in/latest/corporate/story/how-sunil-mittals-bharti-enterprises-is-orchestrating-a-textbook-succession-522833-2026-03-28) · businesstoday.in |
| 27 Mar 2026 | Key people | With Sunil Bharti Mittal’s exit, Gopal Vittal will currently be the new executive vice-chairman of Bharti Airtel and will take over as non-executive… | [Sunil Bharti Mittal to step down as Airtel Africa Chairman, Gopal…](https://www.indiatvnews.com/technology/news/sunil-bharti-mittal-to-step-down-as-airtel-africa-chairman-gopal-vittal-to-take-charge-2026-03-27-1035299) · indiatvnews.com |
| 12 Mar 2026 | Capital infusion | Bharti Airtel has called in Rs 15,800 crore from shareholders through the final installment on partly paid shares issued under its 2021 rights… | [Airtel calls Rs 15,800 crore from 2021 rights issue](https://www.financialexpress.com/business/news/airtel-calls-rs-15800-crore-from-2021-rights-issue/4170766/) · financialexpress.com |
| 10 Mar 2026 | Announcement | BHARTI AIRTEL ANNOUNCED on Tuesday the expansion of its network footprint to Marwah, a geographically remote area, in Kishtwar district of Jammu and… | [Airtel expands connectivity in J&K \| Financial Express Mumbai -…](https://www.magzter.com/ja/stories/newspaper/Financial-Express-Mumbai/AIRTEL-EXPANDS-CONNECTIVITY-IN-JK) · magzter.com |

## Funding records, Jan – Apr 2026

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 10 Feb 2026 | Bharti Airtel (airtel.in) | Equity | $1.3B | Qatar Foundation Endowment | — | Bharti Airtel, a leading global telecommunications services provider ... will issue 199,870,006 of its new shares to QFE representing a… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company airtel.in --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company airtel.in --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company airtel.in --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company airtel.in --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$PRISM_BUSINESS_API_BASE/v1/business/companies/airtel.in/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "airtel.in", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Uber News](uber-news.md)
- [IBM News](ibm-news.md)
- [Larsen and Toubro News](larsen-and-toubro-news.md)
- [Salesforce News](salesforce-news.md)
