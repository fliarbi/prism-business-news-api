# Insurtech Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “insurtech funding” · 10/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [insurtech-funding.json](../../examples/scenarios/insurtech-funding.json).

**Question.** How many insurtech deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “insurtech”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 187 |
| With a usable reported amount | 163 |
| Reported total (usable amounts) | $5.9B |
| Median reported round | $12.2M |
| Largest reported round | $1.6B |
| Busiest month | Jul 2025 (28 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 4 | 3 | $1.8B | $162M | ███ |
| Jun 2025 | 24 | 22 | $364.6M | $11.5M | █████████████████ |
| Jul 2025 | 28 | 23 | $309.3M | $7M | ████████████████████ |
| Aug 2025 | 7 | 7 | $93M | $12M | █████ |
| Sep 2025 | 10 | 8 | $332.9M | $9.2M | ███████ |
| Oct 2025 | 28 | 21 | $324.3M | $13.8M | ████████████████████ |
| Nov 2025 | 11 | 11 | $117M | $10M | ████████ |
| Dec 2025 | 3 | 3 | $168.7M | $4.3M | ██ |
| Jan 2026 | 24 | 20 | $313.9M | $5M | █████████████████ |
| Feb 2026 | 20 | 20 | $1.8B | $23M | ██████████████ |
| Mar 2026 | 15 | 15 | $334M | $23.2M | ███████████ |
| Apr 2026 | 13 | 10 | $199.8M | $9M | █████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 13 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 14 May 2025 | Hub International (hubinternational.com) | minority equity investment | $1.6B ⚠ check sentence | — | United States | HUB International, a global insurance brokerage firm headquartered in Chicago, has secured a landmark $1.6bn minority equity investment,… |
| 27 Feb 2026 | Acko General Insurance (acko.com) | — | $598M | — | India | ACKO has raised $598 million — the highest among all funded InsurTech companies in India as of January 2026. |
| 27 Feb 2026 | Go Digit Insurance | — | $538M ⚠ check sentence | fairfax financial holdings | India | Go Digit Insurance has raised a total funding of over $538 million since 2017 and is reshaping the Indian insurance industry with a… |
| 27 Feb 2026 | Insurancedekho (insurancedekho.com) | — | $362M ⚠ check sentence | — | India | Founded: 2016 \| Headquarters: Gurugram \| Total Funding: $362 million |
| 8 Sep 2025 | Earnix (earnix.com) | Continuation Vehicle | $290M | JVP, TPG GP Solutions | — | JVP, a leading global venture capital firm, announced today the close of a $290 million single-asset Continuation Vehicle in partnership… |
| 26 Dec 2025 | Wefox (wefox.com) | Strategic funding round | $163.1M | searchlight capital partners | Germany | wefox secured €151 million in a strategic funding round in July. The round comprises a €76 million capital raise from existing investors… |
| 29 May 2025 | Empathy (empathy.com) | Series C | $162M | adams street partners, general catalyst, index ventures | USA | InsurTech startup Empathy has raised $72 million in a Series C round to expand its platform for legacy planning and end-of-life services. |
| 4 Jun 2025 | Bolttech (bolttech.io) | Series C | $147M | sumitomo corporation, iberis capital, Dragon Fund | Singapore | With investments totalling US$147 million, bolttech closes Series C with the addition of new investors |
| 13 Mar 2026 | Alan (alan.com) | Series A | $108M ⚠ check sentence | greenoaks, Kaaf, SH | France | Alan valued at €5bn after €100m funding round |
| 13 Jan 2026 | Corgi (corgi.co.uk) | — | $108M | y combinator, kindred ventures, contrary | US | Corgi, a technology-driven insurance company, has secured $108 million in total financing from a group of investors that includes Y… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Qover (qover.com) | growth financing | — | cibc innovation banking | Belgium | CIBC Innovation Banking today announced that it has provided growth financing to Qover, a European-based embedded insurance platform. |
| 27 Apr 2026 | Segura (segura-moto.fr) | seed | $9M | big_bets, Assaf Wand, Marcelo Blay | Brazil | She just lifted her first institutional round, a portentous R$ 45 million seed coliderated by Andreessen Horowitz (a16z) and Kaszek. The… |
| 27 Apr 2026 | Openly (openly.com) | — | $100M | — | US | The insurtech previously raised $US193 million ($269.92 million) in January last year – a round Allianz also participated in – and $US100… |
| 27 Apr 2026 | Openly (openly.com) | — | — | allianz, Eden Global Partners, advance venture partners | US | Allianz has invested more in Boston-based homeowners insurance platform Openly and expanded a reinsurance partnership. |
| 13 Apr 2026 | Insurteam | — | $1.3M | — | Switzerland | Switzerland-based InsurTech firm Insurteam, a travel insurance automation specialist, has closed a $1.3m funding round to accelerate its… |
| 13 Apr 2026 | Eleos Life (eleos.co.uk) | — | $3M | Mercurius Media Capital | United States | InsurTech Eleos Life has secured $3m in capital from Mercurius Media Capital (MMC), a US-based media-for-equity venture fund, to… |
| 13 Apr 2026 | Flora Fertility | Seed | $5M | ManchesterStory, Slauson, TruStage Ventures | United States | Flora Fertility, a Calgary, Alberta, Canada- and Chicago, IL-based fertility insurance platform provider, raised USD$5M in Seed funding. |
| 6 Apr 2026 | Yuzu Health (yuzu.health) | Series A | $35M | general catalyst, chemistry, Anthropic’s Anthology Fund | USA | Yuzu Health, a next-generation third‑party administrator focused on modernizing the infrastructure behind health insurance plans,… |
| 3 Apr 2026 | Policystreet (policystreet.com) | Series C | $21M | cool japan fund, altara ventures, gobi partners | Malaysia | KUALA LUMPUR, 1 APRIL2026 — PolicyStreet, a Malaysian-born regional insurtech company, has secured US$21 million in the first close of its… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector insurtech --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector insurtech --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector insurtech --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "insurtech", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "insurtech", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Growth Stage Funding](growth-stage-funding.md)
- [D2C Funding](d2c-funding.md)
- [Agritech Funding](agritech-funding.md)
- [Proptech Funding](proptech-funding.md)
