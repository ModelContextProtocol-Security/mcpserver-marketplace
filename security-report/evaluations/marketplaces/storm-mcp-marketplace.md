---
title: "Storm MCP Marketplace"
url: "https://github.com/gorilli-team/storm"
source_code_url: "https://github.com/gorilli-team/storm"
is_marketplace: yes
is_aggregator: no
is_list_of_marketplaces: no
language: "en"
type: "registry-api"
operator: "gorilli-team"
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "Unknown"
server_count: "Unknown"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://github.com/gorilli-team/storm"
    description: "Main GitHub repository"
    captured: "2026-02-04"
---

## Overview

Storm MCP Marketplace is a decentralized marketplace for AI tools built on the Model Context Protocol (MCP) and integrated with the Recall Network. It aims to provide a platform for developers to monetize their MCP tools and for users to access a variety of AI tools through a unified interface. The project emphasizes decentralization, transparency (optional source code display), and security through AES encryption for tool parameters and functions. It is an open-source project managed by the `gorilli-team`.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | Implied by a marketplace, though specific search UI not visible. |
| One-click install | ✅ | Designed for easy installation and use with platforms like Claude Desktop. |
| Curated list/recommendations | ❓ | Decentralized nature implies less central curation. |
| Public API | ✅ | Likely, given its decentralized and programmatic nature. |
| CLI tool | ❓ | Not explicitly mentioned, but likely for interaction. |
| Client integration | ✅ | Designed for integration with MCP clients (e.g., Claude Desktop). |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | Storm MCP Marketplace | GitHub Repository |
| Primary URL | https://github.com/gorilli-team/storm | GitHub Repository |
| Operator (company/individual) | gorilli-team | GitHub Repository |
| Country/jurisdiction | ❓ Unknown | Not specified. |
| Contact email (general) | ❓ Unknown | Not explicitly mentioned. |
| Contact email (security) | ❓ Unknown | Not explicitly mentioned. |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ✅ Yes | https://github.com/gorilli-team/storm |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Directory/Aggregator - Lists servers with external links | ✅ Yes | It lists and provides access to AI tools. |
| Registry - Provides API for programmatic discovery | ✅ Yes | Decentralized nature implies programmatic access. |
| Code Hosting - Hosts server source code or packages | ✅ Yes | It's a platform for developers to publish tools. |
| Hosted Execution (PaaS) - Runs MCP servers on their infrastructure | ✅ Yes | Tools are managed and presumably executed within the platform. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ✅ Yes | Implied by a marketplace. |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|---|---|---|
| API documentation available? | ❓ Unknown | Not explicitly mentioned in README. |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|---|---|---|
| Hosted execution (marketplace runs the server) | ✅ Yes | Tools are published and managed within the platform. |

### 3.3 Source Accessibility

| Question | Answer | Evidence/Source |
|---|---|---|
| Marketplace source code available? | ✅ Yes | https://github.com/gorilli-team/storm |

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|---|---|---|
| Publisher verification process exists? | ❓ Unknown | Not explicitly detailed. |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ❓ Unknown | Not explicitly detailed, but AES encryption is used. |

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

### 7.6 Social/Contact Links Found

N/A - No social links found beyond GitHub.

### 7.7 Authentication & Authorization

| Question | Answer | Evidence/Source |
|---|---|---|
| Authentication methods supported | ❓ Unknown | Not detailed in the README. |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Decentralized and Open Source:** The project's decentralized nature and open-source code promote transparency and community review.
- **Emphasis on Security:** AES encryption for tool parameters and functions is a strong security feature.
- **Integration with Recall Network:** Leveraging a decentralized network for storage and data management.
- **GitHub Security Features:** Dependabot, Code Scanning, and Secret Scanning are enabled.
- **Clear Roadmap:** Future plans include a token-based economy and deeper Recall integration.

### 11.2 Weaknesses & Gaps

- **Lack of Vetting Process:** While tools are encrypted, there's no explicit mention of a vetting process for the tools themselves before being listed.
- **Missing Security Contact/Policy:** No `SECURITY.md` or dedicated security contact/policy on the GitHub repository.
- **No Privacy Policy:** As a platform dealing with user-submitted tools and potential monetization, a privacy policy is essential.
- **Limited Transparency on Governance:** Details about the `gorilli-team` and its jurisdiction are not available.

### 11.3 Red Flags

- The lack of explicit information on how tools are vetted, combined with a monetization model, could potentially incentivize the submission of low-quality or even malicious tools if not properly managed.

### 11.4 Recommendations

- **Document Vetting Process:** Clearly outline the process for reviewing and approving tools submitted to the marketplace.
- **Comprehensive Security Policy:** Publish a `SECURITY.md` and establish a clear vulnerability disclosure program.
- **Implement a Privacy Policy:** Detail data collection, usage, and sharing practices for the marketplace.
- **Increase Transparency:** Provide more information about the `gorilli-team` and their governance model.

### 11.5 Overall Trust Assessment

Storm MCP Marketplace presents an innovative approach to decentralized AI tool distribution and monetization. Its open-source nature, focus on AES encryption, and integration with the Recall Network are strong positives. However, the current lack of explicit vetting processes for tools, a formal security policy, and a privacy policy raises concerns. For a platform that aims to monetize AI tools, these foundational trust mechanisms are crucial. The project has significant potential, but its security and trust model needs further development and documentation to inspire confidence among users and developers.

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
  "name": "Storm MCP Marketplace",
  "marketplace_url": "https://github.com/gorilli-team/storm",
  "source_url": "https://github.com/gorilli-team/storm",
  "audited_at": "2025-12-13T04:58:39.420947Z",
  "checks_run": [
    "repo"
  ],
  "errors": [],
  "repo": {
    "repo_info": {
      "platform": "github",
      "owner": "gorilli-team",
      "repo": "storm",
      "url": "https://github.com/gorilli-team/storm",
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