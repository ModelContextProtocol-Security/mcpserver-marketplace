# MCP Marketplaces

## What This Is

A catalog of known MCP marketplaces - anywhere users discover or install MCP servers.

## Current Count

33+ marketplaces identified across all types.

## Data Files

- [`../marketplaces.csv`](../marketplaces.csv) - Master list with core fields
- `[marketplace-id].md` - Optional detailed files for individual marketplaces

## How to Contribute

**Know a marketplace we're missing?**

- Submit a PR adding a row to `../marketplaces.csv`, or
- File an issue with the name and URL (and any notes you have)

**Have detailed info about a marketplace?**

Create a file `[marketplace-id].md` in this directory with additional details.

**Found an error?**

File an issue or submit a PR with corrections.

---

## CSV Schema

| Field | Required | Description |
|-------|----------|-------------|
| `id` | Yes | Unique identifier (lowercase, hyphens) |
| `name` | Yes | Display name |
| `type` | Yes | Marketplace type (see [marketplace-types](../marketplace-types/)) |
| `url` | Yes | Primary URL |
| `operator` | No | Who runs it (company, community, unknown) |
| `status` | Yes | active, inactive, discontinued |
| `server_count` | No | How many servers listed (if known) |
| `priority` | No | tier-1, tier-2, tier-3 for evaluation priority |
| `last_verified` | No | Date we last checked the URL works (YYYY-MM-DD) |
| `notes` | No | Brief notes |

### Type Values

Use these type identifiers (matching [marketplace-types](../marketplace-types/)):

- `registry` - Registry Marketplace
- `built-in-app` - Built-in Application Marketplace
- `catalog-site` - Informational Catalog Site
- `code-hosting` - Code Hosting and Distribution
- `ai-agent` - AI Agent Recommendations
- `search-engine` - Search Engines
- `community-forum` - Community Forums
- `tutorial` - Tutorial and Documentation Sites

---

## Detailed Markdown Files (Optional)

For marketplaces where we have more to say, create `[id].md`:

```markdown
---
id: smithery
name: Smithery.ai
type: code-hosting
url: https://smithery.ai/
operator: Smithery AI
status: active
server_count: unknown
priority: tier-1
last_verified: 2025-11-19
---

# Smithery.ai

## Overview

Central hub for MCP servers with hosted deployment...

## Security Incident History

- **2025**: Path traversal vulnerability compromised 3,000+ servers...

## Observations

...
```
