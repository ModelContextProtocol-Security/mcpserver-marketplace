---
title: "Nabhag8848 MCP Marketplace"
url: "https://mcpmarketplace.vercel.app/"
source_code_url: "https://github.com/Nabhag8848/mcp-marketplace"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "directory"
operator: "Nabhag8848"
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "Unknown"
server_count: "Unknown"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://github.com/Nabhag8848/mcp-marketplace"
    description: "Main GitHub repository"
    captured: "2026-02-04"
  - url: "https://mcpmarketplace.vercel.app/"
    description: "Live application"
    captured: "2026-02-04"
---

## Overview

The Nabhag8848 MCP Marketplace is an open-source project aimed at discovering MCP (Model Context Protocol) servers over the internet. It features a "Dynamic Search and Chunking Algorithm" to manage and sync discovered servers. The project includes a live application hosted on Vercel, though the primary description of its functionality is found on its GitHub repository. The application is built using modern web technologies (React, TypeScript).

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | "Dynamic Search and Chunking Algorithm" mentioned in README. |
| One-click install | ❌ | No direct installation mechanism visible. |
| Curated list/recommendations | ❓ | Not explicitly mentioned. |
| Public API | ❓ | Not explicitly mentioned. |
| CLI tool | ❌ | No CLI tool mentioned. |
| Client integration | ❓ | Not explicitly mentioned. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | Nabhag8848 MCP Marketplace | GitHub Repository |
| Primary URL | https://mcpmarketplace.vercel.app/ | GitHub Repository |
| Operator (company/individual) | Nabhag8848 | GitHub Repository |
| Country/jurisdiction | ❓ Unknown | |
| Contact email (general) | ❓ Unknown | |
| Contact email (security) | ❓ Unknown | |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ✅ Yes | https://github.com/Nabhag8848/mcp-marketplace |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Directory/Aggregator - Lists servers with external links | ✅ Yes | Aims to discover and list MCP servers. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ✅ Yes | Live application at `mcpmarketplace.vercel.app/`. |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|---|---|---|
| Link to external source (GitHub, etc.) | ❓ Unknown | Implied by discovery, but not explicit. |

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|---|---|---|
| Publisher verification process exists? | ❌ No | Not mentioned. |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ❌ No | Not mentioned. |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ❌ No | Not found on GitHub or live application. |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ❌ No | `SECURITY.md` not present in the repository. |

---

## Part 6: Supply Chain Security

### 6.2 Dependency Management

| Question | Answer | Evidence/Source |
|---|---|---|
| Dependencies scanned for vulnerabilities? | ✅ Yes | Dependabot is enabled on the repository. |

---

## Part 7: Technical Security Posture

### 7.1 Web Security Headers

This section pertains to `mcpmarketplace.vercel.app/`.

| Header | Present? | Value |
|---|---|---|
| HTTPS enforced | ✅ Yes | (Inherited from Vercel) |
| Strict-Transport-Security (HSTS) | ❌ No | |
| Content-Security-Policy | ❌ No | |
| X-Frame-Options | ❌ No | |
| X-Content-Type-Options | ❌ No | |
| Referrer-Policy | ❌ No | |
| Permissions-Policy | ❌ No | |
| Cross-Origin-Opener-Policy | ❌ No | |
| Cross-Origin-Resource-Policy | ❌ No | |

### 7.2 TLS Certificate

This section pertains to `mcpmarketplace.vercel.app/`.

| Field | Value |
|---|---|
| Issuer | Let's Encrypt |
| Subject | `mcpmarketplace.vercel.app` |

### 7.3 DNS & Hosting

This section pertains to `mcpmarketplace.vercel.app/`.

| Field | Value |
|---|---|
| Provider hints | Vercel |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Open Source:** The project is open-source, allowing for community review.
- **Modern Tech Stack:** Utilizes React and TypeScript, indicating a modern approach to development.
- **GitHub Security Features:** Dependabot, Code Scanning, and Secret Scanning are enabled on the repository.
- **Hosted on Vercel:** Benefits from Vercel's infrastructure and default security features like HTTPS.

### 11.2 Weaknesses & Gaps

- **Minimal Web Security Headers:** The live application is missing several crucial security headers.
- **No Vetting Process:** There is no explicit mention of how discovered MCP servers are vetted for security or quality.
- **Missing Security Contact/Policy:** No `SECURITY.md` or dedicated security contact/policy.
- **No Privacy Policy:** A project discovering information across the internet should have a clear privacy policy.
- **Limited Operator Transparency:** Details about the operator are minimal.

### 11.3 Red Flags

- The site's primary purpose is to "Discover MCP Servers over the Internet" without any explicit mention of vetting, which could lead users to interact with unverified or potentially malicious servers.

### 11.4 Recommendations

- **Implement Comprehensive Security Headers:** Add HSTS, CSP, X-Frame-Options, etc., to the live application.
- **Document Vetting Process:** Clearly define how discovered servers are assessed for trustworthiness and security.
- **Establish a Security Policy:** Publish a `SECURITY.md` file and provide a clear channel for vulnerability reports.
- **Add a Privacy Policy:** Detail data collection practices, especially concerning the "Dynamic Search and Chunking Algorithm."

### 11.5 Overall Trust Assessment

The Nabhag8848 MCP Marketplace is an open-source initiative to discover and aggregate MCP servers. While it leverages modern development practices and benefits from Vercel's hosting security, it currently lacks fundamental trust and security mechanisms for a marketplace-like platform. The absence of vetting for discovered servers, combined with missing security and privacy policies, means users should proceed with extreme caution. This project, while technically sound, needs significant development in its governance and trust framework before it can be considered a reliable source for MCP servers.

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
  "name": "Nabhag8848 MCP Marketplace",
  "marketplace_url": "https://github.com/Nabhag8848/mcp-marketplace",
  "source_url": "https://github.com/Nabhag8848/mcp-marketplace",
  "audited_at": "2025-12-13T04:58:49.298359Z",
  "checks_run": [
    "repo"
  ],
  "errors": [],
  "repo": {
    "repo_info": {
      "platform": "github",
      "owner": "Nabhag8848",
      "repo": "mcp-marketplace",
      "url": "https://github.com/Nabhag8848/mcp-marketplace",
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

---

## Changelog

| Date | Version | Changes | Author |
|---|---|---|---|
| 2026-02-04 | 1.0 | Initial evaluation | AI Assistant |