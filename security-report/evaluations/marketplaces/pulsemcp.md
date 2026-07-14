---
title: "PulseMCP"
url: "https://www.pulsemcp.com"
source_code_url: "Unknown"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "directory"
operator: "Unknown"
operator_jurisdiction: "Unknown"
contact_email: "hello@pulsemcp.com"
security_email: "Unknown"
server_count: "Unknown"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://www.pulsemcp.com"
    description: "Main website"
    captured: "2026-02-04"
---

## Overview

PulseMCP is presented as a Model Context Protocol (MCP) server directory and collection website. It aims to provide a platform for discovering and collecting MCP servers. The website seems to be actively maintained, featuring a clean layout and hinting at extensive server listings and filtering options. It has a robust web security posture with good headers and a clear contact email.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | A search and discovery platform for MCP servers. |
| One-click install | ❌ | Not directly available. |
| Curated list/recommendations | ✅ | Implied by "collection website," with filtering options mentioned in user comments in external blog. |
| Public API | ✅ | `/api` endpoint returns 200 (from audit). |
| CLI tool | ❌ | Not mentioned. |
| Client integration | ❌ | Not mentioned. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | PulseMCP | Website Title |
| Primary URL | https://www.pulsemcp.com | Browser |
| Operator (company/individual) | ❓ Unknown | Not found on site. |
| Country/jurisdiction | ❓ Unknown | Not specified. |
| Contact email (general) | ✅ Yes | `hello@pulsemcp.com` (from audit social links). |
| Contact email (security) | ❓ Unknown | Not explicitly mentioned. |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ❌ No | Not mentioned. |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Directory/Aggregator - Lists servers with external links | ✅ Yes | Primary function is listing tools. |
| Curated List - Manually maintained list (e.g., awesome-list) | ✅ Yes | User comments in external blog mention curation. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ✅ Yes | https://www.pulsemcp.com |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|---|---|---|
| API documentation available? | ❓ Unknown | `/api` endpoint returns 200, but no documentation found. |
| Authentication required for read? | ❓ Unknown | |
| Rate limiting? | ❓ Unknown | |
| OpenAPI/Swagger spec? | ❌ No | Not found in audit paths. |
| API terms of use? | ❓ Unknown | |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|---|---|---|
| Link to external source (GitHub, etc.) | ✅ Yes | Implied by server listings. |

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|---|---|---|
| Publisher verification process exists? | ❓ Unknown | Not mentioned. |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ❓ Unknown | Not mentioned. |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ✅ Yes | Path `/privacy-policy` returns 200, but content could not be fetched. |
| User data collected (summary) | ❓ Unknown | Content not fetched. |
| Analytics/tracking tools used | ✅ Yes | Google Analytics (from audit). |

### 5.2 Terms of Service

| Question | Answer | Evidence/Source |
|---|---|---|
| Terms of service exists? | ✅ Yes | Path `/terms-of-service` returns 200, but content could not be fetched. |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ❌ No | All policy-related paths return 404. |

---

## Part 6: Supply Chain Security

N/A - This is a directory of tools, not a hosting/execution platform.

---

## Part 7: Technical Security Posture

### 7.1 Web Security Headers

| Header | Present? | Value |
|---|---|---|
| HTTPS enforced | ✅ Yes | |
| Strict-Transport-Security (HSTS) | ✅ Yes | `max-age=63072000; includeSubDomains` |
| Content-Security-Policy | ❌ No | |
| X-Frame-Options | ✅ Yes | `SAMEORIGIN` |
| X-Content-Type-Options | ✅ Yes | `nosniff` |
| Referrer-Policy | ✅ Yes | `strict-origin-when-cross-origin` |
| Permissions-Policy | ❌ No | |
| Cross-Origin-Opener-Policy | ❌ No | |
| Cross-Origin-Resource-Policy | ❌ No | |

### 7.2 TLS Certificate

| Field | Value |
|---|---|
| Issuer | Let's Encrypt |
| Subject | `www.pulsemcp.com` |

### 7.3 DNS & Hosting

| Field | Value |
|---|---|
| Provider hints | Cloudflare (NS) |

### 7.6 Social/Contact Links Found

| Type | URL |
|---|---|
| GitHub | `https://github.com/tadasant`, `https://github.com/macoughl`, `https://github.com/modelcontextprotocol/registry` |
| Discord | `https://discord.gg/dP2evEyTjS` |
| Twitter | `https://x.com/pulsemcp`, `https://x.com/tadasayy`, `https://x.com/grumpygrowthguy` |
| LinkedIn | `https://www.linkedin.com/company/pulsemcp`, `https://www.linkedin.com/in/tadas-antanavicius/`, `https://www.linkedin.com/in/mike-coughlin-ggg/` |
| Email | `mailto:hello@pulsemcp.com` |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Good Web Security Headers:** Implements HSTS, X-Frame-Options, X-Content-Type-Options, and Referrer-Policy.
- **Clear Contact Information:** Provides an email address and multiple social media links.
- **Active Social Presence:** Engages on Discord, Twitter, and LinkedIn.
- **Dedicated Policy Paths:** Privacy Policy and Terms of Service paths exist and return 200.
- **API Endpoint:** An `/api` endpoint returns 200, suggesting programmatic access to data.

### 11.2 Weaknesses & Gaps

- **Missing Content Security Policy (CSP):** A critical security header for preventing XSS attacks is missing.
- **Inaccessible Policy Content:** Despite status 200 for policy paths, the actual content could not be fetched, hindering transparency.
- **No Operator Transparency:** The operator is anonymous.
- **No Explicit Vetting Information:** No explicit mention of how listed MCP servers are vetted for security or quality.
- **No Security Policy:** Absence of a formal security policy or vulnerability disclosure process.
- **Google Analytics:** Uses tracking without accessible content for its privacy policy.

### 11.3 Red Flags

- The inability to fetch the content of the Privacy Policy and Terms of Service, combined with the use of Google Analytics, is a concern regarding user data handling and transparency.
- The lack of explicit vetting for listed MCP servers poses a risk to users.

### 11.4 Recommendations

- **Implement a Content Security Policy (CSP):** This is a crucial next step for web security.
- **Ensure Accessible Policy Content:** Make sure the content of Privacy Policy and Terms of Service is readily fetchable and clear.
- **Provide Operator Transparency:** Clearly identify the operator and provide details about their organization.
- **Document Vetting Process:** Clearly define how listed MCP servers are evaluated for security and quality.
- **Establish a Security Policy:** Publish a `SECURITY.md` file and provide a clear channel for vulnerability reports.

### 11.5 Overall Trust Assessment

PulseMCP presents a professional image as an MCP server directory with a strong set of web security headers and active social engagement. Its provision of clear contact information and dedicated policy paths are positive. However, the inability to fetch the actual content of its privacy and terms of service, coupled with the absence of a Content Security Policy and explicit vetting processes for listed servers, creates significant trust gaps. Users should approach PulseMCP as a discovery tool but exercise caution, understanding that crucial transparency around data handling and server trustworthiness remains unverified.

---

## Evaluation Metadata

| Field | Value |
|---|---|
| Evaluator | AI Assistant |
| Evaluation Date | 2026-02-04 |
| Marketplace Version/State | As of 2026-02-04 |
| Automated Audit Tool Version | N/A (Used pre-existing data) |
| Evidence Archive Location | N/A |
| Sent to Operator for Review? | No |
| Operator Response Received? | N/A |
| Operator Verified? | No |
| Last Updated | 2026-02-04 |

---

## Audit Evidence

### tier1_audit.py Output

```json
{
  "name": "PulseMCP",
  "marketplace_url": "https://www.pulsemcp.com",
  "source_url": "",
  "audited_at": "2025-12-13T04:58:11.736083Z",
  "checks_run": [
    "domain",
    "web"
  ],
  "errors": [],
  "domain": {
    "hostname": "www.pulsemcp.com",
    "registrable_domain": "pulsemcp.com",
    "dns": {
      "a": [
        "209.38.78.103"
      ],
      "aaaa": [],
      "cname": [],
      "ns": [
        "ns4.dnsimple-edge.org",
        "ns1.dnsimple.com",
        "ns2.dnsimple-edge.net",
        "ns3.dnsimple.com"
      ],
      "mx": [
        "mailsec.protonmail.ch",
        "mail.protonmail.ch"
      ],
      "txt": [
        "v=spf1 include:_spf.protonmail.ch ~all",
        "google-site-verification=n7AzCW--DId0f2xNLGIb7llVbEabVELoXrWTfUMzyzs",
        "google-site-verification=pDnUScvIHkG_OjRAVYYr9Lleq5xpHZ7sr_F7WzUn4Lk",
        "google-site-verification=vymzDqoBLMrGuqXfHWr4Ea-1qHDnk0bztwOB0JvlAgk",
        "protonmail-verification=ae13aac07f10d01db0a9743669d817e302f16b09"
      ]
    },
    "tls": {
      "ok": true,
      "issuer": "C=US, O=Let's Encrypt, CN=E8",
      "subject": "CN=www.pulsemcp.com",
      "not_before": "Nov 25 12:18:38 2025 GMT",
      "not_after": "Feb 23 12:18:37 2026 GMT",
      "sha256_fingerprint": null,
      "san": [
        "www.pulsemcp.com"
      ],
      "error": null
    },
    "provider_hints": [],
    "reverse_dns": {
      "209.38.78.103": ""
    },
    "errors": []
  },
  "web": {
    "url": "https://www.pulsemcp.com",
    "http": {
      "ok": true,
      "final_url": "https://www.pulsemcp.com",
      "status_code": 200,
      "status_chain": [
        "HTTP/2 200"
      ],
      "redirect_chain": [],
      "headers": {
        "alt-svc": "h3=\":443\"; ma=2592000",
        "cache-control": "max-age=0, private, must-revalidate",
        "content-type": "text/html; charset=utf-8",
        "date": "Sat, 13 Dec 2025 04:58:13 GMT",
        "etag": "W/\"8145e42302837efa9f796bb1338b857d\"",
        "link": "</assets/tailwind-f176ee988496ad3d24cc9d10766bd1597577da7a5314444a2263d954f2ba4422.css>; rel=preload; as=style; nopush,</assets/fonts-3081ff0998ece685a3fcf78c2df043c926883ad15b83f48a6d01a37c40bd8ec6.css>; rel=preload; as=style; nopush,</assets/application-4b52082300000b66c943ad80b18cf1b3782c8262094833b536c6801205905c2a.css>; rel=preload; as=style; nopush",
        "referrer-policy": "strict-origin-when-cross-origin",
        "set-cookie": "mt=6fb3ead8-4bdb-4756-929c-c76b6dac76b8; domain=.pulsemcp.com; path=/; expires=Wed, 13 Dec 2045 04:58:13 GMT; secure; samesite=lax\n_pulsemcp_session=PcxhFn5BS%2FLYAbigQjTzVwYZePCiIJpnrRi2ccycjY8zpWPbvXMXIiF%2Fhl25ibFBhnEY%2BlsiB9f7Xy8zkfbASpWPrVqrNlKwaMlSRUf3fnt6F1rsAAowRD6lVvRAjaubZlzz%2BiedzW7%2FmPLNKC0ujO8LitK7a4w2kxdz381ABv%2FKPbLsDgUjMP9ayhKJaWmYHwK1g%2BwHBXzu4ZK9NcvebeYTqvuWffHmEyRCLmmyiYwqC%2BKqWV8L9YbKdqIYD93yVhJeL1CcDsbER3NU3HfYWF8%2BH7LjYYrgA%3D%3D--9lSloiVc0aJtuJZK--%2B%2BIfKovrcyyX9r%2B1ZJH9HQ%3D%3D; domain=.pulsemcp.com; path=/; secure; httponly; samesite=lax",
        "strict-transport-security": "max-age=63072000; includeSubDomains",
        "vary": "Accept-Encoding",
        "x-content-type-options": "nosniff",
        "x-frame-options": "SAMEORIGIN",
        "x-permitted-cross-domain-policies": "none",
        "x-request-id": "26b31d03-ac46-43cb-8661-b620e8b9307f",
        "x-runtime": "0.063778",
        "x-xss-protection": "0"
      },
      "response_time_ms": 420,
      "error": null
    },
    "security_headers": {
      "strict_transport_security": "max-age=63072000; includeSubDomains",
      "content_security_policy": null,
      "x_frame_options": "SAMEORIGIN",
      "x_content_type_options": "nosniff",
      "referrer_policy": "strict-origin-when-cross-origin",
      "permissions_policy": null,
      "cross_origin_opener_policy": null,
      "cross_origin_resource_policy": null,
      "cross_origin_embedder_policy": null,
      "_present": [
        "strict_transport_security",
        "x_frame_options",
        "x_content_type_options",
        "referrer_policy"
      ],
      "_missing": [
        "content_security_policy",
        "permissions_policy",
        "cross_origin_opener_policy",
        "cross_origin_resource_policy",
        "cross_origin_embedder_policy"
      ]
    },
    "paths": {
      "/privacy": {
        "path": "/privacy",
        "status_code": 404,
        "redirect_to": null
      },
      "/privacy-policy": {
        "path": "/privacy-policy",
        "status_code": 200,
        "redirect_to": null
      },
      "/terms": {
        "path": "/terms",
        "status_code": 404,
        "redirect_to": null
      },
      "/tos": {
        "path": "/tos",
        "status_code": 404,
        "redirect_to": null
      },
      "/terms-of-service": {
        "path": "/terms-of-service",
        "status_code": 200,
        "redirect_to": null
      },
      "/security": {
        "path": "/security",
        "status_code": 404,
        "redirect_to": null
      },
      "/security.txt": {
        "path": "/security.txt",
        "status_code": 404,
        "redirect_to": null
      },
      "/.well-known/security.txt": {
        "path": "/.well-known/security.txt",
        "status_code": 404,
        "redirect_to": null
      },
      "/legal": {
        "path": "/legal",
        "status_code": 404,
        "redirect_to": null
      },
      "/about": {
        "path": "/about",
        "status_code": 301,
        "redirect_to": "https://www.pulsemcp.com/#about-us"
      },
      "/contact": {
        "path": "/contact",
        "status_code": 301,
        "redirect_to": "https://www.pulsemcp.com/#contact"
      },
      "/robots.txt": {
        "path": "/robots.txt",
        "status_code": 200,
        "redirect_to": null
      },
      "/sitemap.xml": {
        "path": "/sitemap.xml",
        "status_code": 200,
        "redirect_to": null
      },
      "/status": {
        "path": "/status",
        "status_code": 404,
        "redirect_to": null
      },
      "/health": {
        "path": "/health",
        "status_code": 404,
        "redirect_to": null
      },
      "/api": {
        "path": "/api",
        "status_code": 200,
        "redirect_to": null
      },
      "/docs": {
        "path": "/docs",
        "status_code": 404,
        "redirect_to": null
      },
      "/api-docs": {
        "path": "/api-docs",
        "status_code": 404,
        "redirect_to": null
      },
      "/documentation": {
        "path": "/documentation",
        "status_code": 404,
        "redirect_to": null
      },
      "/swagger": {
        "path": "/swagger",
        "status_code": 404,
        "redirect_to": null
      },
      "/swagger.json": {
        "path": "/swagger.json",
        "status_code": 404,
        "redirect_to": null
      },
      "/swagger.yaml": {
        "path": "/swagger.yaml",
        "status_code": 404,
        "redirect_to": null
      },
      "/openapi.json": {
        "path": "/openapi.json",
        "status_code": 404,
        "redirect_to": null
      },
      "/openapi.yaml": {
        "path": "/openapi.yaml",
        "status_code": 404,
        "redirect_to": null
      },
      "/graphql": {
        "path": "/graphql",
        "status_code": 404,
        "redirect_to": null
      }
    },
    "mixed_content": {
      "http_links_count": 0,
      "http_subresources_count": 0,
      "samples": []
    },
    "trackers": [
      {
        "name": "Google Analytics",
        "type": "analytics",
        "evidence": "ga.js"
      }
    ],
    "social_links": [
      {
        "type": "github",
        "url": "https://github.com/tadasant"
      },
      {
        "type": "github",
        "url": "https://github.com/macoughl"
      },
      {
        "type": "github",
        "url": "https://github.com/modelcontextprotocol/registry"
      },
      {
        "type": "discord",
        "url": "https://discord.gg/dP2evEyTjS"
      },
      {
        "type": "twitter",
        "url": "https://x.com/pulsemcp"
      },
      {
        "type": "twitter",
        "url": "https://x.com/tadasayy"
      },
      {
        "type": "twitter",
        "url": "https://x.com/grumpygrowthguy"
      },
      {
        "type": "linkedin",
        "url": "https://www.linkedin.com/company/pulsemcp"
      },
      {
        "type": "linkedin",
        "url": "https://www.linkedin.com/in/tadas-antanavicius/"
      },
      {
        "type": "linkedin",
        "url": "https://www.linkedin.com/in/mike-coughlin-ggg/"
      },
      {
        "type": "email",
        "url": "mailto:hello@pulsemcp.com"
      }
    ],
    "cookies": [
      {
        "name": "mt",
        "secure": true,
        "httponly": false,
        "samesite": "lax"
      },
      {
        "name": "_pulsemcp_session",
        "secure": true,
        "httponly": true,
        "samesite": "lax"
      }
    ],
    "server_info": {},
    "errors": []
  },
  "success": true
}
```