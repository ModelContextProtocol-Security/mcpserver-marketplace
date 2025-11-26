# MCP Marketplace Data

Structured data about the MCP marketplace ecosystem.

## Datasets

| Dataset | Description | Format | Count |
|---------|-------------|--------|-------|
| [Marketplace Types](./marketplace-types/) | Categories of how users discover MCP servers | Markdown files | 8 |
| [Marketplaces](./marketplaces.csv) | Known MCP marketplaces | CSV | 33+ |
| [MCP Clients](./mcp-clients.csv) | Clients and their marketplace behavior | CSV | 25+ |
| [Vendors](./vendors/) | Verified vendor registry | CSV | Planned |

## How to Contribute

### Found a marketplace we're missing?

- **Submit a PR** adding a row to `marketplaces.csv`, or
- **File an issue** with the name and URL

### Found an MCP client we're missing?

- **Submit a PR** adding a row to `mcp-clients.csv`, or
- **File an issue** with the name and URL

### Think we're missing a marketplace type?

File an issue describing the type and how it differs from the existing 8 types.

### Want to add details to an existing entry?

For marketplaces and MCP clients, you can create a detailed markdown file in the appropriate subdirectory (e.g., `marketplaces/smithery.md` or `mcp-clients/claude-desktop.md`).

---

## Data Formats

### CSV Files

We use CSV for the master lists because:
- Easy to scan and compare entries
- Simple diffs in PRs
- Tool-friendly for analysis

### Markdown Detail Files (Optional)

When we have more to say about a specific entry (security observations, history, detailed notes), we create a markdown file with YAML frontmatter:

```markdown
---
id: example-marketplace
name: Example Marketplace
url: https://example.com
# ... other fields from CSV
---

# Example Marketplace

## Overview
...

## Security Observations
...
```

See the README in each subdirectory for the specific schema.
