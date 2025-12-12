# Evaluation Templates

Output formats for security evaluations.

## Marketplace Templates

| Template | Purpose |
|----------|---------|
| [marketplace-evaluation-unified-template.md](./marketplace-evaluation-unified-template.md) | **Main template** - questionnaire + report + audit fields |
| [marketplace-evaluation-outreach-template.md](./marketplace-evaluation-outreach-template.md) | Email templates for contacting operators |

## Client Templates

| Template | Purpose |
|----------|---------|
| [mcp-client-evaluation.md](./mcp-client-evaluation.md) | Client security evaluation template |

## How to Use

### Marketplace Evaluation
1. Copy `marketplace-evaluation-unified-template.md`
2. Follow `prompts/marketplace-evaluation-prompt.md` for guidance
3. Run `tools/tier1_audit.py [URL]` to populate Part 7 (Technical Security)
4. Save to `evaluations/marketplaces/[name].md`

### Client Evaluation
1. Copy `mcp-client-evaluation.md`
2. Follow `prompts/mcp-client-evaluation-prompt.md` for guidance
3. Save to `evaluations/clients/[name].md`

### Contacting Operators
1. Use `marketplace-evaluation-outreach-template.md` for email templates
2. Attach the completed evaluation for their review
3. Track responses in the evaluation's metadata section

## Template Design

The unified marketplace template serves three purposes:
1. **Questionnaire** - Structured Q&A for operators to verify
2. **Report Format** - Final published evaluation
3. **Audit Target** - Fields auto-populated by tier1_audit.py

## Related Files

- **Prompts**: `../prompts/` - Instructions for using these templates
- **Tools**: `../tools/` - Automated checks that feed into templates
- **Evaluations**: `../evaluations/` - Completed evaluations using these templates
