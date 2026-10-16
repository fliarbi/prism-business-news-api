# Bank Mergers News: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “bank mergers news” · 33,100/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of archive rows (1 of 14 shards offline): counts are lower bounds. Saved API responses: [bank-mergers-news.json](../../examples/scenarios/bank-mergers-news.json).

**Question.** How many bank mergers events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `ma` and the word “bank” in the event sentence.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 1,688 |
| Companies (with a domain) | 923 |
| Source articles | 1,080 |
| Busiest month | Oct 2025 (179 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 6.8% · 4.8% · 88% of 842 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 113 | █████████████ |
| Jun 2025 | 114 | █████████████ |
| Jul 2025 | 121 | ██████████████ |
| Aug 2025 | 125 | ██████████████ |
| Sep 2025 | 129 | ██████████████ |
| Oct 2025 | 179 | ████████████████████ |
| Nov 2025 | 131 | ███████████████ |
| Dec 2025 | 125 | ██████████████ |
| Jan 2026 | 178 | ████████████████████ |
| Feb 2026 | 165 | ██████████████████ |
| Mar 2026 | 170 | ███████████████████ |
| Apr 2026 | 138 | ███████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 5 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | anz.com.au | M&A | The bank has signed a binding agreement to acquire Worldline’s 51% stake in ANZ Worldline for an enterprise value of A$89m, giving it complete… | [ANZ takes full control of venture with Worldline](https://paymentsindustryintelligence.com/anz-takes-full-control-of-venture-with-worldline/) · paymentsindustryintelligence.com |
| 30 Apr 2026 | lcl.fr | M&A | LCL's acquisition of the Milleis Group, composed of Milleis Bank and its subsidiaries Milleis Vie, Cholet Dupont Oudart and Cholet Dupont Asset… | [CREDIT AGRICOLE SA : LCL et Crédit Agricole Assurances finalisent…](https://fr.finance.yahoo.com/actualites/credit-agricole-lcl-cr%C3%A9dit-agricole-163300926.html) · fr.finance.yahoo.com |
| 30 Apr 2026 | federalbank.co.in | M&A | Federal Bank has entered into an agreement with Standard Chartered Bank India to acquire the British lender’s select portfolio of credit card… | [Federal Bank snaps up StaC’s credit card biz](https://www.newindianexpress.com/business/2026/Apr/30/federal-bank-snaps-up-stacs-credit-card-biz) · newindianexpress.com |
| 30 Apr 2026 | federalbank.co.in | M&A | The Board of Directors of Federal Bank, at its meeting held on April 30, 2026, has approved that the bank proceed to enter into a deed of assignment… | [Federal Bank Skips Deutsche Bank Deal, Picks Up StanChart's Credit…](https://www.outlookbusiness.com/corporate/federal-bank-skips-deutsche-bank-deal-picks-up-stancharts-credit-card-portfolio-instead) · outlookbusiness.com |
| 30 Apr 2026 | novobanco.pt | M&A | Today announced it has successfully completed the sale of its majority stake in Novo Banco, S.A. (“novobanco” or “the bank”), Portugal’s… | article unavailable |
| 30 Apr 2026 | holmarcom.ma | M&A | Following discussions announced in December 2025, BNP Paribas announced an agreement to sell to Holmarcom Finance Company its 67% majority stake in… | [Bnp paribas act.a : BNP Paribas vend la BMCI à Holmarcom au Maroc](https://tradingsat.com/bnp-paribas-acta-FR0000131104/actualites/bnp-paribas-acta-bnp-paribas-vend-la-bmci-a-holmarcom-au-maroc-1161786.html) · tradingsat.com |
| 29 Apr 2026 | holmarcom.ma | M&A | BNP Paribas and Holmarcom Finance Company have concluded an agreement concerning the sale by BNP Paribas to HFC of its full 67% majority stake in… | article unavailable |
| 29 Apr 2026 | bnccorp.com | M&A | Sidley is representing digital finance company OppFi Inc. (NYSE: OPFI) in its US$130 million agreement to acquire BNCCORP, Inc. (OTCQX: BNCC) and… | [Sidley Represents OppFi In Its Acquisition of BNCC and BNC National…](https://www.sidley.com/ja/newslanding/newsannouncements/2026/04/sidley-represents-oppfi-in-its-acquisition-of-bncc-and-bnc-national-bank) · sidley.com |
| 29 Apr 2026 | mtn.com | M&A | MTN Nigeria Communications Plc has unveiled plans to sell a 60 percent stake in its fintech subsidiaries MoMo Payment Service Bank and Y’ello… | [MTN Nigeria Plans N152bn Fintech Stake Sale to Parent Company,…](https://thewillnews.com/mtn-nigeria-plans-n152bn-fintech-stake-sale-to-parent-company-retains-40-percent-holding/) · thewillnews.com |
| 29 Apr 2026 | mtn.com | M&A | MTN Nigeria has announced it is selling a 60% majority stake in its fintech subsidiaries, MoMo Payment Service Bank and Y’ello Digital Financial… | [MTN Group Tightens Grip on Nigeria’s Fintech Business as It…](https://innovation-village.com/mtn-group-tightens-grip-on-nigerias-fintech-business-as-it-centralises-africa-payments-strategy/) · innovation-village.com |
| 29 Apr 2026 | equitygroupholdings.com | M&A | Angola is the most advanced target with Equity moving to acquire a majority stake in an undisclosed Angolan bank in 2026, having reprioritized after… | article unavailable |
| 29 Apr 2026 | mtn.com | M&A | MTN Nigeria Communications Plc has announced plans to sell a 60% stake in its fintech subsidiaries, MoMo Payment Service Bank and Y’ello Digital… | article unavailable |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type ma --q bank --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type ma --q bank --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type ma --q bank --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["ma"], "q": "bank", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["ma"], "q": "bank", "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the archive was offline (93% of archive rows (1 of 14 shards offline)). Every count is a lower bound.
- Article filters require a matching source article in the same window; records without a matching article are excluded. Each deal still counts once.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.
- Zero-count periods are included; partial_period marks buckets only partly covered by the window.
- shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)

## Related demonstrations

- [Class Action Lawsuit](class-action-lawsuit.md)
- [Fundraise](fundraise.md)
- [Insolvency](insolvency.md)
- [Joint Venture](joint-venture.md)
