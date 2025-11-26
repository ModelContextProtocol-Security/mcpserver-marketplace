---
title: MCP Marketplace Security Evaluation – Project Overview
owner: Kurt Seifried
status: active
version: 1.1.0
updated: 2025-11-25
tags: [project-overview, mcp, security, marketplace]
---

# MCP Marketplace Security Evaluation

**Status**: Active – designing checks, patterns, and community workflows while starting initial marketplace evaluations
**Last Updated**: 2025-11-25
**Owner**: Kurt Seifried
**Operational Complexity**: Moderate

---

## The Core Question

> **"How do I ultimately safely get an MCP server?"**

This project exists to answer that question for users, administrators, and decision makers.

---

## Overview

The MCP ecosystem is in a **"Wild West" phase** – similar to npm/PyPI before major security incidents drove change:

- **6,480+ MCP servers** listed across various marketplaces
- **No standard verification processes** for authenticity
- **Logo misuse is common** (brands used without authorization)
- **AI agents recommending servers** have highest reach but lowest security

We have a window to establish security norms **proactively** before incidents shape the narrative.

This project defines what an MCP marketplace is (broadly), creates a neutral evaluation model, and captures concrete evaluations in a public, repeatable format. This enables CSA, the community, and vendors to present and consume MCP marketplace entries with clear security-relevant information.

---

## Broad Marketplace Definition

**"Anything that helps find, select, or install MCP servers is a marketplace"**

### 8 Marketplace Types

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

**Critical insight**: AI agents recommending MCP servers have the highest risk because they combine maximum user trust with zero security mechanisms.

---

## High-Priority Evaluation Targets

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

## Documents

### Mandatory

- **Goals** (public): [`MCP-MARKETPLACE-SECURITY-EVAL-GOALS.md`](./MCP-MARKETPLACE-SECURITY-EVAL-GOALS.md)
- **Internal Business Case** (CSA internal): [`MCP-MARKETPLACE-SECURITY-EVAL-INTERNAL-BUSINESS-CASE.md`](./MCP-MARKETPLACE-SECURITY-EVAL-INTERNAL-BUSINESS-CASE.md)
- **AI-Usage-Guidelines**: [`MCP-MARKETPLACE-SECURITY-EVAL-AI-USAGE-GUIDELINES.md`](./MCP-MARKETPLACE-SECURITY-EVAL-AI-USAGE-GUIDELINES.md)
- **Contributing**: [`MCP-MARKETPLACE-SECURITY-EVAL-CONTRIBUTING.md`](./MCP-MARKETPLACE-SECURITY-EVAL-CONTRIBUTING.md)

### Project Execution

- **Source of Truth**:
  - GitHub: [`security-report/`](./security-report/) – definitions, patterns, templates, and concrete evaluations
  - Google Drive folder (planning & internal docs):
    https://drive.google.com/drive/folders/1pGOYZDOOnm93QGe3fGWtLRPP_H3scj-L

- **Project Management**:
  - GitHub Projects board (TBD): `https://github.com/ModelContextProtocol-Security/mcpserver-marketplace/projects`

- **Communication**:
  - CSA Slack: `#mcp-security`
  - GitHub Issues/Discussions for public, async input

---

## Deliverables

1. **Marketplace Evaluation Database** - Structured data on all marketplaces evaluated
2. **Scoring Rubric** - Weighted evaluation methodology and tools
3. **Verified Vendor Registry** - Registry of verified official vendors
4. **Operator Guidance** - Guide for marketplace operators on security best practices
5. **User Guidance** - Tiered guidance for end users, IT admins, and decision makers
6. **"Wild West" Awareness Content** - State of ecosystem awareness pieces (blog posts, reports)
7. **Comprehensive Evaluation Report** - Full evaluation of major marketplaces
8. **Automation Tools** - Tools for ongoing monitoring and evaluation

---

## Current Status

The project is **active** and in early execution:

- We have committed to a three-part MCP Security Evaluation Suite:
  1. Marketplace Security Evaluation (this project)
  2. MCP Client Security Evaluation
  3. MCP Server Security Evaluation

- **Current focus**:
  - Finalize the definition and taxonomy of MCP marketplaces (8 types identified)
  - Stand up the initial structure under `security-report/`:
    - `README.md` describing scope and community involvement model
    - `TEMPLATE-evaluation.md` for marketplace/listing evaluations
    - `patterns/checks.md` for initial security checks and themes
  - Identify and evaluate high-priority marketplaces (see table above)
  - Validate the AI-mediated contribution workflow

- **Key risks being managed**:
  - Avoiding premature "certification" language while still providing useful trust signals
  - Keeping checks lightweight enough for community use but meaningful enough to matter
  - Coordinating with the future MCP Client and MCP Server evaluation efforts

If you want to help right now, the most useful contributions are: proposing marketplaces to evaluate, helping refine the evaluation criteria, and piloting the evaluation template on one real marketplace using an AI-assisted workflow.

---

## Resources

- **Primary owner**: Kurt Seifried (CINO, CSA)
- **Implementation**: MCP Security working group and collaborators in the `ModelContextProtocol-Security` GitHub org
- **Repos**:
  - Marketplace focus: https://github.com/ModelContextProtocol-Security/mcpserver-marketplace
- **Primary folder for docs & planning**:
  https://drive.google.com/drive/folders/1pGOYZDOOnm93QGe3fGWtLRPP_H3scj-L

---

## Contact

**Owner**: Kurt Seifried – `kurt.seifried@cloudsecurityalliance.org`

**Questions / Participation**:
- Open an issue or discussion in the `mcpserver-marketplace` repo
- Or contact via CSA Slack (`#mcp-security`)

**Contributing**:
See [`MCP-MARKETPLACE-SECURITY-EVAL-CONTRIBUTING.md`](./MCP-MARKETPLACE-SECURITY-EVAL-CONTRIBUTING.md) for how to get involved, including AI-mediated contribution pathways for non-programmers.
