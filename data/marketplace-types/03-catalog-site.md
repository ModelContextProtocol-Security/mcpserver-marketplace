---
type_id: 3
name: Informational Catalog Site
risk_level: medium-high
examples:
  - MCP.so
  - mcpservers.org
  - PulseMCP
  - Awesome MCP Servers lists
---

# Informational Catalog Site

## Definition

Websites that list, describe, and categorize MCP servers without directly facilitating installation. Users discover servers here, then install them elsewhere.

## Characteristics

- Aggregates information from various sources
- Categorization and search
- Descriptions and documentation links
- Typically no direct installation
- Verification varies widely
- Update frequency varies

## Trust Model

- Community-driven or organization-maintained
- Users must verify information independently
- No installation responsibility (informational only)
- Reputation-based curation

## Security Opportunities

- Can display security metadata (if available)
- Can link to verification sources
- Can flag known issues
- Can provide security ratings

## Security Risks

- **AI agents may treat catalog as authoritative**
- No verification requirement for listings
- Outdated information persists
- No mechanism to remove malicious listings quickly
- Users may copy-paste installation commands without verification

## Evaluation Priority

**High** - Widely referenced and linked, AI agents may scrape these for recommendations, information persists even if outdated, no accountability for listing malicious servers.

## Critical Questions

1. What verification is required for listings?
2. How quickly are malicious listings removed?
3. Is security information displayed?
4. Do listings link to trusted sources?
5. Is listing criteria transparent?
6. Who can submit listings?
