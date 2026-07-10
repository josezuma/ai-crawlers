# Contributing to ai-crawlers

Thanks for helping keep this dataset accurate!

## Adding a New Crawler

1. Add an entry to `crawlers.json` following the existing format
2. Run `python generate_readme.py` to validate and regenerate the README
3. Run `python scripts/export_yaml.py` to regenerate the YAML export
4. Open a PR

## Updating an Existing Crawler

Update the relevant fields in `crawlers.json`, then regenerate the README.

## Entry Requirements

- Must include official documentation URL
- User-agent string must be verified from official sources
- Purpose must be one of: training, search, agent, research, other
- Status must be: active, deprecated, or unknown
