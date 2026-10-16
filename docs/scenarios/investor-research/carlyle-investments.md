# Carlyle Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “carlyle investments” · 30/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [carlyle-investments.json](../../examples/scenarios/carlyle-investments.json).

**Question.** Which rounds did Carlyle appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Carlyle”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 55 |
| With a usable reported amount | 45 |
| Reported total (usable amounts) | $26.3B |
| Median reported round | $313.2M |
| Largest reported round | $8.5B |
| Amounts left out as implausible or unconverted | 2 |
| Busiest month | Mar 2026 (15 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 1 | 0 | — | — | █ |
| Jun 2025 | 6 | 3 | $1.6B | $801.2M | ████████ |
| Jul 2025 | 2 | 2 | $4.7B | $2.4B | ███ |
| Aug 2025 | 1 | 0 | — | — | █ |
| Sep 2025 | 4 | 4 | $350.3M | $175.1M | █████ |
| Oct 2025 | 10 | 6 | $10.1B | $700M | █████████████ |
| Nov 2025 | 3 | 3 | $669.3M | $89.5M | ████ |
| Dec 2025 | 2 | 2 | $475.2M | $237.6M | ███ |
| Jan 2026 | 1 | 1 | $30M | $30M | █ |
| Feb 2026 | 5 | 5 | $2.7B | $252M | ███████ |
| Mar 2026 | 15 | 15 | $4.5B | $145M | ████████████████████ |
| Apr 2026 | 5 | 4 | $2.3B | $875M | ███████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 23 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 13 Oct 2025 | Basf Coatings (basf-coatings.com) | — | $8.5B | basf, carlyle, qatar investment authority | — | BASF and global investment firm Carlyle are investing £6.7bn in BASF Coatings |
| 15 Jul 2025 | Yes Bank (yesbank.in) | equity | $2.7B | sumitomo mitsui financial group, carlyle | India | The fresh investment would bring the total amount to $2.7 billion, giving SMFG a roughly 25% stake in Yes Bank. |
| 16 Feb 2026 | The Very Group (theverygroup.com) | securitisation | $2.2B | carlyle | United Kingdom | The Very Group extended its £1.77bn UK securitisation facility to February 2029 |
| 3 Jul 2025 | Diversified Energy (div.energy) | — | $2B | carlyle | USA | A recently announced partnership with Carlyle intends to invest USD2 billion in U.S. natural gas and oil assets, expected to boost… |
| 19 Jun 2025 | Trucordia | equity | $1.3B | Carlyle Group | USA | The refinancing coincides with a $1.3bn investment from the Carlyle Group, announced earlier this month. |
| 1 Apr 2026 | Nxtra Data (nxtradata.com) | — | $1B | alpha wave global, carlyle, Anchorage Capital | India | The company’s announcement of a $1 billion investment in Nxtra Data by global investors including Alpha Wave Global, Carlyle and Anchorage… |
| 29 Apr 2026 | Bridgepointe Technologies (bridgepointetechnologies.com) | senior debt | $875M | morgan stanley private credit, Carlyle AlpInvest,… | USA | Morgan Stanley Investment Management announced today that funds managed by Morgan Stanley Private Credit have led an $875 million senior… |
| 21 Oct 2025 | FCA Re | — | $700M | fortitude re, carlyle, T&D Insurance Group | Bermuda | FCA Re is capitalized with more than $700 million in deployable capital, comprising both equity and anticipated debt capacity. |
| 20 Oct 2025 | NEP Group (nepgroup.com) | — | $700M | 26North Partners, carlyle | — | 26North Partners has led a $700m investment in the NEP Group events and broadcast technology company. |
| 24 Nov 2025 | Spicejet (spicejet.com) | Equity | $529M | carlyle aviation partners | India | The budget carrier recently completed the allotment of equity shares to Carlyle Aviation Partners. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Orbcomm (orbcomm.com) | Refinancing | $460M | carlyle, Bain Credit’s Private Credit Group, morgan… | — | Orbcomm has closed a $460 million refinancing that the company says will support growth initiatives and large-scale customer deployments… |
| 29 Apr 2026 | Bridgepointe Technologies (bridgepointetechnologies.com) | senior debt | $875M | morgan stanley private credit, Carlyle AlpInvest,… | USA | Morgan Stanley Investment Management announced today that funds managed by Morgan Stanley Private Credit have led an $875 million senior… |
| 10 Apr 2026 | Bridgepointe Technologies (bridgepointetechnologies.com) | growth investment | — | charlesbank capital partners, Carlyle AlpInvest | — | Bridgepointe Technologies announced a growth investment led by Charlesbank Capital Partners, with participation from Carlyle AlpInvest,… |
| 1 Apr 2026 | Nxtra Data (nxtradata.com) | — | $1B | alpha wave global, carlyle, Anchorage Capital | India | The company’s announcement of a $1 billion investment in Nxtra Data by global investors including Alpha Wave Global, Carlyle and Anchorage… |
| 31 Mar 2026 | Nxtra (nxtra.in) | Strategic | $1B | alpha wave global, carlyle, Anchorage Capital | India | Bharti Airtel’s data centre subsidiary Nxtra has raised $1 billion (around Rs 9,400 crore) in a strategic funding round led by Alpha Wave… |
| 31 Mar 2026 | Nxtra (nxtra.in) | investment | $965M | alpha wave global, carlyle, Bharti Airtel | India | Alpha Wave Global and Carlyle have each committed $435 million and $240 million, respectively, to the data centre company, with Airtel… |
| 31 Mar 2026 | Nxtra (Nxtra Data Ltd) | — | $1B | alpha wave global, carlyle, Anchorage Capital | India | Bharti Airtel Ltd announced on Monday,31 March, a new financial infusion of around $1 billion into its data centre subsidiary Nxtra, as… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Carlyle --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Carlyle --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Carlyle --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Carlyle", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Carlyle", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Softbank Investments](softbank-investments.md)
- [Hillhouse Investments](hillhouse-investments.md)
- [Warburg Pincus Portfolio](warburg-pincus-portfolio.md)
- [Benchmark Investments](benchmark-investments.md)
