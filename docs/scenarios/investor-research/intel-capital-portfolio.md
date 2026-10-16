# Intel Capital Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “intel capital portfolio” · 10/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [intel-capital-portfolio.json](../../examples/scenarios/intel-capital-portfolio.json).

**Question.** Which rounds did Intel Capital appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Intel Capital”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 52 |
| With a usable reported amount | 49 |
| Reported total (usable amounts) | $7B |
| Median reported round | $61.4M |
| Largest reported round | $1.5B |
| Busiest month | Aug 2025 (12 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 2 | 2 | $400M | $200M | ███ |
| Jun 2025 | 2 | 2 | $15M | $15M | ███ |
| Jul 2025 | 5 | 5 | $102.7M | $51.4M | ████████ |
| Aug 2025 | 12 | 10 | $1.1B | $314M | ████████████████████ |
| Sep 2025 | 7 | 7 | $2.2B | $71M | ████████████ |
| Oct 2025 | 1 | 1 | $15.5M | $15.5M | ██ |
| Nov 2025 | 7 | 6 | $275M | $50M | ████████████ |
| Dec 2025 | 0 | 0 | — | — |  |
| Jan 2026 | 3 | 3 | $320M | $70M | █████ |
| Feb 2026 | 4 | 4 | $774M | $200M | ███████ |
| Mar 2026 | 4 | 4 | $1.9B | $195M | ███████ |
| Apr 2026 | 5 | 5 | $452.1M | $70M | ████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 23 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 24 Mar 2026 | SambaNova | Series E | $1.5B | battery ventures, cambium capital partners, first data | USA |  |
| 23 Sep 2025 | Figure AI | Series C | $1B ⚠ check sentence | brookfield asset management, nvidia, macquarie capital | United States | Figure AI, the robotics startup known for its work in humanoid robots, has closed a Series C funding round exceeding US$1 billion,… |
| 27 Aug 2025 | FieldAI | Series C | $405M | nventures, bezos expeditions, khosla ventures | — | FieldAI, a robotics software startup backed by Nvidia, Bezos Expeditions, and Bill Gates’s foundation, announced a massive $405 million… |
| 21 Aug 2025 | Field AI (fieldai.com) | — | $405M | nventures, bezos expeditions, khosla ventures | USA | Field AI, a robotics startup backed by Bill Gates, has raised $405 million across two funding rounds, attracting investments from Nvidia’s… |
| 9 May 2025 | Ai21 Labs (ai21.com) | Series D | $300M | google, nvidia, intel capital | Israel | AI21 Labs, an Israeli startup building its own large language models, is raising a $300 million Series D funding round, a person with… |
| 22 Jan 2026 | Upscale AI (upscale.ai) | Series A | $200M ⚠ check sentence | tiger global management, premji invest, xora innovation | United States | Upscale AI’s $200 million Series A funding round represents a pivotal milestone for the young company, elevating it to unicorn status with… |
| 11 Apr 2026 | Sifive (sifive.com) | — | $175M ⚠ check sentence | Coatue Management, intel capital, qualcomm ventures | — | SiFive hasn’t raised since March 2022, Pitchbook estimates, when it brought in $175 million led by Coatue Management at a pre-money… |
| 6 Apr 2026 | Censys (censys.com) | total equity | $143.1M | decibel partners, google ventures, greylock | United States | Censys has now raised a total of $143.1M in total equity funding and is backed by Decibel Partners, Google Ventures, Greylock, Intel… |
| 27 May 2025 | Exo (exoprotein.com) | Late-stage (Series undisclosed) | $100M | sands capital, bold capital, Qubit Health | USA | Exo, a Silicon Valley-based medical imaging startup, is finalizing a funding round of up to $100 million to expand its AI-enhanced… |
| 8 Jan 2026 | Articul8 AI | Series B | $70M ⚠ check sentence | adara ventures, NXC Corporation, Aditya Birla Ventures | United States | Articul8 AI has announced the first closing of its Series B round, targeting approximately $70 million in total funding. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 11 Apr 2026 | Sifive (sifive.com) | — | $175M ⚠ check sentence | Coatue Management, intel capital, qualcomm ventures | — | SiFive hasn’t raised since March 2022, Pitchbook estimates, when it brought in $175 million led by Coatue Management at a pre-money… |
| 7 Apr 2026 | Censys (censys.com) | Series D | $70M | morgan stanley expansion capital, decibel partners,… | — | Censys, the internet intelligence and insights platform, has raised $70m in a combined funding round to accelerate the development of its… |
| 6 Apr 2026 | Q-factor (qfactor.dk) | Seed | $24M | nfx, tpy capital, intel capital | Israel | The round was led by NFX and TPY Capital, with participation from Intel Capital... |
| 6 Apr 2026 | Censys (censys.com) | total equity | $143.1M | decibel partners, google ventures, greylock | United States | Censys has now raised a total of $143.1M in total equity funding and is backed by Decibel Partners, Google Ventures, Greylock, Intel… |
| 1 Apr 2026 | Censys (censys.com) | Series D equity | $40M | morgan stanley expansion capital, decibel partners,… | — | The financing includes a $40 million Series D equity round alongside $30 million in debt financing. |
| 25 Mar 2026 | EPIC Microsystems | Series A | $21M | Seligman Ventures, intel capital, AICONIC Ventures | USA | EPIC Microsystems, a semiconductor company developing breakthrough power delivery solutions for AI infrastructure, announced a $21 million… |
| 24 Mar 2026 | SambaNova | Series E | $1.5B | battery ventures, cambium capital partners, first data | USA |  |
| 5 Mar 2026 | Sambanova Systems (sambanova.ai) | new funding round | $350M | vista equity partners, Cambium Capital, intel capital | USA | California-based SambaNova Systems, established in 2017, recently raised USD 350 million in a new funding round and struck a partnership… |
| 25 Feb 2026 | SambaNova | Series E | $350M | vista equity partners, Cambium Capital, intel capital | — | Intel-backed Nvidia rival SambaNova has raised $350m in a Series E round led by Vista Equity Partners and Cambium Capital, with strong… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "Intel Capital" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "Intel Capital" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "Intel Capital" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Intel Capital", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Intel Capital", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [First Round Capital Portfolio](first-round-capital-portfolio.md)
- [GV Investments](gv-investments.md)
- [Prosus Investments](prosus-investments.md)
- [Breakthrough Energy Ventures Portfolio](breakthrough-energy-ventures-portfolio.md)
