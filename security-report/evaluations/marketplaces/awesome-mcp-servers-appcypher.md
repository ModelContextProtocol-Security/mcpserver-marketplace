---
title: "Awesome MCP Servers (appcypher)"
url: "https://github.com/appcypher/awesome-mcp-servers"
source_code_url: "https://github.com/appcypher/awesome-mcp-servers"
is_marketplace: no
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "curated-list"
operator: "appcypher"
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "Unknown"
server_count: "Unknown"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://github.com/appcypher/awesome-mcp-servers"
    description: "Main GitHub repository"
    captured: "2026-02-04"
---

## Overview

"Awesome MCP Servers (appcypher)" is a curated list of Model Context Protocol (MCP) server implementations hosted on GitHub. It categorizes various MCP servers by their functionality, serving as a directory for discovery. Notably, the repository includes explicit security warnings and best practices for running MCP servers, highlighting the importance of sandboxing. It acts purely as an informational resource rather than a platform for direct server deployment or interaction.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | A curated list for browsing and discovering servers. |
| One-click install | ❌ | Purely informational, links to external projects. |
| Curated list/recommendations | ✅ | The entire repository is a curated list. |
| Public API | ❌ | No API is available. |
| CLI tool | ❌ | Not directly. |
| Client integration | ❌ | Provides information for integration, but is not a client itself. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | Awesome MCP Servers (appcypher) | GitHub Repository |
| Primary URL | https://github.com/appcypher/awesome-mcp-servers | GitHub Repository |
| Operator (company/individual) | appcypher | GitHub Repository |
| Country/jurisdiction | ❓ Unknown | |
| Contact email (general) | ❓ Unknown | |
| Contact email (security) | ❓ Unknown | |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ✅ Yes | https://github.com/appcypher/awesome-mcp-servers |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Directory/Aggregator - Lists servers with external links | ✅ Yes | Links to various MCP server implementations. |
| Curated List - Manually maintained list (e.g., awesome-list) | ✅ Yes | The definition of an "awesome list." |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ✅ Yes | GitHub repository can be browsed. |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|---|---|---|
| Link to external source (GitHub, etc.) | ✅ Yes | Links to the source repositories of listed MCP servers. |

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|---|---|---|
| Publisher verification process exists? | ❌ No | Not applicable for a curated list. |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ✅ Yes | Implied by "curated list"; explicit security warnings are provided. |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ❌ No | Not applicable for a static GitHub list. |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ❌ No | `SECURITY.md` not present in the repository, but security warnings are in README. |

---

## Part 6: Supply Chain Security

N/A - This is a curated list of links, not a platform that hosts or runs code directly.

---

## Part 7: Technical Security Posture

### 7.1 Web Security Headers

N/A - This is a GitHub repository; web security headers apply to deployed instances.

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Curated List:** Provides a categorized list of MCP servers, aiding discovery.
- **Security Awareness:** Explicitly includes security warnings and best practices, showing awareness of potential risks.
- **Open Source:** The list itself is open source and can be contributed to.
- **GitHub Security Features:** Dependabot, Code Scanning, and Secret Scanning are enabled on the repository.

### 11.2 Weaknesses & Gaps

- **No Formal Vetting Process:** While curated, the specific criteria for inclusion and continuous monitoring are not detailed.
- **No License:** The audit data indicates a license file was not found, which is a legal ambiguity for a public repository.
- **No Explicit Security Policy:** Although security warnings are present, a formal `SECURITY.md` is missing.
- **Limited Scope:** As a static list, it lacks dynamic features like real-time status updates or user reviews.

### 11.3 Red Flags

- The absence of a clear license is a legal red flag for any public repository.

### 11.4 Recommendations

- **Add a License:** Include a clear open-source license (e.g., MIT, Apache 2.0) to the repository.
- **Formalize Vetting:** Document the criteria and process for adding/removing servers from the list.
- **Add a `SECURITY.md`:** Provide a formal vulnerability disclosure process.

### 11.5 Overall Trust Assessment

"Awesome MCP Servers (appcypher)" is a valuable informational resource for the MCP community. Its curated nature and inclusion of security warnings are positive aspects, encouraging responsible use of MCP servers. However, the lack of a clear license, formal vetting process details, and a dedicated security policy are areas for improvement. While not a "marketplace" in the traditional sense, its influence as a discovery hub means its recommendations carry weight, and a more robust trust framework would benefit its users.

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
  "name": "Awesome MCP Servers (appcypher)",
  "marketplace_url": "https://github.com/appcypher/awesome-mcp-servers",
  "source_url": "https://github.com/appcypher/awesome-mcp-servers",
  "audited_at": "2025-12-13T04:58:52.461426Z",
  "checks_run": [
    "repo"
  ],
  "errors": [],
  "repo": {
    "repo_info": {
      "platform": "github",
      "owner": "appcypher",
      "repo": "awesome-mcp-servers",
      "url": "https://github.com/appcypher/awesome-mcp-servers",
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
