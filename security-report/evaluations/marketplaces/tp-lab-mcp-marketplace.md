---
title: "TP-Lab MCP Marketplace"
url: "https://mcp.tp.xyz/"
source_code_url: "https://github.com/TP-Lab/mcp-marketplace"
is_marketplace: yes
is_aggregator: no
is_list_of_marketplaces: no
language: "en"
type: "client-embedded"
operator: "TP-Lab"
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "Unknown"
server_count: "1 (Wallet MCP)"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://github.com/TP-Lab/mcp-marketplace"
    description: "Main GitHub repository"
    captured: "2026-02-04"
  - url: "https://mcp.tp.xyz/"
    description: "Official Website"
    captured: "2026-02-04"
---

## Overview

TP-Lab MCP Marketplace presents itself as an "MCP Marketplace" with a current focus on the "Wallet MCP," a tool designed to enable Claude to interact with blockchain technologies (Solana and EVM networks). The project is open-source, with its repository hosted on GitHub. While the GitHub repository indicates the marketplace is "under construction," the associated website `mcp.tp.xyz` provides detailed information about the Wallet MCP and its functionalities, including wallet connection, transaction signing, and token transfers.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ❌ | Only "Wallet MCP" is highlighted. |
| One-click install | ⚠️ | Installation involves manual configuration of Claude for Desktop. |
| Curated list/recommendations | ❌ | Only one MCP is detailed. |
| Public API | ❓ | The Wallet MCP exposes an API for blockchain interaction. |
| CLI tool | ❌ | Not directly. |
| Client integration | ✅ | Specifically designed for Claude for Desktop. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | TP-Lab MCP Marketplace (Wallet MCP) | GitHub Repository, Website |
| Primary URL | https://mcp.tp.xyz/ | Website |
| Operator (company/individual) | TP-Lab | GitHub Repository |
| Country/jurisdiction | ❓ Unknown | Not specified. |
| Contact email (general) | ❓ Unknown | Telegram group mentioned for support. |
| Contact email (security) | ❓ Unknown | Not explicitly mentioned. |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ✅ Yes | https://github.com/TP-Lab/mcp-marketplace |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Registry - Provides API for programmatic discovery | ✅ Yes | The Wallet MCP provides programmatic blockchain interaction. |
| Client-Embedded - Built into a specific MCP client | ✅ Yes | Designed for integration with Claude for Desktop. |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ✅ Yes | https://mcp.tp.xyz/ |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|---|---|---|
| API documentation available? | ❓ Unknown | Implicit from code examples, no formal docs linked. |
| Authentication required for read? | ❓ Unknown | |
| Rate limiting? | ❓ Unknown | |
| OpenAPI/Swagger spec? | ❌ No | |
| API terms of use? | ❌ No | |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|---|---|---|
| One-click install to client config | ⚠️ | Manual JSON configuration in Claude for Desktop. |

### 3.3 Source Accessibility

| Question | Answer | Evidence/Source |
|---|---|---|
| Marketplace source code available? | ✅ Yes | https://github.com/TP-Lab/mcp-marketplace |

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|---|---|---|
| Publisher verification process exists? | ❌ No | Not mentioned. |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ❓ Unknown | Only one MCP (Wallet MCP) is detailed. |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ❌ No | Not found on website or GitHub. |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ❌ No | `SECURITY.md` not present in the repository, nor on the website. |

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

This section pertains to `mcp.tp.xyz`.

| Header | Present? | Value |
|---|---|---|
| HTTPS enforced | ✅ Yes | |
| Strict-Transport-Security (HSTS) | ❌ No | |
| Content-Security-Policy | ❌ No | |
| X-Frame-Options | ❌ No | |
| X-Content-Type-Options | ❌ No | |
| Referrer-Policy | ❌ No | |
| Permissions-Policy | ❌ No | |
| Cross-Origin-Opener-Policy | ❌ No | |
| Cross-Origin-Resource-Policy | ❌ No | |

### 7.2 TLS Certificate

This section pertains to `mcp.tp.xyz`.

| Field | Value |
|---|---|
| Issuer | Let's Encrypt |
| Subject | CN=mcp.tp.xyz |

### 7.3 DNS & Hosting

This section pertains to `mcp.tp.xyz`.

| Field | Value |
|---|---|
| Provider hints | Unknown |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- **Open Source:** The project's source code is publicly available on GitHub, fostering transparency.
- **Clear Use Case:** Focuses on a specific and relevant integration (blockchain interaction for Claude).
- **GitHub Security Features:** Dependabot, Code Scanning, and Secret Scanning are enabled on the repository.
- **Detailed Website:** The `mcp.tp.xyz` website provides clear instructions and examples for the Wallet MCP.

### 11.2 Weaknesses & Gaps

- **Lack of Comprehensive Security Headers:** The website `mcp.tp.xyz` is missing critical security headers beyond HTTPS.
- **Missing Security Contact/Policy:** No `SECURITY.md` or dedicated security contact/policy.
- **No Privacy Policy:** For a tool interacting with sensitive blockchain wallets, a privacy policy is essential.
- **Limited Scope:** Currently, only the "Wallet MCP" is detailed, suggesting the "marketplace" aspect is nascent.
- **Manual Installation:** Requires manual JSON configuration in Claude, which could be error-prone.

### 11.3 Red Flags

- The absence of a privacy policy for a tool handling sensitive blockchain interactions is a significant red flag. Users are providing configuration details and implicitly trusting the tool with their wallet interactions.

### 11.4 Recommendations

- **Implement Full Security Headers:** Ensure `mcp.tp.xyz` has comprehensive security headers including HSTS, CSP, and X-Frame-Options.
- **Develop a Robust Privacy Policy:** Clearly outline data handling practices, especially concerning blockchain interactions and user information.
- **Establish a Security Policy:** Publish a `SECURITY.md` file and provide a clear channel for vulnerability reports.
- **Improve Transparency:** Provide clear information about TP-Lab, its governance, and long-term vision for the "marketplace."
- **Simplify Installation:** Explore more streamlined installation methods for Claude for Desktop.

### 11.5 Overall Trust Assessment

TP-Lab MCP Marketplace, primarily represented by its Wallet MCP, offers an innovative integration for Claude with blockchain technologies. While its open-source nature and use of GitHub's security features are positive, the absence of a privacy policy for a sensitive tool, along with missing web security headers and a formal security policy, raises significant trust concerns. Users interacting with blockchain assets should exercise extreme caution and fully understand the code and implications before configuring Wallet MCP. The "marketplace" aspect is currently minimal, focusing on a single tool.

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
  "name": "TP-Lab MCP Marketplace",
  "marketplace_url": "https://github.com/TP-Lab/mcp-marketplace",
  "source_url": "https://github.com/TP-Lab/mcp-marketplace",
  "audited_at": "2025-12-13T04:58:48.244568Z",
  "checks_run": [
    "repo"
  ],
  "errors": [],
  "repo": {
    "repo_info": {
      "platform": "github",
      "owner": "TP-Lab",
      "repo": "mcp-marketplace",
      "url": "https://github.com/TP-Lab/mcp-marketplace",
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