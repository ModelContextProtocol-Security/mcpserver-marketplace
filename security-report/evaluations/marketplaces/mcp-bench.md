---
title: "MCP Bench"
url: "https://mcpbench.ai"
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
server_count: "1521"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://mcpbench.ai"
    description: "Main website"
    captured: "2026-02-04"
  - url: "https://mcpbench.ai/about"
    description: "About page"
    captured: "2026-02-04"
---

## Overview

MCP Bench is a directory for browsing Model Context Protocol (MCP) servers. It aggregates server data from the official MCP registry and enhances it with classifications, analytics, and additional metadata provided by MCPBench. The platform allows users to filter servers based on various criteria such as hosting, source availability, transport, target, maintainer, and packages. It presents itself as a tool for exploring the MCP ecosystem.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | Browseable list of 1521 servers with extensive filters. |
| One-click install | ❌ | No direct installation. |
| Curated list/recommendations | ✅ | Provides classifications and additional metadata. |
| Public API | ❌ | No explicit API, data comes from official MCP registry. |
| CLI tool | ❌ | Not mentioned. |
| Client integration | ❌ | Not mentioned. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | MCP Bench | Website Title |
| Primary URL | https://mcpbench.ai | Browser |
| Operator (company/individual) | ❓ Unknown | Not found on site. |
| Country/jurisdiction | ❓ Unknown | Not specified. |
| Contact email (general) | ❓ Unknown | No contact page. |
| Contact email (security) | ❓ Unknown | Not explicitly mentioned. |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ❌ No | Not mentioned. |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Directory/Aggregator - Lists servers with external links | ✅ Yes | Aggregates from official MCP registry. |
| Curated List - Manually maintained list (e.g., awesome-list) | ✅ Yes | Provides classifications and additional metadata. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ✅ Yes | https://mcpbench.ai |

### 2.2 API Details (if applicable)

N/A - No direct API provided by MCP Bench itself, it consumes the official MCP Registry API.

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
| Publisher verification process exists? | ❓ Unknown | Depends on the official MCP registry. |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ❓ Unknown | Depends on the official MCP registry. |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ❌ No | All policy-related paths return 404. |
| User data collected (summary) | ❓ Unknown | Not available. |
| Analytics/tracking tools used | ✅ Yes | Google Tag Manager (from audit). |

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
| HTTPS enforced | ✅ Yes | |
| Strict-Transport-Security (HSTS) | ❌ No | |
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
| Subject | `mcpbench.ai` |

### 7.3 DNS & Hosting

| Field | Value |
|---|---|
| Provider hints | Google Cloud (A) |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Aggregates Official Data:** Draws server data from the official MCP registry.
- **Enhanced Discoverability:** Provides classifications, analytics, and filters for better server discovery.
- **Good Basic Security:** Uses HTTPS and has a valid TLS certificate.
- **Social Links:** Provides links to GitHub projects for listed servers.

### 11.2 Weaknesses & Gaps

- **Missing All Major Security Headers:** A significant gap in web security posture.
- **No Operator Transparency:** The operator is anonymous, and contact information is missing.
- **No Policies:** Lacks privacy policy, terms of service, or security policy.
- **Google Tag Manager:** Uses tracking without a clear privacy policy.
- **No Explicit Vetting Information:** While it uses official registry data, its own vetting process for additional metadata is unclear.

### 11.3 Red Flags

- The complete lack of transparency regarding the operator, coupled with the absence of privacy and security policies while using a tracking tool (GTM), is a significant red flag concerning user data and overall trustworthiness.

### 11.4 Recommendations

- **Implement All Security Headers:** Add comprehensive security headers to enhance web security.
- **Provide Operator Transparency:** Clearly identify the operator and provide contact information.
- **Publish Comprehensive Policies:** Develop and publish clear privacy, terms of service, and security policies.
- **Clarify Vetting Process:** Detail how additional metadata and classifications are generated and vetted.

### 11.5 Overall Trust Assessment

MCP Bench serves as a valuable directory for exploring MCP servers, leveraging data from the official MCP registry and enhancing it with additional metadata. However, its overall trustworthiness is severely undermined by a complete lack of transparency regarding its operator, and the absence of fundamental policies (privacy, terms, security). The website's poor web security headers and use of Google Tag Manager without a privacy policy raise significant concerns about user data handling. Users should use MCP Bench as a discovery tool but exercise extreme caution due to these critical gaps in transparency and security.

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
  "name": "MCP Bench",
  "marketplace_url": "https://mcpbench.ai",
  "source_url": "",
  "audited_at": "2025-12-13T04:58:11.731937Z",
  "checks_run": [
    "domain",
    "web"
  ],
  "errors": [],
  "domain": {
    "hostname": "mcpbench.ai",
    "registrable_domain": "mcpbench.ai",
    "dns": {
      "a": [
        "34.66.85.157"
      ],
      "aaaa": [],
      "cname": [],
      "ns": [
        "ns2.dnsowl.com",
        "ns3.dnsowl.com",
        "ns1.dnsowl.com"
      ],
      "mx": [],
      "txt": [
        "google-site-verification=OpGKlzMX4wKMCLdZyBQZKYyKKP6XvAo_5SSUeDK7bCw"
      ]
    },
    "tls": {
      "ok": true,
      "issuer": "C=US, O=Let's Encrypt, CN=E7",
      "subject": "CN=mcpbench.ai",
      "not_before": "Dec  3 10:32:04 2025 GMT",
      "not_after": "Mar  3 10:32:03 2026 GMT",
      "sha256_fingerprint": null,
      "san": [
        "mcpbench.ai"
      ],
      "error": null
    },
    "provider_hints": [],
    "reverse_dns": {
      "34.66.85.157": "157.85.66.34.bc.googleusercontent.com"
    },
    "errors": []
  },
  "web": {
    "url": "https://mcpbench.ai",
    "http": {
      "ok": true,
      "final_url": "https://mcpbench.ai",
      "status_code": 200,
      "status_chain": [
        "HTTP/2 200"
      ],
      "redirect_chain": [],
      "headers": {
        "server": "nginx/1.24.0 (Ubuntu)",
        "date": "Sat, 13 Dec 2025 04:58:13 GMT",
        "content-type": "text/html;charset=utf-8",
        "x-robots-tag": "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1",
        "x-powered-by": "Nuxt"
      },
      "response_time_ms": 498,
      "error": null
    },
    "security_headers": {
      "strict_transport_security": null,
      "content_security_policy": null,
      "x_frame_options": null,
      "x_content_type_options": null,
      "referrer_policy": null,
      "permissions_policy": null,
      "cross_origin_opener_policy": null,
      "cross_origin_resource_policy": null,
      "cross_origin_embedder_policy": null,
      "_present": [],
      "_missing": [
        "strict_transport_security",
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
        "status_code": 200,
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
    "trackers": [
      {
        "name": "Google Tag Manager",
        "type": "analytics",
        "evidence": "gtm-alpha"
      }
    ],
    "social_links": [
      {
        "type": "github",
        "url": "https://github.com/modelcontextprotocol/registry"
      },
      {
        "type": "github",
        "url": "https://github.com/neo4j-contrib/mcp-neo4j"
      },
      {
        "type": "github",
        "url": "https://github.com/shashwatgtm/gtm-expert-schema"
      },
      {
        "type": "github",
        "url": "https://github.com/byteplant-dev/byteplant-mcp"
      },
      {
        "type": "github",
        "url": "https://github.com/bahfahh/noteit-mcp"
      },
      {
        "type": "github",
        "url": "https://github.com/civicteam/civic-mcp"
      },
      {
        "type": "github",
        "url": "https://github.com/aringad/fattureincloud-mcp"
      },
      {
        "type": "github",
        "url": "https://github.com/king-of-the-grackles/reddit-research-mcp"
      },
      {
        "type": "github",
        "url": "https://github.com/homeassistant-ai/ha-mcp.git"
      },
      {
        "type": "github",
        "url": "https://github.com/domdomegg/google-drive-mcp.git"
      },
      {
        "type": "github",
        "url": "https://github.com/domdomegg/google-drive-mcp#readme"
      },
      {
        "type": "github",
        "url": "https://github.com/domdomegg/google-documents-mcp.git"
      },
      {
        "type": "github",
        "url": "https://github.com/domdomegg/google-documents-mcp#readme"
      },
      {
        "type": "github",
        "url": "https://github.com/domdomegg/google-sheets-mcp.git"
      },
      {
        "type": "github",
        "url": "https://github.com/domdomegg/google-sheets-mcp#readme"
      }
    ],
    "cookies": [],
    "server_info": {
      "server": "nginx/1.24.0 (Ubuntu)",
      "powered_by": "Nuxt"
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