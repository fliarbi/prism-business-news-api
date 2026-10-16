# KKR Investments: measured deals with sources (to Apr 2026)

[Investor research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “kkr investments” · 5,400/month India · 2,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [kkr-investments.json](../../examples/scenarios/kkr-investments.json).

**Question.** Which rounds did KKR appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?

**Filters.** investor “KKR”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 116 |
| With a usable reported amount | 93 |
| Reported total (usable amounts) | $102.7B |
| Median reported round | $500M |
| Largest reported round | $10B |
| Amounts left out as implausible or unconverted | 3 |
| Busiest month | Nov 2025 (16 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 5 | 4 | $12.1B | $5.1B | ██████ |
| Jun 2025 | 10 | 6 | $2.7B | $546M | ████████████ |
| Jul 2025 | 11 | 9 | $5.7B | $330M | ██████████████ |
| Aug 2025 | 8 | 5 | $3.6B | $290.5M | ██████████ |
| Sep 2025 | 11 | 10 | $27.5B | $3.6B | ██████████████ |
| Oct 2025 | 3 | 1 | $60M | $60M | ████ |
| Nov 2025 | 16 | 12 | $13B | $750M | ████████████████████ |
| Dec 2025 | 9 | 9 | $1.5B | $312M | ███████████ |
| Jan 2026 | 10 | 7 | $14.2B | $1.7B | ████████████ |
| Feb 2026 | 5 | 5 | $11.5B | $1.5B | ██████ |
| Mar 2026 | 15 | 12 | $5.9B | $310M | ███████████████████ |
| Apr 2026 | 13 | 13 | $6.1B | $750M | ████████████████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 21 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 24 Sep 2025 | Sempra Infrastructure Partners | Equity sale | $10B | canada pension plan investment board, kkr | USA | Topping the list is its agreement to sell 45 percent of Sempra Infrastructure Partners, one of North America’s leading energy… |
| 21 May 2025 | Masorange | — | $6.8B | orange, providence, kkr | Spain | This financing package includes €6.25 billion to improve Masorange’s financial conditions by refinancing the senior debt |
| 20 Jan 2026 | AV AirFinance (avairfinance.com) | — | $5B | kkr, KKR-managed funds | — | The investment is financed by the KKR balance sheet and is supplemented by the already over 5 billion USD, which has invested KKR-managed… |
| 20 Jan 2026 | Altavair (altavair.com) | — | $5B | kkr, KKR-managed funds | — | The investment is financed by the KKR balance sheet and is supplemented by the already over 5 billion USD, which has invested KKR-managed… |
| 11 Nov 2025 | St Telemedia Global Data Centres (stt Gdc) (sttelemediagdc.com) | bridge loan | $5B | kkr, singtel | Singapore | Singapore - A consortium comprising KKR and Singtel is in talks with banks for a loan of around $5 billion to support its proposed… |
| 24 Feb 2026 | Beverage (dedebeverage.com) | convertible preferred equity | $4.5B | apollo, kkr, T Rowe Price Investment Management | USA | The upsized convertible preferred equity round is co-led by Apollo and KKR, with additional participation from backerts including accounts… |
| 24 Feb 2026 | Global Coffee Co. Pod Manufacturing Joint Venture | equity investment | $4B | apollo, kkr, Goldman Sachs Alternatives | — | That JV includes a $4bn investment co-led by Apollo and KKR, with participation from Goldman Sachs Alternatives, and remains subject to… |
| 27 Nov 2025 | Serentica Renewables (serenticaglobal.com) | — | $3B | kkr | India | The first phase of the planned investment, about $3 billion, is fully funded |
| 19 Aug 2025 | Flexera Software (flexerasoftware.com) | debt financing | $3B | kkr | — | KKR ( NYSE: KKR ) announced on Tuesday an investment in the debt financing round for recapitalization of the technology spend and risk… |
| 30 Jul 2025 | New Reinsurance Sidecar-like Co-investment Vehicle | Co-investment sidecar vehicle | $2B | japan post insurance, kkr, global atlantic | Japan | Japan Post Insurance investing the maximum $2 billion into the structure, as it looks to diversify its own sources of insurance-linked… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 28 Apr 2026 | Baby Memorial Hospital (babymhospital.org) | initial investment | $252M | kkr | India | KKR had initially invested ₹2,100 crore in Baby Memorial Hospital in July 2024 to create a platform of hospitals in southern India. |
| 28 Apr 2026 | Baby Memorial Hospital (babymhospital.org) | rights issue | $210M | kkr | India | KKR has pumped ₹1,750 crore in Baby Memorial Hospital by way of a rights issue as it positions the Kozhikode-based healthcare player for a… |
| 28 Apr 2026 | Baby Memorial Hospital (babymhospital.org) | follow-on investment | $151.3M | kkr | India | It increased its investment by ₹1,261 crore in the hospital in September last year before the latest funding round, the documents showed. |
| 24 Apr 2026 | Vertical Bridge (verticalbridge.com) | Strategic Equity | $1.5B | kkr, digitalbridge, CDPQ | United States | Vertical Bridge has secured a $1.5 billion strategic equity investment from KKR to accelerate the expansion of its nationwide wireless… |
| 23 Apr 2026 | Vertical Bridge REIT | equity investment | $1.5B | kkr | — | KKR has plans to make a $1.5 billion equity investment in Vertical Bridge REIT to support its future growth. |
| 15 Apr 2026 | Samsung Sds (samsungsds.com) | convertible bonds | $915M | KKR & Co. | South Korea | Samsung SDS Co., South Korea’s enterprise IT service provider, has raised 1.22 trillion won ($820 million) from KKR & Co. through… |
| 14 Apr 2026 | Skeena Gold & Silver | Senior secured notes | $750M | kkr, bank of america | Canada | Skeena Gold & Silver announced it has completed a $750 million aggregate principal offering of 8.500% senior secured notes maturing in 2031 |
| 10 Apr 2026 | Skeena Resources (skeenaresources.com) | Debt | $750M | kkr, bank of america | Canada | The strong support for this debt issuance from leading global investment firms, including KKR and Bank of America, underscores growing… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --investor KKR --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --investor KKR --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --investor KKR --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"investor": "KKR", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ["API_BASE"] + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"investor": "KKR", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Investor names match broadly (a name can match several firms or funds); use a domain for a narrower match.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [Blackstone Investments](blackstone-investments.md)
- [Mubadala Investments](mubadala-investments.md)
