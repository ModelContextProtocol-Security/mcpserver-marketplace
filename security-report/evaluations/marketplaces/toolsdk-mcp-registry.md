---
title: "ToolSDK MCP Registry"
url: "https://toolsdk.ai"
source_code_url: "https://github.com/toolsdk-ai/toolsdk-mcp-registry"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "directory"
operator: "ToolSDK.ai"
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "Unknown"
server_count: "5000+"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://toolsdk.ai"
    description: "Main website"
    captured: "2026-02-04"
  - url: "https://toolsdk.ai/privacy-policy"
    description: "Privacy Policy"
    captured: "2026-02-04"
  - url: "https://toolsdk.ai/terms-of-service"
    description: "Terms of Service"
    captured: "2026-02-04"
---

## Overview

ToolSDK.ai provides a free TypeScript SDK designed to help developers connect their agentic AI applications to over 5,000 MCP servers and AI tools. The project emphasizes security, with features like built-in OAuth management and isolated sandboxes for MCP servers. While its primary product is the SDK, the website also functions as a directory or marketplace for discovering these MCP servers. The operator is ToolSDK.ai, but specific details about the company or its jurisdiction are not available.

## Features Summary

*Quick reference - details in Part 2*

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | Website with search and browsing capabilities. |
| One-click install | ⚠️ | Not a direct install, but provides SDK for integration. |
| Curated list/recommendations | ✅ | Features popular and trending servers. |
| Public API | ✅ | An `openapi.json` file is available. |
| CLI tool | ❓ | The website focuses on a TypeScript SDK, no CLI mentioned. |
| Client integration | ✅ | The entire purpose is to integrate MCP servers into apps via their SDK. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | ToolSDK.ai | Website Title |
| Primary URL | https://toolsdk.ai | Browser |
| Operator (company/individual) | ToolSDK.ai | Terms of Service |
| Country/jurisdiction | ❓ Unknown | Not specified in ToS or Privacy Policy. |
| Contact email (general) | ❓ Unknown | `/contact` path is 404; no email found. |
| Contact email (security) | ❓ Unknown | No security policy or email found. |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ✅ Yes | https://github.com/toolsdk-ai/toolsdk-mcp-registry |

### 1.2 Marketplace Type

*Check all that apply:*

| Type | Yes/No | Notes |
|---|---|---|
| Directory/Aggregator - Lists servers with external links | ✅ Yes | The site lists thousands of servers with links to their source. |
| Registry - Provides API for programmatic discovery | ✅ Yes | An `openapi.json` is present, suggesting an API. The SDK also acts as a registry client. |
| Code Hosting - Hosts server source code or packages | ❌ No | Links to external GitHub repositories. |
| Hosted Execution (PaaS) - Runs MCP servers on their infrastructure | ❌ No | |
| Client-Embedded - Built into a specific MCP client | ✅ Yes | The SDK is the "client" in this case. |
| Curated List - Manually maintained list (e.g., awesome-list) | ✅ Yes | Features curated lists of servers. |

### 1.3 Scale & Activity

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers listed (approximate count) | 5000+ | Website claim. |
| Update frequency | ❓ Unknown | No changelog visible on the main site. |
| Publisher/contributor count | ❓ Unknown | |
| Changelog or update history available? | ⚠️ | Release notes are mentioned in docs, but not easily found. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ✅ Yes | https://toolsdk.ai |
| Public API (registry endpoint) | ✅ Yes | https://toolsdk.ai/openapi.json |
| CLI tool | ❌ No | |
| IDE/editor plugin | ❌ No | |
| Integrated into MCP client(s) | ✅ Yes | The ToolSDK itself is the client. |
| Browser extension | ❌ No | |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|---|---|---|
| API documentation available? | ✅ Yes | /docs page and an OpenAPI spec are available. |
| Authentication required for read? | ❓ Unknown | Based on the spec, it seems some endpoints may require auth. |
| Rate limiting? | ❓ Unknown | Not documented. |
| OpenAPI/Swagger spec? | ✅ Yes | https://toolsdk.ai/openapi.json |
| API terms of use? | ✅ Yes | Covered in the main Terms of Service. |

### 2.3 Metadata Provided Per Server

(Based on website observation)
| Field | Provided? | Notes |
|---|---|---|
| Server name | ✅ Yes | |
| Description | ✅ Yes | |
| Author/publisher | ✅ Yes | |
| Source code URL | ✅ Yes | |
| License | ❓ Unknown | Not displayed on the marketplace cards. |
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
| Link to external source (GitHub, etc.) | ✅ Yes | The site links to the source of the MCP servers. |
| Direct download (zip, tarball) | ❌ No | |
| Package manager (npm, pip, etc.) | ✅ Yes | The primary delivery method is via their `npm` package. |
| Container image (Docker) | ❌ No | |
| One-click install to client config | ❌ No | |
| Hosted execution (marketplace runs the server) | ❌ No | |

### 3.3 Source Accessibility

| Question | Answer | Evidence/Source |
|---|---|---|
| Marketplace source code available? | ✅ Yes | https://github.com/toolsdk-ai/toolsdk-mcp-registry |
| API documentation URL | ✅ Yes | https://toolsdk.ai/docs |
| Self-hostable? | ❓ Unknown | The GitHub repo is for the registry, not the full platform. |

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
| Servers reviewed before listing? | ❓ Unknown | No information on the vetting process. |
| Automated security scanning? | ❓ Unknown | |
| Malware detection? | ❓ Unknown | |
| Dependency vulnerability scanning? | ❓ Unknown | |
| Flagged server removal speed? | ❓ Unknown | No reporting mechanism is visible. |
| Typosquatting/namesquatting protection? | ❓ Unknown | |

### 4.3 Community Trust Signals

| Question | Answer | Evidence/Source |
|---|---|---|
| Users can report problematic servers? | ❌ No | No "Report" button found. |
| Visible "Report" button? | ❌ No | |
| User reviews or ratings? | ❌ No | |
| Download/usage count visible? | ❌ No | |
| "Last updated" timestamp visible? | ❌ No | |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ✅ Yes | https://toolsdk.ai/privacy-policy |
| Privacy policy URL | ✅ Yes | https://toolsdk.ai/privacy-policy |
| User data collected (summary) | Activity, app usage, browser/device info, MCP server usage, API keys, avatar pictures. | Privacy Policy |
| Data shared with third parties? | ⚠️ Yes | The policy is vague, mentioning sharing with partners and for legal compliance. |
| Analytics/tracking tools used | ✅ Yes | Google Analytics, Google Tag Manager. |
| Data retention policy? | ❓ Unknown | Not specified. |
| GDPR compliance claimed? | ❓ Unknown | Not mentioned. |

### 5.2 Terms of Service

| Question | Answer | Evidence/Source |
|---|---|---|
| Terms of service exists? | ✅ Yes | https://toolsdk.ai/terms-of-service |
| Terms of service URL | ✅ Yes | https://toolsdk.ai/terms-of-service |
| Prohibited publisher activities | ❓ Unknown | ToS focuses on user behavior. |
| Prohibited user activities | ✅ Yes | Standard restrictions on illegal use, reverse engineering, etc. |
| Liability limitations | ✅ Yes | Includes standard disclaimers of warranties and liability limitations. |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ❌ No | `/security` and `security.txt` return 404. |
| Vulnerability disclosure process? | ❌ No | |
| Bug bounty program? | ❌ No | |
| Past security incidents disclosed? | ❌ No | |
| Status page for uptime/incidents? | ❌ No | `/status` returns 404. |

---

## Part 6: Supply Chain Security

As this is primarily a directory and an SDK, most of the supply chain risk is inherited from the packages it lists and the npm ecosystem.

### 6.1 Code Integrity

| Question | Answer | Evidence/Source |
|---|---|---|
| Packages/images signed? | ❓ Unknown | npm packages are generally not signed. No mention of other signing. |
| Provenance attestation provided? | ❌ No | |
| SBOMs (Software Bill of Materials) available? | ❌ No | |
| Reproducible build support? | ❌ No | |

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
| Issuer | C=US, O=Let's Encrypt, CN=R12 |
| Subject | CN=toolsdk.ai |
| Valid from | Nov 23 01:40:02 2025 GMT |
| Valid until | Feb 21 01:40:01 2026 GMT |
| SHA256 fingerprint | null |

### 7.3 DNS & Hosting

| Field | Value |
|---|---|
| A records | `35.82.152.42`, `44.240.47.189` |
| AAAA records | [] |
| CNAME records | [] |
| NS records | `sloan.ns.cloudflare.com`, `burt.ns.cloudflare.com` |
| Provider hints | Cloudflare (NS) |

### 7.4 Path Availability (Automated Probe)

| Path | Status Code | Notes |
|---|---|---|
| /privacy-policy | 200 | |
| /terms-of-service | 200 | |
| /about | 200 | |
| /docs | 200 | |
| /robots.txt | 200 | |
| /sitemap.xml | 200 | |
| /openapi.json | 200 | |
| /security | 404 | |
| /contact | 404 | |

---

## Part 8: Operator Transparency

### 8.1 Business Model

| Question | Answer | Evidence/Source |
|---|---|---|
| Free or paid? | ✅ Free | The SDK is advertised as free. |
| Pricing model (if paid) | N/A | |
| Revenue source | ❓ Unknown | Future enterprise features are mentioned on the roadmap. |
| Registered business entity? | ❓ Unknown | |

### 8.2 Communication & Support

| Question | Answer | Evidence/Source |
|---|---|---|
| Public documentation URL | ✅ Yes | https://toolsdk.ai/docs |
| Community (Discord/Slack/Forum) | ❌ No | No links found. |
| Official social media | ⚠️ Partial | Only GitHub organization found. |
| Support response time | ❓ Unknown | No support channel found. |
| Issue tracker for bug reports | ✅ Yes | GitHub issues are available. |

---

## Part 9: Security Incidents

No public security incidents were found related to "ToolSDK.ai" during a web search on 2026-02-04.

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- Provides a TypeScript SDK that aims to simplify MCP integration for developers.
- The project has a clear focus on the developer experience.
- The source code for the registry is available on GitHub.
- The presence of an OpenAPI spec is a positive sign for API support.
- The project's GitHub repository has Dependabot, code scanning, and secret scanning enabled.

### 11.2 Weaknesses & Gaps

- **Missing all major security headers.** This is a significant gap in the web security posture.
- Complete lack of publisher or server verification processes.
- No community trust signals (reviews, reporting, etc.).
- Operator anonymity is a concern.
- No security policy or vulnerability disclosure process.

### 11.3 Red Flags

- **Poor Web Security:** The total absence of security headers on a site that provides developer tools is a major red flag. It suggests a lack of attention to basic security practices.
- **Inherited Risk:** The SDK encourages connecting to thousands of unvetted MCP servers, shifting the entire security burden onto the developer. While the SDK itself may be secure, it facilitates a potentially insecure practice. Developers should use the SDK with caution and should not assume that any server discovered through ToolSDK.ai is trustworthy.

### 11.4 Recommendations

- **Implement All Recommended Security Headers:** HSTS, CSP, X-Frame-Options, etc., should be implemented immediately.
- **Establish Trust & Verification:** Create a process for vetting servers and verifying publishers.
- **Improve Transparency:** Provide clear information about the operating entity and a security contact.
- **Publish a Security Policy:** A `security.txt` file and a vulnerability disclosure policy are essential for a project in this space.

### 11.5 Overall Trust Assessment

ToolSDK.ai is an interesting developer-focused project that aims to solve a real problem in the AI agent ecosystem. However, the website itself has a very poor security posture, lacking all basic security headers. This undermines the project's claims of being "security-first". While the SDK may be well-built, the lack of vetting for the 5,000+ servers it provides access to means that developers are on their own to assess the risk of each integration. Developers should use the SDK with caution and should not assume that any server discovered through ToolSDK.ai is trustworthy.

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
- Review of main page, privacy policy, terms of service, docs, and about page.

### tier1_audit.py Output

```json
{
  "name": "ToolSDK MCP Registry",
  "marketplace_url": "https://toolsdk.ai",
  "source_url": "https://github.com/toolsdk-ai/toolsdk-mcp-registry",
  "audited_at": "2025-12-13T04:58:11.736171Z",
  "checks_run": [
    "domain",
    "web",
    "source_repo"
  ],
  "errors": [],
  "domain": {
    "hostname": "toolsdk.ai",
    "registrable_domain": "toolsdk.ai",
    "dns": {
      "a": [
        "35.82.152.42",
        "44.240.47.189"
      ],
      "aaaa": [],
      "cname": [],
      "ns": [
        "sloan.ns.cloudflare.com",
        "burt.ns.cloudflare.com"
      ],
      "mx": [
        "eforward5.registrar-servers.com",
        "eforward1.registrar-servers.com",
        "eforward2.registrar-servers.com",
        "eforward3.registrar-servers.com",
        "eforward4.registrar-servers.com"
      ],
      "txt": [
        "google-site-verification=VlrvPiArJBwWZOig3sFJcqLkO8X11AEcPyBbmAYuB0I",
        "v=spf1 include:spf.efwd.registrar-servers.com ~all"
      ]
    },
    "tls": {
      "ok": true,
      "issuer": "C=US, O=Let's Encrypt, CN=R12",
      "subject": "CN=toolsdk.ai",
      "not_before": "Nov 23 01:40:02 2025 GMT",
      "not_after": "Feb 21 01:40:01 2026 GMT",
      "sha256_fingerprint": null,
      "san": [
        "registry.toolsdk.ai",
        "toolsdk.ai"
      ],
      "error": null
    },
    "provider_hints": [
      "Cloudflare (NS)"
    ],
    "reverse_dns": {
      "35.82.152.42": "ec2-35-82-152-42.us-west-2.compute.amazonaws.com",
      "44.240.47.189": "ec2-44-240-47-189.us-west-2.compute.amazonaws.com"
    },
    "errors": []
  },
  "web": {
    "url": "https://toolsdk.ai",
    "http": {
      "ok": true,
      "final_url": "https://toolsdk.ai",
      "status_code": 200,
      "status_chain": [
        "HTTP/2 200"
      ],
      "redirect_chain": [],
      "headers": {
        "cache-control": "private, no-cache, no-store, max-age=0, must-revalidate",
        "content-type": "text/html; charset=utf-8",
        "date": "Sat, 13 Dec 2025 04:58:13 GMT",
        "link": "<_next/static/chunks/f492710c9655e256.css>; rel=preload; as=\"style\", <_next/static/chunks/df7f6499700dadfa.css>; rel=preload; as=\"style\"",
        "vary": "rsc, next-router-state-tree, next-router-prefetch, next-router-segment-prefetch, Accept-Encoding",
        "x-clerk-auth-reason": "session-token-and-uat-missing",
        "x-clerk-auth-status": "signed-out",
        "x-middleware-rewrite": "/",
        "x-powered-by": "Next.js"
      },
      "response_time_ms": 543,
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
      }
    ],
    "social_links": [
      {
        "type": "github",
        "url": "https://github.com/toolsdk-ai/awesome-mcp-registry"
      },
      {
        "type": "github",
        "url": "https://github.com/toolsdk-ai/toolsdk"
      }
    ],
    "cookies": [],
    "server_info": {
      "powered_by": "Next.js"
    },
    "errors": []
  },
  "source_repo": {
    "repo_info": {
      "platform": "github",
      "owner": "toolsdk-ai",
      "repo": "toolsdk-mcp-registry",
      "url": "https://github.com/toolsdk-ai/toolsdk-mcp-registry",
      "is_org": true
    },
    "security_files": {
      "security_md": false,
      "security_md_url": null,
      "security_policy": false,
      "code_of_conduct": false,
      "contributing_md": true,
      "license": "MIT",
      "license_url": "https://github.com/toolsdk-ai/toolsdk-mcp-registry/blob/main/LICENSE"
    },
    "org_verification": {
      "is_org": true,
      "org_name": "toolsdk.ai",
      "verified": false,
      "verified_domains": []
    },
    "activity": {
      "stars": 0,
      "forks": 0,
      "watchers": 0,
      "open_issues": 0,
      "open_prs": 0,
      "last_commit": null,
      "last_release": null,
      "created_at": null,
      "updated_at": null,
      "archived": false
    },
    "security_features": {
      "dependabot_enabled": true,
      "code_scanning_enabled": true,
      "secret_scanning_enabled": true,
      "branch_protection": false,
      "signed_commits": false,
      "security_advisories": []
    },
    "topics": [],
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

---

## Audit Evidence

### Testing Methodology

**Automated checks performed:**
- Date: 2025-12-13 (from pre-existing audit data)

**Manual checks performed:**
- Review of main page, privacy policy, terms of service, docs, and about page.

### tier1_audit.py Output

```json
{
  "name": "ToolSDK MCP Registry",
  "marketplace_url": "https://toolsdk.ai",
  "source_url": "https://github.com/toolsdk-ai/toolsdk-mcp-registry",
  "audited_at": "2025-12-13T04:58:11.736171Z",
  "checks_run": [
    "domain",
    "web",
    "source_repo"
  ],
  "errors": [],
  "domain": {
    "hostname": "toolsdk.ai",
    "registrable_domain": "toolsdk.ai",
    "dns": {
      "a": [
        "35.82.152.42",
        "44.240.47.189"
      ],
      "aaaa": [],
      "cname": [],
      "ns": [
        "sloan.ns.cloudflare.com",
        "burt.ns.cloudflare.com"
      ],
      "mx": [
        "eforward5.registrar-servers.com",
        "eforward1.registrar-servers.com",
        "eforward2.registrar-servers.com",
        "eforward3.registrar-servers.com",
        "eforward4.registrar-servers.com"
      ],
      "txt": [
        "google-site-verification=VlrvPiArJBwWZOig3sFJcqLkO8X11AEcPyBbmAYuB0I",
        "v=spf1 include:spf.efwd.registrar-servers.com ~all"
      ]
    },
    "tls": {
      "ok": true,
      "issuer": "C=US, O=Let's Encrypt, CN=R12",
      "subject": "CN=toolsdk.ai",
      "not_before": "Nov 23 01:40:02 2025 GMT",
      "not_after": "Feb 21 01:40:01 2026 GMT",
      "sha256_fingerprint": null,
      "san": [
        "registry.toolsdk.ai",
        "toolsdk.ai"
      ],
      "error": null
    },
    "provider_hints": [
      "Cloudflare (NS)"
    ],
    "reverse_dns": {
      "35.82.152.42": "ec2-35-82-152-42.us-west-2.compute.amazonaws.com",
      "44.240.47.189": "ec2-44-240-47-189.us-west-2.compute.amazonaws.com"
    },
    "errors": []
  },
  "web": {
    "url": "https://toolsdk.ai",
    "http": {
      "ok": true,
      "final_url": "https://toolsdk.ai",
      "status_code": 200,
      "status_chain": [
        "HTTP/2 200"
      ],
      "redirect_chain": [],
      "headers": {
        "cache-control": "private, no-cache, no-store, max-age=0, must-revalidate",
        "content-type": "text/html; charset=utf-8",
        "date": "Sat, 13 Dec 2025 04:58:13 GMT",
        "link": "<_next/static/chunks/f492710c9655e256.css>; rel=preload; as=\"style\", <_next/static/chunks/df7f6499700dadfa.css>; rel=preload; as=\"style\"",
        "vary": "rsc, next-router-state-tree, next-router-prefetch, next-router-segment-prefetch, Accept-Encoding",
        "x-clerk-auth-reason": "session-token-and-uat-missing",
        "x-clerk-auth-status": "signed-out",
        "x-middleware-rewrite": "/",
        "x-powered-by": "Next.js"
      },
      "response_time_ms": 543,
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
      }
    ],
    "social_links": [
      {
        "type": "github",
        "url": "https://github.com/toolsdk-ai/awesome-mcp-registry"
      },
      {
        "type": "github",
        "url": "https://github.com/toolsdk-ai/toolsdk"
      }
    ],
    "cookies": [],
    "server_info": {
      "powered_by": "Next.js"
    },
    "errors": []
  },
  "source_repo": {
    "repo_info": {
      "platform": "github",
      "owner": "toolsdk-ai",
      "repo": "toolsdk-mcp-registry",
      "url": "https://github.com/toolsdk-ai/toolsdk-mcp-registry",
      "is_org": true
    },
    "security_files": {
      "security_md": false,
      "security_md_url": null,
      "security_policy": false,
      "code_of_conduct": false,
      "contributing_md": true,
      "license": "MIT",
      "license_url": "https://github.com/toolsdk-ai/toolsdk-mcp-registry/blob/main/LICENSE"
    },
    "org_verification": {
      "is_org": true,
      "org_name": "toolsdk.ai",
      "verified": false,
      "verified_domains": []
    },
    "activity": {
      "stars": 0,
      "forks": 0,
      "watchers": 0,
      "open_issues": 0,
      "open_prs": 0,
      "last_commit": null,
      "last_release": null,
      "created_at": null,
      "updated_at": null,
      "archived": false
    },
    "security_features": {
      "dependabot_enabled": true,
      "code_scanning_enabled": true,
      "secret_scanning_enabled": true,
      "branch_protection": false,
      "signed_commits": false,
      "security_advisories": []
    },
    "topics": [],
    "errors": []
  },
  "success": true
}
```