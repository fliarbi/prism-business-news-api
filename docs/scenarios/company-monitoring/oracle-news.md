# Oracle News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “oracle news” · 8,100/month India · 14,800/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [oracle-news.json](../../examples/scenarios/oracle-news.json).

**Question.** What has the news reported about Oracle in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `oracle.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `oracle.com` |
| Headlines, Jan – Apr 2026 (estimate) | 160 |
| Events, May 2025 – Apr 2026 | 439 |
| Most frequent event types | Earnings (101), Key people (72), Layoffs (56) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 43% · 1.3% · 56% of 160 articles |
| Funding records, Jan – Apr 2026 | 4 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 3 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 27 Apr 2026 | [New types of downsizing: AI layoffs in the tech industry surge past 39,000](https://www.digitaljournal.com/business/new-types-of-downsizing-ai-layoffs-in-the-tech-industry-surge-past-39000/article) | digitaljournal.com | 8 | negative | Layoffs |
| 22 Apr 2026 | [Deutsche Regierung nutzt für Milliarden Lizenzen von US-Techkonzernen](https://www.derstandard.de/story/3000000317680/deutsche-regierung-nutzt-fuer-milliarden-lizenzen-von-us-techkonzernen) | derstandard.de | 7 | neutral | Contracts |
| 19 Apr 2026 | [Over 73,200 IT layoffs recorded in first 3 months of 2026 - The Statesman](https://www.thestatesman.com/business/over-73200-it-layoffs-recorded-in-first-3-months-of-2026-1503583644.html) | thestatesman.com | 7 | negative | Layoffs |
| 17 Apr 2026 | [Global tech layoffs hit 80,000 in Q1, tally may cross 3 lakh this year: Report - www.lokmattimes.com](https://www.lokmattimes.com/technology/global-tech-layoffs-hit-80000-in-q1-tally-may-cross-3-lakh-this-year-report-1/) | lokmattimes.com | 8 | negative | Layoffs |
| 17 Apr 2026 | [तकनीकी दुनिया में कोहराम! 3 महीने में 80,000 नौकरियां खत्म, क्या आपकी जॉब भी खतरे में है?](https://www.etvbharat.com/hi/business/global-tech-layoffs-hit-80000-in-q1-may-surpass-3-lakh-this-year-hin26041703317) | etvbharat.com | 7 | positive | Announcement |
| 17 Apr 2026 | [Global tech layoffs hit 80,000 in Q1, tally may cross 3 lakh this year: Report - Social News XYZ](https://www.socialnews.xyz/2026/04/17/global-tech-layoffs-hit-80000-in-q1-tally-may-cross-3-lakh-this-year-report/) | socialnews.xyz | 8 | negative | Layoffs |
| 14 Apr 2026 | [Oracle sobe pelo 2º dia e Bloom Energy dispara 20% - SpaceMoney](https://www.spacemoney.com.br/economia/exterior/oracle-sobe-bloom-energy-dispara-20-acordo-energia-data-center-ia-3/) | spacemoney.com.br | 6 | positive | Contracts |
| 14 Apr 2026 | [Bloom Energy spikes after vastly expanding its deal to supply fuel cells to Oracle](https://sherwood.news/markets/bloom-energy-spikes-expanding-fuel-cell-power-deal-oracle-warrants/) | sherwood.news | 7 | positive | Contracts |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 101 |
| Key people | 72 |
| Layoffs | 56 |
| Contracts | 55 |
| New product | 55 |
| Announcement | 29 |
| Lawsuit | 27 |
| Capital infusion | 11 |
| Asset acquisition | 9 |
| M&A | 8 |
| Funding round | 7 |
| Job creation | 4 |
| Regulatory | 3 |
| IPO | 1 |
| Buyback | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | Key people | Layoffs | Contracts |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 6 | 0 | 0 | 0 | 1 | █ |
| Jun 2025 | 21 | 17 | 3 | 0 | 1 | ███ |
| Jul 2025 | 17 | 3 | 0 | 0 | 6 | ███ |
| Aug 2025 | 34 | 4 | 2 | 10 | 3 | ██████ |
| Sep 2025 | 122 | 26 | 41 | 13 | 19 | ████████████████████ |
| Oct 2025 | 32 | 6 | 0 | 0 | 6 | █████ |
| Nov 2025 | 10 | 1 | 2 | 1 | 2 | ██ |
| Dec 2025 | 37 | 24 | 1 | 0 | 3 | ██████ |
| Jan 2026 | 15 | 0 | 4 | 3 | 3 | ██ |
| Feb 2026 | 38 | 0 | 1 | 3 | 2 | ██████ |
| Mar 2026 | 40 | 16 | 6 | 3 | 1 | ███████ |
| Apr 2026 | 67 | 4 | 12 | 23 | 8 | ███████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 2 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 27 Apr 2026 | Layoffs | The largest contributor to these reductions is the U.S. technology giant Oracle (25,254 layoffs). | [New types of downsizing: AI layoffs in the tech industry surge past…](https://www.digitaljournal.com/business/new-types-of-downsizing-ai-layoffs-in-the-tech-industry-surge-past-39000/article) · digitaljournal.com |
| 22 Apr 2026 | Contracts | Oracle is the leading Oracle company with a total volume of 4.69 billion euros. | [Deutsche Regierung nutzt für Milliarden Lizenzen von US-Techkonzernen](https://www.derstandard.de/story/3000000317680/deutsche-regierung-nutzt-fuer-milliarden-lizenzen-von-us-techkonzernen) · derstandard.de |
| 22 Apr 2026 | Contracts | IT framework agreements of the Oracle is the leader with a total volume of 4.69 billion euros | article unavailable |
| 19 Apr 2026 | Layoffs | Oracle Corporation is also undertaking one of the largest restructuring drives. It has rolled out plans to cut between 20,000 and 30,000 jobs… | [Over 73,200 IT layoffs recorded in first 3 months of 2026 - The…](https://www.thestatesman.com/business/over-73200-it-layoffs-recorded-in-first-3-months-of-2026-1503583644.html) · thestatesman.com |
| 17 Apr 2026 | Layoffs | Oracle has reported the highest number of layoffs globally in 2026, cutting more than 25,000 roles as part of a major restructuring tied to its AI… | [Global tech layoffs hit 80,000 in Q1, tally may cross 3 lakh this…](https://www.lokmattimes.com/technology/global-tech-layoffs-hit-80000-in-q1-tally-may-cross-3-lakh-this-year-report-1/) · lokmattimes.com |
| 17 Apr 2026 | Announcement | ORACLE STRENGTHENS ITS AI INFRASTRUCTURE | [तकनीकी दुनिया में कोहराम! 3 महीने में 80,000 नौकरियां खत्म, क्या…](https://www.etvbharat.com/hi/business/global-tech-layoffs-hit-80000-in-q1-may-surpass-3-lakh-this-year-hin26041703317) · etvbharat.com |
| 14 Apr 2026 | Contracts | Oracle confirmed the expansion of the energy capacity agreement with the company. | [Oracle sobe pelo 2º dia e Bloom Energy dispara 20% - SpaceMoney](https://www.spacemoney.com.br/economia/exterior/oracle-sobe-bloom-energy-dispara-20-acordo-energia-data-center-ia-3/) · spacemoney.com.br |
| 14 Apr 2026 | Contracts | the company expanded an energy supply contract with Bloom Energy, specialized in fuel cells for data centers. | [Oracle sobe pelo 2º dia e Bloom Energy dispara 20% - SpaceMoney](https://www.spacemoney.com.br/economia/exterior/oracle-sobe-bloom-energy-dispara-20-acordo-energia-data-center-ia/) · spacemoney.com.br |
| 14 Apr 2026 | Contracts | a filing showed that Oracle received warrants to buy 3.53 million shares of Bloom Energy for $113.28 apiece on April 9, as part of an agreement… | article unavailable |
| 14 Apr 2026 | Contracts | In concert with this announcement, a filing showed that Oracle received warrants to buy 3.53 million shares of Bloom Energy for $113.28 apiece on… | [Bloom Energy spikes after vastly expanding its deal to supply fuel…](https://sherwood.news/markets/bloom-energy-spikes-expanding-fuel-cell-power-deal-oracle-warrants/) · sherwood.news |
| 14 Apr 2026 | Announcement | Oracle launched a new public cloud region in Casablanca, Morocco. | [Oracle Surges 13% as AI Announcements Spark Broad Software Rally](https://www.fxleaders.com/news/2026/04/14/oracle-surges-13-as-ai-announcements-spark-broad-software-rally/) · fxleaders.com |

## Funding records, Jan – Apr 2026

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 3 Feb 2026 | Oracle (oracle.com) | bond placement | $25B | — | — | The Oracle technology group is testing the boom of artificial intelligence in the markets this week by launching an express bond placement… |
| 2 Feb 2026 | Oracle (oracle.com) | — | — | — | — | Oracle Oracle Corp. plans to raise between US$45,000 and US$50 billion this year through a combination of debt sales and shares to build… |
| 1 Feb 2026 | Oracle (oracle.com) | at-the-market equity program | $20B | Citigroup | United States | Goldman Sachs & Co. LLC will be leading the senior unsecured bond offering, and Citigroup will be leading the at-the-market issuance and… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company oracle.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company oracle.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company oracle.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company oracle.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$PRISM_BUSINESS_API_BASE/v1/business/companies/oracle.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "oracle.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Zomato News](zomato-news.md)
- [Hdfc Bank News](hdfc-bank-news.md)
- [AMD News](amd-news.md)
- [Anthropic News](anthropic-news.md)
