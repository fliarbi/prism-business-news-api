# Fundraise: measured events and news with sources (to Apr 2026)

[Company events research](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

> **Search demand:** “fundraise” · 5,400/month India · 49,500/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 93% of indexed articles (1 of 14 shards offline): counts are lower bounds. Saved API responses: [fundraise.json](../../examples/scenarios/fundraise.json).

**Question.** How many fundraise events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?

**Filters.** event types `funds_raising`.

## At a glance

| Measure | Value |
| --- | ---: |
| Events, May 2025 – Apr 2026 | 2,256 |
| Companies (with a domain) | 1,203 |
| Source articles | 1,977 |
| Busiest month | Feb 2026 (257 events) |
| Tone, Jan–Apr 2026 (negative · neutral · positive) | 1.8% · 0.2% · 98% of 800 articles |

## Twelve months of events

Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).

| Month | Events |  |
| --- | ---: | --- |
| May 2025 | 138 | ███████████ |
| Jun 2025 | 114 | █████████ |
| Jul 2025 | 166 | █████████████ |
| Aug 2025 | 147 | ███████████ |
| Sep 2025 | 205 | ████████████████ |
| Oct 2025 | 160 | ████████████ |
| Nov 2025 | 246 | ███████████████████ |
| Dec 2025 | 164 | █████████████ |
| Jan 2026 | 214 | █████████████████ |
| Feb 2026 | 257 | ████████████████████ |
| Mar 2026 | 228 | ██████████████████ |
| Apr 2026 | 217 | █████████████████ |

## Latest events, Jan – Apr 2026

`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once. Source details were unavailable for 5 of these events at capture time.

| Published | Company domain | Type | Evidence sentence | Source |
| --- | --- | --- | --- | --- |
| 30 Apr 2026 | isquaredcapital.com | Fundraising | the ISQ Global Infrastructure Credit Fund II is expecting a final close in the coming months on its $2.5 billion hard-cap. The fund was launched in… | article unavailable |
| 30 Apr 2026 | voxcapital.com.br | Fundraising | VOX Capital has just signed a check of R$ 10.8 billion in a seed round for startup. According to VOX in a note sent to Startups, this is the initial… | [VOX aporta R$ 10,8M em agtech que une laser e IA para analisar solo…](https://startups.com.br/negocios/agtech/vox-aporta-r-108m-em-agtech-que-une-laser-e-ia-para-analisar-solo/) · startups.com.br |
| 30 Apr 2026 | novastarventures.com | Fundraising | Novastar Ventures has closed its third fund, Africa People and Planet Fund III (NVIII), at $147 million, strengthening its position as one of the… | article unavailable |
| 30 Apr 2026 | crescentcove.com | Fundraising | The final close at $446 million beat the target of $400 million with the support of both existing and new limited partners, Private Debt Investor… | [Crescent Cove Advisors holds close on $446m](https://www.privatedebtinvestor.com/crescent-cove-advisors-holds-close-on-448m/) · privatedebtinvestor.com |
| 30 Apr 2026 | bmwiventures.com | Fundraising | BMW i Ventures plans to finance start-ups in North America and Europe with Fund III. | article unavailable |
| 30 Apr 2026 | eif.org | Fundraising | The European Investment Fund is raising a €15 billion fund of funds to unlock up to €80 billion in scale-up funding. | [Europe’s Earlybird VC closes €360M Fund VIII](https://thenextweb.com/news/earlybird-360m-fund-viii-perpetual-ownership) · thenextweb.com |
| 30 Apr 2026 | earlybird.com | Fundraising | Earlybird Venture Capital has closed its eighth early-stage fund at €360 million, the largest in the Berlin firm’s 29-year history, the company… | [Europe’s Earlybird VC closes €360M Fund VIII](https://thenextweb.com/news/earlybird-360m-fund-viii-perpetual-ownership) · thenextweb.com |
| 30 Apr 2026 | getearlybird.io | Fundraising | Fund laid up and the Handelsblatt explains to have collected with investors for 360 million euros. | [Investoren: Neuer Fonds von Earlybird ist grÃ¶Ãer als seine…](http://www.handelsblatt.com/unternehmen/start-ups/investoren-neuer-fonds-von-earlybird-ist-groesser-als-seine-vorgaenger/100219669.html) · handelsblatt.com |
| 29 Apr 2026 | primarywave.com | Fundraising | Primary Wave confirmed the sizable tranche, specifically consisting of $2.225 billion in commitments, today. | [Primary Wave Confirms 'Final Closing' of $2.2 Billion Fourth Fund](https://www.digitalmusicnews.com/2026/04/29/primary-wave-fourth-fund/) · digitalmusicnews.com |
| 29 Apr 2026 | bmwiventures.com | Fundraising | BMW i Ventures has launched its third fund with a volume of $300 million. | article unavailable |
| 29 Apr 2026 | illuminatefinancial.com | Fundraising | Illuminate Financial, the specialist venture capital firm focused on technology for financial services, today announced it has raised $135 million… | [Illuminate Financial Closes $135m Early Growth Fund to Back the Next…](https://globalfintechseries.com/finance/illuminate-financial-closes-135m-early-growth-fund-to-back-the-next-generation-of-ai-fintech-for-financial-services/) · globalfintechseries.com |
| 29 Apr 2026 | sechacapital.com | Fundraising | Secha Capital has reached a second close of its $40m growth fund, with E Squared Investments joining as a new backer. | [New Secha Capital fund looks to close South Africa's SME growth gap](https://www.zawya.com/en/economy/africa/new-secha-capital-fund-looks-to-close-south-africas-sme-growth-gap-xak2172l) · zawya.com |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
prism-business-news event-trends --event-type funds_raising --since 2025-05-01 --until 2026-04-30 --granularity monthly
prism-business-news events --event-type funds_raising --since 2026-01-01 --until 2026-04-30 --sort newest --limit 15 --resolve true
prism-business-news sentiment --event-type funds_raising --since 2026-01-01 --until 2026-04-30 --granularity monthly
```

The first request with curl, and the second in Python:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/business/event-trends" -H "X-API-Key: $PRISM_API_KEY" -H 'Content-Type: application/json' \
  -d '{"event_type": ["funds_raising"], "since": "2025-05-01", "until": "2026-04-30", "granularity": "monthly"}'
```

```python
import os, requests
r = requests.post(os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/events", headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
                  json={"event_type": ["funds_raising"], "since": "2026-01-01", "until": "2026-04-30", "sort": "newest", "limit": 15, "resolve": true}, timeout=60)
print(r.json()["data"])
```

## Read the result carefully

- Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.
- Dates are source publication dates, not necessarily when a deal or event happened.
- Captured while part of the news index was offline (93% of indexed articles (1 of 14 shards offline)). Every count is a lower bound.
- Article filters require a matching source article in the same window; records without a matching article are excluded. Each deal still counts once.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.
- Zero-count periods are included; partial_period marks buckets only partly covered by the window.
- shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)

## Related demonstrations

- [Bonus Issue](bonus-issue.md)
- [Class Action Lawsuit](class-action-lawsuit.md)
- [Bank Mergers News](bank-mergers-news.md)
- [Insolvency](insolvency.md)
