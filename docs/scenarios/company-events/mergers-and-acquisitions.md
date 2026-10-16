# Mergers and Acquisitions: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “mergers and acquisitions” · 9,900/month India · 18,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [mergers-and-acquisitions.json](../../examples/scenarios/mergers-and-acquisitions.json).

**Question.** How many mergers and acquisitions events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `ma`.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 63,611 |
| Companies (with a domain) | 28,088 |
| Source articles | 38,935 |
| Busiest month | Dec 2025 (6,304 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 4.7% · 3.7% · 92% of 14,402 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 3,758 | ████████████ |
| Jun 2025 | 4,191 | █████████████ |
| Jul 2025 | 5,189 | ████████████████ |
| Aug 2025 | 4,716 | ███████████████ |
| Sep 2025 | 5,328 | █████████████████ |
| Oct 2025 | 5,348 | █████████████████ |
| Nov 2025 | 4,769 | ███████████████ |
| Dec 2025 | 6,304 | ████████████████████ |
| Jan 2026 | 5,636 | ██████████████████ |
| Feb 2026 | 6,209 | ████████████████████ |
| Mar 2026 | 5,861 | ███████████████████ |
| Apr 2026 | 6,302 | ████████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 5 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | skio.com | M&A | Skio, a 2020 Y Combinator alum that was founded by self‑described college dropout Kennan Frost, has been acquired by competitor Recharge, the… | [Y Combinator alum Skio sells for $105M cash, only raised $8M,…](https://techcrunch.com/2026/04/30/y-combinator-alum-skio-sells-for-105m-cash-only-raised-8m-founder-says/) · techcrunch.com |
| 30 Apr 2026 | getrecharge.com | M&A | Skio, a 2020 Y Combinator alum that was founded by self‑described college dropout Kennan Frost, has been acquired by competitor Recharge, the… | [Y Combinator alum Skio sells for $105M cash, only raised $8M,…](https://techcrunch.com/2026/04/30/y-combinator-alum-skio-sells-for-105m-cash-only-raised-8m-founder-says/) · techcrunch.com |
| 30 Apr 2026 | polarislabs.com | M&A | Oil Check Laboratory Services Limited (OCLS), a fluid analysis laboratory business based in South Yorkshire, has been acquired by a US group. | article unavailable |
| 30 Apr 2026 | edenfutures.org | M&A | Eden Futures, a private equity-backed independent supported living provider, has expanded with the acquisition of Complesso. | [PE-backed supported living provider acquires home care business](https://www.business-sale.com/news/business-sale/pebacked-supported-living-provider-acquires-home-care-business-229137) · business-sale.com |
| 30 Apr 2026 | complesso.co.uk | M&A | Eden Futures, a private equity-backed independent supported living provider, has expanded with the acquisition of Complesso. | [PE-backed supported living provider acquires home care business](https://www.business-sale.com/news/business-sale/pebacked-supported-living-provider-acquires-home-care-business-229137) · business-sale.com |
| 30 Apr 2026 | devonenergy.com | M&A | Devon Energy Corp. (NYSE: DVN ) is acquiring Coterra Energy in a deal expected to close soon, pending final closing conditions. | [S&P 500 swap on May 7 puts Veeva in and removes Coterra](https://www.stocktitan.net/news/SPGI/veeva-systems-set-to-join-s-p-pgiwfg3po3wz.html) · stocktitan.net |
| 30 Apr 2026 | coterra.com | M&A | Devon Energy Corp. (NYSE: DVN ) is acquiring Coterra Energy in a deal expected to close soon, pending final closing conditions. | [S&P 500 swap on May 7 puts Veeva in and removes Coterra](https://www.stocktitan.net/news/SPGI/veeva-systems-set-to-join-s-p-pgiwfg3po3wz.html) · stocktitan.net |
| 30 Apr 2026 | udlive.io | M&A | Badger Meter, Inc. (NYSE:BMI) completed the acquisition of UDlive Limited on May 1, 2026. | article unavailable |
| 30 Apr 2026 | badgermeter.com | M&A | Badger Meter, Inc. (NYSE:BMI) completed the acquisition of UDlive Limited on May 1, 2026. | article unavailable |
| 30 Apr 2026 | aimco.ca | M&A | AIMCo acquired 1.38 million strategic Inc. (MSTR) shares worth 219 million dollars. | [Gigante de pensiones canadiense adquiere 219 millones de dólares en…](https://crypto-economy.com/es/gigante-de-pensiones-canadiense-adquiere-219-millones-de-dolares-en-strategy-shares-y-suma-138-millones-de-mstr/) · crypto-economy.com |
| 30 Apr 2026 | flowcontrolgroup.com | M&A | Flow Control Group (“the Company” or “FCG”), a leading North American network of technical flow control and industrial automation distributors and… | article unavailable |
| 30 Apr 2026 | teledyne.com | M&A | Teledyne Technologies is merging ChartWorld and Raymarine Commercial under a single commercial navigation brand. | [Teledyne folds ChartWorld into Raymarine Commercial brand - Splash247](https://splash247.com/teledyne-folds-chartworld-into-raymarine-commercial-brand/) · splash247.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type ma --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type ma --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type ma --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["ma"], "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["ma"], "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
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

- [Insolvency](insolvency.md)
- [Joint Venture](joint-venture.md)
- [Government Contract](government-contract.md)
- [Earnings](earnings.md)
