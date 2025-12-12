# MCP Client Marketplace Feature Detection

## Objective

Determine which MCP clients include "marketplace" features - meaning features that influence user choice about which MCP servers to use, rather than just supporting manual configuration of MCP servers.

## Definition of Marketplace Features

A client has marketplace features if it **puts MCP server options in front of the user** rather than requiring the user to already know what servers they want.

### Counts as Marketplace Features

1. **Built-in curated server list**: Pre-configured servers that users can enable/disable (e.g., Claude Desktop's toggleable servers in settings)

2. **External registry integration**: Integration with third-party MCP server registries/marketplaces such as:
   - mcp.run
   - smithery.ai
   - mcpmarket.com
   - glama.ai
   - Composio
   - PulseMCP
   - Other registries

3. **Hosted server catalog**: The client maintains their own browsable directory/catalog of MCP servers

4. **Featured/recommended servers**: UI that highlights or recommends specific servers to users

5. **Search integration**: Ability to search for servers against a registry (the registry choice itself influences what users discover)

6. **One-click install from list**: Installing servers from a provided list or catalog

### Does NOT Count as Marketplace Features

1. **Config file only**: Manual editing of configuration files (e.g., claude_desktop_config.json style)

2. **Generic "add server" UI**: Form where user must provide all server details themselves (name, command, args, etc.)

3. **Documentation links**: Links to general MCP documentation about how to configure servers

4. **Manual URL/path entry**: User must know and enter the server location themselves

**Key distinction**: Does the client influence what servers users see/consider, or must users arrive with prior knowledge of what they want?

## Detection Methodology

### Step 1: Gather Source Material

For each MCP client, collect:

1. **README content** (for clients with source_code_url)
   - Primary source for feature descriptions
   - Usually lists key capabilities

2. **Main website/documentation** (from main_url)
   - Official feature lists
   - Installation/setup guides mentioning server discovery

### Step 2: Keyword Pattern Search

Search collected content for indicators of marketplace features:

#### Curation/Recommendation Keywords
- "featured servers", "popular servers", "recommended servers"
- "server gallery", "server catalog", "server library", "server store"
- "browse servers", "discover servers", "explore servers"
- "marketplace", "registry"
- "one-click install", "install from"
- "enable/disable servers", "toggle servers"
- "built-in servers", "included servers", "default servers", "bundled servers"
- "server directory", "server list"

#### Registry Integration Keywords
- Explicit mentions of known registries: "mcp.run", "smithery", "mcpmarket", "glama", "composio", "pulsemcp"
- "registry integration", "marketplace integration"
- "search servers", "find servers"

#### UI Feature Keywords
- "server browser", "server picker", "server selector"
- "add from catalog", "install from registry"

### Step 3: Classification

Based on findings, classify each client:

#### Classification Values

- **yes**: Clear evidence of marketplace features
- **no**: No evidence of marketplace features (config-only or manual setup)
- **unclear**: Ambiguous - needs manual investigation
- **unknown**: Could not gather sufficient information

#### Evidence Recording

For each client, record:
- `has_marketplace_features`: yes/no/unclear/unknown
- `marketplace_type`: (if yes) built-in-list | registry-integration | hosted-catalog | search-integration | multiple
- `integrated_registries`: (if applicable) list of registry names
- `evidence`: List of items, each with a URL and description of what was found (including relevant quotes, observations, or why it's interesting - even if not directly related to marketplace features)

### Step 4: Output

Update each client's markdown file in `mcp-client-dataset/` with findings in the YAML frontmatter:

```yaml
---
title: "Client Name"
main_url: "https://example.com"
source_code_url: "https://github.com/example/repo"
has_marketplace_features: yes
marketplace_type: registry-integration
integrated_registries:
  - smithery.ai
  - mcp.run
evidence:
  - url: "https://github.com/example/repo#features"
    description: "README Features section - states 'Browse and install MCP servers directly from Smithery marketplace with one-click installation'"
  - url: "https://github.com/example/repo/blob/main/docs/server-installation.md"
    description: "Install docs - describes registry integration, mentions mcp.run search"
  - url: "https://github.com/example/repo/blob/main/src/registries/"
    description: "Source code - found registry integration modules for multiple providers"
---
```

For clients with `has_marketplace_features: no`, still record what was examined:

```yaml
---
title: "Config-Only Client"
main_url: "https://example.com"
source_code_url: "https://github.com/example/repo"
has_marketplace_features: no
evidence:
  - url: "https://github.com/example/repo#configuration"
    description: "README - only describes manual JSON config file editing, no discovery features"
  - url: "https://example.com/docs/setup"
    description: "Setup docs - requires user to specify server command and args manually"
---
```

Record all interesting URLs examined, even if they don't directly answer the marketplace question - this data may be useful for later research stages.

## Privacy, PII, and Scope Policy (must follow)
- Only use public information visible on the client's website/documentation or its directly linked GitHub repository.
- Do not aggregate public information across platforms. Stay platform‑local:
  - Allowed: a cursory look at the linked GitHub repository and its public org page.
  - Not allowed: following links to personal social media, blogs, email archives, forums (e.g., Reddit), or third‑party data brokers.
- Do not collect or store personal emails, postal addresses, phone numbers, or any non‑public data. If public emails appear in commit metadata, do not record them.
- Limit contributor checks to a brief, public‑only glance:
  - View public fields on the GitHub profile (display name, public "company", public website) and public org membership as shown on GitHub.
  - Do not infer beyond what is explicitly public; if unclear, mark "unknown".
- No deanonymization attempts, no cross‑referencing identities, and no scraping beyond the immediate public pages needed for the evaluation.
- Prefer clarity over completeness. When signals are insufficient, record "unknown" with a short note.

## Ownership & Hosting (surface check for MCP clients)
1) Site‑claims (what the client/vendor says)
- From footer/about/privacy/terms, extract any legal entity name and contact email/domain shown.
- Record visible badges/labels (e.g., "Official", "Verified").
- Capture links to GitHub org/repo and social profiles shown on the site.

2) Quick investigative (public, non‑invasive)
- Hosting hints from headers: CDN/edge (Cloudflare/Vercel/CloudFront/Fastly), server banner (nginx/Caddy/OpenResty), obvious framework (Next/Nuxt/etc.).
- DNS basics: NS, A/AAAA, CNAME (hosting context only; do not treat as ownership).
- If a GitHub repo is linked:
  - Repo owner: user vs org; if org, note org "Verified" domain (from org profile banner).
  - CODEOWNERS present? (yes/no).
  - Contributors (cursory, public‑only): list up to 3 recent top contributors with login + display name + public profile "company" or website (if provided). Do not record emails.

3) Cross‑check & confidence (lightweight)
- Compare site‑claimed operator vs GitHub org (and verified domain if shown).
- Set consistency: consistent / partial / mismatch / unknown.
- Add a one‑line confidence note (e.g., "org verified domain matches site; repo owned by org").

### Optional Ownership Fields in Client YAML
You may add the following optional fields to the client's YAML frontmatter when ownership is relevant:

```yaml
operator_claimed:
  name: "Vendor, Inc." # if present
  domain: "vendor.com"  # if present
  sources:
    - "https://client.example.com/privacy"
hosting_hint:
  cdn_edge: "Cloudflare"
  server: "nginx"
  framework: "Next.js"
github_glance:
  repo_owner:
    type: "org"
    name: "vendor-org"
    verified_domain: "vendor.com"
  codeowners_present: true
  contributors_glance:
    - { login: "dev1", name: "Dev One", public_company_or_org: "Vendor" }
consistency: "consistent" # site-claims vs github
confidence_note: "Org verified domain matches site; repo in org"
```

## Known MCP Server Registries/Marketplaces

For reference, these are some known MCP server discovery platforms to look for. Note: A comprehensive registry discovery is planned as a separate stage of this research.

| Registry | URL | Notes |
|----------|-----|-------|
| mcp.run | https://mcp.run | |
| Smithery | https://smithery.ai | |
| MCP Market | https://mcpmarket.com | |
| Glama | https://glama.ai | |
| Composio | https://composio.dev | |
| PulseMCP | https://pulsemcp.com | |
| MCP Hub | https://mcphub.io | |
| MCP.so | https://mcp.so | |

This list is preliminary. Additional registries discovered during client analysis should be noted and will inform the later registry discovery stage.

## Implementation Notes

1. **Rate limiting**: When fetching URLs, respect rate limits and add delays between requests

2. **Caching**: Cache fetched content to avoid repeated requests during development

3. **Fallback**: If README fetch fails, try main_url documentation

4. **Manual review queue**: Generate a list of "unclear" cases for human review

5. **False positive handling**: Some keywords may appear in unrelated contexts - look for contextual confirmation
