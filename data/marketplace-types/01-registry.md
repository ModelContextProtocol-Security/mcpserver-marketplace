---
type_id: 1
name: Registry Marketplace
risk_level: lower
examples:
  - Official MCP Registry
  - GitHub MCP Registry
  - Docker MCP Catalog
---

# Registry Marketplace

## Definition

Traditional package registry model with centralized hosting, search, and distribution. The operator controls publication and can enforce security requirements.

## Characteristics

- Centralized package hosting
- Publisher accounts and authentication
- Search and discovery interface
- Version management
- Download/installation APIs
- Metadata and documentation hosting
- May have security scanning
- May have verification processes

## Trust Model

- Registry operator controls publication
- Can enforce security requirements
- Can scan before publication
- Can remove malicious packages
- Single point of accountability

## Security Opportunities

- Mandatory 2FA for publishers
- Automated malware scanning
- Namespace management
- Provenance attestation
- Runtime sandboxing integration
- Centralized incident response

## Security Risks

- Single point of failure
- Centralized compromise impact
- Operator trust required
- Scaling challenges for security review

## Evaluation Priority

**Highest** - Most control over security, best opportunity to implement package registry lessons, centralized enforcement possible.
