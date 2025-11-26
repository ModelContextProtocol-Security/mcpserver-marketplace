# MCP Marketplace Types

## What This Is

A taxonomy of **how users discover and install MCP servers**. Different marketplace types have fundamentally different security profiles.

## Why It Matters

- A curated registry can enforce security requirements
- An AI agent recommendation may have zero verification
- A tutorial blog post may have outdated, vulnerable instructions

Understanding the type helps us set appropriate security expectations.

## Current Types

| # | Type | Risk Level | Example |
|---|------|------------|---------|
| 1 | [Registry](./01-registry.md) | Lower | Official MCP Registry, Docker Catalog |
| 2 | [Built-in App](./02-built-in-app.md) | Medium | Claude Desktop Extensions |
| 3 | [Catalog Site](./03-catalog-site.md) | Medium-High | MCP.so, PulseMCP |
| 4 | [Code Hosting](./04-code-hosting.md) | Medium | Smithery, GitHub |
| 5 | [AI Agent Recommendations](./05-ai-agent-recommendations.md) | **Highest** | ChatGPT suggesting servers |
| 6 | [Search Engines](./06-search-engines.md) | Medium | Google results |
| 7 | [Community Forums](./07-community-forums.md) | Higher | Discord, Reddit |
| 8 | [Tutorials](./08-tutorials.md) | Higher | Blog posts, guides |

## Is This List Complete?

Probably not. The MCP ecosystem is evolving rapidly.

**Think we're missing a type?** File an issue describing:
- What the type is
- How it differs from existing types
- Examples of marketplaces in this category
- Why the security profile is distinct

**Think a type definition is wrong or incomplete?** File an issue or submit a PR.

---

## Type File Schema

Each type file uses YAML frontmatter:

```yaml
---
type_id: 1
name: Registry Marketplace
risk_level: lower
examples:
  - Official MCP Registry
  - Docker MCP Catalog
---
```

Followed by sections:
- Definition
- Characteristics
- Trust Model
- Security Opportunities
- Security Risks
- Evaluation Priority
