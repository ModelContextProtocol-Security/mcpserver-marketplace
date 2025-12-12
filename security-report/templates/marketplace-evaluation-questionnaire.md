# MCP Marketplace Security Evaluation Questionnaire

**Version**: 1.0 (Draft)
**Purpose**: Structured evaluation of MCP server marketplaces, registries, and directories
**Usage**: Internal evaluation + community engagement ("Please verify our findings")

---

## How to Use This Questionnaire

**For Evaluators**: Complete each section based on publicly available information. Mark items as:
- ✅ Yes (with evidence URL)
- ❌ No (not found)
- ⚠️ Partial (explain)
- ❓ Unknown (couldn't determine)
- N/A (not applicable to this marketplace type)

**For Marketplace Operators**: We've completed this based on public information. Please correct any errors and fill in unknowns. Your responses help the community make informed decisions.

---

## Part 1: Identity & Classification

### 1.1 Basic Information

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Official name of the marketplace? | | |
| Primary URL? | | |
| Who operates this marketplace? (Company/individual name) | | |
| Country/jurisdiction of operator? | | |
| Contact email for general inquiries? | | |
| Contact email for security issues? | | |
| When was this marketplace launched? | | |
| Is the marketplace source code available? | | |

### 1.2 What Type of Marketplace Is This?

Check all that apply:

| Type | Yes/No | Notes |
|------|--------|-------|
| **Directory/Aggregator** - Lists servers with links to external sources | | |
| **Registry** - Provides API for programmatic server discovery | | |
| **Code Hosting** - Hosts server source code or packages | | |
| **Hosted Execution (PaaS)** - Runs MCP servers on your infrastructure | | |
| **Client-Embedded** - Built into a specific MCP client | | |
| **Curated List** - Manually maintained list (e.g., awesome-list) | | |

### 1.3 Scale & Activity

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| How many servers are listed? (approximate) | | |
| How often is the listing updated? | | |
| How many publishers/contributors? | | |
| Is there a changelog or update history? | | |

---

## Part 2: Discovery & Access

### 2.1 How Do Users Find Servers?

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
| Is API documentation available? | | |
| Is authentication required for read access? | | |
| Is there rate limiting? | | |
| Is there an OpenAPI/Swagger spec? | | |
| Are there terms of use for the API? | | |

### 2.3 What Metadata Is Provided Per Server?

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

### 3.1 How Are Servers Delivered to Users?

| Method | Supported? | Details |
|--------|------------|---------|
| Link to external source (GitHub, etc.) | | |
| Direct download (zip, tarball) | | |
| Package manager (npm, pip, etc.) | | |
| Container image (Docker) | | |
| One-click install to client config | | |
| Hosted execution (marketplace runs the server) | | |

### 3.2 If Marketplace Hosts/Runs Servers (PaaS Model)

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| How are servers isolated from each other? | | |
| How are user credentials/secrets handled? | | |
| Are secrets stored? If so, how? | | |
| Is there audit logging of server activity? | | |
| What is the build/deployment process? | | |
| Can publishers access build logs? | | |
| Is there multi-tenant isolation documentation? | | |

---

## Part 4: Trust & Verification

### 4.1 Publisher Verification

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Is there a publisher verification process? | | |
| What is required to become a verified publisher? | | |
| Is 2FA/MFA required for publishers? | | |
| Are there different trust tiers (verified, official, etc.)? | | |
| Is the verification criteria publicly documented? | | |

### 4.2 Server Vetting

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Are servers reviewed before listing? | | |
| Is there automated security scanning? | | |
| Is there malware detection? | | |
| Is there dependency vulnerability scanning? | | |
| How quickly are flagged servers removed? | | |
| Is there typosquatting/namesquatting protection? | | |

### 4.3 Community Trust Signals

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Can users report problematic servers? | | |
| Is there a visible "Report" button? | | |
| Are there user reviews or ratings? | | |
| Is download/usage count visible? | | |
| Is "last updated" timestamp visible? | | |

---

## Part 5: Policies & Legal

### 5.1 Privacy

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Is there a privacy policy? | | |
| Privacy policy URL? | | |
| What user data is collected? | | |
| Is data shared with third parties? | | |
| Are analytics/tracking tools used? (list them) | | |
| Is there a data retention policy? | | |
| GDPR compliance claimed? | | |

### 5.2 Terms of Service

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Are there terms of service? | | |
| Terms of service URL? | | |
| What is prohibited for publishers? | | |
| What is prohibited for users? | | |
| What are the liability limitations? | | |

### 5.3 Security & Disclosure

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Is there a security policy? | | |
| Security policy/SECURITY.md URL? | | |
| Is there a vulnerability disclosure process? | | |
| Is there a bug bounty program? | | |
| Has the marketplace disclosed past security incidents? | | |
| Is there a status page for uptime/incidents? | | |

---

## Part 6: Supply Chain Security (For Code Hosting/PaaS)

### 6.1 Code Integrity

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Are packages/images signed? | | |
| Is provenance attestation provided? | | |
| Are SBOMs (Software Bill of Materials) available? | | |
| Is there reproducible build support? | | |

### 6.2 Dependency Management

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Are dependencies scanned for vulnerabilities? | | |
| Is there protection against dependency confusion? | | |
| Are lock files required/validated? | | |
| Is there notification for vulnerable dependencies? | | |

### 6.3 Update & Patch Management

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| How are security updates communicated? | | |
| Are auto-updates supported? | | |
| Can users pin to specific versions? | | |
| Is there a deprecation/EOL policy? | | |

---

## Part 7: Technical Security Posture

### 7.1 Web Security (Observable)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced? | | |
| HSTS header present? | | |
| Content-Security-Policy header? | | |
| X-Frame-Options header? | | |
| X-Content-Type-Options header? | | |
| Referrer-Policy header? | | |

### 7.2 Authentication & Authorization

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| What authentication methods are supported? | | |
| Is OAuth/OIDC used? If so, which providers? | | |
| Is session management documented? | | |
| Are API tokens scoped and time-limited? | | |

---

## Part 8: Operator Transparency

### 8.1 Business Model

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Is the service free or paid? | | |
| If paid, what is the pricing model? | | |
| What is the business model/revenue source? | | |
| Is the operator a registered business entity? | | |

### 8.2 Communication & Support

| Question | Answer | Evidence/Source |
|----------|--------|-----------------|
| Is there public documentation? | | |
| Is there a community forum/Discord/Slack? | | |
| Is there official social media presence? | | |
| What is the support response time? | | |
| Is there an issue tracker for bug reports? | | |

---

## Part 9: Evaluator's Assessment

### 9.1 Strengths
*What does this marketplace do well from a security/trust perspective?*

### 9.2 Weaknesses & Gaps
*What is missing, undocumented, or concerning?*

### 9.3 Red Flags
*Any specific concerns that users should be aware of?*

### 9.4 Recommendations
*What should the marketplace operator improve?*

### 9.5 Overall Trust Assessment
*Summary assessment for users considering this marketplace*

---

## Evaluation Metadata

| Field | Value |
|-------|-------|
| Evaluator | |
| Evaluation Date | |
| Marketplace Version/State | |
| Evidence Archive Location | |
| Sent to Operator for Review? | |
| Operator Response Received? | |
| Last Updated | |

---

## Changelog

| Date | Version | Changes |
|------|---------|---------|
| YYYY-MM-DD | 1.0 | Initial questionnaire |

