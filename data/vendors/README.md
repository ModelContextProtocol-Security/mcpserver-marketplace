# Verified Vendors Registry

## What This Is

A registry of verified vendor MCP servers - servers that are officially blessed by the vendors whose services they access.

## Status

**Not Started** - This dataset is planned but not yet implemented.

## Why It Matters

One of the biggest gaps in the MCP marketplace ecosystem is distinguishing official vendor servers from third-party implementations:

- Is the "Airtable MCP server" actually from Airtable?
- Is the "GitHub MCP server" actually from GitHub?
- Which Slack integration is the official one?

This registry would provide a source of truth for verified vendor relationships.

## Proposed Approach

Evidence-based verification:
- Link from vendor's official documentation to their MCP server
- Domain verification (mcp.vendor.com or vendor.com/mcp)
- GitHub organization with verified badge matching vendor domain

## How to Contribute

**Want to help design this?** File an issue with your thoughts on:
- What fields should we track?
- What counts as "verified"?
- How should this integrate with the marketplaces data?

**Know of a vendor with an official MCP server?** File an issue with:
- Vendor name
- MCP server URL
- Evidence of official relationship (link from vendor docs, verified GitHub org, etc.)
