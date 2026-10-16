# Temasek Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “temasek portfolio” · 70/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [temasek-portfolio.json](../../examples/scenarios/temasek-portfolio.json).

**Question.** Which rounds did Temasek appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Temasek”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 113 |
| With a usable reported amount | 95 |
| Reported total (usable amounts) | $67.3B |
| Median reported round | $181.8M |
| Largest reported round | $16B |
| Amounts left out as implausible or unconverted | 5 |
| Busiest month | Mar 2026 (23 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 6 | 4 | $1.7B | $845M | █████ |
| Jun 2025 | 5 | 4 | $938.9M | $130.8M | ████ |
| Jul 2025 | 9 | 8 | $2.6B | $480M | ████████ |
| Aug 2025 | 16 | 14 | $2.7B | $162M | ██████████████ |
| Sep 2025 | 12 | 12 | $2.8B | $136M | ██████████ |
| Oct 2025 | 3 | 0 | — | — | ███ |
| Nov 2025 | 4 | 4 | $805M | $275M | ███ |
| Dec 2025 | 9 | 8 | $17.4B | $654M | ████████ |
| Jan 2026 | 6 | 6 | $12.7B | $2.4B | █████ |
| Feb 2026 | 7 | 5 | $21.3B | $180M | ██████ |
| Mar 2026 | 23 | 21 | $22.5B | $408.6M | ████████████████████ |
| Apr 2026 | 13 | 9 | $3.1B | $392M | ███████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 22 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 27 Mar 2026 | Waymo (waymo.com) | Series D | $16B | alphabet, Andreessen Horowitz, bdt & msd partners | — | Mountain View-based Waymo is a mobility technology company that improves transportation by developing self‑driving solutions for travelers… |
| 13 Dec 2025 | Swiggy (swiggy.com) | Qualified Institutional Placement | $12B | icici prudential mutual fund, sbi mutual fund, Aditya… | India | Swiggy has said it plans to deploy ₹4,475 crore from the QIP proceeds towards expanding its quick commerce network. |
| 10 Feb 2026 | Databricks (databricks.com) | Series K | $5B ⚠ check sentence | qatar investment authority, Singapore Temasek, Macquarie… | United States | United States data & artificial intelligence (AI) company Databrick has raised $5 billion funding at $134 billion valuation, and with… |
| 13 Jan 2026 | QXO | Series C convertible perpetual preferred stock | $3B | apollo global management, temasek, other investors | USA | QXO has expanded its previously announced financing to $3 billion, increasing its capacity to pursue acquisitions as it targets… |
| 13 Jan 2026 | QXO Inc | convertible preferred equity financing | $3B | apollo funds, temasek, other investors | — | On January 12, 2026, QXO Inc. announced it had upsized its previously disclosed convertible preferred equity financing, boosting the total… |
| 14 May 2025 | Hub International (hubinternational.com) | equity | $1.6B ⚠ check sentence | T. Rowe Price Investment Management Inc., Alpha Wave… | — | Financial services firm Hub International Ltd. was valued at $29 billion for a $1.6 billion equity investment led by T. Rowe Price… |
| 14 Apr 2026 | Stegra | Rescue funding | $1.5B | Wallenberg family, temasek, imas | Sweden | Swedish green-tech startup Stegra has secured €1.4bn in rescue funding from a consortium led by the prominent Swedish Wallenberg family,… |
| 1 Aug 2025 | Bharti Airtel Africa Unit | — | $1.2B | Warberg Pinks, temasek, singtel | — | The Africa Unit of Bharti Airtel is raising $ 1.25 billion (approximately Rs 9200 crore) by releasing fresh shares to six global investors… |
| 1 Jul 2025 | Jsw Paints (jswpaints.in) | Acquisition | $1.1B | Sajjan Jindal and family, barclays, kkr | India | JSW Paints’ ₹9,000 crore Akzo India buy will propel the Sajjan Jindal-led company to the No 4 slot in the Indian paints market. |
| 13 Apr 2026 | AMI Labs | — | $1B ⚠ check sentence | cathay innovation, bezos expeditions, temasek | — | In March the company raised $1.03bn at a pre money valuation of $3.5bn. led by Cathay Innovation, Bezos Expeditions, Temasek and Nvidia. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 14 Apr 2026 | Stegra | Rescue funding | $1.5B | Wallenberg family, temasek, imas | Sweden | Swedish green-tech startup Stegra has secured €1.4bn in rescue funding from a consortium led by the prominent Swedish Wallenberg family,… |
| 14 Apr 2026 | Nio Inc. | Investment | $392M | Anhui provincial government entities, Tencent Holdings,… | China | In an effort to control costs, Nio reduced unprofitable ventures, and concurrently, the company steps up funding efforts, securing a 2.8… |
| 13 Apr 2026 | AMI Labs | — | $1B ⚠ check sentence | cathay innovation, bezos expeditions, temasek | — | In March the company raised $1.03bn at a pre money valuation of $3.5bn. led by Cathay Innovation, Bezos Expeditions, Temasek and Nvidia. |
| 8 Apr 2026 | Terawatt Technology (terawatt-technology.com) | Series C | — | khosla ventures, temasek, jic venture growth investments | USA | TeraWatt Technology announced the completion of the final close of its Series C funding round, bringing in a mix of financial and… |
| 8 Apr 2026 | Injewelme (injewelme.com) | pre-seed | $1.2M | Temasek Trust's C3H (Catalytic Capital for Climate and… | Singapore | Singapore-based healthtech startup Injewelme has raised $1.2 million in a funding round to propel its AI-driven health monitoring… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Temasek --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Temasek --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Temasek --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Temasek", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Temasek", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [General Catalyst Portfolio](general-catalyst-portfolio.md)
- [Andreessen Horowitz Portfolio](andreessen-horowitz-portfolio.md)
- [8vc Portfolio](8vc-portfolio.md)
- [Kleiner Perkins Portfolio](kleiner-perkins-portfolio.md)
