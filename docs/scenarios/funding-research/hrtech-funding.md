# Hrtech Funding: measured deals with sources (to Apr 2026)

[Startup funding research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “hrtech funding” · volume below estimate threshold  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [hrtech-funding.json](../../examples/scenarios/hrtech-funding.json).

**Question.** How many hrtech deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?

**Filters.** sector “hrtech”.

## At a glance

| Measure | Value |
| --- | ---: |
| Deal records, May 2025 – Apr 2026 | 35 |
| With a usable reported amount | 32 |
| Reported total (usable amounts) | $806.2M |
| Median reported round | $7.2M |
| Largest reported round | $450M |
| Busiest month | May 2025 (7 deals) |

## Twelve months of deals

Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).

| Month | Deals | With amount | Reported total | Median |  |
| --- | ---: | ---: | ---: | ---: | --- |
| May 2025 | 7 | 5 | $32.6M | $5M | ████████████████████ |
| Jun 2025 | 3 | 3 | $63M | $20M | █████████ |
| Jul 2025 | 3 | 3 | $28.1M | $3.8M | █████████ |
| Aug 2025 | 1 | 1 | $40M | $40M | ███ |
| Sep 2025 | 3 | 3 | $5.5M | $1.1M | █████████ |
| Oct 2025 | 4 | 4 | $95M | $28.1M | ███████████ |
| Nov 2025 | 5 | 4 | $19.7M | $2.2M | ██████████████ |
| Dec 2025 | 1 | 1 | $27.5M | $27.5M | ███ |
| Jan 2026 | 0 | 0 | — | — |  |
| Feb 2026 | 5 | 5 | $32.9M | $5.5M | ██████████████ |
| Mar 2026 | 1 | 1 | $8.1M | $8.1M | ███ |
| Apr 2026 | 2 | 2 | $453.8M | $226.9M | ██████ |

## Largest reported rounds, May 2025 – Apr 2026

`sort=amount`, limit 40; the largest record per company is shown. 4 further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 2 Apr 2026 | Vensure Employer Solutions | Term loan | $450M | Stone Point Capital Markets | — | Vensure Employer Solutions received $450 million in support for its expansion strategy through a delayed draw term loan from Stone Point… |
| 29 Oct 2025 | Sesame (sesamecare.com) | growth | $54M | BBVA Spark | Spain | Sesame, a Spanish HRTech startup specializing in AI-driven talent management, has secured up to €50 million in growth funding through a… |
| 14 Aug 2025 | Darwinbox (darwinbox.com) | — | $40M | Teachers' Venture Growth (TVG) | India | HRTech startup Darwinbox has raised US$40 million (approx. Rs 350 crore) from Teachers’ Venture Growth (TVG), which is the late‑stage… |
| 28 Oct 2025 | Maki (makimaki.nl) | — | $28.1M | — | France | In France, Maki attracted €26 million to develop conversational AI agents for HR workflows. |
| 17 Dec 2025 | Ben (benfleetservices.com) | Series B | $27.5M | Mercia Ventures, atomico, cherry ventures | United Kingdom | Today, Ben has secured $27.5 million in Series B funding, led by Mercia Ventures with participation from long‑time backers Atomico, Cherry… |
| 30 Jul 2025 | Wingspan (wingspan.app) | Series B | $24M | Touring Capital, Andreessen Horowitz, long journey ventures | — | Wingspan, the first modern payroll platform purpose‑built for contractor management, announced that it has raised $24 million in Series B… |
| 16 Jun 2025 | Workwhile (workwhilejobs.com) | Series B | $23M | rethink impact, khosla ventures, reach capital | United States | WorkWhile, the innovative AI-powered labor platform that matches businesses with reliable hourly workers, announced that it has raised $23… |
| 19 May 2025 | Origin (originww.com) | Series A | $21M | felix capital, acadian ventures, notion capital | United Kingdom | Origin, a London, UK-based AI-powered global benefits intelligence platform, has raised $21 million in Series A funding. |
| 24 Jun 2025 | Paraform (paraform.com) | Series A | $20M | A*, bond, dst global | USA | Paraform, the hiring marketplace built for elite recruiters, today announced its $20 million in Series A funding led by Felicis, with… |
| 12 Jun 2025 | Zorro (myzorro.co) | Series A | $20M | entrée capital, 10d, pitango | United States | Zorro (the “Company”), a next-generation benefits administration platform using advanced technology and big data to transform how… |

## Latest rounds, Jan – Apr 2026

`sort=newest`, limit 10.

| Published | Company | Round | Amount (USD) | Investors | Country | Evidence sentence |
| --- | --- | --- | ---: | --- | --- | --- |
| 21 Apr 2026 | Inploi (inploi.com) | — | $3.8M | yfm equity partners | UK | inploi has secured £3 million in funding from YFM Equity Partners to support its platform candidates use during the hiring process, which… |
| 2 Apr 2026 | Vensure Employer Solutions | Term loan | $450M | Stone Point Capital Markets | — | Vensure Employer Solutions received $450 million in support for its expansion strategy through a delayed draw term loan from Stone Point… |
| 31 Mar 2026 | Novaworks (novaworks.com) | Seed | $8.1M | Stalwart Ventures, servicenow, Bell Ventures | United States | Novaworks has raised $8M in funding from Stalwart Ventures. |
| 27 Feb 2026 | Comp (compareemcasa.com.br) | Series A | $17.5M | khosla ventures, kaszek, canary | Brazil | The Brazilian HRtech raised $17.5 million in a Series A round led by Khosla Ventures, marking the firm’s first investment in Brazil.… |
| 25 Feb 2026 | Elly (elly.io) | — | $8M | sorenson capital, atomic, Next Wave Capital | USA | Elly announced the launch of its AI-native hiring platform along with $8 million in funding led by Sorenson Capital, with participation… |
| 17 Feb 2026 | Clarait GmbH | seed | $1.6M | TGFS Technologiegründerfonds Sachsen, HR Angels Club | — | clarait GmbH, a B2B SaaS company specialized in digital committee work and HR processes, has collected over 1.5 million euros in a seed… |
| 17 Feb 2026 | Atypical Advantage (atypicaladvantage.in) | Seed | $290k | Next Bharat Ventures | India | Atypical Advantage Enterprise Applications &gt; HRTech Jharkhand $290K Seed Next Bharat Ventures |
| 11 Feb 2026 | Pelgo | seed | $5.5M | Flybridge Capital Partners, eniac ventures, primary… | — | Pelgo, the AI-powered career transition agent, announced it has raised $5.5 million in seed funding. Led by Flybridge Capital Partners,… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news funding-summary --sector hrtech --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news funding --sector hrtech --since 2025-05-01 --until 2026-04-30 --sort amount --limit 40
prism-business-news funding --sector hrtech --since 2026-01-01 --until 2026-04-30 --sort newest --limit 10
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/funding/summary" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"sector": "hrtech", "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/funding", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"sector": "hrtech", "since": "2025-05-01", "until": "2026-04-30", "sort": "amount", "limit": 40}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.

## Related demonstrations

- [E-commerce Funding](e-commerce-funding.md)
- [Foodtech Funding](foodtech-funding.md)
- [Legaltech Funding](legaltech-funding.md)
- [Lending Startup Funding](lending-startup-funding.md)
