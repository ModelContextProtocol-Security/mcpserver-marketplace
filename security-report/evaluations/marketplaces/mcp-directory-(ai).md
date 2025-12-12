---
title: "MCP Directory (AI)"
url: "https://mcpdirectory.ai/"
source_code_url: ""
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: ""
type: ""
evidence:
  - url: "https://mcpdirectory.ai/"
    description: "Homepage / primary listing"
last_evaluated: "2025-12-11"
  - url: "https://mcpdirectory.ai/robots.txt"
    description: "/robots.txt 200"
  - url: "https://mcpdirectory.ai/sitemap.xml"
    description: "/sitemap.xml 200"
---

# MCP Directory (AI)

## Overview
AWS CloudFront–backed directory site (Next.js) listing MCP resources. Minimal landing metadata; Discord invite present.

## Features
- Discovery/search: ❓ Unknown
- One‑click install: ❓ Unknown
- Curated list/recommendations: ❓ Unknown
- API: ❓ Unknown
- Client integration: ❓ Unknown

## Marketplace Classification (Tier 0)

Type: directory/aggregator

Discovery & Metadata Delivery:
- Website: https://mcpdirectory.ai/ (CloudFront + Next.js)
- Registry API: ❓ Unknown

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 200` via CloudFront |
| TLS/security headers | ❌ Missing | No HSTS/CSP/XFO/XCTO observed at root |
| No mixed content | ✅ Yes | 0 HTTP subresource loads detected |
| Contact/community | ⚠️ Partial | Discord invite present |

DNS/Hosting:
- A: multiple AWS ranges (3.164.255.x); NS: AWS Route 53
- Provider: AWS CloudFront (X-Cache; x-amz-* headers)

Policy/API Endpoints:
- `/robots.txt` and `/sitemap.xml` 200; other policy paths redirect (308)
- API probes: None observed at root; OpenAPI/Swagger 404

## Notes

New/Interesting:
- Strong CDN caching via CloudFront; Next.js static site behavior.

### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 200
- Provider hints: AWS (x-amz-* headers), AWS CloudFront (X-Cache)
- DNS: A=3.164.255.92, 3.164.255.27, 3.164.255.95; CNAME=-; NS=ns-1021.awsdns-63.net., ns-1525.awsdns-62.org., ns-1899.awsdns-45.co.uk.
- Security headers: HSTS=(missing), XFO=(missing), XCTO=(missing)
- Mixed content: http_subresources=0; http_literals=0
- Policy endpoints 200: /robots.txt, /sitemap.xml
- API endpoints 200: (none)
- Social links detected: 1 (showing up to 5)
  - discord: https://discord.gg/3yhZNa32

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.
