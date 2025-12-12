# MCP Marketplace Discovery and Classification Prompt

## Objective
Build and maintain a comprehensive list of MCP marketplaces, registries, and marketplace-like directories (including client-embedded directories and enterprise/private catalogs). Capture both English and non‑English sources.

## What Counts
- Actual marketplaces/registries/directories that put MCP servers in front of users (browsing, search, curation, one‑click install, API access, etc.).
- Client-embedded marketplaces (e.g., Claude Desktop Extensions Directory, client app has a curated directory/installer UI).
- Enterprise/private registries and gateways (e.g., ToolHive, Archestra) exposing catalogs to users.
- Meta-lists/browsers that aggregate MCP servers via the official registry or other sources (e.g., MCP Bench, Datasette browsers, TeamSpark ToolCatalog).

## What Does Not Count
- Single MCP server repositories (unless they host a catalog/registry for others).
- Generic blog posts that do not list or link to multiple marketplaces/registries.

## Discovery Hints (Keywords)
- English: "MCP marketplace", "MCP registry", "MCP directory", "MCP catalog", "MCP server search", "MCP install".
- Chinese: "MCP 市场", "MCP 服务市场", "MCP 导航", "MCP 目录", "MCP 注册/注册表".
- Japanese: "MCP マーケットプレイス", "MCP ディレクトリ", "MCP レジストリ".
- Korean: "MCP 마켓플레이스", "MCP 레지스트리", "MCP 디렉터리".
- Also search by specific marketplace names to uncover related lists (mcp.so, MCP Hub, PulseMCP, ToolHive, Docker MCP, Smithery, MCP Market, Glama, mcp.run, MCP Bench, TeamSpark ToolCatalog, Datasette browser, Archestra, mcpm.sh, Cline Marketplace, LobeChat Marketplace, etc.).

## Classification Fields
For each candidate, capture the following fields:
- name
- url
- source_code_url (repo or docs if available)
- is_marketplace (yes/no)
- is_aggregator (yes/no)
- is_list_of_marketplaces (yes/no) — set to yes only for pages that enumerate multiple marketplace sites
- language (en, zh, ja, ko, es, etc.)
- evidence: list of { url, description or quote }

### Ownership & Hosting (surface) – Optional Extended Fields
- operator_claimed: { name?, domain?, sources: [urls] }
- hosting_hint: { cdn_edge?, server?, framework?, deployment_hint? }
- github_glance (if a repo/org is linked on the site):
  - repo_owner: { type: "org|user", name, verified_domain? }
  - codeowners_present: true|false
  - contributors_glance: [{ login, name?, public_company_or_org? }] (limit to a few, public-only)
- policy_status: { privacy, terms, security, robots, sitemap } (HTTP codes)
- api_status: { api, docs, openapi_json, openapi_yaml, swagger_json } (HTTP codes or "ghost" if returns HTML)
- consistency: "consistent|partial|mismatch|unknown" (site-claims vs investigative)
- confidence_note: short text

## Output Target
- CSV row in `security-report/working-data/mcp-marketplaces.csv` with: Marketplace Name, Marketplace URL, Source Code URL, Is Marketplace, Is Aggregator, Is List Of Marketplaces
- If additional metadata (language, features, security notes) is collected, record them in a per‑entry note in `security-report/working-data/list-of-sources-marketplaces.md` or a future per‑marketplace markdown file.

## Evidence Examples
- "Title shows MCP Directory / Marketplace"
- "Install flow / one‑click installation mentioned"
- "Browse/search across N servers"
- "Implements MCP Registry API / subregistry per official OpenAPI"
- "Client settings include curated list with toggles"

## Process
1) Start from known seeds (existing CSV and markdown files) and follow links.
2) Search GitHub repos and code for marketplace/registry keywords in multiple languages.
3) Search on the open web for marketplace sites and roundup posts; prefer first‑party sources.
4) Add or update CSV entries; add sources to the markdown list.
5) Mark roundup posts listing multiple marketplaces with `is_list_of_marketplaces: yes`.
6) When ambiguous, set `is_marketplace: no` and add to a manual review queue.

## Privacy, PII, and Scope Policy (must follow)
- Only use public information visible on the target page or its directly linked GitHub repository.
- Do not aggregate public information across platforms. Stay platform‑local:
  - Allowed: a cursory look at the linked GitHub repository and its public org page.
  - Not allowed: following links to personal social media, blogs, email archives, forums (e.g., Reddit), or third‑party data brokers.
- Do not collect or store personal emails, postal addresses, phone numbers, or any non‑public data. If public emails appear in commit metadata, do not record them.
- Limit contributor checks to a brief, public‑only glance:
  - View public fields on the GitHub profile (display name, public "company", public website) and public org membership as shown on GitHub.
  - Do not infer beyond what is explicitly public; if unclear, mark "unknown".
- No deanonymization attempts, no cross‑referencing identities, and no scraping beyond the immediate public pages needed for the evaluation.
- Prefer clarity over completeness. When signals are insufficient, record "unknown" with a short note.

## Ownership & Hosting (surface check)
1) Site‑claims (what the site says)
- From footer/about/privacy/terms, extract any legal entity name and contact email/domain shown.
- Record visible badges/labels (e.g., "Official", "Verified", "Vendor").
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

## Quality Checks
- Avoid duplicates; prefer canonical names/URLs.
- For 403/blocked pages, note reachability but keep the entry if it is known and accessible via standard browsers.
- Keep evidence URLs for traceability.

---

## Single‑Shot System Prompt (for use with web-enabled assistants)
"""
You are mapping the MCP (Model Context Protocol) marketplace ecosystem.
Return a JSON array of marketplaces, registries, or marketplace-like directories (including client-embedded directories) with fields:
- name, url, source_code_url (if any), is_marketplace (yes/no), is_aggregator (yes/no), is_list_of_marketplaces (yes/no), language, evidence: [{url, note}]

Also include ownership/hosting (surface) fields when available:
- operator_claimed: { name?, domain?, sources: [urls] }
- hosting_hint: { cdn_edge?, server?, framework?, deployment_hint? }
- github_glance (if a repo/org is linked on the site): { repo_owner: { type, name, verified_domain? }, codeowners_present: bool, contributors_glance: [{ login, name?, public_company_or_org? }] }
- policy_status: { privacy, terms, security, robots, sitemap }
- api_status: { api, docs, openapi_json, openapi_yaml, swagger_json }
- consistency: "consistent|partial|mismatch|unknown"
- confidence_note: short text

Scope:
- Include English and non‑English sources (Chinese, Japanese, Korean, Spanish are priorities).
- Include enterprise/private registries if they present a browsable catalog (e.g., ToolHive, Archestra).
- Include registry browsers (MCP Bench, Datasette browser, TeamSpark ToolCatalog).
- Include client‑embedded marketplaces (Claude Desktop Extensions, Cline Marketplace, LobeChat Marketplace).
- Include vendor catalogs (Docker MCP Catalog).
- Exclude individual MCP servers unless they host multi‑server registries.

For each item, add at least 2 evidence links (homepage plus one supporting page with a title/quote indicating marketplace/registry features).
Avoid duplicates; prefer canonical names.

Privacy, PII, and scope policy (must follow):
- Only use public information visible on the target page or its directly linked GitHub repository.
- Do not aggregate public information across platforms (do not follow personal social links, email archives, forums, or third‑party data brokers).
- Do not collect or store personal emails, postal addresses, phone numbers, or any non‑public data. If public emails appear in commit metadata, do not record them.
- Limit contributor checks to a brief, public‑only glance (display name, public "company", public website, public org memberships on GitHub). Do not infer beyond what is explicitly public; if unclear, mark "unknown".
- No deanonymization, no cross‑referencing identities, and no scraping beyond immediate public pages needed for the evaluation.
"""
