---
type_id: 6
name: Search Engines and Discovery Tools
risk_level: medium
examples:
  - Google Search
  - Bing
  - DuckDuckGo
  - Specialized MCP search engines (if any emerge)
---

# Search Engines and Discovery Tools

## Definition

General-purpose search engines or specialized tools that index and surface MCP servers. Users find MCP servers through search results, then install from the linked sources.

## Characteristics

- Broad discovery across many sources
- Ranking algorithms influence visibility
- No security vetting
- No verification process
- Mixes trusted and untrusted sources

## Trust Model

- Users generally understand search requires verification
- No implied trust from search engine
- Ranking may inadvertently promote malicious servers

## Security Opportunities

- Can integrate security warnings (like malware warnings)
- Can de-rank known malicious servers
- Can display security badges from trusted sources

## Security Risks

- SEO manipulation (malicious servers rank highly)
- Users may not verify search results
- AI agents using search may lack verification capability
- No accountability for search results

## Evaluation Priority

**Medium** - Users generally understand search requires verification, AI agents may not apply same skepticism, indirect influence on discovery.
