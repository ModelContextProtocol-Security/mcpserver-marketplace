---
title: "Claude Desktop"
main_url: "https://claude.ai/download"
source_code_url: ""
has_marketplace_features: yes
marketplace_type: multiple
integrated_registries:
  - Anthropic Desktop Extensions Directory
evidence:
  - url: "https://www.anthropic.com/engineering/desktop-extensions"
    description: "Built-in curated directory of extensions. Users can browse, search, and install with one click. Launched with .mcpb (MCP Bundle) format - ZIP archives containing server + manifest. One-click install: download .mcpb, double-click, click Install."
  - url: "https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop"
    description: "Settings > Extensions for browsing directory. Extensions auto-update. Enterprise has allowlist controls via isDesktopExtensionEnabled and isDesktopExtensionDirectoryEnabled settings."
  - url: "https://docs.mcp.run/mcp-clients/claude-desktop/"
    description: "mcp.run documentation for Claude Desktop integration."
---

# Claude Desktop

## Notes

Anthropic's official desktop app with comprehensive MCP marketplace features:
- **Built-in Extension Directory**: Curated, searchable directory accessible via Settings > Extensions
- **One-click Installation**: Desktop Extensions (.mcpb files) install with single click
- **Auto-updates**: Extensions from official directory update automatically
- **.mcpb Format**: Open-source bundle format (ZIP with manifest.json) portable to other apps
- **Enterprise Controls**: Allowlist management for permitted extensions
- **Built-in Node.js**: No developer tools required for users
- **Secure Storage**: Sensitive data in OS keychain

Also supports manual config via claude_desktop_config.json and custom extension upload for Team/Enterprise plans.
