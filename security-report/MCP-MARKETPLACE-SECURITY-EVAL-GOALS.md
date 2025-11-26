# MCP Marketplace Security Evaluation – Goals Document (v0.3)

**Owner**: Kurt Seifried, Chief Innovation Officer, Cloud Security Alliance
**Last Updated**: 2025-11-25
**Primary Folder**: [https://drive.google.com/drive/folders/1pGOYZDOOnm93QGe3fGWtLRPP_H3scj-L](https://drive.google.com/drive/folders/1pGOYZDOOnm93QGe3fGWtLRPP_H3scj-L)
**Project**: MCP Marketplace Security Evaluation
**Parent Program**: CSA MCP Security

---

## The Core Question

> **"How do I ultimately safely get an MCP server?"**

This question drives everything. Every evaluation criterion, every deliverable, every piece of guidance should help answer this for users, administrators, and decision makers.

---

## Context: The "Wild West" Phase

The MCP marketplace ecosystem is currently in a **pre-incident phase** similar to npm/PyPI before major security incidents drove change. Key facts:

- **6,480+ MCP servers** listed across various marketplaces
- **No standard verification processes** for server authenticity
- **Logo misuse is common** (vendors' logos used without authorization)
- **Provenance information is regressing** (some clients removed details links)
- **AI agents recommending servers** have highest reach but lowest security mechanisms

We have a window to establish security norms **proactively** before bad actors and incidents shape the narrative.

### Lessons from Package Registries

PyPI and npm have 10 years of security lessons and **778,529+ documented malicious packages**:

- **Optional security fails** (10-15% adoption when voluntary)
- **Mandatory security works** (100% adoption when required)
- **Same attacks are coming**: Typosquatting, dependency confusion, maintainer compromise
- **Key principle**: "Security cannot be retrofitted at scale"

This project applies those lessons proactively to the MCP ecosystem.

---

## Broad Marketplace Definition

**"Anything that helps find, select, or install MCP servers is a marketplace"**

### 8 Marketplace Types

1. **Official Registries** - modelcontextprotocol.io and official sources
2. **Built-in App Lists** - Claude Desktop, Cursor, and other MCP clients with integrated server lists
3. **Third-party Catalogs** - PulseMCP, MCP Server Finder, LobeHub, Portkey
4. **Code Hosting Discovery** - GitHub search, Glama.ai, Smithery.ai
5. **AI Agent Recommendations** - ChatGPT, Claude, or other AI suggesting servers to users
6. **Search Engine Results** - Google, Bing results for "MCP server for X"
7. **Community Forums** - Discord, Reddit, Slack discussions recommending servers
8. **Tutorial/Blog Sites** - How-to guides that include server recommendations

### Critical Insight

**AI agents recommending MCP servers represent the highest-risk marketplace type**:
- Highest user trust ("the AI knows")
- Lowest security mechanisms (none)
- Highest reach (millions of users)
- Bypasses human judgment entirely

---

## Evaluation Framework

### 6 Evaluation Categories

1. **Transparency and Information Disclosure**
   - Developer/author information visible
   - Source code accessibility
   - License information
   - Update history and changelog

2. **Vendor Verification**
   - Domain validation (does server match vendor's official domain?)
   - Organization verification badges
   - Official vs. third-party distinction clear to users

3. **Security Indicators**
   - HTTPS requirement for hosted servers
   - Security audit information available
   - Vulnerability disclosure process documented

4. **Feedback and Reporting Mechanisms**
   - Public issue tracking
   - Security vulnerability reporting channel
   - User reviews/ratings

5. **Coverage and Completeness**
   - Hosted servers included (not just local)
   - Provenance/details information
   - Contact mechanisms for server maintainers

6. **Type-Specific Criteria**
   - Different weights and expectations for different marketplace types

### 8 Critical Gaps to Address

| Gap | Severity | Description |
|-----|----------|-------------|
| Missing Hosted Servers | Critical | Many marketplaces only list local servers |
| Logo Misuse | High | No verification of brand/logo usage |
| Provenance Regression | High | Less info available than before (e.g., Claude Desktop removed details) |
| No Reporting Mechanisms | Medium | Can't report malicious or misconfigured servers |
| No Vendor Verification | High | Anyone can claim to be official |
| Domain Validation Complex | Medium | Hard to verify official sources programmatically |
| Third-Party Not Distinguished | High | Users can't tell official from community-built |
| No Shared Registry | Medium | Each marketplace reinvents verification |

---

## Purpose

This document defines the goals for the **MCP Marketplace Security Evaluation** project.
Goals are grouped by stakeholder:

* **CSA** – CSA organizational goals
* **Community** – ecosystem, practitioners, researchers, adopters
* **Partners** – vendors, service providers, platforms
* **Shared** – goals that benefit multiple groups simultaneously

---

# 1. CSA Goals

---

### CSA Goal 1 – Establish a neutral, credible evaluation model for MCP marketplaces

**Stakeholder**: CSA

Create and maintain a vendor-neutral, transparent approach for evaluating MCP marketplaces and their listings, forming the baseline for later client and server evaluation work. This positions CSA as the first organization to define security expectations around agent/tool marketplaces.

---

### CSA Goal 2 – Use evaluation outputs to inform CSA frameworks and education

**Stakeholder**: CSA

Feed patterns, insights, examples, and evaluations into CSA frameworks (CCM, AICM, STAR) and future training programs related to AI agents and MCP security. Generate content for labs, certification questions, and practical exam exercises.

---

### CSA Goal 3 – Strengthen CSA's leadership position in AI agent security

**Stakeholder**: CSA

Demonstrate clear, practical leadership in defining how secure agent ecosystems should work, with marketplaces as the first anchor point. Establish CSA as the authority on MCP marketplace security before incidents force reactive industry responses.

---

# 2. Community Goals

---

### Community Goal 1 – Help users answer "How do I safely get an MCP server?"

**Stakeholder**: Community

Provide clear guidance for the three user personas:
- **End users** (non-technical): Simple trust signals and safe defaults
- **IT administrators**: Evaluation criteria for enterprise deployment
- **Decision makers**: Risk assessment frameworks for procurement

---

### Community Goal 2 – Publish reusable evaluation patterns, checklists, and templates

**Stakeholder**: Community

Provide open, accessible resources that practitioners can use to evaluate MCP listings consistently and independently across all 8 marketplace types.

---

### Community Goal 3 – Enable non-programmers to contribute using AI-assisted workflows

**Stakeholder**: Community

Allow contributors who cannot write code to participate fully through AI-assisted evaluations, summaries, risk analyses, and security insight reports.

---

### Community Goal 4 – Normalize AI-mediated analyses and reports as valid contributions

**Stakeholder**: Community

Accept and integrate AI-generated or AI-assisted evaluation artifacts as legitimate contributions, provided they are reviewed and transparent about their origin.

---

### Community Goal 5 – Support skill development for broader participation in standards work

**Stakeholder**: Community

Use the marketplace evaluation effort as a learning environment where practitioners acquire the knowledge needed to engage with CSA working groups and standards processes.

---

### Community Goal 6 – Address AI agent recommendation risk

**Stakeholder**: Community

Explicitly create guidance for the highest-risk marketplace type: AI agents recommending MCP servers directly to users. Help the community understand and mitigate this emerging attack vector.

---

# 3. Partner Goals

---

### Partner Goal 1 – Provide a neutral structure for vendors to describe security posture

**Stakeholder**: Partners

Give vendors a simple, consistent way to express the security characteristics of their MCP servers or agents listed in a marketplace, including clear distinction between official and third-party implementations.

---

### Partner Goal 2 – Reduce friction in enterprise security reviews

**Stakeholder**: Partners

Help partners by providing baseline evaluation criteria that align with real organizational needs, reducing ad-hoc questionnaires and bespoke review processes.

---

### Partner Goal 3 – Create verified vendor registry

**Stakeholder**: Partners

Establish a registry of verified vendors so users and marketplaces can distinguish official implementations from community-built alternatives.

---

# 4. Shared Goals

---

### Shared Goal 1 – Improve transparency, clarity, and trust in the MCP ecosystem

**Stakeholder**: Shared

Make MCP marketplace listings clearer, safer, and more trustworthy through consistent evaluations and security-aware documentation. Address the current "Wild West" state before major incidents occur.

---

### Shared Goal 2 – Create the foundation reused by future MCP Client and MCP Server evaluation projects

**Stakeholder**: Shared

Develop templates, checks, definitions, and community workflows that the upcoming Client and Server evaluation projects can directly inherit and extend.

---

### Shared Goal 3 – Capture and share insights from real evaluation exercises

**Stakeholder**: Shared

Document lessons learned, emerging patterns, recurring gaps, and effective practices identified during marketplace evaluations and feed them back into MCP Security.

---

### Shared Goal 4 – Support governable productivity for MCP-based agents

**Stakeholder**: Shared

Enable safe, controlled adoption of AI agents through transparency, structured evaluations, and documented trust signals around marketplace-discoverable servers.

---

### Shared Goal 5 – Apply package registry lessons proactively

**Stakeholder**: Shared

Use the decade of lessons from PyPI and npm security to prevent the same mistakes in the MCP ecosystem. Design for mandatory security from day one rather than retrofitting after incidents.

---

# 5. Deliverables

The project will produce:

1. **Marketplace Evaluation Database** - Structured data on all marketplaces evaluated
2. **Scoring Rubric** - Weighted evaluation methodology and tools
3. **Verified Vendor Registry** - Registry of verified official vendors
4. **Operator Guidance** - Guide for marketplace operators on security best practices
5. **User Guidance** - Tiered guidance for end users, IT admins, and decision makers
6. **"Wild West" Awareness Content** - State of ecosystem awareness pieces (blog posts, reports)
7. **Comprehensive Evaluation Report** - Full evaluation of major marketplaces
8. **Automation Tools** - Tools for ongoing monitoring and evaluation

---

# End of Document
