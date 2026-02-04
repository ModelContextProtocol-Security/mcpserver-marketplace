---
title: "MCP Jungle"
url: "https://github.com/mcpjungle/MCPJungle"
source_code_url: "https://github.com/mcpjungle/MCPJungle"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "paas"
operator: "mcpjungle"
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "Unknown"
server_count: "Unknown"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://github.com/mcpjungle/MCPJungle"
    description: "Main GitHub repository"
    captured: "2026-02-04"
---

## Overview

MCPJungle is an open-source, self-hosted Gateway for Model Context Protocol (MCP) Servers, designed for AI agents. It allows developers to register and manage MCP servers and their tools from a central location, acting as a unified MCP gateway for AI Agents. It provides features for server management, tool registration, client integration (e.g., Claude, Cursor), and supports various transports. It also includes advanced capabilities like authentication, Access Control Lists (ACLs), and observability for "enterprise mode" deployments.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | Allows AI agents to discover registered tools/servers. |
| One-click install | ❓ | Installation involves deploying the gateway, then registering servers. |
| Curated list/recommendations | ✅ | Tools can be registered and managed. |
| Public API | ✅ | Functions as a unified MCP gateway for AI Agents. |
| CLI tool | ✅ | `mcpjungle` CLI for interaction. |
| Client integration | ✅ | Provides configuration examples for Claude and Cursor. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | MCP Jungle | GitHub Repository |
| Primary URL | https://github.com/mcpjungle/MCPJungle | GitHub Repository |
| Operator (company/individual) | mcpjungle | GitHub Repository |
| Country/jurisdiction | ❓ Unknown | |
| Contact email (general) | ❓ Unknown | |
| Contact email (security) | ❓ Unknown | |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ✅ Yes | https://github.com/mcpjungle/MCPJungle |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Registry - Provides API for programmatic discovery | ✅ Yes | Acts as an MCP gateway with programmatic access. |
| Code Hosting - Hosts server source code or packages | ✅ Yes | It's a platform for managing/registering servers. |
| Hosted Execution (PaaS) - Runs MCP servers on their infrastructure | ✅ Yes | Manages registered MCP servers and provides a gateway for execution. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| CLI tool | ✅ Yes | `mcpjungle` CLI. |
| Integrated into MCP client(s) | ✅ Yes | Integrates with Claude and Cursor. |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|---|---|---|
| API documentation available? | ✅ Yes | The README provides extensive details on usage and features. |
| Authentication required for read? | ✅ Yes | Supported in enterprise mode. |
| Rate limiting? | ❓ Unknown | Not explicitly mentioned. |
| OpenAPI/Swagger spec? | ❓ Unknown | Not explicitly mentioned. |
| API terms of use? | ❓ Unknown | |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|---|---|---|
| Package manager (npm, pip, etc.) | ✅ Yes | Installation via Homebrew or Docker image. |
| Hosted execution (marketplace runs the server) | ✅ Yes | Manages and provides access to registered MCP servers. |

### 3.3 Source Accessibility

| Question | Answer | Evidence/Source |
|---|---|---|
| Marketplace source code available? | ✅ Yes | https://github.com/mcpjungle/MCPJungle |
| Self-hostable? | ✅ Yes | It is designed as a self-hosted gateway. |

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|---|---|---|
| Publisher verification process exists? | ❓ Unknown | Not explicitly mentioned for registered servers/tools. |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ❓ Unknown | No explicit vetting process mentioned for tools. |

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

N/A - This is a self-hosted gateway; web security headers depend on the deployment.

### 7.7 Authentication & Authorization

| Question | Answer | Evidence/Source |
|---|---|---|
| Authentication methods supported | ✅ Yes | Enterprise mode supports authentication with static tokens. |
| API tokens scoped and time-limited? | ❓ Unknown | |
| Access Control Lists (ACLs) | ✅ Yes | Supported in enterprise mode. |
| Role-Based Access Control (RBAC) | ✅ Yes | User accounts with limited privileges. |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Open Source and Self-Hosted:** Provides transparency and full control to the deployer.
- **Comprehensive Gateway Features:** Offers robust management for MCP servers, tools, and clients.
- **Enterprise Features:** Includes authentication, ACLs, and observability, indicating a focus on production use.
- **Strong GitHub Security:** Utilizes Dependabot, Code Scanning, and Secret Scanning.
- **Stateful Connections:** Addresses performance issues for STDIO-based servers.
- **Flexible Deployment:** Supports Homebrew, Docker, and direct binary execution.

### 11.2 Weaknesses & Gaps

- **Missing Security Policy:** No `SECURITY.md` or documented vulnerability disclosure process.
- **No Privacy Policy:** For a gateway that manages communication and potentially user data (in enterprise mode), a privacy policy is essential.
- **Vetting of Registered Tools:** While it manages tools, there's no explicit mention of vetting for the security or quality of those tools.
- **Operator Transparency:** While the GitHub organization is clear, details about the team or its governance are not.

### 11.3 Red Flags

- None immediately apparent for the core gateway software itself, assuming a secure deployment. The risks are more related to the lack of guidance for deployers regarding privacy and security policies, and the potential for unvetted tools.

### 11.4 Recommendations

- **Implement a Security Policy:** Publish a `SECURITY.md` with clear vulnerability disclosure guidelines.
- **Develop a Privacy Policy:** Provide guidance for deployers on data handling, especially concerning user accounts and observability features.
- **Guidance on Tool Vetting:** Offer advice or mechanisms for deployers to vet the MCP servers and tools they register.
- **Enhance Operator Transparency:** Provide more details about the `mcpjungle` team and project governance.

### 11.5 Overall Trust Assessment

MCP Jungle is a highly capable and well-designed open-source gateway for MCP servers, offering significant features for managing AI agent interactions. Its self-hosted nature grants deployers considerable control and security. However, as an infrastructure component, the project needs to bolster its own trust framework by implementing clear security and privacy policies. The lack of a `SECURITY.md` and a privacy policy, especially with enterprise features like user accounts and observability, represents a notable gap. Deployers should carefully review its code and implement their own robust security and privacy measures.

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
  "name": "MCP Jungle",
  "marketplace_url": "https://github.com/mcpjungle/MCPJungle",
  "source_url": "https://github.com/mcpjungle/MCPJungle",
  "audited_at": "2025-12-13T04:58:39.366295Z",
  "checks_run": [
    "repo"
  ],
  "errors": [],
  "repo": {
    "repo_info": {
      "platform": "github",
      "owner": "mcpjungle",
      "repo": "MCPJungle",
      "url": "https://github.com/mcpjungle/MCPJungle",
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