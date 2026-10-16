# Crypto Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “crypto funding” · 320/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [crypto-funding.json](../../examples/scenarios/crypto-funding.json).

**Question.** How many crypto deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “crypto”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 105 |
| With a usable reported amount | 100 |
| Reported total (usable amounts) | $38.2B |
| Median reported round | $22.3M |
| Largest reported round | $10B |
| Busiest month | Sep 2025 (17 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2 | 2 | $1.1B | $567.5M | ██ |
| Jun 2025 | 7 | 7 | $5.5B | $40M | ████████ |
| Jul 2025 | 5 | 5 | $175.1M | $4M | ██████ |
| Aug 2025 | 15 | 15 | $10.4B | $21.6M | ██████████████████ |
| Sep 2025 | 17 | 17 | $8.7B | $20M | ████████████████████ |
| Oct 2025 | 12 | 11 | $1.1B | $15M | ██████████████ |
| Nov 2025 | 9 | 8 | $1.6B | $32.4M | ███████████ |
| Dec 2025 | 1 | 1 | $1B | $1B | █ |
| Jan 2026 | 12 | 12 | $264.9M | $14.2M | ██████████████ |
| Feb 2026 | 4 | 4 | $50.7M | $11.2M | █████ |
| Mar 2026 | 11 | 10 | $8B | $100M | █████████████ |
| Apr 2026 | 10 | 8 | $250.7M | $7.9M | ████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 13 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 23 Aug 2025 | ETHZilla | — | $10B | clear street | — | ETHZilla, an Ethereum reserve company, announced plans on August 23 to sell common stock worth up to $10 billion via Clear Street LLC. |
| 16 Mar 2026 | Metaplanet (metaplanet.jp) | stock acquisition rights | $5.4B | — | — | Bloomberg reported a separate, larger capital program of roughly $5.4 billion tied to stock acquisition rights, which moved the share… |
| 12 Jun 2025 | DeFi Development Corp. | Equity Line of Credit | $5B | RK Capital | — | Publicly traded DeFi Development Corp. entered into an agreement for a $5 billion equity line of credit with RK Capital |
| 26 Sep 2025 | Terawulf (terawulf.com) | — | $3.2B | morgan stanley, google | U.S. | Crypto mining company TeraWulf is reportedly raising approximately $3 billion through Morgan Stanley to build data centers. |
| 29 Sep 2025 | Cipher Mining (ciphermining.com) | equity stake | $1.4B | google | — | Last week, Google agreed to backstop $1.4B of Fluidstack’s lease obligations in a 10-year deal with crypto miner Cipher Mining. In return,… |
| 12 Dec 2025 | Jiuzi Holdings, Inc. | Private Placement | $1B | several institutional investors | China | Jiuzi Holdings, Inc. (Nasdaq: JZXN) ("Jiuzi" or the "Company") today announced that it has signed a Memorandum of Understanding ("MOU")… |
| 28 May 2025 | SOL Strategies Inc. | Shelf prospectus | $1B | — | Canada | SOL Strategies Inc. (CSE: HODL), a Vancouver-based company focused on the growth and development of the Solana (SOL) network, announced… |
| 19 Nov 2025 | Kraken (kraken.com) | — | $800M | citadel securities, jane street, drw venture capital | United States | Kraken said the funding will be used to enhance its regulated presence and expand its product suite through organic development and… |
| 5 Mar 2026 | Core Scientific (corescientific.com) | financing facility | $500M | morgan stanley | USA | Core Scientific secured a $500 million financing facility granted by Morgan Stanley through a 364-day loan arrangement, with an expansion… |
| 5 Nov 2025 | Ripple (rippleenergy.com) | Strategic Investment | $500M ⚠ check sentence | fortress investment group, citadel securities, pantera… | USA | Ripple Lands $500M in Funding at $40B Valuation to Build Out Crypto Banking Empire |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 24 Apr 2026 | Robin Markets | angel | $475k | fabric vc, animoca brands, ATKA Incubator | — | Robin Markets has completed a $475,000 angel round led by Fabric VC, with joint leads from Animoca Brands, ATKA Incubator, John Lilic, and… |
| 22 Apr 2026 | Minter (minter.network) | A series | — | east group, legend capital, individual investors | — | Now, the vehicle announced a new contribution, leading an A series at Minter, a company specializing in infrastructure for data centers… |
| 22 Apr 2026 | BetHog | Series A | $10M | will ventures, RockawayX, pcv | US | BetHog has announced a $10 million Series A financing and the launch of Sentient Studios, a new B2B provider that enables casino operators… |
| 21 Apr 2026 | QLink World | Strategic Investment | $20M | foresight ventures | United Arab Emirates | Leading the Web3 super gateways: QLink World received $20 million strategic investment led by Foresight Ventures, aiming to jointly build… |
| 21 Apr 2026 | Eden Block (edenblock.com) | equity investment | — | optiver | — | Optiver has made an equity investment in crypto and AI venture capital fund Eden Block to gain exposure to early-stage AI and digital… |
| 19 Apr 2026 | Maxi Doge | — | $4.3M | — | — | The project has raised roughly $4.3 million |
| 19 Apr 2026 | Pepeto | — | $9.2M | — | — | Pepeto leads with over $9.2 million raised, a SolidProof audit, and a confirmed Binance listing |
| 17 Apr 2026 | NectarFi | seed | $170k | — | Nigeria | The startup raised early funding alongside its public launch, having already onboarded more than 1,000 users across Nigeria, South Africa,… |
| 14 Apr 2026 | Payward | Strategic Investment | $200M | German stock exchange | Germany | The broker from Eschborn near Frankfurt acquires a share of 1.5 percent of the Kraken parent company Payward for 200 million dollars, as… |
| 1 Apr 2026 | Ozak AI | Presale | $6.6M | — | — | Currently, Ozak AI has raised over $6.58 million in presale funding, and over 1.156 billion OZ tokens have been sold. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector crypto --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector crypto --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector crypto --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "crypto", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "crypto", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Series C Funding](series-c-funding.md)
- [Biotech Funding News](biotech-funding-news.md)
- [Series D Funding](series-d-funding.md)
- [Gaming Funding](gaming-funding.md)
