# MCP Marketplace Security Evaluation Checklist

A comprehensive checklist for evaluating MCP marketplace security, derived from hands-on evaluation of marketplaces and lessons from package registry security research.

## How to Use This Checklist

Evaluate each marketplace against these checks. For each item:
- ✅ = Implemented/Present
- ⚠️ = Partial/Unclear
- ❌ = Missing/Not implemented
- N/A = Not applicable to this marketplace type

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

### Tier 1: Automated Checks
| Check | Status | Notes |
|-------|--------|-------|
| HTTPS | ✅/⚠️/❌ | |
| Contact info | ✅/⚠️/❌ | |
| Issue tracker | ✅/⚠️/❌ | |
| ... | | |

### Tier 2: Manual Investigation
| Check | Status | Notes |
|-------|--------|-------|
| Privacy policy | ✅/⚠️/❌ | |
| Report button | ✅/⚠️/❌ | |
| ... | | |

### Tier 3: Registry-Specific
| Check | Status | Notes |
|-------|--------|-------|
| 2FA required | ✅/⚠️/❌ | |
| Malware scanning | ✅/⚠️/❌ | |
| ... | | |

### Red Flags
- [List any red flags found]

### Security Incidents
- [Document any known past incidents]

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
