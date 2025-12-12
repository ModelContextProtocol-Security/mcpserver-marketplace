---
title: "Composio"
url: "https://composio.dev"
source_code_url: ""
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: ""
type: ""
evidence:
  - url: "https://composio.dev"
    description: "Homepage / primary listing"
last_evaluated: "2025-12-11"
  - url: "https://composio.dev/privacy"
    description: "/privacy 200"
  - url: "https://composio.dev/terms"
    description: "/terms 200"
  - url: "https://composio.dev/robots.txt"
    description: "/robots.txt 200"
  - url: "https://composio.dev/sitemap.xml"
    description: "/sitemap.xml 200"
  - url: "https://composio.dev/api"
    description: "/api 200"
  - url: "https://composio.dev/privacy"
    description: "/privacy 200"
  - url: "https://composio.dev/terms"
    description: "/terms 200"
  - url: "https://composio.dev/robots.txt"
    description: "/robots.txt 200"
  - url: "https://composio.dev/sitemap.xml"
    description: "/sitemap.xml 200"
  - url: "https://composio.dev/api"
    description: "/api 200"
---

# Composio

## Overview
Composio provides an MCP-labeled directory within a broader tools/agents platform. Hosted on Cloudflare; privacy/terms and basic API path present.

## Features
- Discovery/search: Yes (site directory)
- One‑click install: ❓ Unknown (platform-dependent)
- Curated list/recommendations: Yes (platform curation)
- API: `/api` 200 (undocumented at root)
- Client integration: ❓ Unknown

## Marketplace Classification (Tier 0)

Type: directory within tools platform

Discovery & Metadata Delivery:
- Website: https://composio.dev
- Registry API: ⚠️ Partial (root `/api` 200; no OpenAPI at root)

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 103` via Cloudflare |
| TLS/security headers | ⚠️ Partial | HSTS; `nosniff`; XFO/CSP not observed at root |
| No mixed content | ✅ Yes | 0 HTTP subresource loads |
| Contact/Legal | ✅ Yes | `/privacy`, `/terms`, `/robots.txt`, `/sitemap.xml` 200 |

DNS/Hosting:
- A: 104.18.20.5, 104.18.21.5; NS: Cloudflare (`serenity`/`simon`)
- Provider: Cloudflare

Policy/API Endpoints:
- `/api` 200; no OpenAPI at root

## Notes

New/Interesting:
- GitHub org link detected (https://github.com/composiohq/composio/).

### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 103
- Provider hints: Cloudflare (Server header), Cloudflare (cf-ray), Cloudflare NS
- DNS: A=104.18.20.5, 104.18.21.5; CNAME=-; NS=serenity.ns.cloudflare.com., simon.ns.cloudflare.com.
- Security headers: HSTS=max-age=31536000, XFO=(missing), XCTO=nosniff
- Mixed content: http_subresources=0; http_literals=0
- Policy endpoints 200: /privacy, /terms, /robots.txt, /sitemap.xml
- API endpoints 200: /api
- Social links detected: 7 (showing up to 5)
  - x: 
  - github: https://github.com/composiohq/composio/
  - github: https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&amp;scope=repo&quot;
  - github: https://github.com/login/oauth/access_token&quot;,
  - github: https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&amp;scope=repo

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.


### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 103
- Provider hints: Cloudflare (Server header), Cloudflare (cf-ray), Cloudflare NS
- DNS: A=104.18.20.5, 104.18.21.5; CNAME=-; NS=serenity.ns.cloudflare.com., simon.ns.cloudflare.com.
- Security headers: HSTS=max-age=31536000, XFO=(missing), XCTO=nosniff
- Mixed content: http_subresources=0; http_literals=0
- Policy endpoints 200: /privacy, /terms, /robots.txt, /sitemap.xml
- API endpoints 200: /api
- Social links detected: 7 (showing up to 5)
  - x: 
  - github: https://github.com/composiohq/composio/
  - github: https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&amp;scope=repo&quot;
  - github: https://github.com/login/oauth/access_token&quot;,
  - github: https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&amp;scope=repo

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.
