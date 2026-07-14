---
title: "MCP Registry"
url: "https://registry.modelcontextprotocol.io/"
source_code_url: "Unknown"
is_marketplace: yes
is_aggregator: no
is_list_of_marketplaces: no
language: "en"
type: "registry-api"
operator: "Model Context Protocol"
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "Unknown"
server_count: "Unknown"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://registry.modelcontextprotocol.io/docs#/operations/list-servers-v0.1"
    description: "API Documentation"
    captured: "2026-02-04"
  - url: "https://registry.modelcontextprotocol.io/openapi.json"
    description: "OpenAPI Specification"
    captured: "2026-02-04"
  - url: "https://modelcontextprotocol.io/"
    description: "Main Model Context Protocol website"
    captured: "2026-02-04"
---

## Overview

The MCP Registry is the official, open-source registry for Model Context Protocol (MCP) servers. It provides a programmatic API for discovering and managing MCP servers, acting as a central hub for the MCP ecosystem. The registry's API is documented, and an OpenAPI specification is available. It is operated by the "Model Context Protocol" organization, which also maintains the main `modelcontextprotocol.io` website.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | Provides programmatic discovery of servers via API. |
| One-click install | ❌ | Not directly, provides API for integrations. |
| Curated list/recommendations | ❓ | The registry serves as a central list. |
| Public API | ✅ | Core functionality is a public REST API. |
| CLI tool | ❌ | Not directly. |
| Client integration | ✅ | Designed for integration into MCP clients. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | Official MCP Registry | Website Title |
| Primary URL | https://registry.modelcontextprotocol.io/ | Browser |
| Operator (company/individual) | Model Context Protocol | Main website |
| Country/jurisdiction | ❓ Unknown | |
| Contact email (general) | ❓ Unknown | Not found on registry or main website. |
| Contact email (security) | ❓ Unknown | Not explicitly mentioned on registry or main website. |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ❓ Unknown | Not directly linked from registry/main website. |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Registry - Provides API for programmatic discovery | ✅ Yes | Core function. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Public API (registry endpoint) | ✅ Yes | `https://registry.modelcontextprotocol.io/v0.1/servers` (from docs). |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|---|---|---|
| API documentation available? | ✅ Yes | https://registry.modelcontextprotocol.io/docs#/operations/list-servers-v0.1 |
| Authentication required for read? | ❌ No | Unauthenticated read-only (from aggregators doc). |
| Rate limiting? | ❓ Unknown | Not mentioned in available documentation. |
| OpenAPI/Swagger spec? | ✅ Yes | https://registry.modelcontextprotocol.io/openapi.json |
| API terms of use? | ❓ Unknown | Not found on registry or main website. |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|---|---|---|
| Links to external sources | ✅ Yes | Servers listed will have external sources. |

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|---|---|---|
| Publisher verification process exists? | ❓ Unknown | Not explicitly detailed in available documentation. |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ❓ Unknown | Not explicitly detailed in available documentation. |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ❌ No | Paths return 404; not found on main website. |

### 5.2 Terms of Service

| Question | Answer | Evidence/Source |
|---|---|---|
| Terms of service exists? | ❌ No | Paths return 404; not found on main website. |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ❌ No | Paths return 404; not found on main website. |

---

## Part 6: Supply Chain Security

N/A - This is a registry/API, not a platform for hosting or executing code directly.

---

## Part 7: Technical Security Posture

### 7.1 Web Security Headers

| Header | Present? | Value |
|---|---|---|
| HTTPS enforced | ✅ Yes | |
| Strict-Transport-Security (HSTS) | ✅ Yes | `max-age=31536000; includeSubDomains` |
| Content-Security-Policy | ❌ No | |
| X-Frame-Options | ❌ No | |
| X-Content-Type-Options | ❌ No | |
| Referrer-Policy | ❌ No | |
| Permissions-Policy | ❌ No | |
| Cross-Origin-Opener-Policy | ❌ No | |
| Cross-Origin-Resource-Policy | ❌ No | |

### 7.2 TLS Certificate

| Field | Value |
|---|---|
| Issuer | Let's Encrypt |
| Subject | `prod.registry.modelcontextprotocol.io` |

### 7.3 DNS & Hosting

| Field | Value |
|---|---|
| Provider hints | Cloudflare (NS), Google Cloud (IP), Google Workspace (MX) |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Core Registry:** Provides a central, programmatic hub for MCP server discovery.
- **OpenAPI Specification:** Offers a machine-readable API definition for easy integration.
- **Strong TLS and HSTS:** Implements HTTPS and HSTS for secure communication.
- **Backed by Model Context Protocol:** Associated with the official MCP organization.

### 11.2 Weaknesses & Gaps

- **Missing Major Security Headers:** Lacks crucial web security headers beyond HSTS, such as CSP and X-Frame-Options.
- **No Operator Transparency on Policies:** Despite being the "official" registry, explicit privacy policy, terms of service, or security policy are not readily available or linked from the registry or main `modelcontextprotocol.io` website.
- **No Clear Vetting Process:** Information on how MCP servers are vetted or moderated before being listed is not apparent.
- **Contact Information Missing:** No clear contact details for general or security inquiries.

### 11.3 Red Flags

- The absence of clear privacy, terms of service, and security policies for an "official" registry is a significant red flag. Users and developers relying on this registry lack transparent information about data handling, terms of use, and vulnerability disclosure.

### 11.4 Recommendations

- **Implement Full Security Headers:** Add comprehensive web security headers to the registry's web interface.
- **Publish Comprehensive Policies:** Clearly link and provide privacy policy, terms of service, and a formal security policy on both the registry and the main `modelcontextprotocol.io` websites.
- **Document Vetting Process:** Detail the process by which MCP servers are reviewed and approved for inclusion in the registry.
- **Provide Contact Information:** Offer clear contact details for both general inquiries and security-related reports.

### 11.5 Overall Trust Assessment

The MCP Registry is a foundational component of the Model Context Protocol ecosystem, offering a valuable programmatic interface for server discovery. Its use of strong TLS and an OpenAPI spec promotes interoperability. However, its trustworthiness is significantly hampered by the absence of transparent privacy, terms of service, and security policies, as well as the lack of crucial web security headers. For an "official" and central registry, these are critical omissions. Without clear guidelines on data handling, terms of use, and a documented vetting process for listed servers, users and developers must approach the registry with caution, understanding the lack of transparent governance and security assurances.

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
  "name": "MCP Registry",
  "marketplace_url": "https://registry.modelcontextprotocol.io/docs#/operations/list-servers-v0.1",
  "source_url": "",
  "audited_at": "2025-12-13T04:58:11.730176Z",
  "checks_run": [
    "domain",
    "web"
  ],
  "errors": [],
  "domain": {
    "hostname": "registry.modelcontextprotocol.io",
    "registrable_domain": "modelcontextprotocol.io",
    "dns": {
      "a": [
        "prod.registry.modelcontextprotocol.io.",
        "34.61.200.254"
      ],
      "aaaa": [],
      "cname": [
        "prod.registry.modelcontextprotocol.io"
      ],
      "ns": [
        "todd.ns.cloudflare.com",
        "chin.ns.cloudflare.com"
      ],
      "mx": [
        "smtp.google.com"
      ],
      "txt": [
        "google-site-verification=0jJ1JQ6pdBjRe2r6UCzi2RJbsjvglJUmekPb5rpUQXQ",
        "google-site-verification=UI0Tjq-ecUgNu3kFATkW87qcabX6kTljsbYjms2-FdQ",
        "v=spf1 include:_spf.google.com ~all",
        "czyymtp25a"
      ]
    },
    "tls": {
      "ok": true,
      "issuer": "C=US, O=Let's Encrypt, CN=R13",
      "subject": "CN=prod.registry.modelcontextprotocol.io",
      "not_before": "Dec 11 14:12:58 2025 GMT",
      "not_after": "Mar 11 14:12:57 2026 GMT",
      "sha256_fingerprint": null,
      "san": [
        "prod.registry.modelcontextprotocol.io",
        "registry.modelcontextprotocol.io"
      ],
      "error": null
    },
    "provider_hints": [
      "Cloudflare (NS)",
      "Google Workspace (MX)"
    ],
    "reverse_dns": {
      "prod.registry.modelcontextprotocol.io.": "254.200.61.34.bc.googleusercontent.com",
      "34.61.200.254": "254.200.61.34.bc.googleusercontent.com"
    },
    "errors": []
  },
  "web": {
    "url": "https://registry.modelcontextprotocol.io/docs#/operations/list-servers-v0.1",
    "http": {
      "ok": true,
      "final_url": "https://registry.modelcontextprotocol.io/docs#/operations/list-servers-v0.1",
      "status_code": 200,
      "status_chain": [
        "HTTP/2 200"
      ],
      "redirect_chain": [],
      "headers": {
        "date": "Sat, 13 Dec 2025 04:58:13 GMT",
        "content-type": "text/html",
        "content-length": "823",
        "vary": "Origin",
        "strict-transport-security": "max-age=31536000; includeSubDomains"
      },
      "response_time_ms": 334,
      "error": null
    },
    "security_headers": {
      "strict_transport_security": "max-age=31536000; includeSubDomains",
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
        "status_code": 404,
        "redirect_to": null
      },
      "/sitemap.xml": {
        "path": "/sitemap.xml",
        "status_code": 404,
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
        "status_code": 200,
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
        "status_code": 200,
        "redirect_to": null
      },
      "/openapi.yaml": {
        "path": "/openapi.yaml",
        "status_code": 200,
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
    "server_info": {},
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