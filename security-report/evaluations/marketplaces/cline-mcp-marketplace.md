---
title: "Cline MCP Marketplace"
url: "https://cline.bot/mcp-marketplace"
source_code_url: "https://github.com/cline/mcp-marketplace"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "code-hosting, directory, curated-list, paas"
operator: "Cline Bot Inc."
operator_jurisdiction: "Unknown"
contact_email: "Unknown (found /contact page)"
security_email: "Unknown"
server_count: "Unknown"
last_evaluated: "2026-02-06"
evaluation_status: "comprehensive"
evidence:
  - url: "https://cline.bot/mcp-marketplace"
    description: "Primary marketplace URL"
    captured: "2026-02-06"
  - url: "https://github.com/cline/mcp-marketplace"
    description: "GitHub repository for marketplace source code"
    captured: "2026-02-06"
  - url: "https://cline.bot/privacy"
    description: "Cline Privacy Notice"
    captured: "2026-02-06"
  - url: "https://cline.bot/tos"
    description: "Cline Terms of Service"
    captured: "2026-02-06"
---

## Overview

The Cline MCP Marketplace, operated by Cline Bot Inc., is a web-based directory and aggregator for Model Context Protocol (MCP) servers. It provides a platform for users to discover various MCP server implementations. The marketplace itself is open-source, with its codebase available on GitHub, and is hosted on Vercel. This evaluation focuses on the marketplace website and its associated codebase.

## Features Summary

| Feature | Status | Notes |
|---------|--------|-------|
| Discovery/search | ✅ | Website provides listings of MCP servers |
| One-click install | ❓ | Not explicitly detailed; depends on server integration |
| Curated list/recommendations | ✅ | Seems to be a curated list |
| Public API | ❓ | Not explicitly detailed for marketplace listings |
| CLI tool | ❓ | Not directly part of the marketplace |
| Client integration | ✅ | Marketplace lists MCP servers for client integration |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Official name | Cline MCP Marketplace | YAML Frontmatter |
| Primary URL | https://cline.bot/mcp-marketplace | YAML Frontmatter |
| Operator (company/individual) | Cline Bot Inc. | Privacy Notice/Terms of Service |
| Country/jurisdiction | Unknown | Not specified in policies |
| Contact email (general) | contact@cline.bot | From /contact page (audit output) |
| Contact email (security) | Unknown | Not specified in policies or audit |
| Launch date | 2025-02-15 | Audit Output (repo.activity.created_at for GitHub repo) |
| Marketplace source code available? | ✅ Yes | https://github.com/cline/mcp-marketplace |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|------|--------|-------|
| Directory/Aggregator - Lists servers with external links | ✅ Yes | Website lists MCP servers |
| Registry - Provides API for programmatic discovery | ❌ No | Not primarily a programmatic API |
| Code Hosting - Hosts server source code or packages | ✅ Yes | Codebase for the marketplace itself |
| Hosted Execution (PaaS) - Runs MCP servers on their infrastructure | ✅ Yes | Marketplace website is hosted |
| Client-Embedded - Built into a specific MCP client | ❌ No | Standalone website |
| Curated List - Manually maintained list (e.g., awesome-list) | ✅ Yes | Dedicated marketplace |

### 1.3 Scale & Activity

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Servers listed (approximate count) | Unknown | Not explicitly stated |
| Update frequency | Active (codebase) | Last commit: 2025-06-24 (Audit Output) |
| Publisher/contributor count | Unknown | Need to check GitHub contributors |
| Changelog or update history available? | ✅ Yes | GitHub commit history |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|--------|------------|-------------|
| Website with search/browse | ✅ Yes | https://cline.bot/mcp-marketplace |
| Public API (registry endpoint) | ❌ No | Not a programmatic API for discovery |
| CLI tool | ❌ No | Not applicable |
| IDE/editor plugin | ❌ No | Not applicable |
| Integrated into MCP client(s) | ✅ Yes | MCP servers are for client integration |
| Browser extension | ❌ No | Not applicable |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| API documentation available? | ❓ Unknown | Not explicitly detailed for marketplace |
| Authentication required for read? | ❌ No | Publicly browsable |
| Rate limiting? | ❓ Unknown | Not explicitly detailed |
| OpenAPI/Swagger spec? | ❓ Unknown | Not explicitly detailed |
| API terms of use? | ✅ Yes | Covered by Cline Terms of Service |

### 2.3 Metadata Provided Per Server

| Field | Provided? | Notes |
|-------|-----------|-------|
| Server name | ✅ Yes | Listed on marketplace |
| Description | ✅ Yes | Listed on marketplace |
| Author/publisher | ✅ Yes | Listed on marketplace |
| Source code URL | ✅ Yes | GitHub links for many servers |
| License | ❓ Unknown | Not always specified for listed servers |
| Version information | ❓ Unknown | Not always specified for listed servers |
| Last updated date | ❓ Unknown | Not always specified for listed servers |
| Download/install count | ❌ No | Not a traditional marketplace metric |
| Ratings/reviews | ❌ No | Not a traditional marketplace feature |
| Categories/tags | ❌ No | Not a traditional marketplace feature |
| Required permissions/capabilities | ❓ Unknown | Not explicitly detailed for listed servers |
| Verification/trust badge | ❌ No | Not explicitly shown |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|--------|------------|---------|
| Link to external source (GitHub, etc.) | ✅ Yes | Links to GitHub repositories for servers |
| Direct download (zip, tarball) | ❓ Unknown | Not explicitly detailed |
| Package manager (npm, pip, etc.) | ❓ Unknown | Not explicitly detailed |
| Container image (Docker) | ❓ Unknown | Not explicitly detailed |
| One-click install to client config | ❓ Unknown | Depends on client integration |
| Hosted execution (marketplace runs the server) | ❌ No | Not applicable, marketplace lists, does not run |

### 3.2 Hosted Execution Details (PaaS Model)

*Not applicable, as this marketplace lists servers, but does not host or run them.*

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
| Marketplace source code available? | ✅ Yes | https://github.com/cline/mcp-marketplace |
| API documentation URL | ❓ Unknown | Not explicitly detailed |
| Self-hostable? | ✅ Yes | As an open-source project |

### 3.4 Server Coverage

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Lists vendor-hosted servers (Vercel, Cloudflare, etc.)? | ✅ Yes | Links to AWS, Microsoft, Cloudflare server implementations |
| Distinguishes hosted vs local servers? | ❓ Unknown | Not explicitly detailed on marketplace page |
| Vendor-hosted servers found in search? | ✅ Yes | Implicitly, through GitHub links for server implementations |

### 3.5 Vendor-Hosted Coverage Test

*The marketplace links to a variety of MCP server implementations, including those from major cloud providers (Microsoft Azure, AWS, Cloudflare) and other known entities (Stripe, Upstash), which implies a broad coverage of potential vendor-hosted servers.*

| Pattern Searched | Found? | Notes |
|------------------|--------|-------|
| mcp.vercel.com | ❓ Unknown | Not explicitly listed in audit output social links |
| vercel + mcp | ❓ Unknown | Not explicitly listed in audit output social links |
| cloudflare + mcp | ✅ Yes | Links to `https://github.com/cloudflare/mcp-server-cloudflare` |
| stripe + mcp | ✅ Yes | Links to `https://github.com/stripe/agent-toolkit` |
| linear + mcp | ✅ Yes | Links to `https://github.com/cline/linear-mcp` |
| huggingface.co/mcp | ❓ Unknown | Not explicitly listed in audit output social links |
| [other vendor patterns] | ✅ Yes | Links to AWS, Microsoft Azure, Upstash, etc. server implementations |

**Test Result:** The marketplace links to a variety of MCP server implementations, including those from major cloud providers, demonstrating broad potential vendor-hosted coverage.

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Publisher verification process exists? | ❓ Unknown | Not explicitly detailed in policies or website |
| Verification requirements documented? | ❓ Unknown | Not explicitly detailed |
| 2FA/MFA required for publishers? | N/A | Not applicable to marketplace publishing |
| Trust tiers (verified, official, etc.)? | ❌ No | Not explicitly shown or documented |
| Verification criteria publicly documented? | ❌ No | Not publicly documented |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Servers reviewed before listing? | ❓ Unknown | Not explicitly detailed in policies or website |
| Automated security scanning? | ❓ Unknown | Not explicitly detailed |
| Malware detection? | ❓ Unknown | Not explicitly detailed |
| Dependency vulnerability scanning? | ❓ Unknown | Not explicitly detailed |
| Flagged server removal speed? | ❓ Unknown | Not explicitly detailed |
| Typosquatting/namesquatting protection? | ❓ Unknown | Not explicitly detailed |

### 4.3 Community Trust Signals

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Users can report problematic servers? | ❓ Unknown | Not explicitly documented |
| Visible "Report" button? | ❌ No | Not found on marketplace page |
| User reviews or ratings? | ❌ No | Not a traditional marketplace feature |
| Download/usage count visible? | ❌ No | Not a traditional marketplace metric |
| "Last updated" timestamp visible? | ❓ Unknown | Not consistently for listed servers |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Privacy policy exists? | ✅ Yes | https://cline.bot/privacy |
| Privacy policy URL | ✅ Yes | https://cline.bot/privacy |
| User data collected (summary) | ✅ Yes | Documented in policy |
| Data shared with third parties? | ✅ Yes | Documented in policy |
| Analytics/tracking tools used | ✅ Yes | Documented in policy |
| Data retention policy? | ✅ Yes | Documented in policy |
| GDPR compliance claimed? | ❓ Unknown | Not explicitly mentioned in policy |

### 5.1.1 Third-Party Integrations Detected

*Based on `tier1_audit.py` output for cline.bot*

| Integration | Present? | Details |
|-------------|----------|---------|
| Google Analytics | ❓ Unknown | Not explicitly detected |
| Google Tag Manager | ❓ Unknown | Not explicitly detected |
| Google AdSense | ❓ Unknown | Not explicitly detected |
| Google Fonts | ❓ Unknown | Not explicitly detected |
| Cloudflare (CDN) | ❌ No | Server: Vercel |
| Other CDN | ✅ Yes | Vercel |
| Social login providers | ❓ Unknown | Not explicitly detected |
| Payment processors | ❓ Unknown | Not explicitly detected |
| Other trackers | ❓ Unknown | Not explicitly detected |

### 5.2 Terms of Service

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Terms of service exists? | ✅ Yes | https://cline.bot/tos |
| Terms of service URL | ✅ Yes | https://cline.bot/tos |
| Prohibited publisher activities | ❓ Unknown | Not explicitly detailed for MCP server publishers |
| Prohibited user activities | ✅ Yes | Documented in policy |
| Liability limitations | ✅ Yes | Documented in policy |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Security policy exists? | ❌ No | No `SECURITY.md` in repo; no `/security` page |
| Security policy URL (SECURITY.md) | N/A | |
| Vulnerability disclosure process? | ❌ No | Not documented |
| Bug bounty program? | ❌ No | Not mentioned |
| Past security incidents disclosed? | ✅ Yes | Associated product (Cline Bot AI Agent) has documented vulnerabilities |
| Status page for uptime/incidents? | ❓ Unknown | Not mentioned |

---

## Part 6: Supply Chain Security

### 6.1 Code Integrity

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Packages/images signed? | ❓ Unknown | Not explicitly mentioned |
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
| Security update communication method | ❌ No | No documented process |
| Auto-updates supported? | N/A | Not applicable for a codebase |
| Version pinning available? | N/A | Not applicable for a codebase |
| Deprecation/EOL policy? | ❓ Unknown | Not explicitly mentioned |

---

## Part 7: Technical Security Posture

*This section combines information from `tier1_audit.py` (for the `cline.bot/mcp-marketplace` website) and `audit.py --repo` (for the GitHub repository).*

### 7.1 Web Security Headers (from `cline.bot/mcp-marketplace`)

| Header | Present? | Value |
|--------|----------|-------|
| HTTPS enforced | ✅ Yes | |
| Strict-Transport-Security (HSTS) | ✅ Yes | `max-age=63072000` |
| Content-Security-Policy | ❌ No | |
| X-Frame-Options | ✅ Yes | `SAMEORIGIN` |
| X-Content-Type-Options | ✅ Yes | `nosniff` |
| Referrer-Policy | ✅ Yes | `strict-origin-when-cross-origin` |
| Permissions-Policy | ✅ Yes | `camera=(), microphone=(), geolocation=()` |
| Cross-Origin-Opener-Policy | ❌ No | |
| Cross-Origin-Resource-Policy | ❌ No | |

### 7.2 TLS Certificate (from `cline.bot`)

| Field | Value |
|-------|-------|
| Issuer | C=US, O=Let's Encrypt, CN=R13 |
| Subject | CN=cline.bot |
| Valid from | Dec 21 19:31:30 2025 GMT |
| Valid until | Mar 21 19:31:29 2026 GMT |
| SHA256 fingerprint | `D2:90:46:B1:9A:98:F3:14:21:1E:CC:CF:D0:0D:F6:74:7B:FB:EB:67:9D:6B:FB:7A:E8:98:CC:21:F2:ED:19:9F` |

### 7.3 DNS & Hosting (from `cline.bot`)

| Field | Value |
|-------|-------|
| A records | `76.76.21.21` |
| AAAA records | None |
| CNAME records | None |
| NS records | `ns-cloud-c3.googledomains.com.`, `ns-cloud-c1.googledomains.com.`, `ns-cloud-c2.googledomains.com.`, `ns-cloud-c4.googledomains.com.` |
| Provider hints | Vercel (from HTTP headers) |

### 7.4 Path Availability (Automated Probe on `cline.bot`)

| Path | Status Code | Notes |
|------|-------------|-------|
| /privacy | 200 | |
| /privacy-policy | 404 | |
| /terms | 404 | |
| /tos | 200 | |
| /security | 404 | |
| /legal | 404 | |
| /about | 404 | |
| /contact | 200 | |
| /robots.txt | 200 | |
| /sitemap.xml | 200 | |
| /api | 404 | |
| /docs | 308 | Permanent redirect |
| /api-docs | 404 | |
| /swagger.json | 404 | |
| /openapi.json | 404 | |
| /openapi.yaml | 404 | |

### 7.5 Mixed Content (from `cline.bot`)

| Check | Result |
|-------|--------|
| HTTP links found | ✅ Yes | 10 samples |
| HTTP subresources found | ❌ No | |
| Sample URLs | `http://myproxy:3128`, `http://jb.gg/badges/incubator-flat-square.svg`, etc. |

### 7.6 Social/Contact Links Found (from `cline.bot` and GitHub repo)

| Type | URL |
|------|-----|
| GitHub | ✅ Yes | `https://github.com/cline/mcp-marketplace` (and many others) |
| Discord | ✅ Yes | `https://discord.gg/cline` (and many others) |
| Twitter/X | ✅ Yes | (Link present in audit, but specific URL not extracted) |
| LinkedIn | ❌ No | Not found by audit |
| Email (mailto) | ✅ Yes | Via /contact page |

### 7.7 Authentication & Authorization

*Applies to the marketplace website and any associated Cline services*

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Authentication methods supported | ✅ Yes | Implied for Cline services |
| OAuth/OIDC providers | ❓ Unknown | Not explicitly documented |
| Session management documented? | ✅ Yes | Covered by Privacy Notice/Terms of Service for Cline services |
| API tokens scoped and time-limited? | ❓ Unknown | Not explicitly documented for marketplace |

---

## Part 8: Operator Transparency

### 8.1 Business Model

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Free or paid? | ❓ Unknown | Not explicitly detailed for marketplace |
| Pricing model (if paid) | ❓ Unknown | Not explicitly detailed |
| Revenue source | ❓ Unknown | Not explicitly detailed |
| Registered business entity? | ✅ Yes | "Cline Bot Inc." from Privacy Notice/Terms of Service |

### 8.2 Communication & Support

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Public documentation URL | ❓ Unknown | Not explicitly detailed for marketplace |
| Community (Discord/Slack/Forum) | ✅ Yes | Discord links found in audit |
| Official social media | ✅ Yes | Twitter/X links found in audit |
| Support response time | ❓ Unknown | Not explicitly detailed |
| Issue tracker for bug reports | ✅ Yes | GitHub Issues |

---

## Part 9: Security Incidents

*Document any known security incidents:*

| Date | Severity | Description | Resolution | Source |
|------|----------|-------------|------------|--------|
| Unknown | High | Prompt injection vulnerabilities leading to data theft and remote code execution in "Cline Bot AI Agent" (associated product). | Mitigation strategies recommended: restricting bot access, strict input validation, monitoring, user consent, avoiding token passthrough. | Web search (Offsec, Mindgard, Arxiv, Hackread) |

---

## Part 10: Delivery Method Security

*Security assessment per delivery channel:*

### Website (`cline.bot/mcp-marketplace`)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | |
| Privacy policy present | ✅ Yes | |
| CSP headers | ❌ No | |
| Login method | ❓ Unknown | Not explicitly detailed |

### API (for listed MCP servers)

*This refers to the APIs of the MCP servers listed by the marketplace.*

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ❓ Unknown | Depends on individual server |
| Authentication for reads | ❓ Unknown | Depends on individual server |
| Authentication for writes | ❓ Unknown | Depends on individual server |
| Rate limiting | ❓ Unknown | Depends on individual server |
| API versioning | ❓ Unknown | Depends on individual server |

### CLI (if applicable)

*Not applicable to this marketplace.*

| Check | Status | Notes |
|-------|--------|-------|
| Package manager | N/A | |
| License | N/A | |
| Package signing | N/A | |
| Update mechanism | N/A | |

### Client Integration (for listed MCP servers)

*This refers to how MCP clients integrate with the listed servers.*

| Check | Status | Notes |
|-------|--------|-------|
| Which clients integrate | ✅ Yes | Many clients integrate with MCP servers |
| Data format (JSON, etc.) | ✅ Yes | MCP Protocol implies structured data |
| Client-side verification | ❓ Unknown | Dependent on client implementation |
| Trust model | ❓ Unknown | Dependent on client and server |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

*What does this marketplace do well from a security/trust perspective?*

-   **Established Policies:** Existence of a Privacy Notice and Terms of Service on `cline.bot`. ✅
-   **Strong Web Security Headers:** The `cline.bot` website uses HTTPS, HSTS, X-Content-Type-Options, X-Frame-Options, Referrer-Policy, and Permissions-Policy, demonstrating good web security practices. ✅
-   **Strong Supply Chain Security Practices (for the marketplace codebase):** Enabled Dependabot, Code Scanning, and Secret Scanning on the GitHub repository, indicating proactive vulnerability and secret management. ✅
-   **Code Integrity (for the marketplace codebase):** All commits are signed (`signed_commits: true`). ✅
-   **Active Development (for the marketplace codebase):** Evidenced by frequent commits on GitHub. ✅
-   **Extensive Listing of MCP Servers:** The marketplace links to a wide variety of MCP server implementations, including those from major cloud providers (AWS, Microsoft Azure, Cloudflare) and other known entities. ✅

### 11.2 Weaknesses & Gaps

*What is missing, undocumented, or concerning?*

-   **Known Vulnerabilities in Associated Products:** The "Cline Bot AI Agent" (associated with Cline) has been found vulnerable to high-severity prompt injection attacks leading to data theft and RCE. This raises concerns about the security posture of the broader Cline ecosystem, including the marketplace. ❌
-   **Lack of Dedicated Security Policy:** No `SECURITY.md` in the GitHub repo, and no `/security` page on the website. This means no clear, documented process for reporting vulnerabilities to the project. ❌
-   **Lack of Branch Protection (for the marketplace codebase):** The GitHub repository does not have branch protection enabled (`branch_protection: false`). This is a significant security gap. ⚠️
-   **Absence of Community Contribution Guidelines:** Lack of `CODE_OF_CONDUCT.md` and `CONTRIBUTING.md` can hinder positive community engagement. ⚠️
-   **Undefined Publisher/Server Vetting:** The policies do not explicitly detail how MCP server publishers are verified or how listed MCP servers are vetted for security. This creates a trust gap. ❓
-   **Mixed Content on Website:** The `tier1_audit.py` revealed HTTP links within the HTTPS-served website, which can be a minor security concern. ⚠️
-   **No Public CSP:** The website lacks a Content-Security-Policy header, which is a significant web security best practice. ❌
-   **Infrequent Releases (for codebase):** `last_release: null` in audit output implies infrequent or no formal releases, which can impact timely security updates. ❓

### 11.3 Red Flags

*Specific concerns users should be aware of:*

-   **Known High-Severity Vulnerabilities in Ecosystem:** High Severity. The existence of high-severity vulnerabilities (prompt injection, RCE) in an associated product (Cline Bot AI Agent) is a major red flag, as it indicates potential systemic security issues or a lack of rigorous security testing across the product suite.
-   **Absence of `SECURITY.md` and Branch Protection:** High Severity. This combination for the marketplace codebase suggests a lack of robust security governance.
-   **Missing CSP Header:** Medium Severity. Without a Content-Security-Policy, the website is more vulnerable to XSS attacks and content injection.

### 11.4 Recommendations

*What should the marketplace operator improve?*

-   **Address Known Vulnerabilities:** Publicly address and provide robust mitigations for the identified prompt injection and RCE vulnerabilities in the Cline Bot AI Agent, and communicate how these lessons are applied across the Cline ecosystem, including the MCP Marketplace.
-   **Implement a `SECURITY.md`:** Create a `SECURITY.md` file in the GitHub repository detailing the process for reporting security vulnerabilities to the marketplace project.
-   **Enable Branch Protection:** Immediately enable branch protection for the `main` branch (and any other critical branches) requiring pull request reviews, status checks, and signed commits for the marketplace codebase.
-   **Define Publisher/Server Vetting:** Document the processes for verifying MCP server publishers and vetting listed MCP servers for security. This should be transparently communicated on the marketplace website.
-   **Add Missing Web Security Headers:** Implement a strong Content-Security-Policy for the `cline.bot` website.
-   **Add Community Guidelines:** Include `CODE_OF_CONDUCT.md` and `CONTRIBUTING.md` in the GitHub repository.
-   **Address Mixed Content:** Review and update all HTTP links on `cline.bot/mcp-marketplace` to use HTTPS.
-   **Implement Formal Release Process:** Establish a clear and consistent release process for the codebase to ensure timely delivery of updates and security patches.

### 11.5 Overall Trust Assessment

*Summary assessment for users considering this marketplace:*

The "Cline MCP Marketplace" demonstrates a commendable effort in providing an open-source platform for discovering MCP servers, with strong web security headers and robust GitHub-integrated supply chain security for its codebase. However, significant concerns arise from documented high-severity vulnerabilities in its associated "Cline Bot AI Agent," coupled with a lack of transparency regarding its security governance (missing `SECURITY.md`, no branch protection, undefined vetting processes for listed servers). The absence of a Content-Security-Policy on the website further compounds these issues. While the project is active and fosters a wide ecosystem, these critical security gaps and the presence of known vulnerabilities in its broader suite significantly impact its overall trustworthiness. Overall: **Poor to Moderate (with critical security practice and web security improvements needed)**.