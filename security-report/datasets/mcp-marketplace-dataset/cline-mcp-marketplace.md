---
title: "Cline MCP Marketplace"
url: "https://cline.bot/mcp-marketplace"
source_code_url: "https://github.com/cline/mcp-marketplace"
is_marketplace: yes
is_aggregator: no
is_list_of_marketplaces: no
language: ""
type: ""
evidence:
  - url: "https://cline.bot/mcp-marketplace"
    description: "Homepage / primary listing"
last_evaluated: "2025-12-11"
  - url: "https://cline.bot/mcp-marketplace/privacy"
    description: "/privacy 200"
  - url: "https://cline.bot/mcp-marketplace/tos"
    description: "/tos 200"
  - url: "https://cline.bot/mcp-marketplace/contact"
    description: "/contact 200"
  - url: "https://cline.bot/mcp-marketplace/robots.txt"
    description: "/robots.txt 200"
  - url: "https://cline.bot/mcp-marketplace/sitemap.xml"
    description: "/sitemap.xml 200"
  - url: "https://cline.bot/mcp-marketplace/privacy"
    description: "/privacy 200"
  - url: "https://cline.bot/mcp-marketplace/tos"
    description: "/tos 200"
  - url: "https://cline.bot/mcp-marketplace/contact"
    description: "/contact 200"
  - url: "https://cline.bot/mcp-marketplace/robots.txt"
    description: "/robots.txt 200"
  - url: "https://cline.bot/mcp-marketplace/sitemap.xml"
    description: "/sitemap.xml 200"
  - url: "https://cline.bot/mcp-marketplace/privacy"
    description: "/privacy 200"
  - url: "https://cline.bot/mcp-marketplace/tos"
    description: "/tos 200"
  - url: "https://cline.bot/mcp-marketplace/contact"
    description: "/contact 200"
  - url: "https://cline.bot/mcp-marketplace/robots.txt"
    description: "/robots.txt 200"
  - url: "https://cline.bot/mcp-marketplace/sitemap.xml"
    description: "/sitemap.xml 200"
---

# Cline MCP Marketplace

## Overview
Cline’s marketplace on `cline.bot` lists MCP servers for the Cline client. Hosted on Vercel (Next.js). Provides privacy, TOS, contact pages.

## Features
- Discovery/search: Yes (marketplace page)
- One‑click install: ❓ Unknown (Cline client integration assumed)
- Curated list/recommendations: Yes (curated marketplace content)
- API: No public API at root (`/api` 404)
- Client integration: Yes (for Cline)

## Marketplace Classification (Tier 0)

Type: client-embedded (web marketplace for Cline)

Discovery & Metadata Delivery:
- Website: https://cline.bot/mcp-marketplace (Vercel)
- Policy pages: `/privacy`, `/tos`, `/contact` present

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 200` |
| TLS/security headers | ⚠️ Partial | HSTS set; CSP/XFO/XCTO not observed at root |
| No mixed content | ✅ Yes | No HTTP subresource loads; http:// literals in code/examples only |
| Contact/Legal | ✅ Yes | `/privacy`, `/tos`, `/contact` 200 |

DNS/Hosting:
- A: 76.76.21.21 (Vercel); NS: Google Domains
- Provider: Vercel (x-vercel-id)

Policy/API Endpoints:
- Privacy/TOS/Contact/robots/sitemap present
- API probes: 404

## Notes

New/Interesting:
- Many Discord invite links embedded (community-driven marketplace feel)
- http:// literals include dev placeholders (e.g., `0.0.0.0:<port>`, `host.docker.internal`) — not active subresources.

### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 200
- Provider hints: (none)
- DNS: A=76.76.21.21; CNAME=-; NS=ns-cloud-c3.googledomains.com., ns-cloud-c4.googledomains.com., ns-cloud-c1.googledomains.com.
- Security headers: HSTS=max-age=63072000, XFO=(missing), XCTO=(missing)
- Mixed content: http_subresources=0; http_literals=10
- Policy endpoints 200: /privacy, /tos, /contact, /robots.txt, /sitemap.xml
- API endpoints 200: (none)
- Social links detected: 724 (showing up to 5)
  - discord: https://discord.gg/cline
  - discord: https://discord.gg/Dmm69peqjh
  - discord: https://discord.gg/GQrFB3Ec3W
  - discord: https://discord.gg/ES2rDhBJt3
  - discord: https://discord.gg/MMeYNTmh3x

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.


### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 200
- Provider hints: (none)
- DNS: A=76.76.21.21; CNAME=-; NS=ns-cloud-c3.googledomains.com., ns-cloud-c4.googledomains.com., ns-cloud-c1.googledomains.com.
- Security headers: HSTS=max-age=63072000, XFO=(missing), XCTO=(missing)
- Mixed content: http_subresources=0; http_literals=10
- Policy endpoints 200: /privacy, /tos, /contact, /robots.txt, /sitemap.xml
- API endpoints 200: (none)
- Social links detected: 724 (showing up to 5)
  - discord: https://discord.gg/cline
  - discord: https://discord.gg/Dmm69peqjh
  - discord: https://discord.gg/GQrFB3Ec3W
  - discord: https://discord.gg/ES2rDhBJt3
  - discord: https://discord.gg/MMeYNTmh3x

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.


### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 200
- Provider hints: (none)
- DNS: A=76.76.21.21; CNAME=-; NS=ns-cloud-c3.googledomains.com., ns-cloud-c4.googledomains.com., ns-cloud-c1.googledomains.com.
- Security headers: HSTS=max-age=63072000, XFO=(missing), XCTO=(missing)
- Mixed content: http_subresources=0; http_literals=10
- Policy endpoints 200: /privacy, /tos, /contact, /robots.txt, /sitemap.xml
- API endpoints 200: (none)
- Social links detected: 724 (showing up to 5)
  - discord: https://discord.gg/cline
  - discord: https://discord.gg/Dmm69peqjh
  - discord: https://discord.gg/GQrFB3Ec3W
  - discord: https://discord.gg/ES2rDhBJt3
  - discord: https://discord.gg/MMeYNTmh3x

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.
