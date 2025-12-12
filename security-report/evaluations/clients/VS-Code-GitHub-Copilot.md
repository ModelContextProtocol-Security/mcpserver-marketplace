---
title: "VS Code GitHub Copilot"
main_url: "https://code.visualstudio.com/"
source_code_url: "https://github.com/microsoft/vscode"
has_marketplace_features: yes
marketplace_type: registry-integration
integrated_registries:
  - GitHub MCP Registry
evidence:
  - url: "https://code.visualstudio.com/docs/copilot/customization/mcp-servers"
    description: "MCP support GA in VS Code 1.102+. Servers configurable via GitHub MCP Registry or manual JSON. Access registry from Extensions view. VS Code Marketplace extensions can also provide MCP servers."
  - url: "https://github.blog/changelog/2025-11-18-internal-mcp-registry-and-allowlist-controls-for-vs-code-stable-in-public-preview/"
    description: "Enterprise registry and allowlist controls. Admins can configure internal registries for discovery and allowlisting. 'Registry only' policy blocks non-approved servers."
  - url: "https://docs.github.com/copilot/customizing-copilot/using-model-context-protocol/extending-copilot-chat-with-mcp"
    description: "GitHub Copilot MCP extension documentation."
---

# VS Code GitHub Copilot

## Notes

VS Code with GitHub Copilot integration has full MCP marketplace via GitHub MCP Registry. Features:
- **GitHub MCP Registry**: Curated server catalog, browse from Extensions view
- **One-click installation**: Remote or local server options
- **Enterprise Controls**: Internal registries, allowlist policies for organizations
- **VS Code Marketplace**: Extensions can provide additional MCP servers
- **OAuth support**: For remote MCP servers (VS Code 1.101+)

Config via JSON settings or registry UI. Enterprise admins can enforce approved-only servers via registry policy.
