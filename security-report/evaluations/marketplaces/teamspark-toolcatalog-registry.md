---
title: "TeamSpark ToolCatalog (Registry)"
url: "https://teamsparkai.github.io/ToolCatalog/registry"
source_code_url: "https://github.com/TeamSparkAI/ToolCatalog"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "curated-list"
operator: "TeamSparkAI"
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "Unknown"
server_count: "Unknown"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://teamsparkai.github.io/ToolCatalog/registry"
    description: "Main website"
    captured: "2026-02-04"
  - url: "https://github.com/TeamSparkAI/ToolCatalog"
    description: "Source code repository"
    captured: "2026-02-04"
---

## Overview

The TeamSpark ToolCatalog is a registry of MCP (Model Context Protocol) servers hosted on GitHub Pages. It is maintained by TeamSparkAI and serves as a curated list of tools. The website itself is a client-side rendered application that loads the server registry. The project emphasizes its role in facilitating the integration of MCP servers into AI agents.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ⚠️ | Client-side rendered, search functionality not directly observable. |
| One-click install | ❌ | It's a catalog, not an installer. |
| Curated list/recommendations | ✅ | Explicitly a "ToolCatalog." |
| Public API | ❓ | No API documentation, `/api` returns 404. |
| CLI tool | ❌ | Not directly, though the project likely supports tooling. |
| Client integration | ✅ | The purpose is to integrate tools into clients. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | TeamSpark ToolCatalog (Registry) | Website Title and Audit Data |
| Primary URL | https://teamsparkai.github.io/ToolCatalog/registry | Browser |
| Operator (company/individual) | TeamSparkAI | GitHub Repository |
| Country/jurisdiction | ❓ Unknown | |
| Contact email (general) | ❓ Unknown | |
| Contact email (security) | ❓ Unknown | |
| Launch date | 2025-07-05 | GitHub Repository Created At |
| Marketplace source code available? | ✅ Yes | https://github.com/TeamSparkAI/ToolCatalog |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Directory/Aggregator - Lists servers with external links | ✅ Yes | Links to external tools/servers. |
| Curated List - Manually maintained list (e.g., awesome-list) | ✅ Yes | Described as a "ToolCatalog." |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ✅ Yes | Hosted on GitHub Pages. |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|---|---|---|
| Link to external source (GitHub, etc.) | ✅ Yes | Implied by "ToolCatalog" nature. |

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|---|---|---|
| Publisher verification process exists? | ❌ No | No information found. |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ❓ Unknown | No information on the vetting process. |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ❌ No | All policy-related paths return 404. |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ❌ No | `SECURITY.md` not present in the repository. |

---

## Part 6: Supply Chain Security

This marketplace is a static website hosted on GitHub Pages that lists tools. Supply chain security largely depends on the tools it links to and GitHub's platform security.

### 6.1 Code Integrity

| Question | Answer | Evidence/Source |
|---|---|---|
| Packages/images signed? | ❌ No | Not applicable for a simple catalog. |

### 6.2 Dependency Management

| Question | Answer | Evidence/Source |
|---|---|---|
| Dependencies scanned for vulnerabilities? | ✅ Yes | Dependabot is enabled on the repository. |

---

## Part 7: Technical Security Posture

### 7.1 Web Security Headers

| Header | Present? | Value |
|---|---|---|
| HTTPS enforced | ✅ Yes | Inherited from GitHub Pages. |
| Strict-Transport-Security (HSTS) | ✅ Yes | `max-age=31556952` (Inherited from GitHub Pages). |
| Content-Security-Policy | ❌ No | Not explicitly set for the page. |
| X-Frame-Options | ❌ No | Not explicitly set. |
| X-Content-Type-Options | ❌ No | Not explicitly set. |
| Referrer-Policy | ❌ No | Not explicitly set. |

### 7.2 TLS Certificate

| Field | Value |
|---|---|
| Issuer | C=GB, ST=Greater Manchester, L=Salford, O=Sectigo Limited, CN=Sectigo RSA Domain Validation Secure Server CA |
| Subject | CN=*.github.io |

### 7.3 DNS & Hosting

| Field | Value |
|---|---|
| Provider hints | GitHub Pages (AWS Route53) |

---

## Part 8: Operator Transparency

### 8.1 Business Model

| Question | Answer | Evidence/Source |
|---|---|---|
| Free or paid? | ✅ Free | Implied, as it's a GitHub Pages site. |
| Registered business entity? | ❓ Unknown | |

### 8.2 Communication & Support

| Question | Answer | Evidence/Source |
|---|---|---|
| Public documentation URL | ❓ Unknown | No specific documentation other than the repo itself. |
| Issue tracker for bug reports | ✅ Yes | GitHub Issues are available on the repository. |

---

## Part 9: Security Incidents

No public security incidents were found related to "TeamSpark ToolCatalog (Registry)" during a web search on 2026-02-04.

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- Hosted on GitHub Pages, benefiting from GitHub's platform security (HTTPS, HSTS).
- Source code is open and available for review.
- The repository utilizes Dependabot, Code Scanning, and Secret Scanning, indicating attention to code security.
- Contains an MIT License, clarifying usage terms.

### 11.2 Weaknesses & Gaps

- **Lack of Specific Security Headers:** The GitHub Pages site does not implement additional security headers like CSP or X-Frame-Options.
- **No Vetting Process:** There's no documented process for reviewing or vetting the quality or security of listed tools.
- **Limited Operator Transparency:** Basic contact and jurisdiction information are missing.
- **No Privacy or Security Policies:** No dedicated policies for the registry itself.

### 11.3 Red Flags

- The implicit endorsement of listed tools without a clear vetting process could lead users to trust potentially insecure tools.

### 11.4 Recommendations

- **Implement additional Security Headers:** While GitHub Pages provides a baseline, adding a Content Security Policy and X-Frame-Options would enhance security.
- **Document Vetting Process:** Clearly outline how tools are selected and reviewed for inclusion in the catalog.
- **Provide Contact Information:** Offer clear ways for users to contact TeamSparkAI, especially regarding security concerns.
- **Add Security.md:** A `SECURITY.md` file in the repository would formalize vulnerability reporting.

### 11.5 Overall Trust Assessment

The TeamSpark ToolCatalog (Registry) offers a curated list of MCP servers, benefiting from GitHub's underlying security infrastructure. The open-source nature and active use of GitHub's security features for the repository itself are positive. However, as a simple catalog, it lacks independent vetting mechanisms for the listed tools and transparency regarding its operation and security policies. Users should treat this as a helpful discovery tool but must exercise their own due diligence in evaluating the security of any tool found within the catalog.

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
  "name": "TeamSpark ToolCatalog (Registry)",
  "marketplace_url": "https://teamsparkai.github.io/ToolCatalog/registry",
  "source_url": "https://github.com/TeamSparkAI/ToolCatalog",
  "audited_at": "2025-12-13T04:58:11.734774Z",
  "checks_run": [
    "domain",
    "web",
    "source_repo"
  ],
  "errors": [],
  "domain": {
    "hostname": "teamsparkai.github.io",
    "registrable_domain": "github.io",
    "dns": {
      "a": [
        "185.199.110.153",
        "185.199.111.153",
        "185.199.108.153",
        "185.199.109.153"
      ],
      "aaaa": [
        "2606:50c0:8002::153",
        "2606:50c0:8003::153",
        "2606:50c0:8000::153",
        "2606:50c0:8001::153"
      ],
      "cname": [],
      "ns": [
        "dns4.p05.nsone.net",
        "ns-1339.awsdns-39.org",
        "ns-1622.awsdns-10.co.uk",
        "ns-393.awsdns-49.com",
        "ns-692.awsdns-22.net",
        "dns1.p05.nsone.net",
        "dns2.p05.nsone.net",
        "dns3.p05.nsone.net"
      ],
      "mx": [],
      "txt": [
        "v=spf1 a -all"
      ]
    },
    "tls": {
      "ok": true,
      "issuer": "C=GB, ST=Greater Manchester, L=Salford, O=Sectigo Limited, CN=Sectigo RSA Domain Validation Secure Server CA",
      "subject": "CN=*.github.io",
      "not_before": "Mar  7 00:00:00 2025 GMT",
      "not_after": "Mar  7 23:59:59 2026 GMT",
      "sha256_fingerprint": null,
      "san": [
        "*.github.io",
        "*.github.com",
        "*.githubusercontent.com",
        "github.com",
        "github.io",
        "githubusercontent.com",
        "www.github.com"
      ],
      "error": null
    },
    "provider_hints": [
      "AWS Route53 (NS)"
    ],
    "reverse_dns": {
      "185.199.110.153": "cdn-185-199-110-153.github.com",
      "185.199.111.153": "cdn-185-199-111-153.github.com",
      "185.199.108.153": "cdn-185-199-108-153.github.com"
    },
    "errors": []
  },
  "web": {
    "url": "https://teamsparkai.github.io/ToolCatalog/registry",
    "http": {
      "ok": true,
      "final_url": "https://teamsparkai.github.io/ToolCatalog/registry",
      "status_code": 200,
      "status_chain": [
        "HTTP/2 200"
      ],
      "redirect_chain": [],
      "headers": {
        "server": "GitHub.com",
        "content-type": "text/html; charset=utf-8",
        "last-modified": "Sat, 13 Dec 2025 02:47:58 GMT",
        "access-control-allow-origin": "*",
        "strict-transport-security": "max-age=31556952",
        "etag": "\"693cd3de-1746\"",
        "expires": "Sat, 13 Dec 2025 04:55:25 GMT",
        "cache-control": "max-age=600",
        "x-proxy-cache": "MISS",
        "x-github-request-id": "8F14:C2206:193EA2:1A061E:693CEF65",
        "accept-ranges": "bytes",
        "age": "0",
        "date": "Sat, 13 Dec 2025 04:58:13 GMT",
        "via": "1.1 varnish",
        "x-served-by": "cache-bfi-krnt7300062-BFI",
        "x-cache": "HIT",
        "x-cache-hits": "0",
        "x-timer": "S1765601893.927912,VS0,VE92",
        "vary": "Accept-Encoding",
        "x-fastly-request-id": "b699035994aada8943c21ee90798ab0d7fcfafba",
        "content-length": "5958"
      },
      "response_time_ms": 309,
      "error": null
    },
    "security_headers": {
      "strict_transport_security": "max-age=31556952",
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
      "server": "GitHub.com",
      "via": "1.1 varnish"
    },
    "errors": []
  },
  "source_repo": {
    "repo_info": {
      "platform": "github",
      "owner": "TeamSparkAI",
      "repo": "ToolCatalog",
      "url": "https://github.com/TeamSparkAI/ToolCatalog",
      "is_org": true
    },
    "security_files": {
      "security_md": false,
      "security_md_url": null,
      "security_policy": false,
      "code_of_conduct": false,
      "contributing_md": false,
      "license": "MIT",
      "license_url": "https://github.com/TeamSparkAI/ToolCatalog/blob/main/LICENSE"
    },
    "org_verification": {
      "is_org": true,
      "org_name": "TeamSpark, LLC",
      "verified": false,
      "verified_domains": []
    },
    "activity": {
      "stars": 8,
      "forks": 1,
      "watchers": 0,
      "open_issues": 0,
      "open_prs": 0,
      "last_commit": "2025-12-13T02:46:40Z",
      "last_release": null,
      "created_at": "2025-07-05T20:41:44Z",
      "updated_at": "2025-12-13T02:46:45Z",
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