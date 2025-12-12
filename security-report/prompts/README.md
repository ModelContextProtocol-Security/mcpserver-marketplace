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

## Evaluation Lifecycle

The project uses a **two-AI model**: one AI creates, another AI validates. This catches errors and reduces bias.

```
Discovery → Creation → Validation → Publication
```

### Phase 1: Discovery

**Goal**: Find marketplaces/clients to evaluate

| Task | Prompt | Output |
|------|--------|--------|
| Find marketplaces | `mcp-marketplace-discovery-prompt.md` | Add to `working-data/mcp-marketplaces.csv` |
| Generate stubs | Run `working-data/scripts/generate_marketplaces_from_csv.py` | Stub files in `evaluations/marketplaces/` |

### Phase 2: Creation (Evaluation AI)

**Goal**: Produce initial evaluation

**For Marketplaces:**
1. Pick a marketplace from `working-data/mcp-marketplaces.csv`
2. Use `marketplace-evaluation-prompt.md`
3. Use template `../templates/marketplace-evaluation-unified-template.md`
4. Run `../tools/tier1_audit.py [URL]` for automated checks
5. Save to `../evaluations/marketplaces/[name].md`

**For Clients:**
1. Pick a client from `working-data/mcp-clients.csv`
2. Use `mcp-client-evaluation-prompt.md`
3. Use template `../templates/mcp-client-evaluation.md`
4. Save to `../evaluations/clients/[name].md`

### Phase 3: Validation (Validation AI)

**Goal**: Peer-review the evaluation, catch errors

| Task | Prompt | What It Checks |
|------|--------|----------------|
| Validate marketplace eval | `marketplace-evaluation-validation-prompt.md` | Factual accuracy, completeness, missed findings |
| Validate client eval | `mcp-client-evaluation-validation-prompt.md` | Factual accuracy, completeness, missed findings |

The Validation AI:
- Re-runs key checks independently
- Compares findings with the original evaluation
- Flags discrepancies, errors, or low-confidence claims
- Produces a validation report

### Phase 4: Publication

**Goal**: Finalize and optionally contact operator

1. Address validation findings
2. Update evaluation status in CSV
3. Optionally use `../templates/marketplace-evaluation-outreach-template.md` to contact operator
4. Mark as "Operator Verified" if they confirm findings

## Why Two AIs?

From `../VALIDATION_GOALS.md`:
- **Trust, but Verify**: No single AI's output is accepted without verification
- **Catches errors**: Factual inaccuracies, missed endpoints, omissions
- **Reduces bias**: Different AI may catch systematic bias in evaluations
- **Full traceability**: All validation logged for audit history

## Quick Reference

| I want to... | Use this prompt |
|--------------|-----------------|
| Evaluate a marketplace | `marketplace-evaluation-prompt.md` |
| Validate a marketplace eval | `marketplace-evaluation-validation-prompt.md` |
| Evaluate a client | `mcp-client-evaluation-prompt.md` |
| Validate a client eval | `mcp-client-evaluation-validation-prompt.md` |
| Find new marketplaces | `mcp-marketplace-discovery-prompt.md` |
| Detect marketplace features in a client | `mcp-client-marketplace-detection-prompt.md` |

## Related Files

- **Templates**: `../templates/` - Output formats for evaluations
- **Tools**: `../tools/` - Automated audit scripts
- **Working Data**: `../working-data/` - CSV datasets and sources
