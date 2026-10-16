# Insight Partners Portfolio: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “insight partners portfolio” · 30/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [insight-partners-portfolio.json](../../examples/scenarios/insight-partners-portfolio.json).

**Question.** Which rounds did Insight Partners appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Insight Partners”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 225 |
| With a usable reported amount | 202 |
| Reported total (usable amounts) | $33.4B |
| Median reported round | $38.5M |
| Largest reported round | $13B |
| Amounts left out as implausible or unconverted | 5 |
| Busiest month | Jul 2025 (29 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 14 | 13 | $393.5M | $24M | ██████████ |
| Jun 2025 | 14 | 13 | $339M | $50M | ██████████ |
| Jul 2025 | 29 | 29 | $716.7M | $25M | ████████████████████ |
| Aug 2025 | 17 | 15 | $1.2B | $34.2M | ████████████ |
| Sep 2025 | 23 | 21 | $15.1B | $50M | ████████████████ |
| Oct 2025 | 24 | 19 | $1.4B | $47.8M | █████████████████ |
| Nov 2025 | 19 | 17 | $900.5M | $72M | █████████████ |
| Dec 2025 | 16 | 14 | $4.3B | $30.5M | ███████████ |
| Jan 2026 | 18 | 16 | $5.4B | $69M | ████████████ |
| Feb 2026 | 23 | 22 | $5.9B | $25.5M | ████████████████ |
| Mar 2026 | 13 | 11 | $1.2B | $29.5M | █████████ |
| Apr 2026 | 15 | 12 | $2.1B | $72M | ██████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 26 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 2 Sep 2025 | Anthropic (anthropic.com) | Series ? | $13B ⚠ check sentence | iconiq capital, Fidelity Management and Research Co.,… | — | Anthropic has closed a deal to raise $13 billion from investors in a new funding round that nearly triples its valuation to $183 billion,… |
| 10 Feb 2026 | Databricks (databricks.com) | Series K | $5B ⚠ check sentence | qatar investment authority, Singapore Temasek, Macquarie… | United States | United States data & artificial intelligence (AI) company Databrick has raised $5 billion funding at $134 billion valuation, and with… |
| 22 Apr 2026 | Factory (factory.com) | Series C | $1.5B ⚠ check sentence | khosla ventures, sequoia capital, blackstone | — | Factory announced it has raised $150 million in a Series C funding round led by Khosla Ventures, with participation from Sequoia Capital,… |
| 24 Mar 2026 | Ayar Labs (ayarlabs.com) | Series E | $871.5M | 1789 Capital, alchip, AMD Ventures | USA |  |
| 7 Feb 2026 | Kiteworks (kiteworks.com) | growth-equity | $450M | insight partners, Sixth Street Growth | — | Kiteworks announced a $450 million growth-equity investment from global software investors Insight Partners and Sixth Street Growth. |
| 6 Oct 2025 | Builder AI | — | $424.2M ⚠ check sentence | microsoft, Qatar’s sovereign wealth fund, insight partners | — | Builder AI raised £334 million from investors including Microsoft, Qatar’s sovereign wealth fund and Insight Partners. The company… |
| 12 Nov 2025 | Armis Security (armis.com) | Pre‑IPO financing | $400M | one equity partners, insight partners, Brookfield… | USA |  |
| 2 Oct 2025 | Filevine (filevine.com) | Series E & F | $400M | insight partners, accel, Halo Fund | United States | Filevine, a Salt Lake City-based legal tech startup, has raised $400 million in funding across two rounds |
| 23 Jan 2026 | Torq (torqlogistics.com) | — | $332M | Merlin Ventures, insight partners, bessemer venture partners | Israel | The round raised $332 million and included participation from Insight Partners, Bessemer Venture Partners, Greenfield Partners, Evolution… |
| 6 Apr 2026 | Scaleops (scaleops.com) | total equity | $209.5M | glilot capital partners, insight partners, lightspeed… | United States | ScaleOps has now raised a total of $209.5M in total equity funding and is backed by Glilot Capital Partners, Insight Partners, Lightspeed… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 23 Apr 2026 | Cloudsmith (cloudsmith.io) | Series C | $72M | tcv, insight partners, other existing investors | United Kingdom | Cloudsmith Raises $72M Series C for AI-Era Software Supply Chain Security |
| 22 Apr 2026 | Factory (factory.com) | Series C | $1.5B ⚠ check sentence | khosla ventures, sequoia capital, blackstone | — | Factory announced it has raised $150 million in a Series C funding round led by Khosla Ventures, with participation from Sequoia Capital,… |
| 20 Apr 2026 | Screenpoint Medical (screenpoint-medical.com) | Growth funding | $14M | insight partners, siemens healthineers | — | ScreenPoint Medical raised $14M growth funding for breast imaging AI. |
| 20 Apr 2026 | Factory (factory.com) | Series C | $150M | khosla ventures, sequoia capital, blackstone | — | Factory, an autonomous software engineering platform used by enterprises including Nvidia, Adobe and Adyen, raised $150 million in a… |
| 17 Apr 2026 | Screenpoint Medical (screenpoint-medical.com) | — | $16M | insight partners, siemens healthineers, non-dilutive… | Netherlands | ScreenPoint Medical has secured $16 million in fresh capital, combining $14 million from existing investors Insight Partners and Siemens… |
| 15 Apr 2026 | Seifert Dynamics | Series A | $13.4M | palantir technologies, insight partners, shield capital | United States | Seifert Dynamics, a rising leader in the operational intelligence (OI) sector, announced today the successful closing of a $13.4 million… |
| 6 Apr 2026 | Openai (openai.com) | — | — ⚠ implausible size | amazon, nvidia, softbank | — | OpenAI has raised USD $122 billion in committed capital, valuing the company at USD $852 billion after the investment. The round was… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor "Insight Partners" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor "Insight Partners" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor "Insight Partners" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Insight Partners", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Insight Partners", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Founders Fund Portfolio](founders-fund-portfolio.md)
- [NEA Investments](nea-investments.md)
- [Lightspeed Investments](lightspeed-investments.md)
- [Khosla Ventures Portfolio](khosla-ventures-portfolio.md)
