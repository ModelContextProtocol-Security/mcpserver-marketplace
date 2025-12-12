---
title: "Amp"
main_url: "https://ampcode.com"
source_code_url: ""
has_marketplace_features: no
evidence:
  - url: "https://ampcode.com/manual"
    description: "Manual shows MCP server config via amp.mcpServers in config files, CLI 'amp mcp add' command, or VS Code settings. No marketplace or registry - users must know server URL/command beforehand. Examples provided (Playwright, Linear, Semgrep) but these are illustrative, not discoverable through Amp."
  - url: "https://ampcode.com/news/mcp-permissions"
    description: "MCP permissions system for controlling which servers can be accessed - enterprise admin controls. Recommends 'only use vendor-supported MCP servers' but doesn't provide discovery."
  - url: "https://github.com/sourcegraph/amp-examples-and-guides/blob/main/guides/amp-mcp-setup-guide.md"
    description: "Setup guide from Sourcegraph showing manual configuration process."
---

# Amp

## Notes

Coding agent from Sourcegraph. Supports MCP servers via manual configuration (config files, CLI, VS Code UI). No built-in marketplace or registry - users must supply server URLs/commands directly. Has enterprise permission controls for MCP servers.
