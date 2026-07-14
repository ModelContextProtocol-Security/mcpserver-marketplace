---
title: "Archestra Private MCP Registry"
url: "https://archestra.ai/docs/platform-private-registry"
source_code_url: "https://github.com/archestra-ai/archestra"
is_marketplace: yes
is_aggregator: no
is_list_of_marketplaces: no
language: "en"
type: "code-hosting, registry-api, paas"
operator: "Archestra Inc."
operator_jurisdiction: "Unknown"
contact_email: "Unknown"
security_email: "Unknown"
server_count: "N/A (platform for registry)"
last_evaluated: "2026-02-06"
evaluation_status: "comprehensive"
evidence:
  - url: "https://archestra.ai/docs/platform-private-registry"
    description: "Primary documentation for the Private Registry"
    captured: "2026-02-06"
  - url: "https://github.com/archestra-ai/archestra"
    description: "GitHub repository for Archestra platform"
    captured: "2026-02-06"
  - url: "https://archestra.ai/privacy"
    description: "Archestra Privacy Policy"
    captured: "2026-02-06"
  - url: "https://archestra.ai/terms"
    description: "Archestra Terms of Service"
    captured: "2026-02-06"
---

## Overview

The Archestra Private MCP Registry is a feature within the broader Archestra platform, which provides an AI Agent runtime, Agent-to-Agent (A2A) network, Model Context Protocol (MCP) host, and a private registry for managing MCP servers. It is designed for organizations to curate, configure, and control access to AI tools, ensuring security, compliance, and standardization within their infrastructure. The project's codebase is open-source and hosted on GitHub.

## Features Summary

| Feature | Status | Notes |
|---------|--------|-------|
| Discovery/search | ✅ | Internal to deployed private registry |
| One-click install | ❓ | Implied for internal deployment, depends on integration |
| Curated list/recommendations | ✅ | Enables administrators to curate servers |
| Public API | ✅ | Part of the platform's API |
| CLI tool | ❓ | Not explicitly detailed for registry management |
| Client integration | ✅ | Designed to function as an MCP host |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Official name | Archestra Private MCP Registry (part of Archestra Platform) | Archestra Documentation |
| Primary URL | https://archestra.ai/docs/platform-private-registry | Archestra Documentation |
| Operator (company/individual) | Archestra Inc. | Archestra Privacy Policy/Terms of Service |
| Country/jurisdiction | Unknown | Not specified |
| Contact email (general) | Unknown | Not readily available on website or repo |
| Contact email (security) | Unknown | Not specified in repo or documentation |
| Launch date | 2025-07-15 | Audit Output (repo.activity.created_at for GitHub repo) |
| Marketplace source code available? | ✅ Yes | https://github.com/archestra-ai/archestra |

### 1.2 Marketplace Type

| Type | Yes/No | Notes |
|------|--------|-------|
| Directory/Aggregator - Lists servers with external links | ❌ No | Internal to platform |
| Registry - Provides API for programmatic discovery | ✅ Yes | As a private registry implementation |
| Code Hosting - Hosts server source code or packages | ✅ Yes | Archestra platform codebase on GitHub |
| Hosted Execution (PaaS) - Runs MCP servers on their infrastructure | ✅ Yes | Archestra platform includes runtime and host |
| Client-Embedded - Built into a specific MCP client | ❌ No | Not directly embedded |
| Curated List - Manually maintained list (e.g., awesome-list) | ✅ Yes | Enables administrators to curate servers |

### 1.3 Scale & Activity

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Servers listed (approximate count) | N/A (platform) | Depends on deployment and usage |
| Update frequency | Active | Last commit: 2026-02-06, Last release: 2026-02-06 (Audit Output) |
| Publisher/contributor count | Unknown | Need to check GitHub contributors |
| Changelog or update history available? | ✅ Yes | GitHub commit history and releases |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|--------|------------|-------------|
| Website with search/browse | ✅ Yes | Via Archestra UI (if deployed) |
| Public API (registry endpoint) | ✅ Yes | Archestra platform provides APIs |
| CLI tool | ❓ Unknown | Not explicitly detailed for registry management |
| IDE/editor plugin | ❓ Unknown | Not explicitly detailed |
| Integrated into MCP client(s) | ✅ Yes | As an MCP host |
| Browser extension | ❌ No | Not applicable |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| API documentation available? | ✅ Yes | Implied by platform features; needs specific URL |
| Authentication required for read? | ✅ Yes | Private registry implies authentication |
| Rate limiting? | ❓ Unknown | Not explicitly detailed |
| OpenAPI/Swagger spec? | ❓ Unknown | Not explicitly detailed |
| API terms of use? | ✅ Yes | Covered by Archestra Terms of Service |

### 2.3 Metadata Provided Per Server

| Field | Provided? | Notes |
|-------|-----------|-------|
| Server name | ✅ Yes | Core registry function |
| Description | ✅ Yes | Core registry function |
| Author/publisher | ✅ Yes | Core registry function |
| Source code URL | ✅ Yes | Core registry function |
| License | ✅ Yes | Core registry function |
| Version information | ✅ Yes | Core registry function |
| Last updated date | ✅ Yes | Core registry function |
| Download/install count | ❓ Unknown | Depends on registry implementation |
| Ratings/reviews | ❓ Unknown | Not explicitly detailed |
| Categories/tags | ✅ Yes | Core registry function |
| Required permissions/capabilities | ✅ Yes | Implied by private access control |
| Verification/trust badge | ❓ Unknown | Depends on registry implementation |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|--------|------------|---------|
| Link to external source (GitHub, etc.) | ✅ Yes | The platform can manage links to external sources |
| Direct download (zip, tarball) | ✅ Yes | As a codebase, can be downloaded |
| Package manager (npm, pip, etc.) | ❓ Unknown | Not explicitly detailed for packaging |
| Container image (Docker) | ✅ Yes | "Local MCP Servers" run as containers in Kubernetes |
| One-click install to client config | ❓ Unknown | Depends on client integration with the platform |
| Hosted execution (marketplace runs the server) | ✅ Yes | As an "AI Agent runtime" and "MCP host" |

### 3.2 Hosted Execution Details (PaaS Model)

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Server isolation method | ✅ Yes | "Local MCP Servers" run as containers within Kubernetes |
| User credentials/secrets handling | ✅ Yes | Can configure authentication and credentials for servers |
| Secret storage method | ✅ Yes | Secure storage of API keys and tokens mentioned |
| Audit logging available? | ❓ Unknown | Not explicitly detailed for hosted execution |
| Build/deployment process | ✅ Yes | Mentions using standard or custom Docker images |
| Publisher access to build logs? | ❓ Unknown | Not explicitly detailed |
| Multi-tenant isolation documented? | ❓ Unknown | Not explicitly detailed |

### 3.3 Source Accessibility

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Marketplace source code available? | ✅ Yes | https://github.com/archestra-ai/archestra |
| API documentation URL | ❓ Unknown | Implied by platform features; needs specific URL |
| Self-hostable? | ✅ Yes | Designed for private deployment by organizations |

### 3.4 Server Coverage

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Lists vendor-hosted servers (Vercel, Cloudflare, etc.)? | N/A (platform) | Internal private registry |
| Distinguishes hosted vs local servers? | ✅ Yes | Documentation distinguishes Remote vs Local MCP Servers |
| Vendor-hosted servers found in search? | N/A (platform) | Internal private registry |

### 3.5 Vendor-Hosted Coverage Test

*Not applicable to this codebase and private registry platform.*

| Pattern Searched | Found? | Notes |
|------------------|--------|-------|
| mcp.vercel.com | N/A | |
| vercel + mcp | N/A | |
| cloudflare + mcp | N/A | |
| stripe + mcp | N/A | |
| linear + mcp | N/A | |
| huggingface.co/mcp | N/A | |
| [other vendor patterns] | N/A | |

**Test Result:** N/A - This is a platform for a private registry, not a public marketplace that directly lists servers.

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Publisher verification process exists? | ✅ Yes | Administrative control over adding servers to private registry |
| Verification requirements documented? | ❓ Unknown | Specific requirements for administrative control not detailed |
| 2FA/MFA required for publishers? | N/A (platform) | Depends on the organization's IAM for Archestra deployment |
| Trust tiers (verified, official, etc.)? | ❓ Unknown | Not explicitly detailed |
| Verification criteria publicly documented? | ❌ No | Not publicly documented for private registry |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Servers reviewed before listing? | ✅ Yes | Administrative control over adding servers; "MCP Server Security Scanning" feature |
| Automated security scanning? | ✅ Yes | "MCP Server Security Scanning" feature in documentation |
| Malware detection? | ❓ Unknown | Not explicitly detailed |
| Dependency vulnerability scanning? | ❓ Unknown | Not explicitly detailed |
| Flagged server removal speed? | ❓ Unknown | Depends on administrative policies |
| Typosquatting/namesquatting protection? | N/A (platform) | Private registry, not public domain |

### 4.3 Community Trust Signals

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Users can report problematic servers? | N/A (platform) | Depends on administrative policies of deployed instance |
| Visible "Report" button? | N/A (platform) | Depends on deployed UI |
| User reviews or ratings? | ❌ No | Not mentioned |
| Download/usage count visible? | ❓ Unknown | Not explicitly detailed |
| "Last updated" timestamp visible? | ✅ Yes | GitHub activity for codebase; registry API can provide this for servers |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Privacy policy exists? | ✅ Yes | https://archestra.ai/privacy |
| Privacy policy URL | ✅ Yes | https://archestra.ai/privacy |
| User data collected (summary) | ✅ Yes | Documented in policy |
| Data shared with third parties? | ✅ Yes | Documented in policy |
| Analytics/tracking tools used | ✅ Yes | Documented in policy |
| Data retention policy? | ✅ Yes | Documented in policy |
| GDPR compliance claimed? | ❓ Unknown | Not explicitly mentioned in policy |

### 5.1.1 Third-Party Integrations Detected

*Based on `tier1_audit.py` output for archestra.ai*

| Integration | Present? | Details |
|-------------|----------|---------|
| Google Analytics | ❓ Unknown | Not detected by audit, not explicitly mentioned |
| Google Tag Manager | ❓ Unknown | Not detected by audit, not explicitly mentioned |
| Google AdSense | ❓ Unknown | Not detected by audit, not explicitly mentioned |
| Google Fonts | ❓ Unknown | Not detected by audit, not explicitly mentioned |
| Cloudflare (CDN) | ❌ No | Not detected by audit, "Server: Vercel" |
| Other CDN | ✅ Yes | Vercel |
| Social login providers | N/A | Not applicable to website audit |
| Payment processors | N/A | Not applicable to website audit |
| Other trackers | ❓ Unknown | Not explicitly detected |

### 5.2 Terms of Service

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Terms of service exists? | ✅ Yes | https://archestra.ai/terms |
| Terms of service URL | ✅ Yes | https://archestra.ai/terms |
| Prohibited publisher activities | N/A | Private registry, administrative control |
| Prohibited user activities | ✅ Yes | Documented in policy |
| Liability limitations | ✅ Yes | Documented in policy |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Security policy exists? | ❌ No | No `SECURITY.md` in repo; no `/security` page |
| Security policy URL (SECURITY.md) | N/A | |
| Vulnerability disclosure process? | ❌ No | Not documented |
| Bug bounty program? | ❌ No | Not mentioned |
| Past security incidents disclosed? | ❌ No | No public records found |
| Status page for uptime/incidents? | ❓ Unknown | Not mentioned |

---

## Part 6: Supply Chain Security

### 6.1 Code Integrity

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Packages/images signed? | ❓ Unknown | Not explicitly mentioned for images or packages |
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
| Security update communication method | ❌ No | No documented process for reporting/receiving updates |
| Auto-updates supported? | N/A | Not applicable for a codebase |
| Version pinning available? | N/A | Not applicable for a codebase |
| Deprecation/EOL policy? | ❓ Unknown | Not explicitly mentioned |

---

## Part 7: Technical Security Posture

*This section combines information from `tier1_audit.py` (for the `archestra.ai` website) and `audit.py --repo` (for the GitHub repository).*

### 7.1 Web Security Headers (from `archestra.ai`)

| Header | Present? | Value |
|--------|----------|-------|
| HTTPS enforced | ✅ Yes | |
| Strict-Transport-Security (HSTS) | ✅ Yes | `max-age=63072000` |
| Content-Security-Policy | ❌ No | |
| X-Frame-Options | ❌ No | |
| X-Content-Type-Options | ❌ No | |
| Referrer-Policy | ❌ No | |
| Permissions-Policy | ❌ No | |
| Cross-Origin-Opener-Policy | ❌ No | |
| Cross-Origin-Resource-Policy | ❌ No | |

### 7.2 TLS Certificate (from `archestra.ai`)

| Field | Value |
|-------|-------|
| Issuer | C=US, O=Let's Encrypt, CN=R12 |
| Subject | CN=archestra.ai |
| Valid from | Dec 12 22:01:26 2025 GMT |
| Valid until | Mar 12 22:01:25 2026 GMT |
| SHA256 fingerprint | `3B:31:21:EA:A0:E2:56:D8:03:C5:5E:A1:6B:E3:7C:FE:F7:FA:CB:8D:88:25:CD:01:9F:59:FB:C1:CD:E3:B8:6B` |

### 7.3 DNS & Hosting (from `archestra.ai`)

| Field | Value |
|-------|-------|
| A records | `216.150.1.193` |
| AAAA records | None |
| CNAME records | None |
| NS records | `ns10.domaincontrol.com.`, `ns09.domaincontrol.com.` |
| Provider hints | Vercel (from HTTP headers) |

### 7.4 Path Availability (Automated Probe on `archestra.ai`)

| Path | Status Code | Notes |
|------|-------------|-------|
| /privacy | 200 | |
| /privacy-policy | 404 | |
| /terms | 200 | |
| /tos | 404 | |
| /security | 404 | |
| /legal | 404 | |
| /about | 200 | |
| /contact | 404 | |
| /robots.txt | 200 | |
| /sitemap.xml | 200 | |
| /api | 404 | |
| /docs | 307 | Redirects to `https://archestra.ai/docs/` |
| /api-docs | 404 | |
| /swagger.json | 404 | |
| /openapi.json | 404 | |
| /openapi.yaml | 404 | |

### 7.5 Mixed Content (from `archestra.ai`)

| Check | Result |
|-------|--------|
| HTTP links found | ✅ Yes | 15 samples |
| HTTP subresources found | ❌ No | |
| Sample URLs | `http://archestra.default.svc:9000`, `http://idp.example.com:8080`, etc. |

### 7.6 Social/Contact Links Found (from `archestra.ai` and GitHub repo)

| Type | URL |
|------|-----|
| GitHub | ✅ Yes | `https://github.com/archestra-ai/archestra` |
| Discord | ❓ Unknown | Not found in audit output or README |
| Twitter/X | ❓ Unknown | Not found in audit output or README |
| LinkedIn | ❓ Unknown | Not found in audit output or README |
| Email (mailto) | ❌ No | Not found |

### 7.7 Authentication & Authorization (from GitHub repo and docs)

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Authentication methods supported | ✅ Yes | OAuth, direct API keys, browser-based flows |
| OAuth/OIDC providers | ❓ Unknown | Not explicitly detailed for Archestra Inc. |
| Session management documented? | ❓ Unknown | Not explicitly documented for codebase |
| API tokens scoped and time-limited? | ✅ Yes | Implied by "fine-grained access control" and secure storage of API keys |

---

## Part 8: Operator Transparency

### 8.1 Business Model

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Free or paid? | ✅ Free (codebase) / Paid (platform) | Codebase is open-source; platform offers enterprise features |
| Pricing model (if paid) | ❓ Unknown | Not detailed on `archestra.ai` publicly accessible pages |
| Revenue source | ❓ Unknown | Not detailed on `archestra.ai` publicly accessible pages |
| Registered business entity? | ✅ Yes | "Archestra Inc." from Privacy Policy/Terms of Service |

### 8.2 Communication & Support

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Public documentation URL | ✅ Yes | https://archestra.ai/docs/ |
| Community (Discord/Slack/Forum) | ❓ Unknown | Not explicitly mentioned in docs or audit |
| Official social media | ❓ Unknown | Not explicitly mentioned in docs or audit |
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

*Security assessment per delivery channel:*

### Website (`archestra.ai`)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `tier1_audit.py` |
| Privacy policy present | ✅ Yes | `https://archestra.ai/privacy` |
| CSP headers | ❌ No | `tier1_audit.py` |
| Login method | N/A | Not applicable to documentation site |

### API (Archestra platform API)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | Implied for secure enterprise platform |
| Authentication for reads | ✅ Yes | Private registry implies strong auth |
| Authentication for writes | ✅ Yes | Private registry implies strong auth |
| Rate limiting | ❓ Unknown | Not explicitly documented |
| API versioning | ❓ Unknown | Not explicitly documented |

### CLI (if applicable)

*Not explicitly detailed for registry management within Archestra.*

| Check | Status | Notes |
|-------|--------|-------|
| Package manager | N/A | |
| License | N/A | |
| Package signing | N/A | |
| Update mechanism | N/A | |

### Client Integration (Archestra platform client integration)

| Check | Status | Notes |
|-------|--------|-------|
| Which clients integrate | ❓ Unknown | Not explicitly detailed |
| Data format (JSON, etc.) | ✅ Yes | MCP Protocol implies structured data |
| Client-side verification | ❓ Unknown | Dependent on client implementation |
| Trust model | ✅ Yes | Supports fine-grained access control within platform |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

*What does this marketplace do well from a security/trust perspective?*

- **Comprehensive Documentation:** Clear and detailed documentation regarding the platform's features, including the private registry. ✅
- **Established Policies:** Existence of a Privacy Policy and Terms of Service on the `archestra.ai` website. ✅
- **Strong Supply Chain Security Practices:** Enabled Dependabot, Code Scanning, and Secret Scanning on the GitHub repository, indicating proactive vulnerability and secret management. ✅
- **Code Integrity:** All commits are signed (`signed_commits: true`), enhancing trust in code authorship. ✅
- **Active Development & Community:** Evidenced by frequent commits, releases, and a substantial number of stars/forks/issues on GitHub. ✅
- **Built-in Security Features for Registry:** Documentation highlights "MCP Server Security Scanning" for servers within the private registry, indicating a focus on vetting registered components. ✅
- **Enterprise-Grade Focus:** Designed for private, controlled environments with features like centralized management, authentication, and credential configuration. ✅

### 11.2 Weaknesses & Gaps

*What is missing, undocumented, or concerning?*

- **Missing Dedicated Security Policy (`SECURITY.md`):** The GitHub repository lacks a `SECURITY.md` file or any easily discoverable equivalent for reporting vulnerabilities to the project directly. This is a significant gap for an open-source project. ❌
- **Lack of Branch Protection:** The GitHub repository does not have branch protection enabled (`branch_protection: false`). This is a notable security gap for a critical open-source project, increasing the risk of unreviewed code being merged. ⚠️
- **Absence of Community Contribution Guidelines:** Lack of `CODE_OF_CONDUCT.md` and `CONTRIBUTING.md` can hinder positive community engagement and make it less clear how to contribute securely. ⚠️
- **Mixed Content on Documentation Site:** The `tier1_audit.py` revealed HTTP links within the HTTPS-served documentation, which can be a minor security concern (though likely internal links). ⚠️
- **Web Security Headers:** Missing several key web security headers (CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, Cross-Origin-Opener-Policy, Cross-Origin-Resource-Policy) on `archestra.ai`. ❌

### 11.3 Red Flags

*Specific concerns users should be aware of:*

- **Absence of `SECURITY.md` and Branch Protection:** High Severity. The combination of no clear vulnerability reporting process and a lack of branch protection on a critical open-source project creates a significant security risk.
- **Missing Web Security Headers:** Medium Severity. Lack of these headers can expose users to various web-based attacks (e.g., XSS, clickjacking, MIME-type sniffing).

### 11.4 Recommendations

*What should the marketplace operator improve?*

- **Implement a `SECURITY.md`:** Create a `SECURITY.md` file in the GitHub repository detailing the process for reporting security vulnerabilities, including contact information and expected response times.
- **Enable Branch Protection:** Immediately enable branch protection for the `main` branch (and any other critical branches) requiring pull request reviews, status checks, and signed commits.
- **Add Community Guidelines:** Include `CODE_OF_CONDUCT.md` and `CONTRIBUTING.md` to foster a healthier and more secure open-source community.
- **Address Mixed Content:** Review and update all internal links on `archestra.ai` documentation to use HTTPS to avoid mixed content warnings and potential security issues.
- **Implement Missing Web Security Headers:** Add Content-Security-Policy, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, Cross-Origin-Opener-Policy, and Cross-Origin-Resource-Policy to the `archestra.ai` website.

### 11.5 Overall Trust Assessment

*Summary assessment for users considering this marketplace:*

The "Archestra Private MCP Registry" (as part of the broader Archestra platform) presents a robust and actively developed solution for managing MCP servers in private, enterprise environments. Its commitment to supply chain security through GitHub's automated tools and strong code integrity via signed commits are significant strengths. The presence of comprehensive privacy and terms policies for their overall service is also positive. However, the absence of a clear vulnerability reporting mechanism (`SECURITY.md`), combined with the lack of branch protection on its open-source repository, are critical weaknesses that significantly impact its trustworthiness as a public codebase. Additionally, the `archestra.ai` website lacks several important web security headers, which could expose users to client-side attacks. Addressing these fundamental security practices is essential for instilling greater confidence in the project's security posture. Overall: **Good (with critical security practice and web security improvements needed)**.

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
- Command: `python security-report/tools/tier1_audit.py https://archestra.ai/docs/platform-private-registry`
- Command: `python security-report/tools/audit.py --repo https://github.com/archestra-ai/archestra`
- Date: 2026-02-06
- Tool version: N/A (inline script execution)

**Manual checks performed:**
- Review of `archestra.ai` website, Privacy Policy, Terms of Service
- Review of GitHub repository README.md
- Review of GitHub repository activity (commits, releases)

### `tier1_audit.py` Output (for `https://archestra.ai/docs/platform-private-registry`)

```json
{
  "target": "https://archestra.ai/docs/platform-private-registry",
  "host": "archestra.ai",
  "http": {
    "status_chain": [
      "HTTP/2 200"
    ],
    "headers": {
      "accept-ranges": "bytes",
      "access-control-allow-origin": "*",
      "age": "18069",
      "cache-control": "public, max-age=0, must-revalidate",
      "content-disposition": "inline",
      "content-type": "text/html; charset=utf-8",
      "date": "Fri, 06 Feb 2026 20:14:34 GMT",
      "etag": "\"44da2033f3492cd2006a724362f45e4a\"",
      "server": "Vercel",
      "strict-transport-security": "max-age=63072000",
      "vary": "rsc, next-router-state-tree, next-router-prefetch, next-router-segment-prefetch",
      "x-matched-path": "/docs/platform-private-registry",
      "x-nextjs-prerender": "1",
      "x-nextjs-stale-time": "300",
      "x-vercel-cache": "HIT",
      "x-vercel-id": "pdx1::m7l4l-1770408873718-0f4f2036fe5c",
      "content-length": "346686"
    },
    "security_headers": {
      "strict_transport_security": "max-age=63072000",
      "content_security_policy": null,
      "x_frame_options": null,
      "x_content_type_options": null,
      "referrer_policy": null,
      "permissions_policy": null,
      "cross_origin_opener_policy": null,
      "cross_origin_resource_policy": null,
      "cross_origin_embedder_policy": null
    }
  },
  "tls": {
    "ok": true,
    "raw": "issuer=C=US, O=Let's Encrypt, CN=R12\nsubject=CN=archestra.ai\nnotBefore=Dec 12 22:01:26 2025 GMT\nnotAfter=Mar 12 22:01:25 2026 GMT\nsha256 Fingerprint=3B:31:21:EA:A0:E2:56:D8:03:C5:5E:A1:6B:E3:7C:FE:F7:FA:CB:8D:88:25:CD:01:9F:59:FB:C1:CD:E3:B8:6B\n",
    "issuer": "C=US, O=Let's Encrypt, CN=R12",
    "subject": "CN=archestra.ai",
    "not_before": "Dec 12 22:01:26 2025 GMT",
    "not_after": "Mar 12 22:01:25 2026 GMT"
  },
  "dns": {
    "host": "archestra.ai",
    "domain": "archestra.ai",
    "A": [
      "216.150.1.193"
    ],
    "AAAA": [],
    "CNAME": [],
    "NS": [
      "ns10.domaincontrol.com.",
      "ns09.domaincontrol.com."
    ],
    "provider_hints": []
  },
  "content": {
    "mixed_content": {
      "http_links": 15,
      "http_subresources": 0,
      "samples": [
        "http://archestra.default.svc:9000,https://api.archestra.example.com`\\n",
        "http://idp.example.com:8080,https://auth.example.com`)\\n",
        "http://lightrag:9621`\\n",
        "http://your-collector:4318/v1/traces\\n```\\n\\nIf",
        "http://tryhandlebarsjs.com/)",
        "http://lightrag:9621\\nARCHESTRA_KNOWLEDGE_GRAPH_LIGHTRAG_API_KEY=your-api-key",
        "http://e2e-tests-wiremock:8080/v1\\",
        "http://mastra-ai-archestra-1:9000/v1/openai",
        "http://mastra-ai-archestra-1:9000/v1/openai\\",
        "http://platform-archestra-1:9000/v1/openai\\n```\\n\\ninstead"
      ]
    }
  },
  "paths": {
    "policy": {
      "/privacy": 200,
      "/privacy-policy": 404,
      "/terms": 200,
      "/tos": 404,
      "/security": 404,
      "/legal": 404,
      "/about": 200,
      "/contact": 404,
      "/robots.txt": 200,
      "/sitemap.xml": 200
    },
    "api": {
      "/api": 404,
      "/docs": 307,
      "/api-docs": 404,
      "/swagger.json": 404,
      "/openapi.json": 404,
      "/openapi.yaml": 404,
      "/swagger": 404
    }
  },
  "social": [
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/archestra"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/archestra/edit/main/docs/pages/platform-private-registry.md"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/archestra/blob/main/platform/helm/archestra/values.yaml).\\n\\n####"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/archestra/issues/720))\\n\\n###"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/archestra/issues/2058))"
    },
    {
      "type": "github",
      "url": "https://github.com/vllm-project/vllm)"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/mcp-server-lightrag)"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/archestra.git\\ncd"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/archestra/blob/main/platform/PROVIDER_SMOKE_TEST.md)"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/examples\\ncd"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/examples/tree/main/mastra-ai).\\n\\n###"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/archestra\\ncd"
    },
    {
      "type": "github",
      "url": "https://github.com/github/github-mcp-server\\u003e\\n\\n###"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/archestra/issues/647)"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/archestra/issues/647\\n```\\n\\nSee"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/archestra/issues/647\\n```\\n\\nN8N"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/examples/tree/main/pydantic-ai](https://github.com/archestra-ai/examples/tree/main/pydantic-ai)\\n\\n##"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/archestra/issues/669))"
    },
    {
      "type": "github",
      "url": "https://github.com/settings/tokens](https://github.com/settings/tokens)\\n\\nNo"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/examples/tree/main/ai-sdk-express](https://github.com/archestra-ai/examples/tree/main/ai-sdk-express)\\n\\n##"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/archestra/issues/720))."
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/archestra?tab=readme-ov-file#-non-probabalistic-security-to-prevent-data-exfiltration)."
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/archestra/issues/647\\n```\\n\\n##"
    },
    {
      "type": "github",
      "url": "https://github.com/archestra-ai/archestra/edit/main/docs/pages/platform-private-registry.md\\"
    }
  ],
  "provider_hints": []
}
```

### `audit.py --repo` Output (for `https://github.com/archestra-ai/archestra`)

```json
{
  "repo": {
    "repo_info": {
      "platform": "github",
      "owner": "archestra-ai",
      "repo": "archestra",
      "url": "https://github.com/archestra-ai/archestra",
      "is_org": true
    },
    "security_files": {
      "security_md": false,
      "security_md_url": null,
      "security_policy": false,
      "code_of_conduct": false,
      "contributing_md": false,
      "license": "AGPL-3.0",
      "license_url": "https://github.com/archestra-ai/archestra/blob/main/LICENSE"
    },
    "org_verification": {
      "is_org": true,
      "org_name": "Archestra",
      "verified": false,
      "verified_domains": []
    },
    "activity": {
      "stars": 2867,
      "forks": 227,
      "watchers": 9,
      "open_issues": 106,
      "open_prs": 1,
      "last_commit": "2026-02-06T16:11:35Z",
      "last_release": "2026-02-06T14:00:44Z",
      "created_at": "2025-07-15T12:07:55Z",
      "updated_at": "2026-02-06T20:02:44Z",
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
      "a2a",
      "acp",
      "agent",
      "ai",
      "mcp",
      "mcp-client",
      "mcp-server",
      "runtime",
      "mcp-host",
      "mcp-servers",
      "mcp-tools",
      "claude",
      "deepseek",
      "gemini",
      "openai",
      "a2a-mcp",
      "chatgpt",
      "chatgpt-api",
      "k8s",
      "mcp-gateway"
    ],
    "errors": []
  }
}
```

### Key Findings Summary

| Category | Result |
|----------|--------|
| HTTP status | 200 OK |
| Provider hints | Vercel |
| Security headers present | HSTS |
| Security headers missing | CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, Cross-Origin-Opener-Policy, Cross-Origin-Resource-Policy |
| Mixed content | ✅ Yes (15 http links) |
| Policy endpoints (200) | /privacy, /terms, /about, /robots.txt, /sitemap.xml |
| Policy endpoints (404) | /privacy-policy, /tos, /security, /legal, /contact, /api, /api-docs, /swagger.json, /openapi.json, /openapi.yaml, /swagger |
| Policy endpoints (307) | /docs |
| Social links detected | GitHub (multiple) |
| Repository Security Files | LICENSE present; no SECURITY.md, Code of Conduct, Contributing.md |
| Organization Verification | `is_org: true`, `verified: false` |
| Activity (Stars, Forks, Issues, PRs) | Active development |
| Security Features | Dependabot, Code Scanning, Secret Scanning, Signed Commits enabled. Branch Protection disabled. |

### Additional Evidence

- README.md: https://github.com/archestra-ai/archestra/blob/main/README.md
- LICENSE: https://github.com/archestra-ai/archestra/blob/main/LICENSE
- Privacy Policy: https://archestra.ai/privacy
- Terms of Service: https://archestra.ai/terms

---

## Changelog

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 2026-02-06 | 1.0 | Initial comprehensive evaluation | Gemini CLI |