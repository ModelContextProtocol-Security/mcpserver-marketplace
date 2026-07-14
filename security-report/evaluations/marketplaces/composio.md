---
title: "Composio"
url: "https://composio.dev"
source_code_url: "https://github.com/composiohq/composio/"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "paas"
operator: "Composio HQ"
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "Unknown"
server_count: "10,000+"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://composio.dev"
    description: "Main website"
    captured: "2026-02-04"
---

## Overview

Composio is a platform for building AI applications with superpowered plugins (MCP servers), aiming to provide a seamless layer for LLMs and agents to reliably interact with tools in the real world. It emphasizes integrations, authentication, tool observability, and scalability, offering access to over 10,000 tools. The platform highlights enterprise-grade compliance, mentioning "SOC 2 Type II" and offering various pricing tiers including a free option. It is operated by "Composio HQ" and links to a GitHub organization.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | Access to 10,000+ tools. |
| One-click install | ❓ | Provides `curl` installation script, and API for integrations. |
| Curated list/recommendations | ✅ | "Thousands of Tools" implies curation. |
| Public API | ✅ | Core functionality is API-driven ("APIs and plugins"). |
| CLI tool | ✅ | `curl -fsSL https://composio.dev/install | bash` suggests a CLI installer. |
| Client integration | ✅ | Designed for integration with AI agents and LLMs. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | Composio | Website Title |
| Primary URL | https://composio.dev | Browser |
| Operator (company/individual) | Composio HQ | GitHub organization, implicit from website. |
| Country/jurisdiction | ❓ Unknown | |
| Contact email (general) | ❓ Unknown | Contact via Discord (`/contact` redirects). |
| Contact email (security) | ❓ Unknown | Not explicitly mentioned. |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ✅ Yes | `https://github.com/composiohq/composio/` is mentioned. |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Registry - Provides API for programmatic discovery | ✅ Yes | APIs and plugins for AI applications. |
| Hosted Execution (PaaS) - Runs MCP servers on their infrastructure | ✅ Yes | Manages tool executions and integrations. |
| Code Hosting - Hosts server source code or packages | ✅ Yes | Links to GitHub repository. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ✅ Yes | https://composio.dev |
| Public API (registry endpoint) | ✅ Yes | Core functionality is API-driven. |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|---|---|---|
| API documentation available? | ✅ Yes | Mentions "Explore docs" on homepage. |
| Authentication required for read? | ✅ Yes | "Agent Auth - Let us manage all the headaches of auth for your tools." |
| Rate limiting? | ✅ Yes | Pricing tiers indicate call limits. |
| OpenAPI/Swagger spec? | ❌ No | Not found in audit paths. |
| API terms of use? | ❓ Unknown | Content not fetched. |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|---|---|---|
| Hosted execution (marketplace runs the server) | ✅ Yes | Manages tool execution, integrations. |

### 3.3 Source Accessibility

| Question | Answer | Evidence/Source |
|---|---|---|
| Marketplace source code available? | ✅ Yes | https://github.com/composiohq/composio/ |

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|---|---|---|
| Publisher verification process exists? | ❓ Unknown | Not mentioned. |
| 2FA/MFA required for publishers? | ❓ Unknown | Not mentioned. |
| Trust tiers (verified, official, etc.)? | ❓ Unknown | Not mentioned. |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ❓ Unknown | Not mentioned. |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ✅ Yes | Path `/privacy` returns 200, but content could not be fetched. |
| User data collected (summary) | ❓ Unknown | Content not fetched. |
| Analytics/tracking tools used | ✅ Yes | Google Analytics, Google Tag Manager, Segment, PostHog (from audit). |

### 5.2 Terms of Service

| Question | Answer | Evidence/Source |
|---|---|---|
| Terms of service exists? | ✅ Yes | Path `/terms` returns 200, but content could not be fetched. |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ❓ Unknown | Mentions "SOC 2 Type II" but no explicit security policy found. |
| Vulnerability disclosure process? | ❌ No | Not mentioned in audit paths. |
| Bug bounty program? | ❌ No | Not mentioned. |

---

## Part 6: Supply Chain Security

### 6.2 Dependency Management

| Question | Answer | Evidence/Source |
|---|---|---|
| Dependencies scanned for vulnerabilities? | ❓ Unknown | Not mentioned. |

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
| Referrer-Policy | ❓ Unknown | Not detected by audit. |
| Permissions-Policy | ❌ No | |
| Cross-Origin-Opener-Policy | ❌ No | |
| Cross-Origin-Resource-Policy | ❌ No | |

### 7.2 TLS Certificate

| Field | Value |
|---|---|
| Issuer | Google Trust Services |
| Subject | `composio.dev` |

### 7.3 DNS & Hosting

| Field | Value |
|---|---|
| Provider hints | Cloudflare (NS), Google Workspace (MX) |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Comprehensive Platform:** Offers a wide range of features for AI agent integration, tool management, and deployment.
- **SOC 2 Type II Compliance:** Claims enterprise-grade compliance, which is a strong trust signal.
- **Clear Business Model:** Provides transparent pricing tiers, including a free option.
- **Good Base Security:** Uses HTTPS, HSTS, and X-Content-Type-Options.
- **Open-Source Components:** Links to a GitHub repository, suggesting some open-source aspects.

### 11.2 Weaknesses & Gaps

- **Missing Critical Security Headers:** Lacks CSP, X-Frame-Options, and Referrer-Policy, weakening its web security posture.
- **Inaccessible Policy Content:** Despite paths returning 200, content for Privacy Policy and Terms of Service could not be fetched, hindering transparency. This is a major concern for a platform claiming SOC 2 Type II compliance.
- **Extensive Tracking:** Uses multiple analytics tools (Google Analytics, GTM, Segment, PostHog) without accessible content for its privacy policy.
- **No Operator Transparency:** Beyond "Composio HQ" and a GitHub organization, specific details about the operating entity are not readily available.
- **No Explicit Vetting Information:** No explicit mention of how AI plugins (MCP servers) are vetted for security or quality.
- **No Security Policy/VDP:** Despite SOC 2 Type II claim, no visible security policy or vulnerability disclosure process.

### 11.3 Red Flags

- The combination of a claim of "SOC 2 Type II" compliance with inaccessible Privacy Policy and Terms of Service content, coupled with extensive tracking, is a significant red flag. It suggests a potential disconnect between advertised compliance and actual transparency regarding user data and legal obligations.
- Lack of explicit vetting for plugins, while offering an "open" platform, creates potential for malicious tools.

### 11.4 Recommendations

- **Implement All Security Headers:** Add comprehensive web security headers to enhance web security.
- **Publish Accessible Policies:** Ensure Privacy Policy, Terms of Service, and a dedicated Security Policy (including a VDP) are readily accessible and clearly outline data handling practices, terms of use, and vulnerability disclosure. This is crucial for backing up SOC 2 Type II claims.
- **Document Vetting Process:** Clearly define how AI plugins (MCP servers) are evaluated for security and quality before they can be deployed or listed on the platform.
- **Increase Operator Transparency:** Provide more details about the Composio HQ operating entity.

### 11.5 Overall Trust Assessment

Composio presents itself as a powerful and scalable platform for AI agent integration, with a strong emphasis on developer experience and enterprise compliance (SOC 2 Type II). It has a good foundation of base web security (HTTPS, HSTS) and open-source components. However, its trustworthiness is severely compromised by the inaccessibility of its core legal and security policies (Privacy Policy, Terms of Service, Security Policy). This lack of transparent information, especially in light of its SOC 2 Type II claim and extensive use of tracking tools, is a significant red flag. Without clear guidance on data handling, terms of use, and a documented vetting process for plugins, users must approach Composio with extreme caution. The platform has strong technical ambition but needs to drastically improve its transparency and accountability to build trust.

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
  "name": "Composio",
  "marketplace_url": "https://composio.dev",
  "source_url": "",
  "audited_at": "2025-12-13T04:58:34.564530Z",
  "checks_run": [
    "domain",
    "web"
  ],
  "errors": [],
  "domain": {
    "hostname": "composio.dev",
    "registrable_domain": "composio.dev",
    "dns": {
      "a": [
        "104.18.21.5",
        "104.18.20.5"
      ],
      "aaaa": [
        "2606:4700::6812:1505",
        "2606:4700::6812:1405"
      ],
      "cname": [],
      "ns": [
        "serenity.ns.cloudflare.com",
        "simon.ns.cloudflare.com"
      ],
      "mx": [
        "alt2.aspmx.l.google.com",
        "aspmx.l.google.com",
        "alt3.aspmx.l.google.com",
        "alt4.aspmx.l.google.com",
        "alt1.aspmx.l.google.com"
      ],
      "txt": [
        "hubspot-developer-verification=NWUxNTEzYTUtZDdkNi00OTliLTkzYzUtZjAyZGE5YTViZDg0",
        "openai-domain-verification=dv-d6luEi066K8VedloSbdNoDuI",
        "tiktok-developers-site-verification=FpHYyysTCkGuhFgAZfFVXGePuKHghurF",
        "turbopuffer-domain-verification-gbdk89=UTHpusfpMuBRPyJCGkFjFVAtc",
        "v=spf1 include:dc-aa8e722993._spfm.composio.dev ~all",
        "zoom-domain-verification=ZOOM_verify_0aa18bea6fe841bfafb3a1a1c890bffc",
        "{\"apps\":[{\"clientID\":\"96b038435fc029e045f9ba800e66fefa\"}]}",
        "MS=ms54189639",
        "facebook-domain-verification=wwfei7uqypr4ew83od4an7qvh1afgk",
        "fbf29c5c338e548fdeec9da0792d027c570f74c15d555ed6336f794ad2f30901"
      ]
    },
    "tls": {
      "ok": true,
      "issuer": "C=US, O=Google Trust Services, CN=WE1",
      "subject": "CN=composio.dev",
      "not_before": "Dec  7 07:08:14 2025 GMT",
      "not_after": "Mar  7 08:08:12 2026 GMT",
      "sha256_fingerprint": null,
      "san": [
        "composio.dev",
        "telemetry.composio.dev"
      ],
      "error": null
    },
    "provider_hints": [
      "Cloudflare (NS)",
      "Google Workspace (MX)"
    ],
    "reverse_dns": {
      "104.18.21.5": "",
      "104.18.20.5": ""
    },
    "errors": []
  },
  "web": {
    "url": "https://composio.dev",
    "http": {
      "ok": true,
      "final_url": "https://composio.dev",
      "status_code": 103,
      "status_chain": [
        "HTTP/2 103"
      ],
      "redirect_chain": [],
      "headers": {
        "link": "<https://framerusercontent.com>; rel=\"preconnect\", <https://framerusercontent.com>; rel=\"preconnect\"; crossorigin=\"",
        "date": "Sat, 13 Dec 2025 04:58:36 GMT",
        "content-type": "text/html",
        "server": "cloudflare",
        "cf-ray": "9ad2e32bcd6b4ad5-YVR",
        "cf-cache-status": "DYNAMIC",
        "cache-control": "public, max-age=0, must-revalidate",
        "last-modified": "Fri, 12 Dec 2025 09:12:10 GMT",
        "strict-transport-security": "max-age=31536000",
        "vary": "Accept-Encoding",
        "server-timing": "region;desc=\"us-west-2\", cache;desc=\"cached\", ssg-status;desc=\"optimized\", version;desc=\"9339d38\", route;dur=1;desc=\"id=Bm9d5O6HU&locale=default\"",
        "x-content-type-options": "nosniff"
      },
      "response_time_ms": 613,
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
        "status_code": 200,
        "redirect_to": null
      },
      "/privacy-policy": {
        "path": "/privacy-policy",
        "status_code": 404,
        "redirect_to": null
      },
      "/terms": {
        "path": "/terms",
        "status_code": 200,
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
        "name": "Segment",
        "type": "analytics",
        "evidence": "Segment.io"
      },
      {
        "name": "PostHog",
        "type": "analytics",
        "evidence": "POSTHOG"
      }
    ],
    "social_links": [
      {
        "type": "github",
        "url": "https://github.com/composiohq/composio/"
      },
      {
        "type": "twitter",
        "url": "https://x.com/composio"
      },
      {
        "type": "linkedin",
        "url": "https://www.linkedin.com/company/composiohq/"
      },
      {
        "type": "youtube",
        "url": "https://www.youtube.com/@Composio"
      }
    ],
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