#!/usr/bin/env python3
"""
Batch audit for MCP marketplaces.

Reads marketplace list from CSV and runs audits in parallel,
saving results to date-stamped directory.

Usage:
    python batch_audit.py                          # Run all
    python batch_audit.py --limit 5                # Test with first 5
    python batch_audit.py --dry-run                # Show what would run
    python batch_audit.py --github-token TOKEN     # Use GitHub token
"""

import argparse
import csv
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

from mcp_audit import check_domain, check_web, check_repo


def slugify(name: str) -> str:
    """Convert marketplace name to filename-safe slug."""
    # Lowercase, replace spaces/special chars with hyphens
    slug = re.sub(r'[^\w\s-]', '', name.lower())
    slug = re.sub(r'[-\s]+', '-', slug).strip('-')
    return slug[:50]  # Limit length


def is_github_url(url: str) -> bool:
    """Check if URL is a GitHub URL."""
    if not url:
        return False
    return 'github.com' in url.lower()


def extract_hostname(url: str) -> Optional[str]:
    """Extract hostname from URL."""
    if not url or not url.startswith('http'):
        return None
    parsed = urlparse(url)
    return parsed.hostname


def audit_marketplace(
    name: str,
    marketplace_url: str,
    source_url: str,
    github_token: Optional[str] = None
) -> dict:
    """
    Audit a single marketplace.

    Returns dict with results and metadata.
    """
    result = {
        "name": name,
        "marketplace_url": marketplace_url,
        "source_url": source_url,
        "audited_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "checks_run": [],
        "errors": [],
    }

    # Determine what to check
    has_website = marketplace_url and not is_github_url(marketplace_url)
    has_github_marketplace = marketplace_url and is_github_url(marketplace_url)
    has_source_repo = source_url and is_github_url(source_url)

    # Run website checks (domain + web)
    if has_website:
        try:
            hostname = extract_hostname(marketplace_url)
            if hostname:
                result["domain"] = check_domain(hostname).to_dict()
                result["checks_run"].append("domain")
        except Exception as e:
            result["errors"].append(f"domain check failed: {e}")

        try:
            result["web"] = check_web(marketplace_url).to_dict()
            result["checks_run"].append("web")
        except Exception as e:
            result["errors"].append(f"web check failed: {e}")

    # Run repo check on marketplace URL if it's GitHub
    if has_github_marketplace:
        try:
            result["repo"] = check_repo(marketplace_url, github_token).to_dict()
            result["checks_run"].append("repo")
        except Exception as e:
            result["errors"].append(f"repo check failed: {e}")

    # Run repo check on source URL if different from marketplace URL
    if has_source_repo and source_url != marketplace_url:
        try:
            result["source_repo"] = check_repo(source_url, github_token).to_dict()
            result["checks_run"].append("source_repo")
        except Exception as e:
            result["errors"].append(f"source_repo check failed: {e}")

    result["success"] = len(result["errors"]) == 0
    return result


def load_marketplaces(csv_path: str) -> list[dict]:
    """Load marketplaces from CSV."""
    marketplaces = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get('Marketplace Name', '').strip()
            url = row.get('Marketplace URL', '').strip()
            source = row.get('Source Code URL', '').strip()

            # Skip empty rows
            if not name:
                continue

            marketplaces.append({
                'name': name,
                'marketplace_url': url,
                'source_url': source,
                'slug': slugify(name),
            })

    return marketplaces


def main():
    parser = argparse.ArgumentParser(
        description="Batch audit MCP marketplaces",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        '--csv',
        default='../working-data/mcp-marketplaces.csv',
        help='Path to marketplaces CSV (default: ../working-data/mcp-marketplaces.csv)',
    )
    parser.add_argument(
        '--output-dir',
        default='../working-data/audit-results',
        help='Output directory (default: ../working-data/audit-results)',
    )
    parser.add_argument(
        '--limit',
        type=int,
        help='Limit number of marketplaces to audit',
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be audited without running',
    )
    parser.add_argument(
        '--workers',
        type=int,
        default=8,
        help='Number of parallel workers (default: 8)',
    )
    parser.add_argument(
        '--github-token',
        help='GitHub token for API requests (or set GITHUB_TOKEN env var)',
    )

    args = parser.parse_args()

    # Resolve paths relative to script location
    script_dir = Path(__file__).parent
    csv_path = (script_dir / args.csv).resolve()
    output_base = (script_dir / args.output_dir).resolve()

    # Get GitHub token
    github_token = args.github_token or os.environ.get('GITHUB_TOKEN')

    # Load marketplaces
    if not csv_path.exists():
        print(f"Error: CSV not found: {csv_path}", file=sys.stderr)
        sys.exit(1)

    marketplaces = load_marketplaces(str(csv_path))
    print(f"Loaded {len(marketplaces)} marketplaces from {csv_path.name}")

    if args.limit:
        marketplaces = marketplaces[:args.limit]
        print(f"Limited to {len(marketplaces)} marketplaces")

    # Dry run - just show what would be done
    if args.dry_run:
        print("\nDry run - would audit:")
        for m in marketplaces:
            checks = []
            if m['marketplace_url'] and not is_github_url(m['marketplace_url']):
                checks.append('domain+web')
            if m['marketplace_url'] and is_github_url(m['marketplace_url']):
                checks.append('repo')
            if m['source_url'] and m['source_url'] != m['marketplace_url']:
                checks.append('source_repo')
            print(f"  {m['name']}: {', '.join(checks) or 'no checks'}")
        return

    # Create output directory with date
    date_str = datetime.now().strftime('%Y-%m-%d')
    output_dir = output_base / date_str
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {output_dir}")

    # Run audits in parallel
    results = []
    failed = []

    print(f"\nRunning audits with {args.workers} workers...")
    print("-" * 60)

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        # Submit all tasks
        future_to_marketplace = {
            executor.submit(
                audit_marketplace,
                m['name'],
                m['marketplace_url'],
                m['source_url'],
                github_token,
            ): m
            for m in marketplaces
        }

        # Process as they complete
        for future in as_completed(future_to_marketplace):
            marketplace = future_to_marketplace[future]
            slug = marketplace['slug']

            try:
                result = future.result()
                results.append(result)

                # Save individual result
                result_path = output_dir / f"{slug}.json"
                with open(result_path, 'w') as f:
                    json.dump(result, f, indent=2)

                status = "OK" if result['success'] else "ERRORS"
                checks = ', '.join(result['checks_run']) or 'none'
                print(f"  [{status}] {marketplace['name']}: {checks}")

            except Exception as e:
                failed.append({'name': marketplace['name'], 'error': str(e)})
                print(f"  [FAIL] {marketplace['name']}: {e}")

    # Create index
    index = {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "csv_source": csv_path.name,
        "total_marketplaces": len(marketplaces),
        "successful": len([r for r in results if r['success']]),
        "with_errors": len([r for r in results if not r['success']]),
        "failed": len(failed),
        "marketplaces": [
            {
                "name": r['name'],
                "slug": slugify(r['name']),
                "success": r['success'],
                "checks_run": r['checks_run'],
                "errors": r['errors'],
            }
            for r in results
        ],
        "failures": failed,
    }

    index_path = output_dir / "index.json"
    with open(index_path, 'w') as f:
        json.dump(index, f, indent=2)

    # Summary
    print("-" * 60)
    print(f"\nComplete!")
    print(f"  Total: {len(marketplaces)}")
    print(f"  Successful: {index['successful']}")
    print(f"  With errors: {index['with_errors']}")
    print(f"  Failed: {index['failed']}")
    print(f"\nResults saved to: {output_dir}")


if __name__ == "__main__":
    main()
