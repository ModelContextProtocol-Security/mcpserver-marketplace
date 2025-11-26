---
type_id: 4
name: Code Hosting and Distribution
risk_level: medium
examples:
  - Smithery.ai
  - Glama.ai
  - GitHub (modelcontextprotocol/servers)
  - GitLab
---

# Code Hosting and Distribution

## Definition

Platforms that host MCP server source code and facilitate sharing/installation. May provide one-click deployment or require manual setup.

## Characteristics

- Source code hosting and version control
- Installation instructions or automation
- May provide one-click deployment
- Security vetting varies
- May pull dependencies from external sources

## Trust Model

- Users trust platform's infrastructure security
- Developer reputation-based for code quality
- May leverage platform verification (GitHub verified orgs)
- Code review possible but not guaranteed

## Security Opportunities

- Source code available for inspection
- Commit history provides transparency
- Can integrate security scanning (GitHub Advanced Security)
- Can link to CI/CD provenance
- Community code review possible

## Security Risks

- **One-click deployment may bypass review**
- Source code doesn't guarantee safety (obfuscation possible)
- Dependencies pulled at runtime may be malicious
- Developer account compromise
- Limited security vetting before deployment

## Evaluation Priority

**High** - Platforms like Smithery provide instant deployment (high friction reduction), GitHub widely trusted (may create false sense of security), source availability doesn't equal security review.

## Critical Questions

1. Is code review required or encouraged?
2. Are dependencies scanned for vulnerabilities?
3. Is one-click deployment sandboxed?
4. What happens if source account compromised?
5. Is deployment tracked/auditable?

## Notable Incidents

- **Smithery.ai (2025)**: Path traversal vulnerability compromised 3,000+ servers and exposed thousands of API keys.
