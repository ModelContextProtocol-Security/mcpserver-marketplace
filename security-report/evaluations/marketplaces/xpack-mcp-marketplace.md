---
title: "XPack MCP Marketplace"
url: "https://xpack.ai"
source_code_url: "https://github.com/xpack-ai/XPack-MCP-Marketplace"
is_marketplace: yes
is_aggregator: no
is_list_of_marketplaces: no
language: "en"
type: "code-hosting"
operator: "xpack.ai"
operator_jurisdiction: "Unknown"
contact_email: "contact@xpack.com"
security_email: "Unknown"
server_count: "Unknown"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://github.com/xpack-ai/XPack-MCP-Marketplace"
    description: "Main GitHub repository"
    captured: "2026-02-04"
---

## Overview

XPack MCP Marketplace is described as the "world's first open-source MCP monetization platform," enabling users to quickly create and sell their own MCP servers. It provides a full stack solution including a frontend, backend, billing integration, and user management. The project is open-source under the Apache 2.0 license and is designed for commercial use. It emphasizes easy deployment and boasts integration with several AI tools and platforms.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | Implied by "marketplace" and "monetization platform." |
| One-click install | ✅ | "Quick-start.sh" script for deployment. |
| Curated list/recommendations | ❓ | No explicit curation, but it's a platform for selling. |
| Public API | ✅ | Allows users to create/sell MCP servers via API. |
| CLI tool | ✅ | Deployment via `curl` and `bash` script. |
| Client integration | ✅ | Mentions partners like Claude Code, Cursor, LobeChat. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | XPack MCP Marketplace | GitHub Repository |
| Primary URL | https://xpack.ai | GitHub Repository |
| Operator (company/individual) | xpack.ai | GitHub Repository |
| Country/jurisdiction | ❓ Unknown | Not specified. |
| Contact email (general) | ✅ Yes | `contact@xpack.com` (from GitHub) |
| Contact email (security) | ❓ Unknown | Not explicitly mentioned. |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ✅ Yes | https://github.com/xpack-ai/XPack-MCP-Marketplace |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Registry - Provides API for programmatic discovery | ✅ Yes | Functions as a platform where APIs are consumed/sold. |
| Code Hosting - Hosts server source code or packages | ✅ Yes | Users sell their MCP servers, implying hosting. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ✅ Yes | `xpack.ai` (implied). |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|---|---|---|
| API documentation available? | ✅ Yes | Implied by "One-click OpenAPI → MCP service config". |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|---|---|---|
| Hosted execution (marketplace runs the server) | ✅ Yes | The platform helps users "sell their own MCP server", implying execution. |

### 3.3 Source Accessibility

| Question | Answer | Evidence/Source |
|---|---|---|
| Marketplace source code available? | ✅ Yes | https://github.com/xpack-ai/XPack-MCP-Marketplace |

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|---|---|---|
| Publisher verification process exists? | ❓ Unknown | Not explicitly detailed. |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ❓ Unknown | Not explicitly detailed. |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ❓ Unknown | Not found on GitHub, `xpack.ai` not checked. |

### 5.2 Terms of Service

| Question | Answer | Evidence/Source |
|---|---|---|
| Terms of service exists? | ❓ Unknown | Not found on GitHub, `xpack.ai` not checked. |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ❌ No | `SECURITY.md` not present in the repository. |

---

## Part 6: Supply Chain Security

XPack is a platform for building and selling MCP servers, making supply chain security critical.

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

This evaluation is based on the GitHub repository only. No web audit was performed for `xpack.ai`. The security posture for the hosted platform would depend on its implementation.

### 7.2 TLS Certificate

N/A - Based on GitHub repository.

### 7.3 DNS & Hosting

N/A - Based on GitHub repository.

### 7.6 Social/Contact Links Found

| Type | URL |
|---|---|
| GitHub | https://github.com/xpack-ai |
| Discord | Link |

### 7.7 Authentication & Authorization

| Question | Answer | Evidence/Source |
|---|---|---|
| Authentication methods supported | ✅ Yes | Email & Google OAuth Sign in. |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Open-Source with Commercial Focus:** The platform is open-source and explicitly designed for commercial use, offering transparency and flexibility.
- **Comprehensive Feature Set:** Includes billing, user management, and SEO-friendly pages for MCP services.
- **Active Security Features:** The GitHub repository utilizes Dependabot, Code Scanning, and Secret Scanning.
- **Clear Deployment Instructions:** Offers both quick-start and Docker Compose deployment options.
- **Explicit Licensing:** Clearly states the Apache 2.0 license.

### 11.2 Weaknesses & Gaps

- **Lack of Vetting Details:** No explicit information on how MCP servers sold through the platform are vetted for security or quality.
- **Missing Security Contact/Policy:** No `SECURITY.md` or dedicated security contact/policy on the GitHub repository.
- **Privacy/ToS for the Hosted Platform:** While a contact email is provided, clear Privacy Policy and Terms of Service for the hosted platform are not readily apparent from the GitHub page alone.
- **Jurisdiction Unknown:** No information about the operating entity's country or legal jurisdiction.

### 11.3 Red Flags

- The lack of explicit security vetting for "sell your own MCP server" could lead to a marketplace of potentially vulnerable or malicious servers if not properly managed.

### 11.4 Recommendations

- **Detailed Vetting Process:** Document and implement a robust vetting process for all MCP servers offered through the platform.
- **Comprehensive Security Policy:** Publish a `SECURITY.md` and establish a clear vulnerability disclosure program.
- **Clear Privacy Policy and Terms of Service:** Ensure these policies are easily accessible on `xpack.ai` and cover the specifics of their monetization platform.
- **Transparency on Jurisdiction:** Clearly state the legal jurisdiction of the operating entity.

### 11.5 Overall Trust Assessment

XPack MCP Marketplace is an ambitious and promising open-source project aiming to build a commercial ecosystem around MCP servers. Its emphasis on a comprehensive feature set and active use of GitHub's security tools are commendable. However, as a platform that enables users to "create and sell their own MCP server," the current lack of transparency around server vetting and a formal security policy presents a significant trust gap. Users looking to purchase or deploy servers from this marketplace should demand clear evidence of security reviews and publisher verification. The project has strong potential but needs to mature its trust mechanisms.

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
  "name": "XPack MCP Marketplace",
  "marketplace_url": "https://github.com/xpack-ai/XPack-MCP-Marketplace",
  "source_url": "https://github.com/xpack-ai/XPack-MCP-Marketplace",
  "audited_at": "2025-12-13T04:58:38.271167Z",
  "checks_run": [
    "repo"
  ],
  "errors": [],
  "repo": {
    "repo_info": {
      "platform": "github",
      "owner": "xpack-ai",
      "repo": "XPack-MCP-Marketplace",
      "url": "https://github.com/xpack-ai/XPack-MCP-Marketplace",
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