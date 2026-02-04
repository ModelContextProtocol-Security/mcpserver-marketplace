---
title: "aiagenta2z MCP Marketplace"
url: "https://github.com/aiagenta2z/mcp-marketplace"
source_code_url: "https://github.com/aiagenta2z/mcp-marketplace"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "registry-api"
operator: "aiagenta2z"
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "Unknown"
server_count: "Unknown"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://github.com/aiagenta2z/mcp-marketplace"
    description: "Main GitHub repository"
    captured: "2026-02-04"
---

## Overview

aiagenta2z MCP Marketplace is an open-source project hosted on GitHub that provides a collection of MCP servers, a registry, web playground, router, and API services. It offers a Python package (`mcp-marketplace`) for searching and listing available MCP tools. The project aims to facilitate the discovery and management of MCP resources for AI agents.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | Python package for searching MCP servers. |
| One-click install | ❓ | Not explicitly stated, but `pip install` is the primary way to get the client. |
| Curated list/recommendations | ❓ | Implied by "collection" but no explicit curation process. |
| Public API | ✅ | "MCP API services" are mentioned. |
| CLI tool | ✅ | Python package with CLI functionality. |
| Client integration | ✅ | Designed for use with AI agents. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | aiagenta2z MCP Marketplace | GitHub Repository |
| Primary URL | https://github.com/aiagenta2z/mcp-marketplace | GitHub Repository |
| Operator (company/individual) | aiagenta2z | GitHub Repository |
| Country/jurisdiction | ❓ Unknown | |
| Contact email (general) | ❓ Unknown | |
| Contact email (security) | ❓ Unknown | |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ✅ Yes | https://github.com/aiagenta2z/mcp-marketplace |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Directory/Aggregator - Lists servers with external links | ✅ Yes | Collects and lists MCP servers. |
| Registry - Provides API for programmatic discovery | ✅ Yes | "MCP Registry" and "MCP API services" mentioned. |
| Code Hosting - Hosts server source code or packages | ✅ Yes | Hosts the `mcp-marketplace` Python package. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Public API (registry endpoint) | ✅ Yes | "MCP API services" mentioned. |
| CLI tool | ✅ Yes | Python package provides CLI for searching. |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|---|---|---|
| Package manager (npm, pip, etc.) | ✅ Yes | `pip install mcp-marketplace`. |

### 3.3 Source Accessibility

| Question | Answer | Evidence/Source |
|---|---|---|
| Marketplace source code available? | ✅ Yes | https://github.com/aiagenta2z/mcp-marketplace |

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
| Privacy policy exists? | ❌ No | Not found in the repository. |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ❌ No | `SECURITY.md` not present in the repository. |

---

## Part 6: Supply Chain Security

### 6.1 Code Integrity

| Question | Answer | Evidence/Source |
|---|---|---|
| SBOMs (Software Bill of Materials) available? | ❌ No | Not mentioned. |

### 6.2 Dependency Management

| Question | Answer | Evidence/Source |
|---|---|---|
| Dependencies scanned for vulnerabilities? | ✅ Yes | Dependabot is enabled on the repository. |

---

## Part 7: Technical Security Posture

### 7.1 Web Security Headers

N/A - This is a GitHub repository; web security headers apply to deployed instances.

### 7.7 Authentication & Authorization

| Question | Answer | Evidence/Source |
|---|---|---|
| Authentication methods supported | ❓ Unknown | Not detailed in the README. |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Open-Source:** The project is open-source, allowing for community review.
- **Python Package:** Provides a convenient Python package for integration with AI agents.
- **Comprehensive Scope:** Aims to provide a collection of servers, registry, playground, router, and API services.
- **GitHub Security Features:** Dependabot, Code Scanning, and Secret Scanning are enabled.

### 11.2 Weaknesses & Gaps

- **Lack of Vetting Process:** No explicit mention of how MCP servers in the collection are vetted for security or quality.
- **Missing Security Contact/Policy:** No `SECURITY.md` or dedicated security contact/policy.
- **No Privacy Policy:** As a project that aggregates and provides access to external resources, a clear privacy policy is important.
- **Limited Transparency:** Details about the operator and the broader governance of the marketplace are not clear.

### 11.3 Red Flags

- The aggregation of MCP servers without clear vetting or security guidelines poses a risk. Users need to be extremely cautious about the security of the individual servers accessed through this marketplace.

### 11.4 Recommendations

- **Document Vetting Process:** Clearly define and document how servers are selected, reviewed, and maintained in the collection.
- **Implement a Security Policy:** Publish a `SECURITY.md` file and establish a clear vulnerability disclosure process.
- **Add a Privacy Policy:** Explain what data, if any, is collected by the Python package or API services.
- **Increase Transparency:** Provide more information about the operator and how the marketplace is governed.

### 11.5 Overall Trust Assessment

aiagenta2z MCP Marketplace is an ambitious open-source effort to create a central hub for MCP servers and services. Its provision of a Python package and API services for discovery is a valuable contribution. However, the current lack of a clear vetting process for the servers it aggregates, along with the absence of security and privacy policies, significantly limits its trustworthiness. Users must exercise extreme caution and perform their own security assessments on any MCP server they discover and integrate through this marketplace.

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
  "name": "aiagenta2z MCP Marketplace",
  "marketplace_url": "https://github.com/aiagenta2z/mcp-marketplace",
  "source_url": "https://github.com/aiagenta2z/mcp-marketplace",
  "audited_at": "2025-12-13T04:58:47.586265Z",
  "checks_run": [
    "repo"
  ],
  "errors": [],
  "repo": {
    "repo_info": {
      "platform": "github",
      "owner": "aiagenta2z",
      "repo": "mcp-marketplace",
      "url": "https://github.com/aiagenta2z/mcp-marketplace",
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
      "updated_at": null
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