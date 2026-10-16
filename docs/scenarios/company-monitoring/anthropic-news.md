# Anthropic News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “anthropic news” · 5,400/month India · 14,800/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [anthropic-news.json](../../examples/scenarios/anthropic-news.json).

**Question.** What has the news reported about Anthropic in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `anthropic.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `anthropic.com` |
| Headlines, Jan – Apr 2026 (estimate) | 169 |
| Events, May 2025 – Apr 2026 | 293 |
| Most frequent event types | Funding round (53), Contracts (48), New product (48) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 14% · 0.0% · 86% of 169 articles |
| Funding records, Jan – Apr 2026 | 35 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 4 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Anthropic weighs $900bn valuation in fundraising round that could eclipse OpenAI](https://proactiveinvestors.co.uk/companies/news/1091493/anthropic-weighs-900bn-valuation-in-fundraising-round-that-could-eclipse-openai-1091493.html) | proactiveinvestors.co.uk | 8 | positive | Capital infusion |
| 27 Apr 2026 | [Google Commits Up to USD 40B to Anthropic as AI Race Intensifies](https://waya.media/google-commits-up-to-usd-40b-to-anthropic-as-ai-race-intensifies/) | waya.media | 8 | positive | Funding round |
| 27 Apr 2026 | [Google joins Amazon in backing Anthropic at a $350B valuation to lock in AI cloud dominance — TFN](https://techfundingnews.com/amid-speculation-of-surpassing-openais-valuation-anthropic-to-land-10b-from-google/) | techfundingnews.com | 8 | positive | Funding round |
| 25 Apr 2026 | [Google’s Bold $40 Billion Bet on AI Startup Anthropic: A New Era in Artificial Intelligence Investment](https://www.theedadvocate.org/googles-bold-40-billion-bet-on-ai-startup-anthropic-a-new-era-in-artificial-intelligence-investment/) | theedadvocate.org | 8 | positive | Funding round |
| 24 Apr 2026 | [Google va investir 40 milliards de dollars dans Anthropic, dont 10 immédiatement](https://www.lalibre.be/economie/entreprises-startup/2026/04/24/google-va-investir-40-milliards-de-dollars-dans-anthropic-dont-10-immediatement-GUQSW4NXWVA4PLCGGB5OJNU66I/) | lalibre.be | 7 | positive | M&A |
| 24 Apr 2026 | [Google envisage un investissement massif dans Anthropic](https://www.tradingsat.com/actualites/informations-societes/google-envisage-un-investissement-massif-dans-anthropic-1161408.html) | tradingsat.com | 7 | positive | Funding round |
| 22 Apr 2026 | [Amazon invirtió US$ 33.000 millones en Anthropic para asegurarse el recurso más escaso del negocio tecnológico](https://www.forbes.com.ec/innovacion/amazon-invirtio-us-33000-millones-anthropic-asegurarse-recurso-mas-escaso-negocio-tecnologico-n89755) | forbes.com.ec | 7 | positive | Capital infusion |
| 21 Apr 2026 | [AI startup Anthropic commits $100 billion to Amazon's AWS over next 10 years](https://www.ajc.com/news/2026/04/ai-startup-anthropic-commits-100-billion-to-amazons-aws-over-next-10-years/) | ajc.com | 8 | positive | Contracts |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Funding round | 53 |
| Contracts | 48 |
| New product | 48 |
| Announcement | 41 |
| Key people | 31 |
| Lawsuit | 18 |
| Job creation | 16 |
| Capital infusion | 15 |
| M&A | 9 |
| Earnings | 7 |
| Regulatory | 2 |
| IPO | 2 |
| Asset acquisition | 1 |
| Board | 1 |
| Buyback | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Funding round | Contracts | New product | Announcement |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 12 | 2 | 1 | 3 | 0 | ███ |
| Jun 2025 | 4 | 0 | 0 | 0 | 1 | █ |
| Jul 2025 | 10 | 4 | 1 | 2 | 1 | ███ |
| Aug 2025 | 6 | 1 | 1 | 1 | 0 | ██ |
| Sep 2025 | 20 | 10 | 2 | 1 | 2 | ██████ |
| Oct 2025 | 26 | 0 | 4 | 2 | 14 | ███████ |
| Nov 2025 | 28 | 3 | 8 | 0 | 4 | ████████ |
| Dec 2025 | 8 | 0 | 4 | 1 | 0 | ██ |
| Jan 2026 | 22 | 9 | 2 | 2 | 0 | ██████ |
| Feb 2026 | 71 | 14 | 3 | 26 | 16 | ████████████████████ |
| Mar 2026 | 17 | 1 | 3 | 2 | 1 | █████ |
| Apr 2026 | 69 | 9 | 19 | 8 | 2 | ███████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 3 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 30 Apr 2026 | Funding round | According to TechCrunch, these involve proposals to raise approximately $50 billion at a valuation between $850 billion and $900 billion. | article unavailable |
| 30 Apr 2026 | Capital infusion | Google said earlier this month that it plans to invest up to $40 billion in Anthropic. | [Anthropic weighs $900bn valuation in fundraising round that could…](https://proactiveinvestors.co.uk/companies/news/1091493/anthropic-weighs-900bn-valuation-in-fundraising-round-that-could-eclipse-openai-1091493.html) · proactiveinvestors.co.uk |
| 27 Apr 2026 | Funding round | Alphabet committed an initial USD 10 billion in cash to Anthropic at a USD 350 billion valuation, with a further USD 30 billion tied to performance… | [Google Commits Up to USD 40B to Anthropic as AI Race Intensifies](https://waya.media/google-commits-up-to-usd-40b-to-anthropic-as-ai-race-intensifies/) · waya.media |
| 27 Apr 2026 | Funding round | Four days earlier, Amazon announced a $5 billion investment into Anthropic, with up to $20 billion more tied to certain commercial milestones,… | [Google joins Amazon in backing Anthropic at a $350B valuation to…](https://techfundingnews.com/amid-speculation-of-surpassing-openais-valuation-anthropic-to-land-10b-from-google/) · techfundingnews.com |
| 25 Apr 2026 | Funding round | Google has announced a staggering investment of up to $40 billion in the AI startup Anthropic. This strategic financial commitment, unveiled on… | [Google’s Bold $40 Billion Bet on AI Startup Anthropic: A New Era in…](https://www.theedadvocate.org/googles-bold-40-billion-bet-on-ai-startup-anthropic-a-new-era-in-artificial-intelligence-investment/) · theedadvocate.org |
| 24 Apr 2026 | M&A | The Seattle Group (Washington State) is planning to acquire, in the longer term, $20 billion in additional stock. | [Google va investir 40 milliards de dollars dans Anthropic, dont 10…](https://www.lalibre.be/economie/entreprises-startup/2026/04/24/google-va-investir-40-milliards-de-dollars-dans-anthropic-dont-10-immediatement-GUQSW4NXWVA4PLCGGB5OJNU66I/) · lalibre.be |
| 24 Apr 2026 | Funding round | Alphabet, Google's parent company, could invest up to $40 billion in Anthropic start-up, according to press reports. | [Google envisage un investissement massif dans Anthropic](https://www.tradingsat.com/actualites/informations-societes/google-envisage-un-investissement-massif-dans-anthropic-1161408.html) · tradingsat.com |
| 23 Apr 2026 | New product | Earlier this month, Anthropic announced Mythos, which had the unprecedented capability to autonomously identify, at scale, hitherto undiscovered… | [AI’s most formidable disruptor](https://www.financialexpress.com/opinion/ais-most-formidable-disruptor/4216707/) · financialexpress.com |
| 22 Apr 2026 | Capital infusion | On April 20, Amazon announced that it would invest up to an additional $25 billion in Anthropic and that it would bring its total commitment to $33… | [Amazon invirtió US$ 33.000 millones en Anthropic para asegurarse el…](https://www.forbes.com.ec/innovacion/amazon-invirtio-us-33000-millones-anthropic-asegurarse-recurso-mas-escaso-negocio-tecnologico-n89755) · forbes.com.ec |
| 21 Apr 2026 | Contracts | Artificial intelligence company Anthropic has agreed to commit more than $100 billion to Amazon's AWS cloud platform over the next 10 years to train… | article unavailable |
| 21 Apr 2026 | Contracts | Artificial intelligence company Anthropic has agreed to commit more than $100 billion to Amazon's AWS cloud platform over the next 10 years to train… | [AI startup Anthropic commits $100 billion to Amazon's AWS over next…](https://www.ajc.com/news/2026/04/ai-startup-anthropic-commits-100-billion-to-amazons-aws-over-next-10-years/) · ajc.com |
| 21 Apr 2026 | Contracts | Artificial intelligence company Anthropic has agreed to commit more than $100 billion to Amazon’s AWS cloud platform over the next 10 years to train… | article unavailable |

## Funding records, Jan – Apr 2026

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Anthropic (anthropic.com) | — | — ⚠ implausible size | — | — | According to TechCrunch, these involve proposals to raise approximately $50 billion at a valuation between $850 billion and $900 billion. |
| 27 Apr 2026 | Anthropic (anthropic.com) | Series H | $10B ⚠ check sentence | google | — | Google is investing $10 billion in Anthropic now, with another $30 billion potentially to follow if Anthropic hits certain performance… |
| 27 Apr 2026 | Anthropic (anthropic.com) | Series G | $5B | amazon | — | Four days earlier, Amazon announced a $5 billion investment into Anthropic, with up to $20 billion more tied to certain commercial… |
| 21 Apr 2026 | Anthropic (anthropic.com) | investment | $25B | amazon | United States | Amazon is investing $5 billion into Anthropic immediately, with the potential to invest up to $20 billion more tied to commercial… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company anthropic.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company anthropic.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company anthropic.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company anthropic.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/anthropic.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "anthropic.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.
- Zero-count periods are included; partial_period marks buckets only partly covered by the window.
- shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)

## Related demonstrations

- [Oracle News](oracle-news.md)
- [AMD News](amd-news.md)
- [Microsoft News](microsoft-news.md)
- [Walmart News](walmart-news.md)
