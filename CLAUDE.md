# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **MCP Marketplace Security** project, part of the Cloud Security Alliance's Model Context Protocol Security initiative. It evaluates security practices of MCP marketplaces (registries, directories, catalog sites) and how MCP clients handle server discovery/installation.

## Repository Structure

- `data/` - Stable reference datasets (CSV files for marketplaces, clients, vendors)
- `security-report/` - Primary project directory containing:
  - `working-data/` - Development datasets and audit results
  - `evaluations/` - Security evaluation markdown files (40+ marketplaces, 130+ clients)
  - `tools/` - Python audit toolkit
  - `prompts/` - AI evaluation prompts
  - `templates/` - Evaluation templates
  - `patterns/` - Reusable evaluation frameworks

## Audit Tools

The `security-report/tools/` directory contains a modular Python audit package:

```bash
# Run from security-report/tools/ directory

# Single marketplace audit (domain + web checks)
python audit.py https://mcp.so --format summary

# Include repository checks
python audit.py https://mcp.so --repo https://github.com/chatmcp/mcpso

# Individual module checks
python -m mcp_audit.domain mcp.so
python -m mcp_audit.web https://mcp.so
python -m mcp_audit.repo https://github.com/owner/repo

# Batch audit all marketplaces from CSV
python batch_audit.py
python batch_audit.py --dry-run    # Preview
python batch_audit.py --limit 5    # Test subset
```

### Tool Dependencies

The audit tools use shell commands (`curl`, `dig`, `openssl`) - no pip dependencies required. Set `GITHUB_TOKEN` environment variable for GitHub API rate limits.

### mcp_audit Package

| Module | Input | Checks |
|--------|-------|--------|
| `domain.py` | hostname | DNS records, TLS certificate, provider detection |
| `web.py` | URL | HTTP status, 9 security headers, path probes, trackers, social links |
| `repo.py` | GitHub URL | SECURITY.md, org verification, activity metrics, security features |

## Evaluation Workflow

This project uses a **two-AI model**: one AI creates evaluations, another validates them.

1. Check `working-data/mcp-marketplaces.csv` for evaluation status
2. Check `working-data/audit-results/YYYY-MM-DD/` for pre-collected JSON data
3. Create evaluation using `templates/marketplace-evaluation-unified-template.md`
4. Place in `evaluations/marketplaces/` or `evaluations/clients/`
5. Validate using the validation prompts in `prompts/`

## Data Model

**Two-tier data:**
- `security-report/working-data/` - Development datasets (active work)
- `data/` (repo root) - Stable reference datasets (synced when validated)

**CSV schemas:** See README.md files in each data subdirectory.

## Key Files

- `security-report/README.md` - Full project documentation
- `security-report/patterns/checks.md` - Security checks we look for
- `security-report/patterns/evaluation-criteria.md` - Detailed criteria
- `security-report/prompts/marketplace-evaluation-prompt.md` - How to evaluate
