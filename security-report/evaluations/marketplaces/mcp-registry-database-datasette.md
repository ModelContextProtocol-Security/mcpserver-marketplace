---
title: "MCP Registry Database (Datasette)"
url: "https://lite.datasette.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Frosmur%2Fofficial-mcp-registry-database%2Fmain%2Fofficial_mcp_registry.db#/official_mcp_registry/servers"
source_code_url: "https://github.com/rosmur/official-mcp-registry-database"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "directory"
operator: "rosmur (Datasette Lite)"
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "Unknown"
server_count: "Unknown"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://lite.datasette.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Frosmur%2Fofficial-mcp-registry-database%2Fmain%2Fofficial_mcp_registry.db#/official_mcp_registry/servers"
    description: "Datasette Lite instance"
    captured: "2026-02-04"
  - url: "https://github.com/rosmur/official-mcp-registry-database"
    description: "GitHub repository for the database"
    captured: "2026-02-04"
---

## Overview

The "MCP Registry Database (Datasette)" is a Datasette Lite instance that provides a browsable interface to a SQLite database of MCP servers. The database itself is hosted as a raw file on a GitHub repository (`rosmur/official-mcp-registry-database`). This setup allows for interactive exploration of MCP server data directly in the browser, leveraging the Datasette tool for data visualization and querying. It functions as a directory, aggregating and displaying data from a community-maintained source.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | Datasette interface allows querying/filtering. |
| One-click install | ❌ | Data browser only. |
| Curated list/recommendations | ✅ | Displays data from a curated database. |
| Public API | ✅ | Datasette provides a JSON API for the data. |
| CLI tool | ❌ | Not directly. |
| Client integration | ❓ | Datasette provides a JSON API for programmatic access. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | MCP Registry Database (Datasette) | CSV entry |
| Primary URL | https://lite.datasette.io/?url=... | Browser |
| Operator (company/individual) | rosmur (for database), Simon Willison (for Datasette) | GitHub repos |
| Country/jurisdiction | ❓ Unknown | |
| Contact email (general) | ❓ Unknown | |
| Contact email (security) | ❓ Unknown | |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ✅ Yes | https://github.com/rosmur/official-mcp-registry-database |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Directory/Aggregator - Lists servers with external links | ✅ Yes | Displays data from an aggregated database. |
| Registry - Provides API for programmatic discovery | ✅ Yes | Datasette provides a JSON API. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ✅ Yes | Datasette interface. |
| Public API (registry endpoint) | ✅ Yes | Datasette JSON API. |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|---|---|---|
| Link to external source (GitHub, etc.) | ✅ Yes | The database contains links to server details. |

### 3.3 Source Accessibility

| Question | Answer | Evidence/Source |
|---|---|---|
| Marketplace source code available? | ✅ Yes | For the database itself (`rosmur/official-mcp-registry-database`). |

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|---|---|---|
| Publisher verification process exists? | ❓ Unknown | Depends on `rosmur`'s database curation process. |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ❓ Unknown | Depends on `rosmur`'s database curation process. |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ❌ No | All Datasette Lite paths return 404. |
| Analytics/tracking tools used | ✅ Yes | Plausible Analytics (from audit). |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ❌ No | All Datasette Lite paths return 404. |

---

## Part 6: Supply Chain Security

### 6.2 Dependency Management

| Question | Answer | Evidence/Source |
|---|---|---|
| Dependencies scanned for vulnerabilities? | ✅ Yes | Datasette Lite (GitHub Pages) and `rosmur`'s repo use Dependabot, Code Scanning, Secret Scanning. |

---

## Part 7: Technical Security Posture

This section refers to the Datasette Lite platform and the upstream GitHub repository.

### 7.1 Web Security Headers (for Datasette Lite)

| Header | Present? | Value |
|---|---|---|
| HTTPS enforced | ✅ Yes | |
| Strict-Transport-Security (HSTS) | ❌ No | |
| Content-Security-Policy | ❌ No | |

### 7.2 TLS Certificate (for Datasette Lite)

| Field | Value |
|---|---|
| Issuer | Let's Encrypt |
| Subject | `lite.datasette.io` |

### 7.3 DNS & Hosting (for Datasette Lite)

| Field | Value |
|---|---|
| Provider hints | Vercel (NS), GitHub Pages (CNAME) |

### 7.7 Authentication & Authorization

| Question | Answer | Evidence/Source |
|---|---|---|
| Authentication methods supported | ❌ No | Not applicable for a public data browser. |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Open Data & Tooling:** Leverages Datasette Lite for transparent, browsable access to MCP server data.
- **GitHub-Hosted Data:** The database source is open and version-controlled on GitHub.
- **GitHub Security Features:** The database repository (`rosmur/official-mcp-registry-database`) utilizes Dependabot, Code Scanning, and Secret Scanning.
- **JSON API:** Datasette automatically provides a JSON API for programmatic access to the data.

### 11.2 Weaknesses & Gaps

- **Limited Security Headers:** Datasette Lite lacks comprehensive web security headers.
- **No Operator Transparency for Datasette:** While `rosmur` operates the database, Datasette Lite itself is a tool from Simon Willison, and there's no clear 'operator' for the combination.
- **No Policies:** Datasette Lite does not provide explicit privacy, terms of service, or security policies, which might be expected for a public-facing data browser.
- **Reliance on Upstream Data:** The quality and vetting of the MCP server data depend entirely on `rosmur`'s curation process for the database.
- **Plausible Analytics:** Uses analytics without a clear privacy policy for the Datasette Lite instance.

### 11.3 Red Flags

- The absence of clear policies (privacy, terms, security) for a public data browser, especially one using analytics, raises transparency concerns.

### 11.4 Recommendations

- **Implement Security Headers:** Datasette Lite (or its deployment) should implement comprehensive web security headers.
- **Clarify Operator/Policies:** For this specific deployment, clear policies (privacy, terms of service) should be provided, or at least links to Datasette's general policies.
- **Document Data Curation:** `rosmur` should clearly document the process for curating and vetting servers included in the database.

### 11.5 Overall Trust Assessment

The "MCP Registry Database (Datasette)" offers a highly transparent and accessible way to browse MCP server data via Datasette Lite. Its strength lies in the open nature of the data source (GitHub) and the Datasette tool itself. However, the specific deployment lacks essential web security headers and explicit policies (privacy, terms, security), creating a trust gap. While the underlying GitHub repository shows good security practices, the public-facing Datasette Lite instance requires more attention to these aspects to be fully trustworthy for a general audience. Users should be aware that the vetting of the listed MCP servers depends solely on the `rosmur` repository's maintainers.

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
  "name": "MCP Registry Database (Datasette)",
  "marketplace_url": "https://lite.datasette.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Frosmur%2Fofficial-mcp-registry-database%2Fmain%2Fofficial_mcp_registry.db#/official_mcp_registry/servers",
  "source_url": "https://github.com/rosmur/official-mcp-registry-database",
  "audited_at": "2025-12-13T04:58:11.732876Z",
  "checks_run": [
    "domain",
    "web",
    "source_repo"
  ],
  "errors": [],
  "domain": {
    "hostname": "lite.datasette.io",
    "registrable_domain": "datasette.io",
    "dns": {
      "a": [
        "simonw.github.io.",
        "185.199.108.153",
        "185.199.109.153",
        "185.199.110.153",
        "185.199.111.153"
      ],
      "aaaa": [
        "simonw.github.io.",
        "2606:50c0:8000::153",
        "2606:50c0:8001::153",
        "2606:50c0:8002::153",
        "2606:50c0:8003::153"
      ],
      "cname": [
        "simonw.github.io"
      ],
      "ns": [
        "ns2.vercel-dns.com",
        "ns1.vercel-dns.com"
      ],
      "mx": [
        "route2.mx.cloudflare.net",
        "route1.mx.cloudflare.net",
        "route3.mx.cloudflare.net"
      ],
      "txt": [
        "google-site-verification=wHw15S1fkNOMzk42PEVK6XLnSG9qEfyq6paO8_G4IVU"
      ]
    },
    "tls": {
      "ok": true,
      "issuer": "C=US, O=Let's Encrypt, CN=R13",
      "subject": "CN=lite.datasette.io",
      "not_before": "Nov  1 04:56:41 2025 GMT",
      "not_after": "Jan 30 04:56:40 2026 GMT",
      "sha256_fingerprint": null,
      "san": [
        "lite.datasette.io"
      ],
      "error": null
    },
    "provider_hints": [
      "Vercel (NS)",
      "GitHub Pages (CNAME)"
    ],
    "reverse_dns": {
      "simonw.github.io.": "cdn-185-199-111-153.github.com",
      "185.199.108.153": "cdn-185-199-108-153.github.com",
      "185.199.109.153": "cdn-185-199-109-153.github.com"
    },
    "errors": []
  },
  "web": {
    "url": "https://lite.datasette.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Frosmur%2Fofficial-mcp-registry-database%2Fmain%2Fofficial_mcp_registry.db#/official_mcp_registry/servers",
    "http": {
      "ok": true,
      "final_url": "https://lite.datasette.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Frosmur%2Fofficial-mcp-registry-database%2Fmain%2Fofficial_mcp_registry.db#/official_mcp_registry/servers",
      "status_code": 200,
      "status_chain": [
        "HTTP/2 200"
      ],
      "redirect_chain": [],
      "headers": {
        "server": "GitHub.com",
        "content-type": "text/html; charset=utf-8",
        "last-modified": "Wed, 10 Sep 2025 12:33:56 GMT",
        "access-control-allow-origin": "*",
        "etag": "\"68c17034-2b8b\"",
        "expires": "Sat, 13 Dec 2025 04:55:25 GMT",
        "cache-control": "max-age=600",
        "x-proxy-cache": "MISS",
        "x-github-request-id": "8B4A:12F5FE:19E5AF:1AAED3:693CEF63",
        "accept-ranges": "bytes",
        "age": "0",
        "date": "Sat, 13 Dec 2025 04:58:13 GMT",
        "via": "1.1 varnish",
        "x-served-by": "cache-bfi-krnt7300082-BFI",
        "x-cache": "HIT",
        "x-cache-hits": "0",
        "x-timer": "S1765601893.255637,VS0,VE89",
        "vary": "Accept-Encoding",
        "x-fastly-request-id": "cf3be1048e30d8b42c91c29356aced6268a9779a",
        "content-length": "11147"
      },
      "response_time_ms": 279,
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
    "paths": {},
    "mixed_content": {
      "http_links_count": 0,
      "http_subresources_count": 0,
      "samples": []
    },
    "trackers": [
      {
        "name": "Plausible",
        "type": "analytics",
        "evidence": "plausible.io"
      }
    ],
    "social_links": [
      {
        "type": "github",
        "url": "https://github.com/simonw/datasette-lite"
      }
    ],
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
      "owner": "rosmur",
      "repo": "official-mcp-registry-database",
      "url": "https://github.com/rosmur/official-mcp-registry-database",
      "is_org": false
    },
    "security_files": {
      "security_md": false,
      "security_md_url": null,
      "security_policy": false,
      "code_of_conduct": false,
      "contributing_md": false,
      "license": "GPL-3.0",
      "license_url": "https://github.com/rosmur/official-mcp-registry-database/blob/main/LICENSE"
    },
    "org_verification": {
      "is_org": false,
      "org_name": null,
      "verified": false,
      "verified_domains": []
    },
    "activity": {
      "stars": 3,
      "forks": 1,
      "watchers": 0,
      "open_issues": 0,
      "open_prs": 0,
      "last_commit": null,
      "last_release": null,
      "created_at": "2025-09-12T00:30:11Z",
      "updated_at": "2025-12-13T00:20:48Z",
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

```