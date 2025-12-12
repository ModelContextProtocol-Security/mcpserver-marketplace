---
title: "MCP Server Directory"
url: "https://mcpserverdirectory.org/"
source_code_url: ""
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: ""
type: ""
evidence:
  - url: "https://mcpserverdirectory.org/"
    description: "Homepage / primary listing"
---

# MCP Server Directory

## Overview
Vercel-hosted directory listing MCP servers, with many links to official MCP server repos. Privacy policy present; robots present.

## Features
- Discovery/search: Yes (directory UI)
- One‑click install: ❓ Unknown
- Curated list/recommendations: Yes
- API: No public API at root

## Marketplace Classification (Tier 0)

Type: directory/aggregator

Discovery & Metadata Delivery:
- Website: https://mcpserverdirectory.org/

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 200` |
| TLS/security headers | ⚠️ Partial | HSTS preload; `nosniff`; Referrer-Policy set; XFO/CSP not observed |
| No mixed content | ✅ Yes | 0 HTTP subresource loads |
| Contact/Legal | ⚠️ Partial | `/privacy-policy` 200; no `/terms` or `/security` |

DNS/Hosting:
- NS: Vercel DNS; A: 216.198.79.1, 64.29.17.1
- Provider: Vercel

Policy/API Endpoints:
- Privacy policy and robots present; no sitemap; API probes 404

## Notes

New/Interesting:
- Numerous links to `modelcontextprotocol/servers` components; directory likely curated to official repos.
