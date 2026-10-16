# Mubadala Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “mubadala investments” · 720/month India · 1,300/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [mubadala-investments.json](../../examples/scenarios/mubadala-investments.json).

**Question.** Which rounds did Mubadala appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Mubadala”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 58 |
| With a usable reported amount | 51 |
| Reported total (usable amounts) | $65.9B |
| Median reported round | $300M |
| Largest reported round | $16B |
| Amounts left out as implausible or unconverted | 1 |
| Busiest month | Jul 2025 (17 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2 | 2 | $16.5B | $8.2B | ██ |
| Jun 2025 | 2 | 2 | $900M | $450M | ██ |
| Jul 2025 | 17 | 14 | $6.4B | $710M | ████████████████████ |
| Aug 2025 | 3 | 3 | $112M | $30M | ████ |
| Sep 2025 | 4 | 4 | $7.7B | $2.2B | █████ |
| Oct 2025 | 8 | 8 | $13.9B | $1.4B | █████████ |
| Nov 2025 | 2 | 1 | $183M | $183M | ██ |
| Dec 2025 | 1 | 1 | $78M | $78M | █ |
| Jan 2026 | 8 | 6 | $368M | $50M | █████████ |
| Feb 2026 | 5 | 5 | $19.1B | $497M | ██████ |
| Mar 2026 | 5 | 4 | $16.6B | $575M | ██████ |
| Apr 2026 | 1 | 1 | $40M | $40M | █ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 19 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 27 Mar 2026 | Waymo (waymo.com) | Series D | $16B | alphabet, Andreessen Horowitz, bdt & msd partners | — | Mountain View-based Waymo is a mobility technology company that improves transportation by developing self‑driving solutions for travelers… |
| 9 May 2025 | TWG Global | Equity raise | $15B | Mubadala Capital | Hong Kong | Under this strategic investment alliance and as part of TWG’s $15 billion equity raise, Mubadala Capital will anchor and lead a $10… |
| 22 Oct 2025 | Nextdecade (next-decade.com) | Positive FID & Financing | $6.7B | Rio Grande LNG Train 5, LLC, Rio Grande LNG Train 5, LLC,… | — | To fully fund the expected costs for Train 5 and related infrastructure, the Company successfully closed on approximately $6.7 billion in… |
| 22 Sep 2025 | Ardonagh Group | equity investment | $3.2B | Madison Dearborn Partners, hps investment partners, mubadala | — | In May, Ardonagh Group also completed a £2.5 billion equity investment led by existing shareholders Madison Dearborn Partners and HPS… |
| 8 Sep 2025 | Aquarian Holdings (aquarianlp.com) | — | $3B | Mubadala Capital, qatar investment authority | — | Aquarian, a private capital group with a speciality in managing insurance assets, is in advanced talks with Mubadala Capital, Qatar… |
| 14 Jul 2025 | Cityfibre (cityfibre.com) | financing agreement | $2.9B | Infrastructure at Goldman Sachs Alternatives, antin… | United Kingdom | CityFibre, the UK’s largest independent full fibre platform, has announced a major £2.3 billion financing agreement to accelerate its… |
| 17 Jul 2025 | Revolut (revolut.com) | primary | $2B ⚠ check sentence | mubadala | UK | Revolut, the UK-based fintech, is in talks about $2 billion raise at a $75 billion valuation, combining primary and secondary shares. |
| 29 May 2025 | Telegram (telegram.org) | Debt issuance | $1.5B | blackrock, mubadala, citadel | — | Telegram looks to raise $1.5 billion via a five-year bond offering backed by finance giants, including asset management firm BlackRock,… |
| 24 Oct 2025 | Crusoe (crusoe.ai) | — | $1.4B ⚠ check sentence | valor equity partners, Mubadala Capital, nvidia | USA | Crusoe, which calls itself 'the AI Factory Company,' is valued at over $10 billion in this latest $1.4 billion funding round. |
| 31 Mar 2026 | Whoop (whoop.com) | Series G | $575M ⚠ check sentence | collaborative fund, 2PointZero Group, qatar investment… | USA | WHOOP, the human performance company, today announced it has raised $575 million in Series G funding at a $10.1 billion valuation,… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 15 Apr 2026 | Alloy Therapeutics (alloytx.com) | Series E | $40M | 8vc, jic venture growth investments, echo capital | USA | Alloy Therapeutics, a biotechnology ecosystem company, announced a $40 million Series E financing round. |
| 31 Mar 2026 | Whoop (whoop.com) | Series G | $575M ⚠ check sentence | collaborative fund, 2PointZero Group, qatar investment… | USA | WHOOP, the human performance company, today announced it has raised $575 million in Series G funding at a $10.1 billion valuation,… |
| 27 Mar 2026 | Waymo (waymo.com) | Series D | $16B | alphabet, Andreessen Horowitz, bdt & msd partners | — | Mountain View-based Waymo is a mobility technology company that improves transportation by developing self‑driving solutions for travelers… |
| 24 Mar 2026 | Waymo (waymo.com) | Series D | — ⚠ implausible size | alphabet, Andreessen Horowitz, bdt & msd partners | USA |  |
| 4 Mar 2026 | 4ig (4ig.hu) | convertible loan | $50M | mubadala | Hungary | Mubadala will provide a USD 50 million convertible loan to Hungary’s 4iG. |
| 5 Feb 2026 | L-nutra (l-nutra.com) | Series D | $83.5M | mubadala | United States | L-Nutra Inc., the world’s first nutri-technology company announced today a $36.5 million investment in its Series D funding round. The… |
| 4 Feb 2026 | Ivc Evidensia (ivcevidensia.com) | — | $497M | mubadala, eqt, silver lake | United Kingdom | Mubadala Invests $497M in Europe’s Largest Veterinary Care Provider |
| 4 Feb 2026 | Stake (stake.rent) | Series B | $31M | emirates nbd, mubadala, middle east venture partners | UAE | Emirates NBD leads $31 million round as Stake accelerates expansion in Saudi Arabia and the US. |
| 3 Feb 2026 | Waymo (waymo.com) | Series? | $2.5B | mubadala | United States | It was part of Waymo’s $2.5 billion funding round in 2020. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Mubadala --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Mubadala --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Mubadala --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Mubadala", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Mubadala", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [KKR Investments](kkr-investments.md)
- [Blackstone Investments](blackstone-investments.md)
- [Sequoia Investments](sequoia-investments.md)
- [Thrive Capital Portfolio](thrive-capital-portfolio.md)
