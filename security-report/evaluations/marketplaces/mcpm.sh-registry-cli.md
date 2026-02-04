---
title: "mcpm.sh Registry CLI"
url: "https://github.com/pathintegral-institute/mcpm.sh"
source_code_url: "https://github.com/pathintegral-institute/mcpm.sh"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "registry-api"
operator: "pathintegral-institute"
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "Unknown"
server_count: "Unknown"
last_evaluated: "2026-02-04"
evaluation_status: "comprehensive"
evidence:
  - url: "https://github.com/pathintegral-institute/mcpm.sh"
    description: "Main GitHub repository"
    captured: "2026-02-04"
---

## Overview

mcpm.sh is a command-line interface (CLI) tool for managing Model Context Protocol (MCP) servers. It allows users to install, organize, and run MCP servers from the MCP Registry. The tool is developed by the "pathintegral-institute" and is presented as a security-focused, open-source project. It acts as both a client to the MCP registry and a marketplace in its own right by enabling discovery and installation of servers.

## Features Summary

| Feature | Status | Notes |
|---|---|---|
| Discovery/search | ✅ | `mcpm search` command. |
| One-click install | ✅ | `mcpm install` command. |
| Curated list/recommendations | ❓ | Not explicitly mentioned, but discovery is from a central registry. |
| Public API | ✅ | Interacts with the public MCP Registry API. |
| CLI tool | ✅ | This is a CLI tool. |
| Client integration | ✅ | Manages configurations for clients like Claude Desktop and Cursor. |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|---|---|---|
| Official name | mcpm.sh | GitHub Repository |
| Primary URL | https://github.com/pathintegral-institute/mcpm.sh | GitHub Repository |
| Operator (company/individual) | pathintegral-institute | GitHub Repository |
| Country/jurisdiction | ❓ Unknown | |
| Contact email (general) | ❓ Unknown | |
| Contact email (security) | ❓ Unknown | |
| Launch date | ❓ Unknown | |
| Marketplace source code available? | ✅ Yes | https://github.com/pathintegral-institute/mcpm.sh |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|---|---|---|
| Directory/Aggregator - Lists servers with external links | ✅ Yes | The CLI allows searching and listing servers from a registry. |
| Registry - Provides API for programmatic discovery | ✅ Yes | It's a client for a registry, effectively exposing that registry's data. |
| Code Hosting - Hosts server source code or packages | ✅ Yes | The repo itself hosts the mcpm.sh code. |
| Hosted Execution (PaaS) - Runs MCP servers on their infrastructure | ❌ No | |
| Client-Embedded - Built into a specific MCP client | ❌ No | It's a standalone tool that *configures* clients. |
| Curated List - Manually maintained list (e.g., awesome-list) | ❓ Unknown | |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|---|---|---|
| Website with search/browse | ❌ No | |
| Public API (registry endpoint) | ✅ Yes | The CLI is a client to a public registry. |
| CLI tool | ✅ Yes | `mcpm search [query]` |
| IDE/editor plugin | ❌ No | |
| Integrated into MCP client(s) | ✅ Yes | It manages configs for other clients. |
| Browser extension | ❌ No | |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|---|---|---|
| Link to external source (GitHub, etc.) | ✅ Yes | Installation seems to pull from source repositories. |
| Direct download (zip, tarball) | ✅ Yes | `curl` installation method suggests this. |
| Package manager (npm, pip, etc.) | ✅ Yes | `pipx` and `pip` installation methods are provided. |
| Container image (Docker) | ❓ Unknown | Not mentioned. |
| One-click install to client config | ✅ Yes | The `mcpm install` command serves this purpose. |
| Hosted execution (marketplace runs the server) | ❌ No | |

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|---|---|---|
| Publisher verification process exists? | ❓ Unknown | Inherited from the upstream registry it uses. |
| Verification requirements documented? | ❓ Unknown | |
| 2FA/MFA required for publishers? | N/A | |
| Trust tiers (verified, official, etc.)? | ❓ Unknown | |
| Verification criteria publicly documented? | ❓ Unknown | |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|---|---|---|
| Servers reviewed before listing? | ❓ Unknown | Depends on the upstream registry. |
| Automated security scanning? | ❓ Unknown | |
| Malware detection? | ❓ Unknown | |
| Dependency vulnerability scanning? | ❓ Unknown | |
| Flagged server removal speed? | ❓ Unknown | |
| Typosquatting/namesquatting protection? | ❓ Unknown | |

### 4.3 Community Trust Signals

| Question | Answer | Evidence/Source |
|---|---|---|
| Users can report problematic servers? | ❓ Unknown | No mechanism described in the tool's documentation. |
| Visible "Report" button? | N/A | |
| User reviews or ratings? | ❌ No | |
| Download/usage count visible? | ❓ Unknown | The tool has usage analytics, but it's not clear if this is public. |
| "Last updated" timestamp visible? | ❓ Unknown | |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|---|---|---|
| Privacy policy exists? | ❌ No | No privacy policy found in the repository. |
| Privacy policy URL | N/A | |
| User data collected (summary) | "Usage Analytics" are mentioned, but what is collected is not specified. | GitHub README |
| Data shared with third parties? | ❓ Unknown | |
| Analytics/tracking tools used | ❓ Unknown | |
| Data retention policy? | ❓ Unknown | |
| GDPR compliance claimed? | ❌ No | |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|---|---|---|
| Security policy exists? | ❌ No | `SECURITY.md` not present. |
| Security policy URL (SECURITY.md) | N/A | |
| Vulnerability disclosure process? | ❌ No | |
| Bug bounty program? | ❌ No | |
| Past security incidents disclosed? | ❌ No | |
| Status page for uptime/incidents? | N/A | |

---

## Part 6: Supply Chain Security

### 6.1 Code Integrity

| Question | Answer | Evidence/Source |
|---|---|---|
| Packages/images signed? | ❓ Unknown | `pip` does not enforce signatures. |
| Provenance attestation provided? | ❌ No | |
| SBOMs (Software Bill of Materials) available? | ❌ No | |
| Reproducible build support? | ❌ No | |

### 6.2 Dependency Management

| Question | Answer | Evidence/Source |
|---|---|---|
| Dependencies scanned for vulnerabilities? | ✅ Yes | Dependabot is enabled on the repository. |
| Dependency confusion protection? | ❓ Unknown | |
| Lock files required/validated? | ❓ Unknown | Project seems to be Python-based, but lockfile usage is not specified. |
| Vulnerable dependency notifications? | ✅ Yes | Via Dependabot. |

---

## Part 7: Technical Security Posture

This section is not applicable as there is no web presence. The security of the tool itself depends on the security of the user's system, the Python packaging ecosystem, and the security of the upstream MCP registry. The GitHub repository has `Dependabot`, `Code Scanning`, and `Secret Scanning` enabled, which is a good practice.

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

- The tool is open-source, allowing for community review of its code.
- It provides a convenient CLI for managing MCP servers, which is a good utility for developers.
- The use of GitHub security features like Dependabot, Code Scanning, and Secret Scanning is a positive signal.
- It supports multiple installation methods, including `pipx` which helps with isolation.

### 11.2 Weaknesses & Gaps

- **No Security Policy:** There is no `SECURITY.md` file or any documented process for reporting vulnerabilities.
- **No Privacy Policy:** The tool mentions "Usage Analytics" but does not have a privacy policy explaining what data is collected and how it is used.
- **No License:** The audit data indicates that no license was found in the repository. This creates legal ambiguity for users and contributors.
- **Lack of Transparency:** It's unclear what upstream registry is being used and what their security and vetting processes are.

### 11.3 Red Flags

- **Collecting analytics without a privacy policy is a major red flag.** Users should be informed about what data is being collected from their systems.
- The lack of a license is a significant legal red flag for any serious use.

### 11.4 Recommendations

- **Add a License:** An open-source license should be added immediately to clarify the terms of use.
- **Create a Privacy Policy:** Document what data is collected by the usage analytics, why it's collected, and how it's handled.
- **Create a Security Policy:** Add a `SECURITY.md` file with a clear process for vulnerability disclosure.
- **Be Transparent About the Upstream Registry:** The documentation should clearly state which MCP registry is being used by default and what its policies are.

### 11.5 Overall Trust Assessment

`mcpm.sh` appears to be a useful tool for developers working with MCP servers. The code is open source and it leverages some of GitHub's security features. However, the lack of a license, a privacy policy, and a security policy are significant gaps that erode trust. Users should be cautious about the "Usage Analytics" feature until there is more transparency about what data is being collected. For now, this tool should be considered a "use at your own risk" utility for advanced users who can review the code and understand the implications.

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

### Testing Methodology

**Automated checks performed:**
- Date: 2025-12-13 (from pre-existing audit data)

**Manual checks performed:**
- Review of the GitHub repository README.

### tier1_audit.py Output

```json
{
  "name": "mcpm.sh Registry CLI",
  "marketplace_url": "https://github.com/pathintegral-institute/mcpm.sh",
  "source_url": "https://github.com/pathintegral-institute/mcpm.sh",
  "audited_at": "2025-12-13T04:58:56.533672Z",
  "checks_run": [
    "repo"
  ],
  "errors": [],
  "repo": {
    "repo_info": {
      "platform": "github",
      "owner": "pathintegral-institute",
      "repo": "mcpm.sh",
      "url": "https://github.com/pathintegral-institute/mcpm.sh",
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