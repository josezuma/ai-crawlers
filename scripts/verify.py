#!/usr/bin/env python3
"""Verify crawler documentation URLs are still reachable."""
import json, sys, os
import requests as r

data = json.load(open("crawlers.json"))
failures = []
for c in data:
    url = c.get("docs_url", "")
    if url:
        try:
            resp = r.head(url, timeout=10, allow_redirects=True)
            if resp.status_code >= 400:
                failures.append(f"{c['name']}: {url} -> {resp.status_code}")
        except Exception as e:
            failures.append(f"{c['name']}: {url} -> {e}")

if failures:
    msg = "Documentation URL check failures:\n"
    for f in failures:
        msg += f"  - {f}\n"
    print(msg)
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        import subprocess
        subprocess.run([
            "gh", "issue", "create",
            "--title", "Crawler documentation URLs need attention",
            "--body", msg,
        ], capture_output=True)
    sys.exit(1)
else:
    print("All crawler documentation URLs are reachable ✓")
