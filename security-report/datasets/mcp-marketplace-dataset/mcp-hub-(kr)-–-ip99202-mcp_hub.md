---
title: "MCP Hub (KR) – ip99202/mcp_hub"
url: "https://github.com/ip99202/mcp_hub"
source_code_url: "https://github.com/ip99202/mcp_hub"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: ""
type: ""
evidence:
  - url: "https://github.com/ip99202/mcp_hub"
    description: "Homepage / primary listing"
last_evaluated: "2025-12-11"
  - url: "https://github.com/ip99202/mcp_hub/privacy"
    description: "/privacy 200"
  - url: "https://github.com/ip99202/mcp_hub/privacy-policy"
    description: "/privacy-policy 200"
  - url: "https://github.com/ip99202/mcp_hub/security"
    description: "/security 200"
  - url: "https://github.com/ip99202/mcp_hub/about"
    description: "/about 200"
  - url: "https://github.com/ip99202/mcp_hub/robots.txt"
    description: "/robots.txt 200"
  - url: "https://github.com/ip99202/mcp_hub/docs"
    description: "/docs 200"
  - url: "https://github.com/ip99202/mcp_hub/api-docs"
    description: "/api-docs 200"
  - url: "https://github.com/ip99202/mcp_hub/swagger"
    description: "/swagger 200"
---

# MCP Hub (KR) – ip99202/mcp_hub

## Overview
GitHub repository hosting MCP hub content (Korean). Curated resources rather than a hosted registry.

## Features
- Discovery/search: Via repo content
- Curated list/recommendations: Yes

## Marketplace Classification (Tier 0)

Type: informational (GitHub repository)

Discovery & Metadata Delivery:
- Repo: https://github.com/ip99202/mcp_hub

## Security

### Tier 1: Automated/Observable Checks (GitHub pages)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | GitHub `HTTP/2 200` |
| TLS/security headers | ✅ Strong | HSTS, CSP, XFO=deny, XCTO=nosniff |
| Mixed content | ✅ None | HTTP literals present are examples (not subresources) |

## Notes

New/Interesting:
- Example endpoints in README (e.g., `sk-axstudio.com:8000/mcp/fakestore_api`) appear as text, not active loads.

### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 200
- Provider hints: (none)
- DNS: A=140.82.113.3; CNAME=-; NS=ns-1707.awsdns-21.co.uk., ns-421.awsdns-52.com., ns-520.awsdns-01.net.
- Security headers: HSTS=max-age=31536000; includeSubdomains; preload, XFO=deny, XCTO=nosniff
- Mixed content: http_subresources=0; http_literals=13
- Policy endpoints 200: /privacy, /privacy-policy, /security, /about, /robots.txt
- API endpoints 200: /docs, /api-docs, /swagger
- Social links detected: 54 (showing up to 5)
  - github: https://github.com/fluidicon.png
  - github: https://github.com/ip99202/mcp_hub
  - github: https://github.com/ip99202/mcp_hub.git
  - github: https://github.com/ip99202/mcp_hub&quot;,&quot;user_id&quot;:null}}
  - github: https://github.com/features/copilot

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.
