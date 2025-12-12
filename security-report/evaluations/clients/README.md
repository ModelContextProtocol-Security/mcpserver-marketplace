# MCP Client Evaluations

Security evaluations for MCP clients' marketplace behavior and security posture.

## Contents

This directory contains **134 client evaluation files** covering:
- Desktop applications (Claude Desktop, Cursor, VS Code extensions)
- CLI tools (mcp-cli, mcpx, Amazon Q CLI)
- Web applications (LobeChat, LibreChat)
- Framework integrations (LangChain, Semantic Kernel)
- IDE plugins and extensions

## Evaluation Status

Most files are stubs awaiting detailed evaluation. Completed evaluations:

| Client | Date | Status | Link |
|--------|------|--------|------|
| Claude Desktop | 2025-11-19 | Comprehensive | [claude-desktop/](./claude-desktop/) |

## How to Contribute

1. Pick a client from `security-report/working-data/mcp-clients.csv`
2. Read `security-report/prompts/mcp-client-evaluation-prompt.md`
3. Use `security-report/templates/mcp-client-evaluation.md`
4. Create or update the evaluation file
5. Submit PR

## Evaluation Focus Areas

Unlike marketplace evaluations, client evaluations focus on:

1. **Marketplace Integration** - Built-in discovery, one-click install
2. **Installation Security** - How servers are installed and configured
3. **Runtime Security** - Sandboxing, permission models, isolation
4. **Credential Storage** - How API keys and secrets are handled
5. **Update Mechanisms** - How server updates are managed
6. **Enterprise Controls** - Policy enforcement, admin controls

## Why Client Evaluations Matter

The client is where marketplace security becomes real - it's the installation and runtime environment. A secure marketplace means nothing if the client:
- Runs servers with full user permissions
- Stores credentials in plaintext
- Auto-updates without verification
- Has no permission model for tool access

## File Naming

Files are named after the client: `client-name.md`

For clients with detailed evaluations (multiple documents, screenshots, etc.), use a subdirectory: `client-name/README.md`
