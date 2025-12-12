# MCP Marketplace Evaluations

Security evaluations for MCP marketplaces, registries, and directories.

## Contents

This directory contains **43 marketplace evaluations** covering:
- Registries (Smithery, MCP Registry, ToolHive)
- Directories (MCP.so, PulseMCP, Glama)
- Curated lists (awesome-mcp-servers)
- Client-embedded marketplaces (Cline, LobeChat, Claude Desktop Extensions)
- Vendor catalogs (Docker MCP Catalog)

## Evaluation Status

| Status | Count | Description |
|--------|-------|-------------|
| Comprehensive | ~4 | Full Tier 0-3 evaluation with evidence |
| Tier 1-2 | ~10 | Automated + some manual checks |
| Stub | ~29 | Minimal frontmatter, needs evaluation |

## Key Evaluations

| Marketplace | Type | Status |
|-------------|------|--------|
| [Smithery](./smithery-playground.md) | Registry/PaaS | Comprehensive |
| [Docker MCP Catalog](./docker-mcp-catalog.md) | Curated Catalog | Comprehensive |
| [MCP.so](./mcp.so.md) | Directory | Comprehensive |
| [ToolHive](./toolhive-registry.md) | Registry | Comprehensive |

## How Files Are Generated

Stub files are generated from the canonical CSV:
- **CSV**: `security-report/working-data/mcp-marketplaces.csv`
- **Script**: `security-report/working-data/scripts/generate_marketplaces_from_csv.py`

Regeneration is idempotent and will not overwrite existing files.

## How to Contribute

1. Pick a marketplace with `Stub` status
2. Read `security-report/prompts/marketplace-evaluation-prompt.md`
3. Use `security-report/templates/marketplace-evaluation-unified-template.md`
4. Run `security-report/tools/tier1_audit.py [URL]` for automated checks
5. Update the evaluation file with findings
6. Submit PR

## Frontmatter Schema

Each file uses YAML frontmatter:

```yaml
---
title: "Marketplace Name"
url: "https://example.com"
source_code_url: "https://github.com/..."
is_marketplace: yes
is_aggregator: yes/no
is_list_of_marketplaces: no
language: "en"
type: "directory | registry-api | code-hosting | paas | client-embedded | curated-list"
evaluation_status: "comprehensive | tier-1-2-moderate | tier-1-basic | stub | blocked"
evidence:
  - url: "https://..."
    description: "What this proves"
---
```

## Template File

Use `000-template.md` as a starting point for new evaluations.
