---
title: "Cursor Directory – MCPs"
url: "https://cursor.directory/mcp"
source_code_url: ""
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: ""
type: ""
evidence:
  - url: "https://cursor.directory/mcp"
    description: "Homepage / primary listing"
last_evaluated: "2025-12-11"
  - url: "https://cursor.directory/mcp/privacy"
    description: "/privacy 200"
  - url: "https://cursor.directory/mcp/privacy-policy"
    description: "/privacy-policy 200"
  - url: "https://cursor.directory/mcp/terms"
    description: "/terms 200"
  - url: "https://cursor.directory/mcp/tos"
    description: "/tos 200"
  - url: "https://cursor.directory/mcp/security"
    description: "/security 200"
  - url: "https://cursor.directory/mcp/legal"
    description: "/legal 200"
  - url: "https://cursor.directory/mcp/about"
    description: "/about 200"
  - url: "https://cursor.directory/mcp/contact"
    description: "/contact 200"
  - url: "https://cursor.directory/mcp/robots.txt"
    description: "/robots.txt 200"
  - url: "https://cursor.directory/mcp/sitemap.xml"
    description: "/sitemap.xml 200"
  - url: "https://cursor.directory/mcp/api"
    description: "/api 200"
  - url: "https://cursor.directory/mcp/docs"
    description: "/docs 200"
  - url: "https://cursor.directory/mcp/api-docs"
    description: "/api-docs 200"
  - url: "https://cursor.directory/mcp/swagger.json"
    description: "/swagger.json 200"
  - url: "https://cursor.directory/mcp/openapi.json"
    description: "/openapi.json 200"
  - url: "https://cursor.directory/mcp/openapi.yaml"
    description: "/openapi.yaml 200"
  - url: "https://cursor.directory/mcp/swagger"
    description: "/swagger 200"
---

# Cursor Directory – MCPs

## Overview
Community directory for MCP servers on the `cursor.directory` domain (Vercel). Provides policy pages and exposes an API with OpenAPI/Swagger endpoints.

## Features
- Discovery/search: Yes (directory UI)
- One‑click install: ❓ Unknown
- Curated list/recommendations: Yes (community curation)
- API: ✅ Public endpoints (`/api`, `/openapi.json`, `/swagger.json`)
- Client integration: ❓ Unknown (outside of directory use)

## Marketplace Classification (Tier 0)

Type: directory/aggregator with public API

Discovery & Metadata Delivery:
- Website: https://cursor.directory/mcp (Vercel)
- API docs: Available at `/openapi.json`, `/openapi.yaml`, `/swagger.json`

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 200` |
| TLS/security headers | ⚠️ Partial | HSTS set; CSP/XFO/XCTO not observed at root |
| No mixed content | ✅ Yes | 0 HTTP subresource loads |
| Contact/Legal | ✅ Yes | Privacy/terms/security/legal/about/contact, robots/sitemap all 200 |
| API docs | ✅ Yes | `/api`, `/docs`, `/api-docs`, `/swagger`, OpenAPI endpoints all 200 |

DNS/Hosting:
- NS: Vercel DNS; A: Vercel IPs
- Provider: Vercel

## Notes

New/Interesting:
- Many GitHub links to MCP repos; API is exposed and documented (OpenAPI).

### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 200
- Provider hints: (none)
- DNS: A=216.150.1.129, 216.150.1.193; CNAME=-; NS=ns1.vercel-dns.com., ns2.vercel-dns.com.
- Security headers: HSTS=max-age=63072000, XFO=(missing), XCTO=(missing)
- Mixed content: http_subresources=0; http_literals=0
- Policy endpoints 200: /privacy, /privacy-policy, /terms, /tos, /security, /legal, /about, /contact, /robots.txt, /sitemap.xml
- API endpoints 200: /api, /docs, /api-docs, /swagger.json, /openapi.json, /openapi.yaml, /swagger
- Social links detected: 30 (showing up to 5)
  - github: https://github.com/pontusab/cursor.directory
  - github: https://github.com/pontusab/cursor.directory\
  - github: https://github.com/getrupt/ashra-mcp/tree/main/src/operations\
  - github: https://github.com/dqhieu/compresto-mcp\
  - github: https://github.com/caiyunapp/mcp-caiyun-weather\

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.
