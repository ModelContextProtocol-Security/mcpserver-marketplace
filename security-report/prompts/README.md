# Evaluation Prompts

AI prompts for conducting and validating security evaluations.

## Marketplace Prompts

| Prompt | Purpose | When to Use |
|--------|---------|-------------|
| [marketplace-evaluation-prompt.md](./marketplace-evaluation-prompt.md) | Conduct a marketplace evaluation | Evaluating a new marketplace |
| [marketplace-evaluation-validation-prompt.md](./marketplace-evaluation-validation-prompt.md) | Peer-review an evaluation | Validating someone else's evaluation |
| [mcp-marketplace-discovery-prompt.md](./mcp-marketplace-discovery-prompt.md) | Find new marketplaces | Expanding the marketplace list |

## Client Prompts

| Prompt | Purpose | When to Use |
|--------|---------|-------------|
| [mcp-client-evaluation-prompt.md](./mcp-client-evaluation-prompt.md) | Conduct a client evaluation | Evaluating a new MCP client |
| [mcp-client-evaluation-validation-prompt.md](./mcp-client-evaluation-validation-prompt.md) | Peer-review a client evaluation | Validating someone else's evaluation |
| [mcp-client-marketplace-detection-prompt.md](./mcp-client-marketplace-detection-prompt.md) | Detect marketplace features in clients | Analyzing client marketplace integration |

## Other Prompts

| Prompt | Purpose |
|--------|---------|
| [mcp-marketplace-security-evaluation-prompt.md](./mcp-marketplace-security-evaluation-prompt.md) | Comprehensive security evaluation (older, detailed) |

## Workflow

### Evaluating a Marketplace
1. Use `marketplace-evaluation-prompt.md` with the unified template
2. Run `tools/tier1_audit.py` for automated checks
3. Have another AI validate using `marketplace-evaluation-validation-prompt.md`

### Evaluating a Client
1. Use `mcp-client-evaluation-prompt.md` with the client template
2. Have another AI validate using `mcp-client-evaluation-validation-prompt.md`

### Discovering New Marketplaces
1. Use `mcp-marketplace-discovery-prompt.md`
2. Add findings to `working-data/mcp-marketplaces.csv`
3. Generate stub files with `working-data/scripts/generate_marketplaces_from_csv.py`

## Related Files

- **Templates**: `../templates/` - Output formats for evaluations
- **Tools**: `../tools/` - Automated audit scripts
- **Working Data**: `../working-data/` - CSV datasets and sources
