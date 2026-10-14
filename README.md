# Prism Business News API

Explore business news within Fliar’s **450M+ news archive**. Archive size is supplied by Fliar; query counts reflect available matching coverage.

Search business coverage, monitor company events, and explore funding deals. Combine sentiment, priority, GCP content codes and themes to turn a broad news search into a focused reading list.

**Private preview.** Production dashboard key issuance and the public API rollout are pending. Proposed API hosts are preview addresses, not confirmed live services. Use the business `API_BASE` supplied when access is granted. Plans are drafts; there is no active checkout.

## Get access and make a first request

1. Sign in to the [Fliar dashboard](https://fliarbi.com/radar/dashboard?tab=apikeys), then open **Fliar Prism workspace → API keys**. Once enabled for your account, create and copy a key. If unavailable, request preview access from Fliar.
2. Set `API_BASE` to the Business News API base URL supplied with your access and `PRISM_API_KEY` to your issued key. The two APIs use the same key and share account quotas.
3. Check access, then search:

```bash
curl -sS "$API_BASE/v1/me" -H "X-API-Key: $PRISM_API_KEY"

curl -sS --get "$API_BASE/v1/business/headlines" \
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
    os.environ["API_BASE"].rstrip("/") + "/v1/business/headlines",
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
