# Atomico Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “atomico investments” · 20/month India · 70/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [atomico-investments.json](../../examples/scenarios/atomico-investments.json).

**Question.** Which rounds did Atomico appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “Atomico”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 58 |
| With a usable reported amount | 55 |
| Reported total (usable amounts) | $2.3B |
| Median reported round | $38.1M |
| Largest reported round | $300M |
| Busiest month | Oct 2025 (12 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 0 | 0 | — | — |  |
| Jun 2025 | 7 | 5 | $378.4M | $93.3M | ████████████ |
| Jul 2025 | 0 | 0 | — | — |  |
| Aug 2025 | 3 | 3 | $192.4M | $96.2M | █████ |
| Sep 2025 | 4 | 4 | $70M | $27M | ███████ |
| Oct 2025 | 12 | 12 | $350.4M | $15.1M | ████████████████████ |
| Nov 2025 | 4 | 4 | $252.8M | $64.8M | ███████ |
| Dec 2025 | 6 | 6 | $115M | $21.6M | ██████████ |
| Jan 2026 | 5 | 5 | $442M | $61M | ████████ |
| Feb 2026 | 9 | 9 | $396.3M | $40M | ███████████████ |
| Mar 2026 | 6 | 5 | $210M | $40M | ██████████ |
| Apr 2026 | 2 | 2 | $157M | $78.5M | ███ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 23 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 22 Jan 2026 | Mews (mews.com) | Series D | $300M ⚠ check sentence | eqt growth, atomico, harbourvest partners | Czech Republic | Czech-founded Mews, a hospitality technology company, has secured a $300 million (€255.17 million) in fresh investment, pushing its… |
| 2 Feb 2026 | Pomelo Care (pomelocare.com) | Series C | $179M | Andreessen Horowitz, atomico, boxgroup | — |  |
| 3 Nov 2025 | Dexory (dexory.com) | Series C | $165M | LTS Growth, endeavor catalyst, dtcp | UK | In October 2025, Dexory secured a $165 million Series C round led by Eurazeo’s Growth team, with participation from LTS Growth, Endeavor… |
| 23 Jun 2025 | Physicsx (physicsx.ai) | Series B | $135M | atomico, temasek, siemens | United Kingdom | London-based PhysicsX, a deeptech startup building AI to power engineering, has secured $135M (nearly €117.43M) in Series B funding led by… |
| 30 Mar 2026 | Zocdoc (zocdoc.com) | — | $130M ⚠ check sentence | baillie gifford, atomico | USA | was valued at roughly $1.8 billion in 2015 after a $130 million round led by Baillie Gifford and Atomico |
| 6 Apr 2026 | OpenFX | total equity | $117M | accel, atomico, faction | United States | OpenFX has now raised a total of $117M in total equity funding and is backed by Accel, Atomico, Faction, Flybridge, and Hash3. |
| 29 Aug 2025 | Framer (framer.com) | Series D | $100M | meritech capital partners, atomico | Netherlands | Framer, the Amsterdam- and San Francisco-based website design platform, has raised $100 million in Series D funding, valuing the company… |
| 10 Feb 2026 | Tem (tem.energy) | — | $75M | lightspeed venture partners, Hitachi Ventures, atomico | UK | London-based energy technology company Tem has raised $75 million in fresh funding as it looks to expand internationally and accelerate… |
| 11 Nov 2025 | Vay Technology GmbH | Strategic Investment | $64.8M | Grab Holdings Limited, atomico, project a | Germany | The investment will involve an initial cash investment of 60 million euros. |
| 12 Jun 2025 | Abacum (abacum.io) | Series B | $60M | scale venture partners, cathay innovation, y combinator | United States | Abacum, a New York-based business planning software company, has raised $60 million in Series B funding. |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 6 Apr 2026 | OpenFX | total equity | $117M | accel, atomico, faction | United States | OpenFX has now raised a total of $117M in total equity funding and is backed by Accel, Atomico, Faction, Flybridge, and Hash3. |
| 1 Apr 2026 | Lace (laceeng.com.br) | venture | $40M | atomico, M12 (Microsoft’s Venture Fund), sett | — | Lace raised $40 million in venture funding backed by Atomico, M12 (Microsoft’s Venture Fund), and SETT. |
| 30 Mar 2026 | Zocdoc (zocdoc.com) | — | $130M ⚠ check sentence | baillie gifford, atomico | USA | was valued at roughly $1.8 billion in 2015 after a $130 million round led by Baillie Gifford and Atomico |
| 26 Mar 2026 | Dexory (dexory.com) | Series C | — | british business bank, eurazeo, LTS Growth | United Kingdom | The British Business Bank has invested £8.5 million in Dexory as part of the company's Series C funding round. |
| 24 Mar 2026 | Lace Lithography (lacelithography.com) | Series A | $40M | atomico, m12, linse capital | Norway | Lace Lithography has raised $40 million in a Series A round co-led Atomico and M12, with participation from Linse Capital, SETT, Nysnø,… |
| 13 Feb 2026 | Electric Twin (electrictwin.com) | Series A / Seed | $10M | atomico, localglobe, mercuri | United Kingdom | The raise includes a USD $10 million round led by Atomico, with participation from LocalGlobe, Mercuri and Samos Investments. |
| 12 Feb 2026 | Electric Twin (electrictwin.com) | — | $13M | atomico, localglobe, mercuri | UK | London’s Electric Twin, an AI platform building synthetic audiences that model how people think and behave in real life, is announcing… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor Atomico --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor Atomico --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor Atomico --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "Atomico", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "Atomico", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
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

- [Plug and Play Investments](plug-and-play-investments.md)
- [GIC Portfolio](gic-portfolio.md)
- [Dst Global Portfolio](dst-global-portfolio.md)
- [Lux Capital Portfolio](lux-capital-portfolio.md)
