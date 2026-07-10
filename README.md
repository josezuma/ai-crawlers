<div align="center">
  <h1>🤖 AI Crawlers</h1>
  <p><em>Machine-readable dataset of AI crawler user-agents — GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Bytespider, and more.</em></p>
  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
    <a href="https://github.com/josezuma/ai-crawlers/actions/workflows/verify.yml"><img src="https://github.com/josezuma/ai-crawlers/actions/workflows/verify.yml/badge.svg" alt="Weekly Verification"></a>
    <a href="https://github.com/josezuma/ai-crawlers"><img src="https://img.shields.io/github/stars/josezuma/ai-crawlers?style=social" alt="Stars"></a>
  </p>
  <p>by <a href="https://brandvirality.com">BrandVirality</a> — Every AI crawler in one place. Block or allow them all with one command.</p>

  <p><strong>Author:</strong> <a href="https://github.com/josezuma">Jose Zuma — Expert in AI Visibility</a></p>
</div>

---

## Quick Start

```bash
# Get all crawlers as JSON
curl -s https://raw.githubusercontent.com/josezuma/ai-crawlers/main/crawlers.json | jq '.[] | {name, vendor, purpose}'

# Generate robots.txt to ALLOW all AI crawlers
curl -s https://raw.githubusercontent.com/josezuma/ai-crawlers/main/crawlers.json | \
  python3 -c "import json,sys;c=json.load(sys.stdin);[print(e['allow_recipe']+'') for e in c if e.get('allow_recipe')]"

# Generate robots.txt to BLOCK all AI crawlers
curl -s https://raw.githubusercontent.com/josezuma/ai-crawlers/main/crawlers.json | \
  python3 -c "import json,sys;c=json.load(sys.stdin);[print(e['disallow_recipe']+'') for e in c if e.get('disallow_recipe')]"
```

## Dataset

**18 crawlers** documented and verified. Schema: [schema.json](schema.json)

| Crawler | Vendor | Purpose | Status |
|---------|--------|---------|--------|
| Amazonbot | Amazon | research | ✅ active |
| Anthropic AI Crawler | Anthropic | training | ✅ active |
| Applebot | Apple | search | ✅ active |
| Bingbot | Microsoft | search | ✅ active |
| Bytespider | ByteDance (TikTok) | training | ✅ active |
| ClaudeBot | Anthropic | training | ✅ active |
| Cohere AI Crawler | Cohere | training | ✅ active |
| Common Crawl (CCBot) | Common Crawl Foundation | research | ✅ active |
| DuckDuckBot | DuckDuckGo | search | ✅ active |
| Google AI Overviews (via Googlebot) | Google | search | ✅ active |
| Google-Extended | Google | training | ✅ active |
| GPTBot | OpenAI | training | ✅ active |
| Grok Social Crawler | xAI | training | ✅ active |
| Meta-ExternalAgent | Meta (Facebook) | training | ✅ active |
| Microsoft AI Crawler | Microsoft | training | ✅ active |
| OpenAI Search Crawler | OpenAI | search | ✅ active |
| PerplexityBot | Perplexity AI | search | ✅ active |
| SemrushBot | Semrush | research | ✅ active |

## robots.txt Recipes

### Amazonbot
Amazon's web crawler for AI research and model training.

Allow:
```txt
User-agent: Amazonbot
Allow: /
```

Block:
```txt
User-agent: Amazonbot
Disallow: /
```

### Anthropic AI Crawler
Secondary Anthropic crawler for specific AI training purposes.

Allow:
```txt
User-agent: Anthropic-AI
Allow: /
```

Block:
```txt
User-agent: Anthropic-AI
Disallow: /
```

### Applebot
Apple's web crawler for Siri and Apple Intelligence search features.

Allow:
```txt
User-agent: Applebot
Allow: /
```

Block:
```txt
User-agent: Applebot
Disallow: /
```

### Bingbot
Microsoft Bing's search crawler. Sources content for Bing Chat/Copilot answers.

Allow:
```txt
User-agent: bingbot
Allow: /
```

Block:
```txt
User-agent: bingbot
Disallow: /
```

### Bytespider
ByteDance's AI training crawler. Known for aggressive crawling rates.

Allow:
```txt
User-agent: Bytespider
Allow: /
```

Block:
```txt
User-agent: Bytespider
Disallow: /
```

### ClaudeBot
Anthropic's web crawler for training Claude models.

Allow:
```txt
User-agent: ClaudeBot
Allow: /
```

Block:
```txt
User-agent: ClaudeBot
Disallow: /
```

### Cohere AI Crawler
Cohere's web crawler for training enterprise AI models.

Allow:
```txt
User-agent: cohere-ai
Allow: /
```

Block:
```txt
User-agent: cohere-ai
Disallow: /
```

### Common Crawl (CCBot)
Non-profit web crawl dataset widely used for training AI models. Opt out via robots.txt.

Allow:
```txt
User-agent: CCBot
Allow: /
```

Block:
```txt
User-agent: CCBot
Disallow: /
```

### DuckDuckBot
DuckDuckGo's search crawler. Sources content for their AI-generated answers.

Allow:
```txt
User-agent: DuckDuckBot
Allow: /
```

Block:
```txt
User-agent: DuckDuckBot
Disallow: /
```

### Google AI Overviews (via Googlebot)
Google's main crawler. AI Overviews content is sourced from Googlebot's index.

Allow:
```txt
User-agent: Googlebot
Allow: /
```

Block:
```txt
User-agent: Googlebot
Disallow: /
```

### Google-Extended
Google's separate user-agent for AI model training. Does not affect Google Search indexing.

Allow:
```txt
User-agent: Google-Extended
Allow: /
```

Block:
```txt
User-agent: Google-Extended
Disallow: /
```

### GPTBot
OpenAI's web crawler for training GPT models. Respects robots.txt.

Allow:
```txt
User-agent: GPTBot
Allow: /
```

Block:
```txt
User-agent: GPTBot
Disallow: /
```

### Grok Social Crawler
xAI's crawler for training Grok models.

Allow:
```txt
User-agent: GrokSocial
Allow: /
```

Block:
```txt
User-agent: GrokSocial
Disallow: /
```

### Meta-ExternalAgent
Meta's crawler for AI training data collection.

Allow:
```txt
User-agent: Meta-ExternalAgent
Allow: /
```

Block:
```txt
User-agent: Meta-ExternalAgent
Disallow: /
```

### Microsoft AI Crawler
Microsoft's AI training crawler for Copilot and other AI products.

Allow:
```txt
User-agent: Microsoft-AI
Allow: /
```

Block:
```txt
User-agent: Microsoft-AI
Disallow: /
```

### OpenAI Search Crawler
OpenAI's search crawler for ChatGPT web search functionality.

Allow:
```txt
User-agent: OAI-SearchBot
Allow: /
```

Block:
```txt
User-agent: OAI-SearchBot
Disallow: /
```

### PerplexityBot
Perplexity AI's search crawler for real-time information retrieval.

Allow:
```txt
User-agent: PerplexityBot
Allow: /
```

Block:
```txt
User-agent: PerplexityBot
Disallow: /
```

### SemrushBot
SEO tool crawler. Also provides AI visibility analytics.

Allow:
```txt
User-agent: SemrushBot
Allow: /
```

Block:
```txt
User-agent: SemrushBot
Disallow: /
```

## Schema

The dataset validates against [schema.json](schema.json). Each entry contains:

- **id** — unique kebab-case identifier
- **name** — display name
- **user_agent** — the full user-agent string
- **purpose** — `training`, `search`, `agent`, `research`, or `other`
- **vendor** — operating company
- **docs_url** — official documentation
- **status** — `active`, `deprecated`, or `unknown`
- **respects_robots_txt** — boolean
- **robots_txt_entry** — the `User-agent` token for robots.txt
- **allow_recipe** / **disallow_recipe** — ready-to-use robots.txt snippets
- **added** / **updated** — ISO 8601 dates

## Weekly Verification

A GitHub Action runs every Monday to re-check each vendor's documentation page. If a crawler's docs URL changes or the crawler is deprecated, the Action opens an issue so this dataset stays accurate. [View workflow](.github/workflows/verify.yml)

## Examples

See [examples/](examples/) for real robots.txt files built from this dataset.

## Related

- [awesome-ai-visibility](https://github.com/josezuma/awesome-ai-visibility) — Curated list of AI visibility/GEO resources
- [geo-audit-skill](https://github.com/josezuma/geo-audit-skill) — Agent skill for AI-search readiness auditing
- [geo-prompts](https://github.com/josezuma/geo-prompts) — Benchmark prompts for LLM share-of-voice
- [BrandVirality](https://brandvirality.com) — SaaS for AI visibility

## License

[MIT](LICENSE) © 2026 Jose Zuma / BrandVirality
