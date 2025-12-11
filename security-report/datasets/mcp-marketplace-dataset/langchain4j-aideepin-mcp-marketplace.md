---
title: "Langchain4j AIDeepin MCP Marketplace"
url: "http://www.aideepin.com"
source_code_url: "https://github.com/moyangzhan/langchain4j-aideepin"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: ""
type: ""
evidence:
  - url: "http://www.aideepin.com"
    description: "Homepage / primary listing"
last_evaluated: "2025-12-11"
---

# Langchain4j AIDeepin MCP Marketplace

## Overview
GitHub repository and website for an AIDeepin + Langchain4j MCP marketplace. The website is HTTP-only landing with minimal signals; the GitHub repo is authoritative for code.

## Features
- Discovery/search: Via repo content/website
- One‑click install: ❓ Unknown
- Curated list/recommendations: Yes (repo-driven)
- API: ❓ Unknown

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ❌ No | Website is HTTP (no TLS) |
| TLS/security headers | ❌ Missing | No HSTS/CSP/XFO/XCTO on website |
| No mixed content | ✅ Yes | No HTTP subresource loads detected (static) |
| Policy pages | ❌ None | No policy/contact endpoints detected on website |

Repo Security (GitHub): Strong headers (HSTS, CSP, XFO deny, nosniff)

## Notes

New/Interesting:
- HTTP-only website; prefer the GitHub repository for authoritative content and provenance.

### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/1.1 200 OK
- Provider hints: (none)
- DNS: A=107.155.55.44; CNAME=-; NS=dns13.hichina.com., dns14.hichina.com.
- Security headers: HSTS=(missing), XFO=(missing), XCTO=(missing)
- Mixed content: http_subresources=0; http_literals=0
- Policy endpoints 200: (none)
- API endpoints 200: (none)
- Social links detected: 0 (showing up to 5)

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.
