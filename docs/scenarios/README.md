# Prism Business News API demonstrations: 200 worked examples

[README](../../README.md) · [Keyword research](../research/KEYWORD_RESEARCH.md) · [User guide](../USER_GUIDE.md) · [Animated gallery](../ANIMATED_USE_CASES.md)

Each demonstration answers one real search query with saved responses from the live API:
twelve-month deal or event totals, a monthly series, the records behind them with evidence
sentences and sources, and the exact requests to reproduce it. Topics were chosen by
[keyword research](../research/KEYWORD_RESEARCH.md) (India and US monthly searches) and kept
only when the API returned populated results.

| Segment | Pages | Highest-demand pages |
| --- | ---: | --- |
| [Startup funding research](funding-research/README.md) | 50 | [Seed Funding](funding-research/seed-funding.md), [Series A Funding](funding-research/series-a-funding.md), [Series B Funding](funding-research/series-b-funding.md) |
| [Company events research](company-events/README.md) | 50 | [IPO](company-events/ipo.md), [Upcoming IPO](company-events/upcoming-ipo.md), [Product Recall](company-events/product-recall.md) |
| [Company monitoring research](company-monitoring/README.md) | 50 | [Vodafone Idea News](company-monitoring/vodafone-idea-news.md), [Adani News](company-monitoring/adani-news.md), [Tesla News](company-monitoring/tesla-news.md) |
| [Investor research](investor-research/README.md) | 50 | [KKR Investments](investor-research/kkr-investments.md), [Blackstone Investments](investor-research/blackstone-investments.md), [Mubadala Investments](investor-research/mubadala-investments.md) |

Captured 16 Oct 2026 from the live API. Part of the news index was offline (1 of 14 shards,
about 93% of rows available), so every count is a lower bound; some source articles were
temporarily unavailable and each page says how many.

Regenerate: `scripts/plan_scenarios.py` → `scripts/capture_scenarios.py` → `scripts/build_scenario_pages.py`.
