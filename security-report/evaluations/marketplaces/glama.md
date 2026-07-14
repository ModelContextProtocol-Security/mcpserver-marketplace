---
title: "Glama"
url: "https://glama.ai"
source_code_url: "Unknown"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "directory"
operator: "Glama"
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "security@glama.ai"
server_count: "Unknown"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://glama.ai"
    description: "Main website"
    captured: "2026-02-04"
  - url: "https://status.glama.ai/"
    description: "Status page"
    captured: "2026-02-04"
  - url: "https://glama.ai/.well-known/security.txt"
    description: "Security.txt file"
    captured: "2026-02-04"
  - url: "https://glama.ai/policies/vulnerability-disclosure"
    description: "Vulnerability Disclosure Policy"
    captured: "2026-02-04"
---

## Overview

Glama is a platform designed to discover, connect to, index, scan, and rank Model Context Protocol (MCP) servers, clients, and tools. It emphasizes "enterprise-grade security and privacy" and aims to provide a reliable resource for the MCP ecosystem. The platform also features integration with a ChatGPT-like UI. Glama demonstrates a strong commitment to web security through its comprehensive security headers and a well-defined Vulnerability Disclosure Policy.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | Indexes, scans, and ranks MCP servers. |
| One-click install | ❓ | Not explicitly mentioned. |
| Curated list/recommendations | ✅ | Ranks servers based on security, compatibility, etc. |
| Public API | ❓ | Not explicitly mentioned; `/api` returns 404. |
| CLI tool | ❌ | Not mentioned. |
| Client integration | ✅ | Mentions integration with a ChatGPT-like UI. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | Glama | Website Title |
| Primary URL | https://glama.ai | Browser |
| Operator (company/individual) | Glama | Website content |
| Country/jurisdiction | ❓ Unknown | Not specified. |
| Contact email (general) | ❓ Unknown | Not found on site. |
| Contact email (security) | ✅ Yes | `security@glama.ai` (from security.txt and VDP). |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ❌ No | Not mentioned. |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Directory/Aggregator - Lists servers with external links | ✅ Yes | Primary function is listing tools. |
| Curated List - Manually maintained list (e.g., awesome-list) | ✅ Yes | Ranks servers based on criteria. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ✅ Yes | https://glama.ai |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|---|---|---|
| API documentation available? | ❌ No | All API-related paths return 404. |

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
| Publisher verification process exists? | ❓ Unknown | Not explicitly detailed. |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ✅ Yes | "scans, and ranks servers based on security, compatibility" (from website). |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ❌ No | All policy-related paths return 404. |
| User data collected (summary) | ❓ Unknown | Content not fetched. |
| Analytics/tracking tools used | ✅ Yes | PostHog (from audit). |

### 5.2 Terms of Service

| Question | Answer | Evidence/Source |
|---|---|---|
| Terms of service exists? | ❌ No | All policy-related paths return 404. |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ✅ Yes | https://glama.ai/policies/vulnerability-disclosure |
| Security policy URL (SECURITY.md) | ✅ Yes | `/.well-known/security.txt` points to it. |
| Vulnerability disclosure process? | ✅ Yes | Detailed VDP is available. |

---

## Part 6: Supply Chain Security

N/A - This is a directory of tools, not a hosting/execution platform.

---

## Part 7: Technical Security Posture

### 7.1 Web Security Headers

| Header | Present? | Value |
|---|---|---|
| HTTPS enforced | ✅ Yes | |
| Strict-Transport-Security (HSTS) | ✅ Yes | `max-age=31536000; includeSubDomains; preload` |
| Content-Security-Policy | ✅ Yes | Extensive and detailed. |
| X-Frame-Options | ✅ Yes | `SAMEORIGIN` |
| X-Content-Type-Options | ✅ Yes | `nosniff` |
| Referrer-Policy | ✅ Yes | `strict-origin-when-cross-origin` |
| Permissions-Policy | ✅ Yes | Comprehensive list of permissions. |
| Cross-Origin-Opener-Policy | ✅ Yes | `same-origin-allow-popups` |
| Cross-Origin-Resource-Policy | ✅ Yes | `same-origin` |

### 7.2 TLS Certificate

| Field | Value |
|---|---|
| Issuer | ZeroSSL |
| Subject | `glama.ai` |

### 7.3 DNS & Hosting

| Field | Value |
|---|---|
| Provider hints | Cloudflare (NS), Google Workspace (MX), Fly.io (Reverse DNS) |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Exceptional Web Security Headers:** Implements a very comprehensive set of security headers, including a strong CSP, HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, Cross-Origin-Opener-Policy, and Cross-Origin-Resource-Policy.
- **Vulnerability Disclosure Policy (VDP):** A clear and detailed VDP is available, including a dedicated security contact email.
- **Status Page:** Provides a public status page, indicating operational transparency.
- **Explicit Vetting:** Claims to scan and rank servers based on security.
- **Clear Purpose:** Focuses on discovery, indexing, and ranking of MCP servers, clients, and tools.

### 11.2 Weaknesses & Gaps

- **Missing Privacy Policy and Terms of Service:** Despite excellent technical security, the absence of accessible privacy and terms of service documents is a significant legal and transparency gap, especially given its use of analytics (PostHog).
- **No Operator Transparency:** Details about the operating entity beyond "Glama" are not available.
- **Placeholder Security Contact in `security.txt`:** While the VDP gives `security@glama.ai`, the `security.txt` file initially showed `security@example.com`.

### 11.3 Red Flags

- The discrepancy between robust technical security and the absence of accessible privacy and terms of service policies is a red flag. It suggests a potential disconnect between technical implementation and legal/ethical transparency.

### 11.4 Recommendations

- **Publish Comprehensive Privacy Policy and Terms of Service:** These documents are essential for any public-facing platform, especially one that claims "enterprise-grade security and privacy" and uses analytics.
- **Correct `security.txt` Placeholder:** Ensure the `security.txt` file is accurate and consistent with the VDP.
- **Increase Operator Transparency:** Provide more details about the Glama operating entity.

### 11.5 Overall Trust Assessment

Glama stands out with its exceptionally strong web security headers and a commendable Vulnerability Disclosure Policy, indicating a high level of technical security awareness. Its mission to scan and rank MCP servers also points towards a proactive approach to ecosystem safety. However, the absence of accessible privacy and terms of service policies is a critical flaw, especially for a platform emphasizing "enterprise-grade privacy" and utilizing analytics. This lack of legal transparency, coupled with an anonymous operator, creates a significant trust gap. While technically secure, users need clear assurances about data handling and terms of use to fully trust Glama. It has the potential to be highly trustworthy but needs to close its policy and transparency gaps.

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
  "name": "Glama",
  "marketplace_url": "https://glama.ai",
  "source_url": "",
  "audited_at": "2025-12-13T04:58:11.738545Z",
  "checks_run": [
    "domain",
    "web"
  ],
  "errors": [],
  "domain": {
    "hostname": "glama.ai",
    "registrable_domain": "glama.ai",
    "dns": {
      "a": [
        "66.241.124.71",
        "37.16.29.120"
      ],
      "aaaa": [
        "2a09:8280:1::5c:44fc:0"
      ],
      "cname": [],
      "ns": [
        "isaac.ns.cloudflare.com",
        "davina.ns.cloudflare.com"
      ],
      "mx": [
        "smtp.google.com"
      ],
      "txt": [
        "domain-verification=75cb76e4e272f2a5669cef9f2a1e9e622f146f5e3f0f0e4e81d6cd5ea8947eb9",
        "google-site-verification=_PZWHb4k00HAd5fZiXICbK4VUsYy-ZcQbmcvPjl21qo",
        "google-site-verification=qwC-QSzoqkPqWT3ranYq74cRxYijlNPDkt-L1YAJf6U",
        "v=spf1 include:amazonses.com include:_spf.google.com ~all",
        "yandex-verification: 615ed967bdc3be00",
        "ahrefs-site-verification_f6bad253fc7c9ba948fb72dcb33020f2db2166066d37e08041d6cd5ea8947eb9"
      ]
    },
    "tls": {
      "ok": true,
      "issuer": "C=AT, O=ZeroSSL, CN=ZeroSSL RSA Domain Secure Site CA",
      "subject": "CN=glama.ai",
      "not_before": "May 16 00:00:00 2025 GMT",
      "not_after": "May 16 23:59:59 2026 GMT",
      "sha256_fingerprint": null,
      "san": [
        "glama.ai",
        "www.glama.ai"
      ],
      "error": null
    },
    "provider_hints": [
      "Cloudflare (NS)",
      "Google Workspace (MX)"
    ],
    "reverse_dns": {
      "66.241.124.71": "ip-66-241-124-71.shared.customer.flyio.net",
      "37.16.29.120": "ip-37-16-29-120.customer.flyio.net"
    },
    "errors": []
  },
  "web": {
    "url": "https://glama.ai",
    "http": {
      "ok": true,
      "final_url": "/mcp",
      "status_code": 103,
      "status_chain": [
        "HTTP/2 103"
      ],
      "redirect_chain": [
        "/mcp"
      ],
      "headers": {
        "alt-svc": "h3=\":443\"; ma=2592000",
        "link": "<https://static.glama.ai/client/fonts/inter/Inter-VariableFont.woff2>; rel=preload; as=font; crossorigin=\"anonymous\", <https://static.glama.ai/client/assets/global-DMmRoD5W.css>; rel=preload; as=style, <https://static.glama.ai/client/assets/manifest-c05a90bd.js>; rel=preload; as=script; crossorigin=anonymous, <https://static.glama.ai/client/entry.client-D3xfUc2j.js>; rel=preload; as=script; crossorigin=anonymous, <https://static.glama.ai/client/ui-5GkDKlAJ.js>; rel=preload; as=script; crossorigin=anonymous, <https://static.glama.ai/client/client-D9W5io62.js>; rel=preload; as=script; crossorigin=anonymous, <https://static.glama.ai/client/chunk-WWGJGFF6-YM2jJzZi.js>; rel=preload; as=script; crossorigin=anonymous, <https://static.glama.ai/client/rolldown-runtime-D66wRDZ4.js>; rel=preload; as=script; crossorigin=anonymous, <https://static.glama.ai/client/preload-helper--1o5oJ3j.js>; rel=preload; as=script; crossorigin=anonymous, <https://static.glama.ai/client/root-CsJDirNX.js>; rel=preload; as=script; crossorigin=anonymous, <https://static.glama.ai/client/Link-EDoh5618.js>; rel=preload; as=script; crossorigin=anonymous, <https://static.glama.ai/client/NotFoundErrorDialog-Cr2pP1UE.js>; rel=preload; as=script; crossorigin=anonymous, <https://static.glama.ai/client/CommandBar-CWWK1zLU.js>; rel=preload; as=script; crossorigin=anonymous, <https://static.glama.ai/client/useModal-BM7i856a.js>; rel=preload; as=script; crossorigin=anonymous, <https://static.glama.ai/client/usePublicConfig-Cg4lMEAD.js>; rel=preload; as=script; crossorigin=anonymous, <https://static.glama.ai/client/useVisitor-Bn_z1IwC.js>; rel=preload; as=script; crossorigin=anonymous",
        "server": "Caddy",
        "accept-ch": "Sec-CH-DPR, Sec-CH-Width, Sec-CH-Viewport-Width",
        "content-security-policy": "base-uri 'self'; connect-src 'self' https://*.google-analytics.com https://*.intercom.io https://*.intercomcdn.com https://*.intercomcdn.eu https://*.intercomusercontent.com https://*.sentry.io https://*.stripe.com/ https://accounts.google.com/gsi/ https://connect.facebook.net https://conversions-config.reddit.com/ https://maps.googleapis.com/ https://pixel-config.reddit.com https://static.glama.ai/ https://www.facebook.com https://www.redditstatic.com wss://*.intercom.io; default-src 'self' https://static.glama.ai/; font-src 'self' data: https://*.intercomcdn.com https://static.glama.ai/; frame-src 'self' https://*.stripe.com/ https://accounts.google.com/gsi/ https://demo.arcade.software/ https://intercom-sheets.com https://static.glama.ai/ https://www.facebook.com https://www.redditstatic.com https://www.youtube.com; frame-ancestors 'self'; img-src 'self' blob: data: https://*.intercom-attachments-1.com https://*.intercom-attachments-2.com https://*.intercom-attachments-3.com https://*.intercom-attachments-4.com https://*.intercom-attachments-5.com https://*.intercom-attachments-6.com https://*.intercom-attachments-7.com https://*.intercom-attachments-8.com https://*.intercom-attachments-9.com https://*.intercom-attachments.eu https://*.intercom.io https://*.intercomassets.com https://*.intercomassets.eu https://*.intercomcdn.com https://*.intercomcdn.eu https://*.intercomusercontent.com https://*.reddit.com/ https://*.stripe.com https://glama.ai/uploads/ https://i.ytimg.com https://static.glama.ai/ https://www.facebook.com https://www.googletagmanager.com; media-src 'self' https://*.intercomcdn.com https://*.intercomcdn.eu https://static.glama.ai/; object-src 'none'; script-src 'nonce-4794081583a96afa1c03c78204cf03b8' 'strict-dynamic' 'wasm-unsafe-eval' https://*.intercom.io https://*.stripe.com/ https://accounts.google.com/gsi/client https://connect.facebook.net https://googletagmanager.com https://js.intercomcdn.com https://map... [truncated]",
        "cross-origin-opener-policy": "same-origin-allow-popups",
        "cross-origin-resource-policy": "same-origin",
        "date": "Sat, 13 Dec 2025 04:58:14 GMT",
        "location": "/mcp",
        "permissions-policy": "attribution-reporting=(), bluetooth=(), browsing-topics=(), compute-pressure=(), display-capture=(), gamepad=(), hid=(), idle-detection=(), local-fonts=(), magnetometer=(), midi=(), otp-credentials=(), publickey-credentials-create=(), publickey-credentials-get=(), screen-wake-lock=(), serial=(), storage-access=(), usb=(), window-management=(), xr-spatial-tracking=(), camera=(self), microphone=(self), geolocation=(self), identity-credentials-get=(self), accelerometer=(*), autoplay=(*), encrypted-media=(*), fullscreen=(*), gyroscope=(*), picture-in-picture=(*), payment=(*)",
        "referrer-policy": "strict-origin-when-cross-origin",
        "set-cookie": "_glama=019b1612-de44-757a-a32b-ebf4ba93cbf6.iep5yeYcIM4MvC%2BR9jE9yIKR7yjoFAscjSkwFYbe5Co; Path=/;Expires=Mon, 12 Jan 2026 04:58:13 GMT; HttpOnly; Secure; SameSite=Lax\n_glama=019b1612-df00-759e-a691-d5b7d98dc37d.r1Ctm3Efcjcm6OXnv8RJs8KmzD7VA6QoHbDzw09LLjY; Path=/;Expires=Mon, 12 Jan 2026 04:58:14 GMT; HttpOnly; Secure; SameSite=Lax",
        "strict-transport-security": "max-age=31536000; includeSubDomains; preload",
        "vary": "Sec-CH-DPR, Sec-CH-Width, Sec-CH-Viewport-Width",
        "via": "1.1 Caddy",
        "x-content-type-options": "nosniff",
        "x-frame-options": "SAMEORIGIN",
        "content-length": "0",
        "content-type": "text/html; charset=utf-8",
        "server-timing": "shell;dur=11.38;desc=\"Shell Render\""
      },
      "response_time_ms": 813,
      "error": null
    },
    "security_headers": {
      "strict_transport_security": "max-age=31536000; includeSubDomains; preload",
      "content_security_policy": "base-uri 'self'; connect-src 'self' https://*.google-analytics.com https://*.intercom.io https://*.intercomcdn.com https://*.intercomcdn.eu https://*.intercomusercontent.com https://*.sentry.io https://*.stripe.com/ https://accounts.google.com/gsi/ https://connect.facebook.net https://conversions-config.reddit.com/ https://maps.googleapis.com/ https://pixel-config.reddit.com https://static.glama.ai/ https://www.facebook.com https://www.redditstatic.com wss://*.intercom.io; default-src 'self' https://static.glama.ai/; font-src 'self' data: https://*.intercomcdn.com https://static.glama.ai/; frame-src 'self' https://*.stripe.com/ https://accounts.google.com/gsi/ https://demo.arcade.software/ https://intercom-sheets.com https://static.glama.ai/ https://www.facebook.com https://www.redditstatic.com https://www.youtube.com; frame-ancestors 'self'; img-src 'self' blob: data: https://*.intercom-attachments-1.com https://*.intercom-attachments-2.com https://*.intercom-attachments-3.com https://*.intercom-attachments-4.com https://*.intercom-attachments-5.com https://*.intercom-attachments-6.com https://*.intercom-attachments-7.com https://*.intercom-attachments-8.com https://*.intercom-attachments-9.com https://*.intercom-attachments.eu https://*.intercom.io https://*.intercomassets.com https://*.intercomassets.eu https://*.intercomcdn.com https://*.intercomcdn.eu https://*.intercomusercontent.com https://*.reddit.com/ https://*.stripe.com https://glama.ai/uploads/ https://i.ytimg.com https://static.glama.ai/ https://www.facebook.com https://www.googletagmanager.com; media-src 'self' https://*.intercomcdn.com https://*.intercomcdn.eu https://static.glama.ai/; object-src 'none'; script-src 'nonce-4794081583a96afa1c03c78204cf03b8' 'strict-dynamic' 'wasm-unsafe-eval' https://*.intercom.io https://*.stripe.com/ https://accounts.google.com/gsi/client https://connect.facebook.net https://googletagmanager.com https://js.intercomcdn.com https://map... [truncated]",
      "x_frame_options": "SAMEORIGIN",
      "x_content_type_options": "nosniff",
      "referrer_policy": "strict-origin-when-cross-origin",
      "permissions_policy": "attribution-reporting=(), bluetooth=(), browsing-topics=(), compute-pressure=(), display-capture=(), gamepad=(), hid=(), idle-detection=(), local-fonts=(), magnetometer=(), midi=(), otp-credentials=(), publickey-credentials-create=(), publickey-credentials-get=(), screen-wake-lock=(), serial=(), storage-access=(), usb=(), window-management=(), xr-spatial-tracking=(), camera=(self), microphone=(self), geolocation=(self), identity-credentials-get=(self), accelerometer=(*), autoplay=(*), encrypted-media=(*), fullscreen=(*), gyroscope=(*), picture-in-picture=(*), payment=(*)",
      "cross_origin_opener_policy": "same-origin-allow-popups",
      "cross_origin_resource_policy": "same-origin",
      "cross_origin_embedder_policy": null,
      "_present": [
        "strict_transport_security",
        "content_security_policy",
        "x_frame_options",
        "x_content_type_options",
        "referrer_policy",
        "permissions_policy",
        "cross_origin_opener_policy",
        "cross_origin_resource_policy"
      ],
      "_missing": [
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
        "status_code": 200,
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
        "status_code": 302,
        "redirect_to": "https://status.glama.ai/"
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
        "name": "PostHog",
        "type": "analytics",
        "evidence": "POSTHOG"
      }
    ],
    "social_links": [],
    "cookies": [
      {
        "name": "_glama",
        "secure": true,
        "httponly": true,
        "samesite": "lax"
      },
      {
        "name": "_glama",
        "secure": true,
        "httponly": true,
        "samesite": "lax"
      }
    ],
    "server_info": {
      "server": "Caddy",
      "via": "1.1 Caddy"
    },
    "errors": []
  },
  "success": true
}
```