#!/usr/bin/env python3
"""Turn the keyword research into docs/scenarios/plan.json: per segment, candidate
scenarios in search-demand order, each with the exact (validated) API calls behind
its page. capture_scenarios.py then keeps the first `target` populated ones."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import scenario_common as sc  # noqa: E402
from prism_business_api.filters import BusinessFilters  # noqa: E402

RESEARCH_FILE = sc.RESEARCH / "keyword-research-2026-10-16.json"
TARGET = 50
WINDOW = {"since": "2026-01-01", "until": "2026-04-30"}
YEAR = {"since": "2025-05-01", "until": "2026-04-30"}

# Funding: how each researched topic maps onto the funding filters.
SECTOR = {"ai startup": "ai", "ev startup": "electric vehicle", "logistics startup": "logistics",
          "semiconductor startup": "semiconductor", "quantum startup": "quantum", "drone startup": "drone",
          "battery startup": "battery", "solar startup": "solar", "mental health startup": "mental health",
          "pet care startup": "pet", "travel startup": "travel", "media startup": "media",
          "manufacturing startup": "manufacturing", "waste management startup": "waste management",
          "payments startup": "payments", "lending startup": "lending", "climate tech": "climate",
          "deep tech": "deep tech", "space tech": "space", "defence tech": "defense", "construction tech": "construction",
          "b2b marketplace": "marketplace", "creator economy": "creator", "water tech": "water"}
ROUND = {"seed": "seed", "pre-seed": "pre seed", "series a": "series a", "series b": "series b",
         "series c": "series c", "series d": "series d", "growth stage": "growth", "venture debt": "venture debt",
         "bridge round": "bridge"}
COUNTRY = {"india": "India", "usa": "United States", "germany": "Germany", "france": "France",
           "singapore": "Singapore", "israel": "Israel", "uae": "United Arab Emirates", "saudi arabia": "Saudi Arabia",
           "indonesia": "Indonesia", "japan": "Japan", "canada": "Canada", "australia": "Australia",
           "brazil": "Brazil", "nigeria": "Nigeria", "kenya": "Kenya", "china": "China", "korea": "South Korea",
           "london": None}
CITY = {"bangalore": "Bengaluru", "mumbai": "Mumbai", "delhi": "Delhi", "san francisco": "San Francisco",
        "new york": "New York", "london": "London", "africa": "Africa"}

# Company events: topic -> (event types, headline word filter or None).
EVENTS = {
    "tech layoffs": (["layoffs"], "tech"), "startup layoffs": (["layoffs"], "startup"), "bank layoffs": (["layoffs"], "bank"),
    "layoffs": (["layoffs"], None), "fintech layoffs": (["layoffs"], "fintech"), "pharma layoffs": (["layoffs"], "pharma"),
    "auto industry layoffs": (["layoffs"], "auto"), "retail layoffs": (["layoffs"], "retail"), "media layoffs": (["layoffs"], "media"),
    "gaming layoffs": (["layoffs"], "gaming"), "ai layoffs": (["layoffs"], "AI"), "it layoffs": (["layoffs"], "IT"),
    "job cuts": (["layoffs"], "job cuts"), "hiring freeze": (["layoffs"], "hiring freeze"),
    "mergers and acquisitions": (["ma"], None), "tech acquisitions": (["ma"], "tech"), "pharma acquisitions": (["ma"], "pharma"),
    "bank mergers": (["ma"], "bank"), "telecom mergers": (["ma"], "telecom"), "media mergers": (["ma"], "media"),
    "ipo": (["ipo"], None), "tech ipo": (["ipo"], "tech"), "ipo india": (["ipo"], "India"), "upcoming ipo": (["ipo"], "upcoming"),
    "sme ipo": (["ipo"], "SME"), "earnings": (["earnings"], None), "quarterly results": (["earnings"], "quarter"),
    "q4 results": (["earnings"], "Q4"), "bank results": (["earnings"], "bank"), "it company results": (["earnings"], "IT"),
    "ceo resigns": (["key_people"], "resign"), "ceo appointment": (["key_people"], "CEO"), "cfo appointment": (["key_people"], "CFO"),
    "board changes": (["board_updates"], None), "new product launch": (["new_product"], None),
    "product recall": (["company_announcement", "regulatory"], "recall"), "fda approval": (["fda_approval"], None),
    "drug approval": (["fda_approval", "regulatory"], "approval"), "lawsuit": (["lawsuit"], None),
    "class action lawsuit": (["lawsuit"], "class action"), "patent lawsuit": (["lawsuit"], "patent"),
    "antitrust lawsuit": (["lawsuit", "regulatory"], "antitrust"), "regulatory fine": (["regulatory"], "fine"),
    "sebi order": (["regulatory"], "SEBI"), "government contract": (["contracts"], "government"),
    "defence contract": (["contracts"], "defence"), "order win": (["contracts"], "order"), "share buyback": (["buyback"], None),
    "dividend announcement": (["company_announcement"], "dividend"), "stock split": (["company_announcement"], "split"),
    "bonus issue": (["company_announcement"], "bonus"), "rights issue": (["funds_raising", "capital_infusion"], "rights issue"),
    "qip": (["funds_raising"], "QIP"), "fundraise": (["funds_raising"], None), "debt raise": (["funds_raising"], "debt"),
    "bond issue": (["funds_raising"], "bond"), "plant expansion": (["company_announcement", "asset_acquisition"], "plant"),
    "new factory": (["company_announcement", "asset_acquisition"], "factory"), "hiring": (["job_creation"], None),
    "joint venture": (["company_announcement", "contracts"], "joint venture"),
    "strategic partnership": (["company_announcement", "contracts"], "partnership"), "stake sale": (["ma"], "stake"),
    "delisting": (["regulatory", "company_announcement"], "delist"), "bankruptcy": (["company_announcement", "lawsuit"], "bankruptcy"),
    "insolvency": (["company_announcement", "lawsuit"], "insolvency"), "restructuring": (["company_announcement"], "restructuring"),
    "spin-off": (["company_announcement", "ma"], "spin"), "demerger": (["company_announcement", "ma"], "demerger"),
    "asset sale": (["asset_acquisition", "ma"], "sale"), "capital infusion": (["capital_infusion"], None),
    "incorporation": (["incorporation"], None), "new subsidiary": (["incorporation"], "subsidiary"),
    "ai partnership": (["company_announcement", "contracts"], "AI"), "data center investment": (["asset_acquisition", "company_announcement"], "data center"),
    "semiconductor plant": (["asset_acquisition", "company_announcement"], "semiconductor"),
    "ev plant": (["asset_acquisition", "company_announcement"], "EV"), "battery plant": (["asset_acquisition", "company_announcement"], "battery"),
}

# Company monitoring: topic -> company domain (the events listing and briefing require a domain).
DOMAIN = {
    "tesla": "tesla.com", "nvidia": "nvidia.com", "apple": "apple.com", "microsoft": "microsoft.com", "google": "google.com",
    "amazon": "amazon.com", "meta": "meta.com", "openai": "openai.com", "netflix": "netflix.com", "intel": "intel.com",
    "amd": "amd.com", "samsung": "samsung.com", "tsmc": "tsmc.com", "alibaba": "alibaba.com", "tencent": "tencent.com",
    "byd": "byd.com", "toyota": "toyota.com", "ford": "ford.com", "general motors": "gm.com", "boeing": "boeing.com",
    "airbus": "airbus.com", "walmart": "walmart.com", "disney": "disney.com", "uber": "uber.com", "airbnb": "airbnb.com",
    "spotify": "spotify.com", "paypal": "paypal.com", "visa": "visa.com", "mastercard": "mastercard.com",
    "jpmorgan": "jpmorganchase.com", "goldman sachs": "goldmansachs.com", "morgan stanley": "morganstanley.com",
    "blackrock": "blackrock.com", "berkshire hathaway": "berkshirehathaway.com", "pfizer": "pfizer.com",
    "moderna": "modernatx.com", "novo nordisk": "novonordisk.com", "eli lilly": "lilly.com",
    "johnson and johnson": "jnj.com", "astrazeneca": "astrazeneca.com", "reliance industries": "ril.com",
    "tata motors": "tatamotors.com", "tata steel": "tatasteel.com", "tcs": "tcs.com", "infosys": "infosys.com",
    "wipro": "wipro.com", "hcl technologies": "hcltech.com", "hdfc bank": "hdfcbank.com", "icici bank": "icicibank.com",
    "sbi": "sbi.co.in", "adani": "adani.com", "adani enterprises": "adanienterprises.com", "larsen and toubro": "larsentoubro.com",
    "mahindra": "mahindra.com", "maruti suzuki": "marutisuzuki.com", "bajaj finance": "bajajfinserv.in",
    "zomato": "zomato.com", "swiggy": "swiggy.com", "paytm": "paytm.com", "ola electric": "olaelectric.com",
    "byju's": "byjus.com", "flipkart": "flipkart.com", "nykaa": "nykaa.com", "airtel": "airtel.in", "jio": "jio.com",
    "vodafone idea": "myvi.in", "ongc": "ongcindia.com", "coal india": "coalindia.in", "itc": "itcportal.com",
    "hindustan unilever": "hul.co.in", "asian paints": "asianpaints.com", "sun pharma": "sunpharma.com",
    "dr reddy's": "drreddys.com", "cipla": "cipla.com", "anthropic": "anthropic.com", "xai": "x.ai",
    "perplexity": "perplexity.ai", "databricks": "databricks.com", "stripe": "stripe.com", "shein": "shein.com",
    "bytedance": "bytedance.com", "xiaomi": "mi.com", "huawei": "huawei.com", "sony": "sony.com",
    "nintendo": "nintendo.com", "ibm": "ibm.com", "oracle": "oracle.com", "salesforce": "salesforce.com",
    "adobe": "adobe.com", "cisco": "cisco.com", "qualcomm": "qualcomm.com", "broadcom": "broadcom.com", "arm": "arm.com",
    "palantir": "palantir.com", "snowflake": "snowflake.com", "coinbase": "coinbase.com", "binance": "binance.com",
    "shopify": "shopify.com", "rivian": "rivian.com", "lucid": "lucidmotors.com",
}

INVESTOR = {"a16z": "Andreessen Horowitz", "gv": "GV", "nea": "New Enterprise Associates", "peak xv": "Peak XV",
            "google ventures": "GV", "tencent investments": "Tencent", "alibaba investments": "Alibaba",
            "nvidia investments": "Nvidia", "partech africa": "Partech", "dcvc": "DCVC", "kkr": "KKR", "tpg": "TPG",
            "gic": "GIC", "stv": "STV", "8vc": "8VC", "500 global": "500 Global", "hongshan": "HongShan",
            "sv angel": "SV Angel", "eqt ventures": "EQT Ventures", "iconiq": "ICONIQ", "ggv capital": "GGV Capital",
            "qed investors": "QED Investors"}


def funding_filters(topic: str) -> tuple[dict, str]:
    """Funding filters for one researched topic and a short description of them."""
    if topic in ROUND:
        return {"round_type": ROUND[topic]}, f"round type “{ROUND[topic]}”"
    if topic == "unicorn":
        return {"q": "unicorn"}, "deal sentences mentioning “unicorn”"
    if topic.startswith("startup funding "):
        place = topic.removeprefix("startup funding ")
        if COUNTRY.get(place):
            return {"country": COUNTRY[place]}, f"deal country {COUNTRY[place]}"
        return {"q": CITY[place]}, f"deal sentences mentioning {CITY[place]}"
    sector = SECTOR.get(topic, topic)
    return {"sector": sector}, f"sector “{sector}”"


def funding_calls(filters: dict) -> list[dict]:
    return [
        {"name": "summary", "method": "POST", "path": "/v1/business/funding/summary",
         "body": {**filters, **YEAR, "granularity": "monthly"}},
        {"name": "largest", "method": "POST", "path": "/v1/business/funding",
         "body": {**filters, **YEAR, "sort": "amount", "limit": 40}},
        {"name": "latest", "method": "POST", "path": "/v1/business/funding",
         "body": {**filters, **WINDOW, "sort": "newest", "limit": 10}},
    ]


def event_calls(types: list[str], q: str | None) -> list[dict]:
    base = {"event_type": types, **({"q": q} if q else {})}
    return [
        {"name": "event_trends", "method": "POST", "path": "/v1/business/event-trends",
         "body": {**base, **YEAR, "granularity": "monthly"}},
        {"name": "events", "method": "POST", "path": "/v1/business/events",
         "body": {**base, **WINDOW, "sort": "newest", "limit": 15, "resolve": True}},
        {"name": "sentiment", "method": "POST", "path": "/v1/business/sentiment",
         "body": {**base, **WINDOW, "granularity": "monthly"}},
    ]


def company_calls(domain: str) -> list[dict]:
    return [
        {"name": "company_news", "method": "GET", "path": f"/v1/business/companies/{domain}/news",
         "body": {**WINDOW, "limit": 12}},
        {"name": "event_trends", "method": "POST", "path": "/v1/business/event-trends",
         "body": {"company": domain, **YEAR, "granularity": "monthly"}},
        {"name": "sentiment", "method": "POST", "path": "/v1/business/sentiment",
         "body": {"company": domain, **WINDOW, "granularity": "monthly"}},
        {"name": "events", "method": "POST", "path": "/v1/business/events",
         "body": {"company": domain, **WINDOW, "sort": "newest", "limit": 12, "resolve": True}},
    ]


def investor_calls(name: str) -> list[dict]:
    return funding_calls({"investor": name})


def validate(c: dict) -> None:
    body = {k: v for k, v in c["body"].items() if k not in ("granularity", "resolve")}
    BusinessFilters.model_validate({k: (",".join(v) if isinstance(v, list) else v) for k, v in body.items()})


def recipe(seg: str, topic: str) -> tuple[list[dict], dict, dict]:
    """(calls, primary check, page facts) for one topic of one segment."""
    if seg == "funding-research":
        filters, desc = funding_filters(topic)
        return funding_calls(filters), {"call": "summary", "field": "totals.deals", "min": 8}, {"filters": desc}
    if seg == "company-events":
        types, q = EVENTS[topic]
        return event_calls(types, q), {"call": "event_trends", "field": "totals.events", "min": 8}, \
            {"event_types": types, "word": q}
    if seg == "company-monitoring":
        domain = DOMAIN[topic]
        return company_calls(domain), {"call": "event_trends", "field": "totals.events", "min": 5}, {"domain": domain}
    name = INVESTOR.get(topic, sc.title_case(topic))
    return investor_calls(name), {"call": "summary", "field": "totals.deals", "min": 5}, {"investor": name}


def main() -> None:
    research = json.loads(RESEARCH_FILE.read_text())
    segments = []
    for seg in research["segments"]:
        scen = []
        for t in seg["topics"]:
            if t.get("excluded"):
                continue
            calls, primary, facts = recipe(seg["id"], t["topic"])
            for c in calls:
                validate(c)
            scen.append({"slug": sc.slugify(t["target"]["phrase"]), "segment": seg["id"], "topic": t["topic"],
                         "keyword": t["target"], "score": t["score"], "calls": calls, "primary": primary, **facts})
        segments.append({"id": seg["id"], "title": seg["title"], "target": TARGET, "scenarios": scen})
    sc.SCEN.mkdir(parents=True, exist_ok=True)
    sc.PLAN.write_text(json.dumps({"window": WINDOW, "year": YEAR, "research": RESEARCH_FILE.name,
                                   "segments": segments}, indent=1, ensure_ascii=False) + "\n")
    print({s["id"]: len(s["scenarios"]) for s in segments})


if __name__ == "__main__":
    main()
