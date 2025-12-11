---
title: "MCP Directory (.io)"
url: "https://mcpdirectory.io/"
source_code_url: ""
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: ""
type: ""
evidence:
  - url: "https://mcpdirectory.io/"
    description: "Homepage / primary listing"
last_evaluated: "2025-12-11"
---

# MCP Directory (.io)

## Overview
Simple public directory hosted on Vercel, redirecting to `www.mcpdirectory.io`. Minimal landing content; likely a curated link list.

## Features
- Discovery/search: ❓ Unknown
- One‑click install: ❓ Unknown
- Curated list/recommendations: ❓ Unknown
- API: ❓ Unknown
- Client integration: ❓ Unknown

## Marketplace Classification (Tier 0)

Type: directory/aggregator

Discovery & Metadata Delivery:
- Website: https://mcpdirectory.io → https://www.mcpdirectory.io (Vercel)
- Registry API: ❓ Unknown

Code/Server Delivery:
- Link to source: ❓ Unknown

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 308` to `www` subdomain |
| TLS/security headers | ⚠️ Partial | HSTS set; other headers (CSP/XFO/XCTO) not observed at apex response |
| No mixed content | ✅ Yes | 0 HTTP subresource loads detected |
| Contact information | ⚠️ Minimal | `mailto:jarek@theimpl.com` found in HTML |

DNS/Hosting:
- A: 76.76.21.21 (Vercel)
- NS: OVH (ns20/dns20.ovh.net)
- Provider: Vercel (x-vercel-id; x-vercel-cache)

Policy/API Endpoints:
- All root paths tested return 308 redirect to `www` subdomain (privacy/terms/security/robots; API probes as well)

## Notes

New/Interesting:
- Vercel hosting with complete redirect to `www` suggests content resides on subdomain; audit the `www` target for full signals next.

### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 308
- Provider hints: (none)
- DNS: A=76.76.21.21; CNAME=-; NS=ns20.ovh.net., dns20.ovh.net.
- Security headers: HSTS=max-age=63072000, XFO=(missing), XCTO=(missing)
- Mixed content: http_subresources=0; http_literals=0
- Policy endpoints 200: (none)
- API endpoints 200: (none)
- Social links detected: 1 (showing up to 5)
  - mailto: mailto:jarek@theimpl.com

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.
