# MCP Marketplace Data Model — Design

**Date:** 2026-08-31
**Status:** Proposed
**Author:** Drafted with Claude Code, for review by Kurt Seifried (CSA)

---

## 1. Problem

### 1.1 The same marketplace exists in five places, and they disagree

| # | Representation | Schema | Authoritative for |
|---|---|---|---|
| 1 | `security-report/working-data/mcp-marketplaces.csv` | Title Case, 7 cols | discovery status |
| 2 | `data/marketplaces.csv` | snake_case, 10 cols | public dataset |
| 3 | `security-report/evaluations/marketplaces/*.md` frontmatter | YAML, ~12 keys | evaluation findings |
| 4 | `security-report/working-data/list-of-sources-marketplaces.md` | prose bullets | source provenance, **language** |
| 5 | `security-report/working-data/audit-results/<date>/*.json` | tool output | technical checks |

Nothing reconciles them. Concrete drift observed at time of writing:

- Smithery is `code-hosting` in `data/marketplaces.csv` and `registry-api` in its own evaluation frontmatter.
- `[lang: zh]` / `[lang: ko]` / `[lang: en]` tags exist **only** in the prose sources file and are absent from every structured representation.
- `Is List Of Marketplaces` is `yes` on 1 of 41 rows, though the sources file identifies several meta-lists.
- Two rows in `data/marketplaces.csv` use `type` values (`marketplace`, `research-dataset`) outside the documented 8-type vocabulary. CI does not catch this because `scripts/validate_csv.py` checks field *counts* only.

### 1.2 20% of the catalogued marketplaces are wrong

Live probe of all 41 entries in `working-data/mcp-marketplaces.csv`, 2026-08-31:

| Verdict | n | Evidence |
|---|---|---|
| Domain gone | 2 | `mcpdirectory.ai` (NS delegated, zero A records); `mcpserverdirectory.org` (no NS — expired) |
| Suspended | 1 | `mcphub.io` → HTTP **402 Payment Required** behind Cloudflare |
| Unreachable | 1 | `mcpbench.ai` — A record present (GCP), connection times out |
| Moved / rebranded | 3 | `mcp.run` → `turbomcp.ai`; `toolhive.dev` → `stacklok.com/download`; Smithery `/playground` → 404 |
| Archived upstream | 1 | `appcypher/awesome-mcp-servers` — archived, ★5,763, still listed as live |
| **Bot-blocked but alive** | 3 | PulseMCP 403; `mcpmarket.com` 429; `cursor.directory` 429 |

Of 25 GitHub-backed entries, 10 had no push in 90+ days; 2 exceeded a year.

### 1.3 Nobody else has built this

Surveyed 2026-08-31:

| Source | Lists | Machine-readable |
|---|---|---|
| `modelcontextprotocol/registry` → `docs/community-projects.md` | registry browsers/aggregators | No — curated Markdown |
| modelcontextprotocol.io → Registry Aggregators | *defines* aggregator/subregistry; names none | No |
| `awesome-mcp-registry`, `toolsdk-mcp-registry` | **servers** | Yes, wrong entity |
| Canopii Trust Index, polygraph.so, Glama scorecards | **servers**, security-graded | Yes, wrong entity |
| Descope / TrueFoundry / Apigene / dev.to listicles | registries | No — blog prose |

**Everyone machine-readable indexes servers. Everyone indexing registries writes prose.** A structured, evidence-backed dataset of *marketplaces* and their security posture is unoccupied ground. `list-of-sources-marketplaces.md` is already the most complete such list found anywhere — and it is trapped in a Markdown bullet list.

---

## 2. Goals and non-goals

**Goals**

1. One editable record per marketplace. Every other representation becomes a generated artifact.
2. Publish a canonical, versioned, machine-readable meta-registry with a public JSON Schema.
3. Score security posture across multiple independent dimensions, aligned to OpenSSF where alignment exists.
4. Record liveness as dated, reproducible *observations*, with any verdict *derived* from them by a versioned rule.
5. Never emit a fabricated value. Unknown is a first-class state, distinct from absent and from negative.
6. Keep the CSV contribution on-ramp for drive-by contributors.

**Non-goals**

- Evaluating individual MCP *servers*. That space is occupied (Canopii, polygraph, Glama) and is a different repo's job.
- Replacing the narrative evaluations. Prose stays in `evaluations/`; it stops duplicating structured fields.
- Automating D1–D3 scoring. Those require human judgement (§7.3).
- Real-time monitoring. Liveness refresh is scheduled, not continuous.

---

## 3. Prior art adopted

### 3.1 ecosyste.ms — the registry-of-registries schema

Indexes 100 package registries via public JSON API. Per-registry object:

```
name  url  ecosystem  default(bool)  purl_type  packages_count  versions_count
maintainers_count  namespaces_count  downloads  github  icon_url
metadata{rate_limit,…}  created_at  updated_at  packages_url  maintainers_url
```

Adopted:
- **`default: bool`** — is this the canonical registry for its ecosystem, or a mirror/alternative (`rubygems.org` vs `gem.coop`). Maps to official MCP Registry vs downstream aggregator.
- **A join key into a shared identifier taxonomy** (their `purl_type`).
- **An open `metadata{}` extension dict**, so new fields need no schema bump. Mirrors MCP's own `_meta` convention.
- **Scale counts as first-class fields**, not notes.

### 3.2 Package URL (purl)

42 registered types; each declares a canonical repository, and the `repository_url` qualifier expresses "same package, different host" — the custody question already formalised. **There is no `pkg:mcp` type.** Registering one is a possible upstream contribution (§10).

### 3.3 OpenSSF Principles for Package Repository Security

L0–L3 across four dimensions: Authentication, Authorization, General Capabilities, CLI Tooling. Representative requirements — L1: email verification, documented account recovery, TOTP MFA, vulnerability disclosure policy, typosquatting protection. L2: abandoned-domain detection, WebAuthn, MFA for critical packages, leaked-credential scanning, unpublish policy, malware scanning. L3: passwordless/OIDC trusted publishing, universal MFA, security audits, transparency logs, standardised advisory format.

The document is v0.1 and **explicitly not machine-readable**. Adopting its levels and dimension names gives citation alignment; publishing scored data against them fills a gap OpenSSF left open.

### 3.4 The `_meta` distribution channel

`server.schema.json` permits subregistries to inject namespaced metadata:

```json
"_meta": { "com.example.subregistry/custom": { "security_scan": { "…": "…" } } }
```

A stable CSA namespace (`org.cloudsecurityalliance.mcp-marketplace-security/…`) lets marketplace operators carry these findings in their own registry payloads. This channel exists only if the data is JSON with a stable schema.

---

## 4. Core architectural principle

> **Facts are recorded unconditionally. Dimensions are scored only where applicable, and applicability is derived from the facts.**

An awesome-list has no publisher accounts, so D1 (Authentication) is **N/A, not L0**. A link-only directory does not sign artifacts it never hosts, so custody controls are N/A rather than failing. Collapsing "not applicable" into "scores zero" would punish simple marketplaces for threats they do not have, and would make the dataset unusable for comparison.

Every dimension therefore carries `applicable: true | false` with a reason, and a score only when applicable.

---

## 5. The ten dimensions

| # | Dimension | Origin | Applicable when | L3 looks like |
|---|---|---|---|---|
| D1 | Authentication | OpenSSF | has publisher accounts | passwordless/OIDC, universal MFA |
| D2 | Authorization | OpenSSF | accepts submissions | trusted publishing, scoped tokens |
| D3 | General capabilities | OpenSSF | always | transparency logs, audits, standard advisories |
| D4 | Client / CLI tooling | OpenSSF (adapted) | ships install tooling | signed installs, verified updates, rollback |
| D5 | Custody & execution | MCP | always | `builds` + signing + attestations + SBOM |
| D6 | Liveness & maintenance | MCP | always | active catalog, monitored, incidents published |
| D7 | Transparency | MCP | always | provenance, publisher identity, version, freshness all surfaced |
| D8 | Discovery interface | MCP | always | documented API, bulk export, licensed, published rate limits |
| D9 | Intake & curation | MCP | always | documented gate, enforced review, stated coverage claim |
| D10 | Openness & auditability | MCP | always | code open, catalog data open and licensed |

Scores are a **profile, not an average.** Smithery scores high on D2/D4 and lower on D3; collapsing that to one letter destroys the actionable part. Consumers may compute their own aggregate; the dataset does not ship one.

### 5.1 Dimensions the project already had, relocated

`is_aggregator`, `implements_mcp_registry_openapi`, `has_mcp_server` and `artifact_custody` stop being loose booleans and become factual evidence *under* D5/D8/D9.

The existing Tier 0–3 model measures **evaluation depth** (how hard we looked), which is orthogonal to marketplace maturity (how good they are). Both are retained, in separate fields: `evaluation.tier_reached` and `dimensions.D*.level`.

---

## 6. Record schema

One JSON file per marketplace at `data/marketplaces/<id>.json`.

> **The record below is a schema illustration, not a committed record.** Values shown as
> `null` with `needs_review` are fields that could not be established from an observed source
> at drafting time — demonstrating §6.1 rather than guessing. Migration (§11) applies the same
> discipline.

```jsonc
{
  "$schema": "https://modelcontextprotocol-security.io/schemas/marketplace/v1.json",
  "id": "smithery",
  "name": "Smithery",
  "aliases": ["Smithery.ai"],
  "url": "https://smithery.ai",
  "source_code_url": "https://github.com/smithery-ai",
  "languages": ["en"],
  "operator": {
    "name": "Clavia, Inc.",
    "legal_entity": "Clavia, Inc.",
    "country": "US",
    "contact_email": "contact@smithery.ai"
  },

  "taxonomy": {
    "type": "code-hosting",              // the 8-value vocabulary in data/marketplace-types/
    "is_default_registry": false,        // ecosyste.ms `default` — is this THE canonical registry
    "is_aggregator": true,
    "is_meta_list": false
  },

  // ---- FACTS (recorded unconditionally) ----

  "custody": {
    "artifact_custody": "builds",        // link_only | proxy | hosts | builds
    "install_mechanisms": ["one_click", "hosted_endpoint", "manual_config"],
    "provenance": {
      "signing": false, "attestations": false, "sbom": false, "immutable_versions": false
    }
  },

  "execution": {
    "model": "hosted_offered",           // index_only | self_hosted_only | hosted_offered | hosted_only
    "runs_user_traffic": true,           // operator is positioned to observe every tool call
    "hosted_endpoint_pattern": "server.smithery.ai/{name}/mcp"
  },

  "intake": {
    "mechanisms": ["self_submission_account"],   // evaluation describes publisher
                                                 // self-submission via GitHub deploy
    // self_submission_pr | self_submission_form | self_submission_account
    // | crawled | ingested_upstream | curated_manual | vendor_only
    "gate": "automated_checks",          // none | automated_checks | human_review | contractual
    "gate_evidence_url": null,
    "accepts_unsolicited": true,
    "ingests_from": ["registry.modelcontextprotocol.io"],
    "crawls": null,                      // not established — needs_review
    "curation_claim": "verified_badge"   // what they claim, so claim-vs-gate mismatch is visible
  },

  "distribution": {
    "has_api": true,
    "api_spec_url": "https://smithery.ai/docs/use/registry",
    "implements_mcp_registry_openapi": false,   // = is it a subregistry?
    "has_mcp_server": null,                     // queryable BY an agent — see §6.2.
                                                // A "Smithery Registry MCP Server" exists but
                                                // first-party ownership is unconfirmed.
    "mcp_server_url": null,
    "has_cli": true,
    "bulk_export_url": null,
    "data_license": null,
    "rate_limit": null
  },

  "openness": {
    "marketplace_open_source": false,
    "license": null,
    "catalog_data_open": false,          // distinct from code being open
    "catalog_data_license": null
  },

  "feedback": {
    "abuse_report_url": null,
    "security_contact": "contact@smithery.ai",
    "security_txt": false,
    "vuln_disclosure_policy_url": null,
    "takedown_policy_url": null,
    "observed_response": null            // { reported, acknowledged, resolved }
  },

  "scale": {
    "server_count": 3202,
    "server_count_asof": "2025-12-10",
    "maintainers_count": null
  },

  "liveness": { /* §7 */ },

  // ---- SCORES (only where applicable) ----

  "dimensions": {
    "D1": { "applicable": true,  "level": null, "needs_review": true,
            "rationale": null, "evidence": [] },
    "D5": { "applicable": true,  "level": 1,
            "rationale": "Builds and hosts servers; no signing, attestations or SBOM observed.",
            "evidence": ["https://smithery.ai/docs/use/registry"] }
    // … D2, D3, D4, D6, D7, D8, D9, D10
  },

  "evaluation": {
    "tier_reached": 3,                   // evaluation DEPTH — orthogonal to dimension levels
    "last_evaluated": "2025-12-10",
    "evaluation_path": "security-report/evaluations/marketplaces/smithery.md",
    "operator_verified": false
  },

  "provenance": {
    "last_verified": "2026-08-31",
    "sources": ["https://smithery.ai/privacy"],
    "notes": null
  },

  "metadata": {}                          // open extension dict (ecosyste.ms pattern)
}
```

### 6.1 Unknown is not false

Every optional field distinguishes three states: `null` (not yet determined), `false`/`"none"` (determined absent), and a value. A `needs_review: true` flag marks fields awaiting human judgement. **The generator must never write a non-null value it did not observe.**

### 6.2 `has_mcp_server` raises scrutiny; it is not a gold star

A marketplace reachable through an MCP server converts discovery into an agent-mediated flow — type `05-ai-agent-recommendations` in this project's own taxonomy, rated **Highest** risk. The schema documentation must state this explicitly so the flag is not misread as a maturity signal.

Servers of this kind are confirmed to exist (a Smithery Registry MCP server, a Registry MCP server for the official registry, `mcp-registry-cli`), but **ownership varies and must be recorded**, because the trust situations differ:

```jsonc
"mcp_access": {
  "first_party": null,      // operator ships it: one hop, operator-controlled
  "third_party": null,      // someone else wraps their API: an ADDITIONAL untrusted hop
  "urls": []
}
```

A third-party wrapper is not evidence of marketplace maturity — it is an extra intermediary between the agent and the catalogue, controlled by neither the user nor the marketplace operator. Collapsing both into one boolean would hide that.

### 6.3 Claim-vs-gate mismatch

`intake.curation_claim` alongside `intake.gate` makes visible the dangerous combination: a marketplace that **crawls the world while implying curation**. Crawling and self-submission are a trust *trade*, not a ranking — broad coverage with no gate is honest; broad coverage advertised as vetted is not.

---

## 7. Liveness

### 7.1 Facts, then a derived verdict

```jsonc
"liveness": {
  "observations": {
    "service_status": 403,
    "service_checked_at": "2026-08-31",
    "service_block_reason": "cloudflare_bot_management",   // alive, blocking us
    "service_final_url": "https://www.pulsemcp.com",
    "source_last_commit": "2025-07-09",                    // the container
    "source_archived": false,
    "catalog_last_entry_added": "2026-08-21",              // ← the vital sign
    "catalog_entries_added_30d": 2,
    "catalog_entries_added_90d": 377,
    "catalog_size": 3774,
    "catalog_size_checked_at": "2026-08-31",
    "measurement_method": "git_log_path:servers/"
    // api_updated_since | git_log_path:<path> | rss | scrape | manual | unmeasurable
  },
  "derived": {
    "activity": "active",        // active | slowing | dormant | abandoned | unknown
    "reachability": "blocked",   // ok | blocked | suspended | moved | unreachable | dead
    "rule_version": "1.0",
    "computed_at": "2026-08-31"
  }
}
```

`derived` is computed from `observations` by a versioned rule, never authored by hand. Recording `rule_version` allows history to be re-derived when the rule changes.

### 7.2 Derivation rules v1.0

**`activity`** — from `catalog_last_entry_added`: `active` <30d · `slowing` 30–90d · `dormant` 90–365d · `abandoned` >365d · `unknown` when `measurement_method` is `unmeasurable`.

**`reachability`** — `dead` when DNS resolves no address or has no NS · `suspended` on HTTP 402 · `moved` when the final URL host differs from the recorded host · `blocked` on 403/429 with a bot-management signature · `unreachable` on timeout with DNS resolving · `ok` on 2xx.

### 7.3 Why the verdict cannot be a boolean

A naive checker would have declared **PulseMCP dead** — it returns 403 even with full browser headers, yet it is among the healthiest directories in the ecosystem. Bot-blocking is a marketplace *property*, not a probe error. Three separate false-positive classes were observed:

| Case | Naive signal | Reality |
|---|---|---|
| PulseMCP | HTTP 403 → "dead" | Alive; Cloudflare bot management |
| MCP.so | repo cold 522d → "dead" | Site live and widely used |
| `docker/mcp-registry` | README cold 13mo → "dead" | 3,774 catalog commits; most recent 10 days ago |

**Every liveness signal must point at the catalog, not the container.** Repo activity, README dates and HTTP status all fail, in opposite directions. The only signal that survived every case is *when a listing last changed*.

### 7.4 Measurement methods, in preference order

1. **`api_updated_since`** — API-backed registries. The official registry's `?updated_since=` returned 100+ servers for a 14-day window.
2. **`git_log_path:<path>`** — git-backed catalogs. Requires locating the *entry path*, not the README: `docker/mcp-registry` → `servers/`; `cline/mcp-marketplace` has no catalog directory, so its README **is** the catalog (last changed 2025-06-24).
3. **`rss`** — where a changelog or feed exists.
4. **`scrape`** — dated listings in HTML. Fragile; record the selector used.
5. **`unmeasurable`** — record honestly; `activity` becomes `unknown`, never `abandoned`.

---

## 8. File layout

```
data/
  schema/
    marketplace.v1.json          # published JSON Schema
    dimensions.v1.json           # D1–D10 definitions, levels, OpenSSF mapping
  marketplaces/
    <id>.json                    # SOURCE OF TRUTH — one file per marketplace
  marketplaces.json              # GENERATED aggregate
  marketplaces.csv               # GENERATED — back-compat, human-scannable
scripts/
  build_dataset.py               # records → aggregate JSON + CSV
  check_liveness.py              # refreshes liveness.observations
  validate_dataset.py            # schema + referential integrity + vocabularies
```

`data/marketplaces/<id>.json` is the only hand-edited artifact. **Generated files carry a header comment naming their generator**; CI fails if a generated file is edited directly or is out of date relative to its sources.

### 8.1 Why file-per-entity

Considered and rejected:

| Option | Merge conflicts | Verdict |
|---|---|---|
| Single `marketplaces.json` array | Every PR touches one file | Rejected — conflicts on every concurrent contribution |
| Evaluation `.md` frontmatter as truth | Low | Rejected — consumers would parse YAML-in-Markdown; mixes editorial with structured data |
| **File per entity** | None | **Chosen** — one file per PR, clean diffs, mirrors the existing `evaluations/` layout |

CSV does not die; it stops being authoritative. A drive-by contributor still gets a one-line change via an `add-marketplace` helper that scaffolds the JSON record.

---

## 9. Validation and CI

`scripts/validate_dataset.py` replaces the field-count-only check and adds:

1. **JSON Schema** validation of every record.
2. **Vocabulary enforcement** — `taxonomy.type` against `data/marketplace-types/` (this alone catches the two existing off-vocabulary rows), plus every other enum.
3. **Referential integrity** — `evaluation.evaluation_path` resolves; every evaluation file has a record; no duplicate `id` or `url`.
4. **Evidence discipline** — any `dimensions.D*.level` that is non-null has non-empty `evidence`.
5. **Freshness** — `provenance.last_verified` older than N days emits a warning, not a failure.
6. **Generated-file currency** — regenerate and diff; fail if stale.

Two scheduled workflows: liveness refresh (weekly, opens a PR with observation changes) and staleness report (monthly).

The existing `scripts/validate_csv.py` is retained for the generated CSV.

---

## 10. Publication

- `data/marketplaces.json` + `data/schema/marketplace.v1.json` served at stable URLs.
- Schema versioned in the path; `v1` never breaks. Additive changes only within a major version.
- Explicit data licence (proposal: **CC-BY-4.0** for data, matching the repo's Apache-2.0 for code — ecosyste.ms uses CC-BY-SA for comparable data).
- Publish the CSA `_meta` namespace (§3.4) so operators can embed findings in their own payloads.
- Possible upstream contributions, out of scope for implementation but enabled by this design: a `pkg:mcp` purl type; a machine-readable encoding of the OpenSSF principles; supplying `modelcontextprotocol/registry` with a structured aggregator list to replace hand-curated `community-projects.md`.

---

## 11. Migration

All 41 marketplaces are converted. Fields are populated only where they can be *derived from an observed source*:

| Fields | Source | Method |
|---|---|---|
| identity, taxonomy, scale | existing CSVs + evaluation frontmatter | mechanical merge |
| `languages` | `list-of-sources-marketplaces.md` `[lang: xx]` tags | parse — **currently lost in every structured copy** |
| `liveness.observations` | live probe + GitHub API | `check_liveness.py` |
| `feedback.security_txt`, headers, paths | `working-data/audit-results/` | mechanical |
| `distribution.has_api`, `openness.*` | evaluation prose + repo metadata | extract, flag low-confidence |
| **D1, D2, D3 levels** | — | **`null` + `needs_review: true`** |
| D5–D10 levels | facts above | derived where the rule is unambiguous; else `null` |

**Conflicts are surfaced, not resolved.** Where representations disagree (Smithery `code-hosting` vs `registry-api`), migration emits a `conflicts.md` worklist naming the field, the competing values and their sources, for adjudication. The migration never silently picks a winner.

Deliverables: 41 records, the generator, the validator, the liveness collector, the conflict worklist, and a `MIGRATION.md` recording what was derived versus carried over.

---

## 12. Risks

| Risk | Mitigation |
|---|---|
| Defaming a live marketplace as dead | Tri-state reachability; bot-blocking recorded as a property; `unmeasurable` never becomes `abandoned` |
| Scores read as authoritative grades | Profile not average; `needs_review` visible in generated artifacts; documented methodology |
| Liveness probing looks like abuse | Weekly cadence, identifying User-Agent, honour `robots.txt`, low concurrency |
| Schema churn breaking consumers | Versioned path; additive-only within v1; open `metadata{}` for experiments |
| Migration importing existing errors | Conflict worklist; `provenance.sources` per record |
| Ten dimensions too heavy for contributors | Only identity + taxonomy required to add a marketplace; everything else nullable |

---

## 13. Open questions

1. **Data licence** — CC-BY-4.0 proposed. Needs a CSA decision.
2. **Publication URL** — `modelcontextprotocol-security.io/schemas/…` assumed; needs confirmation the site can serve static JSON.
3. **`working-data/` after migration** — does the working tier remain for discovery, or collapse into `data/` with a `status: draft` field? Recommend collapsing; two tiers with different schemas caused the original problem.
4. **Client dataset** — this design covers marketplaces. `mcp-clients.csv` (132 working / 25 stable rows) has the same disease and wants a parallel `client.v1.json`. Recommend a follow-on spec rather than expanding this one.
5. **Scoring D1–D3 at scale** — 41 marketplaces × 3 human-judgement dimensions is a real workload. Worth considering whether the two-AI evaluation model produces a draft score with a confidence level for human confirmation.
