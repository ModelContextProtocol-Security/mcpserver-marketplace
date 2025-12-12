---
title: "Claude Desktop Extensions Directory"
url: "https://www.anthropic.com/engineering/desktop-extensions"
source_code_url: ""
is_marketplace: yes
is_aggregator: no
is_list_of_marketplaces: no
language: ""
type: ""
evidence:
  - url: "https://www.anthropic.com/engineering/desktop-extensions"
    description: "Homepage / primary listing"
last_evaluated: "2025-12-11"
  - url: "https://www.anthropic.com/engineering/desktop-extensions/robots.txt"
    description: "/robots.txt 200"
  - url: "https://www.anthropic.com/engineering/desktop-extensions/sitemap.xml"
    description: "/sitemap.xml 200"
  - url: "https://www.anthropic.com/engineering/desktop-extensions/robots.txt"
    description: "/robots.txt 200"
  - url: "https://www.anthropic.com/engineering/desktop-extensions/sitemap.xml"
    description: "/sitemap.xml 200"
  - url: "https://www.anthropic.com/engineering/desktop-extensions/robots.txt"
    description: "/robots.txt 200"
  - url: "https://www.anthropic.com/engineering/desktop-extensions/sitemap.xml"
    description: "/sitemap.xml 200"
---

# Claude Desktop Extensions Directory

## Overview
Anthropic’s official engineering page for Desktop Extensions (built-in marketplace). Documents how to build/submit extensions and links to `anthropics/dxt` examples.

## Features
- Discovery/search: Yes (built-in to Claude Desktop, documented on site)
- One‑click install: Yes (mcpb bundles and in-app directory)
- Curated list/recommendations: Yes (official curation by Anthropic)
- API: N/A (docs page; no API at this URL)
- Client integration: Claude Desktop

## Marketplace Classification (Tier 0)

Type: client-embedded (official, vendor-operated)

Discovery & Metadata Delivery:
- Docs: https://www.anthropic.com/engineering/desktop-extensions
- Repo: `anthropics/dxt` (linked from page)

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 200` via Cloudflare |
| TLS/security headers | ✅ Strong | HSTS preload; CSP with nonce; XFO SAMEORIGIN; `nosniff` |
| No mixed content | ⚠️ Minor | 1 HTTP subresource and a few http literals detected |
| Contact/Legal | ✅ Yes | Corporate site; policy pages elsewhere on anthropic.com |

DNS/Hosting:
- NS: Cloudflare (randy/isla); A/AAAA Anthropic infra
- Provider: Cloudflare CDN

## Notes

New/Interesting:
- The page links to `anthropics/dxt` MANIFEST and examples; useful for provenance and submission references.

### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 200
- Provider hints: Cloudflare (Server header), Cloudflare (cf-ray), Cloudflare NS
- DNS: A=160.79.104.10; CNAME=-; NS=randy.ns.cloudflare.com., isla.ns.cloudflare.com.
- Security headers: HSTS=max-age=63072000; includeSubDomains; preload, XFO=SAMEORIGIN, XCTO=nosniff
- Mixed content: http_subresources=1; http_literals=3
- Policy endpoints 200: /robots.txt, /sitemap.xml
- API endpoints 200: (none)
- Social links detected: 17 (showing up to 5)
  - x: 
  - github: https://github.com/anthropics/dxt/blob/main/MANIFEST.md
  - github: https://github.com/your-username/my-mcp-extension&quot;
  - github: https://github.com/your-username/my-extension/issues&quot;,
  - github: https://github.com/anthropics/dxt/tree/main/examples

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.


### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 103
- Provider hints: Cloudflare (Server header), Cloudflare (cf-ray), Cloudflare NS
- DNS: A=160.79.104.10; CNAME=-; NS=randy.ns.cloudflare.com., isla.ns.cloudflare.com.
- Security headers: HSTS=max-age=63072000; includeSubDomains; preload, XFO=SAMEORIGIN, XCTO=nosniff
- Mixed content: http_subresources=1; http_literals=3
- Policy endpoints 200: /robots.txt, /sitemap.xml
- API endpoints 200: (none)
- Social links detected: 17 (showing up to 5)
  - x: 
  - github: https://github.com/anthropics/dxt/blob/main/MANIFEST.md
  - github: https://github.com/your-username/my-mcp-extension&quot;
  - github: https://github.com/your-username/my-extension/issues&quot;,
  - github: https://github.com/anthropics/dxt/tree/main/examples

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.


### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 103
- Provider hints: Cloudflare (Server header), Cloudflare (cf-ray), Cloudflare NS
- DNS: A=160.79.104.10; CNAME=-; NS=randy.ns.cloudflare.com., isla.ns.cloudflare.com.
- Security headers: HSTS=max-age=63072000; includeSubDomains; preload, XFO=SAMEORIGIN, XCTO=nosniff
- Mixed content: http_subresources=1; http_literals=3
- Policy endpoints 200: /robots.txt, /sitemap.xml
- API endpoints 200: (none)
- Social links detected: 17 (showing up to 5)
  - x: 
  - github: https://github.com/anthropics/dxt/blob/main/MANIFEST.md
  - github: https://github.com/your-username/my-mcp-extension&quot;
  - github: https://github.com/your-username/my-extension/issues&quot;,
  - github: https://github.com/anthropics/dxt/tree/main/examples

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.
