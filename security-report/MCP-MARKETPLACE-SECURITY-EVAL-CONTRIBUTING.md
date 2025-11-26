# Contributing Guidelines – MCP Marketplace Security Evaluation (v0.2)

**Owner**: Kurt Seifried
**Last Updated**: 2025-11-25
**Project**: MCP Marketplace Security Evaluation
**Parent Program**: CSA MCP Security
**Folder**: https://drive.google.com/drive/folders/1pGOYZDOOnm93QGe3fGWtLRPP_H3scj-L

---

## The Core Question

> **"How do I ultimately safely get an MCP server?"**

Your contributions help us answer this question for users, administrators, and decision makers across all marketplace types.

---

## Introduction

Thank you for your interest in contributing to the **MCP Marketplace Security Evaluation** project!

This project welcomes contributions from:

- Security engineers  
- Developers  
- Policy/governance experts  
- Documentation specialists  
- Researchers  
- People who cannot code but can analyze, critique, or summarize  
- People using AI assistants to help produce evaluations  

We value **clarity**, **neutrality**, **honesty**, and **inclusive participation**.

All contributions should support the project's goals (see `GOALS.md`).

---

## The 8 Marketplace Types

Contributions may focus on any of these marketplace types:

| Type | Examples | Risk Level |
|------|----------|------------|
| Official Registries | modelcontextprotocol.io | Lower |
| Built-in App Lists | Claude Desktop, Cursor | Medium |
| Third-party Catalogs | PulseMCP, MCP Server Finder, LobeHub | Medium |
| Code Hosting Discovery | GitHub search, Glama.ai, Smithery.ai | Medium |
| AI Agent Recommendations | ChatGPT/Claude suggesting servers | **Highest** |
| Search Engine Results | Google, Bing | Medium |
| Community Forums | Discord, Reddit, Slack | Higher |
| Tutorial/Blog Sites | How-to guides with server lists | Higher |

**Critical insight**: AI agents recommending MCP servers represent the highest-risk marketplace type due to high user trust combined with zero security mechanisms.

---

## Ways You Can Contribute

### 1. Evaluate an MCP Marketplace or Listing
Use the template at:
`security-report/TEMPLATE-evaluation.md`

You can:

- Evaluate **marketplaces** (any of the 8 types above)
- Evaluate **specific listings** (MCP servers, agents, tools)
- Submit the evaluation as:
  - A pull request
  - A GitHub issue (paste it, we'll place it correctly)

Evaluations may be:
- Fully human-written
- AI-assisted
- AI-generated + human reviewed

All are welcome.

---

### 2. Improve the Evaluation Template
If you see missing fields, redundant areas, or needed clarifications, open a PR or issue to propose improvements.

---

### 3. Propose or Refine Security Checks
Help define what we should look for when evaluating across the 6 evaluation categories:

1. **Transparency and Information Disclosure** - Developer info, source code, licenses, changelogs
2. **Vendor Verification** - Domain validation, organization verification, official vs. third-party distinction
3. **Security Indicators** - HTTPS, security audits, vulnerability disclosure
4. **Feedback and Reporting** - Issue tracking, security reporting, user reviews
5. **Coverage and Completeness** - Hosted servers, provenance, contact mechanisms
6. **Type-Specific Criteria** - Different weights for different marketplace types

Add your suggestions to:

`security-report/patterns/checks.md`

---

### 4. Submit AI-Mediated Reports
We strongly encourage:

- Conversations with AI tools
- Asking the AI to summarize insights
- Submitting the summary as a draft evaluation or analysis

These contributions help scale the working group and invite broader voices.

Just disclose AI assistance:

```
AI-Assistance: Yes
Tool: [model]
Method: [brief description, e.g., "Draft generated from conversation with AI"]
```

See `MCP-MARKETPLACE-SECURITY-EVAL-AI-USAGE-GUIDELINES.md` for detailed guidance.


---

### 5. Participate in Discussions (GitHub or CSA Slack)
We use issues and discussions for async collaboration.

You can:

- Ask questions
- Propose new marketplaces to evaluate
- Suggest improvements
- Flag unclear documentation
- Help shape the future Client and Server evaluation projects

---

### 6. Contribute Marketplace Metadata
If you know of a marketplace not yet listed, add it under:

`security-report/marketplaces/_index.md`

Or list it in an issue.

**High-priority marketplaces we're seeking evaluations for:**

| Marketplace | Type | Why Priority |
|-------------|------|--------------|
| PulseMCP | Catalog | 6,480+ servers, major reach |
| Smithery.ai | Hosting | Installation/hosting platform |
| MCP Server Finder | Catalog | Dedicated discovery site |
| Glama.ai | Hosting | Hosting platform |
| Docker MCP Catalog | Registry | Official Docker integration |
| LobeHub | Catalog | Large server directory |
| modelcontextprotocol.io | Official | The official source |
| GitHub search | Discovery | How developers find servers |

---

### 7. Document Threats, Mitigations, and Patterns
Help expand:

- `patterns/threat-model.md`
- `patterns/trust-signals.md`

Examples, anecdotes, and real-world concerns are extremely valuable.

**Key gaps we're working to address:**

| Gap | Severity |
|-----|----------|
| Missing Hosted Servers | Critical |
| Logo Misuse | High |
| Provenance Regression | High |
| No Vendor Verification | High |
| Third-Party Not Distinguished | High |
| No Reporting Mechanisms | Medium |
| Domain Validation Complex | Medium |
| No Shared Registry | Medium |

---

### 8. Help Build Project Deliverables
The project is working toward 8 key deliverables:

1. **Marketplace Evaluation Database** - Structured data on all marketplaces evaluated
2. **Scoring Rubric** - Weighted evaluation methodology and tools
3. **Verified Vendor Registry** - Registry of verified official vendors
4. **Operator Guidance** - Guide for marketplace operators on security best practices
5. **User Guidance** - Tiered guidance for end users, IT admins, and decision makers
6. **"Wild West" Awareness Content** - State of ecosystem awareness pieces
7. **Comprehensive Evaluation Report** - Full evaluation of major marketplaces
8. **Automation Tools** - Tools for ongoing monitoring and evaluation

Contributions toward any of these are welcome.

---

## Contribution Process

### Step 1: Create or Refine Content
Evaluate something, suggest a change, or draft a new pattern.

### Step 2: Submit
You may submit via:

- Pull request
- GitHub issue
- Email to the WG (if not comfortable with GitHub)
- CSA Slack

### Step 3: Review
A project maintainer (or the WG) will:

- Review for clarity, accuracy, neutrality
- Propose edits or improvements
- Merge or discuss next steps

---

## Contributor Expectations

- Be factual — avoid speculation presented as fact
- Document uncertainties clearly ("unknown", "not documented", etc.)
- Maintain a neutral tone
- Avoid implying CSA endorsement of specific vendors or products
- Make evaluations transparent and reproducible
- When using AI, always apply human review

We value contributions from all skill levels.
You do **not** need deep MCP knowledge to provide valuable input.

**Why your contribution matters**: The MCP ecosystem is currently in a "Wild West" phase with 6,480+ servers listed across marketplaces, no standard verification, and AI agents recommending servers with zero security mechanisms. Your contributions help establish security norms proactively before incidents force reactive responses.

---

## Licensing

All contributions to this repository must be released under the project’s license (see `LICENSE`).

---

## Code of Conduct

This project follows the Cloud Security Alliance’s Code of Conduct.  
Be respectful, constructive, and collaborative.

---

# End of Document

