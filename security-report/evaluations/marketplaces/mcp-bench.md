---
title: "MCP Bench"
url: "https://mcpbench.ai"
source_code_url: ""
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: ""
type: ""
evidence:
  - url: "https://mcpbench.ai"
    description: "Homepage / primary listing"
last_evaluated: "2025-12-11"
  - url: "https://mcpbench.ai/about"
    description: "/about 200"
  - url: "https://mcpbench.ai/robots.txt"
    description: "/robots.txt 200"
  - url: "https://mcpbench.ai/sitemap.xml"
    description: "/sitemap.xml 200"
---

# MCP Bench

## Overview
Public browsable directory of MCP servers with a focus on showcasing and benchmarking ecosystem entries. Nuxt-based site on nginx.

## Features
- Discovery/search: Yes (directory UI)
- One‑click install: ❓ Unknown
- Curated list/recommendations: Yes (showcase/bench focus)
- API: No public API at root

## Marketplace Classification (Tier 0)

Type: directory/aggregator

Discovery & Metadata Delivery:
- Website: https://mcpbench.ai

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 200` |
| TLS/security headers | ❌ Missing | No HSTS/CSP/XFO/XCTO observed at root |
| No mixed content | ✅ Yes | 0 HTTP subresource loads |
| Contact/Legal | ⚠️ Minimal | `/about` present; no privacy/terms/security at tested paths |

DNS/Hosting:
- A: 34.66.85.157; NS: DNSOwl
- Server: nginx; X-Powered-By: Nuxt

Policy/API Endpoints:
- `/about`, `/robots.txt`, `/sitemap.xml` 200; other policy paths 404

## Notes

New/Interesting:
- Links to a variety of MCP repos across the ecosystem; good discovery surface.

### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 200
- Provider hints: (none)
- DNS: A=34.66.85.157; CNAME=-; NS=ns3.dnsowl.com., ns1.dnsowl.com., ns2.dnsowl.com.
- Security headers: HSTS=(missing), XFO=(missing), XCTO=(missing)
- Mixed content: http_subresources=0; http_literals=0
- Policy endpoints 200: /about, /robots.txt, /sitemap.xml
- API endpoints 200: (none)
- Social links detected: 13 (showing up to 5)
  - github: https://github.com/modelcontextprotocol/registry
  - github: https://github.com/Daghis/teamcity-mcp
  - github: https://github.com/withinfocus/tba-mcp-server
  - github: https://github.com/sbroenne/mcp-server-excel
  - github: https://github.com/MauriceIsrael/SmartMemory

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.
