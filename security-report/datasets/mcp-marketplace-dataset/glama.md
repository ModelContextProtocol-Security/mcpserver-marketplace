---
title: "Glama"
url: "https://glama.ai"
source_code_url: ""
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "client + directory"
operator: "❓ Unknown"
last_evaluated: "2025-12-11"
evidence:
  - url: "https://glama.ai"
    description: "Homepage (Caddy server)"
  - url: "https://glama.ai/robots.txt"
    description: "robots.txt 200"
  - url: "https://glama.ai/sitemap.xml"
    description: "sitemap.xml 200"
---

# Glama

## Overview
Glama appears to combine an MCP-capable client experience with a directory/discovery surface. The site uses a strong security header posture (HSTS, CSP, XFO, Referrer-Policy), and serves static assets from `static.glama.ai` with a strict CSP/nonces.

## Features
- Discovery/search: ❓ Unknown from landing (likely within app experience)
- One‑click install: ❓ Unknown
- Curated list/recommendations: ❓ Unknown
- API: ❓ Unknown (no public API endpoints at root)
- Client integration: Appears to be its own client platform

## Marketplace Classification (Tier 0)

Type: client + directory

Discovery & Metadata Delivery:
- Website: https://glama.ai
- Registry API: ❓ Unknown
- Client/app: Present (site/app routing suggests in-app `/mcp` route)

Code/Server Delivery:
- Link to source: ❓ Unknown
- Local installation: ❓ Unknown
- Hosted execution: ❓ Unknown

Source Accessibility:
- Marketplace/client source code: ❓ Unknown
- API docs: ❓ Unknown

Server Coverage:
- Lists vendor-hosted servers: ❓ Unknown
- Distinguishes hosted vs local: ❓ Unknown

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 103` with `Location: /mcp` |
| TLS/security headers | ✅ Strong | HSTS `includeSubDomains; preload`; CSP with nonces; XFO=SAMEORIGIN; Referrer-Policy=strict-origin-when-cross-origin; Permissions-Policy set |
| No mixed content | ✅ Yes | 0 HTTP subresource loads detected |
| Contact information | ❓ Unknown | No contact page at tested root paths |
| Issue tracker | ❓ Unknown | Not linked on landing |
| Provenance visible | ❓ Unknown | Not evaluated in-app |
| Official vs third‑party | ❓ Unknown |
| Timestamps | ❓ Unknown |

DNS/CDN and Hosting:
- A: 66.241.124.71, 37.16.29.120; AAAA: 2a09:8280:1::5c:44fc:0
- NS: Cloudflare (isaac, davina)
- Server: Caddy with robust security headers; static assets served from `static.glama.ai`

Policy/API Endpoints:
- `/robots.txt` 200; `/sitemap.xml` 200
- `/api`, `/docs`, OpenAPI probes: 404 at root

### Tier 2: Manual Investigation

| Check | Status | Notes |
|-------|--------|-------|
| Privacy policy exists | ❓ Unknown | Not on root paths tested |
| Terms of service | ❓ Unknown |
| Legal entity identified | ❓ Unknown |
| Data collection disclosed | ⚠️ Partial | CSP references Google Analytics/Intercom/Stripe/Reddit/Facebook (implies trackers/integrations) |
| Publisher verification documented | ❓ Unknown |
| Moderation policy public | ❓ Unknown |
| Report button | ❓ Unknown |
| Vulnerability disclosure policy | ❓ Unknown |
| Badge criteria/process | ❓ Unknown |

### Security Score Summary (qualitative)

Strengths:
- Very strong web security posture (CSP with nonces, HSTS preload, XFO, Referrer-Policy, Permissions-Policy)
- Organized static asset separation (`static.glama.ai`)

Unknowns:
- Marketplace behaviors (provenance, curation, reporting) not visible at root; likely in app

Overall Assessment: Strong baseline web security; marketplace-specific signals need in-app review.

## Notes

New/Interesting:
- CSP includes strict-dynamic and specific third-party domains (Intercom, Stripe, GA), indicating controlled integrations.

## Audit Evidence (2025‑12‑11)

- Command: `python3 security-report/tools/tier1_audit.py https://glama.ai`
- HTTP/security headers: HSTS preload; CSP with nonce; XFO SAMEORIGIN; Referrer-Policy strict-origin-when-cross-origin; Permissions-Policy populated.
- DNS: Cloudflare NS; dual A and AAAA.

### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 103
- Provider hints: Cloudflare NS
- DNS: A=66.241.124.71, 37.16.29.120; CNAME=-; NS=isaac.ns.cloudflare.com., davina.ns.cloudflare.com.
- Security headers: HSTS=max-age=31536000; includeSubDomains; preload, XFO=SAMEORIGIN, XCTO=nosniff
- Mixed content: http_subresources=0; http_literals=0
- Policy endpoints 200: /robots.txt, /sitemap.xml
- API endpoints 200: (none)
- Social links detected: 0 (showing up to 5)

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.
