---
title: "ShareMCP 导航"
url: "https://sharemcp.com/"
source_code_url: "https://github.com/ArcStellars/ShareMCP"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "zh"
type: "directory"
operator: "ArcStellars"
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "Unknown"
server_count: "186"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://sharemcp.com/"
    description: "Main website"
    captured: "2026-02-04"
---

## Overview

ShareMCP 导航 is a Chinese-language website that serves as a simple directory or "navigation" site for MCP servers. It lists 186 servers, categorized by function (e.g., Browser Automation, Cloud Platforms, Databases). The site is operated by "ArcStellars" according to the GitHub repository. It is a very basic, static HTML page that links to external resources, presumably the MCP servers themselves, though the links were not inspected.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ⚠️ | No search, but provides category-based browsing. |
| One-click install | ❌ | It is a simple link directory. |
| Curated list/recommendations | ✅ | The entire site is a curated list. |
| Public API | ❌ | No API is available. |
| CLI tool | ❌ | No CLI tool is mentioned. |
| Client integration | ❌ | No integrations are mentioned. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | ShareMCP 服务资源站 (Share MCP Service Resource Station) | Website Title |
| Primary URL | https://sharemcp.com/ | Browser |
| Operator (company/individual) | ArcStellars | GitHub Repository |
| Country/jurisdiction | ❓ Unknown | |
| Contact email (general) | ❓ Unknown | |
| Contact email (security) | ❓ Unknown | |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ✅ Yes | https://github.com/ArcStellars/ShareMCP

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Directory/Aggregator - Lists servers with external links | ✅ Yes | This is its primary function. |
| Curated List - Manually maintained list (e.g., awesome-list) | ✅ Yes | The site is a static, curated list of links. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ✅ Yes | https://sharemcp.com/ |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|---|---|---|
| Link to external source (GitHub, etc.) | ✅ Yes | This is the only method. |

---

## Part 4: Trust & Verification

This section is not applicable, as there are no trust or verification mechanisms present on the site. It is a simple list of links.

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ❌ No | All policy-related paths return 404. |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ❌ No | All security-related paths return 404. |

---

## Part 6: Supply Chain Security

N/A - This is a static link directory.

---

## Part 7: Technical Security Posture

### 7.1 Web Security Headers

| Header | Present? | Value |
|---|---|---|
| HTTPS enforced | ✅ Yes | |
| Strict-Transport-Security (HSTS) | ✅ Yes | `max-age=31536000` |
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
| Issuer | C=US, O=Let's Encrypt, CN=E7 |
| Subject | CN=sharemcp.com |
| Valid from | Nov 17 23:02:12 2025 GMT |
| Valid until | Feb 15 23:02:11 2026 GMT |
| SHA256 fingerprint | null |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- The site uses HTTPS and has an HSTS header, which is a good baseline.
- The source code for the website is available on GitHub.

### 11.2 Weaknesses & Gaps

- The website is missing almost all recommended security headers.
- There are no policies (Privacy, ToS, Security) of any kind.
- The GitHub repository is sparse, with no license, documentation, or any files other than the website's HTML.
- There is no information about the operator or how to contact them.
- There is no information about how the list is curated or vetted.

### 11.3 Red Flags

- **Complete Lack of Transparency:** The operator is anonymous, and there are no policies or contact methods.
- **No Trust Signals:** This is just a list of links with no indication of quality, safety, or trustworthiness.

### 11.4 Recommendations

- **Add Basic Security Headers:** Implement CSP, X-Frame-Options, and other standard headers.
- **Add a License:** The GitHub repository should have a license.
- **Add Basic Policies:** A simple Privacy Policy and Terms of Service would add a layer of transparency.
- **Provide Contact Information:** A way to contact the operator is essential.

### 11.5 Overall Trust Assessment

ShareMCP 导航 is a very simple, static webpage that lists links to MCP servers. It should not be considered a marketplace, but rather an unvetted, unaudited "awesome list". Users should exercise extreme caution and perform their own security evaluations on any link they follow from this site. It carries no signals of trust.

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
  "name": "ShareMCP 导航",
  "marketplace_url": "https://sharemcp.com/",
  "source_url": "https://github.com/ArcStellars/ShareMCP",
  "audited_at": "2025-12-13T04:59:07.918886Z",
  "checks_run": [
    "domain",
    "web",
    "source_repo"
  ],
  "errors": [],
  "domain": {
    "hostname": "sharemcp.com",
    "registrable_domain": "sharemcp.com",
    "dns": {
      "a": [
        "34.142.151.139"
      ],
      "aaaa": [],
      "cname": [],
      "ns": [
        "dns2.hichina.com",
        "dns1.hichina.com"
      ],
      "mx": [],
      "txt": []
    },
    "tls": {
      "ok": true,
      "issuer": "C=US, O=Let's Encrypt, CN=E7",
      "subject": "CN=sharemcp.com",
      "not_before": "Nov 17 23:02:12 2025 GMT",
      "not_after": "Feb 15 23:02:11 2026 GMT",
      "sha256_fingerprint": null,
      "san": [
        "sharemcp.com",
        "www.sharemcp.com"
      ],
      "error": null
    },
    "provider_hints": [],
    "reverse_dns": {
      "34.142.151.139": "139.151.142.34.bc.googleusercontent.com"
    },
    "errors": []
  },
  "web": {
    "url": "https://sharemcp.com/",
    "http": {
      "ok": true,
      "final_url": "https://sharemcp.com/",
      "status_code": 200,
      "status_chain": [
        "HTTP/2 200"
      ],
      "redirect_chain": [],
      "headers": {
        "server": "openresty",
        "date": "Sat, 13 Dec 2025 04:59:10 GMT",
        "content-type": "text/html",
        "content-length": "471",
        "last-modified": "Thu, 20 Mar 2025 06:31:17 GMT",
        "etag": "\"67dbb635-1d7\"",
        "strict-transport-security": "max-age=31536000",
        "accept-ranges": "bytes"
      },
      "response_time_ms": 672,
      "error": null
    },
    "security_headers": {
      "strict_transport_security": "max-age=31536000",
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
    "paths": {},
    "mixed_content": {
      "http_links_count": 0,
      "http_subresources_count": 0,
      "samples": []
    },
    "trackers": [],
    "social_links": [],
    "cookies": [],
    "server_info": {
      "server": "openresty"
    },
    "errors": []
  },
  "source_repo": {
    "repo_info": {
      "platform": "github",
      "owner": "ArcStellars",
      "repo": "ShareMCP",
      "url": "https://github.com/ArcStellars/ShareMCP",
      "is_org": false
    },
    "security_files": {
      "security_md": false,
      "security_md_url": null,
      "security_policy": false,
      "code_of_conduct": false,
      "contributing_md": false,
      "license": null,
      "license_url": null
    },
    "org_verification": {
      "is_org": false,
      "org_name": null,
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