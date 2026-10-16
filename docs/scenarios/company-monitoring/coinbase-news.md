# Coinbase News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “coinbase news” · 880/month India · 5,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [coinbase-news.json](../../examples/scenarios/coinbase-news.json).

**Question.** What has the news reported about Coinbase in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `coinbase.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `coinbase.com` |
| Headlines, Jan – Apr 2026 (estimate) | 13,499 |
| Events, May 2025 – Apr 2026 | 38 |
| Most frequent event types | Earnings (16), M&A (5), Lawsuit (4) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 34% · 0.8% · 65% of 13,499 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 1 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [Riot Platforms rises following Q1 revenue beat](https://sherwood.news/crypto/riot-platforms-q1-2026-earnings/) | sherwood.news | 7 | positive | — |
| 30 Apr 2026 | [Coinbase Debuts ‘CUSHY’ Fund to Give Institutions Onchain Access to Stablecoin Lending Yields - Crypto Economy](https://crypto-economy.com/coinbase-debuts-cushy-fund-to-give-institutions-onchain-access-to-stablecoin-lending-yields/) | crypto-economy.com | 7 | positive | — |
| 30 Apr 2026 | [MEGA Token Goes Live With $1.6B FDV Across Major Exchanges](https://www.cryptotimes.io/2026/05/01/mega-token-goes-live-with-1-6b-fdv-across-major-exchanges/) | cryptotimes.io | 7 | positive | — |
| 30 Apr 2026 | [Washington’s Pivot From Policing Crypto to Owning It](https://intpolicydigest.org/washington-s-pivot-from-policing-crypto-to-owning-it/) | intpolicydigest.org | 7 | positive | — |
| 30 Apr 2026 | [From Cathie Wood to Cantor Fitzgerald, the big money is betting that Robinhood’s (HOOD) crypto slump is just…](https://www.coindesk.com/markets/2026/04/30/from-cathie-wood-to-cantor-fitzgerald-the-big-money-is-betting-that-robinhood-s-crypto-slump-is-just-a-temporary-speed-bump) | coindesk.com | 7 | positive | — |
| 30 Apr 2026 | [8 leading crypto apps for 2026: Trade, automate, and earn crypto](https://crypto.news/8-leading-crypto-apps-for-2026-trade-automate-and-earn-crypto/) | crypto.news | 6 | positive | — |
| 30 Apr 2026 | [Syndicate Labs Key Leak Spurs 18.5M SYND Bridge Transfer](https://coincu.com/syndicate-labs-private-key-leak-18-5m-synd-bridge-transfer/) | coincu.com | 8 | negative | — |
| 30 Apr 2026 | [Coinbase Builds on Growing Stablecoin Economy With CUSHY](https://www.cryptotimes.io/2026/04/30/coinbase-builds-on-growing-stablecoin-economy-with-cushy/) | cryptotimes.io | 7 | positive | — |
| 30 Apr 2026 | [Coinbase launches CUSHY digital credit strategy with tokenized share structure](https://crypto.news/coinbase-launches-cushy-digital-credit-strategy-with-tokenized-share-structure/) | crypto.news | 7 | positive | — |
| 30 Apr 2026 | [Gamma Prime Brings the Tokenized Capital Summit to Miami on May 4th, showcasing its platform for investors’…](https://crypto.news/gamma-prime-brings-the-tokenized-capital-summit-to-miami-on-may-4th-showcasing-its-platform-for-investors-dealflow/) | crypto.news | 7 | positive | — |
| 30 Apr 2026 | [WhiteBIT Coin rallies 8% after FC Barcelona partnership, more gains incoming?](https://crypto.news/whitebit-coin-rallies-8-after-fc-barcelona-partnership-more-gains-incoming/) | crypto.news | 7 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Earnings | 16 |
| M&A | 5 |
| Lawsuit | 4 |
| Key people | 3 |
| New product | 3 |
| Incorporation | 3 |
| Contracts | 1 |
| Funding round | 1 |
| Asset acquisition | 1 |
| Regulatory | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Earnings | M&A | Lawsuit | Key people |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 7 | 5 | 1 | 0 | 0 | ████████████████ |
| Jun 2025 | 0 | 0 | 0 | 0 | 0 |  |
| Jul 2025 | 2 | 1 | 0 | 0 | 0 | ████ |
| Aug 2025 | 2 | 1 | 0 | 0 | 0 | ████ |
| Sep 2025 | 0 | 0 | 0 | 0 | 0 |  |
| Oct 2025 | 8 | 5 | 1 | 0 | 1 | ██████████████████ |
| Nov 2025 | 5 | 1 | 1 | 0 | 0 | ███████████ |
| Dec 2025 | 1 | 0 | 1 | 0 | 0 | ██ |
| Jan 2026 | 1 | 0 | 0 | 0 | 0 | ██ |
| Feb 2026 | 9 | 3 | 1 | 4 | 0 | ████████████████████ |
| Mar 2026 | 2 | 0 | 0 | 0 | 2 | ████ |
| Apr 2026 | 1 | 0 | 0 | 0 | 0 | ██ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 6 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 10 Apr 2026 | Regulatory | The US Office of the Comptroller of the Currency (OCC) has granted conditional approval for a National Trust Company Charter to cryptocurrency… | [Top five fintech news stories of the week – 10 April 2026](https://www.fintechfutures.com/fintech/fintech-futures-top-five-news-stories-of-the-week-10-april-2026) · fintechfutures.com |
| 31 Mar 2026 | Key people | Del Corral confirmed he will be joining Coinbase as Vice President of Customer Experience. | [Tesla Head of Customer Experience Jose del Corral Moves to Coinbase](https://driveteslacanada.ca/news/tesla-head-of-customer-experience-jose-del-corral-moves-to-coinbase/) · driveteslacanada.ca |
| 25 Mar 2026 | Key people | The 13 initial appointees also include Oracle founder Larry Ellison, Google co-founder Sergey Brin, AMD CEO Lisa Su, and Dell Technologies CEO… | article unavailable |
| 19 Feb 2026 | M&A | Coinbase acquired Liquifi last summer. | [Kraken Acquires Magna As $60B Peak TVL Boosts Expansion](https://www.tronweekly.com/kraken-acquires-magna-as-60b-peak-tvl-boosts/) · tronweekly.com |
| 19 Feb 2026 | Lawsuit | Last month, the Delaware Court of Chancery in Adam Grabski ex rel. Coinbase Global, Inc. v. Andreessen denied a motion by Coinbase Global, Inc.’s… | [Business Organization, Construction, Insurance \| JD Supra](https://www.jdsupra.com/law-news/business-organizations/construction-law/insurance-law/) · jdsupra.com |
| 19 Feb 2026 | Lawsuit | Last month, the Delaware Court of Chancery in Adam Grabski ex rel. Coinbase Global, Inc. v. Andreessen denied a motion by Coinbase Global, Inc.’s… | article unavailable |
| 19 Feb 2026 | Lawsuit | Last month, the Delaware Court of Chancery in Adam Grabski ex rel. Coinbase Global, Inc. v. Andreessen denied a motion by Coinbase Global, Inc.’s… | article unavailable |
| 17 Feb 2026 | New product | Coinbase launched Agentic Wallets, a wallet infrastructure built specifically for agents to equip them with autonomous spending, earning, and… | article unavailable |
| 12 Feb 2026 | Earnings | Coinbase just dropped a grenade on Wall Street. The company missed big, reporting Q4 revenue of $1.78 billion, down 31%, and an earnings per share… | article unavailable |
| 12 Feb 2026 | Earnings | Coinbase’s total revenue for 2025 was $7.18 billion, up 9% from 2024. | article unavailable |
| 10 Feb 2026 | Earnings | Coinbase beat analysts’ revenue expectations by 4.5% last quarter, reporting revenues of $1.87 billion, up 55.1% year on year. | [Coinbase (COIN) Reports Q4: Everything You Need To Know Ahead Of…](https://www.theglobeandmail.com/investing/markets/stocks/COIN/pressreleases/145865/coinbase-coin-reports-q4-everything-you-need-to-know-ahead-of-earnings/) · theglobeandmail.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company coinbase.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company coinbase.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company coinbase.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company coinbase.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/coinbase.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "coinbase.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Paypal News](paypal-news.md)
- [Icici Bank News](icici-bank-news.md)
- [Spotify News](spotify-news.md)
- [Bajaj Finance News](bajaj-finance-news.md)
