---
title: "MCP Market"
url: "https://mcpmarket.com"
source_code_url: ""
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: ""
type: ""
evidence:
  - url: "https://mcpmarket.com"
    description: "Homepage / primary listing"
---

# MCP Market

## Overview
Domain is Vercel-hosted but currently returns 403 for all paths (including root). Content may be restricted or not deployed.

## Features
- Discovery/search: ❌ Unavailable (403)
- One‑click install: ❌ Unavailable (403)
- Curated list/recommendations: ❌ Unavailable (403)
- API: ❌ Unavailable (403)

## Marketplace Classification (Tier 0)

Type: ❓ Unknown (site inaccessible)

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ⚠️ Partial | `HTTP/2 403` at root |
| TLS/security headers | ❌ Missing | No HSTS/CSP/XFO/XCTO observed (403 minimal response) |
| No mixed content | ✅ Yes | 0 HTTP subresource loads |

DNS/Hosting:
- NS: `ns1.vercel-dns.com`, `ns2.vercel-dns.com` (Vercel DNS)
- A: 216.150.16.65, 216.150.1.129
- Provider: Vercel (x-vercel-id)

Policy/API Endpoints:
- All tested paths return 403

## Notes

Problem/Blocker:
- Site currently returns 403 for root and common paths. Unable to evaluate further. Revisit later.

## Audit Evidence (2025‑12‑11)

- Command: `python3 security-report/tools/tier1_audit.py https://mcpmarket.com`
- HTTP: `HTTP/2 403`; Vercel headers present; all policy/API probes 403.
