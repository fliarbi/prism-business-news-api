# E-commerce Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “e-commerce funding” · volume below estimate threshold  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [e-commerce-funding.json](../../examples/scenarios/e-commerce-funding.json).

**Question.** How many e-commerce deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “e-commerce”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 208 |
| With a usable reported amount | 184 |
| Reported total (usable amounts) | $37.6B |
| Median reported round | $12M |
| Largest reported round | $15B |
| Busiest month | Aug 2025 (27 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 5 | 5 | $65.2M | $5.4M | ████ |
| Jun 2025 | 19 | 17 | $524.5M | $32.5M | ██████████████ |
| Jul 2025 | 12 | 8 | $724.9M | $4.8M | █████████ |
| Aug 2025 | 27 | 24 | $280.7M | $8.4M | ████████████████████ |
| Sep 2025 | 22 | 19 | $3.4B | $9M | ████████████████ |
| Oct 2025 | 14 | 14 | $1.3B | $59M | ██████████ |
| Nov 2025 | 13 | 13 | $15.3B | $2.7M | ██████████ |
| Dec 2025 | 20 | 16 | $2B | $18M | ███████████████ |
| Jan 2026 | 18 | 18 | $1.2B | $7M | █████████████ |
| Feb 2026 | 21 | 16 | $8.3B | $12M | ████████████████ |
| Mar 2026 | 24 | 23 | $2.1B | $65M | ██████████████████ |
| Apr 2026 | 13 | 11 | $2.4B | $10M | ██████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 14 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 20 Nov 2025 | Amazon.com, Inc. | — | $15B | goldman sachs, J.P. Morgan, morgan stanley | — | On November 20, 2025, Amazon.com, Inc. successfully closed the sale of $14.961 billion in aggregate principal amount of notes with varying… |
| 11 Feb 2026 | Sea Limited (sealimited.com) | — | $8B | — | Singapore | Sea Limited, home to Shopee and Garena, follows closely with nearly $8 billion raised, cementing Singapore's e-commerce dominance. |
| 11 Sep 2025 | Alibaba Group (alibabagroup.com) | Convertible bond | $3.2B | — | — | Alibaba Group Holding Ltd. said that it will raise $3.2 billion through a zero-coupon convertible bond. |
| 20 Apr 2026 | Flipkart (flipkart.com) | pre-IPO | $2.2B | — | India | E-commerce major Flipkart is exploring a $2-2.5 billion (around Rs 18,570-23,213 crore) pre-IPO fundraise, while private‑equity firm KKR… |
| 27 Jan 2026 | Perch (perchinteractive.com) | Equity financing | $775M | softbank group | — | The restructuring wiped out US$775 million of equity financing that SoftBank had led three years earlier |
| 5 Dec 2025 | Mercado Libre | senior unsecured notes | $750M | Citigroup, goldman sachs, J.P. Morgan | — | Mercado Libre (NASDAQ:MELI) has just priced USD 750 million of 4.900% senior unsecured notes due 2033 in its first debt issuance since… |
| 9 Jul 2025 | Dhl Supply Chain (dhl.com) | — | $698.5M | — | — | DHL Supply Chain today announced an investment of £550 million (€637 million) to expand its infrastructure and accelerate the deployment… |
| 19 Oct 2025 | Meesho (meesho.com) | equity | $510M | elevation capital, peak xv partners, Highway Series 1 | India | Bengaluru-based online marketplace Meesho has filed its updated draft red herring prospectus (UDRHP) with the SEBI to raise up to ₹4,250… |
| 16 Mar 2026 | Quince (quince.com) | — | $500M | iconiq capital, wellington management, dst global | United States | Online retailer Quince has raised $500 million in funding, valuing the company at $10.1 billion. |
| 20 Dec 2025 | Noon (noon.energy) | — | $500M | public investment fund, Mohammed Alabbar | — | Middle East e-commerce platform noon has raised $500 million in new funding from existing backers, including Saudi Arabia’s Public… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Shiprazor (shiprazor.com) | seed | $2.6M | norrsken22, aaic, e4e | South Africa | Shiprazor, the Cape Town-based e-commerce merchant technology and smart logistics platform, has raised $2.65 million (R44m) in seed… |
| 30 Apr 2026 | Pratech Brands (pratechbrands.com) | Series A | $10.6M | IvyCap Ventures Fund III, First Bridge India Growth Fund | India | Pratech Brands Private Limited, the parent company of Hyugalife, has raised $10.6 million (~₹100 crore) from a Series A fundraise led by… |
| 28 Apr 2026 | Cube (cubesoftware.com) | Series A | $3.7M | Betatron, M Venture Partners | Thailand | Cube, an e-commerce data intelligence startup, has raised USD 3.7 million in a Series A funding round led by Betatron, with participation… |
| 28 Apr 2026 | Swanky (swankyagency.com) | — | $9.7M | yfm equity partners | United Kingdom | Swanky has received a £7.6m investment from YFM Equity Partners to fund its next phase of growth. |
| 27 Apr 2026 | Vinted (vinted.com) | primary funding round | — | tpg | Lithuania | In 2024 it brought in fresh investors in a round led by US investment group TPG, valuing it at $5bn. |
| 20 Apr 2026 | Flipkart (flipkart.com) | pre-IPO | $2.2B | — | India | E-commerce major Flipkart is exploring a $2-2.5 billion (around Rs 18,570-23,213 crore) pre-IPO fundraise, while private‑equity firm KKR… |
| 16 Apr 2026 | Neato (neato.com) | growth capital | $25M | advantage capital | — | Neato announced it has raised $25 million in growth capital to expand its second-party (2P) eCommerce model across global marketplaces.… |
| 10 Apr 2026 | Minoxidil Bay | Growth | — | Shopify Capital | Canada | Minoxidil Bay, Canada’s trusted online destination for premium hair regrowth products, announced today the expansion of its business… |
| 9 Apr 2026 | Aya (ayacare.com) | Series A | $7M | raed ventures, Nuwa Capital, Sanabil Investments | Saudi Arabia | Aya, a Saudi Arabia-based e-commerce platform focused on demand-driven fashion, has raised $7 million in a Series A round led by RAED… |
| 7 Apr 2026 | Homzmart (homzmart.com) | founding round | $23M | stv, impact46, Outliers Ventures | — | Egyptian e-commerce platform Homzmart raised $23 million in its latest founding round from Riyadh-based venture capital fund STV where… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector e-commerce --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector e-commerce --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector e-commerce --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "e-commerce", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "e-commerce", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Construction Tech Funding](construction-tech-funding.md)
- [Defence Tech Funding](defence-tech-funding.md)
- [Foodtech Funding](foodtech-funding.md)
- [Hrtech Funding](hrtech-funding.md)
