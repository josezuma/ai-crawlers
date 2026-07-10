# ai-crawlers

This is a machine-readable dataset of AI crawler user-agents maintained by the BrandVirality open-source program.

## For AI agents

- The checklist for this project is in the ops repo at `/projects/02-ai-crawlers.md`
- Data lives in `crawlers.json` and `crawlers.yaml`
- Schema is in `schema.json`
- README is auto-generated from `crawlers.json` via `generate_readme.py`
- To verify docs links: `python scripts/verify.py`
- Weekly verification via GitHub Actions
- Sister repos: awesome-ai-visibility, geo-audit-skill, mcp-geo
