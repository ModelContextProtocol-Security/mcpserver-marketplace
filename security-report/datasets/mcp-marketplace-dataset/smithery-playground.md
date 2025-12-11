---
title: "Smithery"
url: "https://smithery.ai"
source_code_url: "https://github.com/smithery-ai"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "registry-api"
operator: "Clavia, Inc."
contact_email: "contact@smithery.ai"
server_count: "3,202+"
last_evaluated: "2025-12-10"
evidence:
  - url: "https://smithery.ai"
    description: "Main marketplace - 3,202 apps listed as of Dec 2025"
  - url: "https://github.com/smithery-ai"
    description: "GitHub org - verified domain smithery.ai, 931+ repos"
  - url: "https://smithery.ai/docs/use/registry"
    description: "Registry API documentation with verification status field"
  - url: "https://smithery.ai/privacy"
    description: "Privacy policy identifying Clavia, Inc. as operator"
  - url: "https://blog.gitguardian.com/breaking-mcp-server-hosting/"
    description: "June 2025 path traversal vulnerability disclosure - fixed in 48 hours"
  - url: "https://blog.gitguardian.com/a-look-into-the-secrets-of-mcp/"
    description: "GitGuardian research: 5.2% of Smithery repos leak secrets"
---

# Smithery

## Overview
Smithery is the largest MCP server registry, hosting 3,200+ servers. Operated by Clavia, Inc. (USA), it provides discovery, hosting, and management of MCP servers. Publishers connect via GitHub to deploy servers. The platform is free to use and widely integrated by MCP clients.

## Features
- Discovery/search: Yes - semantic search with filters (`owner:`, `repo:`, `is:verified`, `is:deployed`)
- One-click install: Yes - hosted servers at `server.smithery.ai/{name}/mcp` with config for Claude Desktop, VS Code, ChatGPT
- Curated list/recommendations: Partial - "verified" badge exists but criteria undocumented
- API: Yes - public registry API at `registry.smithery.ai/servers` with pagination, filtering
- Client integration: Yes - integrated by Cursor, Claude Desktop, and others

## Security

### Tier 1: Automated/Observable Checks

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | All URLs use HTTPS |
| Contact information | ✅ Yes | contact@smithery.ai, Discord, Twitter/X |
| Issue tracker | ⚠️ Partial | GitHub Issues exists (285 open) but many unaddressed |
| Provenance visible | ⚠️ Partial | Namespace shows owner, but no direct source link on listings |
| Official/unofficial distinction | ⚠️ Partial | "verified" badge exists but criteria not public |
| Hosted server coverage | ❌ No | Lists code repos only, no vendor-hosted MCP servers |
| Last updated timestamps | ✅ Yes | `createdAt` and deploy dates shown |

### Tier 2: Manual Investigation

| Check | Status | Notes |
|-------|--------|-------|
| Publisher verification process | ❌ Unknown | No documentation on how verification works |
| Report button | ❌ No | No visible way to report problematic servers |
| Security metadata | ⚠️ Partial | "security scan" field exists but shows null |
| Moderation/curation | ❌ Unknown | No public moderation policy |
| Logo usage policy | ❌ Unknown | No policy on vendor logo usage |
| Security policy (SECURITY.md) | ❌ No | GitHub repos have no SECURITY.md |

### Tier 3: Registry-Specific (Code-Hosting)

| Check | Status | Notes |
|-------|--------|-------|
| 2FA required for publishers | ❌ No evidence | Uses GitHub OAuth but no documented 2FA requirement |
| Malware scanning | ❌ No evidence | "security scan" field exists but appears unused |
| Namespace policies | ✅ Yes | `owner/repo-name` format enforced |
| Typosquatting protection | ❌ No evidence | No documented detection |
| API security | ⚠️ Partial | OAuth 2.1 + PKCE documented for MCP auth |
| Response time SLA | ⚠️ Good | 48-hour fix for critical vuln (June 2025) |

### Security Incidents

**June 2025 - Path Traversal Vulnerability (Critical)**
- GitGuardian discovered path traversal in `dockerBuildPath` parameter
- Exposed 3,000+ servers and thousands of API keys
- Disclosed June 13, fixed June 15 (48 hours)
- No evidence of exploitation before patch
- Source: [GitGuardian Blog](https://blog.gitguardian.com/breaking-mcp-server-hosting/)

**Secret Leaks Analysis (2025)**
- GitGuardian scanned 3,829 Smithery-indexed repos
- 202 repos (5.2%) leaked at least one secret
- Slightly above baseline (4.6% for all public repos)
- Source: [GitGuardian Research](https://blog.gitguardian.com/a-look-into-the-secrets-of-mcp/)

### Security Score Summary

**Strengths:**
- Verified GitHub organization
- Namespace structure prevents some squatting
- Fast incident response (48-hour critical fix)
- OAuth 2.1 + PKCE for MCP auth
- Public registry API

**Weaknesses:**
- No documented verification criteria for "verified" badge
- No SECURITY.md or vulnerability disclosure policy
- No visible malware scanning
- No report button for problematic servers
- 285 open GitHub issues with limited engagement
- No 2FA requirement documented for publishers
- Does not list vendor-hosted MCP servers

**Overall Assessment:** Moderate security posture. Good infrastructure and fast incident response, but lacks transparency on verification process, no security policy, and limited publisher security requirements. The June 2025 incident shows supply chain risks in centralized MCP hosting.

## Notes

**Legal Entity:** Clavia, Inc. (DBA Smithery), United States

**Business Model:** Free to use, signup at /signup

**Key Links:**
- Documentation: https://smithery.ai/docs
- Privacy Policy: https://smithery.ai/privacy
- Status Page: https://smithery.instatus.com
- Discord: discord.gg/sKd9uycgH9
- GitHub: https://github.com/smithery-ai

**Integration:** Used by Cursor, Claude Desktop, and other MCP clients as primary registry.

**Data Collection:** Per privacy policy, collects keystroke activity, mouse movements, browsing behavior via third-party tracking. Shares data with affiliates, marketing providers, ad networks.
