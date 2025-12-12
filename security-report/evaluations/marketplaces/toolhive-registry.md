---
title: "ToolHive Registry"
url: "https://toolhive.dev"
source_code_url: "https://github.com/stacklok/toolhive"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "api-gateway + client + registry"
operator: "Stacklok, Inc."
contact_email: "hello@stacklok.com"
last_evaluated: "2025-12-11"
evidence:
  - url: "https://toolhive.dev"
    description: "Homepage / primary listing (Cloudflare CDN; Kinsta WP hosting)"
  - url: "https://github.com/stacklok/toolhive"
    description: "ToolHive repo (client/platform)"
  - url: "https://discord.gg/stacklok"
    description: "Community Discord"
  - url: "https://docs.stacklok.com/toolhive"
    description: "Product documentation"
  - url: "mailto:hello@stacklok.com"
    description: "Contact email (footer/contact section)"
  - url: "https://toolhive.dev/robots.txt"
    description: "robots.txt present"
  - url: "https://toolhive.dev/sitemap.xml"
    description: "sitemap.xml 301 (redirect)"
---

# ToolHive Registry

## Overview
ToolHive is an open source MCP platform with a built-in registry, client (ToolHive Studio), and isolation/runtime controls. It focuses on secure, containerized execution of MCP servers and enterprise features (encrypted secret management, optional 1Password integration, JSON permission profiles, SSE proxy).

## Features
- Discovery/search: Yes (built-in registry UI in ToolHive)
- One‑click install: Yes (download installers; one‑click deploy in containers)
- Curated list/recommendations: Yes (vetted servers highlighted; examples shown)
- API: ❓ Unknown (no public registry API endpoints documented on site)
- Client integration: Yes (supports VS Code/Copilot, Cursor, Roo Code, Cline, Claude Code via auto-config or SSE)

## Marketplace Classification (Tier 0)

Type: hybrid (api-gateway + client + registry)

Discovery & Metadata Delivery:
- Website: https://toolhive.dev
- Registry API: ❓ Unknown
- CLI/Client: ToolHive Studio downloads (macOS/Windows/Linux)
- IDE integration: VS Code (Copilot v1.99+), Cursor, Roo Code, Cline, Claude Code
- Docs: https://docs.stacklok.com/toolhive

Code/Server Delivery:
- Link to source: Yes (ToolHive repo; servers referenced in docs/examples)
- Local installation via client: Yes (containerized)
- Package download: Installers (.dmg/.exe/.deb/.rpm)
- Hosted execution (PaaS/SaaS): No (local containers; SSE proxy)
- Container image: Yes (runs MCP servers as containers)
- Source bundle: N/A

Source Accessibility:
- Marketplace/client source: https://github.com/stacklok/toolhive (open source)
- API docs: ❓ Unknown
- Self-hostable: Client is installable; registry gateway status not determined here

Server Coverage:
- Lists vendor-hosted servers: ❓ Unknown on website; examples include common MCPs (GitHub/OSV/Kubernetes/etc.)
- Distinguishes hosted vs local: Yes (local containerization model)
- Vendor-hosted servers found: Not highlighted on homepage

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 200` via Cloudflare |
| TLS certificate | ✅ Yes | Cloudflare edge |
| No mixed content | ✅ Yes | 0 HTTP subresource loads detected |
| Security headers | ⚠️ Partial | `X-Content-Type-Options: nosniff`; HSTS/CSP/XFO not observed |
| Contact information | ✅ Yes | `mailto:hello@stacklok.com` in contact section |
| Issue tracker | ✅ Yes | GitHub repo for ToolHive |
| Provenance visible | ⚠️ Partial | Open source client; registry curation/vetting language on site |
| Official vs third‑party distinction | ⚠️ Partial | “Vetted MCP servers” messaging; criteria not detailed on homepage |
| Last updated timestamps | ❓ Unknown | Not displayed on homepage; site uses Kinsta and Cloudflare caching headers |

DNS/CDN and Hosting:
- A: 162.159.134.42 (Cloudflare Anycast)
- NS: AWS Route 53 (ns-138.awsdns-17.com, etc.)
- Headers: `server: cloudflare`; Kinsta cache headers present
- Provider: Cloudflare CDN; origin likely Kinsta (managed WP)

Third‑Party/Privacy Controls:
- Iubenda cookie/privacy solution embedded (cookiePolicyId present) on homepage

API/Docs Discovery:
- `/api`, `/docs`, `/api-docs`: 404
- `/openapi.yaml`: 403; `/openapi.json`, `/swagger.json`: 404 (no public API specs at root)

### Tier 2: Manual Investigation

| Check | Status | Notes |
|-------|--------|-------|
| Privacy policy exists | ⚠️ Partial | Cookie/privacy solution present; dedicated policy URL not on root paths tested |
| Terms of service | ❓ Unknown | Not present at root tested paths |
| Legal entity identified | ✅ Yes | Stacklok branding; corporate channels (docs/dev.to/YouTube) |
| Data collection disclosed | ⚠️ Partial | Iubenda integration suggests cookie/privacy management |
| Publisher verification documented | ❓ Unknown | “Vetted” language; exact criteria/process not linked |
| Moderation policy public | ❓ Unknown | Not found on homepage |
| Report button | ❓ Unknown | Support via Discord and GitHub issues |
| Vulnerability disclosure policy | ❓ Unknown | Not surfaced on homepage; likely in org-level policies |
| Badge criteria/process | ❓ Unknown | Not documented on homepage |

### Tier 3: Registry‑Specific (local/containerized execution)

| Check | Status | Notes |
|-------|--------|-------|
| 2FA required for publishers | N/A | Local execution; curated registry details not evaluated here |
| Token scopes/expiry | N/A | — |
| Malware/dependency scanning | ❓ Unknown | Not documented on homepage |
| Namespace/typosquatting protection | ❓ Unknown | — |
| Runtime isolation | ✅ Yes | Claims: container isolation; SSE proxy; minimal permissions |
| Package signing/provenance | ❓ Unknown | Not stated on homepage |

### Security Score Summary (qualitative)

Strengths:
- Emphasis on container isolation and encrypted secret management
- Clear client downloads and supported IDE/client integrations
- Open source client and active community channels (GitHub, Discord)

Weaknesses / Unknowns:
- Missing standard security headers (no HSTS/CSP/XFO observed)
- No public registry API documented at root
- Vetted criteria/process and reporting/takedown details not surfaced

Overall Assessment: Strong client/runtime security posture messaging. Registry aspects (API, curation details) need documentation. Good privacy tooling presence, but baseline web security headers can be improved.

## Notes

New/Interesting:
- Iubenda privacy/cookie controls embedded on the homepage (cookiePolicyId shown in source).
- Cloudflare + Kinsta stack (headers indicate Kinsta cache + Cloudflare CDN).
- Security model claims: container isolation, SSE proxy, encrypted secret vault, JSON permission profiles.

## Delivery Method Security

- Website: Cloudflare CDN, Kinsta origin; `nosniff` set; HSTS/CSP/XFO not observed.
- API: No public registry API at root; docs are hosted on `docs.stacklok.com`.
- Client: Installers for macOS/Windows/Linux; supports multiple MCP clients; secret management integrates with OS keyring/1Password.

## Vendor‑Hosted Coverage Test

How tested:
- Scanned homepage for vendor‑hosted endpoints (vercel, ramp, huggingface/mcp, stripe/linear references) — none highlighted; focus is on running local containerized MCPs.

Result: N/A (local-first model).

## Red Flags

- Missing HSTS/CSP/XFO.
- No public registry API spec surfaced.

## Recommendations

For Operator:
- Add HSTS and CSP; consider X-Frame-Options and Referrer-Policy.
- Publish curation criteria and report/takedown process; link policy/legal pages prominently.
- Document registry API (if public) or clarify local-only model.

For Users:
- Favor least-privilege permission profiles; store secrets in encrypted vault; inspect upstream server repos for maintenance/security posture.

## Audit Evidence (2025‑12‑11)

- Command: `python3 security-report/tools/tier1_audit.py https://toolhive.dev`
- HTTP: `HTTP/2 200`; `server: cloudflare`; Kinsta cache headers; `x-content-type-options: nosniff`.
- DNS: A=162.159.134.42; NS=AWS Route 53; Provider hints: Cloudflare.
- Mixed content: 0 subresources; 0 http literals.
- Paths: `/robots.txt` 200; `/sitemap.xml` 301; policy endpoints at root return 404; privacy managed via Iubenda widget.
- Social/contact: Discord invite present; `mailto:hello@stacklok.com` present; GitHub links to ToolHive repos and releases.
