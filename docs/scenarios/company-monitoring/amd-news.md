# AMD News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “amd news” · 22,200/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [amd-news.json](../../examples/scenarios/amd-news.json).

**Question.** What has the news reported about AMD in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `amd.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `amd.com` |
| Headlines, Jan – Apr 2026 (estimate) | 52 |
| Events, May 2025 – Apr 2026 | 152 |
| Most frequent event types | Earnings (43), Contracts (37), Key people (30) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 3.9% · 3.9% · 92% of 52 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 5 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [AMD Appoints Vinay Awasthi as SVP, Asia Pacific, Japan and India (APJ) Sales](https://digitalterminal.in/tech-companies/amd-appoints-vinay-awasthi-as-svp-asia-pacific-japan-and-india-apj-sales) | digitalterminal.in | 7 | positive | Key people |
| 28 Apr 2026 | [People Moves in the Channel](https://newsinthechannel.co.uk/people-moves-in-the-channel-73/) | newsinthechannel.co.uk | 3 | positive | Key people |
| 24 Apr 2026 | [Vinay Awasthi Joins AMD as SVP – Asia Pacific, Japan & India Sales - Global HR News & Updates](https://hrtoday.in/vinay-awasthi-joins-amd-as-svp-asia-pacific-japan-india-sales/) | hrtoday.in | 5 | positive | Key people |
| 11 Apr 2026 | [NVIDIA vs AMD 2026: AI Chip Showdown – Who Dominates Data Centers as Blackwell and MI400 Battle?](https://www.ibtimes.com.au/nvidia-vs-amd-2026-ai-chip-showdown-who-dominates-data-centers-blackwell-mi400-battle-1866177) | ibtimes.com.au | 8 | positive | Earnings |
| 26 Mar 2026 | [Trump names new White House council to help 'the Golden Age of Innovation'](https://www.yahoo.com/news/articles/trump-names-white-house-council-122500726.html) | yahoo.com | 8 | positive | Key people |
| 25 Mar 2026 | [Trump Names Jensen Huang, Mark Zuckerberg To AI Advisory Council: What It Means For NVDA, META - Meta Pla](https://www.benzinga.com/markets/prediction-markets/26/03/51464497/trump-names-jensen-huang-mark-zuckerberg-to-ai-advisory-council) | benzinga.com | 8 | positive | Key people |
| 16 Mar 2026 | [AMD Stock Heads for $200 on Regulatory Relief and Samsung Foundry Talks](https://www.fxleaders.com/news/2026/03/16/amd-stock-heads-for-200-on-regulatory-relief-and-samsung-foundry-talks/) | fxleaders.com | 8 | positive | Regulatory |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 43 |
| Contracts | 37 |
| Key people | 30 |
| M&A | 16 |
| Regulatory | 10 |
| Announcement | 7 |
| Asset acquisition | 3 |
| Lawsuit | 3 |
| Buyback | 3 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Contracts | Key people | M&A |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 23 | 8 | 4 | 3 | 4 | ██████████████ |
| Jun 2025 | 5 | 1 | 2 | 0 | 2 | ███ |
| Jul 2025 | 4 | 0 | 0 | 0 | 0 | ██ |
| Aug 2025 | 22 | 9 | 3 | 5 | 0 | █████████████ |
| Sep 2025 | 2 | 0 | 0 | 0 | 1 | █ |
| Oct 2025 | 16 | 1 | 11 | 0 | 2 | ██████████ |
| Nov 2025 | 25 | 6 | 7 | 7 | 1 | ███████████████ |
| Dec 2025 | 6 | 0 | 3 | 0 | 0 | ████ |
| Jan 2026 | 6 | 3 | 0 | 2 | 1 | ████ |
| Feb 2026 | 33 | 14 | 7 | 6 | 4 | ████████████████████ |
| Mar 2026 | 5 | 0 | 0 | 4 | 0 | ███ |
| Apr 2026 | 5 | 1 | 0 | 3 | 1 | ███ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 4 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Key people | AMD has announced the appointment of Vinay Awasthi as Senior Vice President, Asia Pacific, Japan and India (APJ) Sales | [AMD Appoints Vinay Awasthi as SVP, Asia Pacific, Japan and India…](https://digitalterminal.in/tech-companies/amd-appoints-vinay-awasthi-as-svp-asia-pacific-japan-and-india-apj-sales) · digitalterminal.in |
| 28 Apr 2026 | Key people | Megan Fernandes is now a Senior Channel Marketing Specialist at AMD. | [People Moves in the Channel](https://newsinthechannel.co.uk/people-moves-in-the-channel-73/) · newsinthechannel.co.uk |
| 24 Apr 2026 | Key people | Vinay Awasthi has joined AMD as Senior Vice President – Asia Pacific, Japan & India (APJ) Sales, where he will lead the company's regional sales… | [Vinay Awasthi Joins AMD as SVP – Asia Pacific, Japan & India Sales -…](https://hrtoday.in/vinay-awasthi-joins-amd-as-svp-asia-pacific-japan-india-sales/) · hrtoday.in |
| 16 Apr 2026 | M&A | Border to Coast Pensions Partnership Ltd purchased a new stake in Advanced Micro Devices, Inc. (NASDAQ:AMD – Free Report) in the fourth quarter,… | article unavailable |
| 11 Apr 2026 | Earnings | AMD, meanwhile, posted full-year 2025 Data Center revenue of $16.64 billion, up 32%, and expects continued strong growth in 2026 fueled by its… | [NVIDIA vs AMD 2026: AI Chip Showdown – Who Dominates Data Centers as…](https://www.ibtimes.com.au/nvidia-vs-amd-2026-ai-chip-showdown-who-dominates-data-centers-blackwell-mi400-battle-1866177) · ibtimes.com.au |
| 26 Mar 2026 | Key people | Among its members are Nvidia CEO Jensen Huang, AMD CEO Lisa Su, Meta CEO Mark Zuckerberg, Oracle executive chairman Larry Ellison, Dell co-founder… | [Trump names new White House council to help 'the Golden Age of…](https://www.yahoo.com/news/articles/trump-names-white-house-council-122500726.html) · yahoo.com |
| 25 Mar 2026 | Key people | Advanced Micro Devices Inc. (NASDAQ:AMD) CEO Lisa Su. | [Trump Names Jensen Huang, Mark Zuckerberg To AI Advisory Council:…](https://www.benzinga.com/markets/prediction-markets/26/03/51464497/trump-names-jensen-huang-mark-zuckerberg-to-ai-advisory-council) · benzinga.com |
| 25 Mar 2026 | Key people | Google co-founder Sergey Brin and AMD CEO Lisa Su are also part of the initial batch of 13 members from the industry named to the President's… | article unavailable |
| 25 Mar 2026 | Key people | The 13 initial appointees also include Oracle founder Larry Ellison, Google co-founder Sergey Brin, AMD CEO Lisa Su, and Dell Technologies CEO… | article unavailable |
| 16 Mar 2026 | Regulatory | Policymakers withdrew a proposed global licensing rule that would have restricted exports of advanced AI chips. The decision removes a potential… | [AMD Stock Heads for $200 on Regulatory Relief and Samsung Foundry…](https://www.fxleaders.com/news/2026/03/16/amd-stock-heads-for-200-on-regulatory-relief-and-samsung-foundry-talks/) · fxleaders.com |
| 28 Feb 2026 | Earnings | AMD posted solid Q4FY25 revenue of $10.3 billion, reflecting 34% year-over-year growth, with adjusted EPS of $1.53 exceeding analyst expectations. | article unavailable |
| 27 Feb 2026 | Contracts | Meta is investing in 6 gigawatts of AMD computing power, worth about $100 billion over five years, to build AI capabilities. | [Meta Inks Multi-Billion AI Chip Deal with Google after Nvidia and…](https://www.tipranks.com/news/meta-inks-multi-billion-ai-chip-deal-with-google-after-nvidia-and-amd-pacts) · tipranks.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company amd.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company amd.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company amd.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company amd.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/amd.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "amd.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Hdfc Bank News](hdfc-bank-news.md)
- [Oracle News](oracle-news.md)
- [Anthropic News](anthropic-news.md)
- [Microsoft News](microsoft-news.md)
