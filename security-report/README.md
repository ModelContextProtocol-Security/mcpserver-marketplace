# MCP Marketplace Security Evaluation Project

Systematically evaluating MCP marketplaces and how MCP clients handle server installation.

## What We're Evaluating

1. **Marketplaces** - Where users discover MCP servers (registries, catalogs, AI recommendations, etc.)
2. **MCP Clients** - How they install, configure, permission, and sandbox MCP servers

## Project Status

**In Progress**

See the [project goals](./MCP-MARKETPLACE-SECURITY-EVAL-GOALS.md) for full details.

## Directory Structure

```
security-report/
├── README.md                   # You are here
├── MCP-MARKETPLACE-SECURITY-EVAL-*.md  # Project governance docs
│
├── templates/                  # Evaluation templates
│   ├── marketplace-evaluation.md
│   └── mcp-client-evaluation.md
│
├── patterns/                   # Reusable evaluation frameworks
│   ├── checks.md               # Security checks we look for
│   ├── evaluation-criteria.md  # Detailed criteria and gaps
│   └── trust-signals.md        # What good looks like
│
├── evaluations/                # Completed evaluations
│   ├── marketplaces/
│   └── mcp-clients/
│       └── claude-desktop/     # Example completed evaluation
│
├── research/                   # Background research
│   └── lessons-from-package-registries.md
│
└── conversations/              # Working notes and synthesis
```

## How to Contribute

**Want to evaluate a marketplace or MCP client?**

1. Use a template from `templates/`
2. Submit a PR to `evaluations/`

**Think we're missing a security check?**

Edit `patterns/checks.md` or file an issue.

**Have feedback on the framework?**

File an issue to discuss.

## Completed Evaluations

| Target | Type | Date | Link |
|--------|------|------|------|
| Claude Desktop | MCP Client | 2025-11-19 | [Evaluation](./evaluations/mcp-clients/claude-desktop/) |

## Related Documents

- [Evaluation Criteria](./patterns/evaluation-criteria.md) - Detailed criteria and identified gaps
- [Security Checks](./patterns/checks.md) - What we look for
- [Project Goals](./MCP-MARKETPLACE-SECURITY-EVAL-GOALS.md) - Full project objectives
- [Contributing Guidelines](./MCP-MARKETPLACE-SECURITY-EVAL-CONTRIBUTING.md) - How to participate
