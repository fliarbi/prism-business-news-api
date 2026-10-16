# Prism Business News API

Explore business news within **450M+ historical and real-time news articles** from Fliar. The article count is supplied by Fliar; query counts reflect available matching coverage.

Search business coverage, monitor company events, and explore funding deals. Combine sentiment, priority, GCP content codes and themes to turn a broad news search into a focused reading list.

**Live.** Base URL `https://radar-api.fliarbi.com/business-news` (general news endpoints: `https://radar-api.fliarbi.com/news`). Create your own key in the Fliar dashboard; one key works on the Radar API and both News APIs. Free tier included; see [plans and prices](#plans-and-prices). While part of the news index is offline, answers say so in `meta.notes` and their counts are lower bounds.

<!-- scenarios:start -->
## 200 worked demonstrations

Real questions, real responses: each page answers one researched search query with
saved live API output: twelve-month deal or event totals, a monthly series, the records
behind them with evidence sentences and sources, plus the exact CLI, curl and Python calls.
[Browse all 200](docs/scenarios/README.md) or start with a segment:

| Segment | Pages | Start with |
| --- | ---: | --- |
| **[Startup funding research](docs/scenarios/funding-research/README.md)** | 50 | [Seed](docs/scenarios/funding-research/seed-funding.md) · [Series A](docs/scenarios/funding-research/series-a-funding.md) · [Series B](docs/scenarios/funding-research/series-b-funding.md) · [AI Startup](docs/scenarios/funding-research/ai-startup-funding-news.md) |
| **[Company events research](docs/scenarios/company-events/README.md)** | 50 | [IPO](docs/scenarios/company-events/ipo.md) · [Upcoming IPO](docs/scenarios/company-events/upcoming-ipo.md) · [Product Recall](docs/scenarios/company-events/product-recall.md) · [Layoffs](docs/scenarios/company-events/layoffs.md) |
| **[Company monitoring research](docs/scenarios/company-monitoring/README.md)** | 50 | [Vodafone Idea](docs/scenarios/company-monitoring/vodafone-idea-news.md) · [Adani](docs/scenarios/company-monitoring/adani-news.md) · [Tesla](docs/scenarios/company-monitoring/tesla-news.md) · [Nintendo](docs/scenarios/company-monitoring/nintendo-news.md) |
| **[Investor research](docs/scenarios/investor-research/README.md)** | 50 | [KKR](docs/scenarios/investor-research/kkr-investments.md) · [Blackstone](docs/scenarios/investor-research/blackstone-investments.md) · [Mubadala](docs/scenarios/investor-research/mubadala-investments.md) · [Sequoia](docs/scenarios/investor-research/sequoia-investments.md) |

Topics come from [keyword research](docs/research/KEYWORD_RESEARCH.md) (India and US monthly searches).
Captured with 1 of 14 news-index shards offline, so counts are lower bounds.
<!-- scenarios:end -->

<!-- demos:start -->
## See the API in a research UI

[6 animated Claude Code / Codex workflow concepts](docs/ANIMATED_USE_CASES.md) show
what an assistant can build on this API. They cover AI funding rankings, a layoff tracker, a company's event profile, investor activity by stage, Indian early-stage funding and hiring versus layoffs, all from captured API responses. Each GIF labels saved API
responses or illustrative data; these are client-built UI concepts, not recordings of
official client interfaces or claims of live service availability. Open the
[interactive gallery](docs/demos/index.html) locally for prompts and request recipes.

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>AI funding · April 2026</h3>
      <a href="docs/demos/media/ai-funding-april-2026.gif"><img src="docs/demos/media/ai-funding-april-2026.gif" width="420" alt="Rank the largest AI funding rounds in a month"></a>
      <p>Rank a sector&#x27;s rounds and keep the sentence behind every number. Saved API responses.</p>
    </td>
    <td width="50%" valign="top">
      <h3>Layoff tracker · April 2026</h3>
      <a href="docs/demos/media/layoffs-april-2026.gif"><img src="docs/demos/media/layoffs-april-2026.gif" width="420" alt="Track a layoff wave across companies"></a>
      <p>Watch a signal build week by week, then read the announcements behind it. Saved API responses.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>Company event mix</h3>
      <a href="docs/demos/media/openai-company-events.gif"><img src="docs/demos/media/openai-company-events.gif" width="420" alt="See everything recorded about one company"></a>
      <p>Get a company&#x27;s whole event profile in one call, then drill into examples. Saved API responses.</p>
    </td>
    <td width="50%" valign="top">
      <h3>Investor activity</h3>
      <a href="docs/demos/media/sequoia-portfolio.gif"><img src="docs/demos/media/sequoia-portfolio.gif" width="420" alt="Profile an investor&#x27;s recent deals by stage"></a>
      <p>See where an investor is active, by stage, with the syndicate behind each round. Saved API responses.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>India early-stage · Q1 2026</h3>
      <a href="docs/demos/media/india-early-stage-q1-2026.gif"><img src="docs/demos/media/india-early-stage-q1-2026.gif" width="420" alt="Size early-stage funding in one country"></a>
      <p>Count a market&#x27;s rounds by stage and month, with original currencies intact. Saved API responses.</p>
    </td>
    <td width="50%" valign="top">
      <h3>Hiring vs layoffs · Q1 2026</h3>
      <a href="docs/demos/media/hiring-vs-layoffs-q1-2026.gif"><img src="docs/demos/media/hiring-vs-layoffs-q1-2026.gif" width="420" alt="Compare hiring and layoff announcements"></a>
      <p>Put two business signals on one timeline and see which companies drive each. Saved API responses.</p>
    </td>
  </tr>
</table>
<!-- demos:end -->

## Install in one line

Requires Bash, curl and Python 3.8+. The installer adds `prism-news` and
`prism-business-news` (one client for both APIs) to `~/.local/bin` and sets
`PRISM_API_BASE` and `PRISM_BUSINESS_API_BASE` for every new shell, so curl, Python
and the CLI work without configuring a URL. It never uses sudo or starts services.

```bash
curl -fsSL https://raw.githubusercontent.com/fliarbi/prism-business-news-api/main/scripts/install.sh | bash
```

See [Getting started](docs/GETTING_STARTED.md) for options, every command and troubleshooting.

## Get started in five steps

| Step | Do this | You get |
|---:|---|---|
| 1 | [Fliar dashboard](https://fliarbi.com/radar/dashboard?tab=radarapi) → **API keys** → **Create or manage API keys** → create a key with **All data** or **News only** access | One `rdr_` key for both News APIs and the Radar API |
| 2 | Run the one-line installer above | The `prism-news` and `prism-business-news` commands |
| 3 | `prism-business-news login` | Base URLs and key saved owner-only in `~/.config/prism/config.json` |
| 4 | `prism-business-news status`, then `prism-business-news me` | Data dates, your plan, limits and this month's usage |
| 5 | Open a [demonstration](docs/scenarios/README.md), copy its commands and change the subject | Your own version of a worked example |

| Task | Command | Endpoint |
|---|---|---|
| Business overview | `prism-business-news overview --q "acquisition" --since 2026-01-01 --until 2026-04-30` | `POST /v1/business/overview` |
| Deal totals by month | `prism-business-news funding-summary --sector fintech --granularity monthly` | `POST /v1/business/funding/summary` |
| Largest rounds | `prism-business-news funding --round-type "series a" --sort amount --limit 20 --table` | `POST /v1/business/funding` |
| An investor's rounds | `prism-business-news funding --investor Sequoia --sort newest --table` | `POST /v1/business/funding` |
| Event counts by month | `prism-business-news event-trends --event-type layoffs --granularity monthly` | `POST /v1/business/event-trends` |
| Latest events with sources | `prism-business-news events --event-type ma --resolve true --table` | `POST /v1/business/events` |
| One company | `prism-business-news company tesla.com --since 2026-01-01` | `GET /v1/business/companies/{domain}/news` |
| Business headlines | `prism-business-news headlines "layoffs" --priority-min 7 --table` | `POST /v1/business/headlines` |
| Any endpoint | `prism-business-news call POST /v1/business/themes '{"q": "acquisition"}'` | any |

## Plans and prices

| Plan | Price | Requests / month | Full-text exports / month | Requests / min | At once | Headlines per call | History |
|---|---|---:|---:|---:|---:|---:|---|
| Free | ₹0 | 1,000 | 100 | 30 | 2 | 100 | Last 365 days |
| **Pay as you go** | **₹0.84 / US$0.01 per credit** | 1 credit each | 1 credit each | by level | by level | your plan's | your plan's |
| Pro | ₹4,000 (US$49) / month | 25,000 | 2,500 | 120 | 5 | 100 | Full history |
| Business | ₹15,000 (US$180) / month | 150,000 | 15,000 | 600 | 10 | 500 | Full history |
| Enterprise | Custom | 2,000,000 | 200,000 | 3,000 | 25 | 1,000 | Full history |

Prices exclude GST. One plan covers both the Prism News API and the Prism Business News API.

**Pay as you go** needs no subscription. Buy prepaid credits (minimum 500 credits, US$5)
on the [API key page](https://fliarbi.com/radar-api/developer); one credit pays for one
request or one full-text article. On Free it starts after the free allowance; on a paid
plan, after the plan's monthly allowance, so nothing stops when you run out. The same
wallet pays for Radar API calls. You set a monthly spending limit, failed requests are
refunded, and a response paid with credits says so in `meta.notes`.

**Usage levels.** The more credits an account has used in total (Radar and Prism News
together), the higher its limits. Levels apply automatically and never go down; from
Growth up, your limits are the higher of your plan's and your level's.

| Level | Credits used (lifetime) | Requests / min | Requests at once | Prepaid credits / day |
|---|---:|---:|---:|---:|
| Starter | 0 | plan | plan | 5,000 |
| Growth | 10,000 | 120 | 5 | 25,000 |
| Scale | 100,000 | 300 | 10 | 100,000 |
| Premier | 1,000,000 | 600 | 20 | 500,000 |

Upgrade or buy credits in the [Fliar dashboard](https://fliarbi.com/radar/dashboard?ws=marketai&tab=radarapi)
under **API keys**; Enterprise is by arrangement with Fliar. `/v1/me` shows your plan,
level and effective limits.

## Make a first request with curl or Python

1. Sign in to the [Fliar dashboard](https://fliarbi.com/radar/dashboard?tab=radarapi), open **API keys** (in the Radar or the Fliar Prism workspace) and choose **Create or manage API keys**. On the key page, choose **Connect Radar session**, pick **All data** or **News only** access and create a key. It starts with `rdr_` and also works on the Radar API.
2. The installer sets `PRISM_BUSINESS_API_BASE`; without it, `export PRISM_BUSINESS_API_BASE=https://radar-api.fliarbi.com/business-news`. Set `PRISM_API_KEY` to your key. The two APIs use the same key and share account quotas.
3. Check access, then search:

```bash
curl -sS "$PRISM_BUSINESS_API_BASE/v1/me" -H "X-API-Key: $PRISM_API_KEY"

curl -sS --get "$PRISM_BUSINESS_API_BASE/v1/business/headlines" \
  -H "X-API-Key: $PRISM_API_KEY" \
  --data-urlencode 'q=acquisition' \
  --data-urlencode 'sentiment=negative' \
  --data-urlencode 'priority_min=7' \
  --data-urlencode 'classes=0' \
  --data-urlencode 'limit=100'
```

GCP code `0` means `/News/Business News/Company News`. These filters combine; start with `q` alone if the result is `404 no_data`. `Authorization: Bearer YOUR_API_KEY` is also accepted.

```python
import os
import requests

response = requests.get(
    os.environ.get("PRISM_BUSINESS_API_BASE", "https://radar-api.fliarbi.com/business-news") + "/v1/business/headlines",
    headers={"X-API-Key": os.environ["PRISM_API_KEY"]},
    params={"company": "amazon.com", "limit": 100},
    timeout=60,
)
payload = response.json()
if not response.ok or not payload.get("ok"):
    raise RuntimeError(f"HTTP {response.status_code}: {payload.get('error')}")
print(payload["window"], payload["meta"].get("notes", []))
for article in payload["data"]["items"]:
    print(article["headline"], article["url"], article["events"])
```

## Choose a workflow

| Goal | Start here |
|---|---|
| Review business coverage | `/v1/business/overview`, then `/v1/business/headlines` |
| Discover and read themes | `/v1/business/themes` with required `q`, at most **5** results; pass a returned theme to headlines with `limit=100` |
| Follow a company | `/v1/business/companies/{domain}/news` |
| Monitor events | `/v1/business/events` and `/v1/business/event-trends` |
| Analyze funding | `/v1/business/funding` and `/v1/business/funding/summary` |
| Retrieve full articles | `/v1/articles/{article_id}` or `/v1/export`, **100** per batch by default; follow the guide to preserve scope |

Headline and export requests default to 100; higher limits depend on your plan. Check `/v1/me` for your caps.

Read the **[Business user guide](docs/USER_GUIDE.md)** for filters, workflows, comparisons, response fields and the endpoint reference. This guide is also served as Markdown at `/guide`. The **[shared News API guide](https://github.com/fliarbi/prism-news-api/blob/main/docs/USER_GUIDE.md)** covers authentication, sentiment and priority labels, GCP codes, export formats, errors, retry and quota rules.

News articles, company events and funding deals are different units and may have different `data_through` dates. Check each response's window before comparing counts or interpreting a recent decline.

## Running the service

Copy `.env.example` to `.env` and fill in the deployment's addresses, credentials and table names. `.env` is never committed. Then:

```bash
pip install -r requirements.txt
./run.sh --bg        # gunicorn on :8801, logs under logs/
python3 -m pytest -q # offline tests, no data stores needed
```
