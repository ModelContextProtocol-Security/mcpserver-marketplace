---
title: "mcp.run"
url: "https://mcp.run"
source_code_url: ""
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "directory / aggregator"
operator: "❓ Unknown (Cloudflare; Framer hosting on www subdomain)"
contact_email: "sales@dylibso.ai (found in HTML links)"
last_evaluated: "2025-12-11"
evidence:
  - url: "https://mcp.run"
    description: "Homepage; redirects to https://www.mcp.run/ (Cloudflare + Framer)"
  - url: "https://www.mcp.run/"
    description: "Redirect target"
---

# mcp.run

## Overview
Public MCP directory/aggregator hosted behind Cloudflare with redirect to `www.mcp.run` (appears to be a Framer-hosted site from headers). Limited signals on the landing suggest a list-style resource rather than a fully documented registry.

## Features
- Discovery/search: ❓ Unknown
- One‑click install: ❓ Unknown
- Curated list/recommendations: ❓ Unknown
- API: ❓ Unknown
- Client integration: ❓ Unknown

## Marketplace Classification (Tier 0)

Type: directory/aggregator (assessed from domain and behavior; limited metadata surfaced)

Discovery & Metadata Delivery:
- Website: https://mcp.run (redirects to https://www.mcp.run/)
- Registry API: ❓ Unknown (no endpoints discovered at root)
- CLI/IDE integration: ❓ Unknown

Code/Server Delivery:
- Link to source: ❓ Unknown
- Local installation: ❓ Unknown
- Hosted execution: ❓ Unknown

Source Accessibility:
- Marketplace source code: ❓ Unknown
- API docs: ❓ Unknown
- Self-hostable: ❓ Unknown

Server Coverage:
- Lists vendor-hosted servers: ❓ Unknown
- Distinguishes hosted vs local: ❓ Unknown
- Vendor-hosted servers found: ❓ Unknown

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 301` to `https://www.mcp.run/` |
| TLS/security headers | ✅ Partial | HSTS and `nosniff` present via Cloudflare; CSP/XFO not observed |
| No mixed content | ✅ Yes | 0 HTTP subresource loads detected |
| Contact information | ⚠️ Minimal | `mailto:sales@dylibso.ai` appears in extracted links; no contact page at root |
| Issue tracker | ❓ Unknown | No repo linked on landing |
| Provenance visible | ❓ Unknown | No per-listing provenance observed (landing minimal) |
| Official vs third‑party | ❓ Unknown | No badges observed |
| Timestamps | ❓ Unknown | Not present on landing |

DNS/CDN and Hosting:
- A/AAAA: Cloudflare edges (104.26.x.x, 172.67.72.180; IPv6 present)
- NS: `ada.ns.cloudflare.com`, `drew.ns.cloudflare.com`
- Headers: Cloudflare; `server-timing` shows `region=us-west-2`, `framerusercontent.com` preconnect links (Framer hosting)

Policy/API Endpoints at root:
- All tested root paths return 301 redirect to `www` subdomain (privacy/terms/security/robots, and `/api`/OpenAPI probes)

### Tier 2: Manual Investigation

| Check | Status | Notes |
|-------|--------|-------|
| Privacy policy exists | ❓ Unknown | Redirect to `www`; policy path not surfaced |
| Terms of service | ❓ Unknown | — |
| Legal entity identified | ❓ Unknown | — |
| Data collection disclosed | ❓ Unknown | — |
| Publisher verification documented | ❓ Unknown | — |
| Moderation policy public | ❓ Unknown | — |
| Report button | ❓ Unknown | — |
| Vulnerability disclosure policy | ❓ Unknown | — |
| Badge criteria/process | ❓ Unknown | — |

### Security Score Summary (qualitative)

Strengths:
- Cloudflare fronting; HSTS and `nosniff` at root; Framer hosting suggests modern delivery infra

Unknowns:
- Purpose, operator, and security/maturity are not visible from landing; all key policy/API paths redirect

Overall Assessment: Insufficient public signals on landing. Treat as experimental directory; needs explicit policy pages, provenance, and reporting channels.

## Notes

New/Interesting:
- Redirect to `www.mcp.run` with Framer signals in headers (preconnect to `framerusercontent.com`).

## Audit Evidence (2025‑12‑11)

- Command: `python3 security-report/tools/tier1_audit.py https://mcp.run`
- HTTP: `HTTP/2 301` to `https://www.mcp.run/`; HSTS `max-age=31536000`; `x-content-type-options: nosniff`.
- DNS: Cloudflare A/AAAA; NS `ada`/`drew` (Cloudflare).
- Paths: All tested policy and API paths return 301 to `www`.
