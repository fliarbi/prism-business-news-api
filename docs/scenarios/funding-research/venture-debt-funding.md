# Venture Debt Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “venture debt funding” · 90/month India · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [venture-debt-funding.json](../../examples/scenarios/venture-debt-funding.json).

**Question.** How many venture debt deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** round type “venture debt”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 53 |
| With a usable reported amount | 49 |
| Reported total (usable amounts) | $792.6M |
| Median reported round | $17.6M |
| Largest reported round | $100M |
| Busiest month | Sep 2025 (6 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 4 | 4 | $67.9M | $13.6M | █████████████ |
| Jun 2025 | 5 | 5 | $67.7M | $18.9M | █████████████████ |
| Jul 2025 | 4 | 4 | $87.5M | $21.6M | █████████████ |
| Aug 2025 | 5 | 5 | $121.3M | $14.2M | █████████████████ |
| Sep 2025 | 6 | 5 | $67.8M | $18.9M | ████████████████████ |
| Oct 2025 | 2 | 2 | $59.4M | $29.7M | ███████ |
| Nov 2025 | 5 | 5 | $40.3M | $12M | █████████████████ |
| Dec 2025 | 6 | 5 | $62.7M | $14.2M | ████████████████████ |
| Jan 2026 | 3 | 3 | $6M | $2M | ██████████ |
| Feb 2026 | 6 | 6 | $59.3M | $16M | ████████████████████ |
| Mar 2026 | 2 | 2 | $112.5M | $56.2M | ███████ |
| Apr 2026 | 5 | 3 | $40.2M | $11.1M | █████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 8 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 24 Mar 2026 | Sokin (sokin.com) | venture debt | $100M | oxford finance llc | — | Mishcon de Reya has advised global payments group Sokin on all UK aspects of a $100 million syndicated secured venture debt facility led… |
| 6 Aug 2025 | Roadsurfer (roadsurfer.com) | ABS and Venture Debt | $91.8M | macquarie group, bbva | Germany | The Munich-based company Roadsurfer has received financing totaling €85 million. The funds come from two separate sources: an asset-backed… |
| 24 Oct 2025 | Meva Energy (mevaenergy.com) | Venture Debt Financing | $43.2M | european investment bank | Sweden | Meva Energy, a Gothenburg, Sweden-based cleantech startup, has secured €40 million (approximately $42 million) in venture debt financing… |
| 1 May 2025 | Sidekick Health (sidekickhealth.com) | venture debt | $37.8M | european investment bank | Luxembourg | The European Investment Bank (EIB) has entered into a €35 million venture debt agreement with Sidekick Health |
| 8 Dec 2025 | Samba Tv (samba.tv) | venture debt | $30M | Horizon Technology Finance Corporation | USA | Samba TV has announced that it has secured new financing from Horizon Technology Finance Corporation, an affiliate of Monroe Capital, with… |
| 25 Feb 2026 | Oq Technology (oqtec.space) | venture debt | $27M | european investment bank | Luxembourg | The European Investment Bank (EIB) extended €25M ($29.5M) in venture debt financing to Luxembourg-based D2D satellite operator OQ… |
| 30 Jun 2025 | Gatewatcher (gatewatcher.com) | venture debt | $27M | european investment bank | France | Gatewatcher, a French cybersecurity company, has received a €25m venture debt facility from the European Investment Bank (EIB). |
| 18 Sep 2025 | Trifecta Capital’s Fund IV | Venture debt fund investment | $25M | international finance corporation | — | The International Finance Corporation is set to invest $25 million in Trifecta Capital’s fourth venture debt fund. The fund offers debt… |
| 2 Jul 2025 | Danads (danads.com) | venture debt | $22.7M | european investment bank | Sweden | (PRESS RELEASE) LUXEMBOURG, 2-Jul-2025 — /EuropaWire/ — The European Investment Bank (EIB) is providing a €21 million venture debt… |
| 22 Dec 2025 | HEN Technologies | Series A + Venture Debt | $22M | O’Neil Strategic Capital, NSFO, Tanas Capital | United States | HEN Technologies, a Hayward, California-based deep-tech company, has closed an oversubscribed $20 million Series A financing round, along… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 17 Apr 2026 | Ph7 Technologies (ph7technologies.ca) | Venture debt | — | rbcx | Canada | pH7 has secured venture debt financing from RBCx, bringing the total financing package, including Series B equity and venture debt, to… |
| 17 Apr 2026 | Biolamina (biolamina.com) | venture debt | $21.6M | european investment bank | Sweden | BioLamina, a Stockholm-based BioTech scale-up specialising in matrix biology and cell culture, has secured a €20 million financing… |
| 14 Apr 2026 | Common Wealth (commonwealthretirement.com) | venture debt | $11.1M | flow capital | Canada | This funding builds on the $15 million in venture debt that Common Wealth secured from Flow Capital in mid-2025. |
| 13 Apr 2026 | Ph7 Technologies (ph7technologies.ca) | Venture Debt | $7.5M | rbcx | Canada | The company has layered on $7.5 million in venture debt from RBCx—its second facility of this kind from the bank. |
| 24 Mar 2026 | Sokin (sokin.com) | venture debt | $100M | oxford finance llc | — | Mishcon de Reya has advised global payments group Sokin on all UK aspects of a $100 million syndicated secured venture debt facility led… |
| 5 Mar 2026 | Greater Good Health (greatergoodhealth.com) | venture debt | $12.5M | hsbc innovation banking | — | Greater Good Health has secured a $20.5M Series B led by Allumia Ventures, alongside up to $12.5M in venture debt from HSBC Innovation… |
| 25 Feb 2026 | Oq Technology (oqtec.space) | venture debt | $27M | european investment bank | Luxembourg | The European Investment Bank (EIB) extended €25M ($29.5M) in venture debt financing to Luxembourg-based D2D satellite operator OQ… |
| 8 Feb 2026 | Overland AI (overland.ai) | Venture Debt | $20M ⚠ check sentence | triplepoint capital | United States | The total funding announced includes a $20 million venture debt facility from TriplePoint Capital. |

⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --round-type "venture debt" --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --round-type "venture debt" --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --round-type "venture debt" --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"round_type": "venture debt", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"round_type": "venture debt", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [SAAS Funding News](saas-funding-news.md)
- [Unicorn Funding](unicorn-funding.md)
- [Robotics Funding](robotics-funding.md)
- [Cybersecurity Funding](cybersecurity-funding.md)
