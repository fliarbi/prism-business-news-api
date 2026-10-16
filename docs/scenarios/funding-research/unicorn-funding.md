# Unicorn Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “unicorn funding” · 110/month India · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [unicorn-funding.json](../../examples/scenarios/unicorn-funding.json).

**Question.** How many unicorn deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** deal sentences mentioning “unicorn”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 140 |
| With a usable reported amount | 134 |
| Reported total (usable amounts) | $15.3B |
| Median reported round | $75M |
| Largest reported round | $2.4B |
| Busiest month | Sep 2025 (20 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 3 | 3 | $275M | $100M | ███ |
| Jun 2025 | 8 | 8 | $577.3M | $87M | ████████ |
| Jul 2025 | 15 | 13 | $1.4B | $50M | ███████████████ |
| Aug 2025 | 7 | 7 | $480.3M | $65.5M | ███████ |
| Sep 2025 | 20 | 19 | $4.6B | $116.5M | ████████████████████ |
| Oct 2025 | 12 | 10 | $1B | $75.6M | ████████████ |
| Nov 2025 | 3 | 3 | $118.5M | $50M | ███ |
| Dec 2025 | 15 | 14 | $1.3B | $32.5M | ███████████████ |
| Jan 2026 | 14 | 14 | $1.3B | $100M | ██████████████ |
| Feb 2026 | 16 | 16 | $1.1B | $39.5M | ████████████████ |
| Mar 2026 | 15 | 15 | $1.3B | $80M | ███████████████ |
| Apr 2026 | 12 | 12 | $1.9B | $12.2M | ████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 7 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 15 Sep 2025 | Tamara (tamara.co) | Shariah-compliant debt facility | $2.4B | goldman sachs, citi, Apollo-managed funds | Saudi Arabia | Tamara, a Saudi “buy-now-pay-later” fintech unicorn, secured a massive $2.4 billion Shariah-compliant credit facility to fuel its expansion. |
| 6 Apr 2026 | Helsing (helsing.ai) | — | $1.5B ⚠ check sentence | general catalyst, accel, saab | Germany | Helsing has raised over €1.4 billion, achieving unicorn-plus status with a valuation around €3-4 billion in recent rounds backed by… |
| 15 Dec 2025 | Brevo (brevo.com) | Liquidity event | $540M | general atlantic, oakley, partech | France | Brevo just joined France’s unicorn club with a splashy €500 million announcement, resetting the cap table. |
| 9 Jul 2025 | Zepto (zepto.com.au) | — | $500M ⚠ check sentence | — | — | According to a Moneycontrol report, quick-commerce unicorn Zepto is planning to raise $500 million at a $7 billion valuation. |
| 25 Sep 2025 | Physicswallah (physicswallah.live) | equity issue | $372M | — | India | Edtech unicorn PhysicsWallah (PW) is expanding its offline presence as it prepares to enter the capital markets with a fresh equity issue… |
| 15 Sep 2025 | Firmus Technologies | — | $330M | nvidia, ellerston capital, Phil King’s Regal Funds… | Australia | Firmus Technologies has become the latest Australian-founded startup to reach unicorn status, after the artificial intelligence… |
| 3 Sep 2025 | Iqm (meetiqm.com) | — | $320M | Ten Eleven Ventures, tesi | Finland | The quantum computing company IQM announced that it raised $320 million in a new round of funding, achieving . .unicorn . status with an… |
| 9 Sep 2025 | Porter (helloporter.com) | Series F | $310M | vitruvian partners, elev8 venture partners, kedaara capital | — | Logistics unicorn Porter has raised another $110 million from Vitruvian Partners, Elev8 Venture Partners and others in an extended Series… |
| 3 Feb 2026 | Skyryse (skyryse.com) | Series C | $300M ⚠ check sentence | Autopilot Ventures, Fidelity Management & Research… | USA | Skyryse, an El Segundo, California-based aviation automation startup, has raised more than $300 million in a Series C investment, pushing… |
| 18 Oct 2025 | Vantaca (vantaca.com) | Minority Growth Investment (Late-Stage) | $300M | cove hill partners, JMI Equity | United States | Vantaca, a leading AI-powered platform for community association management, secured over $300 million in a minority growth investment… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 28 Apr 2026 | Snabbit | Series D | $56M | bertelsmann india investments, Susquehanna Venture… | India | Snabbit, India's fastest-growing quick home services platform, today announced a $56 million Series D round co-led by Bertelsmann India… |
| 23 Apr 2026 | Deep Algorithm | Pre-Series A | $19.2M | unicorn india ventures, sb investment | India | Deep Algorithm Raises ₹16 Cr in Pre-Series A Round AI-driven cybersecurity and digital trust company, Deep Algorithms, has raised ₹16… |
| 23 Apr 2026 | M | Seed | $12.2M | peak xv partners, blume ventures, cred | India | Kabeer Biswas' M Raises ₹102 Cr from Peak XV, Blume, and CRED Former Dunzo cofounder Kabeer Biswas' new startup, M, is looking to net ₹102… |
| 9 Apr 2026 | Nava (navacenter.com) | Seed | $9.6M | rtp global, unicorn india ventures, Blume Founders Fund | Singapore | Nava previously raised a $9.6 million seed round led by RTP Global, with participation from Unicorn India Ventures, Blume Founders Fund,… |
| 8 Apr 2026 | Kreditbee (kreditbee.in) | Series E | $280M ⚠ check sentence | — | India | KreditBee has raised $280 million in a Series E round, achieving a valuation of $1.5 billion and entering the unicorn club. |
| 6 Apr 2026 | Helsing (helsing.ai) | — | $1.5B ⚠ check sentence | general catalyst, accel, saab | Germany | Helsing has raised over €1.4 billion, achieving unicorn-plus status with a valuation around €3-4 billion in recent rounds backed by… |
| 6 Apr 2026 | SatLeo Labs (satleolabs.com) | — | $5.5M | unicorn india ventures, merak ventures, Java Capital | India | SatLeo Labs, a growing space-tech startup, has raised a total of $5.5 million in funding. The latest $2.2 million came from Unicorn India… |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --q unicorn --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --q unicorn --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --q unicorn --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"q": "unicorn", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"q": "unicorn", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Fintech Funding](fintech-funding.md)
- [SAAS Funding News](saas-funding-news.md)
- [Venture Debt Funding](venture-debt-funding.md)
- [Robotics Funding](robotics-funding.md)
