# Growth Stage Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “growth stage funding” · 10/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [growth-stage-funding.json](../../examples/scenarios/growth-stage-funding.json).

**Question.** How many growth stage deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** round type “growth”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 624 |
| With a usable reported amount | 441 |
| Reported total (usable amounts) | $26.3B |
| Median reported round | $30M |
| Largest reported round | $1.8B |
| Busiest month | Oct 2025 (87 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 50 | 34 | $1.8B | $23.5M | ███████████ |
| Jun 2025 | 51 | 42 | $2.5B | $30M | ████████████ |
| Jul 2025 | 49 | 30 | $3.1B | $51.4M | ███████████ |
| Aug 2025 | 48 | 37 | $1.7B | $36.7M | ███████████ |
| Sep 2025 | 54 | 38 | $2.3B | $56.5M | ████████████ |
| Oct 2025 | 87 | 64 | $3B | $47.3M | ████████████████████ |
| Nov 2025 | 42 | 27 | $2.2B | $42.1M | ██████████ |
| Dec 2025 | 52 | 40 | $2.1B | $24.2M | ████████████ |
| Jan 2026 | 53 | 35 | $1.5B | $17.5M | ████████████ |
| Feb 2026 | 54 | 40 | $4.5B | $32.4M | ████████████ |
| Mar 2026 | 41 | 26 | $2.1B | $30.2M | █████████ |
| Apr 2026 | 43 | 28 | $2.6B | $24.8M | ██████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 14 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 17 Apr 2026 | K1x (k1x.io) | growth | $1.8B | sumeru equity partners, edison partners | — | K1x, an AI-native tax data platform for private markets, announced it has secured a $175 million growth investment to accelerate the… |
| 16 Feb 2026 | Neysa (neysa.ai) | Growth / Mega Round | $1.2B | blackstone, Teachers’ Venture Growth, tvs capital funds | India | Neysa has secured over $1.2 billion in funding, led by private equity firm Blackstone with participation from Teachers’ Venture Growth,… |
| 4 Mar 2026 | Neura Robotics (neura-robotics.com) | Growth round | $1.1B | Tether Holdings | Germany | Neura Robotics Raising €1B in Funding Round to Build Humanoid Robots |
| 6 Jun 2025 | Grammarly (grammarly.com) | Growth Financing | $1B | general catalyst | USA | Grammarly Raises $1B Growth Round to Expand AI Writing Platform. |
| 24 Jul 2025 | 5c Group (5cgroupcapital.com) | Growth funding (Equity & debt) | $835M | Brookfield, deutsche bank | Canada |  |
| 22 Feb 2026 | Saviynt (saviynt.com) | growth equity | $700M | kkr, Sixth Street Growth, TenEleven | United States | El Segundo-based cybersecurity firm Saviynt had one of the longest stretches between venture rounds, as it raised $700 million of growth… |
| 24 Jul 2025 | Stratos Wealth Holdings and Its Stratos Business | strategic growth investment | $527M | sei | — | Alston & Bird represented Stratos Wealth Holdings and its Stratos business, a family of companies focused on supporting the success of… |
| 13 Nov 2025 | Chaos Industries (getchaos.com) | Growth / Late Stage | $510M | valor equity partners, strategic financial partners | — | Defense‑tech startup CHAOS Industries has raised $510 million in new funding as governments race to modernize national security… |
| 27 Feb 2026 | Vero Networks (veronetworks.com) | Growth | $500M | braemont capital | — | Broadband provider Vero Networks matched MatX with a $500 million growth round backed by Braemont Capital and others. |
| 7 Feb 2026 | Kiteworks (kiteworks.com) | growth-equity | $450M | insight partners, Sixth Street Growth | — | Kiteworks announced a $450 million growth-equity investment from global software investors Insight Partners and Sixth Street Growth. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 30 Apr 2026 | Qover (qover.com) | growth financing | — | cibc innovation banking | Belgium | CIBC Innovation Banking today announced that it has provided growth financing to Qover, a European-based embedded insurance platform. |
| 30 Apr 2026 | Smart Information Technologies | growth loan | $381k | river capital | United Kingdom | Smart Information Technologies, a Kirkham-based business specialising in ERP (enterprise resource planning) software implementation and… |
| 29 Apr 2026 | Sportvot (sportvot.com) | Growth | $39.2M | IAN Alpha Fund, anicut capital, letsventure | India | SportVot Raises ₹32.7 Cr Growth Round Sports streaming and analytics platform, SportVot, raised INR 32.7 crore led by IAN Alpha Fund. |
| 29 Apr 2026 | Sportvot (sportvot.com) | Growth | $3.9M | IAN Alpha Fund, anicut capital, letsventure | India | SportVot Raises ₹32.7 Cr Growth Round |
| 28 Apr 2026 | Altair Semiconductor (altair-semi.com) | Strategic Growth Round (post-spinoff) | $50M | Pitango Venture Capital, sony | Israel | Altair Semiconductor has secured $50 million in funding from Pitango Group. |
| 28 Apr 2026 | CleanDesign (cleandesignic.com) | Growth Investment | $20M | edison partners | — | CleanDesign, a Toronto and Nashville-based software-driven energy technology company, has secured a $20 million growth investment led by… |
| 24 Apr 2026 | Openly (openly.com) | growth | — | Eden Global Partners, advance venture partners, gradient | United States | Openly, a tech-enabled homeowners insurance provider, has secured a growth investment round led by existing investors Eden Global… |
| 23 Apr 2026 | Fasal Bio | growth equity | $7.6M | blackpeak capital | Croatia | Fasal Bio a Zagreb-based company developing a proprietary renewable materials platform aimed at reducing reliance on conventional… |
| 22 Apr 2026 | Render Networks (rendernetworks.com) | private equity growth | $13.2M | existing shareholders | — | Render Networks announced A$20 million in private equity growth funding alongside the acquisition of mPower Innovations |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --round-type growth --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --round-type growth --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --round-type growth --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"round_type": "growth", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"round_type": "growth", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Bridge Round Funding](bridge-round-funding.md)
- [Climate Tech Funding](climate-tech-funding.md)
- [D2C Funding](d2c-funding.md)
- [Insurtech Funding](insurtech-funding.md)
