# Warburg Pincus Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “warburg pincus portfolio” · 210/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [warburg-pincus-portfolio.json](../../examples/scenarios/warburg-pincus-portfolio.json).

**Question.** Which rounds did Warburg Pincus appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Warburg Pincus”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 30 |
| With a usable reported amount | 18 |
| Reported total (usable amounts) | $6.9B |
| Median reported round | $123.9M |
| Largest reported round | $4.2B |
| Busiest month | Jun 2025 (7 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1 | 1 | $96M | $96M | ███ |
| Jun 2025 | 7 | 7 | $180M | $40M | ████████████████████ |
| Jul 2025 | 7 | 3 | $399M | $189M | ████████████████████ |
| Aug 2025 | 3 | 1 | $4.2B | $4.2B | █████████ |
| Sep 2025 | 0 | 0 | — | — |  |
| Oct 2025 | 1 | 0 | — | — | ███ |
| Nov 2025 | 1 | 0 | — | — | ███ |
| Dec 2025 | 4 | 1 | $400M | $400M | ███████████ |
| Jan 2026 | 1 | 1 | $115.2M | $115.2M | ███ |
| Feb 2026 | 2 | 2 | $123.9M | $123.9M | ██████ |
| Mar 2026 | 3 | 2 | $1.4B | $691M | █████████ |
| Apr 2026 | 0 | 0 | — | — |  |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 12 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 23 Aug 2025 | Hertz Global Holdings (hertz.com) | equity capital sponsorship | $4.2B | Centerbridge Partners L.P., warburg pincus, dundon capital… | USA | The sponsorship group, made up of a trio of companies — Centerbridge Partners L.P., Warburg Pincus LLC and Dundon Capital Partners LLC —… |
| 2 Mar 2026 | Global Eggs | — | $1B | warburg pincus | Luxembourg | Global Eggs, a multinational table eggs company founded by Brazilian Ricardo Faria, will receive a contribution of up to $1 billion… |
| 17 Dec 2025 | Service Compression (servicecompression.com) | Asset-based loan | $400M | J.P. Morgan, warburg pincus, masked rider capital | USA | Service Compression, LLC (“Service Compression” or “SC”), a leading provider of natural gas compression services to exploration and… |
| 9 Mar 2026 | Sotera Health (soterahealth.com) | — | $382M | warburg pincus, GTCR, LLC | — | The offering raised approximately $382 million in aggregate gross proceeds for the selling stockholders and closed on March 6, 2026. |
| 21 Jul 2025 | Meril (meril.org) | — | $200M | abu dhabi investment authority, warburg pincus | India | Abu Dhabi Investment Authority (ADIA) has signed a definitive agreement to invest $200 million (approximately ₹1,723 crore) in Meril, a… |
| 23 Jul 2025 | Micro Life Sciences (microlifesciencesprivatelimited.vdtrxn) | — | $189M | warburg pincus | India | In 2022, the promoters tapped Warburg Pincus to raise Rs 1,575 crore by selling a 14% stake in Meril, |
| 9 Feb 2026 | Varo Bank | — | $123.9M | Coliseum Capital Management, Northview Lifesciences,… | US | Varo Bank has now raised a total of $1.2B in total equity funding and is backed by Coliseum Capital Management, Northview LifeSciences,… |
| 10 Jan 2026 | Fleur Hotels | — | $115.2M | warburg pincus | India | Private equity firm Warburg Pincus will invest upto ₹960 crore in Lemon Tree Hotel’s subsidiary, Fleur Hotels as a part of strategic… |
| 24 Jun 2025 | Miami International (miaxglobal.com) | growth | $100M | warburg pincus | United States | in August 2024, Warburg Pincus' Capital Solutions team provided a $100 million growth investment earmarked to support a number of MIH… |
| 12 May 2025 | Fusion Finance (fusionfinance.com) | Rights Issue | $96M | Honey Rose Investment Ltd, warburg pincus, creation… | India | Fusion Finance announced the successful completion of its Rs. 800 crore Rights Issue, which was subscribed 1.5x. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 9 Mar 2026 | Sotera Health (soterahealth.com) | — | $382M | warburg pincus, GTCR, LLC | — | The offering raised approximately $382 million in aggregate gross proceeds for the selling stockholders and closed on March 6, 2026. |
| 3 Mar 2026 | Global Eggs | — | — | warburg pincus | — | Warburg Pincus has concluded an agreement to invest in Global Eggs, in a transaction that assesses the company at $8 billion (around… |
| 2 Mar 2026 | Global Eggs | — | $1B | warburg pincus | Luxembourg | Global Eggs, a multinational table eggs company founded by Brazilian Ricardo Faria, will receive a contribution of up to $1 billion… |
| 9 Feb 2026 | Varo Bank | — | $123.9M | Coliseum Capital Management, Northview Lifesciences,… | US | Varo Bank has now raised a total of $1.2B in total equity funding and is backed by Coliseum Capital Management, Northview LifeSciences,… |
| 10 Jan 2026 | Fleur Hotels | — | $115.2M | warburg pincus | India | Private equity firm Warburg Pincus will invest upto ₹960 crore in Lemon Tree Hotel’s subsidiary, Fleur Hotels as a part of strategic… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "Warburg Pincus" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "Warburg Pincus" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "Warburg Pincus" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Warburg Pincus", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Warburg Pincus", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Investor names match broadly (a name can match several firms or funds); use a domain for a narrower match.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Hillhouse Investments](hillhouse-investments.md)
- [Carlyle Investments](carlyle-investments.md)
- [Benchmark Investments](benchmark-investments.md)
- [General Atlantic Portfolio](general-atlantic-portfolio.md)
