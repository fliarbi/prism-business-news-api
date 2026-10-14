window.PRISM_DEMOS = [
  {
    "duration": 32,
    "width": 1280,
    "height": 800,
    "disclosure": "Concept UI, not a recording of Claude Code or Codex. Request activity is animated; no live requests run.",
    "id": "ai-funding-april-2026",
    "brand": "Prism Business News",
    "kind": "captured",
    "badge": "Captured data · 14 Oct 2026",
    "sources": [
      {
        "file": "../examples/demo/ai-funding-april-2026.json",
        "sha256": "9c462457f94abc9d07beb100c39fc62751f9313c0b2855ab85507a6cca5130b1",
        "kind": "captured"
      }
    ],
    "nav": "AI funding · April 2026",
    "client": "Claude Code",
    "heading": "Follow the money in a sector",
    "title": "Rank the largest AI funding rounds in a month",
    "prompt": "Which AI companies raised the largest rounds in April 2026? Rank them, keep the source sentence for each amount, and tell me how many deals had no usable amount.",
    "steps": [
      {
        "type": "api",
        "method": "POST",
        "path": "/v1/business/funding",
        "body": {
          "sector": [
            "Artificial Intelligence"
          ],
          "since": "2026-04-01",
          "until": "2026-04-30",
          "sort": "amount",
          "limit": 40
        },
        "label": "Funding deals, largest usable amount first"
      },
      {
        "type": "client",
        "label": "Merge repeated records",
        "detail": "40 listing rows → 37 after merging the same company and amount"
      }
    ],
    "overview": {
      "type": "bars",
      "title": "The largest AI rounds of April 2026",
      "prefix": "$",
      "labelWidth": 430,
      "subtitle": "88 AI deal records · amounts as reported, converted to USD",
      "axisLabel": "Usable reported amount (USD)",
      "rows": [
        {
          "label": "Anthropic",
          "sub": "anthropic.com · investment · 21 Apr",
          "value": 25000000000.0,
          "display": "$25B"
        },
        {
          "label": "Coreweave",
          "sub": "coreweave.com · round not stated · 9 Apr",
          "value": 21000000000.0,
          "display": "$21B"
        },
        {
          "label": "Anthropic",
          "sub": "anthropic.com · Series H · 27 Apr",
          "value": 10000000000.0,
          "display": "$10B"
        },
        {
          "label": "Protect Prometheus",
          "sub": "no domain · round not stated · 24 Apr",
          "value": 10000000000.0,
          "display": "$10B"
        },
        {
          "label": "Project Prometheus",
          "sub": "projectprometheus.org · Funding round · 21 Apr",
          "value": 10000000000.0,
          "display": "$10B"
        },
        {
          "label": "Anthropic",
          "sub": "anthropic.com · Series G · 27 Apr",
          "value": 5000000000.0,
          "display": "$5B"
        }
      ],
      "stats": [
        {
          "value": "88",
          "label": "deal records in the window"
        },
        {
          "value": "70",
          "label": "with a usable amount"
        },
        {
          "value": "8",
          "label": "amounts withheld (implausible or unconverted)"
        },
        {
          "value": "$28M",
          "label": "median usable amount"
        }
      ]
    },
    "detail": {
      "type": "table",
      "title": "Each amount, with the sentence it came from",
      "subtitle": "Top rounds after merging repeated records · read the sentence before quoting a figure",
      "headers": [
        "Company",
        "Round",
        "Amount",
        "Source sentence"
      ],
      "widths": [
        19,
        14,
        11,
        56
      ],
      "rows": [
        [
          {
            "main": "Anthropic",
            "sub": "anthropic.com · 21 Apr"
          },
          {
            "tag": "investment"
          },
          {
            "num": "$25B"
          },
          {
            "sub": "Amazon is investing $5 billion into Anthropic immediately, with the potential to invest up to $20 billion more tied to commercial milestones,…"
          }
        ],
        [
          {
            "main": "Coreweave",
            "sub": "coreweave.com · 9 Apr"
          },
          {
            "tag": "not stated"
          },
          {
            "num": "$21B"
          },
          {
            "sub": "Meta doubles its firm commitment to artificial intelligence (AI) and commits to spending an additional $21 billion on cloud infrastructure for AI…"
          }
        ],
        [
          {
            "main": "Anthropic",
            "sub": "anthropic.com · 27 Apr"
          },
          {
            "tag": "Series H"
          },
          {
            "num": "$10B"
          },
          {
            "sub": "Google is investing $10 billion in Anthropic now, with another $30 billion potentially to follow if Anthropic hits certain performance targets, at a…"
          }
        ],
        [
          {
            "main": "Protect Prometheus",
            "sub": "no domain · 24 Apr"
          },
          {
            "tag": "not stated"
          },
          {
            "num": "$10B"
          },
          {
            "sub": "Protect Prometheus, AI lab co-led by Jeff Bezos, has reportedly raised $10 billion in fresh funding."
          }
        ],
        [
          {
            "main": "Project Prometheus",
            "sub": "projectprometheus.org · 21 Apr"
          },
          {
            "tag": "Funding round"
          },
          {
            "num": "$10B"
          },
          {
            "sub": "Jeff Bezos is close to finalizing a $10 billion funding round for his AI startup that’s developing models with the capability of understanding the…"
          }
        ]
      ],
      "note": "Reported amounts can include conditional tranches: the $25B Anthropic row counts $20B tied to milestones in its source sentence."
    },
    "footnote": "Amounts are extracted from news and converted at fixed rates; they are not verified deal values.",
    "takeaway": "Rank a sector's rounds and keep the sentence behind every number.",
    "evidence_summary": "Saved funding listing, AI sector, April 2026",
    "guide": "../USER_GUIDE.md#funding-deals"
  },
  {
    "duration": 32,
    "width": 1280,
    "height": 800,
    "disclosure": "Concept UI, not a recording of Claude Code or Codex. Request activity is animated; no live requests run.",
    "id": "layoffs-april-2026",
    "brand": "Prism Business News",
    "kind": "captured",
    "badge": "Captured data · 14 Oct 2026",
    "sources": [
      {
        "file": "../examples/demo/layoffs-april-2026.json",
        "sha256": "df1285dc0558706fe5ab1b0813b99aefb3183209b5f359c00ac0364b3c2351b8",
        "kind": "captured"
      }
    ],
    "nav": "Layoff tracker · April 2026",
    "client": "Codex",
    "heading": "Track a business signal week by week",
    "title": "Track a layoff wave across companies",
    "prompt": "Track layoff announcements through April 2026 week by week. How many companies were involved, and what are the latest announcements?",
    "steps": [
      {
        "type": "api",
        "method": "POST",
        "path": "/v1/business/events",
        "body": {
          "event_type": [
            "layoffs"
          ],
          "since": "2026-04-01",
          "until": "2026-04-30",
          "limit": 100
        },
        "label": "Layoff events in the window · followed next_cursor for 5 pages"
      },
      {
        "type": "client",
        "label": "Bucket by week",
        "detail": "Client counts every returned event; all pages were read"
      }
    ],
    "overview": {
      "type": "columns",
      "title": "Layoff events per week, April 2026",
      "unit": "events per week",
      "height": 270,
      "subtitle": "419 events from extracted announcements · weeks start Monday",
      "labels": [
        "30 Mar",
        "6 Apr",
        "13 Apr",
        "20 Apr",
        "27 Apr"
      ],
      "sublabels": [
        "partial week",
        "",
        "",
        "",
        "partial week"
      ],
      "series": [
        {
          "name": "Layoff events",
          "tone": "negative",
          "values": [
            43,
            98,
            113,
            100,
            65
          ]
        }
      ],
      "stats": [
        {
          "value": "419",
          "label": "layoff events"
        },
        {
          "value": "274",
          "label": "linked company domains"
        },
        {
          "value": "27",
          "label": "companies with 3+ events"
        },
        {
          "value": "13 Apr",
          "label": "busiest week"
        }
      ]
    },
    "detail": {
      "type": "table",
      "title": "The latest announcements",
      "subtitle": "Newest first · the extracted sentence and the linked company",
      "headers": [
        "Company",
        "Announcement",
        "Published"
      ],
      "widths": [
        22,
        64,
        14
      ],
      "rows": [
        [
          {
            "main": "saks.global",
            "sub": ""
          },
          {
            "sub": "Saks Global is slashing the headcount at its corporate headquarters by 16 percent, impacting a wide spectrum of positions."
          },
          "30 Apr"
        ],
        [
          {
            "main": "bbva.es",
            "sub": ""
          },
          {
            "sub": "BBVA CEO Onur Gen , has clarified that the voluntary departure of approximately 750 employees of the group in the first quarter of 2026 is not linked to the…"
          },
          "30 Apr"
        ],
        [
          {
            "main": "wrenkitchens.com",
            "sub": ""
          },
          {
            "sub": "The company says the move, which has resulted in job losses and store closures, will enable it to channel investment into its UK business, which continues to…"
          },
          "30 Apr"
        ],
        [
          {
            "main": "somfysystems.com",
            "sub": ""
          },
          {
            "sub": "the job safeguard plan (PES) announced in February, which provides for up to 534 job deletions in France, or 20%."
          },
          "30 Apr"
        ],
        [
          {
            "main": "quixote.com",
            "sub": ""
          },
          {
            "sub": "About 70 jobs will be cut across Atlanta and Los Angeles."
          },
          "30 Apr"
        ],
        [
          {
            "main": "metavision.com ⚠",
            "sub": "check link: not Meta's domain"
          },
          {
            "sub": "Sama said would result in 1,108 workers being made redundant."
          },
          "30 Apr"
        ]
      ],
      "note": "An event is one extracted sentence; one article can describe several layoffs, and one layoff can appear in several articles."
    },
    "footnote": "Event dates are article publication dates, not when the layoffs take effect.",
    "takeaway": "Watch a signal build week by week, then read the announcements behind it.",
    "evidence_summary": "Saved layoff events, April 2026, all pages",
    "guide": "../USER_GUIDE.md#company-events"
  },
  {
    "duration": 32,
    "width": 1280,
    "height": 800,
    "disclosure": "Concept UI, not a recording of Claude Code or Codex. Request activity is animated; no live requests run.",
    "id": "openai-company-events",
    "brand": "Prism Business News",
    "kind": "captured",
    "badge": "Captured data · 14 Oct 2026",
    "sources": [
      {
        "file": "../examples/demo/openai-events.json",
        "sha256": "9241d7adb99e6f1750b17954066296fd0bdf8d5736e37e154a6c4323fd454b3d",
        "kind": "captured"
      }
    ],
    "nav": "Company event mix",
    "client": "Claude Code",
    "heading": "Brief yourself on one company",
    "title": "See everything recorded about one company",
    "prompt": "Brief me on OpenAI from November 2025 to April 2026: what kinds of events were reported, and show one recent example of each.",
    "steps": [
      {
        "type": "api",
        "method": "POST",
        "path": "/v1/business/events",
        "body": {
          "company": "openai.com",
          "since": "2025-11-01",
          "until": "2026-04-30",
          "limit": 100
        },
        "label": "Events for one company domain"
      },
      {
        "type": "client",
        "label": "Pick one example per type",
        "detail": "Newest event of each type from the first page"
      }
    ],
    "overview": {
      "type": "donut",
      "title": "OpenAI's recorded events by type",
      "subtitle": "Nov 2025 – Apr 2026 · counts cover the whole window, not just one page",
      "segments": [
        {
          "label": "Key people",
          "value": 105
        },
        {
          "label": "Funding rounds",
          "value": 74
        },
        {
          "label": "Contracts",
          "value": 72
        },
        {
          "label": "M&A",
          "value": 36
        },
        {
          "label": "Announcements",
          "value": 33
        },
        {
          "label": "Lawsuits",
          "value": 27
        },
        {
          "label": "Other types",
          "value": 67,
          "color": "#a3afc0"
        }
      ],
      "centerValue": "414",
      "centerLabel": "events",
      "side": "One article can carry several events; counts are distinct article, type, role and date."
    },
    "detail": {
      "type": "table",
      "title": "One recent example of each event type",
      "subtitle": "Newest first · extracted sentence, role and publication date",
      "headers": [
        "Type",
        "Extracted sentence",
        "Role",
        "Published"
      ],
      "widths": [
        17,
        59,
        11,
        13
      ],
      "rows": [
        [
          {
            "tag": "Lawsuits"
          },
          {
            "sub": "The lawsuit asks the court to award about $130 billion in damages and restore OpenAI to nonprofit status."
          },
          "defendant",
          "29 Apr"
        ],
        [
          {
            "tag": "Contracts"
          },
          {
            "sub": "Under a deal earlier this year, Amazon invested $50 billion (£37bn) in OpenAI"
          },
          "client",
          "29 Apr"
        ],
        [
          {
            "tag": "Key people"
          },
          {
            "sub": "New Delhi: OpenAI has strengthened its international leadership team with the appointment of Emmanuel Marill as its first Managing Director for the…"
          },
          "primary",
          "28 Apr"
        ],
        [
          {
            "tag": "Asset acquisition"
          },
          {
            "sub": "Robinhood Ventures Fund I said it bought about $75 million of OpenAI common stock on April 17."
          },
          "seller",
          "23 Apr"
        ],
        [
          {
            "tag": "New products"
          },
          {
            "sub": "OpenAI releases new image generation model with complex capabilities ChatGPT Images 2.0 marks a big leap forward in image generation as OpenAI seeks…"
          },
          "primary",
          "22 Apr"
        ],
        [
          {
            "tag": "Funding rounds"
          },
          {
            "sub": "Key Highlights Robinhood invested about $75 million in OpenAI, giving it a small stake in the company."
          },
          "primary",
          "22 Apr"
        ]
      ],
      "note": "Role says how the company appears in the event (primary, acquirer, target, client…)."
    },
    "footnote": "Events are extracted from news sentences and linked to a company domain; check the sentence before relying on it.",
    "takeaway": "Get a company's whole event profile in one call, then drill into examples.",
    "evidence_summary": "Saved company events for openai.com",
    "guide": "../USER_GUIDE.md#one-company"
  },
  {
    "duration": 32,
    "width": 1280,
    "height": 800,
    "disclosure": "Concept UI, not a recording of Claude Code or Codex. Request activity is animated; no live requests run.",
    "id": "sequoia-portfolio",
    "brand": "Prism Business News",
    "kind": "captured",
    "badge": "Captured data · 14 Oct 2026",
    "sources": [
      {
        "file": "../examples/demo/sequoia-portfolio.json",
        "sha256": "8eb47623f4c1e8c1f9184cc1c7b9b4a23d9b77fa9c10812c0b7a3d1ef49aaf9b",
        "kind": "captured"
      }
    ],
    "nav": "Investor activity",
    "client": "Codex",
    "heading": "Profile an investor's recent deals",
    "title": "Profile an investor's recent deals by stage",
    "prompt": "Which rounds did Sequoia join between November 2025 and April 2026? Break them down by stage and list the largest with co-investors.",
    "steps": [
      {
        "type": "api",
        "method": "POST",
        "path": "/v1/business/funding",
        "body": {
          "investor": "Sequoia",
          "since": "2025-11-01",
          "until": "2026-04-30",
          "limit": 100
        },
        "label": "Deals naming the investor · followed next_cursor for 2 pages"
      },
      {
        "type": "client",
        "label": "Merge and group",
        "detail": "198 records → 119 after merging the same company and amount; stage from the recorded label"
      }
    ],
    "overview": {
      "type": "bars",
      "title": "Sequoia's recorded rounds by stage",
      "labelWidth": 300,
      "subtitle": "198 deal records naming Sequoia · 119 after merging repeats",
      "axisLabel": "Rounds (merged)",
      "rows": [
        {
          "label": "Pre-seed",
          "value": 5,
          "display": "5 rounds"
        },
        {
          "label": "Seed",
          "value": 12,
          "display": "12 rounds"
        },
        {
          "label": "Series A",
          "value": 9,
          "display": "9 rounds"
        },
        {
          "label": "Series B",
          "value": 19,
          "display": "19 rounds"
        },
        {
          "label": "Series C",
          "value": 14,
          "display": "14 rounds"
        },
        {
          "label": "Series D",
          "value": 8,
          "display": "8 rounds"
        },
        {
          "label": "Series E+",
          "value": 9,
          "display": "9 rounds"
        },
        {
          "label": "Other or undisclosed",
          "value": 41,
          "display": "41 rounds"
        }
      ],
      "stats": [
        {
          "value": "198",
          "label": "deal records"
        },
        {
          "value": "119",
          "label": "after merging repeats"
        },
        {
          "value": "41",
          "label": "stage not stated"
        },
        {
          "value": "$77.5M",
          "label": "median usable amount"
        }
      ]
    },
    "detail": {
      "type": "table",
      "title": "The largest rounds, with co-investors",
      "subtitle": "Merged records · investors as listed in the deal",
      "headers": [
        "Company",
        "Round",
        "Amount",
        "Co-investors",
        "Published"
      ],
      "widths": [
        17,
        15,
        11,
        44,
        13
      ],
      "rows": [
        [
          {
            "main": "Anthropic",
            "sub": "anthropic.com"
          },
          {
            "tag": "not stated"
          },
          {
            "num": "$25B"
          },
          {
            "sub": "gic, coatue, microsoft, nvidia"
          },
          "19 Jan"
        ],
        [
          {
            "main": "Anthropic",
            "sub": "anthropic.com"
          },
          {
            "tag": "Late-stage…"
          },
          {
            "num": "$20B"
          },
          {
            "sub": "nvidia, microsoft, altimeter capital, lightspeed, menlo ventures, coatue, iconiq"
          },
          "9 Feb"
        ],
        [
          {
            "main": "Waymo",
            "sub": "waymo.com"
          },
          {
            "tag": "Series D"
          },
          {
            "num": "$16B"
          },
          {
            "sub": "alphabet, Andreessen Horowitz, bdt & msd partners, bessemer venture partners, capitalg, dragoneer investment…"
          },
          "27 Mar"
        ],
        [
          {
            "main": "Factory",
            "sub": "factory.com"
          },
          {
            "tag": "Series C"
          },
          {
            "num": "$1.5B"
          },
          {
            "sub": "khosla ventures, blackstone, insight partners, Evantic Capital, 20VC, nea, Mantis VC"
          },
          "22 Apr"
        ],
        [
          {
            "main": "Skild AI",
            "sub": ""
          },
          {
            "tag": "Series C"
          },
          {
            "num": "$1.4B"
          },
          {
            "sub": "softbank group, nventures, bezos expeditions, macquarie capital, samsung, lg, schneider electric,…"
          },
          "14 Jan"
        ],
        [
          {
            "main": "Skild AI Inc.",
            "sub": ""
          },
          {
            "tag": "Series C"
          },
          {
            "num": "$1.4B"
          },
          {
            "sub": "softbank group, nvidia, macquarie group, 1789 Capital, bezos expeditions, lightspeed venture partners,…"
          },
          "14 Jan"
        ]
      ],
      "note": "Re-reports and name variants stay separate records (Skild AI / Skild AI Inc.); compare amounts and dates."
    },
    "footnote": "Investor matching is a name match on the deal's investor list; check the name variant in each row.",
    "takeaway": "See where an investor is active, by stage, with the syndicate behind each round.",
    "evidence_summary": "Saved funding deals naming Sequoia, all pages",
    "guide": "../USER_GUIDE.md#funding-deals"
  },
  {
    "duration": 32,
    "width": 1280,
    "height": 800,
    "disclosure": "Concept UI, not a recording of Claude Code or Codex. Request activity is animated; no live requests run.",
    "id": "india-early-stage-q1-2026",
    "brand": "Prism Business News",
    "kind": "captured",
    "badge": "Captured data · 14 Oct 2026",
    "sources": [
      {
        "file": "../examples/demo/india-early-stage-q1-2026.json",
        "sha256": "242cb22abc613b12a5d1f89b798c33c53d441baf40b7f24ce08631540bb87edd",
        "kind": "captured"
      }
    ],
    "nav": "India early-stage · Q1 2026",
    "client": "Claude Code",
    "heading": "Size a startup market by stage",
    "title": "Size early-stage funding in one country",
    "prompt": "How many seed, Series A and Series B rounds were announced in India in Q1 2026, month by month? Show the largest rounds.",
    "steps": [
      {
        "type": "api",
        "method": "POST",
        "path": "/v1/business/funding",
        "body": {
          "country": "India",
          "round_type": [
            "Seed",
            "Series A",
            "Series B"
          ],
          "since": "2026-01-01",
          "until": "2026-03-31",
          "limit": 100
        },
        "label": "Funding deals filtered by country and round type · followed next_cursor for 5 pages"
      },
      {
        "type": "client",
        "label": "Split by recorded stage",
        "detail": "The Seed filter also matches pre-seed labels; the client keeps them apart"
      }
    ],
    "overview": {
      "type": "columns",
      "stacked": true,
      "title": "Indian early-stage rounds by month, Q1 2026",
      "unit": "deal records",
      "height": 270,
      "subtitle": "499 deal records · stage from the recorded round label",
      "labels": [
        "January",
        "February",
        "March"
      ],
      "series": [
        {
          "name": "Pre-seed & seed",
          "values": [
            73,
            82,
            59
          ]
        },
        {
          "name": "Series A",
          "values": [
            65,
            91,
            56
          ]
        },
        {
          "name": "Series B",
          "values": [
            17,
            19,
            36
          ]
        }
      ],
      "stats": [
        {
          "value": "499",
          "label": "deal records"
        },
        {
          "value": "473",
          "label": "with a usable amount"
        },
        {
          "value": "$3.6M",
          "label": "median usable amount"
        },
        {
          "value": "$5.2B",
          "label": "sum, repeats merged"
        }
      ]
    },
    "detail": {
      "type": "table",
      "title": "The largest early-stage rounds",
      "subtitle": "Merged records · original currency kept beside the USD conversion",
      "headers": [
        "Company",
        "Round",
        "USD",
        "As reported",
        "Sector",
        "Published"
      ],
      "widths": [
        24,
        13,
        11,
        18,
        22,
        12
      ],
      "rows": [
        [
          {
            "main": "Neysa",
            "sub": "Mumbai"
          },
          {
            "tag": "Series B"
          },
          {
            "num": "$600M"
          },
          "USD 600,000,000",
          "Artificial Intelligence",
          "29 Mar"
        ],
        [
          {
            "main": "Neysa Enterprise Infrastructure",
            "sub": "Maharashtra"
          },
          {
            "tag": "Series B"
          },
          {
            "num": "$600M"
          },
          "USD 600,000,000",
          "Cloud Infrastructure",
          "17 Feb"
        ],
        [
          {
            "main": "Aditya Birla Housing Finance Limited",
            "sub": ""
          },
          {
            "tag": "Series A"
          },
          {
            "num": "$304M"
          },
          "USD 304,000,000",
          "Housing Finance",
          "6 Feb"
        ],
        [
          {
            "main": "Positron AI",
            "sub": ""
          },
          {
            "tag": "Series B"
          },
          {
            "num": "$230M"
          },
          "USD 230,000,000",
          "Artificial Intelligence…",
          "5 Feb"
        ],
        [
          {
            "main": "Bonkers Corner",
            "sub": "Mumbai"
          },
          {
            "tag": "Series A"
          },
          {
            "num": "$114M"
          },
          "INR 9,500,000,000",
          "Fashion",
          "6 Mar"
        ]
      ],
      "note": "USD uses fixed conversion rates. Neysa / Neysa Enterprise Infrastructure: one round recorded under two company names, not merged automatically."
    },
    "footnote": "Country comes from the deal record; it may describe the company's base rather than where the round closed.",
    "takeaway": "Count a market's rounds by stage and month, with original currencies intact.",
    "evidence_summary": "Saved funding deals, India, seed to Series B, all pages",
    "guide": "../USER_GUIDE.md#funding-deals"
  },
  {
    "duration": 32,
    "width": 1280,
    "height": 800,
    "disclosure": "Concept UI, not a recording of Claude Code or Codex. Request activity is animated; no live requests run.",
    "id": "hiring-vs-layoffs-q1-2026",
    "brand": "Prism Business News",
    "kind": "captured",
    "badge": "Captured data · 14 Oct 2026",
    "sources": [
      {
        "file": "../examples/demo/hiring-vs-layoffs-q1-2026.json",
        "sha256": "62eb957ee570fc7805fe5a8825cd8c97797ff399ef2f4b27d733c0972284e4ad",
        "kind": "captured"
      }
    ],
    "nav": "Hiring vs layoffs · Q1 2026",
    "client": "Codex",
    "heading": "Compare two signals side by side",
    "title": "Compare hiring and layoff announcements",
    "prompt": "Compare job-creation and layoff announcements week by week in Q1 2026. Which companies appear most on each side?",
    "steps": [
      {
        "type": "api",
        "method": "POST",
        "path": "/v1/business/events",
        "body": {
          "event_type": [
            "job_creation",
            "layoffs"
          ],
          "since": "2026-01-01",
          "until": "2026-03-31",
          "limit": 100
        },
        "label": "Job-creation and layoff events · followed next_cursor for 20 pages"
      },
      {
        "type": "client",
        "label": "Count by week and company",
        "detail": "Client counts every returned event; all pages were read"
      }
    ],
    "overview": {
      "type": "columns",
      "title": "Job creation vs layoffs, weekly, Q1 2026",
      "unit": "events per week",
      "height": 270,
      "subtitle": "973 job-creation and 1,002 layoff events · weeks start Monday",
      "labels": [
        "29 Dec",
        "5 Jan",
        "12 Jan",
        "19 Jan",
        "26 Jan",
        "2 Feb",
        "9 Feb",
        "16 Feb",
        "23 Feb",
        "2 Mar",
        "9 Mar",
        "16 Mar",
        "23 Mar",
        "30 Mar"
      ],
      "sublabels": [
        "partial",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "partial"
      ],
      "series": [
        {
          "name": "Job creation",
          "tone": "positive",
          "values": [
            21,
            35,
            82,
            47,
            62,
            128,
            100,
            91,
            80,
            74,
            45,
            68,
            88,
            52
          ]
        },
        {
          "name": "Layoffs",
          "tone": "negative",
          "values": [
            21,
            61,
            60,
            56,
            89,
            120,
            104,
            76,
            102,
            68,
            61,
            73,
            76,
            35
          ]
        }
      ],
      "stats": [
        {
          "value": "973",
          "label": "job-creation events"
        },
        {
          "value": "1,002",
          "label": "layoff events"
        },
        {
          "value": "7",
          "label": "of 14 weeks with more layoffs"
        },
        {
          "value": "1,259",
          "label": "company domains"
        }
      ]
    },
    "detail": {
      "type": "table",
      "title": "Who appears most on each side",
      "subtitle": "Most frequent linked domains · check flagged links against their sentences",
      "headers": [
        "#",
        "Job creation",
        "Layoffs"
      ],
      "widths": [
        6,
        47,
        47
      ],
      "rows": [
        [
          "1",
          {
            "main": "amazon.com",
            "sub": "25 events"
          },
          {
            "main": "amazon.com",
            "sub": "22 events"
          }
        ],
        [
          "2",
          {
            "main": "lidl.com",
            "sub": "13 events"
          },
          {
            "main": "metavision.com ⚠",
            "sub": "17 events · check link: not Meta's domain"
          }
        ],
        [
          "3",
          {
            "main": "aldi.hu",
            "sub": "12 events"
          },
          {
            "main": "ubisoft.com",
            "sub": "12 events"
          }
        ],
        [
          "4",
          {
            "main": "stellantis.com",
            "sub": "9 events"
          },
          {
            "main": "meta.com",
            "sub": "11 events"
          }
        ],
        [
          "5",
          {
            "main": "apple.com",
            "sub": "8 events"
          },
          {
            "main": "meetblock.com ⚠",
            "sub": "11 events · check link: not Block's domain"
          }
        ]
      ],
      "note": "Company links are extracted from text; ⚠ marks captured mislinks, kept as returned."
    },
    "footnote": "Counts are extracted event sentences, not headcount. Many articles repeat one announcement.",
    "takeaway": "Put two business signals on one timeline and see which companies drive each.",
    "evidence_summary": "Saved job-creation and layoff events, Q1 2026, all pages",
    "guide": "../USER_GUIDE.md#company-events"
  }
];
