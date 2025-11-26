# MCP Clients - Marketplace Behavior

## What This Is

Data about how MCP clients handle server discovery, installation, and runtime permissions.

**Important**: This is NOT a general MCP client security evaluation. That's covered in the [mcpclient-security](https://github.com/CloudSecurityAlliance/mcpclient-security) project.

This data is specifically about each client's role as a **distribution point** for MCP servers:
- Does it have a built-in marketplace?
- How do users install MCP servers?
- What permissions do installed servers get?
- Is there sandboxing?

## Why It Matters

The MCP client is where marketplace security becomes real. A secure marketplace means nothing if the client grants full system access to every installed server.

## Current Count

25+ clients identified.

## Data Files

- [`../mcp-clients.csv`](../mcp-clients.csv) - Master list with core fields
- `[client-id].md` - Detailed analysis files (moved from research)

## How to Contribute

**Know an MCP client we're missing?**

- Submit a PR adding a row to `../mcp-clients.csv`, or
- File an issue with the name and URL

**Have detailed info about a client's marketplace behavior?**

Create or update `[client-id].md` in this directory.

**Found outdated info?**

MCP clients update frequently. File an issue or submit a PR.

---

## CSV Schema

| Field | Required | Description |
|-------|----------|-------------|
| `id` | Yes | Unique identifier (lowercase, hyphens) |
| `name` | Yes | Display name |
| `vendor` | No | Company/developer |
| `url` | Yes | Primary URL |
| `type` | No | desktop, ide, web, cli, framework |
| `status` | Yes | active, beta, discontinued |
| `has_builtin_marketplace` | No | yes, no, unknown |
| `marketplace_name` | No | What they call it (Extensions, Connectors, etc.) |
| `allows_manual_config` | No | yes, no, unknown |
| `config_method` | No | json-file, gui, cli, etc. |
| `runtime_sandboxing` | No | yes, no, unknown |
| `permission_model` | No | full-user, capability-based, user-approval, etc. |
| `last_verified` | No | Date we last checked (YYYY-MM-DD) |
| `notes` | No | Brief notes |

---

## Detailed Markdown Files

For clients where we have detailed analysis, create `[id].md`:

```markdown
---
id: claude-desktop
name: Claude Desktop
vendor: Anthropic
url: https://claude.ai/download
type: desktop
status: active
has_builtin_marketplace: yes
marketplace_name: Extensions
allows_manual_config: yes
config_method: json-file
runtime_sandboxing: no
permission_model: user-approval
---

# Claude Desktop

## Overview
...

## Marketplace Behavior
...

## Security Observations
...
```
