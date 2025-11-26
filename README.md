# MCP Marketplace Security

Part of the [Model Context Protocol Security](https://modelcontextprotocol-security.io/) initiative, a Cloud Security Alliance community project.

## What This Is

MCP marketplaces are how users discover and install MCP servers - registries, built-in app stores, catalog sites, AI recommendations, tutorials, and more. This repo contains data, evaluations, and guidance for securing the MCP marketplace ecosystem.

## Why It Matters

MCP servers get powerful access to your systems and data. Where you get them from matters. The ecosystem is young - we can build security in now rather than retrofit after incidents.

---

## MCP Marketplace Security Report

**Status**: In Progress

Our primary project: systematically evaluating MCP marketplaces and how MCP clients handle server installation.

[Full project documentation](./security-report/)

### Completed Evaluations

| Target | Type | Date | Link |
|--------|------|------|------|
| Claude Desktop | MCP Client | 2025-11-19 | [Evaluation](./security-report/evaluations/mcp-clients/claude-desktop/) |

**Want to conduct an evaluation?** Use our [templates](./security-report/templates/) and submit a PR. Or file an issue offering to evaluate a specific marketplace/client.

---

## Data

We maintain structured data about the MCP marketplace ecosystem.

### Marketplace Types

**What**: Categories of how users discover MCP servers (registries, catalog sites, AI recommendations, etc.)

**Current count**: 8 types

[View types](./data/marketplace-types/) ・ [Schema](./data/marketplace-types/README.md)

**Contribute**: Think we're missing a type? File an issue describing it and how it differs from existing types.

---

### Marketplaces

**What**: Known MCP marketplaces - anywhere users discover or get MCP servers.

**Current count**: 33+ marketplaces

[View data](./data/marketplaces.csv) ・ [Schema](./data/marketplaces/README.md)

**Contribute**: Know a marketplace we're missing?
- Submit a PR adding it to `data/marketplaces.csv`, or
- File an issue with the name and URL

---

### MCP Clients

**What**: How MCP clients handle server discovery, installation, and runtime permissions. This is marketplace-specific data (general client security is covered in [mcpclient-security](https://github.com/CloudSecurityAlliance/mcpclient-security)).

**Current count**: 25+ clients

[View data](./data/mcp-clients.csv) ・ [Schema](./data/mcp-clients/README.md)

**Contribute**: Know an MCP client we're missing? Found outdated info?
- Submit a PR adding/updating `data/mcp-clients.csv`, or
- File an issue with the name and URL

---

### Vendors (Planned)

**What**: Registry of verified vendor MCP servers - which servers are officially blessed by the vendors whose services they access.

**Status**: Not started

**Contribute**: Want to help design this? File an issue with your thoughts.

---

## Get Involved

### Quick Contributions

| I found... | Do this |
|------------|---------|
| A marketplace we're missing | File an issue or PR to `data/marketplaces.csv` |
| An MCP client we're missing | File an issue or PR to `data/mcp-clients.csv` |
| Outdated or wrong data | File an issue or PR with corrections |
| A security check we should add | File an issue or PR to `security-report/patterns/checks.md` |

### Bigger Contributions

| I want to... | Do this |
|--------------|---------|
| Evaluate a marketplace or client | Use [templates](./security-report/templates/), submit PR |
| Propose a new marketplace type | File an issue describing it |
| Suggest a framework change | File an issue to discuss |

### Join the Conversation

- **GitHub Issues**: For specific items (missing data, errors, suggestions)
- **CSA Slack**: `#mcp-security` channel
- **Working Group Meetings**: See [modelcontextprotocol-security.io](https://modelcontextprotocol-security.io/) for schedule

---

## Related Projects

| Repo | Focus |
|------|-------|
| [modelcontextprotocol-security.io](https://github.com/CloudSecurityAlliance/modelcontextprotocol-security.io) | Main website and docs |
| [mcpclient-security](https://github.com/CloudSecurityAlliance/mcpclient-security) | MCP client security (general) |
| [mcpserver-audit](https://github.com/CloudSecurityAlliance/mcpserver-audit) | Server auditing tools |
| [vulnerability-db](https://github.com/CloudSecurityAlliance/vulnerability-db) | Vulnerability tracking |
| [audit-db](https://github.com/CloudSecurityAlliance/audit-db) | Audit results database |

Full list at [modelcontextprotocol-security.io](https://modelcontextprotocol-security.io/)

---

## License

Apache 2.0 - see [LICENSE](./LICENSE)

---

*A Cloud Security Alliance community project.*
