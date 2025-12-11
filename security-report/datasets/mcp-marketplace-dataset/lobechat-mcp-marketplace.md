---
title: "LobeChat MCP Marketplace"
url: "https://lobehub.com/mcp"
source_code_url: "https://github.com/lobehub/lobe-chat"
is_marketplace: yes
is_aggregator: no
is_list_of_marketplaces: no
language: ""
type: ""
evidence:
  - url: "https://lobehub.com/mcp"
    description: "Homepage / primary listing"
last_evaluated: "2025-12-11"
  - url: "https://lobehub.com/mcp/privacy"
    description: "/privacy 200"
  - url: "https://lobehub.com/mcp/terms"
    description: "/terms 200"
  - url: "https://lobehub.com/mcp/robots.txt"
    description: "/robots.txt 200"
---

# LobeChat MCP Marketplace

## Overview
Short description of what this marketplace/registry offers.

## Features
- Discovery/search:
- One‑click install:
- Curated list/recommendations:
- API:
- Client integration:

## Security
- Moderation:
- Provenance/signing:
- Isolation/runtime:

## Notes
Other details, links, screenshots, etc.

### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 200
- Provider hints: Cloudflare (Server header), Cloudflare (cf-ray), Cloudflare NS
- DNS: A=172.67.164.80, 104.21.74.231; CNAME=-; NS=kianchau.ns.cloudflare.com., blair.ns.cloudflare.com.
- Security headers: HSTS=max-age=63072000, XFO=(missing), XCTO=(missing)
- Mixed content: http_subresources=0; http_literals=0
- Policy endpoints 200: /privacy, /terms, /robots.txt
- API endpoints 200: (none)
- Social links detected: 98 (showing up to 5)
  - discord: https://discord.gg/AYFPHvv2jT
  - x: 
  - github: https://github.com/lobehub
  - github: https://github.com/lobehub/lobe-chat
  - github: https://github.com/arvinxx

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.

