#!/usr/bin/env python3
"""
generate_readme.py — Generates README.md from crawlers.json data.

Usage:
    python generate_readme.py          # writes README.md
    python generate_readme.py --check  # validates JSON against schema
"""

import json, os, sys, argparse
from pathlib import Path

HERE = Path(__file__).parent
DATA_FILE = HERE / "crawlers.json"
SCHEMA_FILE = HERE / "schema.json"
README_FILE = HERE / "README.md"

def load_data():
    with open(DATA_FILE) as f:
        return json.load(f)

def load_schema():
    with open(SCHEMA_FILE) as f:
        return json.load(f)

def validate():
    """Basic validation of crawlers.json against schema requirements."""
    data = load_data()
    schema = load_schema()
    required = schema["items"]["required"]
    errors = []
    for i, crawler in enumerate(data):
        for field in required:
            if field not in crawler:
                errors.append(f"Entry {i} ({crawler.get('name','?')}): missing required field '{field}'")
        if 'id' in crawler:
            if not crawler['id'].replace('-', '').isalnum():
                errors.append(f"Entry {i}: invalid id '{crawler['id']}'")
        if 'purpose' in crawler and crawler['purpose'] not in schema["items"]["properties"]["purpose"]["enum"]:
            errors.append(f"Entry {i}: invalid purpose '{crawler['purpose']}'")
        if 'status' in crawler and crawler['status'] not in schema["items"]["properties"]["status"]["enum"]:
            errors.append(f"Entry {i}: invalid status '{crawler['status']}'")
    return errors

def robots_txt_block(data):
    """Generate complete robots.txt allow/block recipes."""
    lines = ["# ── AI Crawler robots.txt Recipes ──────────────────────────────", ""]
    lines.append("# Option A: Block ALL AI crawlers")
    lines.append("User-agent: GPTBot")
    lines.append("Disallow: /")
    for c in data:
        if c.get("robots_txt_entry") and c["robots_txt_entry"] != "GPTBot":
            lines.append(f"User-agent: {c['robots_txt_entry']}")
            lines.append("Disallow: /")
    lines.append("")
    lines.append("# Option B: Allow ALL AI crawlers")
    lines.append("User-agent: *")
    lines.append("Disallow:")
    lines.append("")
    lines.append("# Option C: Selective (example — allow search crawlers, block training)")
    for c in data:
        entry = c.get("robots_txt_entry")
        purpose = c.get("purpose", "unknown")
        if entry:
            if purpose == "training":
                lines.append(f"User-agent: {entry}")
                lines.append("  Disallow: /")
            elif purpose in ("search", "agent"):
                lines.append(f"User-agent: {entry}")
                lines.append("  Disallow:")
    return "\n".join(lines)

def purpose_table(data):
    """Generate summary table by purpose."""
    purposes = {}
    for c in data:
        p = c.get("purpose", "other")
        purposes.setdefault(p, []).append(c["name"])
    lines = ["| Purpose | Count | Crawlers |", "|---------|-------|----------|"]
    for p in ["training", "search", "agent", "research", "other"]:
        crawlers = purposes.get(p, [])
        lines.append(f"| {p.title()} | {len(crawlers)} | {', '.join(crawlers) if crawlers else '—'} |")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Generate ai-crawlers README")
    parser.add_argument("--check", action="store_true", help="Only validate data, don't write README")
    args = parser.parse_args()

    errors = validate()
    if errors:
        print("VALIDATION ERRORS:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    print("Validation passed ✓", file=sys.stderr)

    if args.check:
        return

    data = load_data()

    entries = []
    for c in sorted(data, key=lambda x: x["name"].lower()):
        purpose_badge = {
            "training": "🔴 Training",
            "search": "🟡 Search",
            "agent": "🟢 Agent",
            "research": "🔵 Research",
            "other": "⚪ Other",
        }.get(c.get("purpose", "other"), "⚪ Other")

        status_badge = "✅ Active" if c.get("status") == "active" else ("⚠️ Deprecated" if c.get("status") == "deprecated" else "❓ Unknown")

        entries.append(f"""
### {c['name']}  `{c['id']}`

| Field | Value |
|-------|-------|
| **User-Agent** | `{c['user_agent']}` |
| **Purpose** | {purpose_badge} |
| **Status** | {status_badge} |
| **Vendor** | {c['vendor']} |
| **Docs** | [{c['docs_url'].split('//')[1].split('/')[0]}]({c['docs_url']}) |
| **Robots.txt Token** | `{c.get('robots_txt_entry', 'N/A')}` |
| **Respects robots.txt** | {'✅' if c.get('respects_robots_txt', True) else '❌'} |
| **Added** | {c.get('added', 'N/A')} |
{f"| **Notes** | {c.get('notes', '')} |" if c.get('notes') else ''}
""")

    purpose_summary = purpose_table(data)
    robots_block = robots_txt_block(data)

    readme = f"""# 🤖 AI Crawlers — Machine-Readable Dataset

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![JSON Schema](https://img.shields.io/badge/schema-JSON%20Schema-blue)](schema.json)
[![Validation](https://github.com/josezuma/ai-crawlers/actions/workflows/validate.yml/badge.svg)](https://github.com/josezuma/ai-crawlers/actions/workflows/validate.yml)
[![Weekly Verify](https://github.com/josezuma/ai-crawlers/actions/workflows/verify.yml/badge.svg)](https://github.com/josezuma/ai-crawlers/actions/workflows/verify.yml)

> **Curated, machine-readable dataset of AI crawler user-agents.** Know which bots are crawling your site, what they're for, and how to control them with robots.txt.

**20 crawlers** documented — GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Bytespider, and more. Updated regularly with weekly automated verification.

---

## Quick Start

### 1. Get the data

```bash
# JSON (full dataset with all metadata)
curl -O https://raw.githubusercontent.com/josezuma/ai-crawlers/main/crawlers.json

# YAML (auto-generated from JSON)
curl -O https://raw.githubusercontent.com/josezuma/ai-crawlers/main/crawlers.yaml
```

### 2. Validate

```bash
# Requires Python + jsonschema
pip install jsonschema
python generate_readme.py --check
```

### 3. Use in robots.txt

Block GPTBot only:
```robotstxt
User-agent: GPTBot
Disallow: /
```

Block all known AI training crawlers:
```robotstxt
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: Bytespider
Disallow: /
```

---

## Purpose Summary

{purpose_summary}

## Full Crawler List

{''.join(entries)}

---

## robots.txt Recipes

{robots_block}

---

## Weekly Verification

Every Monday, a GitHub Action re-checks each vendor's documentation page for changes. If a crawler's user-agent, purpose, or status has changed, an issue is automatically opened.

This ensures the dataset stays accurate as AI companies update their crawlers.

---

## Schema

The data follows a [JSON Schema](schema.json). The schema is self-documenting with descriptions for every field.

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | ✅ | Unique identifier (kebab-case) |
| `name` | string | ✅ | Display name |
| `user_agent` | string | ✅ | User-agent string or pattern |
| `purpose` | enum | ✅ | training, search, agent, research, other |
| `vendor` | string | ✅ | Operating company |
| `docs_url` | uri | ✅ | Official documentation URL |
| `status` | enum | ✅ | active, deprecated, unknown |
| `respects_robots_txt` | boolean | ❌ | Whether it respects robots.txt |
| `robots_txt_entry` | string | ❌ | Token to use in robots.txt |
| `allow_recipe` | string | ❌ | robots.txt snippet to allow |
| `disallow_recipe` | string | ❌ | robots.txt snippet to block |
| `added` | date | ✅ | Date added (ISO 8601) |
| `updated` | date | ❌ | Date last updated |
| `notes` | string | ❌ | Additional context |

---

## Data Format

The dataset is available in two formats:

- **JSON** ([crawlers.json](crawlers.json)) — Full structured data with all metadata
- **YAML** ([crawlers.yaml](crawlers.yaml)) — Auto-generated from JSON

Both contain identical information. Pick whichever your workflow prefers.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). All contributions welcome — new crawlers, updated documentation links, corrected user-agent strings, or better robots.txt recipes.

---

## Related

- [awesome-ai-visibility](https://github.com/josezuma/awesome-ai-visibility) — Curated list of AI visibility / GEO resources
- [geo-audit-skill](https://github.com/josezuma/geo-audit-skill) — Agent skill that audits URLs for AI-search readiness
- [mcp-geo](https://github.com/josezuma/mcp-geo) — MCP server for GEO auditing

---

## License

[MIT](LICENSE) © 2026 [Jose Zuma](https://brandvirality.com) / BrandVirality

---

<div align="center">
  <sub>Maintained by <a href="https://brandvirality.com">BrandVirality</a> — AI Visibility Agency. We make your business discoverable in every LLM chat.</sub>
</div>
"""

    with open(README_FILE, "w") as f:
        f.write(readme)

    print(f"README written to {README_FILE} ✓", file=sys.stderr)
    print(f"Total crawlers: {len(data)}", file=sys.stderr)

if __name__ == "__main__":
    main()
