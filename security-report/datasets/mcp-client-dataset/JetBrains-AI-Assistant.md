---
title: "JetBrains AI Assistant"
main_url: "https://plugins.jetbrains.com/plugin/22282-jetbrains-ai-assistant"
source_code_url: ""
has_marketplace_features: yes
marketplace_type: registry-integration
integrated_registries:
  - JetBrains Marketplace
evidence:
  - url: "https://www.jetbrains.com/help/ai-assistant/mcp.html"
    description: "MCP configuration via Settings > Tools > AI Assistant > Model Context Protocol. JSON configuration for servers. Status monitoring in IDE."
  - url: "https://plugins.jetbrains.com/plugin/28071-mcp-servers-for-ai-assistants"
    description: "JetBrains Marketplace has 'MCP Servers for AI Assistants' plugin - supports Junie, Windsurf, Firebender. Allows discover, install, manage, and inspect MCP servers."
  - url: "https://plugins.jetbrains.com/plugin/26071-mcp-server"
    description: "MCP Server plugin integrates MCP into IntelliJ-based IDEs for LLM communication."
---

# JetBrains AI Assistant

## Notes

JetBrains AI Assistant supports MCP via marketplace plugins. 'MCP Servers for AI Assistants' plugin enables server discovery and installation. Config via Settings > Tools > AI Assistant. Supports local servers via JSON config and remote servers via mcp-remote proxy for HTTP+SSE. Works with OpenAI, Anthropic, Google models, and local LLMs via Ollama/LM Studio.
