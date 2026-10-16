# Bridge Round Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “bridge round funding” · 30/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [bridge-round-funding.json](../../examples/scenarios/bridge-round-funding.json).

**Question.** How many bridge round deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** round type “bridge”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 140 |
| With a usable reported amount | 118 |
| Reported total (usable amounts) | $16B |
| Median reported round | $5M |
| Largest reported round | $6.5B |
| Amounts left out as implausible or unconverted | 4 |
| Busiest month | Sep 2025 (23 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 12 | 11 | $100.5M | $3.9M | ██████████ |
| Jun 2025 | 11 | 8 | $144.7M | $1.9M | ██████████ |
| Jul 2025 | 10 | 9 | $143.5M | $2.2M | █████████ |
| Aug 2025 | 22 | 21 | $983.5M | $12.3M | ███████████████████ |
| Sep 2025 | 23 | 19 | $83.6M | $10M | ████████████████████ |
| Oct 2025 | 11 | 10 | $17.4M | $1.6M | ██████████ |
| Nov 2025 | 9 | 8 | $11.9B | $125M | ████████ |
| Dec 2025 | 12 | 10 | $456.3M | $10M | ██████████ |
| Jan 2026 | 3 | 3 | $921.2M | $20M | ███ |
| Feb 2026 | 10 | 8 | $45.8M | $1.2M | █████████ |
| Mar 2026 | 9 | 4 | $1.4B | $81.1M | ████████ |
| Apr 2026 | 8 | 7 | $114.9M | $4M | ███████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 18 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 11 Nov 2025 | Ampere (ampere.cars) | bridge loan | $6.5B | — | — | a $6.5 billion bridge loan arranged for the acquisition of Ampere |
| 11 Nov 2025 | St Telemedia Global Data Centres (stt Gdc) (sttelemediagdc.com) | bridge loan | $5B | kkr, singtel | Singapore | Singapore - A consortium comprising KKR and Singtel is in talks with banks for a loan of around $5 billion to support its proposed… |
| 23 Mar 2026 | Companhia Siderúrgica Nacional (csn.com.br) | bridge loan | $1.2B | morgan stanley, Citigroup, credit agricole | Brazil | Companhia Siderúrgica Nacional (CSN), the Brazilian steel and iron ore producer, received from a pool of banks a bridge loan in the amount… |
| 5 Jan 2026 | Sonida Senior Living (sonidaseniorliving.com) | Bridge loan | $900M | rbc capital markets, bmo capital markets, Citizens Bank,… | United States | At the time of the Merger Agreement announcement, a 364-day committed bridge financing (“Bridge Loan Facility”) of $900 million was… |
| 28 Aug 2025 | Gerresheimer Ag (gerresheimer.de) | bridge financing | $567M | — | Germany | the remaining bridge financing of around EUR 525 million |
| 16 Dec 2025 | Encavis (encavis.com) | Bridge financing | $216M | — | Germany | ENCAVIS secures a non-recourse bridge financing of EUR 200 million for the acquisition of the Italian solar portfolio "Giotto" (265 MW). |
| 15 Dec 2025 | Ivanhoe Electric (ivanhoeelectric.com) | Bridge Facility | $200M | national bank of canada, bmo capital markets, societe… | United States | Ivanhoe Electric's wholly-owned subsidiary, Mesa Cobre Holding Corporation, has closed its previously announced senior secured multi-draw… |
| 2 Mar 2026 | Mdh Partners (mdhpartners.com) | bridge debt | $160M | acore capital | US | MDH Partners has landed $160 million of bridge debt to refinance a portfolio of 10 warehouse properties spread among six states,… |
| 4 Aug 2025 | FuriosaAI | Series C bridge | $127.5M | Korea Development Bank, industrial bank of korea, ibk… | South Korea | South Korean AI chip startup FuriosaAI has entered the ranks of the country’s unicorn companies following its ₩170 billion KRW (~$130… |
| 18 Nov 2025 | Clipper Equity (clipperequity.com) | bridge debt | $125M | valley national bank | USA | Clipper Equity has nabbed $125 million of bridge debt for a multifamily development in Flatbush, Brooklyn, at the site of a Sears building… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 29 Apr 2026 | Authid (authid.ai) | Bridge Loan Financing | $4M | — | United States | authID Announces $4,000,000 Bridge Loan Financing 29.04.26 15:45. |
| 28 Apr 2026 | Solidion Technology (solidiontech.com) | bridge facility | — | madison | United States | Madison Bond LLC is a primary stakeholder and long-term investor of Solidion Technology. |
| 23 Apr 2026 | Lifezone Metals (lifezonemetals.com) | Bridge Loan | $25M | Taurus Mining Finance Fund No. 2 L.P. | United States | Current pre-FID, early-stage work, and project financing activities at the Kabanga Nickel Project will continue to be funded via the $60… |
| 22 Apr 2026 | Galeria (galeria.de) | bridge loan | $10.8M | bain capital | Germany | The chain of stores receives a total of ten million euros through this interim financing. |
| 21 Apr 2026 | Wyld Networks (wyldnetworks.com) | bridge loan | $142.5k | Aramia AB | Sweden | Wyld Networks AB has entered into an agreement for a bridge loan of SEK 1.5 million with Aramia AB. |
| 16 Apr 2026 | Norse Atlantic Airways (flynorse.com) | Bridge Loan | $70M | — | Norway | Bridge loan facility of USD70 million to fund the liquidity needs pending completion of the rights issue. |
| 14 Apr 2026 | Prestamype (prestamype.com) | investment bridge | $2M | alive ventures, oikocredit, Salkantay Ventures | Peru | Prestamype, the Peruvian company leading in digital financial services focused on micro, small and medium-sized enterprises (mipymes),… |
| 3 Apr 2026 | PhageLab | Bridge | $3M | Kaszek Ventures | Chile | PhageLab secured a $3 million bridge round led by Kaszek Ventures, bringing its total capital raised to approximately $40 million. |
| 31 Mar 2026 | Nuvilab (nuvilab.com) | Series A bridge | — | NAVER D2SF | — | NAVER Corporation’s venture arm, NAVER D2SF, has made follow-on investments in Nuvilab and Soundable Health, extending earlier seed… |
| 27 Mar 2026 | Openai (openai.com) | bridge financing | — ⚠ implausible size | softbank group | Japan | SoftBank Group has formalized a 40 billion-dollar bridge financing agreement (34,636 million euros) to continue its ambitious investment… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --round-type bridge --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --round-type bridge --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --round-type bridge --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"round_type": "bridge", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"round_type": "bridge", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Web3 Funding](web3-funding.md)
- [Mobility Funding](mobility-funding.md)
- [Climate Tech Funding](climate-tech-funding.md)
- [Growth Stage Funding](growth-stage-funding.md)
