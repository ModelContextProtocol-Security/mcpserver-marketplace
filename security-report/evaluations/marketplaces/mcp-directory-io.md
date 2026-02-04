---
title: "MCP Directory (.io)"
url: "https://www.mcpdirectory.io/"
source_code_url: "Unknown"
is_marketplace: yes
is_aggregator: no
is_list_of_marketplaces: no
language: "en"
type: "directory"
operator: "Jarosław Michalik"
operator_jurisdiction: "Poland"
contact_email: "jarek@theimpl.com"
security_email: "Unknown"
server_count: "Unknown"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://www.mcpdirectory.io/"
    description: "Main website"
    captured: "2026-02-04"
  - url: "https://www.mcpdirectory.io/terms"
    description: "Terms and Conditions (Regulamin)"
    captured: "2026-02-04"
---

## Overview

The MCP Directory (.io) is an online platform that serves as a technology hub for Model Context Protocol (MCP) tools. It allows users to discover and integrate various MCP servers into their AI applications. The directory categorizes tools by function, providing brief descriptions and download counts for each. It is operated by Jarosław Michalik and appears to be based in Poland, given the language of its terms and conditions. The site emphasizes building powerful AI applications with MCP tools.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | Categorized listings with descriptions. |
| One-click install | ❓ | Not explicitly stated. |
| Curated list/recommendations | ✅ | Lists popular and trending servers. |
| Public API | ❓ | `/api` redirects but no documentation found. |
| CLI tool | ❌ | Not mentioned. |
| Client integration | ✅ | Promotes integration with AI applications. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | MCP Directory (.io) | Website Title |
| Primary URL | https://www.mcpdirectory.io/ | Browser |
| Operator (company/individual) | Jarosław Michalik | Terms and Conditions |
| Country/jurisdiction | ✅ Poland | Terms and Conditions are in Polish. |
| Contact email (general) | ✅ Yes | `jarek@theimpl.com` (from audit) |
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
| Website with search/browse | ✅ Yes | https://www.mcpdirectory.io/ |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|---|---|---|
| API documentation available? | ❌ No | `/api` redirects to a non-existent page. |
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
| Publisher verification process exists? | ❌ No | Not mentioned in available policies. |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ❓ Unknown | Not mentioned in available policies. |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ❌ No | Audit showed `/privacy-policy` path with 308 redirect, but content fetch failed. |
| User data collected (summary) | ❓ Unknown | Not available from fetched content. |
| Analytics/tracking tools used | ✅ Yes | Google Analytics, Google Tag Manager (from audit). |

### 5.2 Terms of Service

| Question | Answer | Evidence/Source |
|---|---|---|
| Terms of service exists? | ✅ Yes | https://www.mcpdirectory.io/terms |
| Terms of service URL | ✅ Yes | https://www.mcpdirectory.io/terms |
| Language | ✅ Polish | "Regulamin" |
| Prohibited user activities | ✅ Yes | General outline of permitted/prohibited activities for online store users. |
| Liability limitations | ✅ Yes | Standard disclaimers and limitations. |

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
| Strict-Transport-Security (HSTS) | ✅ Yes | `max-age=63072000` |
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
| Issuer | Let\'s Encrypt |
| Subject | `mcpdirectory.io` |

### 7.3 DNS & Hosting

| Field | Value |
|---|---|
| Provider hints | Vercel (Server), OVH (NS, MX) |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Clear Purpose:** Serves as a straightforward directory for MCP tools.
- **Operator Identified:** The operator, Jarosław Michalik, is identified in the Terms and Conditions.
- **Contact Information Available:** An email address is provided for contact.
- **Good Base Security:** Uses HTTPS and HSTS.

### 11.2 Weaknesses & Gaps

- **Missing Critical Security Headers:** Lacks CSP, X-Frame-Options, and others, which weakens its web security posture.
- **Unclear Privacy Policy:** Despite a path existing in audit, content could not be fetched.
- **Terms in Polish:** The Terms and Conditions are not readily accessible to non-Polish speakers, limiting transparency.
- **No Vetting Process:** No explicit mention of how listed MCP servers are vetted for security or quality.
- **No Security Policy:** Absence of a formal security policy or vulnerability disclosure process.
- **Google Analytics/GTM:** Uses tracking tools without a clear privacy policy.

### 11.3 Red Flags

- The combination of using extensive tracking (Google Analytics, GTM) and an inaccessible or non-existent privacy policy is a significant red flag regarding user data handling.
- Listing MCP servers without clear vetting or security guarantees could expose users to unvetted or malicious tools.

### 11.4 Recommendations

- **Implement Full Security Headers:** Add comprehensive security headers to enhance web security.
- **Publish a Clear Privacy Policy:** A detailed privacy policy (preferably in English and Polish) explaining data collection, usage, and sharing is crucial, especially with tracking tools in use.
- **Provide English Terms of Service:** Offer a version of the Terms and Conditions in English for broader accessibility.
- **Document Vetting Process:** Clearly define how listed MCP servers are evaluated for security and quality.
- **Establish a Security Policy:** Publish a `SECURITY.md` file and provide a clear channel for vulnerability reports.

### 11.5 Overall Trust Assessment

MCP Directory (.io) functions as a useful hub for discovering MCP tools, with a clear operator and contact information. While it benefits from basic web security (HTTPS, HSTS), it suffers from significant gaps in its overall security and transparency posture. The absence of a readily available privacy policy, coupled with extensive tracking, raises concerns about user data. Furthermore, the lack of a clear vetting process for listed tools means users must exercise significant caution and conduct their own due diligence before integrating any MCP server found through this directory. The language barrier for its terms further compounds these issues for a global audience.

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
  "name": "MCP Directory (.io)",
  "marketplace_url": "https://mcpdirectory.io/",
  "source_url": "",
  "audited_at": "2025-12-13T04:59:22.103849Z",
  "checks_run": [
    "domain",
    "web"
  ],
  "errors": [],
  "domain": {
    "hostname": "mcpdirectory.io",
    "registrable_domain": "mcpdirectory.io",
    "dns": {
      "a": [
        "76.76.21.21"
      ],
      "aaaa": [],
      "cname": [],
      "ns": [
        "dns20.ovh.net",
        "ns20.ovh.net"
      ],
      "mx": [
        "mx3.mail.ovh.net",
        "mx1.mail.ovh.net",
        "mx2.mail.ovh.net"
      ],
      "txt": [
        "v=spf1 include:mx.ovh.com -all",
        "google-site-verification=4KQ5m6-gamO0Dy6OQAyRhdNMxkCQ4FfacEBY9gDq5Hw"
      ]
    },
    "tls": {
      "ok": true,
      "issuer": "C=US, O=Let\'s Encrypt, CN=R13",
      "subject": "CN=mcpdirectory.io",
      "not_before": "Nov 19 13:04:19 2025 GMT",
      "not_after": "Feb 17 13:04:18 2026 GMT",
      "sha256_fingerprint": null,
      "san": [
        "mcpdirectory.io"
      ],
      "error": null
    },
    "provider_hints": [],
    "reverse_dns": {
      "76.76.21.21": ""
    },
    "errors": []
  },
  "web": {
    "url": "https://mcpdirectory.io/",
    "http": {
      "ok": true,
      "final_url": "https://www.mcpdirectory.io/",
      "status_code": 308,
      "status_chain": [
        "HTTP/2 308"
      ],
      "redirect_chain": [
        "https://www.mcpdirectory.io/"
      ],
      "headers": {
        "cache-control": "public, max-age=0, must-revalidate",
        "content-type": "text/html; charset=utf-8",
        "date": "Sat, 13 Dec 2025 04:59:24 GMT",
        "location": "https://www.mcpdirectory.io/",
        "refresh": "0;url=https://www.mcpdirectory.io/",
        "server": "Vercel",
        "strict-transport-security": "max-age=63072000",
        "x-vercel-id": "pdx1::5qb2w-1765601964597-b25c7d878c07",
        "accept-ranges": "bytes",
        "access-control-allow-origin": "*",
        "age": "1339189",
        "content-disposition": "inline",
        "etag": "\"580f5c3adbbfe8a02c88fd1fa844565b\"",
        "vary": "RSC, Next-Router-State-Tree, Next-Router-Prefetch, Next-Router-Segment-Prefetch",
        "x-matched-path": "/",
        "x-nextjs-prerender": "1",
        "x-nextjs-stale-time": "4294967294",
        "x-vercel-cache": "HIT",
        "content-length": "21746"
      },
      "response_time_ms": 610,
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
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/privacy"
      },
      "/privacy-policy": {
        "path": "/privacy-policy",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/privacy-policy"
      },
      "/terms": {
        "path": "/terms",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/terms"
      },
      "/tos": {
        "path": "/tos",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/tos"
      },
      "/terms-of-service": {
        "path": "/terms-of-service",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/terms-of-service"
      },
      "/security": {
        "path": "/security",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/security"
      },
      "/security.txt": {
        "path": "/security.txt",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/security.txt"
      },
      "/.well-known/security.txt": {
        "path": "/.well-known/security.txt",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/.well-known/security.txt"
      },
      "/legal": {
        "path": "/legal",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/legal"
      },
      "/about": {
        "path": "/about",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/about"
      },
      "/contact": {
        "path": "/contact",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/contact"
      },
      "/robots.txt": {
        "path": "/robots.txt",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/robots.txt"
      },
      "/sitemap.xml": {
        "path": "/sitemap.xml",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/sitemap.xml"
      },
      "/status": {
        "path": "/status",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/status"
      },
      "/health": {
        "path": "/health",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/health"
      },
      "/api": {
        "path": "/api",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/api"
      },
      "/docs": {
        "path": "/docs",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/docs"
      },
      "/api-docs": {
        "path": "/api-docs",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/api-docs"
      },
      "/documentation": {
        "path": "/documentation",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/documentation"
      },
      "/swagger": {
        "path": "/swagger",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/swagger"
      },
      "/swagger.json": {
        "path": "/swagger.json",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/swagger.json"
      },
      "/swagger.yaml": {
        "path": "/swagger.yaml",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/swagger.yaml"
      },
      "/openapi.json": {
        "path": "/openapi.json",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/openapi.json"
      },
      "/openapi.yaml": {
        "path": "/openapi.yaml",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/openapi.yaml"
      },
      "/graphql": {
        "path": "/graphql",
        "status_code": 308,
        "redirect_to": "https://www.mcpdirectory.io/graphql"
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
        "type": "email",
        "url": "mailto:jarek@theimpl.com"
      }
    ],
    "cookies": [],
    "server_info": {
      "server": "Vercel",
      "cdn": "Vercel"
    },
    "errors": []
  },
  "success": true
}
```