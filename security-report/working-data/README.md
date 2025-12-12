# Working Data

Development datasets used for security report generation. This is the "working copy" - once validated and complete, data syncs to the repo root `data/` directory.

## Datasets

### mcp-marketplaces.csv

Working list of MCP marketplaces (40+ entries).

| Column | Description |
|--------|-------------|
| Marketplace Name | Official name |
| Marketplace URL | Primary URL |
| Source Code URL | GitHub/GitLab if available |
| Is Marketplace | yes/no |
| Is Aggregator | yes/no |
| Is List Of Marketplaces | yes/no (meta-lists) |

**To add marketplaces:**
1. Use `../prompts/mcp-marketplace-discovery-prompt.md`
2. Add rows to this CSV
3. Run `scripts/generate_marketplaces_from_csv.py` to create stub files

**To evaluate marketplaces:**
1. Use `../prompts/marketplace-evaluation-prompt.md`
2. Update the evaluation in `../evaluations/marketplaces/`

### mcp-clients.csv

Working list of MCP clients (130+ entries).

| Column | Description |
|--------|-------------|
| MCP Client Name | Official name |
| MCP Client Main URL | Primary URL |
| MCP Client Source Code URL | GitHub/GitLab if available |
| Listed In modelcontextprotocol.io | Yes/No |

**To add clients:**
1. Add rows to this CSV
2. Create stub file in `../evaluations/clients/`

**To evaluate clients:**
1. Use `../prompts/mcp-client-evaluation-prompt.md`
2. Update the evaluation in `../evaluations/clients/`

## Source Documentation

| File | Description |
|------|-------------|
| [list-of-sources-marketplaces.md](./list-of-sources-marketplaces.md) | Where marketplace data came from |
| [list-of-sources-clients.md](./list-of-sources-clients.md) | Where client data came from |

## Scripts

Located in `scripts/`:

| Script | Purpose |
|--------|---------|
| `extract_mcp_clients.py` | Extract clients from HTML sources |
| `generate_marketplaces_from_csv.py` | Generate stub evaluation files from CSV |

## Raw Sources

Located in `sources/`:

HTML captures of source pages for reproducibility and auditing.

## Data Flow

```
Discovery (prompts/)
    → CSV (working-data/)
    → Stub files (scripts/)
    → Evaluations (evaluations/)
    → Stable data (../data/) [when complete]
```

## Related Files

- **Prompts**: `../prompts/` - Discovery and evaluation prompts
- **Evaluations**: `../evaluations/` - Security evaluation results
- **Stable Data**: `../../data/` - Validated, complete datasets (repo root)
