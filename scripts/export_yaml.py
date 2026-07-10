#!/usr/bin/env python3
"""Export crawlers.json to YAML format."""
import json, yaml, sys
from pathlib import Path

data = json.loads(Path("crawlers.json").read_text())
with open("crawlers.yaml", "w") as f:
    yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
print("crawlers.yaml written ✓")
