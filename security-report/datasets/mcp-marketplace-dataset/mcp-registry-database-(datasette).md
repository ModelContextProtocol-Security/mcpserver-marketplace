---
title: "MCP Registry Database (Datasette)"
url: "https://lite.datasette.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Frosmur%2Fofficial-mcp-registry-database%2Fmain%2Fofficial_mcp_registry.db#/official_mcp_registry/servers"
source_code_url: "https://github.com/rosmur/official-mcp-registry-database"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: ""
type: ""
evidence:
  - url: "https://lite.datasette.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Frosmur%2Fofficial-mcp-registry-database%2Fmain%2Fofficial_mcp_registry.db#/official_mcp_registry/servers"
    description: "Homepage / primary listing"
---

# MCP Registry Database (Datasette)

## Overview
Datasette Lite view over the official MCP registry SQLite database hosted via GitHub Pages. Read-only browser for servers table; useful for quick inspection.

## Features
- Discovery/search: Yes (Datasette filtering/search)
- One‑click install: N/A
- Curated list/recommendations: No (pure browser)
- API: N/A (static; no Datasette API endpoints here)
- Client integration: N/A

## Marketplace Classification (Tier 0)

Type: informational (registry browser)

Discovery & Metadata Delivery:
- Website: Datasette Lite (GitHub Pages), URL-embedded SQLite source
- Source Repo: https://github.com/rosmur/official-mcp-registry-database

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 200` on GitHub Pages |
| TLS/security headers | ❌ Missing | Minimal headers; no HSTS/CSP/XFO/XCTO on page response |
| No mixed content | ✅ Yes | 0 HTTP subresource loads |
| Contact/Legal | ❌ No | No policy pages at root of `lite.datasette.io` |

DNS/Hosting:
- CNAME: `simonw.github.io`; A/AAAA GitHub Pages IPs
- NS: Vercel DNS (domain uses Vercel DNS to CNAME to GitHub Pages)

## Notes

New/Interesting:
- Handy read-only browser of official registry; security posture depends on GitHub Pages delivery; no dynamic backend here.
