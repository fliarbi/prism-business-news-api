# GIC Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “gic portfolio” · 40/month India · 70/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [gic-portfolio.json](../../examples/scenarios/gic-portfolio.json).

**Question.** Which rounds did GIC appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “GIC”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 525 |
| With a usable reported amount | 474 |
| Reported total (usable amounts) | $186.9B |
| Median reported round | $12.2M |
| Largest reported round | $25B |
| Amounts left out as implausible or unconverted | 6 |
| Busiest month | Oct 2025 (57 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 37 | 37 | $1.3B | $6.1M | █████████████ |
| Jun 2025 | 35 | 33 | $879.5M | $5.6M | ████████████ |
| Jul 2025 | 38 | 30 | $16.4B | $18M | █████████████ |
| Aug 2025 | 44 | 41 | $833.5M | $8.7M | ███████████████ |
| Sep 2025 | 46 | 45 | $25.7B | $11.9M | ████████████████ |
| Oct 2025 | 57 | 48 | $13.5B | $12M | ████████████████████ |
| Nov 2025 | 41 | 36 | $23.4B | $12.4M | ██████████████ |
| Dec 2025 | 42 | 40 | $12.1B | $25M | ███████████████ |
| Jan 2026 | 39 | 33 | $61.9B | $10M | ██████████████ |
| Feb 2026 | 55 | 46 | $30.2B | $12.5M | ███████████████████ |
| Mar 2026 | 46 | 44 | $5.3B | $30M | ████████████████ |
| Apr 2026 | 45 | 41 | $2.2B | $19.9M | ████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 21 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 19 Jan 2026 | Anthropic (anthropic.com) | — | $25B | gic, coatue, sequoia capital | United States | the venture capital giant is participating in a round led by Singapore sovereign wealth fund GIC and US investor Coatue, each of which is… |
| 25 Nov 2025 | Nextdecade (next-decade.com) | project financing | $18.4B | gic | USA | Sidley is representing GIC in connection with its commitment to NextDecade Corporation’s (NextDecade) (NASDAQ: NEXT) Phase 1, US$18.4… |
| 24 Sep 2025 | TenneT Germany | — | $10.3B | apg, gic, Norges Bank Investment Management | Germany | Combined, the three investors will inject 9.5 billion euro of new equity until 2029 and will collectively own 46 percent of the company. |
| 1 Jul 2025 | Xai (x.ai) | equity | $10B ⚠ check sentence | morgan stanley, Strategic equity investors | US | Morgan Stanley confirmed Tuesday that the company has secured $10 billion in total funding to expand Grok AI and build massive GPU… |
| 10 Feb 2026 | Databricks (databricks.com) | Series K | $5B ⚠ check sentence | qatar investment authority, Singapore Temasek, Macquarie… | United States | United States data & artificial intelligence (AI) company Databrick has raised $5 billion funding at $134 billion valuation, and with… |
| 10 Feb 2026 | Nitel (nitelusa.com) | acquisition | $2.5B | china unicom, minerva, GiCell | Nigeria | Nigeria’s former state telecoms monopoly, Nitel, has received a $2.5bn offer for a majority stake from a consortium comprising of China… |
| 3 Feb 2026 | Vulcan Energy (v-er.eu) | — | $2.4B | hochtief, Institutional Investors, Retail Investors | Germany | Secured a comprehensive €2.2 billion ($3.9 billion) financing package to fund the construction and development of Phase One Lionheart… |
| 26 Mar 2026 | Shield AI (shield.ai) | Series G | $2B | advent international, JPMorgan Chase's Strategic… | United States | The startup said on Thursday the Series G round was led by Advent International and co‑led by JPMorgan Chase's Strategic Investment Group,… |
| 10 Oct 2025 | Reflection AI (reflectionai.ca) | — | $2B ⚠ check sentence | nvidia, disruptive, dst | United States | Reflection AI on Friday raised $2 billion at an $8 billion valuation, surpassing its previous valuation just seven months ago by 15x from… |
| 10 Dec 2025 | Celsa (celsa.com.co) | debt refinancing | $1.9B | Strategic Value Partners, LLC and its affiliates (SVP) | UK | Celsa has announced the successful completion of its refinancing. As part of the transaction, Celsa is issuing €600m of HoldCo PIK notes,… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Fuelwood (fuelwood.co.uk) | — | $3.2M | strategic investor consortium | — | a further €3 million will be injected into a newly created subsidiary, Fuelwood Finland Oy. |
| 30 Apr 2026 | Cindrigo Holdings (cindrigo.com) | — | $14M | strategic investor consortium | — | Cindrigo Holdings shares climbed sharply on Wednesday after the company unveiled an £11 million funding package alongside a new biomass… |
| 28 Apr 2026 | Voicecomm (myvoicecomm.com) | Subscription | $24.8M | State Fortune Global Strategic LPF | China | the issue of new H Shares to State Fortune Global Strategic LPF was successfully completed on 27 April 2026. |
| 27 Apr 2026 | VisionSys AI Inc. | Proposed strategic investment | $90M | a strategic investor | USA | Based on the terms currently under discussion, the investor plans to invest a total of $90 million in VSA at a price of $1.50 per share. |
| 26 Apr 2026 | Cresora Commerce | seed style | $4M | nashville capital network, strategic private investors | USA | The seed style investment exceeded $4 million, led by Nashville Capital Network with participation from strategic private investors, to… |
| 24 Apr 2026 | Salmon Group (salmongroup.no) | Financing | $100M | Spice Expeditions, Washington University Investment… | Philippines | Salmon raises $100m to fuel Philippines expansion Salmon Group, a technology-driven financial services holding company building a banking… |
| 24 Apr 2026 | Allied Critical Metals (alliedcritical.com) | Debt | $15M | existing strategic investor | Canada | Beyond equity, the tungsten miner has secured a five-year, US$15 million financing facility with its existing strategic investor to build… |
| 24 Apr 2026 | Allied Critical Metals (alliedcritical.com) | Equity | $25M | new strategic investor, existing strategic investor | Canada | The cornerstone of this announcement is a US$25 million non-brokered private placement. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor GIC --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor GIC --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor GIC --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "GIC", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "GIC", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Google Ventures Portfolio](google-ventures-portfolio.md)
- [Plug and Play Investments](plug-and-play-investments.md)
- [Atomico Investments](atomico-investments.md)
- [Dst Global Portfolio](dst-global-portfolio.md)
