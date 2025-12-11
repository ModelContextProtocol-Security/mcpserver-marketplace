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

