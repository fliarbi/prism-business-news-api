# Gaming Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “gaming funding” · 260/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [gaming-funding.json](../../examples/scenarios/gaming-funding.json).

**Question.** How many gaming deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “gaming”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 175 |
| With a usable reported amount | 155 |
| Reported total (usable amounts) | $44.1B |
| Median reported round | $11M |
| Largest reported round | $12B |
| Busiest month | Jan 2026 (32 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 13 | 11 | $3B | $13.5M | ████████ |
| Jun 2025 | 9 | 9 | $815.6M | $3.7M | ██████ |
| Jul 2025 | 18 | 14 | $4.8B | $10.9M | ███████████ |
| Aug 2025 | 20 | 14 | $563.2M | $10M | ████████████ |
| Sep 2025 | 12 | 11 | $357.7M | $5M | ████████ |
| Oct 2025 | 12 | 12 | $433.2M | $15M | ████████ |
| Nov 2025 | 5 | 5 | $1.5B | $10.5M | ███ |
| Dec 2025 | 6 | 5 | $15.9M | $1.8M | ████ |
| Jan 2026 | 32 | 27 | $20.6B | $5M | ████████████████████ |
| Feb 2026 | 9 | 9 | $10.3B | $185M | ██████ |
| Mar 2026 | 8 | 8 | $1.2B | $66M | █████ |
| Apr 2026 | 31 | 30 | $612.1M | $11M | ███████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 14 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 15 Jan 2026 | Savvy Games Group (savvygames.com) | share transfer | $12B | PIF | Saudi Arabia | Saudi Arabia’s Public Investment Fund (PIF) is transferring USD 12 billion worth of gaming company shares to its subsidiary Savvy Games… |
| 11 Feb 2026 | Sea Limited (sealimited.com) | — | $8B | — | Singapore | Sea Limited, home to Shopee and Garena, follows closely with nearly $8 billion raised, cementing Singapore's e-commerce dominance. |
| 15 Jan 2026 | Scopely (scopely.com) | acquisition | $4.9B | savvy games group | — | In 2023, PIF-backed Savvy Games acquired Monopoly Go developer Scopely for USD 4.9 billion. |
| 15 Jan 2026 | Niantic Labs’ Gaming Division | acquisition | $3.5B | savvy games group | — | In 2025, it followed with a USD 3.5 billion acquisition of Niantic Labs’ gaming division, the developer of Pokémon Go. |
| 7 May 2025 | Dream Games (dreamgames.com) | Strategic equity and debt financing | $2.5B | cvc, blackstone, Other investors | Turkey | Turkey-based mobile games developer Dream Games has announced a strategic equity investment from CVC and debt financing from Blackstone… |
| 14 Jul 2025 | Allwyn International | Senior facilities agreement | $2.3B | — | — | Allwyn International has entered a new €2.15 billion ($2.1 billion) senior facilities agreement with a syndicate of international banks. |
| 11 Feb 2026 | Embracer Group (embracer.com) | — | $1.1B | savvy gaming group | Sweden | CEO Releases Letter Lars Wingefor, CEO of Asmodee and Dark Horse parent Embracer Group, has released a letter defending the company’s… |
| 25 Feb 2026 | Gaming and Leisure Properties (glpropinc.com) | public debt | $800M | — | United States | Gaming and Leisure Properties, Inc. (“GLPI”) (NASDAQ: GLPI) today announced the pricing of a public offering of $800,000,000 aggregate… |
| 30 Mar 2026 | Star Entertainment Group (starentertaingroup.com) | Debt Refinancing | $550M | whitehawk capital partners | Australia | Star Entertainment Group has secured a crucial $550 million refinancing deal with WhiteHawk Capital Partners |
| 18 Jun 2025 | Cirsa (cirsa.com) | IPO | $496.8M | — | Spain | The company seeks to raise a total of 460 million euros, with the objective of financing its growth and strengthening its capital… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Sports Entertainment Gaming Global (SEGG) | Convertible promissory notes | $11.8M | — | USA | In March, SEGG agreed to issue unsecured convertible promissory notes to institutional investors with a face value of up to $11.76 million. |
| 30 Apr 2026 | Manamind (manamind.ee) | pre-seed | $1.5M | ewor, ascension, syndicateroom | United Kingdom | London-based ManaMind has raised $1.5 million in a pre-seed funding round to advance its AI-driven game testing platform. |
| 29 Apr 2026 | Metasports Interactive (metasportsinteractive.vdtrxn) | user acquisition (UA) | $20M | metica | — | London-based growth finance firm Metica has provided $20 million in user acquisition (UA) funding to the mobile gaming company Metasports… |
| 29 Apr 2026 | Metasports Interactive (metasportsinteractive.vdtrxn) | other | $8M | prime venture partners, horizon ventures | — | Prime Venture Partners and Horizon Ventures had previously contributed $8 million to Metasports. |
| 27 Apr 2026 | Soloband Games | Series A | — | zubr capital | Cyprus | Soloband Games has raised an undisclosed series A investment to scale its flagship title and expand internationally. |
| 27 Apr 2026 | Hitwicket (hitwicket.com) | user acquisition (UA) funding | $20M | metica | India | The Bengaluru-based studio behind cricket game Hitwicket has secured $20 million in user acquisition (UA) funding from Metica, a… |
| 27 Apr 2026 | Metasports Interactive (metasportsinteractive.vdtrxn) | user acquisition | $10M | metica | India | India-based Metasports Interactive has secured $20 million in user acquisition funding from London-based Metica, the company said in an… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector gaming --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector gaming --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector gaming --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "gaming", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "gaming", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Crypto Funding](crypto-funding.md)
- [Series D Funding](series-d-funding.md)
- [Fintech Funding](fintech-funding.md)
- [SAAS Funding News](saas-funding-news.md)
