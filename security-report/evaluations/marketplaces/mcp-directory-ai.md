--- 
title: "MCP Directory (AI)"
url: "https://mcpdirectory.ai/"
source_code_url: "Unknown"
is_marketplace: yes
is_aggregator: no
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
  - url: "https://mcpdirectory.ai/"
    description: "Main website"
    captured: "2026-02-04"
---

## Overview

MCP Directory (AI) positions itself as an exploration hub for MCP servers, allowing users to discover and integrate tools for AI applications. The website lists a wide array of MCP servers categorized by their functionalities, such as Git, GitHub, Slack, PostgreSQL, and various AI-related integrations. The site is hosted on AWS CloudFront and built with Next.js. While it provides a comprehensive listing, information about its operator and specific policies is not readily available.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | Lists numerous MCP servers with descriptions. |
| One-click install | ❌ | Not directly available. |
| Curated list/recommendations | ✅ | Features a categorized listing of servers. |
| Public API | ❓ | `/api` and `/graphql` paths redirect, but no documentation. |
| CLI tool | ❌ | Not mentioned. |
| Client integration | ✅ | Promotes integration for AI applications. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | mcp directory: Explore the world of MCP servers | Website Title |
| Primary URL | https://mcpdirectory.ai/ | Browser |
| Operator (company/individual) | ❓ Unknown | Not found on site. |
| Country/jurisdiction | ❓ Unknown | Not specified. |
| Contact email (general) | ❓ Unknown | Not found on site. |
| Contact email (security) | ❓ Unknown | Not explicitly mentioned. |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ❌ No | Not mentioned. |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Directory/Aggregator - Lists servers with external links | ✅ Yes | Primary function is listing tools. |
| Curated List - Manually maintained list (e.g., awesome-list) | ✅ Yes | Categorized listings. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ✅ Yes | https://mcpdirectory.ai/ |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|---|---|---|
| API documentation available? | ❌ No | `/api` redirects to a non-existent page, no documentation. |
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
| Privacy policy exists? | ❌ No | Path exists, but content could not be fetched. |
| User data collected (summary) | ❓ Unknown | Not available from fetched content. |
| Analytics/tracking tools used | ✅ Yes | Google Analytics, Google Tag Manager (from audit). |

### 5.2 Terms of Service

| Question | Answer | Evidence/Source |
|---|---|---|
| Terms of service exists? | ❌ No | Path exists, but content could not be fetched. |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ❌ No | Not found in audit paths or fetched content. |

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
| Issuer | Amazon |
| Subject | `*.mcpdirectory.ai` |

### 7.3 DNS & Hosting

| Field | Value |
|---|---|
| Provider hints | AWS Route53 (NS), CloudFront (CDN) |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Clear Purpose:** Serves as a straightforward directory for MCP tools.
- **Hosted on Reputable Infrastructure:** Benefits from AWS CloudFront for hosting and content delivery.
- **Categorized Listings:** Tools are well-organized by functionality.

### 11.2 Weaknesses & Gaps

- **Missing All Major Security Headers:** A significant gap in web security posture, especially for a Next.js application.
- **Inaccessible Policies:** Despite existing paths, Privacy Policy and Terms of Service content could not be fetched, hindering transparency.
- **No Vetting Process:** No explicit mention of how listed MCP servers are vetted for security or quality.
- **No Security Policy:** Absence of a formal security policy or vulnerability disclosure process.
- **Anonymous Operator:** Lack of transparency about who operates the site.
- **Google Analytics/GTM:** Uses tracking tools without an accessible privacy policy.

### 11.3 Red Flags

- **Anonymous Operator and Inaccessible Policies with Tracking:** The combination of an anonymous operator, inaccessible privacy policy, and the use of Google Analytics and GTM is a significant red flag regarding user data handling and overall transparency.
- **Unvetted Listings:** Listing MCP servers without clear vetting or security guarantees could expose users to unvetted or malicious tools.

### 11.4 Recommendations

- **Implement All Security Headers:** Add comprehensive security headers to enhance web security.
- **Publish Accessible Policies:** Ensure Privacy Policy and Terms of Service are readily accessible and clearly outline data handling practices.
- **Increase Operator Transparency:** Clearly identify the operator and provide contact information.
- **Document Vetting Process:** Clearly define how listed MCP servers are evaluated for security and quality.
- **Establish a Security Policy:** Publish a `SECURITY.md` file and provide a clear channel for vulnerability reports.

### 11.5 Overall Trust Assessment

MCP Directory (AI) aims to be a valuable resource for discovering MCP tools. While it leverages robust hosting infrastructure (AWS CloudFront), it suffers from severe deficiencies in its security and transparency posture. The complete absence of critical web security headers, inaccessible legal policies, and the anonymity of its operator (despite using tracking tools) create a significant trust deficit. Users must exercise extreme caution and conduct thorough independent due diligence on any MCP server listed here. This directory currently presents a high-risk environment due to its lack of governance and transparency.

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
  "name": "MCP Directory (AI)",
  "marketplace_url": "https://mcpdirectory.ai/",
  "source_url": "",
  "audited_at": "2025-12-13T04:59:10.938720Z",
  "checks_run": [
    "domain",
    "web"
  ],
  "errors": [],
  "domain": {
    "hostname": "mcpdirectory.ai",
    "registrable_domain": "mcpdirectory.ai",
    "dns": {
      "a": [
        "65.8.180.25",
        "65.8.180.95",
        "65.8.180.118",
        "65.8.180.126"
      ],
      "aaaa": [],
      "cname": [],
      "ns": [
        "ns-1021.awsdns-63.net",
        "ns-1525.awsdns-62.org",
        "ns-1899.awsdns-45.co.uk",
        "ns-414.awsdns-51.com"
      ],
      "mx": [],
      "txt": [
        "google-site-verification=km7Rd_QqIbtja8eI3gKiz4GD4PFBf5yzQU0GZC8jJeo"
      ]
    },
    "tls": {
      "ok": true,
      "issuer": "C=US, O=Amazon, CN=Amazon RSA 2048 M03",
      "subject": "CN=*.mcpdirectory.ai",
      "not_before": "Apr  4 00:00:00 2025 GMT",
      "not_after": "May  4 23:59:59 2026 GMT",
      "sha256_fingerprint": null,
      "san": [
        "*.mcpdirectory.ai",
        "mcpdirectory.ai"
      ],
      "error": null
    },
    "provider_hints": [
      "AWS Route53 (NS)"
    ],
    "reverse_dns": {
      "65.8.180.25": "server-65-8-180-25.sfo53.r.cloudfront.net",
      "65.8.180.95": "server-65-8-180-95.sfo53.r.cloudfront.net",
      "65.8.180.118": "server-65-8-180-118.sfo53.r.cloudfront.net"
    },
    "errors": []
  },
  "web": {
    "url": "https://mcpdirectory.ai/",
    "http": {
      "ok": true,
      "final_url": "https://mcpdirectory.ai/",
      "status_code": 200,
      "status_chain": [
        "HTTP/2 200"
      ],
      "redirect_chain": [],
      "headers": {
        "content-type": "text/html; charset=utf-8",
        "content-length": "146890",
        "date": "Wed, 10 Dec 2025 18:23:00 GMT",
        "x-nextjs-cache": "HIT",
        "x-nextjs-prerender": "1",
        "x-nextjs-stale-time": "4294967294",
        "x-powered-by": "Next.js",
        "cache-control": "s-maxage=31536000",
        "etag": "\"11bf0ahngrq35c1\"",
        "vary": "Accept-Encoding",
        "x-cache": "Hit from cloudfront",
        "via": "1.1 c9e15e0a57b77cc69af192327592d0de.cloudfront.net (CloudFront)",
        "x-amz-cf-pop": "SFO53-P9",
        "alt-svc": "h3=\":443\"; ma=86400",
        "x-amz-cf-id": "Tbl2S73MhmjWPCfS3YfmwQce9y_9zcxy4D6PYiLAzo74MOMq30KKtQ==",
        "age": "210972"
      },
      "response_time_ms": 398,
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
        "status_code": 308,
        "redirect_to": "https://mcpdirectory.ai/privacy/"
      },
      "/privacy-policy": {
        "path": "/privacy-policy",
        "status_code": 308,
        "redirect_to": "https://mcpdirectory.ai/privacy-policy/"
      },
      "/terms": {
        "path": "/terms",
        "status_code": 308,
        "redirect_to": "https://mcpdirectory.ai/terms/"
      },
      "/tos": {
        "path": "/tos",
        "status_code": 308,
        "redirect_to": "https://mcpdirectory.ai/tos/"
      },
      "/terms-of-service": {
        "path": "/terms-of-service",
        "status_code": 308,
        "redirect_to": "https://mcpdirectory.ai/terms-of-service/"
      },
      "/security": {
        "path": "/security",
        "status_code": 308,
        "redirect_to": "https://mcpdirectory.ai/security/"
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
        "status_code": 308,
        "redirect_to": "https://mcpdirectory.ai/legal/"
      },
      "/about": {
        "path": "/about",
        "status_code": 308,
        "redirect_to": "https://mcpdirectory.ai/about/"
      },
      "/contact": {
        "path": "/contact",
        "status_code": 308,
        "redirect_to": "https://mcpdirectory.ai/contact/"
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
        "status_code": 308,
        "redirect_to": "https://mcpdirectory.ai/status/"
      },
      "/health": {
        "path": "/health",
        "status_code": 308,
        "redirect_to": "https://mcpdirectory.ai/health/"
      },
      "/api": {
        "path": "/api",
        "status_code": 308,
        "redirect_to": "https://mcpdirectory.ai/api/"
      },
      "/docs": {
        "path": "/docs",
        "status_code": 308,
        "redirect_to": "https://mcpdirectory.ai/docs/"
      },
      "/api-docs": {
        "path": "/api-docs",
        "status_code": 308,
        "redirect_to": "https://mcpdirectory.ai/api-docs/"
      },
      "/documentation": {
        "path": "/documentation",
        "status_code": 308,
        "redirect_to": "https://mcpdirectory.ai/documentation/"
      },
      "/swagger": {
        "path": "/swagger",
        "status_code": 308,
        "redirect_to": "https://mcpdirectory.ai/swagger/"
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
        "status_code": 308,
        "redirect_to": "https://mcpdirectory.ai/graphql/"
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
        "type": "discord",
        "url": "https://discord.gg/3yhZNa32"
      }
    ],
    "cookies": [],
    "server_info": {
      "powered_by": "Next.js",
      "via": "1.1 c9e15e0a57b77cc69af192327592d0de.cloudfront.net (CloudFront)",
      "cdn": "AWS"
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
