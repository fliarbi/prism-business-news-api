# Prosus Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “prosus investments” · 30/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [prosus-investments.json](../../examples/scenarios/prosus-investments.json).

**Question.** Which rounds did Prosus appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Prosus”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 103 |
| With a usable reported amount | 88 |
| Reported total (usable amounts) | $11.7B |
| Median reported round | $23.5M |
| Largest reported round | $4.4B |
| Busiest month | Sep 2025 (23 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 7 | 7 | $62.3M | $13.5M | ██████ |
| Jun 2025 | 9 | 5 | $45.8M | $7.9M | ████████ |
| Jul 2025 | 10 | 10 | $281.7M | $22.4M | █████████ |
| Aug 2025 | 10 | 8 | $3.3B | $31.5M | █████████ |
| Sep 2025 | 23 | 23 | $2.5B | $27M | ████████████████████ |
| Oct 2025 | 12 | 12 | $607.9M | $47M | ██████████ |
| Nov 2025 | 4 | 4 | $4.6B | $48.2M | ███ |
| Dec 2025 | 3 | 1 | $54M | $54M | ███ |
| Jan 2026 | 4 | 4 | $168.5M | $45.2M | ███ |
| Feb 2026 | 3 | 3 | $32M | $15.8M | ███ |
| Mar 2026 | 17 | 10 | $176.6M | $14.7M | ███████████████ |
| Apr 2026 | 1 | 1 | $18M | $18M | █ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 23 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 21 Nov 2025 | Just Eat Takeaway.com (justeattakeaway.com) | Acquisition | $4.4B | prosus | — | buying Just Eat Takeaway.com for 4.1 billion euros |
| 5 Aug 2025 | Ifood (ifood.com.br) | — | $3.1B | prosus | Brazil | The Brazilian food delivery application iFood, owned by the Dutch investment group Prosus PRX.AS, announced on Tuesday direct investments… |
| 11 Sep 2025 | Eruditus (eruditus.com) | Equity | $741M ⚠ check sentence | prosus, TPG Rise Fund, peak xv partners | — | Eruditus, which has raised a total of $741 million in equity funding from 27 investors including Prosus, TPG Rise Fund, Peak XV Partners… |
| 24 Sep 2025 | Rapido (rapido.bike) | mixed primary and secondary share sales | $570M | prosus, westbridge capital | India | People familiar with the matter said the primary infusion is pegged at $300 million, led by Prosus with $240–250 million, and WestBridge… |
| 2 Jul 2025 | Klar (klar.mx) | — | $190M | general atlantic, Grupo Santander, sdg | Mexico | Klar, a Mexican neobank, recently announced the raising of $190 million in a new round of financing, consisting of $170 million in capital… |
| 10 Oct 2025 | Le Travenues Technologies | — | $156M | prosus | India | Gurugram-based Le Travenues Technologies, the parent company of Ixigo, said it will use part of its ₹1,300 crore fundraise to expand its… |
| 10 Oct 2025 | Ixigo (ixigo.com) | INVESTMENT | $156M | prosus | — | Dutch investment group Prosus will invest INR 13 billion (around $146 million) in Indian online travel company Ixigo for a 10.1% stake. |
| 20 Aug 2025 | Bluestone (bluestone.com) | funding_round | $108M | peak xv partners, prosus, steadview capital | India | BlueStone had closed a Rs 900-crore funding round—a combination of primary and secondary transactions—in August 2024, which saw the… |
| 3 Mar 2026 | Flink (miflink.com) | Growth Capital | $100M | prosus, btomorrow ventures | Germany | Flink has secured around US$100 million in new funding led by Prosus, with Btomorrow Ventures joining as a new investor. |
| 10 Sep 2025 | Cuspai (cusp.ai) | Series A | $100M | new enterprise associates, temasek, nventures | UK | The startup behind a platform for developing new materials to tackle global sustainability and clean energy challenges has secured more… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 3 Apr 2026 | Mevo (mevo.com) | — | $18M | prosus, matrix, Jefferson River Capital | Brazil | Mevo raised $18 million in a round led by Prosus, with participation from Matrix, Jefferson River Capital, and Floating Point. |
| 27 Mar 2026 | Deccan AI | — | $25M | Susquehanna, prosus ventures | USA | Deccan AI is focusing hard on super accuracy, and has just raised $25M to push that mission forward. The round was led by A91 Partners,… |
| 26 Mar 2026 | Dognosis (dognosis.tech) | — | — ⚠ check sentence | accel, prosus | India | Startups can obtain up to $2 million in total funding from investors with check sizes ranging from $200,000 to $1 million. |
| 26 Mar 2026 | QOSMIC | — | — ⚠ check sentence | accel, prosus | India | Startups can obtain up to $2 million in total funding from investors with check sizes ranging from $200,000 to $1 million. |
| 26 Mar 2026 | Ethereal Exploration Guild | — | — ⚠ check sentence | accel, prosus | India | Startups can obtain up to $2 million in total funding from investors with check sizes ranging from $200,000 to $1 million. |
| 26 Mar 2026 | CodeKarma | — | — | prosus | — | Through 2025, the technology investor deployed $675 million in companies such as Urban Company, PayU, Rapido, Ixigo, Wiom, Deccan AI,… |
| 26 Mar 2026 | Arivihan (arivihan.com) | — | — | prosus | — | Through 2025, the technology investor deployed $675 million in companies such as Urban Company, PayU, Rapido, Ixigo, Wiom, Deccan AI,… |
| 26 Mar 2026 | Wiom (wiom.in) | — | — | prosus | — | Through 2025, the technology investor deployed $675 million in companies such as Urban Company, PayU, Rapido, Ixigo, Wiom, Deccan AI,… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Prosus --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Prosus --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Prosus --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Prosus", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Prosus", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [GV Investments](gv-investments.md)
- [Intel Capital Portfolio](intel-capital-portfolio.md)
- [Breakthrough Energy Ventures Portfolio](breakthrough-energy-ventures-portfolio.md)
- [Index Ventures Portfolio](index-ventures-portfolio.md)
