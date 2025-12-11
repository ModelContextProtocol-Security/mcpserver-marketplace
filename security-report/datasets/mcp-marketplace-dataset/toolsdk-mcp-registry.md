---
title: "ToolSDK MCP Registry"
url: "https://toolsdk.ai"
source_code_url: "https://github.com/toolsdk-ai/toolsdk-mcp-registry"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: ""
type: ""
evidence:
  - url: "https://toolsdk.ai"
    description: "Homepage / primary listing"
---

# ToolSDK MCP Registry

## Overview
ToolSDK site with an MCP registry offering. Next.js-based; privacy policy present; robots/sitemap present; OpenAPI JSON present at root.

## Features
- Discovery/search: Yes (site directory)
- One‑click install: ❓ Unknown
- Curated list/recommendations: Yes
- API: ⚠️ Partial (OpenAPI JSON present at `/openapi.json`)

## Marketplace Classification (Tier 0)

Type: directory + registry API

Discovery & Metadata Delivery:
- Website: https://toolsdk.ai
- API docs: `/openapi.json` 200

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 200` |
| TLS/security headers | ❌ Missing | No HSTS/CSP/XFO/XCTO observed at root response |
| No mixed content | ✅ Yes | 0 HTTP subresource loads |
| Contact/Legal | ⚠️ Partial | `/privacy-policy` 200; `/about` 200; others 404 |

DNS/Hosting:
- NS: Cloudflare; A: AWS IPs (44.240.47.189, 35.82.152.42)

Policy/API Endpoints:
- `/robots.txt` 200; `/sitemap.xml` 200; `/openapi.json` 200

## Notes

New/Interesting:
- GitHub org links: https://github.com/toolsdk-ai/toolsdk and curated `awesome-mcp-registry` list.
