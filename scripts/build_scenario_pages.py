#!/usr/bin/env python3
"""Render the demonstration pages from saved captures.

Writes docs/scenarios/<segment>/<slug>.md for every kept scenario, one index per
segment, docs/scenarios/README.md, docs/research/KEYWORD_RESEARCH.md and the
demonstrations section at the top of README.md. Every number on a page comes from
a saved response in docs/examples/scenarios/.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scenario_common as sc  # noqa: E402
from scenario_common import bar, day, esc, month, n, pct, table, title_case, trim, usd  # noqa: E402

PRODUCT, CLI = "Prism Business News API", "prism-business-news"
SEGMENTS = {
    "funding-research": ("Startup funding research", "Size a sector, stage or region by measured deal counts and reported USD amounts over twelve months, then read the largest and latest rounds: VC analysts, corporate development, startup ecosystem teams and journalists."),
    "company-events": ("Company events research", "Count layoffs, acquisitions, IPOs, results, leadership changes, lawsuits and other company events month by month, with the evidence sentence and source for each: risk, sales intelligence, HR and markets teams."),
    "company-monitoring": ("Company monitoring research", "Follow one company: its latest headlines, the events attributed to its domain over twelve months, the tone of its coverage and any funding records: account managers, investor relations, competitive intelligence and analysts."),
    "investor-research": ("Investor research", "See which rounds an investor appears in, how many and how large, month by month, with the largest and latest deals: LPs, founders preparing outreach, VC analysts and deal reporters."),
}
EVENT_LABEL = {"earnings": "Earnings", "key_people": "Key people", "ma": "M&A", "company_announcement": "Announcement",
               "contracts": "Contracts", "funding_rounds": "Funding round", "asset_acquisition": "Asset acquisition",
               "lawsuit": "Lawsuit", "new_product": "New product", "regulatory": "Regulatory", "capital_infusion": "Capital infusion",
               "ipo": "IPO", "job_creation": "Job creation", "layoffs": "Layoffs", "board_updates": "Board", "funds_raising": "Fundraising",
               "buyback": "Buyback", "incorporation": "Incorporation", "fda_approval": "FDA approval"}
CUMULATIVE = re.compile(r"total funding|since (its )?(founding|inception)|to date|valuation|valued at|market cap", re.I)
MISLINKED = {"metavision.com": "Meta", "meetblock.com": "Block"}


def heading(s: dict) -> str:
    h = title_case(s["keyword"]["phrase"])
    return h


def company_key(name: str) -> str:
    """Loose company identity: the same round is often reported as 'X Lab', 'X Labs', 'X Machines Lab'."""
    words = re.findall(r"[a-z0-9]+", (name or "").lower())
    return words[0] if words and len(words[0]) > 3 else " ".join(words[:2])


def deal_rows(items: list[dict], with_investors: bool = True, one_per_company: bool = False) -> tuple[list[list], int]:
    seen, rows, flagged = set(), [], 0
    for d in items:
        key = (company_key(d.get("company_name")),) if one_per_company else ((d.get("company_name") or "").lower(), d.get("amount_usd"))
        if key in seen:
            continue
        seen.add(key)
        warn = ""
        if d.get("amount_flag"):
            warn = f" ⚠ {d['amount_flag'].replace('_', ' ')}"
        elif CUMULATIVE.search(d.get("source_sentence") or ""):
            warn = " ⚠ check sentence"
        flagged += bool(warn)
        names = [i.get("name") or i.get("domain") or "" for i in d.get("investors") or []]
        inv = ", ".join([x for x in names if x.strip().lower() not in ("", "na", "n/a", "none", "undisclosed")][:3]) or "—"
        row = [day(d.get("published_at")), esc(title_case(d.get("company_name") or "—")) + (f" ({esc(d['domain'])})" if d.get("domain") else ""),
               esc(d.get("round_type") or "—"), usd(d.get("amount_usd")) + warn]
        if with_investors:
            row.append(esc(trim(inv, 60)))
        row += [esc(d.get("country") or "—"), esc(trim(d.get("source_sentence"), 140))]
        rows.append(row)
    return rows, flagged


def event_rows(items: list[dict], show_company: bool = True) -> tuple[list[list], int]:
    rows, missing = [], 0
    seen = set()
    for e in items:
        key = (e.get("domain"), e.get("headline"))
        if key in seen:
            continue
        seen.add(key)
        if e.get("url"):
            src = f"[{esc(trim(e.get('title') or e.get('publisher'), 70))}]({e['url']}) · {esc(e.get('publisher'))}"
        else:
            src, missing = "article unavailable", missing + 1
        dom = e.get("domain") or "—"
        if dom in MISLINKED:
            dom += f" ⚠ check link: not {MISLINKED[dom]}'s domain"
        row = [day(e.get("published_at"))] + ([esc(dom)] if show_company else []) + \
              [EVENT_LABEL.get(e.get("event_type"), e.get("event_type")), esc(trim(e.get("headline"), 150)), src]
        rows.append(row)
    return rows[:12], missing


def headline_rows(items: list[dict]) -> list[list]:
    seen, rows = set(), []
    for it in items:
        k = it["headline"].lower().strip()
        if k in seen:
            continue
        seen.add(k)
        ev = ", ".join(sorted({EVENT_LABEL.get(e["event_type"], e["event_type"]) for e in it.get("events") or []})) or "—"
        rows.append([day(it["published_at"]), f"[{esc(trim(it['headline'], 110))}]({it['url']})", esc(it["publisher"]),
                     it.get("priority") or "—", (it.get("sentiment") or {}).get("group", "—"), ev])
    return rows[:12]


def tone_glance(sent: dict) -> list[list]:
    g = {x["group"]: x for x in sent.get("groups") or []}
    if not g:
        return []
    return [["Tone, Jan–Apr 2026 (negative · neutral · positive)",
             " · ".join(pct(g.get(k, {}).get("share")) for k in ("negative", "neutral", "positive"))
             + f" of {n(sent.get('matched'))} articles"]]


def monthly_events(tr: dict) -> list[str]:
    pts = tr.get("points") or []
    if not pts:
        return []
    types = sorted((tr.get("by_type") or {}), key=lambda t: -tr["by_type"][t])[:4]
    top = max(p["events"] for p in pts) or 1
    head = ["Month", "Events"] + ([EVENT_LABEL.get(t, t) for t in types] if len(types) > 1 else []) + [""]
    rows = []
    for p in pts:
        r = [month(p["period"]) + (" (partial)" if p.get("partial_period") else ""), n(p["events"])]
        if len(types) > 1:
            r += [n((p.get("by_type") or {}).get(t, 0)) for t in types]
        rows.append(r + [bar(p["events"], top)])
    return ["## Twelve months of events", "", "Distinct events per month (`POST /v1/business/event-trends`, `granularity=monthly`).", "",
            table(head, rows, "lr" + "r" * (len(head) - 3) + "l"), ""]


def monthly_funding(summ: dict) -> list[str]:
    pts = summ.get("points") or []
    if not pts:
        return []
    top = max(p["deals"] for p in pts) or 1
    rows = [[month(p["period"]) + (" (partial)" if p.get("partial_period") else ""), n(p["deals"]), n(p.get("deals_with_amount")),
             usd(p.get("sum_amount_usd")), usd(p.get("median_amount_usd")), bar(p["deals"], top)] for p in pts]
    return ["## Twelve months of deals", "", "Deal records per month (`POST /v1/business/funding/summary`, `granularity=monthly`).", "",
            table(["Month", "Deals", "With amount", "Reported total", "Median", ""], rows, "lrrrrl"), ""]


def funding_body(s: dict, rec: dict) -> tuple[list[list], list[str]]:
    summ, big, latest = (sc.response(rec, k) for k in ("summary", "largest", "latest"))
    t = summ.get("totals") or {}
    pts = summ.get("points") or []
    peak = max(pts, key=lambda p: p["deals"]) if pts else None
    glance = [["Deal records, May 2025 – Apr 2026", n(t.get("deals"))],
              ["With a usable reported amount", n(t.get("deals_with_amount"))],
              ["Reported total (usable amounts)", usd(t.get("sum_amount_usd"))],
              ["Median reported round", usd(t.get("median_amount_usd"))],
              ["Largest reported round", usd(t.get("largest_amount_usd"))]]
    if t.get("deals_amount_excluded"):
        glance.append(["Amounts left out as implausible or unconverted", n(t["deals_amount_excluded"])])
    if peak:
        glance.append(["Busiest month", f"{month(peak['period'])} ({n(peak['deals'])} deals)"])
    body = monthly_funding(summ)
    rows, f1 = deal_rows(big.get("items") or [], one_per_company=True)
    if rows:
        hidden = len(big.get("items") or []) - len(rows)
        body += ["## Largest reported rounds, May 2025 – Apr 2026", "",
                 "`sort=amount`, limit 40; the largest record per company is shown." +
                 (f" {hidden} further records repeat a company already listed, often the same round under a name variant or a valuation reported as an amount." if hidden else ""), "",
                 table(["Published", "Company", "Round", "Amount (USD)", "Investors", "Country", "Evidence sentence"], rows[:10], "lllrlll"), ""]
    rows2, f2 = deal_rows(latest.get("items") or [])
    if rows2:
        body += ["## Latest rounds, Jan – Apr 2026", "", "`sort=newest`, limit 10.", "",
                 table(["Published", "Company", "Round", "Amount (USD)", "Investors", "Country", "Evidence sentence"], rows2[:10], "lllrlll"), ""]
    if f1 or f2:
        body += ["⚠ marks an amount the API flagged, or an evidence sentence that may describe cumulative funding or a valuation rather than this round. Read the sentence before using the figure.", ""]
    return glance, body


def events_body(s: dict, rec: dict) -> tuple[list[list], list[str]]:
    tr, ev, sent = (sc.response(rec, k) for k in ("event_trends", "events", "sentiment"))
    t = tr.get("totals") or {}
    pts = tr.get("points") or []
    peak = max(pts, key=lambda p: p["events"]) if pts else None
    glance = [["Events, May 2025 – Apr 2026", n(t.get("events"))], ["Companies (with a domain)", n(t.get("companies"))],
              ["Source articles", n(t.get("articles"))]]
    if peak:
        glance.append(["Busiest month", f"{month(peak['period'])} ({n(peak['events'])} events)"])
    glance += tone_glance(sent)
    body = monthly_events(tr)
    rows, missing = event_rows(ev.get("items") or [])
    if rows:
        body += ["## Latest events, Jan – Apr 2026", "",
                 "`POST /v1/business/events` with `resolve=true`, newest first; repeated sentences shown once." +
                 (f" Source details were unavailable for {missing} of these events at capture time." if missing else ""), "",
                 table(["Published", "Company domain", "Type", "Evidence sentence", "Source"], rows, "lllll"), ""]
    return glance, body


def company_body(s: dict, rec: dict) -> tuple[list[list], list[str]]:
    cn, tr, sent, ev = (sc.response(rec, k) for k in ("company_news", "event_trends", "sentiment", "events"))
    t = tr.get("totals") or {}
    hl = cn.get("headlines") or {}
    fu = cn.get("funding") or {}
    glance = [["Company domain", f"`{s['domain']}`"], ["Headlines, Jan – Apr 2026 (estimate)", n(hl.get("total_estimate"))],
              ["Events, May 2025 – Apr 2026", n(t.get("events"))]]
    by = {k: v for k, v in (tr.get("by_type") or {}).items() if v}
    if by:
        top = sorted(by, key=lambda k: -by[k])[:3]
        glance.append(["Most frequent event types", ", ".join(f"{EVENT_LABEL.get(k, k)} ({n(by[k])})" for k in top)])
    glance += tone_glance(sent)
    glance.append(["Funding records, Jan – Apr 2026", n(fu.get("total_estimate") or 0)])
    body = []
    rows = headline_rows(hl.get("items") or [])
    if rows:
        unres = hl.get("unresolved") or 0
        body += ["## Latest headlines, Jan – Apr 2026", "",
                 "From `GET /v1/business/companies/{domain}/news`, newest first." +
                 (f" {unres} requested articles were temporarily unavailable at capture time." if unres else ""), "",
                 table(["Published", "Headline", "Publisher", "Priority", "Tone", "Events"], rows, "lllrll"), ""]
    if by:
        body += ["## Event mix, May 2025 – Apr 2026", "",
                 table(["Event type", "Events"], [[EVENT_LABEL.get(k, k), n(by[k])] for k in sorted(by, key=lambda k: -by[k]) if by[k]], "lr"), ""]
    body += monthly_events(tr)
    erows, missing = event_rows(ev.get("items") or [], show_company=False)
    if erows:
        body += ["## Latest events, Jan – Apr 2026", "", "`POST /v1/business/events` with `resolve=true`." +
                 (f" Source details were unavailable for {missing} of these events." if missing else ""), "",
                 table(["Published", "Type", "Evidence sentence", "Source"], erows, "llll"), ""]
    if fu.get("items"):
        frows, _ = deal_rows(fu["items"])
        body += ["## Funding records, Jan – Apr 2026", "",
                 table(["Published", "Company", "Round", "Amount (USD)", "Investors", "Country", "Evidence sentence"], frows, "lllrlll"), ""]
    return glance, body


def cli_lines(s: dict) -> list[str]:
    out = []
    for c in s["calls"]:
        cmd = {"/v1/business/funding/summary": "funding-summary", "/v1/business/funding": "funding",
               "/v1/business/event-trends": "event-trends", "/v1/business/events": "events",
               "/v1/business/sentiment": "sentiment"}.get(c["path"])
        if c["path"].startswith("/v1/business/companies/"):
            cmd = "company " + c["path"].split("/")[4]
        args = []
        for k, v in c["body"].items():
            vals = v if isinstance(v, list) else [v]
            for x in vals:
                x = str(x).lower() if isinstance(x, bool) else x
                args.append(f"--{k.replace('_', '-')} " + (f'"{x}"' if isinstance(x, str) and " " in x else str(x)))
        out.append(f"{CLI} {cmd} " + " ".join(args))
    return out


def run_it(s: dict) -> str:
    first = s["calls"][0]
    curl = (f"curl -sS --get \"$API_BASE{first['path']}\" -H \"X-API-Key: $PRISM_API_KEY\" " +
            " ".join(f"--data-urlencode '{k}={v}'" for k, v in first["body"].items())) if first["method"] == "GET" else \
        (f"curl -sS \"$API_BASE{first['path']}\" -H \"X-API-Key: $PRISM_API_KEY\" -H 'Content-Type: application/json' \\\n  -d '{json.dumps(first['body'])}'")
    second = s["calls"][1]
    return f"""## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved:

```bash
{chr(10).join(cli_lines(s))}
```

The first request with curl, and the second in Python:

```bash
{curl}
```

```python
import os, requests
r = requests.{second['method'].lower()}(os.environ["API_BASE"] + "{second['path']}", headers={{"X-API-Key": os.environ["PRISM_API_KEY"]}},
                  {'json' if second['method'] == 'POST' else 'params'}={json.dumps(second['body'])}, timeout=60)
print(r.json()["data"])
```
"""


QUESTION = {
    "funding-research": "How many {t} deals were reported over the twelve months to April 2026, how much money did they report, and which rounds were the largest and the latest?",
    "company-events": "How many {t} events were reported each month over the twelve months to April 2026, which companies were involved, and what do the latest evidence sentences say?",
    "company-monitoring": "What has the news reported about {t} in January–April 2026: latest headlines, events attributed to its domain over twelve months, tone and funding records?",
    "investor-research": "Which rounds did {t} appear in over the twelve months to April 2026, how many and how large were they, and which were the largest and latest?",
}
FILTER = {
    "funding-research": lambda s: s["filters"],
    "company-events": lambda s: "event types " + ", ".join(f"`{t}`" for t in s["event_types"]) + (f" and the word “{s['word']}” in the event sentence" if s.get("word") else ""),
    "company-monitoring": lambda s: f"company domain `{s['domain']}`",
    "investor-research": lambda s: f"investor “{s['investor']}”",
}


def page(s: dict, rec: dict, related: list[dict]) -> str:
    seg = s["segment"]
    body_fn = {"funding-research": funding_body, "investor-research": funding_body,
               "company-events": events_body, "company-monitoring": company_body}[seg]
    glance, body = body_fn(s, rec)
    subj = {"company-monitoring": title_case(s["topic"]), "investor-research": s.get("investor", s["topic"])}.get(seg, s["topic"])
    h1 = heading(s)
    out = [f"# {h1}: measured {'deals' if 'funding' in seg or 'investor' in seg else 'events and news'} with sources (to Apr 2026)", "",
           f"[{SEGMENTS[seg][0]}](README.md) · [All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)", "",
           f"> **Search demand:** {sc.search_line(s)}  ",
           f"> **Data:** {sc.coverage_line(rec)}. Saved API responses: [{s['slug']}.json](../../examples/scenarios/{s['slug']}.json).", "",
           f"**Question.** {QUESTION[seg].format(t=subj)}", "",
           f"**Filters.** {FILTER[seg](s)}.", "",
           "## At a glance", "", table(["Measure", "Value"], glance, "lr"), "", *body, run_it(s), "## Read the result carefully", ""]
    caveats = ["Windows: twelve months (1 May 2025 – 30 Apr 2026) for series and totals; 1 Jan – 30 Apr 2026 for the latest lists.",
               "Dates are source publication dates, not necessarily when a deal or event happened."]
    if rec.get("coverage_note"):
        caveats.append(f"Captured while part of the archive was offline ({rec['coverage_note']}). Every count is a lower bound.")
    if seg in ("funding-research", "investor-research"):
        caveats.append("Amounts are reported figures converted at fixed rates; one company and amount count once in totals, and flagged amounts (over $25B or unconverted) are left out.")
    if seg == "investor-research":
        caveats.append("Investor names match broadly (a name can match several firms or funds); use a domain for a narrower match.")
    caveats += [esc(x) for x in sc.notes(rec) if "unavailable" not in x.lower()]
    out += [f"- {c}" for c in dict.fromkeys(caveats)] + [""]
    out += ["## Related demonstrations", ""] + [f"- [{heading(r)}]({r['slug']}.md)" for r in related] + [""]
    return "\n".join(out)


def headline_number(s: dict, rec: dict) -> tuple[str, str]:
    if s["segment"] in ("funding-research", "investor-research"):
        t = sc.response(rec, "summary").get("totals") or {}
        return n(t.get("deals")), usd(t.get("sum_amount_usd"))
    t = sc.response(rec, "event_trends").get("totals") or {}
    return n(t.get("events")), n(t.get("companies"))


def segment_index(seg: dict, kept: list[dict], recs: dict) -> str:
    title, blurb = SEGMENTS[seg["id"]]
    money = seg["id"] in ("funding-research", "investor-research")
    rows = []
    for i, s in enumerate(kept, 1):
        a, b = headline_number(s, recs[s["slug"]])
        v = s["keyword"]["volume"]
        rows.append([i, f"[{heading(s)}]({s['slug']}.md)", n(v.get("in") or None), n(v.get("us") or None), a, b])
    head = ["#", "Demonstration", "India searches/mo", "US searches/mo"] + (["Deals, 12 months", "Reported total"] if money else ["Events, 12 months", "Companies"])
    return f"""# {title}: {len(kept)} worked demonstrations

[All demonstrations](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [User guide](../../USER_GUIDE.md)

{blurb}

Each page answers one researched search query with saved live API responses: twelve-month
totals and a monthly series, the detailed records behind them with evidence sentences and
sources, and the exact CLI, curl and Python requests. Pages are ordered by search demand.

{table(head, rows, "rlrrrr")}
"""


# ── hub, research and README: shared shape with the news repo ────────────────
def main() -> None:
    plan = json.loads(sc.PLAN.read_text())
    log = json.loads(sc.LOG.read_text())
    summary = []
    for seg in plan["segments"]:
        kept = [s for s in seg["scenarios"] if log.get(s["slug"], {}).get("kept")]
        recs = {s["slug"]: sc.load_capture(s["slug"]) for s in kept}
        d = sc.SCEN / seg["id"]
        d.mkdir(parents=True, exist_ok=True)
        for old in d.glob("*.md"):
            old.unlink()
        for i, s in enumerate(kept):
            related = [kept[j] for j in (i - 2, i - 1, i + 1, i + 2) if 0 <= j < len(kept)][:4]
            (d / f"{s['slug']}.md").write_text(page(s, recs[s["slug"]], related))
        (d / "README.md").write_text(segment_index(seg, kept, recs))
        summary.append((seg, kept, recs))
    write_hub(summary)
    write_research(plan, log)
    write_readme(summary)
    print({seg["id"]: len(kept) for seg, kept, _ in summary})


def write_hub(summary: list) -> None:
    total = sum(len(k) for _, k, _ in summary)
    rows = [[f"[{SEGMENTS[seg['id']][0]}]({seg['id']}/README.md)", len(kept),
             ", ".join(f"[{heading(s)}]({seg['id']}/{s['slug']}.md)" for s in kept[:3])] for seg, kept, _ in summary]
    when = min(r["captured_at"] for _, _, recs in summary for r in recs.values())
    (sc.SCEN / "README.md").write_text(f"""# {PRODUCT} demonstrations: {total} worked examples

[README](../../README.md) · [Keyword research](../research/KEYWORD_RESEARCH.md) · [User guide](../USER_GUIDE.md) · [Animated gallery](../ANIMATED_USE_CASES.md)

Each demonstration answers one real search query with saved responses from the live API:
twelve-month deal or event totals, a monthly series, the records behind them with evidence
sentences and sources, and the exact requests to reproduce it. Topics were chosen by
[keyword research](../research/KEYWORD_RESEARCH.md) (India and US monthly searches) and kept
only when the API returned populated results.

{table(["Segment", "Pages", "Highest-demand pages"], rows, "lrl")}

Captured {day(when)} from the live API. Part of the archive was offline (1 of 14 shards,
about 93% of rows available), so every count is a lower bound; some source articles were
temporarily unavailable and each page says how many.

Regenerate: `scripts/plan_scenarios.py` → `scripts/capture_scenarios.py` → `scripts/build_scenario_pages.py`.
""")


def write_research(plan: dict, log: dict) -> None:
    research = json.loads((sc.RESEARCH / plan["research"]).read_text())
    out = ["# Keyword research for the demonstration pages", "",
           f"[All demonstrations](../scenarios/README.md) · [Raw data]({plan['research']})", "",
           f"Research date **{research['date']}**. {research['volume']}", "", research["method"], "",
           "Status: **page** = built; **thin** = captured but below the populated threshold; **excluded** = overlap or ambiguous query (reason shown); **not reached** = the segment already had its pages.", ""]
    for seg in research["segments"]:
        rows = []
        for t in seg["topics"]:
            slug = sc.slugify(t["target"]["phrase"])
            entry = log.get(slug)
            if t.get("excluded"):
                status = f"excluded: {t['excluded']}"
            elif entry and entry.get("kept"):
                status = f"[page](../scenarios/{seg['id']}/{slug}.md)"
            elif entry and entry["why"] != "segment target reached":
                status = f"thin ({esc(entry['why'])})"
            else:
                status = "not reached"
            rows.append([esc(t["topic"]), *(f"{esc(p['phrase'])}: {n(p['volume']['in'])} / {n(p['volume']['us'])}" for p in t["phrases"]),
                         n(t["score"]), status])
        out += [f"## {SEGMENTS[seg['id']][0]}", "", f"Phrases: {' and '.join('`' + v + '`' for v in seg['variants'])}. Volumes are India / US monthly searches.", "",
                table(["Topic", "Phrase 1", "Phrase 2", "Score", "Status"], rows, "lllrl"), ""]
    (sc.RESEARCH / "KEYWORD_RESEARCH.md").write_text("\n".join(out))


def write_readme(summary: list) -> None:
    total = sum(len(k) for _, k, _ in summary)
    rows = [[f"**[{SEGMENTS[seg['id']][0]}](docs/scenarios/{seg['id']}/README.md)**", len(kept),
             " · ".join(f"[{title_case(s.get('investor') or s['topic'])}](docs/scenarios/{seg['id']}/{s['slug']}.md)" for s in kept[:4])]
            for seg, kept, _ in summary]
    section = f"""{sc.README_START}
## {total} worked demonstrations

Real questions, real responses: each page answers one researched search query with
saved live API output: twelve-month deal or event totals, a monthly series, the records
behind them with evidence sentences and sources, plus the exact CLI, curl and Python calls.
[Browse all {total}](docs/scenarios/README.md) or start with a segment:

{table(["Segment", "Pages", "Start with"], rows, "lrl")}

Topics come from [keyword research](docs/research/KEYWORD_RESEARCH.md) (India and US monthly searches).
Captured with 1 of 14 archive shards offline, so counts are lower bounds.
{sc.README_END}"""
    readme = sc.ROOT / "README.md"
    readme.write_text(sc.replace_section(readme.read_text(), section, sc.README_START, sc.README_END,
                                         "## Get access and make a first request"))


if __name__ == "__main__":
    main()
