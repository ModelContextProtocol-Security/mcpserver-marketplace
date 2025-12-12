#!/usr/bin/env python3
"""
MCP Audit - Security audit tool for MCP marketplaces.

Performs three types of checks:
1. Domain: DNS records, TLS certificate, provider detection
2. Web: HTTP headers, security headers, paths, content analysis
3. Repo: GitHub/GitLab security files, org verification, activity

Usage:
    # Run all checks (domain + web, auto-detect from URL)
    python audit.py https://mcp.so

    # Include repository checks
    python audit.py https://mcp.so --repo https://github.com/chatmcp/mcpso

    # Run specific check types
    python audit.py --domain mcp.so
    python audit.py --web https://mcp.so
    python audit.py --repo https://github.com/owner/repo

    # Output options
    python audit.py https://mcp.so --format json    # JSON output (default)
    python audit.py https://mcp.so --format summary # Human-readable summary
"""

import argparse
import json
import sys
from typing import Optional
from urllib.parse import urlparse

from mcp_audit import check_domain, check_web, check_repo


def extract_hostname(url: str) -> str:
    """Extract hostname from URL."""
    if not url.startswith("http"):
        return url
    parsed = urlparse(url)
    return parsed.hostname or url


def print_summary(results: dict) -> None:
    """Print human-readable summary."""

    print("=" * 60)
    print("MCP AUDIT SUMMARY")
    print("=" * 60)

    # Domain results
    if "domain" in results:
        d = results["domain"]
        print("\n## DOMAIN CHECKS")
        print(f"   Hostname: {d['hostname']}")
        print(f"   Registrable domain: {d['registrable_domain']}")

        # DNS
        dns = d["dns"]
        print(f"\n   DNS Records:")
        print(f"     A:     {', '.join(dns['a'][:3]) or 'none'}")
        print(f"     AAAA:  {', '.join(dns['aaaa'][:3]) or 'none'}")
        print(f"     CNAME: {', '.join(dns['cname'][:2]) or 'none'}")
        print(f"     NS:    {', '.join(dns['ns'][:3]) or 'none'}")

        # TLS
        tls = d["tls"]
        if tls["ok"]:
            print(f"\n   TLS Certificate:")
            print(f"     Issuer:  {tls['issuer']}")
            print(f"     Valid:   {tls['not_before']} to {tls['not_after']}")
        else:
            print(f"\n   TLS Certificate: FAILED - {tls.get('error', 'unknown error')}")

        # Providers
        if d["provider_hints"]:
            print(f"\n   Provider Hints: {', '.join(d['provider_hints'])}")

    # Web results
    if "web" in results:
        w = results["web"]
        print("\n## WEB CHECKS")
        print(f"   URL: {w['url']}")

        # HTTP
        http = w["http"]
        if http["ok"]:
            print(f"   Status: {http['status_code']}")
            if http["response_time_ms"]:
                print(f"   Response time: {http['response_time_ms']}ms")
        else:
            print(f"   HTTP FAILED: {http.get('error', 'unknown')}")

        # Security headers
        sh = w["security_headers"]
        present = sh.get("_present", [])
        missing = sh.get("_missing", [])
        print(f"\n   Security Headers:")
        print(f"     Present ({len(present)}): {', '.join(present[:5]) or 'none'}")
        print(f"     Missing ({len(missing)}): {', '.join(missing[:5]) or 'none'}")

        # Paths found
        paths = w["paths"]
        found_paths = [p for p, info in paths.items() if info["status_code"] == 200]
        print(f"\n   Paths Found (200): {', '.join(found_paths[:8]) or 'none'}")

        # Trackers
        trackers = w["trackers"]
        if trackers:
            print(f"\n   Trackers Detected ({len(trackers)}):")
            for t in trackers[:5]:
                print(f"     - {t['name']} ({t['type']})")

        # Mixed content
        mc = w["mixed_content"]
        if mc["http_links_count"] > 0 or mc["http_subresources_count"] > 0:
            print(f"\n   Mixed Content Warning:")
            print(f"     HTTP links: {mc['http_links_count']}")
            print(f"     HTTP subresources: {mc['http_subresources_count']}")

        # Social links
        social = w["social_links"]
        if social:
            print(f"\n   Social Links:")
            for s in social[:5]:
                print(f"     - {s['type']}: {s['url'][:60]}")

    # Repo results
    if "repo" in results:
        r = results["repo"]
        info = r["repo_info"]
        print("\n## REPOSITORY CHECKS")
        print(f"   Platform: {info['platform']}")
        print(f"   Owner/Repo: {info['owner']}/{info['repo']}")

        # Security files
        sf = r["security_files"]
        print(f"\n   Security Files:")
        print(f"     SECURITY.md: {'✅' if sf['security_md'] else '❌'}")
        print(f"     LICENSE: {sf['license'] or '❌'}")
        print(f"     CODE_OF_CONDUCT.md: {'✅' if sf['code_of_conduct'] else '❌'}")
        print(f"     CONTRIBUTING.md: {'✅' if sf['contributing_md'] else '❌'}")

        # Org verification
        org = r["org_verification"]
        if org["is_org"]:
            print(f"\n   Organization:")
            print(f"     Name: {org['org_name']}")
            print(f"     Verified: {'✅' if org['verified'] else '❌'}")
            if org["verified_domains"]:
                print(f"     Verified domains: {', '.join(org['verified_domains'])}")

        # Activity
        act = r["activity"]
        print(f"\n   Activity:")
        print(f"     Stars: {act['stars']:,}")
        print(f"     Forks: {act['forks']:,}")
        print(f"     Open Issues: {act['open_issues']}")
        print(f"     Last Commit: {act['last_commit'] or 'unknown'}")
        print(f"     Archived: {'⚠️ YES' if act['archived'] else 'No'}")

        # Security features
        sec = r["security_features"]
        print(f"\n   Security Features:")
        print(f"     Dependabot: {'✅' if sec['dependabot_enabled'] else '❌'}")
        print(f"     Code Scanning: {'✅' if sec['code_scanning_enabled'] else '❌'}")
        print(f"     Branch Protection: {'✅' if sec['branch_protection'] else '❌'}")
        print(f"     Signed Commits: {'✅' if sec['signed_commits'] else '❌'}")

        if sec["security_advisories"]:
            print(f"\n   Security Advisories ({len(sec['security_advisories'])}):")
            for adv in sec["security_advisories"][:3]:
                print(f"     - {adv['id']}: {adv['severity']} - {adv['summary'][:40]}")

    # Errors
    all_errors = []
    for section in ["domain", "web", "repo"]:
        if section in results and results[section].get("errors"):
            all_errors.extend(results[section]["errors"])

    if all_errors:
        print("\n## ERRORS")
        for err in all_errors:
            print(f"   - {err}")

    print("\n" + "=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="MCP Audit - Security audit tool for MCP marketplaces",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python audit.py https://mcp.so
    python audit.py https://mcp.so --repo https://github.com/chatmcp/mcpso
    python audit.py --domain mcp.so
    python audit.py --web https://mcp.so
    python audit.py --repo https://github.com/owner/repo
        """,
    )

    # Positional argument for URL
    parser.add_argument(
        "url",
        nargs="?",
        help="URL to audit (runs domain + web checks)",
    )

    # Specific check types
    parser.add_argument(
        "--domain",
        metavar="HOSTNAME",
        help="Run only domain checks on hostname",
    )
    parser.add_argument(
        "--web",
        metavar="URL",
        help="Run only web checks on URL",
    )
    parser.add_argument(
        "--repo",
        metavar="URL",
        help="GitHub/GitLab repository URL for repo checks",
    )

    # Options
    parser.add_argument(
        "--format",
        choices=["json", "summary"],
        default="json",
        help="Output format (default: json)",
    )
    parser.add_argument(
        "--github-token",
        metavar="TOKEN",
        help="GitHub token for API requests (or set GITHUB_TOKEN env var)",
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="JSON indent level (default: 2)",
    )

    args = parser.parse_args()

    # Validate arguments
    if not args.url and not args.domain and not args.web and not args.repo:
        parser.print_help()
        sys.exit(1)

    results = {}

    # Run requested checks
    if args.domain:
        results["domain"] = check_domain(args.domain).to_dict()

    if args.web:
        results["web"] = check_web(args.web).to_dict()

    if args.url:
        # Auto-detect: run both domain and web
        hostname = extract_hostname(args.url)
        results["domain"] = check_domain(hostname).to_dict()
        results["web"] = check_web(args.url).to_dict()

    if args.repo:
        results["repo"] = check_repo(args.repo, args.github_token).to_dict()

    # Output
    if args.format == "json":
        print(json.dumps(results, indent=args.indent))
    else:
        print_summary(results)


if __name__ == "__main__":
    main()
