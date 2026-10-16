# Series C Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “series c funding” · 140/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [series-c-funding.json](../../examples/scenarios/series-c-funding.json).

**Question.** How many series c deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** round type “series c”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 817 |
| With a usable reported amount | 767 |
| Reported total (usable amounts) | $104.9B |
| Median reported round | $70M |
| Largest reported round | $13B |
| Busiest month | Jan 2026 (87 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 52 | 51 | $2.8B | $41M | ████████████ |
| Jun 2025 | 66 | 60 | $4.8B | $63M | ███████████████ |
| Jul 2025 | 48 | 44 | $3.2B | $64M | ███████████ |
| Aug 2025 | 68 | 64 | $5.8B | $55M | ████████████████ |
| Sep 2025 | 81 | 77 | $26.7B | $84.2M | ███████████████████ |
| Oct 2025 | 85 | 80 | $10.4B | $77.5M | ████████████████████ |
| Nov 2025 | 56 | 54 | $8B | $115M | █████████████ |
| Dec 2025 | 53 | 50 | $5.1B | $35M | ████████████ |
| Jan 2026 | 87 | 84 | $18.6B | $75M | ████████████████████ |
| Feb 2026 | 66 | 63 | $9.2B | $96M | ███████████████ |
| Mar 2026 | 81 | 74 | $9.9B | $80M | ███████████████████ |
| Apr 2026 | 74 | 66 | $7.4B | $80M | █████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 21 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 2 Sep 2025 | Anthropic (anthropic.com) | Series C (or unspecified) | $13B | iconiq capital, lightspeed, fidelity | USA | Iconiq Capital, Lightspeed, and Fidelity led the round, with Qatar Investment Authority participating after CEO reversed stance on Middle… |
| 13 Jan 2026 | QXO | Series C convertible perpetual preferred stock | $3B | apollo global management, temasek, other investors | USA | QXO has expanded its previously announced financing to $3 billion, increasing its capacity to pursue acquisitions as it targets… |
| 14 Mar 2026 | Nscale (nscale.com) | Series C | $2B | — | United Kingdom | Nscale , a London-based provider of AI infrastructure and cloud platforms, has raised $2 billion in Series C funding, valuing the company… |
| 6 Jan 2026 | Dayone (dayoneny.org) | Series C | $2B | Coatue Management, Indonesia Investment Authority | Singapore | DayOne, the overseas arm of Shanghai-based GDS Holdings, has won the backing of Indonesia’s sovereign wealth fund as part of a Series C… |
| 16 Sep 2025 | Mistral AI (mistral.ai) | Series C | $2B ⚠ check sentence | ASML Holding NV, dst global, Andreessen Horowitz | — | French startup Mistral AI has secured USD 2bn (EUR 1.7bn) in a Series C round, bringing its valuation to USD 13.8bn, the company announced… |
| 22 Apr 2026 | Factory (factory.com) | Series C | $1.5B ⚠ check sentence | khosla ventures, sequoia capital, blackstone | — | Factory announced it has raised $150 million in a Series C funding round led by Khosla Ventures, with participation from Sequoia Capital,… |
| 17 Feb 2026 | SkildAI | Series C | $1.4B | — | — | SkildAI, which builds AI models to power robots, raised a $1.4 billion Series C round that valued the startup at $14 billion. |
| 14 Jan 2026 | Skild AI | Series C | $1.4B | softbank group, nventures, bezos expeditions | US | Skild AI, a Pittsburgh-based robotics AI startup, secured a mammoth $1.4 billion funding round to accelerate development of its… |
| 6 Jan 2026 | QXO Inc | Series C | $1.2B | apollo global management, Other investors | — | On January 5, 2026, QXO Inc. announced that funds managed by Apollo Global Management and other investors agreed to invest up to $1.2… |
| 18 Feb 2026 | World Labs (worldlabs.vdtrxn) | Series C | $1B | autodesk, nvidia, amd | United States | World Labs raises $1B in Series C funding for spatial AI platform |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Lucid Group (wearelucidgroup.com) | Series C | $550M | ayar | USA | On April 28, 2026, Ayar Third Investment Company (“Ayar”), an affiliate of the Public Investment Fund (“PIF”) purchased from Lucid Group,… |
| 29 Apr 2026 | Counterpart (counterpart.biz) | Series C | $50M | valor equity partners, vy capital | United States | today announced the close of its $50M Series C financing round led by Valor Equity Partners, with continued participation from existing… |
| 28 Apr 2026 | Liquid Instruments (liquidinstruments.com) | Series C | $70M | National Reconstruction Fund | Australia | Liquid Instruments announced its plan on Wednesday after winning a $28.45 million stake from the National Reconstruction Fund. |
| 28 Apr 2026 | Liquid Instruments (liquidinstruments.com) | Series C | $50M | keysight technologies, NRFC | United States | Liquid Instruments , a pioneer in software-defined test solutions, today announced the close of its $50 million Series C funding round,… |
| 27 Apr 2026 | Volant (volant.aero) | Series C | $300M | stone, Sequoia China, Fortera Capital | China | Gasgoo Munich- VOLANT has recently closed a Series C funding round exceeding $300 million. |
| 27 Apr 2026 | Kashable (kashable.com) | Series C | $60M | Goldman Sachs Alternatives, revolution, EJF Ventures | — | Kashable, a fintech specializing in employee financial wellness, has secured a $60 million Series C funding round. The investment was led… |
| 24 Apr 2026 | Hqlaᵡ (hqla-x.com) | Series C–1 | — | Broadridge Financial Solutions, digital asset | — | HQLAᵡ announced it has secured strategic minority investments from Broadridge Financial Solutions and Digital Asset in its Series C–1… |
| 24 Apr 2026 | Omni Analytics, Inc. | Series C | $120M ⚠ check sentence | iconiq, Theory Ventures, first round capital | United States | Omni, a San Francisco, CA–based AI analytics platform, has raised $120 million in Series C funding at a $1.5 billion valuation. |
| 23 Apr 2026 | Cloudsmith (cloudsmith.io) | Series C | $72M | tcv, insight partners, other existing investors | United Kingdom | Cloudsmith Raises $72M Series C for AI-Era Software Supply Chain Security |
| 23 Apr 2026 | Omni (exploreomni.com) | Series C | $120M | iconiq, Theory Ventures, first round capital | — | Omni raises $120M Series C for enterprise AI analytics |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --round-type "series c" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --round-type "series c" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --round-type "series c" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"round_type": "series c", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"round_type": "series c", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Series B Funding](series-b-funding.md)
- [AI Startup Funding News](ai-startup-funding-news.md)
- [Biotech Funding News](biotech-funding-news.md)
- [Crypto Funding](crypto-funding.md)
