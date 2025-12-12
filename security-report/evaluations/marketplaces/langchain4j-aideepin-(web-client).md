---
title: "langchain4j-aideepin (Web Client)"
url: "https://github.com/moyangzhan/langchain4j-aideepin-web"
source_code_url: "https://github.com/moyangzhan/langchain4j-aideepin-web"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: ""
type: ""
evidence:
  - url: "https://github.com/moyangzhan/langchain4j-aideepin-web"
    description: "Homepage / primary listing"
last_evaluated: "2025-12-11"
  - url: "https://github.com/moyangzhan/langchain4j-aideepin-web/privacy"
    description: "/privacy 200"
  - url: "https://github.com/moyangzhan/langchain4j-aideepin-web/privacy-policy"
    description: "/privacy-policy 200"
  - url: "https://github.com/moyangzhan/langchain4j-aideepin-web/security"
    description: "/security 200"
  - url: "https://github.com/moyangzhan/langchain4j-aideepin-web/about"
    description: "/about 200"
  - url: "https://github.com/moyangzhan/langchain4j-aideepin-web/robots.txt"
    description: "/robots.txt 200"
  - url: "https://github.com/moyangzhan/langchain4j-aideepin-web/docs"
    description: "/docs 200"
  - url: "https://github.com/moyangzhan/langchain4j-aideepin-web/api-docs"
    description: "/api-docs 200"
  - url: "https://github.com/moyangzhan/langchain4j-aideepin-web/swagger"
    description: "/swagger 200"
---

# langchain4j-aideepin (Web Client)

## Overview
GitHub repository for a web client related to AIDeepin + Langchain4j. Repo acts as code source, not a hosted marketplace.

## Features
- Discovery/search: Via repo content
- API: N/A (code repo)

## Marketplace Classification (Tier 0)

Type: informational (GitHub repository)

Discovery & Metadata Delivery:
- Repo: https://github.com/moyangzhan/langchain4j-aideepin-web

## Security

### Tier 1: Automated/Observable Checks (GitHub pages)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | GitHub responses |
| TLS/security headers | ✅ Strong | HSTS, CSP, XFO=deny, XCTO=nosniff |

## Notes

New/Interesting:
- AIDeepin website (http) is reachable but does not expose policy/API endpoints; not used for this repo entry.

### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 200
- Provider hints: (none)
- DNS: A=140.82.113.4; CNAME=-; NS=ns-1707.awsdns-21.co.uk., ns-421.awsdns-52.com., ns-520.awsdns-01.net.
- Security headers: HSTS=max-age=31536000; includeSubdomains; preload, XFO=deny, XCTO=nosniff
- Mixed content: http_subresources=0; http_literals=9
- Policy endpoints 200: /privacy, /privacy-policy, /security, /about, /robots.txt
- API endpoints 200: /docs, /api-docs, /swagger
- Social links detected: 63 (showing up to 5)
  - github: https://github.com/fluidicon.png
  - github: https://github.com/moyangzhan/langchain4j-aideepin-web
  - github: https://github.com/moyangzhan/langchain4j-aideepin-web.git
  - github: https://github.com/moyangzhan/langchain4j-aideepin-web&quot;,&quot;user_id&quot;:null}}
  - github: https://github.com/features/copilot

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.
