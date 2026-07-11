#!/usr/bin/env python3
"""CLI: ai-crawlers

Ai Crawlers
"""
import sys, json, argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Ai Crawlers")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()
    result = {"tool": "ai-crawlers", "description": "Ai Crawlers", "version": "1.0.0", "author": "Jose Zuma", "timestamp": datetime.utcnow().isoformat() + "Z"}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result[chr(39)+chr(39)+chr(39)+chr(39)+chr(39)+chr(39)+chr(39)+chr(39)]}")

if __name__ == "__main__":
    main()
