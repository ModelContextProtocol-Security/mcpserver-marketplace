# MCP Marketplace Dataset

This directory contains per‑marketplace markdown files with YAML frontmatter. Each file represents a marketplace, registry, or marketplace‑like directory (including client‑embedded directories and enterprise/private catalogs).

## Frontmatter Schema (initial)
- title: Human‑readable name
- url: Primary site URL
- source_code_url: Repository or documentation URL (if available)
- is_marketplace: yes/no
- is_aggregator: yes/no
- is_list_of_marketplaces: yes/no
- language: ISO code(s) like en, zh, ja, ko (optional)
- type: (optional) leave blank for now; to be populated later in evaluation (e.g., hosted-catalog, registry-api, client-embedded, diy)
- evidence: List of evidence items
  - url: Supporting link (homepage, docs, blog post, code, etc.)
  - description: Why the link supports classification (e.g., title/quote indicating marketplace behavior)

## Sections (body)
- Overview: short description
- Features: bullets (search, one‑click install, curation, API, updates, client integration)
- Security: notes (moderation, provenance, signing, sandboxing, install boundaries)
- Notes: free‑form

## How files are generated
Run the generator to (re)create or seed files from the canonical CSV:
- CSV: `security-report/datasets/mcp-marketplaces.csv`
- Script: `security-report/datasets/generate_marketplaces_from_csv.py`

Regeneration is idempotent and will not overwrite existing files by default.
