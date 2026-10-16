# Tiger Global Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “tiger global portfolio” · 140/month India · 90/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [tiger-global-portfolio.json](../../examples/scenarios/tiger-global-portfolio.json).

**Question.** Which rounds did Tiger Global appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Tiger Global”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 74 |
| With a usable reported amount | 66 |
| Reported total (usable amounts) | $40.3B |
| Median reported round | $147M |
| Largest reported round | $16B |
| Amounts left out as implausible or unconverted | 2 |
| Busiest month | Aug 2025 (11 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 0 | 0 | — | — |  |
| Jun 2025 | 7 | 7 | $877M | $135.5M | █████████████ |
| Jul 2025 | 1 | 1 | $340M | $340M | ██ |
| Aug 2025 | 11 | 10 | $9.8B | $143M | ████████████████████ |
| Sep 2025 | 11 | 8 | $1.5B | $143.9M | ████████████████████ |
| Oct 2025 | 5 | 5 | $2.6B | $602.5M | █████████ |
| Nov 2025 | 5 | 5 | $490M | $117.5M | █████████ |
| Dec 2025 | 2 | 1 | $75M | $75M | ████ |
| Jan 2026 | 11 | 11 | $1.6B | $120M | ████████████████████ |
| Feb 2026 | 9 | 9 | $17.7B | $114.5M | ████████████████ |
| Mar 2026 | 9 | 8 | $21.6B | $800M | ████████████████ |
| Apr 2026 | 3 | 1 | $29M | $29M | █████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 18 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 27 Mar 2026 | Waymo (waymo.com) | Series D | $16B | alphabet, Andreessen Horowitz, bdt & msd partners | — | Mountain View-based Waymo is a mobility technology company that improves transportation by developing self‑driving solutions for travelers… |
| 4 Aug 2025 | Openai (openai.com) | Private Funding Round (Late-stage) | $8.3B ⚠ check sentence | dragoneer investment group, blackstone, tpg | USA | OpenAI has raised a massive $8.3 billion in new funding at a staggering $300 billion valuation. |
| 24 Mar 2026 | Cerebras Systems (cerebras.net) | Series H | $2.8B | 1789 Capital, alpha wave global, altimeter capital | USA |  |
| 24 Oct 2025 | Crusoe (crusoe.ai) | Series E | $1.4B ⚠ check sentence | valor equity partners, Mubadala Capital, 137 ventures | USA | Crusoe, the AI factory company, today announced the initial closing of its anticipated $1.375 billion Series E round, bringing the… |
| 11 Mar 2026 | Vast Data (vastdata.com) | Series E / Late Stage | $1B ⚠ check sentence | nvidia, tiger global, goldman sachs | United States | VAST Data raises $1B in funding to unify AI data infrastructure at $30B valuation. |
| 28 Aug 2025 | Commonwealth Fusion Systems (cfs.energy) | Funding Round (private) | $863M | nvidia, google, breakthrough energy ventures | USA | Commonwealth Fusion Systems (CFS), a Massachusetts-based nuclear fusion startup, closed an $863 million funding round. |
| 23 Mar 2026 | Zipline (zipline.io) | Series H | $800M | paradigm, Fidelity Management & Research Company, baillie… | United States | The additional funds, which included participation from crypto investment firm Paradigm, has pushed Zipline’s recent Series H round to… |
| 24 Mar 2026 | Temporal Technologies (temporal.io) | Series D | $649.5M | amplify partners, Andreessen Horowitz, gic | USA |  |
| 24 Jun 2025 | Moglix (moglix.com) | — | $370M ⚠ check sentence | tiger global, accel, alpha wave global | India | Moglix has raised over $370 million to date. |
| 23 Jul 2025 | Gupshup (gupshup.io) | — | $340M | tiger global, Fidelity Management, Think Investments | United States | In 2021, Gupshup raised two funding rounds within four months, securing $340 million from prominent investors, including Tiger Global,… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Battery Smart (batterysmart.in) | Series B (extended) | $29M | tiger global, blume ventures, ecosystem integrity fund | — | With its $65 million Series B round and $29 million extended Series B round, Battery Smart has raised about $192 million in funding thus… |
| 20 Apr 2026 | Spinny (spinny.com) | Series F | — | Accel Leaders Fund, westbridge, elevation capital | — | Valuedrive Technologies Private Limited, dba Spinny, has raised approximately $340 million across its Series F and its Series G fundraises. |
| 14 Apr 2026 | PopUp Bagels | — | — ⚠ check sentence | tiger global management | — | Tiger Global Management has invested in the PopUp Bagels franchise, which now claims a valuation of $300 million. |
| 27 Mar 2026 | Waymo (waymo.com) | Series D | $16B | alphabet, Andreessen Horowitz, bdt & msd partners | — | Mountain View-based Waymo is a mobility technology company that improves transportation by developing self‑driving solutions for travelers… |
| 24 Mar 2026 | Zipline (zipline.io) | Series H | $200M | fidelity, baillie gifford, valor equity partners | United States | US-based drone logistics company Zipline has raised an additional $200 million, bringing its recent Series H funding round to $800 million. |
| 24 Mar 2026 | Temporal Technologies (temporal.io) | Series D | $649.5M | amplify partners, Andreessen Horowitz, gic | USA |  |
| 24 Mar 2026 | Waymo (waymo.com) | Series D | — ⚠ implausible size | alphabet, Andreessen Horowitz, bdt & msd partners | USA |  |
| 24 Mar 2026 | Cerebras Systems (cerebras.net) | Series H | $2.8B | 1789 Capital, alpha wave global, altimeter capital | USA |  |
| 23 Mar 2026 | Zipline (zipline.io) | Series H | $800M | paradigm, Fidelity Management & Research Company, baillie… | United States | The additional funds, which included participation from crypto investment firm Paradigm, has pushed Zipline’s recent Series H round to… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "Tiger Global" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "Tiger Global" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "Tiger Global" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Tiger Global", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Tiger Global", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Investor names match broadly (a name can match several firms or funds); use a domain for a narrower match.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Benchmark Investments](benchmark-investments.md)
- [General Atlantic Portfolio](general-atlantic-portfolio.md)
- [Founders Fund Portfolio](founders-fund-portfolio.md)
- [NEA Investments](nea-investments.md)
