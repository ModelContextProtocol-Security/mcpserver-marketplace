---
type_id: 2
name: Built-in Application Marketplace
risk_level: medium
examples:
  - Claude Desktop Extensions
  - ChatGPT MCP integration
  - Cursor MCP support
  - Windsurf AI
---

# Built-in Application Marketplace

## Definition

MCP server installation/discovery features built into AI client applications. The application vendor curates and controls what servers are available.

## Characteristics

- Integrated user experience
- Application vendor curates selection
- Installation automated/simplified
- May be limited to vendor-approved servers
- May pull from external registries
- Verification standards vary by vendor

## Trust Model

- Users trust application vendor
- Vendor responsible for curation
- May delegate to external registries
- Vendor brand reputation at stake

## Security Opportunities

- Vendor can enforce strict requirements
- Sandboxing integrated into application
- Permissions UI in application
- Monitoring at application level
- Vendor security team oversight

## Security Risks

- Users may over-trust vendor curation
- Unclear verification standards
- May not disclose source of MCP servers
- Limited transparency about security vetting

## Evaluation Priority

**Highest** - Directly impacts users of major AI applications, vendor reputation creates (possibly false) sense of security, often first exposure to MCP servers for users.

## Critical Questions

1. What verification does vendor perform?
2. Where do MCP servers come from (own registry, external)?
3. What security guarantees does vendor make?
4. How are malicious servers detected and removed?
5. Is vendor's security posture transparent?
