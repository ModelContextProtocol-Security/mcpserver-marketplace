# MCP Client Marketplace Feature Analysis Report

**Date:** December 2025
**Scope:** 132 unique MCP clients from punkpeye/awesome-mcp-clients and modelcontextprotocol.io
**Methodology:** Web research, GitHub analysis, product documentation review

---

## Executive Summary

This analysis examined 132 MCP (Model Context Protocol) clients to identify which have "marketplace features" — capabilities that influence user choice about which MCP servers to use by putting server options in front of users, rather than requiring users to arrive with prior knowledge.

**Key Finding:** Nearly half (47%) of MCP clients have some form of marketplace or registry integration, indicating a maturing ecosystem where server discovery is becoming a standard feature rather than an exception.

---

## Classification Results

| Classification | Count | Percentage |
|---------------|-------|------------|
| **YES** (has marketplace features) | 62 | 47% |
| **NO** (no marketplace features) | 63 | 48% |
| **Unclear** | 4 | 3% |
| **Unknown** | 3 | 2% |

### What Counts as a Marketplace Feature

- Built-in curated server lists
- Registry integration (Smithery, mcp.so, GitHub MCP Registry, etc.)
- Hosted catalogs maintained by the client
- Search/browse integration for discovering servers
- One-click install from curated lists
- "Easy MCP" or similar guided setup flows

### What Does NOT Count

- Config file only (JSON/YAML manual editing)
- Generic "add server" UI where user provides all connection details
- Documentation links only
- Framework/library support for MCP without discovery features

---

## Marketplace Types Identified

### 1. Built-in List (`built-in-list`)
Curated servers bundled directly with the client. Users see available options without external lookup.

**Examples:**
- **Claude Desktop** — Extensions Directory with .mcpb bundles, enterprise allowlist controls
- **Anthropic Integrations (Claude.ai)** — 10 pre-built services (Atlassian, Zapier, Cloudflare, etc.)
- **Mistral Le Chat** — 20+ connectors directory (Databricks, Snowflake, GitHub, Asana)
- **Microsoft Copilot Studio** — Built-in MCP servers catalog with onboarding wizard
- **Runbear** — 2,500+ MCP-enabled apps for Slack/Teams
- **Zencoder** — MCP Library with 100+ pre-built servers, one-click install
- **systemprompt** — Built-in GitHub, Sentry, Reddit integrations (mobile)

### 2. Registry Integration (`registry-integration`)
Client connects to external registries for server discovery and installation.

**Examples:**
- **Cline** — MCP Registry integration, conversational server creation
- **SpinAI** — Smithery MCP Registry (install via `npx spinai-mcp`)
- **Tome** — Smithery integration (4,000+ servers)
- **MCP SuperAssistant** — 6,000+ MCP servers via browser extension
- **RecurseChat** — MCP servers repository integration
- **Needle** — Universal MCP-compatible server support
- **Nerve** — Access to publicly available MCP servers

### 3. Hosted Catalog (`hosted-catalog`)
Client maintains its own server directory/marketplace.

**Examples:**
- **5ire** — mcpsvr.com (100+ servers, nanbingxyz/mcpsvr on GitHub)
- **Simtheory** — MCP Store with plug-and-play integrations
- **Smithery Playground** — THE MCP server registry (4,000+ servers)
- **Glama** — MCP Hosting Platform

### 4. Multiple/Hybrid (`multiple`)
Combination of marketplace approaches.

**Examples:**
- **Cursor** — cursor.directory/mcp + mcpmarket.com integration
- **Continue** — hub.continue.dev/explore/mcp marketplace
- **Windsurf** — Plugin Store (built-in) + curated directory

---

## Notable Marketplace Integrations

### Largest Registries by Server Count

| Registry | Server Count | Key Clients |
|----------|-------------|-------------|
| MCP SuperAssistant | 6,000+ | Browser extension for ChatGPT, Perplexity, Gemini, etc. |
| Smithery | 4,000+ | Tome, SpinAI, Smithery Playground, many others |
| Runbear | 2,500+ | Slack/Teams AI assistants |
| Zencoder MCP Library | 100+ | VS Code, JetBrains extensions |
| mcpsvr.com (5ire) | 100+ | 5ire client |

### Enterprise-Focused Marketplaces

- **Microsoft Copilot Studio** — Built-in catalog with VNet integration, DLP controls, OAuth. Streamable transport (SSE deprecated Aug 2025).
- **Klavis AI** — YC X25 company, 100+ prebuilt integrations with web dashboard
- **Kiro** — AWS agentic IDE with "Kiro Powers" for dynamic MCP loading from partners (Datadog, Dynatrace, Neon, Netlify)

### Mobile-First Marketplaces

- **Jenova** — First mobile MCP support (iOS/Android), 100+ integrations, 97.3% tool call reliability
- **systemprompt** — First voice-controlled iOS/Android MCP client with built-in integrations
- **NextChat** — Cross-platform (Web, iOS, macOS, Android, Linux, Windows) with MCP preset servers

### IDE/Editor Marketplaces

| IDE/Editor | Marketplace Feature |
|------------|-------------------|
| **VS Code/GitHub Copilot** | GitHub MCP Registry (@mcp search), enterprise internal registries |
| **Cursor** | cursor.directory/mcp + mcpmarket.com |
| **Windsurf** | Plugin Store with blue checkmark verification |
| **Zed** | Extensions via Command Palette |
| **JetBrains (via Zencoder)** | MCP Library + Zen Agents Marketplace |
| **Theia IDE** | Built-in GitHub/Playwright agents, marketplace discussion ongoing |
| **Kilo Code** | MCP Server Marketplace (750k+ downloads, superset of Cline+Roo) |
| **Roo Code** | Marketplace icon in VS Code sidebar |

---

## Interesting Discoveries

### 1. The "Smithery Effect"
Smithery has emerged as the de facto standard MCP registry, integrated by multiple clients including Tome, SpinAI, and serving as inspiration for client-specific marketplaces. Its "Try in Playground" feature allows browser-based testing before installation.

### 2. Browser Extension Innovation
**MCP SuperAssistant** represents a novel approach — a browser extension that brings 6,000+ MCP servers to AI platforms (ChatGPT, Perplexity, Gemini, Grok, etc.) that don't natively support MCP marketplaces. This "MCP everywhere" approach bypasses the need for individual client integration.

### 3. OpenAI's MCP Adoption
**ChatGPT** now supports MCP via Developer Mode (beta), joining the ecosystem that Anthropic created. Available to Pro, Plus, Business, Enterprise, and Education users on web. OpenAI joined the MCP steering committee.

### 4. Enterprise Control Patterns
Several enterprise clients have sophisticated marketplace controls:
- **Claude Desktop** — `isDesktopExtensionEnabled`, `isDesktopExtensionDirectoryEnabled` for allowlisting
- **Windsurf** — Enterprise whitelist for approved plugins
- **Microsoft Copilot Studio** — Connector infrastructure with VNet, DLP, OAuth controls

### 5. Hosted vs Local Dichotomy
A clear split exists between:
- **Hosted MCP** — Supermachine, Klavis, Smithery hosting, remote MCP URLs
- **Local MCP** — Stdio transport, user runs server locally
- **Hybrid** — Tome, Simtheory offer both options

### 6. Voice and Mobile Frontiers
The MCP ecosystem is expanding beyond desktop:
- **systemprompt** — Voice-controlled MCP management on iOS/Android
- **Jenova** — Production-grade mobile MCP with 97.3% reliability
- **Shortwave** — AI email client with preconfigured integrations

### 7. Framework vs End-User Client Split
Many "no marketplace" clients are actually frameworks/libraries (OpenSumi, NVIDIA AIQ Toolkit, Swarms, Genkit) designed for developers to build MCP-enabled applications rather than end-user tools with discovery features.

---

## Clients Without Marketplace Features — Common Patterns

### Developer Tools/Frameworks
- **NVIDIA AIQ Toolkit** — Enterprise framework, config via mcp_tool_wrapper
- **OpenSumi** — Alibaba IDE framework, not end-user tool
- **Swarms** — Multi-agent orchestration, config via MCP URLs
- **Genkit** — Google/Firebase framework for building agents

### CLI/Terminal Tools
- **y-cli**, **oterm**, **McPico**, **gptme** — Manual config, developer-focused
- **Agent-cli**, **mcp-client-cli** — Config file based

### Specialized/Niche Clients
- **Witsy** — Universal MCP client but no discovery (BYOK model)
- **WhatsMCP** — WhatsApp-specific, connects user-specified servers
- **Zin-MCP-Client** — Reverse engineering focused

### Testing/Development Tools
- **Tester MCP Client** — Apify Actor for testing, not discovery
- **MCPJam** — Inspector/debugging, though has LLM playground

---

## Security Considerations

Several marketplace-enabled clients have implemented security controls:

1. **Enterprise Allowlists** — Claude Desktop, Windsurf, Microsoft Copilot Studio
2. **OAuth 2.1** — Simtheory, Microsoft Copilot Studio, systemprompt
3. **Malware Scanning** — Goose auto-checks extensions
4. **VNet Integration** — Microsoft Copilot Studio
5. **Local Storage** — Tome, RecurseChat emphasize "local first" data control
6. **Pattern-based Allowlists** — VT Code MCP tool policies

The presence of marketplaces introduces supply chain considerations — users may install MCP servers from unknown authors. Enterprise controls and verification badges (Windsurf's blue checkmark) are early mitigation attempts.

---

## Unclear/Unknown Classifications

### Unclear (4)
- **AgentAI** — Limited documentation found
- **AgenticFlow** — JS-heavy site, couldn't verify
- **CodeGPT** — MCP support unclear from available docs
- **LibreChat** — MCP support in development, marketplace status TBD

### Unknown (3)
- **Apify-MCP-Tester** — Primarily a testing tool, marketplace role unclear
- **Qordinate** — Limited public information
- (One additional from earlier batch)

---

## Conclusion

The MCP client ecosystem has rapidly developed marketplace capabilities, with 47% of clients now offering some form of server discovery or registry integration. This shift from "config file only" to "browse and install" mirrors the evolution seen in other developer ecosystems (npm, VS Code extensions, etc.).

**Key Trends:**
1. **Registry consolidation** — Smithery emerging as dominant external registry
2. **Enterprise controls** — Sophisticated allowlisting and security features
3. **Mobile expansion** — MCP reaching iOS/Android via Jenova, systemprompt
4. **Browser extension innovation** — MCP SuperAssistant bringing servers to non-MCP platforms
5. **Major platform adoption** — ChatGPT, Microsoft Copilot Studio joining Claude in MCP support

The presence of marketplaces significantly lowers the barrier to MCP adoption but introduces new considerations around trust, security, and server quality that the ecosystem is beginning to address through verification systems and enterprise controls.

---

## Appendix: Clients by Classification

### YES — Marketplace Features (62)

5ire, AIaW, AIQL-TUUI, Augment-Code, BoltAI, Chatbox, ChatGPT, ChatMCP, Cherry-Studio, Claude-Code, Claude-Desktop, Claude.ai, Cline, Continue, Copilot-MCP, Cursor, DeepChat, eechat, Enconvo, FLUJO, Glama, Glue, Goose, HyperChat, Jenova, JetBrains-AI-Assistant, Kilo-Code, Kiro, Klavis-AI, MCPHub, MCPJam, MCP-SuperAssistant, Microsoft-Copilot-Studio, MindPal, Mistral-AI-Le-Chat, Needle, Nerve, NextChat, Postman, RecurseChat, Roo-Code, Runbear, Shortwave, Simtheory, Smithery-Playground, SpinAI, Superinterface, systemprompt, Tambo, TheiaAI-TheiaIDE, Tome, TypingMind-App, VS-Code-GitHub-Copilot, Warp, Windsurf, Zed, Zencoder

### NO — No Marketplace Features (63)

Agent-cli, Amazon-Q-CLI, Amazon-Q-IDE, Amp, Argo-LocalAI, askit-mcp, Avatar-Shell, BeeAI-Framework, BrowseWiz, Call-Chirp, CarrotAI, Chainlit, ChatFrame, ChatWise, Chorus, ClaudeMind, console-chat-gpt, Daydreams-Agents, Dolphin-MCP, ECA, Emacs-Mcp, fast-agent, FlowDown, Gemini-CLI, Genkit, GenAIScript, gptme, HyperAgent, JetBrains-Junie, kibitz, Langdock, Langflow, LM-Kit.NET, LM-Studio, Lutra, mcp-agent, MCP-Bundler-for-MacOS, MCP-Chatbot, MCP-CLI-client, mcp-client-chatbot, MCP-Simple-Slackbot, mcp-use, MCPCLIHost, MCPOmni-Connect, McPico, Memex, modelcontextchat.com, MooPoint, Msty-Studio, NVIDIA-Agent-Intelligence-toolkit, OpenSumi, oterm, Replit, SeekChat, Simple-AI, Slack-MCP-Client, Superjoin, Swarms, Tencent-CloudBase-AI-DevKit, Tester-MCP-Client, Vercade, VT-Code, WhatsMCP, Witsy, y-cli, Zin-MCP-Client

### Unclear (4)
AgentAI, AgenticFlow, CodeGPT, LibreChat

### Unknown (3)
Apify-MCP-Tester, Qordinate, (+ 1 other)

---

*Report generated from analysis of 132 MCP clients. Data collected December 2025.*
