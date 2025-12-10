---
title: "Claude Code"
main_url: "https://claude.com/product/claude-code"
source_code_url: ""
has_marketplace_features: yes
marketplace_type: multiple
integrated_registries:
  - Claude Code Plugin Marketplaces
evidence:
  - url: "https://docs.anthropic.com/en/docs/claude-code/mcp"
    description: "MCP servers via CLI: 'claude mcp add github --scope user'. Supports HTTP (remote), stdio (local). Can add, list, remove servers via CLI."
  - url: "https://www.anthropic.com/news/claude-code-plugins"
    description: "Plugin system - curated collections of slash commands, agents, MCP servers, hooks. Anyone can build and host plugin marketplaces. Community marketplaces exist (Dan Ávila's DevOps/docs plugins, Seth Hobson's 80+ sub-agents)."
  - url: "https://www.anthropic.com/news/claude-code-remote-mcp"
    description: "Remote MCP support - just add vendor URL, no local setup needed. Vendors handle updates/scaling."
---

# Claude Code

## Notes

Anthropic's CLI coding agent with comprehensive MCP support:
- **CLI commands**: `claude mcp add/list/remove` for server management
- **Plugin Marketplaces**: Anyone can host marketplaces (git repo with marketplace.json). Community marketplaces exist with DevOps, docs, testing plugins
- **Remote MCP**: Add vendor URL directly - no local management needed
- **Desktop Extensions**: .mcpb bundles for one-click installation (shared with Claude Desktop)

Three config methods: HTTP (remote), local servers, plugins. Active community creating plugin marketplaces.
