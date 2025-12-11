# MCP Marketplace Security Evaluation Prompt

## Objective

Evaluate the security posture of MCP marketplaces, registries, and directories. This prompt guides systematic security assessment across multiple tiers, capturing evidence with URLs and detailed notes.

## Prerequisites

Before evaluating, ensure you have:
1. The marketplace's main URL
2. Any known source code URLs
3. Access to web search for supplementary research

## Evaluation Process

### Tier 0: Classification

First, classify the marketplace to understand what security checks apply.

#### 0.1 Determine Marketplace Type

| Type | Description | Security Implications |
|------|-------------|----------------------|
| **code-hosting** | Hosts and runs MCP server code | Highest risk - supply chain, build security, multi-tenant isolation |
| **code-linking** | Links to GitHub repos, user runs locally | Medium risk - depends on linked repos |
| **informational** | Directory/catalog, no install mechanism | Lower risk - but can mislead users |
| **api-gateway** | Provides API to access MCP servers | High risk - centralized trust point |
| **client-embedded** | Built into an MCP client | Risk depends on client vendor |
| **hybrid** | Combination of above | Evaluate each component separately |

**Evidence to capture:**
- URL showing primary functionality
- Description of what the marketplace does

#### 0.2 Identify All Delivery Methods

**Discovery & Metadata Delivery** (how users find servers):
- [ ] Website - main URL
- [ ] Registry API - look for /docs, /api, developer documentation
- [ ] CLI tool - check npm, pip, GitHub releases
- [ ] IDE/Editor plugin - check VS Code marketplace, JetBrains, etc.
- [ ] Client integration - which MCP clients pull from this registry?
- [ ] Browser extension - check Chrome/Firefox stores

**Code/Server Delivery** (how code/functionality reaches users):
- [ ] Link to source - points to GitHub repos
- [ ] Local installation via CLI - downloads code to run locally
- [ ] Hosted execution (PaaS/SaaS) - marketplace runs the server
- [ ] Package download - npm/pip/binary
- [ ] Container image - Docker/OCI

**Key question:** Does the marketplace offer BOTH local and hosted execution? Document both models.

**Evidence to capture:**
- URLs for each delivery method found
- Note whether local, hosted, or both

#### 0.3 Check Source Accessibility

Can we audit the marketplace itself?

- [ ] Is marketplace source code public? (Search GitHub)
- [ ] Is API documentation available?
- [ ] Is it self-hostable?

**Evidence to capture:**
- Source code repo URL if found
- API docs URL
- License type

#### 0.4 Check Vendor-Hosted Server Coverage

Search the marketplace for known vendor-hosted MCP servers:
- mcp.vercel.com (Vercel)
- mcp.ramp.com (Ramp)
- Linear MCP (linear.app)
- Stripe MCP (stripe.com)
- Cloudflare MCP (cloudflare.com)
- Huggingface MCP

**Evidence to capture:**
- Which vendor-hosted servers were found (or "none")
- Whether hosted vs local servers are distinguished in UI

---

### Tier 1: Automated/Observable Checks

These can be verified through direct inspection.

#### 1.1 Basic Security

| Check | How to Verify |
|-------|---------------|
| HTTPS enforced | Visit main URL, API, all endpoints |
| Valid SSL certificate | Check cert in browser |
| No mixed content | Browser dev tools |

#### 1.2 Contact & Accountability

| Check | How to Verify |
|-------|---------------|
| Contact email | Search site, footer, about page |
| Security contact | Look for security@, SECURITY.md |
| Legal entity | Check privacy policy, terms, about page |
| Social media | Twitter/X, Discord, etc. |

#### 1.3 Issue Tracking

| Check | How to Verify |
|-------|---------------|
| Public issue tracker | Find GitHub Issues or equivalent |
| Issues actively managed | Check open/closed ratio, response times |
| Security issues handled | Search for security-related issues |

#### 1.4 Transparency

| Check | How to Verify |
|-------|---------------|
| Server count visible | Check homepage, API |
| Last updated timestamps | Check individual listings |
| Provenance visible | Is source/author shown per server? |
| Official vs third-party distinction | Look for badges, labels |

**Evidence format for each check:**
```
- url: "https://example.com/contact"
  description: "Contact page - found email contact@example.com, Discord invite link"
```

---

### Tier 2: Manual Investigation

These require reading documentation and policies.

#### 2.1 Legal & Privacy

| Check | What to Look For |
|-------|-----------------|
| Privacy policy | Find /privacy, read for company name, data practices |
| Legal entity | Company name, jurisdiction |
| Data collection | What is collected? |
| Third-party sharing | Ad networks, analytics, affiliates |
| Excessive tracking | Keystroke, mouse tracking (unusual for dev tools) |
| Terms of service | Find /terms |

#### 2.2 Publisher Requirements

| Check | What to Look For |
|-------|-----------------|
| Publisher verification | How to submit a server? What's required? |
| Verification criteria | What does "verified" badge mean? |
| Publisher identity | Real identity or just email? |

#### 2.3 Moderation & Reporting

| Check | What to Look For |
|-------|-----------------|
| Report button | Can users flag problematic servers? |
| Moderation policy | Public content policy? |
| Takedown process | How is malicious content removed? |
| Response time | Any SLA for security issues? |

#### 2.4 Security Documentation

| Check | What to Look For |
|-------|-----------------|
| Security page | /security or security docs |
| Vulnerability disclosure | Responsible disclosure process |
| Past incidents | Postmortems, advisories |
| Certifications | SOC2, ISO27001, etc. |

**Evidence format:**
```
- url: "https://example.com/privacy"
  description: "Privacy policy - operated by Example Inc., collects usage data, shares with 'marketing partners'"
```

---

### Tier 3: Registry-Specific Checks (if code-hosting)

Only apply these if the marketplace hosts/runs code.

#### 3.1 Publisher Security

| Check | What to Look For |
|-------|-----------------|
| 2FA required | Check registration docs |
| Hardware key support | WebAuthn/FIDO |
| OAuth integration | GitHub OAuth, etc. |
| Token management | Do tokens expire? Scopes? |

#### 3.2 Malware & Code Scanning

| Check | What to Look For |
|-------|-----------------|
| Automated scanning | Security scanning before publish? |
| Scan results visible | Is there a security field in API/UI? |
| Vulnerability flagging | CVEs shown? |
| Dependency scanning | Are deps checked? |

#### 3.3 Namespace & Naming

| Check | What to Look For |
|-------|-----------------|
| Namespace structure | owner/name format? |
| Typosquatting protection | Reserved names? Detection? |
| Name reuse policy | Can deleted names be reused? |

#### 3.4 Hosted Execution Security (PaaS)

If marketplace runs servers:

| Check | What to Look For |
|-------|-----------------|
| Multi-tenant isolation | Can servers access each other? |
| Secret storage | How are credentials stored? |
| Build isolation | Can builds access other builds? |
| Network isolation | Outbound request restrictions? |
| Resource limits | CPU/memory limits? |
| Credential injection | How are user creds passed? |
| Audit logging | What's logged? Who can access? |
| Data residency | Where does execution happen? |

---

### Tier 4: GitHub/Source Repository Checks

If marketplace has public source code.

#### 4.1 Repository Security

| Check | How to Verify |
|-------|---------------|
| SECURITY.md | Check repo root |
| Security advisories | GitHub Security tab |
| Branch protection | Is main protected? |
| Signed commits | GPG signatures? |

#### 4.2 Organization Verification

| Check | How to Verify |
|-------|---------------|
| GitHub org verified | Look for verified badge |
| Verified domain matches | Does domain match claimed identity? |

---

### Tier 5: Ecosystem & Third-Party Analysis

External research and data.

#### 5.1 Secret Leak Analysis

If possible, analyze repos indexed by the marketplace:
- Use GitGuardian, TruffleHog, or similar
- Compare to baseline (~4.6% for public repos)
- Note types of secrets leaked

#### 5.2 Security Research

Search for:
- Past vulnerabilities (CVE databases, security blogs)
- Security researcher disclosures
- Incident response history

**Useful searches:**
- `"[marketplace name]" vulnerability`
- `"[marketplace name]" security`
- `"[marketplace name]" CVE`
- `site:blog.gitguardian.com "[marketplace name]"`

#### 5.3 Third-Party Integrations

Check privacy policy and site for:
- Analytics (Google Analytics, etc.)
- Ad networks (unusual for B2B dev tools)
- Payment processors

---

## Evidence Recording

For every check, capture:

```yaml
evidence:
  - url: "https://example.com/path"
    description: "What was found, relevant quotes, why it matters"
  - url: "https://github.com/org/repo/security"
    description: "No SECURITY.md found - vulnerability reporting process unclear"
  - url: "https://blog.example.com/incident-report"
    description: "June 2025 incident - path traversal vuln, fixed in 48 hours"
```

**Include:**
- Direct URLs to evidence (not just homepage)
- Specific quotes or observations
- Dates when relevant (incidents, last updated)
- Negative findings ("No X found")

---

## Red Flags to Highlight

### Critical Red Flags
- No HTTPS or invalid certificate
- No contact information
- No way to report malicious content
- Arbitrary code execution without sandboxing
- No authentication for publishing

### Significant Red Flags
- "Verified" badge with undocumented criteria
- Security scan field that's always empty/null ("ghost feature")
- Excessive user tracking (keystroke, mouse)
- Data sharing with ad networks
- No SECURITY.md or disclosure policy
- Hundreds of unaddressed issues
- No 2FA for publishers

---

## Output Format

Generate a markdown file with this structure:

```markdown
---
title: "Marketplace Name"
url: "https://example.com"
source_code_url: "https://github.com/org/repo"
type: "code-hosting"
operator: "Company Name"
contact_email: "contact@example.com"
server_count: "1,000+"
last_evaluated: "YYYY-MM-DD"
evidence:
  - url: "..."
    description: "..."
---

# Marketplace Name

## Overview
[1-2 paragraph description]

## Features
[Bullet list of capabilities]

## Security

### Tier 0: Classification
[Type, delivery methods, source accessibility, server coverage]

### Tier 1: Automated Checks
[Table of checks with status and notes]

### Tier 2: Manual Investigation
[Table of checks with status and notes]

### Tier 3: Registry-Specific (if applicable)
[Table of checks with status and notes]

### Tier 4: GitHub Checks (if applicable)
[Table of checks with status and notes]

### Tier 5: Ecosystem Analysis
[Secret leak rate, past incidents, third-party tracking]

### Security Incidents
[Documented incidents with dates, description, resolution time]

### Delivery Method Security
[Security notes for each delivery method: website, API, CLI, hosted execution]

### Security Score Summary
**Strengths:**
- [List]

**Weaknesses:**
- [List]

**Overall Assessment:**
[1-2 paragraph assessment]

## Notes
[Legal entity, business model, key links, data collection practices]
```

---

## Single-Shot System Prompt

For use with web-enabled AI assistants:

```
You are evaluating the security posture of an MCP marketplace/registry.

For the marketplace at [URL], perform a comprehensive security evaluation:

1. CLASSIFY: Determine type (code-hosting/code-linking/informational/hybrid), all delivery methods (website/API/CLI/hosted execution), source accessibility, vendor-hosted server coverage.

2. CHECK (with evidence URLs for each):
   - Tier 1: HTTPS, contact info, issue tracker, transparency
   - Tier 2: Privacy policy (legal entity, tracking, ad networks), publisher verification, report button, security docs
   - Tier 3 (if code-hosting): 2FA, malware scanning, namespace, hosted execution isolation
   - Tier 4 (if has GitHub): SECURITY.md, org verification
   - Tier 5: Search for past vulnerabilities, security research

3. DOCUMENT: For each finding, provide the specific URL and what you found. Include negative findings ("No SECURITY.md found").

4. FLAG: Red flags (critical and significant), ghost features (exist but not implemented).

5. SUMMARIZE: Strengths, weaknesses, overall assessment.

Output as structured markdown with YAML frontmatter.
```

---

## References

- [marketplace-security-checklist.md](../patterns/marketplace-security-checklist.md) - Full checklist with all tiers
- [LESSONS-FROM-PACKAGE-REGISTRIES.md](../research/LESSONS-FROM-PACKAGE-REGISTRIES.md) - PyPI/npm security lessons
- [evaluation-criteria.md](../patterns/evaluation-criteria.md) - Evaluation criteria
- [trust-signals.md](../patterns/trust-signals.md) - Trust signal hierarchy
