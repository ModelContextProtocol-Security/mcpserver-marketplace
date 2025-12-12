---
title: "MCP Hub"
url: "https://mcphub.io"
source_code_url: ""
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: ""
type: ""
evidence:
  - url: "https://mcphub.io"
    description: "Homepage / primary listing"
last_evaluated: "2025-12-11"
  - url: "https://mcphub.io/robots.txt"
    description: "/robots.txt 200"
  - url: "https://mcphub.io/sitemap.xml"
    description: "/sitemap.xml 200"
---

# MCP Hub

## Overview
Public directory/discovery site hosted on Vercel behind Cloudflare. Minimal landing metadata.

## Features
- Discovery/search: ❓ Unknown
- One‑click install: ❓ Unknown
- Curated list/recommendations: ❓ Unknown
- API: ❓ Unknown
- Client integration: ❓ Unknown

## Marketplace Classification (Tier 0)

Type: directory/aggregator

Discovery & Metadata Delivery:
- Website: https://mcphub.io (Cloudflare + Vercel)

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 200` via Cloudflare |
| TLS/security headers | ⚠️ Partial | HSTS set; CSP/XFO/XCTO not observed at root |
| No mixed content | ✅ Yes | 0 HTTP subresource loads |
| Contact information | ❓ Unknown | No contact/legal at root |

DNS/Hosting:
- A/AAAA: Cloudflare edges; NS: Cloudflare (gabriella/jose)
- Provider: Cloudflare CDN; Vercel (`x-vercel-id`)

Policy/API Endpoints:
- `/robots.txt` 200; `/sitemap.xml` 200; other policy paths 404
- API probes: 404

## Notes

New/Interesting:
- Vercel deployment behind Cloudflare; prerendered Next.js with long stale time.

### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 200
- Provider hints: Cloudflare (Server header), Cloudflare (cf-ray), Cloudflare NS
- DNS: A=104.21.70.34, 172.67.218.211; CNAME=-; NS=gabriella.ns.cloudflare.com., jose.ns.cloudflare.com.
- Security headers: HSTS=max-age=63072000, XFO=(missing), XCTO=(missing)
- Mixed content: http_subresources=0; http_literals=0
- Policy endpoints 200: /robots.txt, /sitemap.xml
- API endpoints 200: (none)
- Social links detected: 0 (showing up to 5)

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.
