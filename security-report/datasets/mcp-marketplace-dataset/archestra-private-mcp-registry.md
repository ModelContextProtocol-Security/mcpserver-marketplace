---
title: "Archestra Private MCP Registry"
url: "https://archestra.ai/docs/platform-private-registry"
source_code_url: "https://github.com/archestra-ai/archestra"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: ""
type: ""
evidence:
  - url: "https://archestra.ai/docs/platform-private-registry"
    description: "Homepage / primary listing"
last_evaluated: "2025-12-11"
  - url: "https://archestra.ai/docs/platform-private-registry/privacy"
    description: "/privacy 200"
  - url: "https://archestra.ai/docs/platform-private-registry/terms"
    description: "/terms 200"
  - url: "https://archestra.ai/docs/platform-private-registry/about"
    description: "/about 200"
  - url: "https://archestra.ai/docs/platform-private-registry/robots.txt"
    description: "/robots.txt 200"
  - url: "https://archestra.ai/docs/platform-private-registry/sitemap.xml"
    description: "/sitemap.xml 200"
  - url: "https://archestra.ai/docs/platform-private-registry/privacy"
    description: "/privacy 200"
  - url: "https://archestra.ai/docs/platform-private-registry/terms"
    description: "/terms 200"
  - url: "https://archestra.ai/docs/platform-private-registry/about"
    description: "/about 200"
  - url: "https://archestra.ai/docs/platform-private-registry/robots.txt"
    description: "/robots.txt 200"
  - url: "https://archestra.ai/docs/platform-private-registry/sitemap.xml"
    description: "/sitemap.xml 200"
  - url: "https://archestra.ai/docs/platform-private-registry/privacy"
    description: "/privacy 200"
  - url: "https://archestra.ai/docs/platform-private-registry/terms"
    description: "/terms 200"
  - url: "https://archestra.ai/docs/platform-private-registry/about"
    description: "/about 200"
  - url: "https://archestra.ai/docs/platform-private-registry/robots.txt"
    description: "/robots.txt 200"
  - url: "https://archestra.ai/docs/platform-private-registry/sitemap.xml"
    description: "/sitemap.xml 200"
  - url: "https://archestra.ai/docs/platform-private-registry/privacy"
    description: "/privacy 200"
  - url: "https://archestra.ai/docs/platform-private-registry/terms"
    description: "/terms 200"
  - url: "https://archestra.ai/docs/platform-private-registry/about"
    description: "/about 200"
  - url: "https://archestra.ai/docs/platform-private-registry/robots.txt"
    description: "/robots.txt 200"
  - url: "https://archestra.ai/docs/platform-private-registry/sitemap.xml"
    description: "/sitemap.xml 200"
---

# Archestra Private MCP Registry

## Overview
Vendor documentation page describing a private MCP registry within the Archestra platform. Vercel-hosted docs; many example http:// literals in text.

## Features
- Discovery/search: N/A (docs page)
- API: Describes platform endpoints and config

## Marketplace Classification (Tier 0)

Type: informational (vendor documentation)

Discovery & Metadata Delivery:
- Docs: https://archestra.ai/docs/platform-private-registry
- Repo: https://github.com/archestra-ai/archestra

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 200` |
| TLS/security headers | ⚠️ Partial | HSTS set; CSP/XFO/XCTO not observed at root |
| No mixed content | ✅ Yes | http:// literals are examples; no subresources detected |
| Contact/Legal | ✅ Yes | `/privacy`, `/terms`, `/about`, robots/sitemap present |

DNS/Hosting:
- NS: GoDaddy (domaincontrol.com); A: Vercel

## Notes

New/Interesting:
- Rich docs include config snippets and platform endpoint examples; useful for evaluating enterprise/private registry design.

### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 200
- Provider hints: (none)
- DNS: A=216.150.1.193; CNAME=-; NS=ns09.domaincontrol.com., ns10.domaincontrol.com.
- Security headers: HSTS=max-age=63072000, XFO=(missing), XCTO=(missing)
- Mixed content: http_subresources=0; http_literals=13
- Policy endpoints 200: /privacy, /terms, /about, /robots.txt, /sitemap.xml
- API endpoints 200: (none)
- Social links detected: 22 (showing up to 5)
  - github: https://github.com/archestra-ai/archestra
  - github: https://github.com/archestra-ai/archestra/edit/main/docs/pages/platform-private-registry.md
  - github: https://github.com/archestra-ai/archestra/blob/main/platform/helm/values.yaml).\n\n####
  - github: https://github.com/archestra-ai/archestra/issues/720))\n\n###
  - github: https://github.com/archestra-ai/archestra/blob/main/platform/dev/grafana/dashboards/platform.json)\n\n##

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.


### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 200
- Provider hints: (none)
- DNS: A=216.150.1.193; CNAME=-; NS=ns09.domaincontrol.com., ns10.domaincontrol.com.
- Security headers: HSTS=max-age=63072000, XFO=(missing), XCTO=(missing)
- Mixed content: http_subresources=0; http_literals=13
- Policy endpoints 200: /privacy, /terms, /about, /robots.txt, /sitemap.xml
- API endpoints 200: (none)
- Social links detected: 22 (showing up to 5)
  - github: https://github.com/archestra-ai/archestra
  - github: https://github.com/archestra-ai/archestra/edit/main/docs/pages/platform-private-registry.md
  - github: https://github.com/archestra-ai/archestra/blob/main/platform/helm/values.yaml).\n\n####
  - github: https://github.com/archestra-ai/archestra/issues/720))\n\n###
  - github: https://github.com/archestra-ai/archestra/blob/main/platform/dev/grafana/dashboards/platform.json)\n\n##

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.


### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 200
- Provider hints: (none)
- DNS: A=216.150.1.193; CNAME=-; NS=ns09.domaincontrol.com., ns10.domaincontrol.com.
- Security headers: HSTS=max-age=63072000, XFO=(missing), XCTO=(missing)
- Mixed content: http_subresources=0; http_literals=13
- Policy endpoints 200: /privacy, /terms, /about, /robots.txt, /sitemap.xml
- API endpoints 200: (none)
- Social links detected: 22 (showing up to 5)
  - github: https://github.com/archestra-ai/archestra
  - github: https://github.com/archestra-ai/archestra/edit/main/docs/pages/platform-private-registry.md
  - github: https://github.com/archestra-ai/archestra/blob/main/platform/helm/values.yaml).\n\n####
  - github: https://github.com/archestra-ai/archestra/issues/720))\n\n###
  - github: https://github.com/archestra-ai/archestra/blob/main/platform/dev/grafana/dashboards/platform.json)\n\n##

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.


### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 200
- Provider hints: (none)
- DNS: A=216.150.1.193; CNAME=-; NS=ns09.domaincontrol.com., ns10.domaincontrol.com.
- Security headers: HSTS=max-age=63072000, XFO=(missing), XCTO=(missing)
- Mixed content: http_subresources=0; http_literals=13
- Policy endpoints 200: /privacy, /terms, /about, /robots.txt, /sitemap.xml
- API endpoints 200: (none)
- Social links detected: 22 (showing up to 5)
  - github: https://github.com/archestra-ai/archestra
  - github: https://github.com/archestra-ai/archestra/edit/main/docs/pages/platform-private-registry.md
  - github: https://github.com/archestra-ai/archestra/blob/main/platform/helm/values.yaml).\n\n####
  - github: https://github.com/archestra-ai/archestra/issues/720))\n\n###
  - github: https://github.com/archestra-ai/archestra/blob/main/platform/dev/grafana/dashboards/platform.json)\n\n##

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.
