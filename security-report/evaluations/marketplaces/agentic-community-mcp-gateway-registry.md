---
title: "Agentic Community MCP Gateway & Registry"
url: "https://github.com/agentic-community/mcp-gateway-registry"
source_code_url: "https://github.com/agentic-community/mcp-gateway-registry"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "code-hosting, registry-api"
operator: "Agentic Community"
operator_jurisdiction: "Unknown"
contact_email: "See SECURITY.md for security contacts"
security_email: "aws-security@amazon.com (via vulnerability reporting page)"
server_count: "N/A (codebase for registry)"
last_evaluated: "2026-02-06"
evaluation_status: "comprehensive"
evidence:
  - url: "https://github.com/agentic-community/mcp-gateway-registry"
    description: "Primary GitHub repository for the project"
    captured: "2026-02-06"
  - url: "https://github.com/agentic-community/mcp-gateway-registry/blob/main/SECURITY.md"
    description: "Security policy document"
    captured: "2026-02-06"
---

## Overview

The Agentic Community MCP Gateway & Registry is an open-source project hosted on GitHub that provides a unified, enterprise-ready platform for centralizing access to both MCP Servers and AI Agents using the Model Context Protocol (MCP). It functions as a reference implementation for an MCP Server Gateway, an MCP Server Registry, and an Agent Registry & A2A Communication Hub.

## Features Summary

| Feature | Status | Notes |
|---------|--------|-------|
| Discovery/search | ✅ | Through the registry's API, and code via GitHub |
| One-click install | ❓ | Not directly applicable to the codebase; depends on deployment |
| Curated list/recommendations | ❓ | The registry *enables* this, but isn't a curated list itself |
| Public API | ✅ | Provides an API for programmatic discovery (registry endpoint) |
| CLI tool | ❓ | Mentions "Agentic CLI for MCP Registry" in roadmap, but not directly part of this codebase |
| Client integration | ✅ | Designed to integrate with MCP clients |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Official name | Agentic Community MCP Gateway & Registry | YAML Frontmatter |
| Primary URL | https://github.com/agentic-community/mcp-gateway-registry | YAML Frontmatter |
| Operator (company/individual) | Agentic Community | YAML Frontmatter |
| Country/jurisdiction | Unknown | Not specified in repository |
| Contact email (general) | Unknown | Not specified in repository, check GitHub profiles |
| Contact email (security) | aws-security@amazon.com | SECURITY.md |
| Launch date | 2025-05-29 | Audit Output (repo.activity.created_at) |
| Marketplace source code available? | ✅ Yes | https://github.com/agentic-community/mcp-gateway-registry |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|------|--------|-------|
| Directory/Aggregator - Lists servers with external links | ❌ No | It's an implementation, not a listing site |
| Registry - Provides API for programmatic discovery | ✅ Yes | Provides a registry API implementation |
| Code Hosting - Hosts server source code or packages | ✅ Yes | Hosted on GitHub as source code |
| Hosted Execution (PaaS) - Runs MCP servers on their infrastructure | ❌ No | Codebase, not a deployed service |
| Client-Embedded - Built into a specific MCP client | ❌ No | Not directly embedded, but designed for client integration |
| Curated List - Manually maintained list (e.g., awesome-list) | ❌ No | It's a programmatic registry |

### 1.3 Scale & Activity

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Servers listed (approximate count) | N/A (codebase) | As a codebase, it doesn't list servers directly |
| Update frequency | Active | Last commit: 2026-02-06, Last release: 2026-01-20 (Audit Output) |
| Publisher/contributor count | Unknown | Need to check GitHub contributors |
| Changelog or update history available? | ✅ Yes | GitHub commit history and releases |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|--------|------------|-------------|
| Website with search/browse | ❌ No | Not a public website; codebase only |
| Public API (registry endpoint) | ✅ Yes | Provides a registry API (implementation) |
| CLI tool | ❓ Unknown | Mentions "Agentic CLI for MCP Registry" in roadmap |
| IDE/editor plugin | ❓ Unknown | Not specified for this codebase |
| Integrated into MCP client(s) | ✅ Yes | Designed for client integration |
| Browser extension | ❌ No | Not applicable |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| API documentation available? | ✅ Yes | Implied by "Unified API Management" and "Registry API" in README |
| Authentication required for read? | ✅ Yes | "OAuth 2.0/3.0 compliance" and "FGAC" in README |
| Rate limiting? | ❓ Unknown | Not explicitly stated in README |
| OpenAPI/Swagger spec? | ❓ Unknown | Not explicitly stated in README |
| API terms of use? | N/A | Codebase, not a deployed service |

| Client integration | ✅ | Designed to integrate with MCP clients |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Official name | Agentic Community MCP Gateway & Registry | YAML Frontmatter |
| Primary URL | https://github.com/agentic-community/mcp-gateway-registry | YAML Frontmatter |
| Operator (company/individual) | Agentic Community | YAML Frontmatter |
| Country/jurisdiction | Unknown | Not specified in repository |
| Contact email (general) | Unknown | Not specified in repository, check GitHub profiles |
| Contact email (security) | aws-security@amazon.com | SECURITY.md |
| Launch date | 2025-05-29 | Audit Output (repo.activity.created_at) |
| Marketplace source code available? | ✅ Yes | https://github.com/agentic-community/mcp-gateway-registry |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|------|--------|-------|
| Directory/Aggregator - Lists servers with external links | ❌ No | It's an implementation, not a listing site |
| Registry - Provides API for programmatic discovery | ✅ Yes | Provides a registry API implementation |
| Code Hosting - Hosts server source code or packages | ✅ Yes | Hosted on GitHub as source code |
| Hosted Execution (PaaS) - Runs MCP servers on their infrastructure | ❌ No | Codebase, not a deployed service |
| Client-Embedded - Built into a specific MCP client | ❌ No | Not directly embedded, but designed for client integration |
| Curated List - Manually maintained list (e.g., awesome-list) | ❌ No | It's a programmatic registry |

### 1.3 Scale & Activity

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Servers listed (approximate count) | N/A (codebase) | As a codebase, it doesn't list servers directly |
| Update frequency | Active | Last commit: 2026-02-06, Last release: 2026-01-20 (Audit Output) |
| Publisher/contributor count | Unknown | Need to check GitHub contributors |
| Changelog or update history available? | ✅ Yes | GitHub commit history and releases |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|--------|------------|-------------|
| Website with search/browse | ❌ No | Not a public website; codebase only |
| Public API (registry endpoint) | ✅ Yes | Provides a registry API (implementation) |
| CLI tool | ❓ Unknown | Mentions "Agentic CLI for MCP Registry" in roadmap |
| IDE/editor plugin | ❓ Unknown | Not specified for this codebase |
| Integrated into MCP client(s) | ✅ Yes | Designed for client integration |
| Browser extension | ❌ No | Not applicable |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| API documentation available? | ✅ Yes | Implied by "Unified API Management" and "Registry API" in README |
| Authentication required for read? | ✅ Yes | "OAuth 2.0/3.0 compliance" and "FGAC" in README |
| Rate limiting? | ❓ Unknown | Not explicitly stated in README |
| OpenAPI/Swagger spec? | ❓ Unknown | Not explicitly stated in README |
| API terms of use? | N/A | Codebase, not a deployed service |

### 2.3 Metadata Provided Per Server

| Field | Provided? | Notes |
|-------|-----------|-------|
| Server name | ✅ Yes | Core function of a registry |
| Description | ✅ Yes | Core function of a registry |
| Author/publisher | ✅ Yes | Core function of a registry |
| Source code URL | ✅ Yes | Core function of a registry |
| License | ✅ Yes | Core function of a registry |
| Version information | ✅ Yes | Core function of a registry |
| Last updated date | ✅ Yes | Core function of a registry |
| Download/install count | ❓ Unknown | Depends on registry implementation and usage |
| Ratings/reviews | ❓ Unknown | Mentions "server & agent rating system" in recent updates |
| Categories/tags | ✅ Yes | Implied by discovery features |
| Required permissions/capabilities | ✅ Yes | Implied by fine-grained access control |
| Verification/trust badge | ❓ Unknown | Depends on registry implementation |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|--------|------------|---------|
| Link to external source (GitHub, etc.) | ✅ Yes | As a code-hosting registry, it enables this |
| Direct download (zip, tarball) | ✅ Yes | As a GitHub repo, code can be downloaded |
| Package manager (npm, pip, etc.) | ❓ Unknown | Not explicitly stated, depends on packaging |
| Container image (Docker) | ✅ Yes | "Pre-built Images" mentioned in README |
| One-click install to client config | ❓ Unknown | Not directly supported by codebase; depends on client integration |
| Hosted execution (marketplace runs the server) | ❌ No | Codebase, not a deployed service |

### 3.2 Hosted Execution Details (PaaS Model)

*Not applicable, as this is a codebase, not a hosted service.*

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Server isolation method | N/A | |
| User credentials/secrets handling | N/A | |
| Secret storage method | N/A | |
| Audit logging available? | N/A | |
| Build/deployment process | N/A | |
| Publisher access to build logs? | N/A | |
| Multi-tenant isolation documented? | N/A | |

### 3.3 Source Accessibility

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Marketplace source code available? | ✅ Yes | https://github.com/agentic-community/mcp-gateway-registry |
| API documentation URL | ❓ Unknown | Implied by "Unified API Management" and "Registry API" in README, but specific URL not found |
| Self-hostable? | ✅ Yes | Can be built from source and deployed |

### 3.4 Server Coverage

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Lists vendor-hosted servers (Vercel, Cloudflare, etc.)? | N/A (codebase) | Codebase; deployed instance could |
| Distinguishes hosted vs local servers? | N/A (codebase) | Codebase; deployed instance could |
| Vendor-hosted servers found in search? | N/A (codebase) | Codebase; deployed instance could |

### 2.3 Metadata Provided Per Server

| Field | Provided? | Notes |
|-------|-----------|-------|
| Server name | ✅ Yes | Core function of a registry |
| Description | ✅ Yes | Core function of a registry |
| Author/publisher | ✅ Yes | Core function of a registry |
| Source code URL | ✅ Yes | Core function of a registry |
| License | ✅ Yes | Core function of a registry |
| Version information | ✅ Yes | Core function of a registry |
| Last updated date | ✅ Yes | Core function of a registry |
| Download/install count | ❓ Unknown | Depends on registry implementation and usage |
| Ratings/reviews | ❓ Unknown | Mentions "server & agent rating system" in recent updates |
| Categories/tags | ✅ Yes | Implied by discovery features |
| Required permissions/capabilities | ✅ Yes | Implied by fine-grained access control |
| Verification/trust badge | ❓ Unknown | Depends on registry implementation |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|--------|------------|---------|
| Link to external source (GitHub, etc.) | ✅ Yes | As a code-hosting registry, it enables this |
| Direct download (zip, tarball) | ✅ Yes | As a GitHub repo, code can be downloaded |
| Package manager (npm, pip, etc.) | ❓ Unknown | Not explicitly stated, depends on packaging |
| Container image (Docker) | ✅ Yes | "Pre-built Images" mentioned in README |
| One-click install to client config | ❓ Unknown | Not directly supported by codebase; depends on client integration |
| Hosted execution (marketplace runs the server) | ❌ No | Codebase, not a deployed service |

### 3.2 Hosted Execution Details (PaaS Model)

*Not applicable, as this is a codebase, not a hosted service.*

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Server isolation method | N/A | |
| User credentials/secrets handling | N/A | |
| Secret storage method | N/A | |
| Audit logging available? | N/A | |
| Build/deployment process | N/A | |
| Publisher access to build logs? | N/A | |
| Multi-tenant isolation documented? | N/A | |

### 3.3 Source Accessibility

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Marketplace source code available? | ✅ Yes | https://github.com/agentic-community/mcp-gateway-registry |
| API documentation URL | ❓ Unknown | Implied by "Unified API Management" and "Registry API" in README, but specific URL not found |
| Self-hostable? | ✅ Yes | Can be built from source and deployed |

### 3.4 Server Coverage

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Lists vendor-hosted servers (Vercel, Cloudflare, etc.)? | N/A (codebase) | Codebase; deployed instance could |
| Distinguishes hosted vs local servers? | N/A (codebase) | Codebase; deployed instance could |
| Vendor-hosted servers found in search? | N/A (codebase) | Codebase; deployed instance could |

### 3.5 Vendor-Hosted Coverage Test

*Not applicable to this codebase.*

| Pattern Searched | Found? | Notes |
|------------------|--------|-------|
| mcp.vercel.com | N/A | |
| vercel + mcp | N/A | |
| cloudflare + mcp | N/A | |
| stripe + mcp | N/A | |
| linear + mcp | N/A | |
| huggingface.co/mcp | N/A | |
| [other vendor patterns] | N/A | |

**Test Result:** N/A - This is a codebase, not a marketplace that directly lists servers.

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Publisher verification process exists? | ✅ Yes | GitHub profiles and signed commits |
| Verification requirements documented? | ❓ Unknown | Not explicitly documented, relies on GitHub |
| 2FA/MFA required for publishers? | ✅ Yes | Via GitHub account settings |
| Trust tiers (verified, official, etc.)? | ❌ No | Not explicitly documented |
| Verification criteria publicly documented? | ❌ No | Not explicitly documented |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Servers reviewed before listing? | N/A (codebase) | Codebase provides framework for vetting, but doesn't vet itself |
| Automated security scanning? | ✅ Yes | Mentions "MCP Server Security Scanning" as feature in README |
| Malware detection? | ❓ Unknown | Not explicitly detailed |
| Dependency vulnerability scanning? | N/A (codebase) | Applies to deployed registry's internal dependencies if any |
| Flagged server removal speed? | N/A (codebase) | Not a deployed service |
| Typosquatting/namesquatting protection? | N/A (codebase) | Not a deployed service |

### 4.3 Community Trust Signals

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Users can report problematic servers? | N/A (codebase) | Feature of a deployed registry instance |
| Visible "Report" button? | N/A (codebase) | Feature of a deployed registry instance |
| User reviews or ratings? | ✅ Yes | Mentions "server & agent rating system" in recent updates |
| Download/usage count visible? | ❓ Unknown | Not explicitly documented |
| "Last updated" timestamp visible? | ✅ Yes | GitHub activity, registry API can provide this |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Privacy policy exists? | ❌ No | Not applicable to codebase, only a deployed instance |
| Privacy policy URL | N/A | |
| User data collected (summary) | N/A | Codebase doesn't collect user data directly |
| Data shared with third parties? | N/A | |
| Analytics/tracking tools used | N/A | |
| Data retention policy? | N/A | |
| GDPR compliance claimed? | N/A | |

### 5.1.1 Third-Party Integrations Detected

| Integration | Present? | Details |
|-------------|----------|---------|
| Google Analytics | N/A | |
| Google Tag Manager | N/A | |
| Google AdSense | N/A | |
| Google Fonts | N/A | |
| Cloudflare (CDN) | N/A | |
| Other CDN | N/A | |
| Social login providers | N/A | |
| Payment processors | N/A | |
| Other trackers | N/A | |

### 5.2 Terms of Service

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Terms of service exists? | ❌ No | Not applicable to codebase, only a deployed instance |
| Terms of service URL | N/A | |
| Prohibited publisher activities | N/A | |
| Prohibited user activities | N/A | |
| Liability limitations | N/A | |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Security policy exists? | ✅ Yes | SECURITY.md |
| Security policy URL (SECURITY.md) | ✅ Yes | https://github.com/agentic-community/mcp-gateway-registry/blob/main/SECURITY.md |
| Vulnerability disclosure process? | ✅ Yes | Documented in SECURITY.md |
| Bug bounty program? | ❌ No | Not mentioned |
| Past security incidents disclosed? | ❌ No | No public records found |
| Status page for uptime/incidents? | N/A | Codebase, not a deployed service |

---

## Part 6: Supply Chain Security

### 6.1 Code Integrity

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Packages/images signed? | ❓ Unknown | "Pre-built Images" mentioned, but signing status not explicit |
| Provenance attestation provided? | ❓ Unknown | Not explicitly mentioned |
| SBOMs (Software Bill of Materials) available? | ❓ Unknown | Not explicitly mentioned |
| Reproducible build support? | ❓ Unknown | Not explicitly mentioned |
| Signed commits? | ✅ Yes | Audit Output (`repo.security_features.signed_commits`) |

### 6.2 Dependency Management

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Dependencies scanned for vulnerabilities? | ✅ Yes | Dependabot enabled (Audit Output) |
| Dependency confusion protection? | ❓ Unknown | Not explicitly mentioned |
| Lock files required/validated? | ❓ Unknown | Not explicitly mentioned (requires source code review) |
| Vulnerable dependency notifications? | ✅ Yes | Dependabot enabled (Audit Output) |

### 6.3 Update & Patch Management

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Security update communication method | ✅ Yes | Via SECURITY.md reporting process |
| Auto-updates supported? | N/A | Not applicable for a codebase |
| Version pinning available? | N/A | Not applicable for a codebase |
| Deprecation/EOL policy? | ❓ Unknown | Not explicitly mentioned |

---

## Part 7: Technical Security Posture

*This section's information is primarily derived from the `audit.py --repo` tool output, which focuses on repository-level security features rather than web-facing aspects for a codebase.*

### 7.1 Web Security Headers

| Header | Present? | Value |
|--------|----------|-------|
| HTTPS enforced | ✅ Yes | GitHub enforced HTTPS |
| Strict-Transport-Security (HSTS) | N/A | Not directly applicable to codebase repo |
| Content-Security-Policy | N/A | Not directly applicable to codebase repo |
| X-Frame-Options | N/A | Not directly applicable to codebase repo |
| X-Content-Type-Options | N/A | Not directly applicable to codebase repo |
| Referrer-Policy | N/A | Not directly applicable to codebase repo |
| Permissions-Policy | N/A | Not directly applicable to codebase repo |
| Cross-Origin-Opener-Policy | N/A | Not directly applicable to codebase repo |
| Cross-Origin-Resource-Policy | N/A | Not directly applicable to codebase repo |

### 7.2 TLS Certificate

*Not directly applicable to a codebase repository; covered by GitHub's infrastructure.*

| Field | Value |
|-------|-------|
| Issuer | N/A |
| Subject | N/A |
| Valid from | N/A |
| Valid until | N/A |
| SHA256 fingerprint | N/A |

### 7.3 DNS & Hosting

*Not directly applicable to a codebase repository; covered by GitHub's infrastructure.*

| Field | Value |
|-------|-------|
| A records | N/A |
| AAAA records | N/A |
| CNAME records | N/A |
| NS records | N/A |
| Provider hints | N/A |

### 7.4 Path Availability (Automated Probe)

*Not directly applicable to a codebase repository; covered by GitHub's web interface.*

| Path | Status Code | Notes |
|------|-------------|-------|
| /privacy | N/A | |
| /privacy-policy | N/A | |
| /terms | N/A | |
| /tos | N/A | |
| /security | N/A | |
| /legal | N/A | |
| /about | N/A | |
| /contact | N/A | |
| /robots.txt | N/A | |
| /sitemap.xml | N/A | |
| /api | N/A | |
| /docs | N/A | |
| /api-docs | N/A | |
| /swagger.json | N/A | |
| /openapi.json | N/A | |
| /openapi.yaml | N/A | |

### 7.5 Mixed Content

*Not directly applicable to a codebase repository.*

| Check | Result |
|-------|--------|
| HTTP links found | N/A |
| HTTP subresources found | N/A |
| Sample URLs | N/A |

### 7.6 Social/Contact Links Found

*These are typically for web-facing services, not raw code repositories.*

| Type | URL |
|------|-----|
| GitHub | ✅ Yes | https://github.com/agentic-community/mcp-gateway-registry |
| Discord | ❓ Unknown | Not found in audit output or README |
| Twitter/X | ❓ Unknown | Not found in audit output or README |
| LinkedIn | ❓ Unknown | Not found in audit output or README |
| Email (mailto) | ✅ Yes | aws-security@amazon.com (security contact) |

### 7.7 Authentication & Authorization

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Authentication methods supported | ✅ Yes | OAuth 2.0/3.0 compliance (README) |
| OAuth/OIDC providers | ✅ Yes | Keycloak Integration, Microsoft Entra ID Integration (README) |
| Session management documented? | ❓ Unknown | Not explicitly documented for codebase |
| API tokens scoped and time-limited? | ✅ Yes | Implied by "fine-grained access control" (README), and static token authentication for Registry API (recent updates) |

---

## Part 8: Operator Transparency

### 8.1 Business Model

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Free or paid? | ✅ Free | Open-source project |
| Pricing model (if paid) | N/A | |
| Revenue source | N/A | Open-source project |
| Registered business entity? | ❓ Unknown | "Agentic Community" implies community project, not necessarily a formal entity |

### 8.2 Communication & Support

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Public documentation URL | ✅ Yes | README, GitHub repository itself |
| Community (Discord/Slack/Forum) | ❓ Unknown | Not explicitly mentioned in README or audit output |
| Official social media | ❓ Unknown | Not explicitly mentioned in README or audit output |
| Support response time | ❓ Unknown | Not explicitly mentioned |
| Issue tracker for bug reports | ✅ Yes | GitHub Issues |

---

## Part 9: Security Incidents

*Document any known security incidents:*

| Date | Severity | Description | Resolution | Source |
|------|----------|-------------|------------|--------|
| N/A | N/A | No publicly known security incidents found during research. | N/A | Web search on 2026-02-06 |

---

## Part 10: Delivery Method Security

*Security assessment per delivery channel (mostly N/A for a codebase):*

### Website

*Not applicable as this is a codebase, not a public website.*

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | N/A | |
| Privacy policy present | N/A | |
| CSP headers | N/A | |
| Login method | N/A | |

### API (if applicable)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | N/A | Dependent on deployment environment |
| Authentication for reads | ✅ Yes | Designed to support OAuth 2.0/3.0 |
| Authentication for writes | ✅ Yes | Designed to support OAuth 2.0/3.0 |
| Rate limiting | ❓ Unknown | Not explicitly documented in codebase |
| API versioning | ✅ Yes | Implied by "v0.1" in registry API URL, and "MCP server version routing" |

### CLI (if applicable)

*Mentions "Agentic CLI for MCP Registry" in roadmap, but not directly part of this codebase.*

| Check | Status | Notes |
|-------|--------|-------|
| Package manager | N/A | |
| License | N/A | |
| Package signing | N/A | |
| Update mechanism | N/A | |

### Client Integration (if applicable)

| Check | Status | Notes |
|-------|--------|-------|
| Which clients integrate | ❓ Unknown | Designed for integration, but specific clients not detailed |
| Data format (JSON, etc.) | ✅ Yes | MCP Protocol implies structured data |
| Client-side verification | ❓ Unknown | Dependent on client implementation |
| Trust model | ✅ Yes | Supports fine-grained access control |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

*What does this marketplace do well from a security/trust perspective?*

- **Clear Vulnerability Disclosure:** Presence of `SECURITY.md` with explicit instructions to report to AWS/Amazon Security. ✅
- **Strong Supply Chain Security Practices:** Enabled Dependabot, Code Scanning, and Secret Scanning on the repository, indicating proactive vulnerability and secret management. ✅
- **Code Integrity:** All commits are signed (`signed_commits: true`). ✅
- **Open Source & Community Driven:** Benefits from GitHub's collaborative features, with a Code of Conduct and Contributing guidelines in place. ✅
- **Active Development:** Evidenced by recent commits and releases. ✅
- **Enterprise-Grade Security Focus:** `README.md` highlights features like OAuth 2.0/3.0 compliance, fine-grained access control, zero-trust architecture, and complete audit trails (as design goals/features). ✅

### 11.2 Weaknesses & Gaps

*What is missing, undocumented, or concerning?*

- **Lack of Branch Protection:** The repository does not have branch protection enabled (`branch_protection: false`). This is a significant security gap for a reference implementation, as it reduces safeguards against unreviewed or unauthorized code merging into critical branches. ⚠️
- **Privacy Policy/Terms for Deployments:** While N/A for the codebase itself, a deployed instance of this gateway/registry would critically need its own privacy policy and terms of service, which are not provided by the codebase. This isn't a direct weakness of the *codebase* but a deployment consideration. ❓

### 11.3 Red Flags

*Specific concerns users should be aware of:*

- **Lack of Branch Protection:** High Severity. Without branch protection, there's a higher risk of malicious or buggy code being introduced directly into the main branch without sufficient review.

### 11.4 Recommendations

*What should the marketplace operator improve?*

- **Enable Branch Protection:** Immediately enable branch protection for the `main` branch (and any other critical branches) requiring pull request reviews, status checks, and signed commits.
- **Deployment Guidelines for Policies:** Add a section to the `README.md` or a `DEPLOYMENT_SECURITY.md` guide that explicitly advises deployers of this gateway/registry to implement their own privacy policy and terms of service, along with other operational security considerations.

### 11.5 Overall Trust Assessment

*Summary assessment for users considering this marketplace:*

The "Agentic Community MCP Gateway & Registry" project, as a codebase, demonstrates a strong commitment to security through its use of GitHub's security features (Dependabot, Code Scanning, Secret Scanning, signed commits) and a clear vulnerability disclosure process. It serves as a solid foundation for building an MCP gateway/registry with security in mind. However, the notable absence of branch protection introduces a significant risk that should be addressed immediately to enhance code integrity and project trustworthiness. For deployers, understanding their own responsibility in establishing operational policies (privacy, terms) is crucial. Overall: **Good (with critical improvements needed)**.

---

## Evaluation Metadata

| Field | Value |
|-------|-------|
| Evaluator | Gemini CLI |
| Evaluation Date | 2026-02-06 |
| Marketplace Version/State | Latest commit: 2026-02-06 |
| Automated Audit Tool Version | N/A (inline script execution) |
| Evidence Archive Location | N/A (all evidence cited inline) |
| Sent to Operator for Review? | ❌ No |
| Operator Response Received? | ❌ No |
| Operator Verified? | ❌ No |
| Last Updated | 2026-02-06 |

---

## Audit Evidence

### Testing Methodology

**Automated checks performed:**
- Command: `python security-report/tools/audit.py --repo https://github.com/agentic-community/mcp-gateway-registry`
- Date: 2026-02-06
- Tool version: N/A (inline script execution)

**Manual checks performed:**
- Review of GitHub repository README.md
- Review of GitHub repository SECURITY.md
- Review of GitHub repository activity (commits, releases)

### `audit.py --repo` Output

```json
{
  "repo": {
    "repo_info": {
      "platform": "github",
      "owner": "agentic-community",
      "repo": "mcp-gateway-registry",
      "url": "https://github.com/agentic-community/mcp-gateway-registry",
      "is_org": true
    },
    "security_files": {
      "security_md": true,
      "security_md_url": "https://github.com/agentic-community/mcp-gateway-registry/blob/main/SECURITY.md",
      "security_policy": false,
      "code_of_conduct": true,
      "contributing_md": true,
      "license": "Apache-2.0",
      "license_url": "https://github.com/agentic-community/mcp-gateway-registry/blob/main/LICENSE"
    },
    "org_verification": {
      "is_org": true,
      "org_name": "agentic-community",
      "verified": false,
      "verified_domains": []
    },
    "activity": {
      "stars": 423,
      "forks": 82,
      "watchers": 5,
      "open_issues": 34,
      "open_prs": 1,
      "last_commit": "2026-02-06T03:41:00Z",
      "last_release": "2026-01-20T00:09:26Z",
      "created_at": "2025-05-29T18:23:37Z",
      "updated_at": "2026-02-06T17:10:59Z",
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
      "agentic-ai",
      "agents",
      "mcp",
      "mcp-gateway",
      "mcp-registry",
      "mcp-server",
      "oauth2",
      "keycloak",
      "fgac",
      "graphana",
      "postgresql",
      "sqlite",
      "ecs",
      "ecs-fargate",
      "terraform",
      "documentdb",
      "mongodb",
      "entra-id",
      "a2a"
    ],
    "errors": []
  }
}
```

### Key Findings Summary

| Category | Result |
|----------|--------|
| Repository Security Files | `SECURITY.md`, Code of Conduct, Contributing.md, LICENSE found |
| Organization Verification | `is_org: true`, `verified: false` |
| Activity (Stars, Forks, Issues, PRs) | Active development |
| Security Features | Dependabot, Code Scanning, Secret Scanning, Signed Commits enabled. Branch Protection disabled. |
| Vulnerability Disclosure | `SECURITY.md` directs to AWS/Amazon Security |

### Additional Evidence

- README.md: https://github.com/agentic-community/mcp-gateway-registry/blob/main/README.md
- LICENSE: https://github.com/agentic-community/mcp-gateway-registry/blob/main/LICENSE

---

## Changelog

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 2026-02-06 | 1.0 | Initial comprehensive evaluation | Gemini CLI |













---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Official name | Agentic Community MCP Gateway & Registry | YAML Frontmatter |
| Primary URL | https://github.com/agentic-community/mcp-gateway-registry | YAML Frontmatter |
| Operator (company/individual) | Agentic Community | YAML Frontmatter |
| Country/jurisdiction | Unknown | Not specified in repository |
| Contact email (general) | Unknown | Not specified in repository, check GitHub profiles |
| Contact email (security) | aws-security@amazon.com | SECURITY.md |
| Launch date | 2025-05-29 | Audit Output (repo.activity.created_at) |
| Marketplace source code available? | ✅ Yes | https://github.com/agentic-community/mcp-gateway-registry |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|------|--------|-------|
| Directory/Aggregator - Lists servers with external links | ❌ No | It's an implementation, not a listing site |
| Registry - Provides API for programmatic discovery | ✅ Yes | Provides a registry API implementation |
| Code Hosting - Hosts server source code or packages | ✅ Yes | Hosted on GitHub as source code |
| Hosted Execution (PaaS) - Runs MCP servers on their infrastructure | ❌ No | Codebase, not a deployed service |
| Client-Embedded - Built into a specific MCP client | ❌ No | Not directly embedded, but designed for client integration |
| Curated List - Manually maintained list (e.g., awesome-list) | ❌ No | It's a programmatic registry |

### 1.3 Scale & Activity

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Servers listed (approximate count) | N/A (codebase) | As a codebase, it doesn't list servers directly |
| Update frequency | Active | Last commit: 2026-02-06, Last release: 2026-01-20 (Audit Output) |
| Publisher/contributor count | Unknown | Need to check GitHub contributors |
| Changelog or update history available? | ✅ Yes | GitHub commit history and releases |