#!/usr/bin/env python3
"""Build source-qualified UI animation stories from saved responses; no live calls.

Every chart is computed from the real API responses in docs/examples/demo/
(scripts/capture_demo_examples.py). Where a view merges or groups rows, the
merge is done here, in the open, and the story says so. Every request body is
validated with the API's own request model before it is written into a recipe.
"""
from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from demo_common import captured_on, day, evidence, kind_of, local, read, trim, usd, write_outputs  # noqa: E402
from prism_business_api.filters import BusinessFilters  # noqa: E402

GUIDE = "../USER_GUIDE.md"
PATHS = {"/v1/business/funding", "/v1/business/events"}
EVENT_LABEL = {"key_people": "Key people", "funding_rounds": "Funding rounds", "contracts": "Contracts", "ma": "M&A",
               "company_announcement": "Announcements", "lawsuit": "Lawsuits", "new_product": "New products",
               "capital_infusion": "Capital infusion", "job_creation": "Job creation", "layoffs": "Layoffs",
               "earnings": "Earnings", "ipo": "IPO", "asset_acquisition": "Asset acquisition", "regulatory": "Regulatory"}
# Company links are extracted from text; these captured domains are known mislinks.
MISLINKED = {"metavision.com": "Meta", "meetblock.com": "Block"}  # domain -> company it was meant for


def validate(path: str, body: dict) -> None:
    """Raise unless the API itself would accept this request body."""
    assert path in PATHS, path
    BusinessFilters.model_validate(body)


def step(name: str, label: str, pages: str = "") -> dict:
    rec = read(name)
    validate(rec["request"]["path"], rec["request"]["body"])
    detail = f" · followed next_cursor for {rec['pages_fetched']} pages" if rec.get("pages_fetched", 1) > 1 else ""
    return {"type": "api", "method": rec["request"]["method"], "path": rec["request"]["path"],
            "body": rec["request"]["body"], "label": label + detail}


def data(name: str) -> dict:
    return read(name)["response"]["data"]


def story(id, names, **kw):
    kind = kind_of(names)
    assert kind == "captured", f"{id}: business demos use captured responses only"
    return {"id": id, "brand": "Prism Business News", "kind": kind,
            "badge": f"Captured data · {captured_on(names)}", "sources": evidence(names), **kw}


def dedupe(items: list[dict]) -> list[dict]:
    """One row per (company, amount): the listing returns deal records, and one
    round is often recorded several times under different round labels."""
    seen, out = set(), []
    for i in items:
        key = ((i["domain"] or i["company_name"] or "").lower(), i["amount_usd"])
        if key not in seen:
            seen.add(key)
            out.append(i)
    return out


def stage(round_type: str | None) -> str:
    r = re.sub(r"[‐-―]", "-", (round_type or "").lower())
    if re.search(r"pre-?\s?seed|angel", r):
        return "Pre-seed"
    if re.search(r"pre-?\s?series a|pre-?a\b", r):
        return "Pre-Series A"
    if re.search(r"pre-?\s?series b", r):
        return "Pre-Series B"
    if "seed" in r:
        return "Seed"
    m = re.search(r"series\s?([a-z])\b|\b([a-z])\s?series", r)
    if m:
        letter = (m.group(1) or m.group(2)).upper()
        return f"Series {letter}" if letter in "ABCD" else "Series E+"
    return "Other or undisclosed"


def name(n: str | None) -> str:
    return (n or "").title() if (n or "").islower() else (n or "")


def tag(label: str | None) -> dict:
    return {"tag": trim(label, 18) if label else "not stated"}


def twins(rows: list[dict]) -> list[str]:
    """Names that share a first word and an amount with another row: one round
    recorded under two company-name variants."""
    first = lambda i: (i["company_name"] or "").lower().split()[0]
    return sorted({name(a["company_name"]) for a in rows for b in rows
                   if a is not b and a["amount_usd"] == b["amount_usd"] and first(a) == first(b)})


def mondays(since: str, until: str) -> list[date]:
    d, end = date.fromisoformat(since), date.fromisoformat(until)
    start = d - timedelta(days=d.weekday())
    return [start + timedelta(weeks=k) for k in range((end - start).days // 7 + 1)]


def weekly(items: list[dict], since: str, until: str, pred=lambda i: True) -> tuple[list[date], list[int]]:
    weeks = mondays(since, until)
    c = Counter()
    for i in items:
        if pred(i):
            d = date.fromisoformat(i["published_at"][:10])
            c[d - timedelta(days=d.weekday())] += 1
    return weeks, [c[w] for w in weeks]


def partial(w: date, since: str, until: str) -> bool:
    return w < date.fromisoformat(since) or w + timedelta(days=6) > date.fromisoformat(until)


def domain_cell(domain: str | None, count: int | None = None) -> dict:
    sub = f"{count} events" if count is not None else ""
    if domain in MISLINKED:
        return {"main": f"{domain} ⚠", "sub": f"{sub} · check link: not {MISLINKED[domain]}'s domain".strip(" ·")}
    return {"main": domain or "unlinked", "sub": sub}


def build() -> None:
    stories = []

    ai = data("ai-funding-april-2026")
    rows = dedupe(ai["items"])
    t = ai["totals"]
    top = [r for r in rows if r["amount_usd"]][:6]
    stories.append(story(
        "ai-funding-april-2026", ["ai-funding-april-2026"],
        nav="AI funding · April 2026", client="Claude Code", heading="Follow the money in a sector",
        title="Rank the largest AI funding rounds in a month",
        prompt="Which AI companies raised the largest rounds in April 2026? Rank them, keep the source sentence for each amount, and tell me how many deals had no usable amount.",
        steps=[step("ai-funding-april-2026", "Funding deals, largest usable amount first"),
               local("Merge repeated records", f"{len(ai['items'])} listing rows → {len(rows)} after merging the same company and amount")],
        overview={"type": "bars", "title": "The largest AI rounds of April 2026", "prefix": "$", "labelWidth": 430,
                  "subtitle": f"{t['deals']} AI deal records · amounts as reported, converted to USD",
                  "axisLabel": "Usable reported amount (USD)",
                  "rows": [{"label": name(r["company_name"]),
                            "sub": f"{r['domain'] or 'no domain'} · {r['round_type'] or 'round not stated'} · {day(r['published_at'])}",
                            "value": r["amount_usd"], "display": usd(r["amount_usd"])} for r in top],
                  "stats": [{"value": str(t["deals"]), "label": "deal records in the window"},
                            {"value": str(t["deals_with_amount"]), "label": "with a usable amount"},
                            {"value": str(t["deals_amount_excluded"]), "label": "amounts withheld (implausible or unconverted)"},
                            {"value": usd(t["median_amount_usd"]), "label": "median usable amount"}]},
        detail={"type": "table", "title": "Each amount, with the sentence it came from",
                "subtitle": "Top rounds after merging repeated records · read the sentence before quoting a figure",
                "headers": ["Company", "Round", "Amount", "Source sentence"], "widths": [19, 14, 11, 56],
                "rows": [[{"main": name(r["company_name"]), "sub": f"{r['domain'] or 'no domain'} · {day(r['published_at'])}"},
                          tag(r["round_type"]), {"num": usd(r["amount_usd"])},
                          {"sub": trim(r["source_sentence"], 150)}] for r in top[:5]],
                "note": "Reported amounts can include conditional tranches: the $25B Anthropic row counts $20B tied to milestones in its source sentence."},
        footnote="Amounts are extracted from news and converted at fixed rates; they are not verified deal values.",
        takeaway="Rank a sector's rounds and keep the sentence behind every number.",
        evidence_summary="Saved funding listing, AI sector, April 2026",
        guide=f"{GUIDE}#funding-deals"))

    lay = data("layoffs-april-2026")
    W = ("2026-04-01", "2026-04-30")
    weeks, counts = weekly(lay["items"], *W)
    companies = Counter(i["domain"] for i in lay["items"] if i["domain"])
    stories.append(story(
        "layoffs-april-2026", ["layoffs-april-2026"],
        nav="Layoff tracker · April 2026", client="Codex", heading="Track a business signal week by week",
        title="Track a layoff wave across companies",
        prompt="Track layoff announcements through April 2026 week by week. How many companies were involved, and what are the latest announcements?",
        steps=[step("layoffs-april-2026", "Layoff events in the window"),
               local("Bucket by week", "Client counts every returned event; all pages were read")],
        overview={"type": "columns", "title": "Layoff events per week, April 2026", "unit": "events per week", "height": 270,
                  "subtitle": f"{lay['total_estimate']} events from extracted announcements · weeks start Monday",
                  "labels": [w.strftime("%-d %b") for w in weeks],
                  "sublabels": ["partial week" if partial(w, *W) else "" for w in weeks],
                  "series": [{"name": "Layoff events", "tone": "negative", "values": counts}],
                  "stats": [{"value": str(lay["total_estimate"]), "label": "layoff events"},
                            {"value": str(len(companies)), "label": "linked company domains"},
                            {"value": str(sum(1 for n in companies.values() if n >= 3)), "label": "companies with 3+ events"},
                            {"value": max(zip(counts, weeks))[1].strftime("%-d %b"), "label": "busiest week"}]},
        detail={"type": "table", "title": "The latest announcements", "subtitle": "Newest first · the extracted sentence and the linked company",
                "headers": ["Company", "Announcement", "Published"], "widths": [22, 64, 14],
                "rows": [[domain_cell(i["domain"]), {"sub": trim(i["headline"], 160)}, day(i["published_at"])] for i in lay["items"][:6]],
                "note": "An event is one extracted sentence; one article can describe several layoffs, and one layoff can appear in several articles."},
        footnote="Event dates are article publication dates, not when the layoffs take effect.",
        takeaway="Watch a signal build week by week, then read the announcements behind it.",
        evidence_summary="Saved layoff events, April 2026, all pages",
        guide=f"{GUIDE}#company-events"))

    oa = data("openai-events")
    by = sorted(oa["by_type"].items(), key=lambda kv: -kv[1])
    segs = [{"label": EVENT_LABEL.get(k, k), "value": v} for k, v in by[:6]]
    segs.append({"label": "Other types", "value": sum(v for _, v in by[6:]), "color": "#a3afc0"})
    picked, seen = [], set()
    for i in oa["items"]:
        if i["event_type"] not in seen:
            seen.add(i["event_type"])
            picked.append(i)
    stories.append(story(
        "openai-company-events", ["openai-events"],
        nav="Company event mix", client="Claude Code", heading="Brief yourself on one company",
        title="See everything recorded about one company",
        prompt="Brief me on OpenAI from November 2025 to April 2026: what kinds of events were reported, and show one recent example of each.",
        steps=[step("openai-events", "Events for one company domain"),
               local("Pick one example per type", "Newest event of each type from the first page")],
        overview={"type": "donut", "title": "OpenAI's recorded events by type",
                  "subtitle": "Nov 2025 – Apr 2026 · counts cover the whole window, not just one page",
                  "segments": segs, "centerValue": f"{oa['total_estimate']}", "centerLabel": "events",
                  "side": "One article can carry several events; counts are distinct article, type, role and date."},
        detail={"type": "table", "title": "One recent example of each event type", "subtitle": "Newest first · extracted sentence, role and publication date",
                "headers": ["Type", "Extracted sentence", "Role", "Published"], "widths": [17, 59, 11, 13],
                "rows": [[{"tag": EVENT_LABEL.get(i["event_type"], i["event_type"])}, {"sub": trim(i["headline"], 150)},
                          i["role"], day(i["published_at"])] for i in picked[:6]],
                "note": "Role says how the company appears in the event (primary, acquirer, target, client…)."},
        footnote="Events are extracted from news sentences and linked to a company domain; check the sentence before relying on it.",
        takeaway="Get a company's whole event profile in one call, then drill into examples.",
        evidence_summary="Saved company events for openai.com",
        guide=f"{GUIDE}#one-company"))

    sq = data("sequoia-portfolio")
    uniq = dedupe(sq["items"])
    order = ["Pre-seed", "Seed", "Series A", "Series B", "Series C", "Series D", "Series E+", "Other or undisclosed"]
    stages = Counter(stage(i["round_type"]) for i in uniq)
    big = [i for i in sorted(uniq, key=lambda i: -(i["amount_usd"] or 0)) if i["amount_usd"]][:6]
    stories.append(story(
        "sequoia-portfolio", ["sequoia-portfolio"],
        nav="Investor activity", client="Codex", heading="Profile an investor's recent deals",
        title="Profile an investor's recent deals by stage",
        prompt="Which rounds did Sequoia join between November 2025 and April 2026? Break them down by stage and list the largest with co-investors.",
        steps=[step("sequoia-portfolio", "Deals naming the investor"),
               local("Merge and group", f"{len(sq['items'])} records → {len(uniq)} after merging the same company and amount; stage from the recorded label")],
        overview={"type": "bars", "title": "Sequoia's recorded rounds by stage", "labelWidth": 300,
                  "subtitle": f"{sq['totals']['deals']} deal records naming Sequoia · {len(uniq)} after merging repeats",
                  "axisLabel": "Rounds (merged)",
                  "rows": [{"label": s, "value": stages[s], "display": f"{stages[s]} rounds"} for s in order if stages[s]],
                  "stats": [{"value": str(sq["totals"]["deals"]), "label": "deal records"},
                            {"value": str(len(uniq)), "label": "after merging repeats"},
                            {"value": str(stages["Other or undisclosed"]), "label": "stage not stated"},
                            {"value": usd(sq["totals"]["median_amount_usd"]), "label": "median usable amount"}]},
        detail={"type": "table", "title": "The largest rounds, with co-investors", "subtitle": "Merged records · investors as listed in the deal",
                "headers": ["Company", "Round", "Amount", "Co-investors", "Published"], "widths": [17, 15, 11, 44, 13],
                "rows": [[{"main": name(i["company_name"]), "sub": i["domain"] or ""}, tag(i["round_type"]), {"num": usd(i["amount_usd"])},
                          {"sub": trim(", ".join(x["name"] for x in i["investors"] if "sequoia" not in x["name"].lower()), 110) or "none listed"},
                          day(i["published_at"])] for i in big],
                "note": "Re-reports and name variants stay separate records" + (f" ({' / '.join(twins(big))})" if twins(big) else "") + "; compare amounts and dates."},
        footnote="Investor matching is a name match on the deal's investor list; check the name variant in each row.",
        takeaway="See where an investor is active, by stage, with the syndicate behind each round.",
        evidence_summary="Saved funding deals naming Sequoia, all pages",
        guide=f"{GUIDE}#funding-deals"))

    ind = data("india-early-stage-q1-2026")
    months = ["2026-01", "2026-02", "2026-03"]
    groups = {"Pre-seed & seed": ("Pre-seed", "Seed"), "Series A": ("Pre-Series A", "Series A"), "Series B": ("Pre-Series B", "Series B")}
    grid = defaultdict(Counter)
    for i in ind["items"]:
        s = stage(i["round_type"])
        g = next((k for k, v in groups.items() if s in v), None)
        if g:
            grid[g][i["published_at"][:7]] += 1
    biggest = [i for i in sorted(dedupe(ind["items"]), key=lambda i: -(i["amount_usd"] or 0)) if i["amount_usd"]][:5]
    pair = twins(biggest)
    twin_note = f" {' / '.join(pair)}: one round recorded under two company names, not merged automatically." if pair else ""
    stories.append(story(
        "india-early-stage-q1-2026", ["india-early-stage-q1-2026"],
        nav="India early-stage · Q1 2026", client="Claude Code", heading="Size a startup market by stage",
        title="Size early-stage funding in one country",
        prompt="How many seed, Series A and Series B rounds were announced in India in Q1 2026, month by month? Show the largest rounds.",
        steps=[step("india-early-stage-q1-2026", "Funding deals filtered by country and round type"),
               local("Split by recorded stage", "The Seed filter also matches pre-seed labels; the client keeps them apart")],
        overview={"type": "columns", "stacked": True, "title": "Indian early-stage rounds by month, Q1 2026", "unit": "deal records", "height": 270,
                  "subtitle": f"{ind['totals']['deals']} deal records · stage from the recorded round label",
                  "labels": ["January", "February", "March"],
                  "series": [{"name": g, "values": [grid[g][m] for m in months]} for g in groups],
                  "stats": [{"value": str(ind["totals"]["deals"]), "label": "deal records"},
                            {"value": str(ind["totals"]["deals_with_amount"]), "label": "with a usable amount"},
                            {"value": usd(ind["totals"]["median_amount_usd"]), "label": "median usable amount"},
                            {"value": usd(ind["totals"]["sum_amount_usd"]), "label": "sum, repeats merged"}]},
        detail={"type": "table", "title": "The largest early-stage rounds", "subtitle": "Merged records · original currency kept beside the USD conversion",
                "headers": ["Company", "Round", "USD", "As reported", "Sector", "Published"], "widths": [24, 13, 11, 18, 22, 12],
                "rows": [[{"main": name(i["company_name"]), "sub": i["city"] or ""}, tag(i["round_type"]), {"num": usd(i["amount_usd"])},
                          f"{i['currency'] or ''} {i['amount']:,.0f}" if i["amount"] else {"missing": "not stated"},
                          trim(i["sector"] or "not stated", 30), day(i["published_at"])] for i in biggest],
                "note": "USD uses fixed conversion rates." + twin_note},
        footnote="Country comes from the deal record; it may describe the company's base rather than where the round closed.",
        takeaway="Count a market's rounds by stage and month, with original currencies intact.",
        evidence_summary="Saved funding deals, India, seed to Series B, all pages",
        guide=f"{GUIDE}#funding-deals"))

    hl = data("hiring-vs-layoffs-q1-2026")
    W2 = ("2026-01-01", "2026-03-31")
    weeks2, hires = weekly(hl["items"], *W2, pred=lambda i: i["event_type"] == "job_creation")
    _, cuts = weekly(hl["items"], *W2, pred=lambda i: i["event_type"] == "layoffs")
    top_h = Counter(i["domain"] for i in hl["items"] if i["event_type"] == "job_creation" and i["domain"]).most_common(6)
    top_l = Counter(i["domain"] for i in hl["items"] if i["event_type"] == "layoffs" and i["domain"]).most_common(6)
    stories.append(story(
        "hiring-vs-layoffs-q1-2026", ["hiring-vs-layoffs-q1-2026"],
        nav="Hiring vs layoffs · Q1 2026", client="Codex", heading="Compare two signals side by side",
        title="Compare hiring and layoff announcements",
        prompt="Compare job-creation and layoff announcements week by week in Q1 2026. Which companies appear most on each side?",
        steps=[step("hiring-vs-layoffs-q1-2026", "Job-creation and layoff events"),
               local("Count by week and company", "Client counts every returned event; all pages were read")],
        overview={"type": "columns", "title": "Job creation vs layoffs, weekly, Q1 2026", "unit": "events per week", "height": 270,
                  "subtitle": f"{hl['by_type']['job_creation']:,} job-creation and {hl['by_type']['layoffs']:,} layoff events · weeks start Monday",
                  "labels": [w.strftime("%-d %b") for w in weeks2],
                  "sublabels": ["partial" if partial(w, *W2) else "" for w in weeks2],
                  "series": [{"name": "Job creation", "tone": "positive", "values": hires},
                             {"name": "Layoffs", "tone": "negative", "values": cuts}],
                  "stats": [{"value": f"{hl['by_type']['job_creation']:,}", "label": "job-creation events"},
                            {"value": f"{hl['by_type']['layoffs']:,}", "label": "layoff events"},
                            {"value": str(sum(1 for a, b in zip(hires, cuts) if b > a)), "label": f"of {len(weeks2)} weeks with more layoffs"},
                            {"value": f"{len({i['domain'] for i in hl['items'] if i['domain']}):,}", "label": "company domains"}]},
        detail={"type": "table", "title": "Who appears most on each side", "subtitle": "Most frequent linked domains · check flagged links against their sentences",
                "headers": ["#", "Job creation", "Layoffs"], "widths": [6, 47, 47],
                "rows": [[str(k + 1), domain_cell(*top_h[k]), domain_cell(*top_l[k])] for k in range(5)],
                "note": "Company links are extracted from text; ⚠ marks captured mislinks, kept as returned."},
        footnote="Counts are extracted event sentences, not headcount. Many articles repeat one announcement.",
        takeaway="Put two business signals on one timeline and see which companies drive each.",
        evidence_summary="Saved job-creation and layoff events, Q1 2026, all pages",
        guide=f"{GUIDE}#company-events"))

    paragraphs = {
        "ai-funding-april-2026": "The funding listing filtered to the Artificial Intelligence sector and sorted by usable amount returns deal records with round labels, investors and the source sentence for each figure. The client merges records with the same company and amount, because one round is often extracted several times under different labels, and ranks the remainder. Totals come from the API and cover the whole window, including how many deals had no usable amount and how many amounts were withheld as implausible or unconverted. The detail view keeps the sentence beside each amount; the largest row, for example, counts a conditional $20B tranche.",
        "layoffs-april-2026": "All layoff events for April 2026 were read by following `next_cursor`, then bucketed by week on the client. Partial weeks at the month's edges are labelled. The detail view lists the newest extracted announcements with their linked company domains. An event is one extracted sentence, so repeated coverage of one layoff can appear more than once.",
        "openai-company-events": "One events request for a company domain returns a page of events plus `by_type` counts for the whole window. The donut uses those window-wide counts; the detail table shows the newest example of each event type from the first page, with the company's role in it.",
        "sequoia-portfolio": "The investor filter matches names in each deal's investor list. Both pages of results were read; the client merges records with the same company and amount and groups the rest by recorded round label. The detail table lists the largest merged rounds with the other investors named in each deal. Some rounds still appear more than once when they were reported on different days with different amounts.",
        "india-early-stage-q1-2026": "Funding deals filtered to India and to seed, Series A and Series B labels were read in full. The API's round filter is a label match, so `Seed` also returns pre-seed rounds; the client splits records by their recorded label and groups pre-rounds with the stage they precede. The detail table keeps the original currency and amount beside the fixed-rate USD conversion.",
        "hiring-vs-layoffs-q1-2026": "Job-creation and layoff events for Q1 2026 were read in full and counted by week and by company domain. The detail table shows the most frequent domains on each side and flags two captured mislinks: most metavision.com rows describe Meta and meetblock.com rows describe Block, but neither is that company's domain. Company links are extracted from text, so the demo keeps those rows visible and labelled instead of silently correcting them.",
    }
    site = {"brand": "Prism Business News",
            "description": f"{len(stories)} animated research UI concepts for the Prism Business News API: sector funding, layoff tracking, company event profiles, investor activity, country funding by stage and hiring vs layoffs.",
            "headline": "See what a connected<br>business-news assistant can build.",
            "intro": "Write a brief in Claude Code or Codex. The Prism Business News API supplies company events, funding deals and business news; your client turns them into a useful view.",
            "provenance": ("Every demo here is computed from saved responses of the real API, captured on the date in its badge. "
                           "Where the client merges repeated records or groups round labels, the story says so; flagged company links "
                           "are shown as returned."),
            "readme_blurb": "They cover AI funding rankings, a layoff tracker, a company's event profile, investor activity by stage, Indian early-stage funding and hiring versus layoffs, all from captured API responses."}
    write_outputs(stories, site, paragraphs)
    print(f"Built {len(stories)} captured stories; all requests validated; no live calls.")


if __name__ == "__main__":
    build()
