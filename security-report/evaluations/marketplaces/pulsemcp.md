---
title: "PulseMCP"
url: "https://www.pulsemcp.com"
source_code_url: ""
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "directory + news/links"
operator: "❓ Unknown"
contact_email: "hello@pulsemcp.com"
last_evaluated: "2025-12-11"
evidence:
  - url: "https://www.pulsemcp.com"
    description: "Homepage (Rails/CSP-lite headers)"
  - url: "https://www.pulsemcp.com/privacy-policy"
    description: "Privacy policy present"
  - url: "https://www.pulsemcp.com/robots.txt"
    description: "robots.txt 200"
  - url: "https://www.pulsemcp.com/sitemap.xml"
    description: "sitemap.xml 200"
  - url: "https://www.pulsemcp.com/api"
    description: "API path responds 200 (undocumented endpoints)"
  - url: "mailto:hello@pulsemcp.com"
    description: "Contact email"
  - url: "https://discord.gg/dP2evEyTjS"
    description: "Community Discord invite"
---

# PulseMCP

## Overview
PulseMCP aggregates MCP servers, clients, and news. The site appears to be a Rails-backed application with curated links and resources for the MCP ecosystem.

## Features
- Discovery/search: Yes (directory UI)
- One‑click install: ❓ Unknown
- Curated list/recommendations: Yes (curated entries and news)
- API: ⚠️ Partial (root `/api` returns 200; endpoints not documented at root)
- Client integration: ❓ Unknown

## Marketplace Classification (Tier 0)

Type: directory + news/links

Discovery & Metadata Delivery:
- Website: https://www.pulsemcp.com
- Registry API: `/api` 200 (no public docs seen)
- Social/community: Discord invite present; personal GitHub profiles linked

Code/Server Delivery:
- Link to source: ❓ Unknown
- Local installation: ❓ Unknown
- Hosted execution: ❓ Unknown

Source Accessibility:
- Marketplace source: ❓ Unknown
- API docs: ❓ Unknown (root `/api` only)

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 200` |
| TLS/security headers | ✅ Good | HSTS includeSubDomains; XFO SAMEORIGIN; XCTO nosniff; Referrer-Policy strict-origin-when-cross-origin |
| No mixed content | ✅ Yes | 0 HTTP subresource loads detected |
| Contact information | ✅ Yes | `hello@pulsemcp.com` mailto |
| Issue tracker | ❓ Unknown | Not linked on landing |
| Provenance visible | ❓ Unknown | Per-entry provenance not evaluated here |
| Official vs third‑party | ❓ Unknown |
| Timestamps | ❓ Unknown |

DNS/Hosting:
- A: 209.38.78.103 (non-CDN direct host)
- NS: DNSimple (ns1/ns3 + edge names)

Policy/API Endpoints:
- `/privacy-policy` 200; `/robots.txt` 200; `/sitemap.xml` 200
- `/api` 200 but no OpenAPI/Swagger specs found at root

### Tier 2: Manual Investigation

| Check | Status | Notes |
|-------|--------|-------|
| Privacy policy exists | ✅ Yes | `/privacy-policy` present |
| Terms of service | ❓ Unknown | `/terms` and `/tos` 404 |
| Legal entity identified | ❓ Unknown |
| Data collection disclosed | ⚠️ Partial | Privacy policy present (content not parsed here) |
| Publisher verification documented | ❓ Unknown |
| Moderation policy public | ❓ Unknown |
| Report button | ❓ Unknown |
| Vulnerability disclosure policy | ❓ Unknown |
| Badge criteria/process | ❓ Unknown |

### Security Score Summary (qualitative)

Strengths:
- HSTS, XFO, XCTO, Referrer-Policy set; simple static asset preload
- Privacy policy and sitemap/robots present

Unknowns:
- API semantics undocumented; curation/verification processes not surfaced; operator identity not disclosed

Overall Assessment: Useful aggregator with decent baseline headers and privacy page. Needs provenance/verification and API documentation for stronger trust.

## Notes

New/Interesting:
- `/api` responds 200, but no OpenAPI or docs at root — consider documenting.
- Discord invite and personal GitHub links suggest a community-driven project.

## Audit Evidence (2025‑12‑11)

- Command: `python3 security-report/tools/tier1_audit.py https://www.pulsemcp.com`
- HTTP/security headers: HSTS includeSubDomains; XFO SAMEORIGIN; XCTO nosniff; Referrer-Policy strict-origin-when-cross-origin.
- DNS: DNSimple NS; A=209.38.78.103.
- Paths: `/privacy-policy` 200; `/robots.txt` 200; `/sitemap.xml` 200; `/api` 200.
