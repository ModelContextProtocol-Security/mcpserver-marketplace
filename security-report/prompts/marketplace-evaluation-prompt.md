# MCP Marketplace Security Evaluation Prompt

## Objective

To perform a comprehensive security evaluation of an MCP (Model Context Protocol) marketplace, registry, or directory. The focus is on evaluating the marketplace's security posture, transparency, trust mechanisms, and supply chain security.

## Inputs

1. **Marketplace Name**: [Name of the MCP Marketplace]
2. **Primary URL**: [Main URL for the marketplace]
3. **Source Code URL**: [URL for the marketplace source code, if available]

## Tools Available

- `tier1_audit.py` - Automated security checks (HTTPS, headers, DNS, policy endpoints)
- Web browser/fetch - Manual investigation of pages
- GitHub/source code review - If source is available

## Task

Produce a detailed security evaluation report in markdown format using the `security-report/templates/marketplace-evaluation-unified-template.md` template. Your analysis should be based on:

1. Automated tool output (`tier1_audit.py`)
2. Manual investigation of the website
3. Review of documentation, policies, and source code (if available)
4. Web searches for security incidents or research about the marketplace

---

## Evaluation Process

### Phase 1: Automated Checks (Tier 1)

Run the automated audit tool and capture results:

```bash
python3 security-report/tools/tier1_audit.py [MARKETPLACE_URL]
```

This provides:
- HTTP status and redirect chain
- Security headers (HSTS, CSP, XFO, XCTO, etc.)
- TLS certificate details
- DNS records and provider hints
- Policy endpoint availability (/privacy, /terms, /security, etc.)
- API endpoint discovery (/api, /docs, /swagger, etc.)
- Social/contact links
- Mixed content detection

Populate Part 7 (Technical Security Posture) with these results.

### Phase 2: Classification (Tier 0)

Determine the marketplace type by investigating:

1. **What type of marketplace is this?**
   - Directory/Aggregator (links to external sources)
   - Registry (programmatic API for discovery)
   - Code Hosting (hosts packages/code)
   - Hosted Execution / PaaS (runs servers for users)
   - Client-Embedded (built into an MCP client)
   - Curated List (manually maintained)

2. **How do users discover servers?**
   - Website, API, CLI, IDE plugin, client integration

3. **How are servers delivered?**
   - External links, downloads, package managers, containers, hosted execution

Populate Parts 1-3 with these findings.

### Phase 3: Trust & Policy Investigation (Tier 2)

Manually investigate:

1. **Privacy Policy** - Read and summarize data collection practices
2. **Terms of Service** - Check for prohibited activities, liability
3. **Security Policy** - Look for SECURITY.md, vulnerability disclosure
4. **Publisher Verification** - How do publishers get verified? What's required?
5. **Server Vetting** - Are servers reviewed before listing?
6. **Community Trust Signals** - Report buttons, ratings, reviews

Populate Parts 4-5 with these findings.

### Phase 4: Supply Chain Security (Tier 3)

If the marketplace hosts code or runs servers:

1. **Code Integrity** - Package signing, provenance, SBOMs
2. **Dependency Management** - Vulnerability scanning, lock files
3. **Build Security** - Isolation between publishers, secret handling
4. **Update Management** - Security update communication

Populate Part 6 with these findings. Mark N/A if directory-only.

### Phase 5: Security Incident Research

Search for known security incidents:

```
"[marketplace name]" + "vulnerability" OR "security issue" OR "data breach" OR "CVE"
```

Check:
- Security blogs (GitGuardian, Snyk, etc.)
- GitHub security advisories
- News articles
- The marketplace's own disclosure history

Populate Part 9 (Security Incidents) with any findings.

### Phase 6: Vendor-Hosted Coverage Test

Search the marketplace for known vendor-hosted MCP servers:

| Pattern | Example |
|---------|---------|
| Vercel | mcp.vercel.com, vercel + mcp |
| Cloudflare | cloudflare + mcp |
| Stripe | stripe + mcp |
| Linear | linear + mcp |
| HuggingFace | huggingface.co/mcp |

Document whether the marketplace lists vendor-hosted servers or only GitHub repos.

Populate Part 3.5 with results.

### Phase 7: Assessment

Based on all findings, write:

1. **Strengths** - What the marketplace does well
2. **Weaknesses & Gaps** - What's missing or undocumented
3. **Red Flags** - Specific concerns users should know
4. **Recommendations** - What the operator should improve
5. **Overall Trust Assessment** - Summary for users

---

## Report Structure

Use the unified template structure:

```
---
[YAML Frontmatter]
---

## Overview
## Features Summary
## Part 1: Identity & Classification
## Part 2: Discovery & Access
## Part 3: Server Delivery Model
## Part 4: Trust & Verification
## Part 5: Policies & Legal
## Part 6: Supply Chain Security
## Part 7: Technical Security Posture
## Part 8: Operator Transparency
## Part 9: Security Incidents
## Part 10: Delivery Method Security
## Part 11: Evaluator Assessment
## Evaluation Metadata
## Audit Evidence
## Changelog
```

---

## Marking Guide

Use these markers consistently:

- ✅ Yes (confirmed with evidence URL)
- ❌ No (not found/not available)
- ⚠️ Partial (exists but incomplete or concerning)
- ❓ Unknown (couldn't determine)
- N/A (not applicable to this marketplace type)

**Always include evidence URLs** where possible.

---

## Important Guidelines

1. **Be thorough but honest** - If you can't find information, mark it as Unknown, not No
2. **Cite evidence** - Every claim should have a URL or source
3. **Don't assume** - If documentation doesn't exist, note it as missing
4. **Consider the user** - Write for someone deciding whether to use this marketplace
5. **Be balanced** - Note both strengths and weaknesses
6. **Check for incidents** - Security history matters
7. **Note limitations** - State what you couldn't verify (e.g., no dynamic testing)

---

## Single-Shot System Prompt

You are a principal security researcher tasked with evaluating an MCP marketplace.

**Marketplace:** [Marketplace Name]
**URL:** [Primary URL]
**Source Code:** [Source Code URL or "Not available"]

Produce a detailed markdown security report using the `security-report/templates/marketplace-evaluation-unified-template.md` template structure.

Your evaluation must include:

1. **Automated audit results** from `tier1_audit.py` (or equivalent checks)
2. **Classification** of the marketplace type and delivery model
3. **Trust & Policy analysis** including privacy policy, ToS, and security policy review
4. **Supply chain security** assessment if the marketplace hosts code or runs servers
5. **Security incident research** - search for any known vulnerabilities or breaches
6. **Vendor-hosted coverage test** - does it list official vendor MCP servers?
7. **Assessment** with strengths, weaknesses, red flags, and recommendations
8. **Limitations** noting what couldn't be verified

Use the marking guide (✅ ❌ ⚠️ ❓ N/A) and cite evidence URLs throughout.

Begin the evaluation now.

---

## Example Evaluations

For reference, see these completed evaluations:

- `security-report/datasets/mcp-marketplace-dataset/smithery-playground.md` - Comprehensive (code-hosting/PaaS)
- `security-report/datasets/mcp-marketplace-dataset/docker-mcp-catalog.md` - Comprehensive (curated catalog)
- `security-report/datasets/mcp-marketplace-dataset/mcp.so.md` - Comprehensive (directory)
