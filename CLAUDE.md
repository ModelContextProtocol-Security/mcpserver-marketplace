# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

The **MCP Marketplace Security** project, part of the Cloud Security Alliance's Model Context
Protocol Security initiative. It evaluates the security practices of MCP marketplaces
(registries, directories, catalog sites) and how MCP clients handle server discovery and
installation.

This is a **data-and-methodology repo, not an application**. There is no build, no test suite,
and no pip dependencies. Most work is: editing CSV datasets, writing evidence-backed Markdown
evaluations, and running the read-only Python audit toolkit against public websites.

## Commands

```bash
# CSV field-count validation (what CI runs)
python3 scripts/validate_csv.py                  # all data/*.csv
python3 scripts/validate_csv.py data/foo.csv     # specific file(s)

# Audit toolkit — run from security-report/tools/
python audit.py https://mcp.so                              # domain + web, JSON (default)
python audit.py https://mcp.so --format summary             # human-readable
python audit.py https://mcp.so --repo https://github.com/chatmcp/mcpso
python audit.py --domain mcp.so                             # single check type
python audit.py --web https://mcp.so
python audit.py --repo https://github.com/owner/repo

# Modules are individually runnable
python -m mcp_audit.domain mcp.so
python -m mcp_audit.web https://mcp.so
python -m mcp_audit.repo https://github.com/owner/repo

# Batch audit every marketplace in the working-data CSV
python batch_audit.py --dry-run                  # preview targets
python batch_audit.py --limit 5                  # test on a subset
python batch_audit.py --workers 8                # default 8 parallel workers
python batch_audit.py                            # full run
```

`batch_audit.py` defaults: `--csv ../working-data/mcp-marketplaces.csv`,
`--output-dir ../working-data/audit-results`. It writes `<output-dir>/<UTC date>/<slug>.json`
plus an `index.json` manifest, where `<slug>` is the marketplace name lowercased,
non-alphanumerics stripped, spaces/dashes collapsed, truncated to 50 chars.

**Requirements:** Python 3.10+ and the system binaries `curl`, `dig`, `openssl`. No pip
packages. Set `GITHUB_TOKEN` (or pass `--github-token`) to avoid GitHub API rate limits on
repo checks.

**Audits hit live third-party sites.** A full `batch_audit.py` run makes hundreds of requests
to other people's infrastructure — use `--dry-run` / `--limit` while iterating, and don't
re-run the full sweep casually.

## Two-Tier Data Model — and the schema break between the tiers

| Tier | Location | Role |
|------|----------|------|
| Working | `security-report/working-data/*.csv` | Active development; where discovery lands |
| Stable | `data/*.csv` | Validated reference datasets; what CI checks and what the README links |

**The two tiers do not share a schema.** Promoting data is a transform, never a copy/paste:

- `working-data/mcp-marketplaces.csv` → `Marketplace Name, Marketplace URL, Source Code URL,
  Is Marketplace, Is Aggregator, Is List Of Marketplaces, Evaluation Status`
- `data/marketplaces.csv` → `id, name, type, url, operator, status, server_count, priority,
  last_verified, notes`
- `working-data/mcp-clients.csv` → `MCP Client Name, MCP Client Main URL,
  MCP Client Source Code URL, Listed In modelcontextprotocol.io`
- `data/mcp-clients.csv` → `id, name, vendor, url, type, status, has_builtin_marketplace,
  marketplace_name, allows_manual_config, config_method, runtime_sandboxing,
  permission_model, last_verified, notes`

`data/vendors.csv` exists with a header and zero rows — the vendor registry is planned, not
started.

Field-level schemas live in the README of each `data/` subdirectory
(`data/marketplaces/README.md`, `data/mcp-clients/README.md`, `data/marketplace-types/README.md`).

## Evaluation Workflow

The project runs a **two-AI model**: one AI produces an evaluation, a second AI independently
peer-reviews it (`prompts/*-validation-prompt.md`, rationale in `VALIDATION_GOALS.md`).

```
Discovery (prompts/) → working-data CSV → stub files (scripts/) → evaluations/ → data/ (when validated)
```

To evaluate a marketplace:

1. Pick a target from `security-report/working-data/mcp-marketplaces.csv`.
2. Check `security-report/working-data/audit-results/<date>/<slug>.json` — the automated data
   may already be collected; don't re-hit the site for it.
3. Follow `security-report/prompts/marketplace-evaluation-prompt.md`.
4. Fill `security-report/templates/marketplace-evaluation-unified-template.md`.
5. Save to `security-report/evaluations/marketplaces/<slug>.md`.
6. Peer-review with `prompts/marketplace-evaluation-validation-prompt.md`.

Clients follow the same shape with `mcp-client-evaluation-prompt.md`,
`templates/mcp-client-evaluation.md`, and `evaluations/clients/`.

### Tier model (Tier 0–3)

Every evaluation is structured by escalating tiers, defined in `patterns/evaluation-criteria.md`:

| Tier | Focus |
|------|-------|
| 0 | Classification — type, delivery model, source accessibility |
| 1 | Automated / observable — HTTPS, security headers, DNS, policy endpoints (this is what the audit tools cover) |
| 2 | Manual investigation — privacy policy, ToS, publisher verification |
| 3 | Registry-specific — 2FA, malware scanning, signing, provenance |

The audit JSON maps onto specific template sections; the mapping table is in
`security-report/tools/README.md` under "Output Integration".

### Evidence convention

Evaluations are YAML frontmatter + Markdown, and **every security claim is backed by a URL** in
the frontmatter `evidence:` list (`- url:` / `description:` pairs). Marketplace evaluations
additionally carry `title, url, source_code_url, is_marketplace, is_aggregator,
is_list_of_marketplaces, type, operator, server_count, last_evaluated`. Match the frontmatter
of a neighboring file rather than inventing fields, and never state a finding without an
evidence URL that supports it.

## CSV validation (CI)

`scripts/validate_csv.py` checks that every row in a CSV has the same field count as its
header — catching the two classic hand-edited-CSV bugs: a trailing comma (extra empty field)
and an unquoted comma inside a value (splits one field in two). It uses the stdlib `csv`
parser, so commas inside properly *quoted* fields are fine.

`.github/workflows/validate-csv.yml` runs it on any PR touching `data/*.csv` or the validator,
and on push to `main`.

**Two limits worth knowing:**
- CI validates `data/*.csv` only, **not** `security-report/working-data/`. Run the validator
  by hand (`python3 scripts/validate_csv.py security-report/working-data/*.csv`) before
  promoting working-data upward.
- It checks field *counts* only — not enum values, not required fields, not dates. Nothing
  enforces the documented `type` vocabulary, and two rows in `data/marketplaces.csv` already
  drift from it (`databricks-mcp-marketplace` uses `marketplace`, `mcp-universe` uses
  `research-dataset`; neither is one of the 8 types in `data/marketplace-types/`).

## Repository Layout Notes

- `security-report/` — the primary project: `evaluations/` (52 marketplace files,
  134 client files), `tools/`, `prompts/`, `templates/`, `patterns/`, `research/`,
  `reports/`, `working-data/`.
- `tools/` at the repo root is an **empty placeholder** (README of planned ideas only). The
  real toolkit is `security-report/tools/`. Don't confuse the two.
- `guidance/` is a stub. `GEMINI.md` is a zero-byte file.
- Governance docs live at `security-report/MCP-MARKETPLACE-SECURITY-EVAL-*.md`;
  roadmap in `security-report/TODO.md`.

## Gotchas

- **`tier1_audit.py` vs `audit.py`.** `tools/README.md` calls `tier1_audit.py` legacy and says
  to prefer `audit.py`, but `prompts/README.md` and `templates/README.md` still instruct
  evaluators to run `tier1_audit.py`. Use `audit.py` for new work; treat the prompt/template
  references as stale.
- **`batch_audit_marketplaces.py` is broken.** Its `DATA_DIR` points at
  `security-report/datasets/mcp-marketplace-dataset`, which does not exist in this repo. It
  also *appends audit output directly into the Markdown files* it processes. Use
  `batch_audit.py` instead unless you are deliberately repairing this script.
- **Duplicate evaluation files.** `evaluations/marketplaces/` contains pairs that differ only
  by parentheses in the slug — e.g. `awesome-mcp-servers-(appcypher).md` alongside
  `awesome-mcp-servers-appcypher.md` (12 such `(paren)` files). Check for an existing variant
  before creating a file, and prefer the paren-free slug that `slugify()` produces.
- **Filename casing is inconsistent across the two evaluation dirs.** `marketplaces/` uses
  lowercase slugs; `clients/` uses the client's own casing (`AgenticFlow.md`, `Amazon-Q-CLI.md`).
  Match the directory you're writing into.
- **`Evaluation Status` in `working-data/mcp-marketplaces.csv` is free text, not an enum.**
  Values range from `Comprehensive` to full paragraphs of findings. Don't write code that
  treats it as a categorical field.
- `security-report/evaluations/clients/claude-desktop/` is a directory (the one detailed client
  evaluation); every other client entry is a flat `.md` file.
