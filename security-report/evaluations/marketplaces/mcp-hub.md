---
title: "MCP Hub"
url: "https://mcphub.io"
source_code_url: "Unknown"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "directory"
operator: "Unknown"
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "Unknown"
server_count: "Unknown"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://mcphub.io"
    description: "Main website"
    captured: "2026-02-04"
---

## Overview

MCP Hub is a website dedicated to the search, discovery, and collection of Model Context Protocol (MCP) servers. It functions as a directory, likely aggregating information about various MCP servers. The site is hosted on a robust infrastructure (Vercel/Cloudflare) and utilizes Next.js. However, transparent information regarding its operator and key policies is not readily available.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | A search and discovery platform for MCP servers. |
| One-click install | ❌ | Not directly available. |
| Curated list/recommendations | ❓ | Implied by "collection website," but curation process is unclear. |
| Public API | ❌ | All API-related paths return 404. |
| CLI tool | ❌ | Not mentioned. |
| Client integration | ❌ | Not mentioned. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | MCP Hub | Website Title |
| Primary URL | https://mcphub.io | Browser |
| Operator (company/individual) | ❓ Unknown | Not found on site. |
| Country/jurisdiction | ❓ Unknown | Not specified. |
| Contact email (general) | ❓ Unknown | No contact page. |
| Contact email (security) | ❓ Unknown | Not explicitly mentioned. |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ❌ No | Not mentioned. |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Directory/Aggregator - Lists servers with external links | ✅ Yes | Primary function is listing tools. |
| Curated List - Manually maintained list (e.g., awesome-list) | ❓ Unknown | Curation process is unclear. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ✅ Yes | https://mcphub.io |

### 2.2 API Details (if applicable)

N/A - All API-related paths return 404.

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
| Publisher verification process exists? | ❌ No | Not mentioned. |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ❓ Unknown | Not mentioned. |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ❌ No | All policy-related paths return 404. |

### 5.2 Terms of Service

| Question | Answer | Evidence/Source |
|---|---|---|
| Terms of service exists? | ❌ No | All policy-related paths return 404. |

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
| HTTPS enforced | ✅ Yes |  |
| Strict-Transport-Security (HSTS) | ✅ Yes | `max-age=63072000` |
| Content-Security-Policy | ❌ No |  |
| X-Frame-Options | ❌ No |  |
| X-Content-Type-Options | ❌ No |  |
| Referrer-Policy | ❌ No |  |
| Permissions-Policy | ❌ No |  |
| Cross-Origin-Opener-Policy | ❌ No |  |
| Cross-Origin-Resource-Policy | ❌ No |  |

### 7.2 TLS Certificate

| Field | Value |
|---|---|
| Issuer | Google Trust Services |
| Subject | `mcphub.io` |

### 7.3 DNS & Hosting

| Field | Value |
|---|---|
| Provider hints | Cloudflare (NS), Vercel (Server) |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Clear Purpose:** Serves as a straightforward directory for MCP tools.
- **Robust Hosting:** Benefits from Vercel/Cloudflare for hosting and content delivery, providing strong base security (HTTPS, HSTS).

### 11.2 Weaknesses & Gaps

- **Missing All Major Security Headers:** A significant gap in web security posture.
- **No Operator Transparency:** The operator is anonymous, and contact information is missing.
- **No Policies:** Lacks privacy policy, terms of service, or security policy.
- **No Explicit Vetting Information:** No explicit mention of how listed MCP servers are vetted for security or quality.

### 11.3 Red Flags

- The combination of an anonymous operator and the complete absence of privacy, terms of service, and security policies is a significant red flag. This indicates a severe lack of transparency and accountability for a platform that aggregates tools.

### 11.4 Recommendations

- **Implement All Security Headers:** Add comprehensive security headers to enhance web security.
- **Provide Operator Transparency:** Clearly identify the operator and provide contact information.
- **Publish Comprehensive Policies:** Develop and publish clear privacy, terms of service, and security policies.
- **Document Vetting Process:** Clearly define how listed MCP servers are evaluated for security and quality.

### 11.5 Overall Trust Assessment

MCP Hub functions as a directory for MCP servers, leveraging robust hosting infrastructure. However, its trustworthiness is severely compromised by a complete lack of transparency. The anonymous nature of its operator, coupled with the absence of fundamental privacy, terms of service, and security policies, raises significant concerns about data handling and accountability. The missing web security headers further weaken its posture. Without clear guidelines on data handling and a documented vetting process for listed servers, users must approach this directory with extreme caution. This marketplace currently presents a high-risk environment due to its lack of governance and transparency.

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
  "name": "MCP Hub",
  "marketplace_url": "https://mcphub.io",
  "source_url": "",
  "audited_at": "2025-12-13T04:58:11.735838Z",
  "checks_run": [
    "domain",
    "web"
  ],
  "errors": [],
  "domain": {
    "hostname": "mcphub.io",
    "registrable_domain": "mcphub.io",
    "dns": {
      "a": [
        "104.21.70.34",
        "172.67.218.211"
      ],
      "aaaa": [
        "2606:4700:3034::6815:4622",
        "2606:4700:3034::ac43:dad3"
      ],
      "cname": [],
      "ns": [
        "jose.ns.cloudflare.com",
        "gabriella.ns.cloudflare.com"
      ],
      "mx": [],
      "txt": [
        "google-site-verification=toKNNoRSs56UKeox9ACpOOCvhcIvyn7SyxnKusczx1o"
      ]
    },
    "tls": {
      "ok": true,
      "issuer": "C=US, O=Google Trust Services, CN=WE1",
      "subject": "CN=mcphub.io",
      "not_before": "Dec  5 09:55:57 2025 GMT",
      "not_after": "Mar  5 10:53:45 2026 GMT",
      "sha256_fingerprint": null,
      "san": [
        "mcphub.io",
        "*.mcphub.io"
      ],
      "error": null
    },
    "provider_hints": [
      "Cloudflare (NS)"
    ],
    "reverse_dns": {
      "104.21.70.34": "",
      "172.67.218.211": ""
    },
    "errors": []
  },
  "web": {
    "url": "https://mcphub.io",
    "http": {
      "ok": true,
      "final_url": "https://mcphub.io",
      "status_code": 200,
      "status_chain": [
        "HTTP/2 200"
      ],
      "redirect_chain": [],
      "headers": {
        "date": "Sat, 13 Dec 2025 04:58:13 GMT",
        "content-type": "text/html; charset=utf-8",
        "access-control-allow-origin": "*",
        "age": "930933",
        "cache-control": "public, max-age=0, must-revalidate",
        "content-disposition": "inline",
        "report-to": "{\"group\":\"cf-nel\",\"max_age\":604800,\"endpoints\":[{\"url\":\"https://a.nel.cloudflare.com/report/v4?s=%2BY108mve8D7lZrRH632RzY03gHkeELsasjUksuJT8daRq%2Fip3pgxyDUaTLmbgDzZuoykUGrGr%2FauwEz5dqv4aGZnY5RV9Lmkag%3D%3D\"}]}",
        "nel": "{\"report_to\":\"cf-nel\",\"success_fraction\":0.0,\"max_age\":604800}",
        "server": "cloudflare",
        "strict-transport-security": "max-age=63072000",
        "vary": "accept-encoding",
        "x-matched-path": "/",
        "x-nextjs-prerender": "1",
        "x-nextjs-stale-time": "4294967294",
        "x-vercel-cache": "HIT",
        "x-vercel-id": "pdx1::zzfrg-1765601893357-edbb2dd7f54c",
        "cf-cache-status": "DYNAMIC",
        "cf-ray": "9ad2e2993d3355d1-SEA",
        "alt-svc": "h3=\":443\"; ma=86400"
      },
      "response_time_ms": 245,
      "error": null
    },
    "security_headers": {
      "strict_transport_security": "max-age=63072000",
      "content_security_policy": null,
      "x_frame_options": null,
      "x_content_type_options": null,
      "referrer_policy": null,
      "permissions_policy": null,
      "cross_origin_opener_policy": null,
      "cross_origin_resource_policy": null,
      "cross_origin_embedder_policy": null,
      "_present": [
        "strict_transport_security"
      ],
      "_missing": [
        "content_security_policy",
        "x_frame_options",
        "x_content_type_options",
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
        "status_code": 404,
        "redirect_to": null
      },
      "/privacy-policy": {
        "path": "/privacy-policy",
        "status_code": 404,
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
        "status_code": 404,
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
        "status_code": 404,
        "redirect_to": null
      },
      "/contact": {
        "path": "/contact",
        "status_code": 404,
        "redirect_to": null
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
        "status_code": 404,
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
    "trackers": [],
    "social_links": [],
    "cookies": [],
    "server_info": {
      "server": "cloudflare",
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