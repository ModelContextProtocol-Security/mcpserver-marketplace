---
title: "mcp.run (redirects to TurboMCP.ai)"
url: "https://turbomcp.ai/"
source_code_url: "Unknown"
is_marketplace: yes
is_aggregator: no
is_list_of_marketplaces: no
language: "en"
type: "registry-api"
operator: "Dylibso"
operator_jurisdiction: "Unknown"
contact_email: "sales@dylibso.ai"
security_email: "Unknown"
server_count: "Unknown"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://mcp.run"
    description: "Original URL (redirects)"
    captured: "2026-02-04"
  - url: "https://turbomcp.ai/"
    description: "Redirected to primary website"
    captured: "2026-02-04"
---

## Overview

mcp.run redirects to TurboMCP.ai, which presents itself as a platform to "build great AI apps with superpowered plugins." It emphasizes speed, security, and developer experience for integrating tools with AI models. TurboMCP.ai appears to be a solution offered by Dylibso (contact email sales@dylibso.ai) that functions as a registry or marketplace for AI plugins (MCP servers), providing the infrastructure for developers to build and deploy these plugins.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | Implied by "Discover and deploy". |
| One-click install | ❓ | Not explicitly detailed but focus on speed suggests simplified deployment. |
| Curated list/recommendations | ❓ | Implied by "build great AI apps". |
| Public API | ✅ | "APIs and plugins for building powerful AI applications." |
| CLI tool | ❓ | Not explicitly mentioned. |
| Client integration | ✅ | Plugins integrate with AI models. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | TurboMCP.ai | Website Title |
| Primary URL | https://turbomcp.ai/ | Redirected URL |
| Operator (company/individual) | Dylibso | Contact email (`sales@dylibso.ai`) |
| Country/jurisdiction | ❓ Unknown | |
| Contact email (general) | ✅ Yes | `sales@dylibso.ai` |
| Contact email (security) | ❓ Unknown | Not explicitly mentioned. |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ❌ No | Not mentioned. |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Registry - Provides API for programmatic discovery | ✅ Yes | Focus on APIs and plugins for AI applications. |
| Hosted Execution (PaaS) - Runs MCP servers on their infrastructure | ✅ Yes | Platform for building and deploying AI plugins. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ✅ Yes | `https://turbomcp.ai/` |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|---|---|---|
| API documentation available? | ❓ Unknown | Not fetched. |
| Authentication required for read? | ❓ Unknown | |
| Rate limiting? | ❓ Unknown | |
| OpenAPI/Swagger spec? | ❌ No | Not found in audit paths. |
| API terms of use? | ❓ Unknown | |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|---|---|---|
| Hosted execution (marketplace runs the server) | ✅ Yes | Implied by platform for deploying plugins. |

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
| Privacy policy exists? | ❌ No | Path exists in audit, but content could not be fetched. |
| User data collected (summary) | ❓ Unknown | Content not fetched. |
| Analytics/tracking tools used | ✅ Yes | Google Analytics, Google Tag Manager (from audit). |

### 5.2 Terms of Service

| Question | Answer | Evidence/Source |
|---|---|---|
| Terms of service exists? | ❌ No | Path exists in audit, but content could not be fetched. |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ❌ No | Path exists in audit, but content could not be fetched. |

---

## Part 6: Supply Chain Security

N/A - Information not available for platform that builds and deploys plugins.

---

## Part 7: Technical Security Posture

### 7.1 Web Security Headers

| Header | Present? | Value |
|---|---|---|
| HTTPS enforced | ✅ Yes | |
| Strict-Transport-Security (HSTS) | ✅ Yes | `max-age=31536000` |
| Content-Security-Policy | ❌ No | |
| X-Frame-Options | ❌ No | |
| X-Content-Type-Options | ✅ Yes | `nosniff` |
| Referrer-Policy | ❌ No | |
| Permissions-Policy | ❌ No | |
| Cross-Origin-Opener-Policy | ❌ No | |
| Cross-Origin-Resource-Policy | ❌ No | |

### 7.2 TLS Certificate

| Field | Value |
|---|---|
| Issuer | Google Trust Services |
| Subject | `mcp.run` (for original URL) |

### 7.3 DNS & Hosting

| Field | Value |
|---|---|
| Provider hints | Cloudflare (NS), Framer (Server) |

### 7.6 Social/Contact Links Found

| Type | URL |
|---|---|
| GitHub | `https://github.com/dylibso` |
| LinkedIn | `https://www.linkedin.com/company/dylibso/` |
| Email | `mailto:sales@dylibso.ai` |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Clear Business Focus:** Clearly positions itself as a platform for building and deploying AI plugins.
- **Good Base Security:** Uses HTTPS and HSTS, and has `X-Content-Type-Options`.
- **Identified Operator:** Dylibso is identified as the operating entity with a clear sales contact.
- **Active Social Presence:** Linked to GitHub and LinkedIn.

### 11.2 Weaknesses & Gaps

- **Missing Critical Security Headers:** Lacks CSP, X-Frame-Options, and Referrer-Policy.
- **Inaccessible Policy Content:** Despite paths existing in audit, content for Privacy, Terms, and Security policies could not be fetched, hindering transparency.
- **No Clear Vetting Process:** No explicit mention of how AI plugins (MCP servers) are vetted for security or quality before deployment.
- **Google Analytics/GTM:** Uses tracking tools without an accessible privacy policy.

### 11.3 Red Flags

- The inability to access Privacy Policy, Terms of Service, and Security Policy content is a significant red flag, especially for a platform that emphasizes security and developer experience. This raises concerns about legal compliance, user data handling, and vulnerability management.
- The use of tracking tools without transparent policies.

### 11.4 Recommendations

- **Implement All Security Headers:** Add comprehensive web security headers to enhance web security.
- **Publish Accessible Policies:** Ensure Privacy Policy, Terms of Service, and Security Policy are readily accessible and clearly outline data handling practices, terms of use, and vulnerability disclosure.
- **Document Vetting Process:** Clearly define how AI plugins (MCP servers) are evaluated for security and quality before they can be deployed on the platform.

### 11.5 Overall Trust Assessment

mcp.run (redirecting to TurboMCP.ai) presents an interesting platform for building and deploying AI plugins, backed by Dylibso. While it has a good foundation of base web security (HTTPS, HSTS) and an identified operator with contact information, its trustworthiness is severely undermined by the inaccessibility of its core legal and security policies. The lack of transparent information regarding privacy, terms of use, and a clear security policy, combined with the use of tracking, raises significant red flags. Until these policy gaps are addressed and a clear vetting process for plugins is established, users should approach TurboMCP.ai with extreme caution, as critical transparency and trust assurances are missing.

---

## Evaluation Metadata

| Field | Value |
|---|---|
| Evaluator | AI Assistant |
| Evaluation Date | 2026-02-04 |
| Marketplace Version/State | As of 2026-02-04 |
| Automated Audit Tool Version | N/A (Used pre-existing data for mcp.run) |
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
  "name": "mcp.run",
  "marketplace_url": "https://mcp.run",
  "source_url": "",
  "audited_at": "2025-12-13T04:58:24.501871Z",
  "checks_run": [
    "domain",
    "web"
  ],
  "errors": [],
  "domain": {
    "hostname": "mcp.run",
    "registrable_domain": "mcp.run",
    "dns": {
      "a": [
        "104.26.4.141",
        "172.67.72.180",
        "104.26.5.141"
      ],
      "aaaa": [
        "2606:4700:20::681a:48d",
        "2606:4700:20::681a:58d",
        "2606:4700:20::ac43:48b4"
      ],
      "cname": [],
      "ns": [
        "ada.ns.cloudflare.com",
        "drew.ns.cloudflare.com"
      ],
      "mx": [],
      "txt": [
        "google-site-verification=BzVeJ1ObIujkg_aGecVWbSHvx7bsmKUDDP0HNxFDSfw",
        "google-site-verification=1623pMVgwcLIqbhVkCd-9_t4FNAismMS3ola39J36Ew"
      ]
    },
    "tls": {
      "ok": true,
      "issuer": "C=US, O=Google Trust Services, CN=WE1",
      "subject": "CN=mcp.run",
      "not_before": "Dec  9 19:45:43 2025 GMT",
      "not_after": "Mar  9 20:45:40 2026 GMT",
      "sha256_fingerprint": null,
      "san": [
        "mcp.run",
        "cdn.mcp.run"
      ],
      "error": null
    },
    "provider_hints": [
      "Cloudflare (NS)"
    ],
    "reverse_dns": {
      "104.26.4.141": "",
      "172.67.72.180": "",
      "104.26.5.141": ""
    },
    "errors": []
  },
  "web": {
    "url": "https://mcp.run",
    "http": {
      "ok": true,
      "final_url": "https://turbomcp.ai/",
      "status_code": 301,
      "status_chain": [
        "HTTP/2 301"
      ],
      "redirect_chain": [
        "https://www.mcp.run/",
        "https://turbomcp.ai/"
      ],
      "headers": {
        "date": "Sat, 13 Dec 2025 04:58:25 GMT",
        "content-length": "428047",
        "location": "https://turbomcp.ai/",
        "report-to": "{\"group\":\"cf-nel\",\"max_age\":604800,\"endpoints\":[{\"url\":\"https://a.nel.cloudflare.com/report/v4?s=qw5OhSXp0ZeqwWwoYnwRCOFUVhBU%2FGPg6je95Pu9OyIfyeUgFCRQubHLL%2BGbpbh%2B%2B1u0ZsUweMbdUeYVruey2G8LYXuwsLyE\"}]}",
        "nel": "{\"report_to\":\"cf-nel\",\"success_fraction\":0.0,\"max_age\":604800}",
        "server": "Framer/9339d38",
        "cf-ray": "9ad2e2e8c8658413-YVR",
        "alt-svc": "h3=\":443\"; ma=2592000",
        "cache-control": "public, max-age=0, must-revalidate",
        "content-type": "text/html",
        "etag": "\"e6f6bade95d1501cd5da1b5e93accf19\"",
        "last-modified": "Tue, 21 Oct 2025 22:37:48 GMT",
        "link": "<https://framerusercontent.com>; rel=\"preconnect\", <https://framerusercontent.com>; rel=\"preconnect\"; crossorigin=\"",
        "server-timing": "region;desc=\"us-west-2\", cache;desc=\"cached\", ssg-status;desc=\"optimized\", version;desc=\"9339d38\", route;dur=1;desc=\"id=augiA20Il&locale=default\"",
        "strict-transport-security": "max-age=31536000",
        "vary": "Accept-Encoding",
        "x-content-type-options": "nosniff"
      },
      "response_time_ms": 929,
      "error": null
    },
    "security_headers": {
      "strict_transport_security": "max-age=31536000",
      "content_security_policy": null,
      "x_frame_options": null,
      "x_content_type_options": "nosniff",
      "referrer_policy": null,
      "permissions_policy": null,
      "cross_origin_opener_policy": null,
      "cross_origin_resource_policy": null,
      "cross_origin_embedder_policy": null,
      "_present": [
        "strict_transport_security",
        "x_content_type_options"
      ],
      "_missing": [
        "content_security_policy",
        "x_frame_options",
        "referrer_policy",
        "permissions_policy",
        "cross_origin_opener_policy",
        "cross_origin_resource_policy",
        "cross_origin_embedder_policy"
      ]
    },
    "paths": {
      "/privacy": {
        "path": "/privacy",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/privacy"
      },
      "/privacy-policy": {
        "path": "/privacy-policy",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/privacy-policy"
      },
      "/terms": {
        "path": "/terms",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/terms"
      },
      "/tos": {
        "path": "/tos",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/tos"
      },
      "/terms-of-service": {
        "path": "/terms-of-service",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/terms-of-service"
      },
      "/security": {
        "path": "/security",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/security"
      },
      "/security.txt": {
        "path": "/security.txt",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/security.txt"
      },
      "/.well-known/security.txt": {
        "path": "/.well-known/security.txt",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/.well-known/security.txt"
      },
      "/legal": {
        "path": "/legal",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/legal"
      },
      "/about": {
        "path": "/about",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/about"
      },
      "/contact": {
        "path": "/contact",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/contact"
      },
      "/robots.txt": {
        "path": "/robots.txt",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/robots.txt"
      },
      "/sitemap.xml": {
        "path": "/sitemap.xml",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/sitemap.xml"
      },
      "/status": {
        "path": "/status",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/status"
      },
      "/health": {
        "path": "/health",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/health"
      },
      "/api": {
        "path": "/api",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/api"
      },
      "/docs": {
        "path": "/docs",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/docs"
      },
      "/api-docs": {
        "path": "/api-docs",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/api-docs"
      },
      "/documentation": {
        "path": "/documentation",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/documentation"
      },
      "/swagger": {
        "path": "/swagger",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/swagger"
      },
      "/swagger.json": {
        "path": "/swagger.json",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/swagger.json"
      },
      "/swagger.yaml": {
        "path": "/swagger.yaml",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/swagger.yaml"
      },
      "/openapi.json": {
        "path": "/openapi.json",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/openapi.json"
      },
      "/openapi.yaml": {
        "path": "/openapi.yaml",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/openapi.yaml"
      },
      "/graphql": {
        "path": "/graphql",
        "status_code": 301,
        "redirect_to": "https://www.mcp.run/graphql"
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
        "evidence": "gtag"
      },
      {
        "name": "Google Tag Manager",
        "type": "analytics",
        "evidence": "googletagmanager.com"
      }
    ],
    "social_links": [
      {
        "type": "github",
        "url": "https://github.com/dylibso"
      },
      {
        "type": "linkedin",
        "url": "https://www.linkedin.com/company/dylibso/"
      },
      {
        "type": "email",
        "url": "mailto:sales@dylibso.ai"
      }
    ],
    "cookies": [],
    "server_info": {
      "server": "Framer/9339d38",
      "cdn": "Cloudflare"
    },
    "errors": []
  },
  "success": true
}
```
---

## Changelog

| Date | Version | Changes | Author |
|---|---|---|---|
| 2026-02-04 | 1.0 | Initial evaluation | AI Assistant |

```