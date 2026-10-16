# Jpmorgan News: measured events and news with sources (to Apr 2026)

[Company monitoring research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “jpmorgan news” · 4,400/month India · 6,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [jpmorgan-news.json](../../examples/scenarios/jpmorgan-news.json).

**Question.** What has the news reported about Jpmorgan in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?

**Filters.** company domain `jpmorganchase.com`.

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `jpmorganchase.com` |
| Headlines, Jan – Apr 2026 (estimate) | 28,811 |
| Events, May 2025 – Apr 2026 | 170 |
| Most frequent event types | Key people (36), Earnings (26), Announcement (26) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 20% · 1.0% · 79% of 28,811 articles |
| Funding records, Jan – Apr 2026 | 0 |

## Latest headlines, Jan – Apr 2026

From `GET /v1/business/companies/{domain}/news`, newest first. 2 requested articles were temporarily unavailable at capture time.

| Published | Headline | Publisher | Priority | Tone | Events |
| --- | --- | --- | ---: | --- | --- |
| 30 Apr 2026 | [GCM Grosvenor Inc. (NASDAQ:GCMG) Short Interest Update](https://baseballnewssource.com/2026/04/30/gcm-grosvenor-inc-nasdaqgcmg-short-interest-update-2/11105200.html) | baseballnewssource.com | 4 | negative | — |
| 30 Apr 2026 | [Kayne Anderson BDC, Inc. (NYSE:KBDC) Short Interest Update](https://baseballnewssource.com/2026/04/30/kayne-anderson-bdc-inc-nysekbdc-short-interest-update/11105198.html) | baseballnewssource.com | 3 | negative | — |
| 30 Apr 2026 | [Exponent (NASDAQ:EXPO) Announces Earnings Results](https://www.tickerreport.com/banking-finance/13424269/exponent-nasdaqexpo-announces-earnings-results.html) | tickerreport.com | 6 | positive | — |
| 30 Apr 2026 | [Casella Waste Systems (NASDAQ:CWST) Posts Quarterly Earnings Results, Beats Expectations By $0.10 EPS](https://www.thelincolnianonline.com/2026/04/30/casella-waste-systems-nasdaqcwst-posts-quarterly-earnings-results-beats-expectations-by-0-10-eps.html) | thelincolnianonline.com | 5 | negative | — |
| 30 Apr 2026 | [Brunswick (NYSE:BC) Updates FY 2026 Earnings Guidance](https://baseballnewssource.com/2026/04/30/brunswick-nysebc-updates-fy-2026-earnings-guidance/11105196.html) | baseballnewssource.com | 4 | positive | Earnings |
| 30 Apr 2026 | [iRhythm Technologies (NASDAQ:IRTC) Issues Earnings Results, Beats Estimates By $0.31 EPS](https://baseballnewssource.com/2026/04/30/irhythm-technologies-nasdaqirtc-issues-earnings-results-beats-estimates-by-0-31-eps/11105193.html) | baseballnewssource.com | 4 | positive | Earnings |
| 30 Apr 2026 | [Sinclair (NASDAQ:SBGI) Announces Quarterly Earnings Results](https://www.tickerreport.com/banking-finance/13424258/sinclair-nasdaqsbgi-announces-quarterly-earnings-results.html) | tickerreport.com | 7 | positive | Earnings |
| 30 Apr 2026 | [Banco De Chile (NYSE:BCH) Posts Earnings Results, Misses Estimates By $0.01 EPS](https://www.tickerreport.com/banking-finance/13424255/banco-de-chile-nysebch-posts-earnings-results-misses-estimates-by-0-01-eps.html) | tickerreport.com | 4 | negative | Earnings |
| 30 Apr 2026 | [American International Group (NYSE:AIG) Releases Quarterly Earnings Results, Beats Expectations By $0.20 EPS](https://www.tickerreport.com/banking-finance/13424253/american-international-group-nyseaig-releases-quarterly-earnings-results-beats-expectations-by-0-20-eps.html) | tickerreport.com | 4 | positive | — |
| 30 Apr 2026 | [Albany International (NYSE:AIN) Posts Earnings Results, Beats Expectations By $0.05 EPS](https://baseballnewssource.com/2026/04/30/albany-international-nyseain-posts-earnings-results-beats-expectations-by-0-05-eps/11105186.html) | baseballnewssource.com | 4 | positive | — |

## Event mix, May 2025 – Apr 2026

| Event type | Events |
| --- | ---: |
| Key people | 36 |
| Earnings | 26 |
| Announcement | 26 |
| M&A | 21 |
| Contracts | 17 |
| Asset acquisition | 10 |
| Lawsuit | 9 |
| Job creation | 9 |
| New product | 4 |
| Regulatory | 4 |
| Capital infusion | 3 |
| Layoffs | 2 |
| Buyback | 2 |
| IPO | 1 |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events | Key people | Earnings | Announcement | M&A |  |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| May 2025 | 8 | 1 | 0 | 2 | 2 | ███████ |
| Jun 2025 | 7 | 4 | 0 | 0 | 2 | ██████ |
| Jul 2025 | 17 | 2 | 5 | 3 | 2 | ███████████████ |
| Aug 2025 | 18 | 3 | 2 | 2 | 2 | ████████████████ |
| Sep 2025 | 14 | 4 | 1 | 3 | 1 | ████████████ |
| Oct 2025 | 21 | 3 | 5 | 8 | 0 | ██████████████████ |
| Nov 2025 | 9 | 0 | 1 | 1 | 0 | ████████ |
| Dec 2025 | 14 | 10 | 0 | 2 | 0 | ████████████ |
| Jan 2026 | 14 | 1 | 4 | 0 | 5 | ████████████ |
| Feb 2026 | 10 | 3 | 0 | 4 | 2 | █████████ |
| Mar 2026 | 15 | 5 | 0 | 0 | 3 | █████████████ |
| Apr 2026 | 23 | 0 | 8 | 1 | 2 | ████████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`. Source details were unavailable for 4 of these events.

| Published | Type | Evidence sentence | Source |
| --- | --- | --- | --- |
| 23 Apr 2026 | M&A | JPMorgan Chase & Co. grew its stake in shares of Raymond James Financial by 4.1% in the third quarter. JPMorgan Chase & Co. now owns 5,847,869… | [United Asset Strategies Inc. Takes $2.56 Million Position in Raymond…](https://www.watchlistnews.com/united-asset-strategies-inc-takes-2-56-million-position-in-raymond-james-financial-inc-rjf/11056845.html) · watchlistnews.com |
| 18 Apr 2026 | Asset acquisition | JPMorgan Chase & Co. now owns 684,783 shares of the company’s stock worth $23,796,000 after purchasing an additional 58,350 shares during the last… | [Amer Sports (NYSE:AS) General Counsel Jutta Karlsson Sells 662 Shares](https://www.watchlistnews.com/amer-sports-nyseas-general-counsel-jutta-karlsson-sells-662-shares/11052819.html) · watchlistnews.com |
| 18 Apr 2026 | Asset acquisition | JPMorgan Chase & Co. acquired a new stake in Figure Technology Solutions in the 3rd quarter valued at $15,529,000. | [Figure Technology Solutions (NASDAQ:FIGR) Director Michael Scott…](https://www.tickerreport.com/banking-finance/13411260/figure-technology-solutions-nasdaqfigr-director-michael-scott-cagney-sells-67840-shares-of-stock.html) · tickerreport.com |
| 14 Apr 2026 | Earnings | The bank reported net income of $16.5 billion, or $5.94 per share, up 17% from a year earlier. | [US Economy Stays Resilient, But 'Significant Risks' Are Building…](https://benzinga.com/markets/earnings/26/04/51805635/us-economy-stays-resilient-but-significant-risks-are-building-fast-jamie-dimon-warns) · benzinga.com |
| 14 Apr 2026 | Earnings | JPMorgan Chase & Co. (JPM – Free Report) came out with quarterly earnings of $5.94 per share, beating the Zacks Consensus Estimate of $5.49 per share. | article unavailable |
| 14 Apr 2026 | Earnings | JPMorgan Chase (JPM) said profits rose 13% year over year in the first three months of 2026 as the US economy remained resilient... | [JPMorgan profits rise 13% as Dimon warns of 'increasingly complex…](https://malaysia.news.yahoo.com/jpmorgan-and-other-big-banks-see-profits-rise-as-dimon-warns-of-increasingly-complex-set-of-risks-105717454.html) · malaysia.news.yahoo.com |
| 14 Apr 2026 | M&A | JP Morgan Chase & Co reported to the AMF that on April 9, indirectly, it had crossed the 5% thresholds of Viridien's capital and voting rights,… | [Viridien (ex cgg) : JP Morgan Chase se renforce au capital de Viridien](https://www.tradingsat.com/viridien-ex-cgg-FR001400PVN6/actualites/viridien-ex-cgg-jp-morgan-chase-se-renforce-au-capital-de-viridien-1160741.html) · tradingsat.com |
| 14 Apr 2026 | Earnings | JPMorgan Chase & Co. has released its first-quarter 2026 financial results. | [$4.9T bank JPMorganChase posts first-quarter results](https://www.stocktitan.net/news/JPM/jp-morgan-chase-reports-first-quarter-2026-financial-63d2qwdkf5p8.html) · stocktitan.net |
| 13 Apr 2026 | Earnings | Analysts expect the company to report earnings per share of $5.49 versus $5.07 year-over-year and to report revenue of $48.77 billion versus $46.01… | article unavailable |
| 13 Apr 2026 | Asset acquisition | JPMorgan Chase & Co. acquired a new stake in shares of H2O America in the 3rd quarter worth approximately $10,556,000. | [Atlas Infrastructure Partners Buys 50,385 Shares of H2O America…](https://baseballnewssource.com/2026/04/13/atlas-infrastructure-partners-buys-50385-shares-of-h2o-america-nasdaqhto-stock/11087735.html) · baseballnewssource.com |
| 13 Apr 2026 | Contracts | JPMorgan Chase is reportedly in negotiations to join the International Olympic Committee’s (IOC) top-tier sponsorship programme. | article unavailable |
| 13 Apr 2026 | Earnings | During the previous quarter, JPMorgan reported $46.77 billion in revenue — a 6.9% annual increase — yet fell short of earnings expectations. | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news company jpmorganchase.com --since 2026-01-01 --until 2026-04-30 --limit 12
prism-business-news event-trends --company jpmorganchase.com --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news sentiment --company jpmorganchase.com --since 2026-01-01 --until 2026-04-30 --granularity monthly
prism-business-news events --company jpmorganchase.com --since 2026-01-01 --until 2026-04-30 --sort newest --limit 12 --resolve true
```

The first request with curl, and the second in Python:

```bash
curl -sS --get "$API_BASE/v1/business/companies/jpmorganchase.com/news" -H "X-API-Key: $PRISM_API_KEY" --data-urlencode 'since=2026-01-01' --data-urlencode 'until=2026-04-30' --data-urlencode 'limit=12'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/event-trends", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"company": "jpmorganchase.com", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}, timeout=60)
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

- [Netflix News](netflix-news.md)
- [Meta News](meta-news.md)
- [SBI News](sbi-news.md)
- [Samsung News](samsung-news.md)
