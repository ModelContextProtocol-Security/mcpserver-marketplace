#!/usr/bin/env python3
import csv
from pathlib import Path
import re

CSV_PATH = Path(__file__).parent / "mcp-marketplaces.csv"
OUT_DIR = Path(__file__).parent / "mcp-marketplace-dataset"


def sanitize_filename(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"[\\/:*?\"<>|]", "-", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-") or "marketplace"


def to_bool(s: str) -> str:
    s = (s or "").strip().lower()
    return "yes" if s == "yes" else "no"


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    created = 0
    updated = 0

    with CSV_PATH.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row.get("Marketplace Name", "").strip()
            url = row.get("Marketplace URL", "").strip()
            src = row.get("Source Code URL", "").strip()
            is_mkt = to_bool(row.get("Is Marketplace", ""))
            is_agg = to_bool(row.get("Is Aggregator", ""))
            is_list = to_bool(row.get("Is List Of Marketplaces", ""))

            if not title:
                continue

            fname = sanitize_filename(title) + ".md"
            fpath = OUT_DIR / fname

            if fpath.exists():
                # Do not overwrite existing files
                updated += 1
                continue

            frontmatter = [
                "---",
                f"title: \"{title}\"",
                f"url: \"{url}\"",
                f"source_code_url: \"{src}\"",
                f"is_marketplace: {is_mkt}",
                f"is_aggregator: {is_agg}",
                f"is_list_of_marketplaces: {is_list}",
                "language: \"\"",
                "type: \"\"",
                "evidence:",
                f"  - url: \"{url}\"",
                "    description: \"Homepage / primary listing\"",
                "---",
                "",
                f"# {title}",
                "",
                "## Overview",
                "Short description of what this marketplace/registry offers.",
                "",
                "## Features",
                "- Discovery/search:",
                "- One‑click install:",
                "- Curated list/recommendations:",
                "- API:",
                "- Client integration:",
                "",
                "## Security",
                "- Moderation:",
                "- Provenance/signing:",
                "- Isolation/runtime:",
                "",
                "## Notes",
                "Other details, links, screenshots, etc.",
                "",
            ]

            fpath.write_text("\n".join(frontmatter), encoding="utf-8")
            created += 1

    print(f"Created: {created}, Skipped/Existing: {updated}")


if __name__ == "__main__":
    main()

