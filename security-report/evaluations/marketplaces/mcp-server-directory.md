---
title: "MCP Server Directory"
url: "https://mcpserverdirectory.org/"
source_code_url: "https://github.com/mcpserverdirectory"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "directory"
operator: "MCP Server Directory"
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "Unknown"
server_count: "~2500"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://mcpserverdirectory.org/"
    description: "Main website"
    captured: "2026-02-04"
  - url: "https://mcpserverdirectory.org/privacy-policy"
    description: "Privacy Policy"
    captured: "2026-02-04"
  - url: "https://mcpserverdirectory.org/terms-of-service"
    description: "Terms of Service"
    captured: "2026-02-04"
---

## Overview

MCP Server Directory is a web-based directory that lists over 2500 Model Context Protocol (MCP) servers and resources. It allows users to discover and filter MCP servers by category. The marketplace appears to be operated by an entity named "MCP Server Directory," with jurisdiction and specific contact information not readily available. The site primarily acts as an aggregator, providing links to external resources, mainly GitHub repositories.

## Features Summary

*Quick reference - details in Part 2*

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | Website with category filtering. |
| One-click install | ❌ | Links to external source code, no direct installation. |
| Curated list/recommendations | ✅ | "Featured servers" are highlighted on the main page. |
| Public API | ❓ | The `/api` path returns a 404; no API documentation found. |
| CLI tool | ❌ | No CLI tool is mentioned. |
| Client integration | ❓ | No specific client integrations are listed. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | MCP Server Directory | Website Title |
| Primary URL | https://mcpserverdirectory.org/ | Browser |
| Operator (company/individual) | MCP Server Directory | Terms of Service |
| Country/jurisdiction | ❓ Unknown | Not specified in ToS or Privacy Policy. |
| Contact email (general) | ❓ Unknown | `/contact` path is a 404; no email found. |
| Contact email (security) | ❓ Unknown | No security policy or email found. |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ✅ Yes | https://github.com/mcpserverdirectory |

### 1.2 Marketplace Type

*Check all that apply:*

| Type | Yes/No | Notes |
|---|---|---|
| Directory/Aggregator - Lists servers with external links | ✅ Yes | Primary function is linking to GitHub. |
| Registry - Provides API for programmatic discovery | ❓ No | No public API found. |
| Code Hosting - Hosts server source code or packages | ❌ No | Links to external repos (GitHub). |
| Hosted Execution (PaaS) - Runs MCP servers on their infrastructure | ❌ No | |
| Client-Embedded - Built into a specific MCP client | ❓ No | No evidence of this. |
| Curated List - Manually maintained list (e.g., awesome-list) | ✅ Yes | Features curated/featured servers. |

### 1.3 Scale & Activity

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers listed (approximate count) | ~2500 | Website claim. |
| Update frequency | ❓ Unknown | No changelog or update history visible. |
| Publisher/contributor count | ❓ Unknown | |
| Changelog or update history available? | ❌ No | |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ✅ Yes | https://mcpserverdirectory.org/ |
| Public API (registry endpoint) | ❌ No | `/api` returns 404. |
| CLI tool | ❌ No | |
| IDE/editor plugin | ❌ No | |
| Integrated into MCP client(s) | ❓ Unknown | |
| Browser extension | ❌ No | |

### 2.2 API Details (if applicable)

N/A

### 2.3 Metadata Provided Per Server

| Field | Provided? | Notes |
|---|---|---|
| Server name | ✅ Yes | |
| Description | ✅ Yes | |
| Author/publisher | ❓ Unknown | Not explicitly listed, inferred from GitHub URL. |
| Source code URL | ✅ Yes | |
| License | ❓ Unknown | Not displayed on the directory. |
| Version information | ❌ No | |
| Last updated date | ❌ No | |
| Download/install count | ❌ No | |
| Ratings/reviews | ❌ No | |
| Categories/tags | ✅ Yes | |
| Required permissions/capabilities | ❌ No | |
| Verification/trust badge | ❌ No | |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|---|---|---|
| Link to external source (GitHub, etc.) | ✅ Yes | Primary method. |
| Direct download (zip, tarball) | ❌ No | |
| Package manager (npm, pip, etc.) | ❌ No | |
| Container image (Docker) | ❌ No | |
| One-click install to client config | ❌ No | |
| Hosted execution (marketplace runs the server) | ❌ No | |

### 3.2 Hosted Execution Details (PaaS Model)

N/A

### 3.3 Source Accessibility

| Question | Answer | Evidence/Source |
|---|---|---|
| Marketplace source code available? | ✅ Yes | https://github.com/mcpserverdirectory |
| API documentation URL | ❌ No | |
| Self-hostable? | ❓ Unknown | No documentation on self-hosting. |

### 3.4 Server Coverage

| Question | Answer | Evidence/Source |
|---|---|---|
| Lists vendor-hosted servers (Vercel, Cloudflare, etc.)? | ❓ Unknown | Search functionality is by category, not free-text. |
| Distinguishes hosted vs local servers? | ❌ No | |
| Vendor-hosted servers found in search? | ❓ Unknown | Cannot perform free-text search to verify. |

### 3.5 Vendor-Hosted Coverage Test

N/A - Cannot be performed due to lack of search functionality.

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|---|---|---|
| Publisher verification process exists? | ❌ No | No information found. |
| Verification requirements documented? | ❌ No | |
| 2FA/MFA required for publishers? | N/A | |
| Trust tiers (verified, official, etc.)? | ❌ No | |
| Verification criteria publicly documented? | ❌ No | |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ❓ Unknown | No information on the curation or vetting process. |
| Automated security scanning? | ❓ Unknown | |
| Malware detection? | ❓ Unknown | |
| Dependency vulnerability scanning? | ❓ Unknown | |
| Flagged server removal speed? | ❓ Unknown | No reporting mechanism is visible. |
| Typosquatting/namesquatting protection? | ❓ Unknown | |

### 4.3 Community Trust Signals

| Question | Answer | Evidence/Source |
|---|---|---|
| Users can report problematic servers? | ❌ No | No "Report" button or similar feature found. |
| Visible "Report" button? | ❌ No | |
| User reviews or ratings? | ❌ No | |
| Download/usage count visible? | ❌ No | |
| "Last updated" timestamp visible? | ❌ No | |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ✅ Yes | https://mcpserverdirectory.org/privacy-policy |
| Privacy policy URL | ✅ Yes | https://mcpserverdirectory.org/privacy-policy |
| User data collected (summary) | Account info, usage details, device info, cookies, payment info, search data. | Privacy Policy |
| Data shared with third parties? | ⚠️ Yes | "Trusted third-party partners under confidentiality agreements." |
| Analytics/tracking tools used | ✅ Yes | Google Analytics, GTM, MS Clarity, PostHog, Sentry |
| Data retention policy? | ❓ Unknown | Not specified. |
| GDPR compliance claimed? | ❓ Unknown | Not mentioned. |

### 5.1.1 Third-Party Integrations Detected

| Integration | Present? | Details |
|---|---|---|
| Google Analytics | ✅ Yes | `gtag` |
| Google Tag Manager | ✅ Yes | `googletagmanager.com` |
| Microsoft Clarity | ✅ Yes | `clarity.ms` |
| PostHog | ✅ Yes | `PostHog` |
| Sentry | ✅ Yes | `Sentry.io` |
| Vercel | ✅ Yes | Hosting and DNS |


### 5.2 Terms of Service

| Question | Answer | Evidence/Source |
|---|---|---|
| Terms of service exists? | ✅ Yes | https://mcpserverdirectory.org/terms-of-service |
| Terms of service URL | ✅ Yes | https://mcpserverdirectory.org/terms-of-service |
| Prohibited publisher activities | ❓ Unknown | ToS focuses on user behavior, not publishers. |
| Prohibited user activities | ✅ Yes | Unauthorized access, redistribution, interference, illegal use. |
| Liability limitations | ✅ Yes | Includes disclaimers of warranties and limitations of liability. |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ❌ No | `/security` and `security.txt` return 404. |
| Security policy URL (SECURITY.md) | ❌ No | |
| Vulnerability disclosure process? | ❌ No | |
| Bug bounty program? | ❌ No | |
| Past security incidents disclosed? | ❌ No | |
| Status page for uptime/incidents? | ❌ No | `/status` and `/health` return 404. |

---

## Part 6: Supply Chain Security

N/A - This marketplace is a directory that links to external source code and does not host packages or execute code.

---

## Part 7: Technical Security Posture

### 7.1 Web Security Headers

| Header | Present? | Value |
|---|---|---|
| HTTPS enforced | ✅ Yes | |
| Strict-Transport-Security (HSTS) | ✅ Yes | `max-age=63072000; includeSubDomains; preload` |
| Content-Security-Policy | ❌ No | |
| X-Frame-Options | ❌ No | |
| X-Content-Type-Options | ✅ Yes | `nosniff` |
| Referrer-Policy | ✅ Yes | `origin-when-cross-origin` |
| Permissions-Policy | ❌ No | |
| Cross-Origin-Opener-Policy | ❌ No | |
| Cross-Origin-Resource-Policy | ❌ No | |

### 7.2 TLS Certificate

| Field | Value |
|---|---|
| Issuer | C=US, O=Let's Encrypt, CN=R12 |
| Subject | CN=*.mcpserverdirectory.org |
| Valid from | Nov 22 19:22:45 2025 GMT |
| Valid until | Feb 20 19:22:44 2026 GMT |
| SHA256 fingerprint | null |

### 7.3 DNS & Hosting

| Field | Value |
|---|---|
| A records | `64.29.17.65`, `216.198.79.65` |
| AAAA records | [] |
| CNAME records | [] |
| NS records | `ns1.vercel-dns.com`, `ns2.vercel-dns.com` |
| Provider hints | Vercel (NS) |

### 7.4 Path Availability (Automated Probe)

| Path | Status Code | Notes |
|---|---|---|
| /privacy | 404 | |
| /privacy-policy | 200 | |
| /terms | 404 | |
| /tos | 404 | |
| /terms-of-service | 200 | |
| /security | 404 | |
| /contact | 404 | |
| /robots.txt | 200 | |
| /sitemap.xml | 404 | |
| /api | 404 | |
| /docs | 404 | |

### 7.5 Mixed Content

| Check | Result |
|---|---|
| HTTP links found | 0 |
| HTTP subresources found | 0 |
| Sample URLs | [] |

### 7.6 Social/Contact Links Found

| Type | URL |
|---|---|
| GitHub | https://github.com/mcpserverdirectory |

### 7.7 Authentication & Authorization

| Question | Answer | Evidence/Source |
|---|---|---|
| Authentication methods supported | ❓ Unknown | Login/registration pages not found. |
| OAuth/OIDC providers | ❓ Unknown | |
| Session management documented? | ❌ No | |
| API tokens scoped and time-limited? | N/A | |

---

## Part 8: Operator Transparency

### 8.1 Business Model

| Question | Answer | Evidence/Source |
|---|---|---|
| Free or paid? | ✅ Free | |
| Pricing model (if paid) | N/A | ToS mentions "purchases", but no pricing page is visible. |
| Revenue source | ❓ Unknown | |
| Registered business entity? | ❓ Unknown | |

### 8.2 Communication & Support

| Question | Answer | Evidence/Source |
|---|---|---|
| Public documentation URL | ❌ No | `/docs` returns 404. |
| Community (Discord/Slack/Forum) | ❌ No | No links found. |
| Official social media | ⚠️ Partial | Only a GitHub organization was found. |
| Support response time | ❓ Unknown | No support channel found. |
| Issue tracker for bug reports | ⚠️ Partial | Can use GitHub issues, but not explicitly stated. |

---

## Part 9: Security Incidents

No public security incidents were found related to "MCP Server Directory" during a web search on 2026-02-04.

---

## Part 10: Delivery Method Security

The primary delivery method is linking to GitHub repositories. The security of this method is dependent on GitHub's security and the user's own diligence in reviewing the source code before use.

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- Good use of `Strict-Transport-Security` header.
- Provides links to the source code for listed servers, allowing for user review.
- Clear Privacy Policy and Terms of Service are available.
- Hosted on Vercel, which provides a modern and secure infrastructure.

### 11.2 Weaknesses & Gaps

- Lack of crucial security headers like `Content-Security-Policy` and `X-Frame-Options`.
- No information on server vetting, publisher verification, or any form of curation process.
- No community trust signals like ratings, reviews, or a "report" button.
- Missing transparency regarding the operator's identity, jurisdiction, and contact information.
- No formal security policy, vulnerability disclosure process, or security contact.
- Heavy use of third-party analytics and tracking services.

### 11.3 Red Flags

- **Anonymity of Operator:** The lack of transparency about who runs the site is a significant red flag. Users have no way to know who they are trusting.
- **No Trust Signals:** The complete absence of any vetting, verification, or community feedback mechanisms means users must treat every listing as potentially untrusted.
- **No Security Contact:** The absence of a `security.txt` file or any security contact makes it difficult to report vulnerabilities.

### 11.4 Recommendations

- **Implement a Content Security Policy (CSP):** To mitigate the risk of XSS attacks.
- **Add X-Frame-Options:** To prevent clickjacking.
- **Create a Security Policy:** Publish a `security.txt` file with a clear contact for vulnerability disclosure.
- **Improve Transparency:** Provide clear information about the operator, their jurisdiction, and a general contact email.
- **Establish Trust Mechanisms:** Document the server submission and vetting process. Implement publisher verification and community feedback features like reviews and reporting.

### 11.5 Overall Trust Assessment

MCP Server Directory serves as a simple aggregator for discovering MCP servers. While it has a clean interface and good technical uptime, it lacks almost all fundamental trust and security mechanisms. The operator is anonymous, there is no vetting process for listed servers, and no way for the community to report malicious or low-quality entries. Users should treat this directory as a search engine for MCP projects on GitHub and must perform their own thorough security review of any server they find through this site. It is not a trusted marketplace.

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

### Testing Methodology

**Automated checks performed:**
- Date: 2025-12-13 (from pre-existing audit data)

**Manual checks performed:**
- Review of main page, privacy policy, and terms of service.
- Check for contact, security, and about pages.

### tier1_audit.py Output

```json
{
  "name": "MCP Server Directory",
  "marketplace_url": "https://mcpserverdirectory.org/",
  "source_url": "",
  "audited_at": "2025-12-13T04:59:12.782542Z",
  "checks_run": [
    "domain",
    "web"
  ],
  "errors": [],
  "domain": {
    "hostname": "mcpserverdirectory.org",
    "registrable_domain": "mcpserverdirectory.org",
    "dns": {
      "a": [
        "64.29.17.65",
        "216.198.79.65"
      ],
      "aaaa": [],
      "cname": [],
      "ns": [
        "ns1.vercel-dns.com",
        "ns2.vercel-dns.com"
      ],
      "mx": [],
      "txt": []
    },
    "tls": {
      "ok": true,
      "issuer": "C=US, O=Let's Encrypt, CN=R12",
      "subject": "CN=*.mcpserverdirectory.org",
      "not_before": "Nov 22 19:22:45 2025 GMT",
      "not_after": "Feb 20 19:22:44 2026 GMT",
      "sha256_fingerprint": null,
      "san": [
        "*.mcpserverdirectory.org",
        "mcpserverdirectory.org"
      ],
      "error": null
    },
    "provider_hints": [
      "Vercel (NS)"
    ],
    "reverse_dns": {
      "64.29.17.65": "",
      "216.198.79.65": ""
    },
    "errors": []
  },
  "web": {
    "url": "https://mcpserverdirectory.org/",
    "http": {
      "ok": true,
      "final_url": "https://mcpserverdirectory.org/",
      "status_code": 200,
      "status_chain": [
        "HTTP/2 200"
      ],
      "redirect_chain": [],
      "headers": {
        "age": "0",
        "cache-control": "private, no-cache, no-store, max-age=0, must-revalidate",
        "content-type": "text/html; charset=utf-8",
        "date": "Sat, 13 Dec 2025 04:59:16 GMT",
        "link": "</_next/static/media/a34f9d1faa5f3315-s.p.woff2>; rel=preload; as=\"font\"; crossorigin=\"\"; type=\"font/woff2\"",
        "referrer-policy": "origin-when-cross-origin",
        "server": "Vercel",
        "strict-transport-security": "max-age=63072000; includeSubDomains; preload",
        "vary": "RSC, Next-Router-State-Tree, Next-Router-Prefetch, Next-Router-Segment-Prefetch",
        "x-content-type-options": "nosniff",
        "x-dns-prefetch-control": "on",
        "x-matched-path": "/",
        "x-vercel-cache": "MISS",
        "x-vercel-id": "pdx1::iad1::8dpxh-1765601955049-0280f33d2a29",
        "x-xss-protection": "1; mode=block"
      },
      "response_time_ms": 2649,
      "error": null
    },
    "security_headers": {
      "strict_transport_security": "max-age=63072000; includeSubDomains; preload",
      "content_security_policy": null,
      "x_frame_options": null,
      "x_content_type_options": "nosniff",
      "referrer_policy": "origin-when-cross-origin",
      "permissions_policy": null,
      "cross_origin_opener_policy": null,
      "cross_origin_resource_policy": null,
      "cross_origin_embedder_policy": null,
      "_present": [
        "strict_transport_security",
        "x_content_type_options",
        "referrer_policy"
      ],
      "_missing": [
        "content_security_policy",
        "x_frame_options",
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
        "evidence": "gtag"
      },
      {
        "name": "Google Tag Manager",
        "type": "analytics",
        "evidence": "googletagmanager.com"
      },
      {
        "name": "Microsoft Clarity",
        "type": "analytics",
        "evidence": "clarity.ms"
      },
      {
        "name": "PostHog",
        "type": "analytics",
        "evidence": "PostHog"
      },
      {
        "name": "Sentry",
        "type": "error_tracking",
        "evidence": "Sentry.io"
      }
    ],
    "social_links": [
      {
        "type": "github",
        "url": "https://github.com/mcpserverdirectory"
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

### Key Findings Summary

| Category | Result |
|---|---|
| HTTP status | 200 OK |
| Provider hints | Vercel |
| Security headers present | `Strict-Transport-Security`, `X-Content-Type-Options`, `Referrer-Policy` |
| Security headers missing | `Content-Security-Policy`, `X-Frame-Options`, `Permissions-Policy` |
| Mixed content | None found |
| Policy endpoints (200) | `/privacy-policy`, `/terms-of-service`, `/robots.txt` |
| Policy endpoints (404) | `/privacy`, `/terms`, `/security`, `/contact`, etc. |
| API endpoints (200) | None |
| Social links detected | GitHub |

---

## Changelog

| Date | Version | Changes | Author |
|---|---|---|---|
| 2026-02-04 | 1.0 | Initial evaluation | AI Assistant |