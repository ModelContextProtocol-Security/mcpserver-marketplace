---
title: "MCP.so"
url: "https://mcp.so"
source_code_url: "https://github.com/chatmcp/mcpso"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en, zh, ja"
type: "directory"
operator: "❓ Unknown"
contact_email: "support@mcp.so"
last_evaluated: "2025-12-11"
evidence:
  - url: "https://mcp.so"
    description: "Homepage / primary listing"
  - url: "https://mcp.so/zh"
    description: "Chinese locale"
  - url: "https://mcp.so/ja"
    description: "Japanese locale"
  - url: "https://github.com/chatmcp/mcpso"
    description: "Source code repository (project)"
  - url: "https://www.googletagmanager.com/gtag/js?id=G-9ZWF7FKDR8"
    description: "Google Analytics present"
  - url: "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"
    description: "Google AdSense present"
  - url: "https://mcp.so/privacy-policy"
    description: "Privacy policy present; contact email support@mcp.so"
  - url: "https://mcp.so/robots.txt"
    description: "robots.txt present"
  - url: "https://mcp.so/sitemap.xml"
    description: "sitemap.xml present"
---

# MCP.so

## Overview
MCP.so is a public directory/aggregator of MCP servers. The homepage advertises "The largest collection of MCP Servers" and provides multilingual UI (EN/ZH/JA). It appears to surface repositories and hosted servers from multiple sources, enabling search and discovery.

## Features
- Discovery/search: Yes (search UI on homepage)
- One‑click install: ❓ Unknown (no explicit one‑click buttons observed on homepage)
- Curated list/recommendations: ❓ Unknown (no curation policy disclosed)
- API: ❓ Unknown (no public API link detected)
- Client integration: ❓ Unknown (no client-specific install workflows observed)

## Marketplace Classification (Tier 0)

Type: code-linking (directory/aggregator)

Discovery & Metadata Delivery:
- Website: https://mcp.so (present)
- Registry API: none discovered (see notes below)
- CLI: none found
- IDE plugin: none found
- Client integration: ❓ Unknown
- Browser extension: none found

Code/Server Delivery:
- Link to source: Yes (links to external GitHub repos)
- Local installation via CLI: ❓ Unknown
- Package download: ❓ Unknown
- Hosted execution (PaaS/SaaS): ❓ Unknown (no evidence surfaced on site)
- Container image: ❓ Unknown
- Source bundle: ❓ Unknown

Source Accessibility:
- Marketplace source code: https://github.com/chatmcp/mcpso
- API docs: none found
- Self-hostable: ❓ Unknown

Server Coverage:
- Lists vendor-hosted servers: No evidence (did not find mcp.vercel.com, mcp.ramp.com, huggingface.co/mcp, etc.)
- Distinguishes hosted vs local: ❓ Unknown
- Vendor-hosted servers found: none

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 200`; all primary pages over HTTPS |
| TLS certificate | ✅ Yes | Served via Cloudflare; edge-terminated TLS |
| No mixed content | ✅ Yes | No HTTP subresource loads detected (0); some `http://` literals appear as text/examples |
| Security headers | ❌ No | No HSTS/CSP/XFO/XCTO/Referrer-Policy/Permissions-Policy observed |
| Contact information | ✅ Yes | Privacy policy provides support@mcp.so |
| Issue tracker | ⚠️ Partial | Project repo exists (`chatmcp/mcpso`), but site-specific issue reporting not linked from UI |
| Provenance visible | ❓ Unknown | Homepage listings not validated here for author/source per item |
| Official vs third‑party distinction | ❓ Unknown | No badge/legend observed on homepage |
| Last updated timestamps | ❓ Unknown | Not confirmed on homepage |

API/Docs Discovery:
- `/api`, `/docs`, `/api-docs`: 404
- `/openapi.json`, `/openapi.yaml`, `/swagger.json`: 200 but serve app shell (HTML), not API specs (likely framework catch-all). Treat as not present.

DNS/CDN and Hosting:
- A/AAAA: 104.21.40.140, 172.67.186.229; 2606:4700:3031::6815:288c, 2606:4700:3033::ac43:bae5
- NS: `graham.ns.cloudflare.com`, `ullis.ns.cloudflare.com`
- Headers: `server: cloudflare`, `cf-ray` present
- Provider: Cloudflare (edge/CDN + DNS)

Third‑Party Integrations:
- Google Tag Manager / Google Analytics (`gtag/js?id=G-9ZWF7FKDR8`)
- Google AdSense (pagead2.g.doubleclick.net JS)
- Google Fonts (fonts.googleapis.com/gstatic)

### Tier 2: Manual Investigation

| Check | Status | Notes |
|-------|--------|-------|
| Privacy policy exists | ✅ Yes | `/privacy-policy` present (Last updated: 2024‑12‑06) |
| Terms of service | ❌ No | `/terms` and `/tos` return 404 |
| Legal entity identified | ❓ Unknown | Not stated in policy text captured |
| Data collection disclosed | ⚠️ Partial | Policy describes collection; GA + AdSense present |
| Publisher verification documented | ❓ Unknown | No submission/verification docs found |
| Moderation policy public | ❓ Unknown | Not found |
| Report button | ❌ No | No visible per‑listing report UI detected |
| Vulnerability disclosure policy | ❌ No | No `/security` or SECURITY.md linked |
| Badge criteria/process | ❓ Unknown | No badge documentation found |

### Tier 3: Registry‑Specific (if hosting/publishing)

| Check | Status | Notes |
|-------|--------|-------|
| 2FA required for publishers | N/A | Directory/aggregator; not confirmed as a publishing registry |
| Token scopes/expiry | N/A | — |
| Malware/dependency scanning | N/A | — |
| Namespace/typosquatting protection | ❓ Unknown | Naming/namespace rules not documented |
| Runtime sandboxing | N/A | Does not host builds/servers (appears directory-only) |
| Package signing/provenance | N/A | — |

### Security Score Summary (qualitative)

Strengths:
- HTTPS with reputable CDN (Cloudflare)
- Multilingual access broadens reach (EN/ZH/JA)

Weaknesses:
- No visible terms/security pages despite presence of third‑party tracking
- No report/takedown channel surfaced
- No documentation of provenance, verification, or moderation
- Unknown curation or API support
- Missing baseline security headers (HSTS/CSP/etc.)
- Apparent "ghost" API endpoints (200 HTML for openapi/swagger paths)

Overall Assessment: Limited transparency on policy, provenance, and reporting. Treat as a directory with minimal surfaced security posture until more documentation is published.

## Notes

- Mixed content note: the homepage HTML contains `http://` strings such as `http://myproxy` and internal service examples; these appear to be textual/code references rather than active subresource loads. Browsers typically do not flag this as mixed content.
- Source repository exists, but the operational website does not link a security or reporting channel.
- Consider adding contact, privacy, and disclosure links to improve baseline trust signals.
- Social: Discord invites are present in page content; no official Twitter/X link detected.
- robots.txt and sitemap.xml present and accessible.

## Delivery Method Security

- Website: Served via Cloudflare; no HSTS/CSP/XFO/etc. observed; GA + AdSense present; privacy policy exists at `/privacy-policy` with support email.
- API: No documented API. Probing common OpenAPI/Swagger endpoints returns app HTML (likely catch‑all) rather than specs.
- CLI: None discovered.
- Client Integration: ❓ Unknown (no direct client consumption documented).

## Vendor‑Hosted Coverage Test

How tested:
- Searched homepage HTML for vendor‑hosted patterns: `mcp.vercel.com`, `mcp.ramp.com`, `huggingface.co/mcp`, `stripe.`, `linear.`, `cloudflare` + `mcp`.

Result: No vendor‑hosted endpoints referenced on homepage.

## Red Flags

- Missing baseline security headers (HSTS/CSP/X-Frame-Options/X-Content-Type-Options).
- Ghost API endpoints respond 200 with HTML for `/openapi.json|yaml` and `/swagger.json`.
- No visible ToS or security/vuln disclosure page.
- No report/takedown mechanism surfaced for specific listings.

## Recommendations

For Operator:
- Add HSTS, CSP (with nonces), X-Frame-Options, X-Content-Type-Options, Referrer-Policy, and Permissions-Policy.
- Publish ToS and a SECURITY.md/vulnerability disclosure page; add a report button per listing.
- If badges exist, document criteria and process. Surface provenance (author, repo/org verification) prominently.
- Remove/correct ghost API endpoints or serve actual OpenAPI specs if an API exists.
- Disclose tracking and third‑party sharing clearly; consider minimizing ad/analytics on dev‑focused pages.

For Users:
- Treat listings as pointers; vet the linked GitHub org (verified badge, SECURITY.md, maintenance). Prefer official vendor‑hosted MCP servers when available.
- Avoid assuming a listing is vetted; check permissions/runtime guidance in your client and run with least privilege.

## Audit Evidence (2025‑12‑11)

- Command: `python3 security-report/tools/tier1_audit.py https://mcp.so`
- HTTP: status chain `HTTP/2 200`; `server: cloudflare`; `cf-ray` present.
- Security headers: none observed (HSTS/CSP/XFO/XCTO/Referrer-Policy/Permissions-Policy all null).
- DNS: NS=`graham.ns.cloudflare.com`, `ullis.ns.cloudflare.com`; A/AAAA in Cloudflare ranges. Provider hints: Cloudflare.
- Mixed content: 0 HTTP subresources; ~30 `http://` literals (text/examples).
- Policy endpoints: `/privacy-policy` 200 (last updated: 2024‑12‑06); `/terms` 404; `/tos` 404; `/security` 404; `/robots.txt` 200; `/sitemap.xml` 200.
- API probes: `/api` 404; `/docs` 404; `/api-docs` 404; `/openapi.json|yaml` 200 (HTML app shell); `/swagger.json` 200 (HTML app shell).
- Social/contact: Discord invites detected (e.g., https://discord.gg/RsYPRrnyqg, https://discord.gg/wez8HtpxqQ, https://discord.gg/vapESyrFmJ, https://discord.gg/cline, https://discord.com/invite/nwu9ANqAf5). No official X/Twitter link detected. Repo issues link present (https://github.com/chatmcp/mcpso/issues).
