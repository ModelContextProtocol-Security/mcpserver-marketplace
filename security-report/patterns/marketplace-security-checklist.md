# MCP Marketplace Security Evaluation Checklist

A comprehensive checklist for evaluating MCP marketplace security, derived from hands-on evaluation of marketplaces and lessons from package registry security research.

## How to Use This Checklist

Evaluate each marketplace against these checks. For each item:
- ✅ = Implemented/Present
- ⚠️ = Partial/Unclear
- ❌ = Missing/Not implemented
- N/A = Not applicable to this marketplace type

---

## Tier 0: Marketplace Classification

Before evaluating security, classify the marketplace type and delivery methods.

### 0.1 Marketplace Type

Determine the primary function of the marketplace:

| Type | Description | Example | Security Implications |
|------|-------------|---------|----------------------|
| **code-hosting** | Hosts and runs MCP server code | Smithery, mcp.run | Highest risk - supply chain attacks, build security |
| **code-linking** | Links to GitHub repos, user runs locally | mcp.so, awesome-mcp-servers | Medium risk - depends on linked repos |
| **informational** | Directory/catalog, no install mechanism | Blog lists, curated lists | Lower risk - but can mislead users |
| **api-gateway** | Provides API to access MCP servers | Enterprise gateways | High risk - centralized trust point |
| **client-embedded** | Built into an MCP client | Claude Desktop directory | Risk depends on client vendor |
| **hybrid** | Combination of above | Smithery (hosts + API + web) | Evaluate each component |

### 0.2 Delivery Methods

Check ALL ways users can access the marketplace:

#### Discovery & Metadata Delivery
How users find and get information about MCP servers:

| Delivery Method | How to Find | What to Check |
|-----------------|-------------|---------------|
| **Website** | Visit main URL | Standard web security checks |
| **Registry API** | Check /docs, /api, developer docs | API security, authentication, what data is exposed |
| **CLI tool** | Check for npm/pip package, GitHub releases | Package signing, update mechanism |
| **IDE/Editor plugin** | Check VS Code marketplace, JetBrains, etc. | Plugin security, permissions |
| **Client integration** | Check if other clients pull from this registry | How clients authenticate, what data they get |
| **Browser extension** | Check Chrome/Firefox stores | Extension permissions, update mechanism |

#### Code/Server Delivery
How the actual MCP server code/functionality reaches users:

| Delivery Method | Description | Security Implications |
|-----------------|-------------|----------------------|
| **Link to source** | Points to GitHub repo, user clones/installs manually | User responsible for vetting code, highest user control |
| **Local installation via CLI** | CLI tool downloads and installs server to run locally | Package integrity, but user controls execution environment |
| **Package download** | Delivers installable package (npm, pip, binary) | Package integrity, signing, supply chain |
| **Hosted execution (PaaS/SaaS)** | Marketplace runs the MCP server, user connects via URL | Marketplace responsible for isolation, multi-tenancy security |
| **Container image** | Delivers Docker/OCI image | Image signing, base image security, registry trust |
| **Source bundle** | Delivers source code archive | Integrity verification, no build-time attacks |

**Local Installation vs Hosted Execution - Key Differences:**

| Aspect | Local Installation | Hosted Execution (PaaS) |
|--------|-------------------|------------------------|
| **Where code runs** | User's machine | Marketplace infrastructure |
| **Who controls execution** | User | Marketplace operator |
| **Credential handling** | Stays on user's machine (env vars) | Passed to marketplace servers |
| **Risk profile** | Lower - user controls environment | Higher - trust marketplace isolation |
| **Visibility** | User can inspect/audit | Opaque - can't see what runs |
| **Example** | Smithery CLI local install | Smithery `server.smithery.ai/{name}/mcp` |

**Important:** Some marketplaces (like Smithery) offer BOTH models. Users should understand which model they're using - a "Remote" or "Hosted" label typically indicates PaaS execution.

**Hosted Execution (PaaS/SaaS) - Special Considerations:**

When a marketplace runs MCP servers on behalf of users (like Smithery's `server.smithery.ai/{name}/mcp`):

| Check | Why It Matters |
|-------|----------------|
| **Multi-tenant isolation** | Can one server access another's data/secrets? |
| **Secret storage** | How are API keys/credentials stored? (June 2025 Smithery vuln exposed secrets) |
| **Build isolation** | Can malicious build configs access other builds? |
| **Network isolation** | Can hosted servers make arbitrary outbound requests? |
| **Resource limits** | CPU/memory/network limits per server? |
| **Execution sandboxing** | What can hosted code access? (filesystem, env vars, etc.) |
| **Credential injection** | How are user credentials passed to hosted servers? |
| **Audit logging** | Are server actions logged? Who can access logs? |
| **Data residency** | Where does execution happen? (region, compliance) |

**Important:** A marketplace may have different security postures across delivery methods. The website might be secure while the API lacks authentication. The registry might be trustworthy but hosted execution might be vulnerable.

### 0.3 Source Accessibility

Can we audit the marketplace itself?

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **Marketplace source code public** | Search GitHub for the marketplace's own code | Can audit for vulnerabilities |
| **API specification public** | Look for OpenAPI/Swagger docs | Understand data exposure |
| **Data format documented** | Check if schema is published | Understand what's transmitted |
| **Self-hostable** | Can users run their own instance? | Independence from central operator |

**Examples:**
- mcp.so: Source at github.com/chatmcp/mcpso ✅
- Smithery: Partial - CLI is open source, platform is not ⚠️
- Claude Desktop directory: Closed source ❌

### 0.4 Server Coverage

Does the marketplace include vendor-hosted MCP servers?

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **Lists vendor-hosted servers** | Search for mcp.vercel.com, mcp.ramp.com, etc. | These are often the safest option |
| **Distinguishes hosted vs local** | Are hosted servers marked differently? | Users should know what they're getting |
| **Prioritizes official hosted** | Are vendor-hosted servers shown first/prominently? | Guide users to safest options |

**Known vendor-hosted MCP servers to search for:**
- mcp.vercel.com (Vercel)
- mcp.ramp.com (Ramp)
- Huggingface.co/mcp (Hugging Face)
- Linear MCP (linear.app)
- Stripe MCP (stripe.com)
- Cloudflare MCP (cloudflare.com)

**Critical Gap:** Most marketplaces only list GitHub repos, ignoring vendor-hosted servers. This drives users toward third-party code instead of official hosted options.

### 0.5 Classification Template

```markdown
## Marketplace Classification

**Type:** [code-hosting | code-linking | informational | api-gateway | client-embedded | hybrid]

**Discovery & Metadata Delivery:**
- [ ] Website: [URL]
- [ ] Registry API: [endpoint]
- [ ] CLI: [package name]
- [ ] IDE plugin: [marketplace link]
- [ ] Client integration: [which clients]
- [ ] Browser extension: [store link]

**Code/Server Delivery:**
- [ ] Link to source: [yes/no - links to GitHub/GitLab]
- [ ] Local installation via CLI: [yes/no - CLI installs to run locally]
- [ ] Package download: [npm/pip/binary]
- [ ] Hosted execution (PaaS/SaaS): [URL pattern, e.g., server.example.com/{name}]
- [ ] Container image: [registry URL]
- [ ] Source bundle: [download mechanism]

**Note:** If marketplace offers BOTH local and hosted, document both and their security differences.

**Source Accessibility:**
- Marketplace source code: [URL or "closed"]
- API docs: [URL or "none"]
- Self-hostable: [yes/no]

**Server Coverage:**
- Lists vendor-hosted servers: [yes/no]
- Distinguishes hosted vs local: [yes/no]
- Vendor-hosted servers found: [list or "none"]
```

---

## Tier 1: Automated/Observable Checks

These can be verified through web inspection, API calls, and automated tools.

### 1.1 Basic Security

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **HTTPS enforced** | Visit all URLs, check for redirects | Prevents MITM attacks, basic hygiene |
| **Valid SSL certificate** | Check cert validity, issuer | Expired/invalid certs indicate neglect |
| **No mixed content** | Browser dev tools | HTTP resources on HTTPS pages leak data |

### 1.2 Contact & Accountability

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **Contact email visible** | Search site for email | Users need way to report issues |
| **Security contact** | Look for security@, SECURITY.md | Dedicated channel for vuln reports |
| **Physical address/entity** | Check privacy policy, about page | Accountability, legal jurisdiction |
| **Social media presence** | Look for Twitter/X, Discord, etc. | Alternative contact channels |

### 1.3 Issue Tracking

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **Public issue tracker** | Find GitHub Issues or equivalent | Transparency about known problems |
| **Issues actively managed** | Check open/closed ratio, response times | Indicates maintenance level |
| **Security issues handled** | Search for security-related issues | Shows security responsiveness |

### 1.4 Transparency

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **Server count visible** | Check homepage/API | Indicates scale and activity |
| **Last updated timestamps** | Check individual listings | Shows freshness of data |
| **Provenance visible** | Check if source/author shown per server | Users need to assess trust |
| **Official vs third-party distinction** | Look for badges, labels | Prevents confusion about official status |

### 1.5 API Security (if applicable)

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **API uses HTTPS** | Test API endpoints | Protects data in transit |
| **Rate limiting** | Test rapid requests | Prevents abuse, DoS |
| **Authentication for writes** | Check if publishing requires auth | Prevents unauthorized submissions |

---

## Tier 2: Manual Investigation

These require deeper inspection of documentation, policies, and behavior.

### 2.1 Legal & Privacy

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **Privacy policy exists** | Find /privacy or footer link | Legal requirement, transparency |
| **Legal entity identified** | Read privacy policy for company name | Accountability |
| **Data collection disclosed** | Read what data is collected | Users should know what's tracked |
| **Third-party sharing disclosed** | Check for ad networks, analytics | Hidden data sharing is a red flag |
| **Excessive tracking** | Look for keystroke/mouse tracking | Unusual for dev tools |
| **Terms of service** | Find /terms or footer link | Defines relationship and liability |

### 2.2 Publisher Requirements

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **Publisher verification documented** | Read docs for submission process | Shows rigor of vetting |
| **Verification criteria public** | Can users understand what "verified" means? | Prevents meaningless badges |
| **Publisher identity required** | Check if real identity or just email | Accountability for publishers |

### 2.3 Moderation & Reporting

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **Report button exists** | Look for "report" on listings | Users need way to flag problems |
| **Moderation policy public** | Search for content policy | Shows what's not allowed |
| **Takedown process documented** | Check if removal process exists | Important for malicious content |
| **Response time SLA** | Look for committed response times | Indicates seriousness |

### 2.4 Security Documentation

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **Security page exists** | Look for /security or security docs | Shows security is prioritized |
| **Vulnerability disclosure policy** | Look for responsible disclosure info | Researchers need clear process |
| **Past incidents disclosed** | Search for postmortems, advisories | Transparency builds trust |
| **Security certifications** | Look for SOC2, ISO27001, etc. | Third-party validation |

### 2.5 Verification Badges

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **Badge criteria documented** | Can users find what badges mean? | Undocumented badges are meaningless |
| **Badge process documented** | Can publishers apply for verification? | Shows systematic approach |
| **Multiple badge types** | Official vs verified vs community? | Nuanced trust levels |

---

## Tier 3: Registry-Specific Checks

For marketplaces that host code or run servers (not just link to GitHub).

### 3.1 Publisher Security

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **2FA required for publishers** | Check registration docs | Prevents account takeover |
| **2FA hardware key support** | Check for WebAuthn/FIDO | Strongest auth protection |
| **OAuth/SSO integration** | Check login options | GitHub OAuth is common |
| **Token management** | Check if API tokens expire | Long-lived tokens are risky |
| **Token scopes** | Are permissions granular? | Least privilege |

### 3.2 Malware & Code Scanning

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **Automated scanning on upload** | Check docs, security page | Catches malware before publish |
| **Scanning results visible** | Is there a security scan field? | Transparency |
| **Known vulnerability flagging** | Are CVEs/advisories shown? | Users need to know risks |
| **Dependency scanning** | Are dependencies checked? | Supply chain security |

### 3.3 Namespace & Naming

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **Namespace structure** | Check naming convention (owner/name) | Prevents confusion |
| **Typosquatting detection** | Try registering similar names | #1 attack vector for 10 years |
| **Reserved names** | Are official vendor names protected? | Prevents impersonation |
| **Name reuse policy** | Can deleted names be reused? | Prevents revival hijack |

### 3.4 Build & Runtime Security

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **Build isolation** | Check if builds are sandboxed | Prevents cross-contamination |
| **Runtime sandboxing** | Are hosted servers isolated? | Limits blast radius |
| **Install script policy** | Are arbitrary scripts allowed? | Major attack vector |
| **Permission system** | Are capabilities declared/enforced? | Least privilege |

### 3.5 Integrity & Provenance

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **Package signing** | Are packages cryptographically signed? | Integrity verification |
| **Provenance attestation** | Is there SLSA or similar? | Proves build origin |
| **Immutability policy** | Can published versions be modified? | Prevents supply chain attacks |
| **Audit logging** | Are changes logged? | Accountability |

---

## Tier 4: GitHub/Source Repository Checks

For marketplaces with public source code or GitHub integration.

### 4.1 Repository Security

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **SECURITY.md exists** | Check repo root | Vuln reporting process |
| **Security advisories published** | Check Security tab | Transparency about vulns |
| **Branch protection** | Check if main is protected | Prevents unauthorized changes |
| **Signed commits** | Check commit signatures | Integrity |

### 4.2 Organization Verification

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **GitHub org verified** | Look for verified badge on org | Domain ownership confirmed |
| **Verified domain matches** | Does badge domain match claimed identity? | Prevents impersonation |
| **Org 2FA required** | Check org settings (if visible) | All members secured |

### 4.3 Code Quality Indicators

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **CI/CD pipeline** | Check for GitHub Actions, etc. | Automated testing |
| **Code scanning enabled** | Check for CodeQL, Dependabot | Automated vuln detection |
| **Dependency updates** | Check Dependabot PRs | Shows maintenance |

---

## Tier 5: Ecosystem & Third-Party Analysis

External data sources and research findings.

### 5.1 Secret Leak Analysis

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **Secret leak rate** | Use GitGuardian, TruffleHog on indexed repos | Indicates code hygiene |
| **Leaked secret types** | What kinds of secrets are exposed? | API keys, tokens, passwords |
| **Comparison to baseline** | Is rate higher than average (~4.6%)? | Context for findings |

**Example:** GitGuardian found 5.2% of Smithery-indexed repos leaked secrets (202/3829 repos).

### 5.2 Security Research

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **Past vulnerabilities** | Search CVE databases, security blogs | History of issues |
| **Researcher engagement** | Has platform worked with researchers? | Bug bounty, disclosures |
| **Incident response history** | How fast were past issues fixed? | Indicates maturity |

### 5.3 Third-Party Integrations

| Check | How to Verify | Why It Matters |
|-------|---------------|----------------|
| **Analytics/tracking** | Check for Google Analytics, etc. | Privacy implications |
| **Ad networks** | Check privacy policy | Unusual for B2B dev tools |
| **Payment processors** | Who handles payments? | PCI compliance |

---

## Red Flags

Immediate concerns that should lower trust significantly:

### Critical Red Flags
- ❌ No HTTPS or invalid certificate
- ❌ No contact information at all
- ❌ No way to report malicious content
- ❌ Arbitrary code execution without sandboxing
- ❌ No authentication for publishing
- ❌ Names can be freely deleted and reused

### Significant Red Flags
- ⚠️ "Verified" badge with no documented criteria
- ⚠️ Security scan field exists but is always empty/null
- ⚠️ Excessive user tracking (keystroke, mouse movement)
- ⚠️ Data sharing with ad networks
- ⚠️ No SECURITY.md or vulnerability disclosure process
- ⚠️ Issue tracker with hundreds of unaddressed issues
- ⚠️ No 2FA requirement for publishers
- ⚠️ Past critical vulnerabilities with slow response

### Ghost Features
Features that exist in UI/API but aren't actually implemented:
- Security scan field that's always null
- Verification badge with no verification process
- Report button that doesn't work
- Terms of service that can't be found

---

## Best Practices to Look For

Signs of a security-mature marketplace:

### Gold Standard
- ✅ Mandatory 2FA with hardware key support for publishers
- ✅ Automated malware scanning before publication
- ✅ Documented, auditable verification process
- ✅ SECURITY.md with clear disclosure policy
- ✅ Published security advisories and incident postmortems
- ✅ <24 hour response time for security issues
- ✅ Namespace protection against typosquatting
- ✅ Package signing and provenance attestation
- ✅ Runtime sandboxing for hosted servers
- ✅ Public security metrics dashboard

### Good
- ✅ 2FA available (even if not mandatory)
- ✅ Some automated scanning
- ✅ Contact email and issue tracker
- ✅ Privacy policy with reasonable data practices
- ✅ Verified GitHub organization
- ✅ Active issue management

### Minimum Acceptable
- ✅ HTTPS everywhere
- ✅ Some way to contact operators
- ✅ Legal entity identified
- ✅ Basic publisher authentication

---

## Evaluation Template

Use this template when evaluating a marketplace:

```markdown
## [Marketplace Name] Security Evaluation

**Date:** YYYY-MM-DD
**Evaluator:** [Name]
**URL:** [URL]

### Summary
[1-2 sentence overall assessment]

### Tier 0: Classification

**Type:** [code-hosting | code-linking | informational | api-gateway | client-embedded | hybrid]

**Discovery & Metadata Delivery:**
- [ ] Website: [URL]
- [ ] Registry API: [endpoint or "none"]
- [ ] CLI: [package name or "none"]
- [ ] IDE plugin: [marketplace link or "none"]
- [ ] Client integration: [which clients or "none"]
- [ ] Browser extension: [store link or "none"]

**Code/Server Delivery:**
- [ ] Link to source: [yes/no]
- [ ] Local installation via CLI: [yes/no]
- [ ] Package download: [format or "none"]
- [ ] Hosted execution (PaaS/SaaS): [URL pattern or "none"]
- [ ] Container image: [registry or "none"]
- Dual model (local + hosted): [yes/no]

**Source Accessibility:**
- Marketplace source code: [URL or "closed source"]
- API docs: [URL or "none"]
- Self-hostable: [yes/no]

**Server Coverage:**
- Lists vendor-hosted servers: [yes/no]
- Distinguishes hosted vs local: [yes/no]
- Vendor-hosted servers found: [list any found, or "none"]

### Tier 1: Automated Checks
| Check | Status | Notes |
|-------|--------|-------|
| HTTPS | ✅/⚠️/❌ | |
| Contact info | ✅/⚠️/❌ | |
| Issue tracker | ✅/⚠️/❌ | |
| Provenance visible | ✅/⚠️/❌ | |
| Official/third-party distinction | ✅/⚠️/❌ | |
| Timestamps | ✅/⚠️/❌ | |

### Tier 2: Manual Investigation
| Check | Status | Notes |
|-------|--------|-------|
| Privacy policy | ✅/⚠️/❌ | Legal entity: |
| Report button | ✅/⚠️/❌ | |
| Moderation policy | ✅/⚠️/❌ | |
| Security docs | ✅/⚠️/❌ | |
| Badge criteria documented | ✅/⚠️/❌ | |

### Tier 3: Registry-Specific (if code-hosting)
| Check | Status | Notes |
|-------|--------|-------|
| 2FA required | ✅/⚠️/❌ | |
| Malware scanning | ✅/⚠️/❌ | |
| Namespace structure | ✅/⚠️/❌ | |
| Build isolation | ✅/⚠️/❌ | |
| Package signing | ✅/⚠️/❌ | |

### Tier 4: GitHub/Source Checks (if applicable)
| Check | Status | Notes |
|-------|--------|-------|
| SECURITY.md | ✅/⚠️/❌ | |
| GitHub org verified | ✅/⚠️/❌ | Domain: |
| Security advisories | ✅/⚠️/❌ | |

### Tier 5: Ecosystem Analysis
| Check | Status | Notes |
|-------|--------|-------|
| Secret leak rate | | % of indexed repos |
| Past vulnerabilities | | CVEs, incidents |
| Excessive tracking | ✅/⚠️/❌ | |

### Delivery Method Security

**Website:**
- [Security notes for web interface]

**API:**
- [Security notes for API - auth, rate limiting, HTTPS]

**CLI:**
- [Security notes for CLI - signing, updates]

**Client Integration:**
- [Which clients use this, how they authenticate]

### Red Flags
- [List any red flags found]

### Security Incidents
- [Document any known past incidents with dates and resolution times]

### Overall Assessment
[Detailed assessment with strengths and weaknesses]
```

---

## References

- [LESSONS-FROM-PACKAGE-REGISTRIES.md](../research/LESSONS-FROM-PACKAGE-REGISTRIES.md) - PyPI/npm security lessons
- [evaluation-criteria.md](./evaluation-criteria.md) - Detailed evaluation criteria
- [trust-signals.md](./trust-signals.md) - Trust signal hierarchy
- [checks.md](./checks.md) - Original checklist

## Contributing

**Found something we should check for?** Submit a PR or file an issue with:
1. What to check
2. Why it matters for security
3. How to verify it
4. Example of good vs bad
