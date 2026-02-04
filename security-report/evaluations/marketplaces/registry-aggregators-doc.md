---
title: "Registry Aggregators (Doc)"
url: "https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/registry-aggregators.mdx"
source_code_url: "https://github.com/modelcontextprotocol/registry"
is_marketplace: no
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "documentation"
operator: "Model Context Protocol"
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "Unknown"
server_count: "Unknown"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/registry-aggregators.mdx"
    description: "Registry Aggregators Documentation"
    captured: "2026-02-04"
  - url: "https://github.com/modelcontextprotocol/registry"
    description: "Main GitHub repository"
    captured: "2026-02-04"
---

## Overview

"Registry Aggregators (Doc)" refers to a documentation file within the `modelcontextprotocol/registry` GitHub repository. This document outlines how external entities, termed "aggregators," can consume the MCP Registry's unauthenticated read-only REST API to build their own server marketplaces, complete with features like user ratings and security scanning. It provides technical details on API consumption, pagination, filtering, and server status management, and introduces the concept of a "Subregistry" that implements the MCP Registry's OpenAPI spec.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | Aggregators can implement this based on the consumed API. |
| Curated list/recommendations | ✅ | Aggregators can provide additional value like user ratings and security scanning. |
| Public API | ✅ | The MCP Registry offers a REST API for consumption. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | Registry Aggregators (Doc) | Document Title |
| Primary URL | https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/registry-aggregators.mdx | Document URL |
| Operator (company/individual) | Model Context Protocol | GitHub Organization |
| Country/jurisdiction | ❓ Unknown | |
| Contact email (general) | ❓ Unknown | Not found in this document. |
| Contact email (security) | ❓ Unknown | Not found in this document. |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ✅ Yes | https://github.com/modelcontextprotocol/registry |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Registry - Provides API for programmatic discovery | ✅ Yes | The document describes how to consume the MCP Registry API. |
| Documentation | ✅ Yes | This entry itself is a piece of documentation. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Public API (registry endpoint) | ✅ Yes | `GET /v0.1/servers` and other endpoints described. |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|---|---|---|
| API documentation available? | ✅ Yes | The `.mdx` file serves as documentation for aggregators. |
| Authentication required for read? | ❌ No | "unauthenticated read-only REST API." |
| Rate limiting? | ❓ Unknown | Not mentioned in this document. |
| OpenAPI/Swagger spec? | ✅ Yes | Aggregators can act as subregistries by implementing the OpenAPI spec. |
| API terms of use? | ❓ Unknown | Not mentioned in this document. |

---

## Part 3: Server Delivery Model

### 3.3 Source Accessibility

| Question | Answer | Evidence/Source |
|---|---|---|
| Marketplace source code available? | ✅ Yes | The `modelcontextprotocol/registry` repository. |

---

## Part 4: Trust & Verification

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ❓ Unknown | The document mentions `status` field for moderation policy violations, but not initial vetting. |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ❌ No | Not found in this document. |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ❌ No | Not found in this document. |

---

## Part 6: Supply Chain Security

### 6.2 Dependency Management

| Question | Answer | Evidence/Source |
|---|---|---|
| Dependencies scanned for vulnerabilities? | ✅ Yes | Dependabot is enabled on the repository. |

---

## Part 7: Technical Security Posture

### 7.1 Web Security Headers

N/A - This is a GitHub documentation file.

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Clear Documentation:** Provides clear instructions for aggregators to consume the MCP Registry API.
- **Open-Source Repository:** Hosted on an active and verified GitHub repository with strong security features (Dependabot, Code Scanning, Secret Scanning, Signed Commits).
- **Verified Organization:** Operated by "Model Context Protocol", a verified GitHub organization.
- **Standardized API:** Encourages use of REST API and OpenAPI spec for interoperability.

### 11.2 Weaknesses & Gaps

- **Limited Scope of Document:** This document is purely technical guidance for aggregators and does not cover the broader security or policy aspects of the main MCP Registry.
- **Absence of Specific Policies:** The document itself does not contain privacy or security policies, which would reside with the main MCP Registry.

### 11.3 Red Flags

- None for the document itself. Potential red flags would be with the main MCP Registry or the aggregators implementing its API.

### 11.4 Recommendations

- **Cross-reference Policies:** The document should ideally link to the privacy and security policies of the main MCP Registry for aggregators to be aware of.
- **Guidance on Aggregator Responsibilities:** Provide guidance to aggregators on their responsibilities for security, privacy, and vetting if they build a marketplace on top of the registry.

### 11.5 Overall Trust Assessment

The "Registry Aggregators (Doc)" document is a highly valuable and well-structured technical guide for building on top of the MCP Registry. It comes from a reputable and secure GitHub organization. While the document itself has no inherent security flaws, its trustworthiness is directly tied to the overall security and policies of the main MCP Registry (which this document is a part of) and the practices of the aggregators who choose to implement it. It serves as an excellent foundation for secure interoperability within the MCP ecosystem.

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
  "name": "Registry Aggregators (Doc)",
  "marketplace_url": "https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/registry-aggregators.mdx",
  "source_url": "https://github.com/modelcontextprotocol/registry",
  "audited_at": "2025-12-13T04:58:11.730650Z",
  "checks_run": [
    "repo",
    "source_repo"
  ],
  "errors": [],
  "repo": {
    "repo_info": {
      "platform": "github",
      "owner": "modelcontextprotocol",
      "repo": "registry",
      "url": "https://github.com/modelcontextprotocol/registry",
      "is_org": true
    },
    "security_files": {
      "security_md": false,
      "security_md_url": null,
      "security_policy": false,
      "code_of_conduct": false,
      "contributing_md": false,
      "license": "MIT",
      "license_url": "https://github.com/modelcontextprotocol/registry/blob/main/LICENSE"
    },
    "org_verification": {
      "is_org": true,
      "org_name": "Model Context Protocol",
      "verified": true,
      "verified_domains": []
    },
    "activity": {
      "stars": 6115,
      "forks": 527,
      "watchers": 73,
      "open_issues": 101,
      "open_prs": 1,
      "last_commit": "2025-12-12T22:38:26Z",
      "last_release": "2025-11-18T08:19:35Z",
      "created_at": "2025-02-05T17:58:01Z",
      "updated_at": "2025-12-13T03:57:40Z",
      "archived": false
    },
    "security_features": {
      "dependabot_enabled": true,
      "code_scanning_enabled": true,
      "secret_scanning_enabled": true,
      "branch_protection": false,
      "signed_commits": true,
      "security_advisories": []
    },
    "topics": [
      "mcp",
      "mcp-servers"
    ],
    "errors": []
  },
  "source_repo": {
    "repo_info": {
      "platform": "github",
      "owner": "modelcontextprotocol",
      "repo": "registry",
      "url": "https://github.com/modelcontextprotocol/registry",
      "is_org": true
    },
    "security_files": {
      "security_md": false,
      "security_md_url": null,
      "security_policy": false,
      "code_of_conduct": false,
      "contributing_md": false,
      "license": "MIT",
      "license_url": "https://github.com/modelcontextprotocol/registry/blob/main/LICENSE"
    },
    "org_verification": {
      "is_org": true,
      "org_name": "Model Context Protocol",
      "verified": true,
      "verified_domains": []
    },
    "activity": {
      "stars": 6115,
      "forks": 527,
      "watchers": 73,
      "open_issues": 101,
      "open_prs": 1,
      "last_commit": "2025-12-12T22:38:26Z",
      "last_release": null,
      "created_at": "2025-02-05T17:58:01Z",
      "updated_at": "2025-12-13T03:57:40Z",
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
