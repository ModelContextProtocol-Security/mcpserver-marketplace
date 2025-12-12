# MCP Marketplace Security Evaluation Template

**Version**: 2.0
**Purpose**: Unified template for MCP marketplace evaluation - serves as both structured questionnaire AND final report format
**Usage**:
- Evaluators: Complete based on automated tools + manual investigation
- Operators: Verify findings and correct errors
- Automated Tools: tier1_audit.py populates Technical Security section

---

## YAML Frontmatter (Required)

```yaml
---
title: "[MARKETPLACE_NAME]"
url: "[PRIMARY_URL]"
source_code_url: "[GITHUB_OR_EMPTY]"
is_marketplace: yes/no
is_aggregator: yes/no
is_list_of_marketplaces: yes/no
language: "[ISO_CODE]"
type: "[TYPE: directory | registry-api | code-hosting | paas | client-embedded | curated-list]"
operator: "[COMPANY_OR_INDIVIDUAL]"
operator_jurisdiction: "[COUNTRY]"
contact_email: "[EMAIL]"
security_email: "[EMAIL_OR_EMPTY]"
server_count: "[COUNT_OR_UNKNOWN]"
last_evaluated: "[YYYY-MM-DD]"
evaluation_status: "[comprehensive | tier-1-2-moderate | tier-1-basic | stub | blocked]"
evidence:
  - url: "[URL]"
    description: "[WHAT_THIS_PROVES]"
    captured: "[YYYY-MM-DD]"
---
```

---

## Overview

[2-3 sentence summary: What is this marketplace, who operates it, what does it do]

## Features Summary

*Quick reference - details in Part 2*

| Feature | Status | Notes |
|---------|--------|-------|
| Discovery/search | | |
| One-click install | | |
| Curated list/recommendations | | |
| Public API | | |
| CLI tool | | |
| Client integration | | |

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Official name | | |
| Primary URL | | |
| Operator (company/individual) | | |
| Country/jurisdiction | | |
| Contact email (general) | | |
| Contact email (security) | | |
| Launch date | | |
| Marketplace source code available? | | |

### 1.2 Marketplace Type

*Check all that apply:*

| Type | Yes/No | Notes |
|------|--------|-------|
| Directory/Aggregator - Lists servers with external links | | |
| Registry - Provides API for programmatic discovery | | |
| Code Hosting - Hosts server source code or packages | | |
| Hosted Execution (PaaS) - Runs MCP servers on their infrastructure | | |
| Client-Embedded - Built into a specific MCP client | | |
| Curated List - Manually maintained list (e.g., awesome-list) | | |

### 1.3 Scale & Activity

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Servers listed (approximate count) | | |
| Update frequency | | |
| Publisher/contributor count | | |
| Changelog or update history available? | | |

---

## Part 2: Discovery & Access

### 2.1 How Users Find Servers

| Method | Available? | URL/Details |
|--------|------------|-------------|
| Website with search/browse | | |
| Public API (registry endpoint) | | |
| CLI tool | | |
| IDE/editor plugin | | |
| Integrated into MCP client(s) | | |
| Browser extension | | |

### 2.2 API Details (if applicable)

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| API documentation available? | | |
| Authentication required for read? | | |
| Rate limiting? | | |
| OpenAPI/Swagger spec? | | |
| API terms of use? | | |

### 2.3 Metadata Provided Per Server

| Field | Provided? | Notes |
|-------|-----------|-------|
| Server name | | |
| Description | | |
| Author/publisher | | |
| Source code URL | | |
| License | | |
| Version information | | |
| Last updated date | | |
| Download/install count | | |
| Ratings/reviews | | |
| Categories/tags | | |
| Required permissions/capabilities | | |
| Verification/trust badge | | |

---

## Part 3: Server Delivery Model

### 3.1 Delivery Methods

| Method | Supported? | Details |
|--------|------------|---------|
| Link to external source (GitHub, etc.) | | |
| Direct download (zip, tarball) | | |
| Package manager (npm, pip, etc.) | | |
| Container image (Docker) | | |
| One-click install to client config | | |
| Hosted execution (marketplace runs the server) | | |

### 3.2 Hosted Execution Details (PaaS Model)

*Complete if marketplace hosts/runs servers:*

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Server isolation method | | |
| User credentials/secrets handling | | |
| Secret storage method | | |
| Audit logging available? | | |
| Build/deployment process | | |
| Publisher access to build logs? | | |
| Multi-tenant isolation documented? | | |

### 3.3 Source Accessibility

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Marketplace source code available? | | |
| API documentation URL | | |
| Self-hostable? | | |

### 3.4 Server Coverage

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Lists vendor-hosted servers (Vercel, Cloudflare, etc.)? | | |
| Distinguishes hosted vs local servers? | | |
| Vendor-hosted servers found in search? | | |

### 3.5 Vendor-Hosted Coverage Test

*Methodology: Search for known vendor-hosted MCP server patterns*

| Pattern Searched | Found? | Notes |
|------------------|--------|-------|
| mcp.vercel.com | | |
| vercel + mcp | | |
| cloudflare + mcp | | |
| stripe + mcp | | |
| linear + mcp | | |
| huggingface.co/mcp | | |
| [other vendor patterns] | | |

**Test Result:** [Summary of vendor-hosted coverage]

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Publisher verification process exists? | | |
| Verification requirements documented? | | |
| 2FA/MFA required for publishers? | | |
| Trust tiers (verified, official, etc.)? | | |
| Verification criteria publicly documented? | | |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Servers reviewed before listing? | | |
| Automated security scanning? | | |
| Malware detection? | | |
| Dependency vulnerability scanning? | | |
| Flagged server removal speed? | | |
| Typosquatting/namesquatting protection? | | |

### 4.3 Community Trust Signals

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Users can report problematic servers? | | |
| Visible "Report" button? | | |
| User reviews or ratings? | | |
| Download/usage count visible? | | |
| "Last updated" timestamp visible? | | |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Privacy policy exists? | | |
| Privacy policy URL | | |
| User data collected (summary) | | |
| Data shared with third parties? | | |
| Analytics/tracking tools used | | |
| Data retention policy? | | |
| GDPR compliance claimed? | | |

### 5.1.1 Third-Party Integrations Detected

| Integration | Present? | Details |
|-------------|----------|---------|
| Google Analytics | | |
| Google Tag Manager | | |
| Google AdSense | | |
| Google Fonts | | |
| Cloudflare (CDN) | | |
| Other CDN | | |
| Social login providers | | |
| Payment processors | | |
| Other trackers | | |

### 5.2 Terms of Service

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Terms of service exists? | | |
| Terms of service URL | | |
| Prohibited publisher activities | | |
| Prohibited user activities | | |
| Liability limitations | | |

### 5.3 Security Policy

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Security policy exists? | | |
| Security policy URL (SECURITY.md) | | |
| Vulnerability disclosure process? | | |
| Bug bounty program? | | |
| Past security incidents disclosed? | | |
| Status page for uptime/incidents? | | |

---

## Part 6: Supply Chain Security

*Required for Code Hosting/PaaS marketplaces:*

### 6.1 Code Integrity

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Packages/images signed? | | |
| Provenance attestation provided? | | |
| SBOMs (Software Bill of Materials) available? | | |
| Reproducible build support? | | |

### 6.2 Dependency Management

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Dependencies scanned for vulnerabilities? | | |
| Dependency confusion protection? | | |
| Lock files required/validated? | | |
| Vulnerable dependency notifications? | | |

### 6.3 Update & Patch Management

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Security update communication method | | |
| Auto-updates supported? | | |
| Version pinning available? | | |
| Deprecation/EOL policy? | | |

---

## Part 7: Technical Security Posture

*Fields in this section can be auto-populated by tier1_audit.py*

### 7.1 Web Security Headers

| Header | Present? | Value |
|--------|----------|-------|
| HTTPS enforced | | |
| Strict-Transport-Security (HSTS) | | |
| Content-Security-Policy | | |
| X-Frame-Options | | |
| X-Content-Type-Options | | |
| Referrer-Policy | | |
| Permissions-Policy | | |
| Cross-Origin-Opener-Policy | | |
| Cross-Origin-Resource-Policy | | |

### 7.2 TLS Certificate

| Field | Value |
|-------|-------|
| Issuer | |
| Subject | |
| Valid from | |
| Valid until | |
| SHA256 fingerprint | |

### 7.3 DNS & Hosting

| Field | Value |
|-------|-------|
| A records | |
| AAAA records | |
| CNAME records | |
| NS records | |
| Provider hints | |

### 7.4 Path Availability (Automated Probe)

| Path | Status Code | Notes |
|------|-------------|-------|
| /privacy | | |
| /privacy-policy | | |
| /terms | | |
| /tos | | |
| /security | | |
| /legal | | |
| /about | | |
| /contact | | |
| /robots.txt | | |
| /sitemap.xml | | |
| /api | | |
| /docs | | |
| /api-docs | | |
| /swagger.json | | |
| /openapi.json | | |
| /openapi.yaml | | |

### 7.5 Mixed Content

| Check | Result |
|-------|--------|
| HTTP links found | |
| HTTP subresources found | |
| Sample URLs | |

### 7.6 Social/Contact Links Found

| Type | URL |
|------|-----|
| GitHub | |
| Discord | |
| Twitter/X | |
| LinkedIn | |
| Email (mailto) | |

### 7.7 Authentication & Authorization

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Authentication methods supported | | |
| OAuth/OIDC providers | | |
| Session management documented? | | |
| API tokens scoped and time-limited? | | |

---

## Part 8: Operator Transparency

### 8.1 Business Model

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Free or paid? | | |
| Pricing model (if paid) | | |
| Revenue source | | |
| Registered business entity? | | |

### 8.2 Communication & Support

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Public documentation URL | | |
| Community (Discord/Slack/Forum) | | |
| Official social media | | |
| Support response time | | |
| Issue tracker for bug reports | | |

---

## Part 9: Security Incidents

*Document any known security incidents:*

| Date | Severity | Description | Resolution | Source |
|------|----------|-------------|------------|--------|
| | | | | |

---

## Part 10: Delivery Method Security

*Security assessment per delivery channel:*

### Website

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | | |
| Privacy policy present | | |
| CSP headers | | |
| Login method | | |

### API (if applicable)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | | |
| Authentication for reads | | |
| Authentication for writes | | |
| Rate limiting | | |
| API versioning | | |

### CLI (if applicable)

| Check | Status | Notes |
|-------|--------|-------|
| Package manager | | |
| License | | |
| Package signing | | |
| Update mechanism | | |

### Client Integration (if applicable)

| Check | Status | Notes |
|-------|--------|-------|
| Which clients integrate | | |
| Data format (JSON, etc.) | | |
| Client-side verification | | |
| Trust model | | |

---

## Part 11: Evaluator Assessment

### 11.1 Strengths

*What does this marketplace do well from a security/trust perspective?*

-
-
-

### 11.2 Weaknesses & Gaps

*What is missing, undocumented, or concerning?*

-
-
-

### 11.3 Red Flags

*Specific concerns users should be aware of:*

-
-
-

### 11.4 Recommendations

*What should the marketplace operator improve?*

-
-
-

### 11.5 Overall Trust Assessment

*Summary assessment for users considering this marketplace:*

[1-2 paragraph assessment covering: security posture, transparency, appropriate use cases, risks]

---

## Evaluation Metadata

| Field | Value |
|-------|-------|
| Evaluator | |
| Evaluation Date | |
| Marketplace Version/State | |
| Automated Audit Tool Version | |
| Evidence Archive Location | |
| Sent to Operator for Review? | |
| Operator Response Received? | |
| Operator Verified? | |
| Last Updated | |

---

## Audit Evidence

*Raw output from automated tools (for reproducibility):*

### Testing Methodology

**Automated checks performed:**
- Command: `python3 security-report/tools/tier1_audit.py [URL]`
- Date: [YYYY-MM-DD]
- Tool version: [VERSION]

**Manual checks performed:**
- [List of manual investigations: privacy policy review, GitHub repo review, etc.]

### tier1_audit.py Output

```json
[PASTE_RAW_JSON_OUTPUT_HERE]
```

### Key Findings Summary

| Category | Result |
|----------|--------|
| HTTP status | |
| Provider hints | |
| Security headers present | |
| Security headers missing | |
| Mixed content | |
| Policy endpoints (200) | |
| Policy endpoints (404) | |
| API endpoints (200) | |
| Social links detected | |

### Additional Evidence

[Screenshots, archived pages, or other evidence]

---

## Changelog

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| | | | |

---

## Marking Guide

When completing this template, use these markers:

- ✅ Yes (confirmed with evidence)
- ❌ No (not found/not available)
- ⚠️ Partial (exists but incomplete or concerning)
- ❓ Unknown (couldn't determine)
- N/A (not applicable to this marketplace type)

Always include evidence URLs where possible. Evidence strengthens findings and enables verification.
