# Evaluation Patterns

Reusable frameworks and criteria for security evaluations.

## Documents

| File | Purpose |
|------|---------|
| [checks.md](./checks.md) | Security checks we look for in evaluations |
| [evaluation-criteria.md](./evaluation-criteria.md) | Detailed criteria with gaps and future work |
| [marketplace-security-checklist.md](./marketplace-security-checklist.md) | Comprehensive security checklist |
| [trust-signals.md](./trust-signals.md) | What "good" looks like - positive indicators |

## How to Use

### When Creating Evaluation Criteria
- Start with `checks.md` for the baseline
- Expand using `evaluation-criteria.md` for detailed requirements
- Reference `trust-signals.md` for positive examples

### When Evaluating
- Use `marketplace-security-checklist.md` as a comprehensive checklist
- Reference `trust-signals.md` to identify strengths
- Use `checks.md` for quick reference

### When Improving the Framework
- Add new checks to `checks.md`
- Document gaps in `evaluation-criteria.md`
- Update templates in `../templates/` to reflect new criteria

## Evaluation Tiers

From `evaluation-criteria.md`:

| Tier | Focus | Checks |
|------|-------|--------|
| Tier 0 | Classification | Type, delivery model, source accessibility |
| Tier 1 | Automated/Observable | HTTPS, headers, DNS, policy endpoints |
| Tier 2 | Manual Investigation | Privacy policy, ToS, publisher verification |
| Tier 3 | Registry-Specific | 2FA, malware scanning, signing, provenance |

## Related Files

- **Prompts**: `../prompts/` - Use patterns in evaluation prompts
- **Templates**: `../templates/` - Patterns inform template structure
- **Research**: `../research/` - Background research informing patterns
