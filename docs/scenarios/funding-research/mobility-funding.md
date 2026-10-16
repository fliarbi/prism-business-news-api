# Mobility Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “mobility funding” · 20/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [mobility-funding.json](../../examples/scenarios/mobility-funding.json).

**Question.** How many mobility deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “mobility”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 278 |
| With a usable reported amount | 243 |
| Reported total (usable amounts) | $12B |
| Median reported round | $10.2M |
| Largest reported round | $1.7B |
| Amounts left out as implausible or unconverted | 1 |
| Busiest month | Nov 2025 (38 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 11 | 10 | $1.6B | $20.3M | ██████ |
| Jun 2025 | 26 | 25 | $1.2B | $10M | ██████████████ |
| Jul 2025 | 23 | 17 | $754.6M | $18M | ████████████ |
| Aug 2025 | 11 | 8 | $701.9M | $4.2M | ██████ |
| Sep 2025 | 28 | 25 | $901.1M | $10M | ███████████████ |
| Oct 2025 | 21 | 20 | $777.3M | $16.2M | ███████████ |
| Nov 2025 | 38 | 31 | $2.9B | $11M | ████████████████████ |
| Dec 2025 | 17 | 14 | $442.9M | $21M | █████████ |
| Jan 2026 | 25 | 24 | $439.7M | $8.6M | █████████████ |
| Feb 2026 | 26 | 24 | $1.1B | $10.9M | ██████████████ |
| Mar 2026 | 34 | 30 | $1.6B | $6M | ██████████████████ |
| Apr 2026 | 18 | 15 | $324.3M | $7.2M | █████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 11 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 10 Nov 2025 | Sixt Se (sixt.de) | syndicated loan | $1.7B | Bayerische Landesbank, caixabank, commerzbank | Germany | Sixt SE has replaced its previous syndicated loan of EUR 950 million with a new revolving credit line of EUR 1.55 billion ahead of schedule. |
| 7 May 2025 | Nfi Group (nfigroup.com) | revolving credit facility | $845M | national bank of canada, National Bank Financial, Bank of… | Canada | NFI Group Inc. (NFI), a leader in propulsion-agnostic bus and coach mobility solutions, today announced that it and certain of its… |
| 16 Mar 2026 | Ola Electric Mobility (olaelectric.com) | Initial Public Offering | $660M | — | India | In August 2024, Ola Electric Mobility raised Rs 5,500 crore through its initial public offering (IPO). |
| 13 Jun 2025 | New Flyer Holdings, Inc. | Debt Offering | $600M | — | Canada | NFI received net proceeds of approximately $591.7 million, after deduction of certain fees, expenses and commissions. |
| 21 May 2025 | Neot (neotcapital.com) | Equity | $378M | mirova, Alba Infra Partners, banque des territoires | — | This strategic initiative is backed by a new equity commitment of €350 million from Neot’s historical partners: Mirova, Alba Infra… |
| 12 Feb 2026 | Vtg (vtgdefense.com) | Loan | $367.2M | KfW IPEX-Bank | Germany | KfW IPEX-Bank arranges and syndicates funding loans for VTG Frankfurt am Main (ots) - - KfW IPEX-Bank acts as Sole Mandated Lead Arranger… |
| 22 Aug 2025 | Zenobē (zenobe.com) | senior debt | $351M | kkr, infracapital, Crédit Agricole CIB | — | Crédit Agricole CIB has joined a €325 million (US $355 million) senior debt financing package to support Zenobē’s rapid expansion across… |
| 10 Nov 2025 | Vay Technology | Potential Additional Investment | $350M | grab | — | The additional US$350 million that Grab plans to invest within the first year after the US$60 million deal closes |
| 6 Nov 2025 | Spotawheel (spotawheel.com) | equity and debt financing | $324M | pollen street capital | Greece | Today, Spotawheel has raised €300 million in equity and debt financing from prominent European investors, including a senior secured… |
| 18 Mar 2026 | Pmi Electro Mobility (pmielectro.com) | — | $310M | kkr | India | KKR’s decision to invest up to $310 million in PMI Electro Mobility marks a turning point in India’s electric bus market, signalling a… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 28 Apr 2026 | Kovon | pre-seed | $250k | TDV Partners | India | Kovon, a cross-border workforce mobility platform, has raised $250,000 in a pre-seed funding round led by TDV Partners. |
| 28 Apr 2026 | Dodai (dodai.co) | Series A | $13M | British International Investment | Ethiopia | British International Investment (BII), the UK’s development finance institution and impact investor, has committed $5 million in debt… |
| 21 Apr 2026 | Surf Air Mobility (surfairmobility.com) | registered direct offering | $15M | institutional investors | United States | The gross proceeds to the Company from the offering were approximately $15 million , before deducting financial advisor's fees and other… |
| 20 Apr 2026 | Sarla Aviation (sarla-aviation.com) | — | — | IndiGo Ventures | India | Sarla Aviation and IndiGo have announced a strategic equity investment of ₹10 crore by IndiGo Ventures in Sarla Aviation. |
| 16 Apr 2026 | Nawgati (nawgati.com) | Series A | $5.2M ⚠ check sentence | — | India | Nawgati, India&#39;s leading fuel-tech company, is in advanced discussions to raise $5.2 million in its upcoming Series A funding round,… |
| 16 Apr 2026 | Zum (ridezum.com) | — | $100M ⚠ check sentence | tpg | United States | Zūm, the leader in Connected Mobility Experience (CMX™), today announced a $100 million strategic investment from TPG, bringing the… |
| 15 Apr 2026 | Faraday Future Intelligent Electric Inc. | — | $12M | Gold King Arthur Holding Limited | USA | today announced that it has amended and restated the securities purchase agreement, initially entered into on February 4, 2026 (the… |
| 15 Apr 2026 | Glydways (glydways.com) | Series C | $170M | suzuki motor corporation, acs group, khosla ventures | United States | Glydways has raised US$170m in an oversubscribed Series C co-led by Suzuki Motor Corporation, ACS Group, and Khosla Ventures. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector mobility --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector mobility --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector mobility --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "mobility", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "mobility", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Edtech Funding](edtech-funding.md)
- [Web3 Funding](web3-funding.md)
- [Bridge Round Funding](bridge-round-funding.md)
- [Climate Tech Funding](climate-tech-funding.md)
