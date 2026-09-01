# MCP Marketplace Data Model Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace five drifting representations of each MCP marketplace with one validated JSON record per entity, plus the generator, validator and liveness collector that keep the derived artifacts honest.

**Architecture:** `data/marketplaces/<id>.json` is the only hand-edited store. A small `scripts/mcpmeta/` package provides schema validation, vocabulary enforcement, liveness derivation and artifact generation; four thin CLIs wrap it. `data/marketplaces.json` and `data/marketplaces.csv` become generated artifacts that CI regenerates and diffs, so drift fails the build.

**Tech Stack:** Python 3.12 (stdlib + `jsonschema`, `PyYAML`, `requests`), pytest, GitHub Actions. `curl`/`dig` shell-outs are retained only where the existing audit toolkit already uses them.

**Spec:** `docs/superpowers/specs/2026-08-31-mcp-marketplace-data-model-design.md`

## Global Constraints

- **Never emit a value that was not observed.** Unknown is `null`; determined-absent is `false`/`"none"`. A generator that cannot establish a field writes `null`, never a default. (Spec §6.1)
- **A non-null `dimensions.D*.level` requires non-empty `evidence`.** Validator-enforced. (Spec §6.4)
- **`applicable: false` is not `level: 0`.** Applicability is derived from facts before any scoring. (Spec §4)
- **Canonical schema URL:** `https://raw.githubusercontent.com/ModelContextProtocol-Security/mcpserver-marketplace/main/data/schema/marketplace.v1.json` — defined ONCE as `mcpmeta.schema.SCHEMA_URL` and normalised into every record on every build. Never hand-written into a record. (Spec §10.2)
- **Canonical type vocabulary** (from `data/marketplaces/README.md`, NOT the `marketplace-types/` filenames, which are plural and are ordering only): `registry`, `built-in-app`, `catalog-site`, `code-hosting`, `ai-agent`, `search-engine`, `community-forum`, `tutorial`.
- **Data licence:** CC-BY-4.0 (`data/LICENSE-DATA`). Code remains Apache-2.0.
- **Liveness derivation rule version:** `"1.0"`. Any change to the thresholds bumps it.
- **Migration surfaces conflicts, never resolves them.** (Spec §11)
- Commit after every task. Conventional-commit prefixes (`feat:`, `fix:`, `test:`, `docs:`, `chore:`), matching repo history.
- Work on a feature branch and open a PR; never commit to `main`.

## File Structure

| File | Responsibility |
|---|---|
| `data/schema/marketplace.v1.json` | The published JSON Schema |
| `data/LICENSE-DATA` | CC-BY-4.0 text |
| `data/marketplaces/<id>.json` | Source of truth, one per marketplace |
| `scripts/mcpmeta/schema.py` | Schema loading, `SCHEMA_URL`, record validation |
| `scripts/mcpmeta/vocab.py` | Enum vocabularies + type-vocabulary cross-check |
| `scripts/mcpmeta/record.py` | Load/save records, `$schema` normalisation, id rules |
| `scripts/mcpmeta/liveness.py` | Observation probes + v1.0 derivation rules |
| `scripts/mcpmeta/generate.py` | Aggregate JSON + CSV emitters |
| `scripts/mcpmeta/migrate.py` | Legacy sources → records + conflict worklist |
| `scripts/validate_dataset.py` | CLI: schema + vocab + integrity |
| `scripts/build_dataset.py` | CLI: records → generated artifacts |
| `scripts/check_liveness.py` | CLI: refresh `liveness.observations` |
| `scripts/migrate_to_records.py` | CLI: one-shot migration |
| `tests/test_*.py` | One test module per package module |
| `.github/workflows/validate-dataset.yml` | CI |
| `requirements-dev.txt` | `jsonschema`, `PyYAML`, `requests`, `pytest` |

**Dependency note:** the existing `security-report/tools/` audit package stays dependency-free (its README promises that). The new `scripts/mcpmeta/` package may use the four libraries above; CI installs them from `requirements-dev.txt`.

---

### Task 1: Schema and vocabulary foundation

**Files:**
- Create: `data/schema/marketplace.v1.json`, `scripts/mcpmeta/__init__.py`, `scripts/mcpmeta/schema.py`, `scripts/mcpmeta/vocab.py`, `requirements-dev.txt`, `data/LICENSE-DATA`
- Test: `tests/test_schema.py`, `tests/test_vocab.py`

**Interfaces:**
- Produces: `mcpmeta.schema.SCHEMA_URL: str`, `mcpmeta.schema.load_schema() -> dict`, `mcpmeta.schema.validate_record(record: dict) -> list[str]` (returns error strings, empty when valid); `mcpmeta.vocab.TYPES: frozenset[str]`, `mcpmeta.vocab.ARTIFACT_CUSTODY`, `mcpmeta.vocab.EXECUTION_MODELS`, `mcpmeta.vocab.INTAKE_MECHANISMS`, `mcpmeta.vocab.INTAKE_GATES`, `mcpmeta.vocab.SCORED_BY`, `mcpmeta.vocab.ACTIVITY`, `mcpmeta.vocab.REACHABILITY`, `mcpmeta.vocab.documented_types() -> set[str]`

- [ ] **Step 1: Create the dependency file and licence**

```bash
cd /Volumes/MacMiniData/Users/kurt/GitHub/ModelContextProtocol-Security/mcpserver-marketplace
git checkout -b feat/marketplace-data-model
mkdir -p scripts/mcpmeta tests data/schema data/marketplaces
printf 'jsonschema>=4.20\nPyYAML>=6.0\nrequests>=2.31\npytest>=8.0\n' > requirements-dev.txt
curl -sL https://creativecommons.org/licenses/by/4.0/legalcode.txt -o data/LICENSE-DATA
head -3 data/LICENSE-DATA
```

If the download fails, write the file with the single line `Creative Commons Attribution 4.0 International (CC BY 4.0) — https://creativecommons.org/licenses/by/4.0/` and continue; the exact text is not load-bearing for tests.

- [ ] **Step 2: Write the failing vocabulary test**

`tests/test_vocab.py`:

```python
from mcpmeta import vocab


def test_types_is_the_documented_singular_vocabulary():
    assert vocab.TYPES == frozenset({
        "registry", "built-in-app", "catalog-site", "code-hosting",
        "ai-agent", "search-engine", "community-forum", "tutorial",
    })


def test_marketplace_type_files_cover_every_documented_type():
    """Filenames are plural and ordered; the documented enum is singular.

    They must still describe the same eight concepts, so a new type file
    without a vocabulary entry (or the reverse) fails here.
    """
    assert len(vocab.documented_types()) == len(vocab.TYPES) == 8


def test_scored_by_vocabulary_matches_spec_6_4():
    assert vocab.SCORED_BY == frozenset({
        "automated_check", "ai_evaluation", "ai_validation",
        "human_reviewed", "operator_verified",
    })
```

- [ ] **Step 3: Run it to verify it fails**

Run: `cd scripts && python3 -m pytest ../tests/test_vocab.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'mcpmeta'`

- [ ] **Step 4: Implement the vocabularies**

`scripts/mcpmeta/__init__.py`:

```python
"""Tooling for the CSA MCP marketplace meta-registry dataset."""
```

`scripts/mcpmeta/vocab.py`:

```python
"""Controlled vocabularies for marketplace records.

The canonical type vocabulary is the one documented in
data/marketplaces/README.md (singular). The filenames under
data/marketplace-types/ are plural and exist only to order the
explanatory documents; they are NOT the enum.
"""
from __future__ import annotations

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

TYPES = frozenset({
    "registry", "built-in-app", "catalog-site", "code-hosting",
    "ai-agent", "search-engine", "community-forum", "tutorial",
})

ARTIFACT_CUSTODY = frozenset({"link_only", "proxy", "hosts", "builds"})
EXECUTION_MODELS = frozenset({
    "index_only", "self_hosted_only", "hosted_offered", "hosted_only",
})
INTAKE_MECHANISMS = frozenset({
    "self_submission_pr", "self_submission_form", "self_submission_account",
    "crawled", "ingested_upstream", "curated_manual", "vendor_only",
})
INTAKE_GATES = frozenset({"none", "automated_checks", "human_review", "contractual"})
SCORED_BY = frozenset({
    "automated_check", "ai_evaluation", "ai_validation",
    "human_reviewed", "operator_verified",
})
CONFIDENCE = frozenset({"high", "medium", "low"})
ACTIVITY = frozenset({"active", "slowing", "dormant", "abandoned", "unknown"})
REACHABILITY = frozenset({
    "ok", "blocked", "suspended", "moved", "unreachable", "dead",
})
STATUS = frozenset({"draft", "published"})
DIMENSIONS = tuple(f"D{n}" for n in range(1, 11))


def documented_types() -> set[str]:
    """The eight concepts described under data/marketplace-types/."""
    return {
        p.stem.split("-", 1)[1]
        for p in (DATA_DIR / "marketplace-types").glob("[0-9]*-*.md")
    }
```

- [ ] **Step 5: Run the vocabulary tests**

Run: `cd scripts && python3 -m pytest ../tests/test_vocab.py -v`
Expected: PASS (3 passed)

- [ ] **Step 6: Write the failing schema test**

`tests/test_schema.py`:

```python
import json

from mcpmeta import schema


MINIMAL = {
    "$schema": schema.SCHEMA_URL,
    "id": "example",
    "name": "Example",
    "url": "https://example.com",
    "status": "draft",
    "taxonomy": {"type": "catalog-site"},
}


def test_schema_file_is_valid_json_schema():
    s = schema.load_schema()
    assert s["$id"] == schema.SCHEMA_URL
    assert s["type"] == "object"


def test_minimal_record_validates():
    assert schema.validate_record(MINIMAL) == []


def test_unknown_type_is_rejected():
    bad = json.loads(json.dumps(MINIMAL))
    bad["taxonomy"]["type"] = "research-dataset"
    assert schema.validate_record(bad) != []


def test_level_without_evidence_is_rejected():
    """Spec §6.4 rule 1: a non-null level requires evidence."""
    bad = json.loads(json.dumps(MINIMAL))
    bad["dimensions"] = {"D5": {"applicable": True, "level": 2, "evidence": []}}
    errors = schema.validate_record(bad)
    assert any("evidence" in e for e in errors)


def test_null_level_without_evidence_is_allowed():
    ok = json.loads(json.dumps(MINIMAL))
    ok["dimensions"] = {"D5": {"applicable": True, "level": None, "evidence": []}}
    assert schema.validate_record(ok) == []
```

- [ ] **Step 7: Run it to verify it fails**

Run: `cd scripts && python3 -m pytest ../tests/test_schema.py -v`
Expected: FAIL — no `schema` module

- [ ] **Step 8: Write the JSON Schema**

`data/schema/marketplace.v1.json` — note the `dimension` definition encodes the evidence rule declaratively via `if/then`, so it is enforced by the schema itself and not only by Python:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/ModelContextProtocol-Security/mcpserver-marketplace/main/data/schema/marketplace.v1.json",
  "title": "MCP Marketplace Record",
  "type": "object",
  "required": ["$schema", "id", "name", "url", "status", "taxonomy"],
  "additionalProperties": false,
  "properties": {
    "$schema": { "type": "string" },
    "id": { "type": "string", "pattern": "^[a-z0-9][a-z0-9.-]*$" },
    "name": { "type": "string", "minLength": 1 },
    "aliases": { "type": "array", "items": { "type": "string" } },
    "url": { "type": "string", "format": "uri" },
    "source_code_url": { "type": ["string", "null"] },
    "languages": { "type": "array", "items": { "type": "string" } },
    "status": { "enum": ["draft", "published"] },
    "operator": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "name": { "type": ["string", "null"] },
        "legal_entity": { "type": ["string", "null"] },
        "country": { "type": ["string", "null"] },
        "contact_email": { "type": ["string", "null"] }
      }
    },
    "taxonomy": {
      "type": "object",
      "required": ["type"],
      "additionalProperties": false,
      "properties": {
        "type": {
          "enum": ["registry", "built-in-app", "catalog-site", "code-hosting",
                   "ai-agent", "search-engine", "community-forum", "tutorial"]
        },
        "is_default_registry": { "type": ["boolean", "null"] },
        "is_aggregator": { "type": ["boolean", "null"] },
        "is_meta_list": { "type": ["boolean", "null"] }
      }
    },
    "custody": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "artifact_custody": { "enum": ["link_only", "proxy", "hosts", "builds", null] },
        "install_mechanisms": { "type": ["array", "null"], "items": { "type": "string" } },
        "provenance": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "signing": { "type": ["boolean", "null"] },
            "attestations": { "type": ["boolean", "null"] },
            "sbom": { "type": ["boolean", "null"] },
            "immutable_versions": { "type": ["boolean", "null"] }
          }
        }
      }
    },
    "execution": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "model": { "enum": ["index_only", "self_hosted_only", "hosted_offered", "hosted_only", null] },
        "runs_user_traffic": { "type": ["boolean", "null"] },
        "hosted_endpoint_pattern": { "type": ["string", "null"] }
      }
    },
    "intake": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "mechanisms": {
          "type": ["array", "null"],
          "items": {
            "enum": ["self_submission_pr", "self_submission_form", "self_submission_account",
                     "crawled", "ingested_upstream", "curated_manual", "vendor_only"]
          }
        },
        "gate": { "enum": ["none", "automated_checks", "human_review", "contractual", null] },
        "gate_evidence_url": { "type": ["string", "null"] },
        "accepts_unsolicited": { "type": ["boolean", "null"] },
        "ingests_from": { "type": ["array", "null"], "items": { "type": "string" } },
        "crawls": { "type": ["array", "null"], "items": { "type": "string" } },
        "curation_claim": { "type": ["string", "null"] }
      }
    },
    "distribution": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "has_api": { "type": ["boolean", "null"] },
        "api_spec_url": { "type": ["string", "null"] },
        "implements_mcp_registry_openapi": { "type": ["boolean", "null"] },
        "has_cli": { "type": ["boolean", "null"] },
        "bulk_export_url": { "type": ["string", "null"] },
        "data_license": { "type": ["string", "null"] },
        "rate_limit": { "type": ["string", "null"] },
        "mcp_access": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "first_party": { "type": ["boolean", "null"] },
            "third_party": { "type": ["boolean", "null"] },
            "urls": { "type": "array", "items": { "type": "string" } }
          }
        }
      }
    },
    "openness": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "marketplace_open_source": { "type": ["boolean", "null"] },
        "license": { "type": ["string", "null"] },
        "catalog_data_open": { "type": ["boolean", "null"] },
        "catalog_data_license": { "type": ["string", "null"] }
      }
    },
    "feedback": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "abuse_report_url": { "type": ["string", "null"] },
        "security_contact": { "type": ["string", "null"] },
        "security_txt": { "type": ["boolean", "null"] },
        "vuln_disclosure_policy_url": { "type": ["string", "null"] },
        "takedown_policy_url": { "type": ["string", "null"] },
        "observed_response": { "type": ["object", "null"] }
      }
    },
    "scale": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "server_count": { "type": ["integer", "null"] },
        "server_count_asof": { "type": ["string", "null"] },
        "maintainers_count": { "type": ["integer", "null"] }
      }
    },
    "liveness": { "$ref": "#/$defs/liveness" },
    "dimensions": {
      "type": "object",
      "additionalProperties": false,
      "patternProperties": { "^D([1-9]|10)$": { "$ref": "#/$defs/dimension" } }
    },
    "evaluation": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "tier_reached": { "type": ["integer", "null"], "minimum": 0, "maximum": 3 },
        "last_evaluated": { "type": ["string", "null"] },
        "evaluation_path": { "type": ["string", "null"] },
        "operator_verified": { "type": ["boolean", "null"] }
      }
    },
    "provenance": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "last_verified": { "type": ["string", "null"] },
        "sources": { "type": "array", "items": { "type": "string" } },
        "notes": { "type": ["string", "null"] }
      }
    },
    "metadata": { "type": "object" }
  },
  "$defs": {
    "dimension": {
      "type": "object",
      "required": ["applicable"],
      "additionalProperties": false,
      "properties": {
        "applicable": { "type": "boolean" },
        "not_applicable_reason": { "type": ["string", "null"] },
        "level": { "type": ["integer", "null"], "minimum": 0, "maximum": 3 },
        "rationale": { "type": ["string", "null"] },
        "evidence": { "type": "array", "items": { "type": "string" } },
        "provenance": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "scored_by": {
              "enum": ["automated_check", "ai_evaluation", "ai_validation",
                       "human_reviewed", "operator_verified", null]
            },
            "confidence": { "enum": ["high", "medium", "low", null] },
            "scored_at": { "type": ["string", "null"] },
            "validated_by": { "enum": ["ai_validation", "human_reviewed", "operator_verified", null] },
            "validated_at": { "type": ["string", "null"] },
            "model_run": { "type": ["string", "null"] }
          }
        }
      },
      "if": { "properties": { "level": { "type": "integer" } }, "required": ["level"] },
      "then": { "properties": { "evidence": { "minItems": 1 } }, "required": ["evidence"] }
    },
    "liveness": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "observations": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "service_status": { "type": ["integer", "null"] },
            "service_checked_at": { "type": ["string", "null"] },
            "service_block_reason": { "type": ["string", "null"] },
            "service_final_url": { "type": ["string", "null"] },
            "dns_resolves": { "type": ["boolean", "null"] },
            "dns_has_ns": { "type": ["boolean", "null"] },
            "source_last_commit": { "type": ["string", "null"] },
            "source_archived": { "type": ["boolean", "null"] },
            "catalog_last_entry_added": { "type": ["string", "null"] },
            "catalog_entries_added_30d": { "type": ["integer", "null"] },
            "catalog_entries_added_90d": { "type": ["integer", "null"] },
            "catalog_size": { "type": ["integer", "null"] },
            "catalog_size_checked_at": { "type": ["string", "null"] },
            "measurement_method": { "type": ["string", "null"] }
          }
        },
        "derived": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "activity": { "enum": ["active", "slowing", "dormant", "abandoned", "unknown", null] },
            "reachability": { "enum": ["ok", "blocked", "suspended", "moved", "unreachable", "dead", null] },
            "rule_version": { "type": ["string", "null"] },
            "computed_at": { "type": ["string", "null"] }
          }
        }
      }
    }
  }
}
```

- [ ] **Step 9: Implement the schema loader**

`scripts/mcpmeta/schema.py`:

```python
"""Loading and validation against the published marketplace JSON Schema."""
from __future__ import annotations

import functools
import json
from pathlib import Path

import jsonschema

SCHEMA_URL = (
    "https://raw.githubusercontent.com/ModelContextProtocol-Security/"
    "mcpserver-marketplace/main/data/schema/marketplace.v1.json"
)

SCHEMA_PATH = Path(__file__).resolve().parents[2] / "data" / "schema" / "marketplace.v1.json"


@functools.lru_cache(maxsize=1)
def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def validate_record(record: dict) -> list[str]:
    """Return a list of human-readable errors; empty means valid."""
    validator = jsonschema.Draft202012Validator(load_schema())
    return [
        f"{'/'.join(str(p) for p in e.absolute_path) or '<root>'}: {e.message}"
        for e in sorted(validator.iter_errors(record), key=lambda e: list(e.absolute_path))
    ]
```

- [ ] **Step 10: Run the schema tests**

Run: `cd scripts && python3 -m pytest ../tests/ -v`
Expected: PASS (8 passed)

- [ ] **Step 11: Commit**

```bash
git add data/schema data/LICENSE-DATA scripts/mcpmeta tests requirements-dev.txt
git commit -m "feat(data): marketplace JSON Schema v1 and controlled vocabularies"
```

---

### Task 2: Record load/save with `$schema` normalisation

**Files:**
- Create: `scripts/mcpmeta/record.py`
- Test: `tests/test_record.py`

**Interfaces:**
- Consumes: `mcpmeta.schema.SCHEMA_URL`, `mcpmeta.schema.validate_record`
- Produces: `mcpmeta.record.RECORDS_DIR: Path`, `load_all() -> list[dict]`, `load(path: Path) -> dict`, `save(record: dict, path: Path | None = None) -> Path`, `slugify(name: str) -> str`

- [ ] **Step 1: Write the failing test**

`tests/test_record.py`:

```python
import json

from mcpmeta import record, schema


def test_slugify_matches_existing_batch_audit_rules():
    """Must match security-report/tools/batch_audit.py slugify so audit
    JSON filenames line up with record ids."""
    assert record.slugify("Awesome MCP Servers (appcypher)") == "awesome-mcp-servers-appcypher"
    assert record.slugify("MCP.so") == "mcpso"
    assert record.slugify("  Spaced   Out  ") == "spaced-out"


def test_save_normalises_schema_url_even_when_wrong(tmp_path):
    rec = {
        "$schema": "https://example.invalid/old.json",
        "id": "x", "name": "X", "url": "https://x.test",
        "status": "draft", "taxonomy": {"type": "registry"},
    }
    p = record.save(rec, tmp_path / "x.json")
    assert json.loads(p.read_text())["$schema"] == schema.SCHEMA_URL


def test_save_adds_schema_url_when_absent(tmp_path):
    rec = {"id": "y", "name": "Y", "url": "https://y.test",
           "status": "draft", "taxonomy": {"type": "registry"}}
    p = record.save(rec, tmp_path / "y.json")
    assert json.loads(p.read_text())["$schema"] == schema.SCHEMA_URL


def test_save_refuses_invalid_record(tmp_path):
    bad = {"id": "z", "name": "Z", "url": "https://z.test",
           "status": "draft", "taxonomy": {"type": "not-a-type"}}
    try:
        record.save(bad, tmp_path / "z.json")
    except ValueError as e:
        assert "not-a-type" in str(e)
    else:
        raise AssertionError("expected ValueError")


def test_save_is_deterministic(tmp_path):
    rec = {"id": "d", "name": "D", "url": "https://d.test",
           "status": "draft", "taxonomy": {"type": "registry"}}
    a = record.save(dict(rec), tmp_path / "d.json").read_text()
    b = record.save(dict(rec), tmp_path / "d.json").read_text()
    assert a == b and a.endswith("\n")
```

- [ ] **Step 2: Run it to verify it fails**

Run: `cd scripts && python3 -m pytest ../tests/test_record.py -v`
Expected: FAIL — no `record` module

- [ ] **Step 3: Implement**

`scripts/mcpmeta/record.py`:

```python
"""Loading, saving and identifying marketplace records."""
from __future__ import annotations

import json
import re
from pathlib import Path

from . import schema

RECORDS_DIR = Path(__file__).resolve().parents[2] / "data" / "marketplaces"


def slugify(name: str) -> str:
    """Filename-safe slug.

    Deliberately identical to security-report/tools/batch_audit.py so a
    record id matches its audit-results JSON filename.
    """
    slug = re.sub(r"[^\w\s-]", "", name.lower())
    slug = re.sub(r"[-\s]+", "-", slug).strip("-")
    return slug[:50]


def load(path: Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_all(records_dir: Path | None = None) -> list[dict]:
    d = Path(records_dir or RECORDS_DIR)
    return [load(p) for p in sorted(d.glob("*.json"))]


def save(rec: dict, path: Path | None = None) -> Path:
    """Normalise $schema, validate, then write deterministically."""
    rec["$schema"] = schema.SCHEMA_URL
    errors = schema.validate_record(rec)
    if errors:
        raise ValueError(f"invalid record {rec.get('id', '<no id>')}: {'; '.join(errors)}")
    target = Path(path) if path else RECORDS_DIR / f"{rec['id']}.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(rec, indent=2, ensure_ascii=False, sort_keys=False) + "\n",
                      encoding="utf-8")
    return target
```

- [ ] **Step 4: Run the tests**

Run: `cd scripts && python3 -m pytest ../tests/ -v`
Expected: PASS (13 passed)

- [ ] **Step 5: Commit**

```bash
git add scripts/mcpmeta/record.py tests/test_record.py
git commit -m "feat(data): record load/save with \$schema normalisation"
```

---

### Task 3: Liveness derivation rules v1.0

Pure functions over observations, no network. The probes come in Task 4.

**Files:**
- Create: `scripts/mcpmeta/liveness.py`
- Test: `tests/test_liveness.py`

**Interfaces:**
- Consumes: nothing
- Produces: `mcpmeta.liveness.RULE_VERSION: str`, `derive_activity(obs: dict, today: date) -> str`, `derive_reachability(obs: dict, recorded_host: str) -> str`, `derive(obs: dict, recorded_host: str, today: date) -> dict`

- [ ] **Step 1: Write the failing test — every case is a real observation from the 2026-08-31 sweep**

`tests/test_liveness.py`:

```python
from datetime import date

from mcpmeta import liveness

TODAY = date(2026, 8, 31)


def test_active_when_catalog_changed_within_30_days():
    obs = {"catalog_last_entry_added": "2026-08-21",
           "measurement_method": "git_log_path:servers/"}
    assert liveness.derive_activity(obs, TODAY) == "active"


def test_abandoned_when_catalog_cold_over_a_year():
    """cline/mcp-marketplace: README IS the catalog, last changed 2025-06-24."""
    obs = {"catalog_last_entry_added": "2025-06-24",
           "measurement_method": "git_log_path:README.md"}
    assert liveness.derive_activity(obs, TODAY) == "abandoned"


def test_unmeasurable_is_unknown_never_abandoned():
    """The single most damaging failure would be calling an unmeasured
    marketplace dead."""
    obs = {"catalog_last_entry_added": None, "measurement_method": "unmeasurable"}
    assert liveness.derive_activity(obs, TODAY) == "unknown"


def test_dead_when_dns_has_no_ns():
    """mcpserverdirectory.org — no NS records at all."""
    obs = {"dns_resolves": False, "dns_has_ns": False, "service_status": None}
    assert liveness.derive_reachability(obs, "mcpserverdirectory.org") == "dead"


def test_dead_when_ns_delegated_but_no_address():
    """mcpdirectory.ai — NS present, zero A records."""
    obs = {"dns_resolves": False, "dns_has_ns": True, "service_status": None}
    assert liveness.derive_reachability(obs, "mcpdirectory.ai") == "dead"


def test_suspended_on_402():
    """mcphub.io — Payment Required behind Cloudflare."""
    obs = {"dns_resolves": True, "dns_has_ns": True, "service_status": 402}
    assert liveness.derive_reachability(obs, "mcphub.io") == "suspended"


def test_blocked_not_dead_on_403():
    """PulseMCP is one of the healthiest directories and still 403s us.
    Calling it dead would be a false accusation about a live business."""
    obs = {"dns_resolves": True, "dns_has_ns": True, "service_status": 403}
    assert liveness.derive_reachability(obs, "www.pulsemcp.com") == "blocked"


def test_blocked_on_429():
    obs = {"dns_resolves": True, "dns_has_ns": True, "service_status": 429}
    assert liveness.derive_reachability(obs, "mcpmarket.com") == "blocked"


def test_moved_when_final_host_differs():
    """mcp.run now redirects to turbomcp.ai."""
    obs = {"dns_resolves": True, "dns_has_ns": True, "service_status": 200,
           "service_final_url": "https://turbomcp.ai/"}
    assert liveness.derive_reachability(obs, "mcp.run") == "moved"


def test_ok_when_redirect_is_only_www():
    """mcpdirectory.io -> www.mcpdirectory.io is not a move."""
    obs = {"dns_resolves": True, "dns_has_ns": True, "service_status": 200,
           "service_final_url": "https://www.mcpdirectory.io/"}
    assert liveness.derive_reachability(obs, "mcpdirectory.io") == "ok"


def test_unreachable_on_timeout_with_dns():
    """mcpbench.ai resolves to GCP but times out."""
    obs = {"dns_resolves": True, "dns_has_ns": True, "service_status": None}
    assert liveness.derive_reachability(obs, "mcpbench.ai") == "unreachable"


def test_derive_stamps_rule_version():
    out = liveness.derive({"measurement_method": "unmeasurable",
                           "dns_resolves": True, "dns_has_ns": True,
                           "service_status": 200}, "x.test", TODAY)
    assert out["rule_version"] == liveness.RULE_VERSION
    assert out["computed_at"] == "2026-08-31"
```

- [ ] **Step 2: Run it to verify it fails**

Run: `cd scripts && python3 -m pytest ../tests/test_liveness.py -v`
Expected: FAIL — no `liveness` module

- [ ] **Step 3: Implement**

`scripts/mcpmeta/liveness.py`:

```python
"""Liveness derivation. Observations in, verdict out. No network here.

Rule version 1.0 — see spec §7.2. Changing any threshold bumps
RULE_VERSION so historical verdicts remain interpretable.
"""
from __future__ import annotations

from datetime import date
from urllib.parse import urlsplit

RULE_VERSION = "1.0"

_ACTIVITY_THRESHOLDS = ((30, "active"), (90, "slowing"), (365, "dormant"))


def _parse(d: str | None) -> date | None:
    if not d:
        return None
    try:
        return date.fromisoformat(d[:10])
    except ValueError:
        return None


def _norm_host(host: str) -> str:
    return host.lower().removeprefix("www.")


def derive_activity(obs: dict, today: date | None = None) -> str:
    today = today or date.today()
    if obs.get("measurement_method") in (None, "unmeasurable"):
        return "unknown"
    last = _parse(obs.get("catalog_last_entry_added"))
    if last is None:
        return "unknown"
    age = (today - last).days
    for limit, label in _ACTIVITY_THRESHOLDS:
        if age < limit:
            return label
    return "abandoned"


def derive_reachability(obs: dict, recorded_host: str) -> str:
    if obs.get("dns_resolves") is False:
        return "dead"
    status = obs.get("service_status")
    if status == 402:
        return "suspended"
    if status in (403, 429):
        return "blocked"
    if status is None:
        return "unreachable"
    if 200 <= status < 300:
        final = obs.get("service_final_url")
        if final:
            got = _norm_host(urlsplit(final).netloc)
            want = _norm_host(urlsplit(recorded_host if "//" in recorded_host
                                       else f"//{recorded_host}").netloc)
            if got and want and got != want:
                return "moved"
        return "ok"
    return "unreachable"


def derive(obs: dict, recorded_host: str, today: date | None = None) -> dict:
    today = today or date.today()
    return {
        "activity": derive_activity(obs, today),
        "reachability": derive_reachability(obs, recorded_host),
        "rule_version": RULE_VERSION,
        "computed_at": today.isoformat(),
    }
```

- [ ] **Step 4: Run the tests**

Run: `cd scripts && python3 -m pytest ../tests/ -v`
Expected: PASS (25 passed)

- [ ] **Step 5: Commit**

```bash
git add scripts/mcpmeta/liveness.py tests/test_liveness.py
git commit -m "feat(liveness): v1.0 derivation rules with false-positive regression tests"
```

---

### Task 4: Liveness probes and the `check_liveness.py` CLI

**Files:**
- Modify: `scripts/mcpmeta/liveness.py` (append probe functions)
- Create: `scripts/check_liveness.py`
- Test: `tests/test_liveness_probes.py`

**Interfaces:**
- Consumes: `mcpmeta.liveness.derive`, `mcpmeta.record.load_all`, `mcpmeta.record.save`
- Produces: `liveness.probe_web(url: str) -> dict`, `liveness.probe_dns(host: str) -> dict`, `liveness.probe_github_catalog(repo: str, catalog_path: str) -> dict`, `liveness.probe_registry_api(base_url: str) -> dict`

**Measurement-method coverage (spec §7.4).** This task implements methods 1 (`api_updated_since`), 2 (`git_log_path`) and 5 (`unmeasurable`). Methods 3 (`rss`) and 4 (`scrape`) are deferred — the vocabulary and schema already accept them, so adding a probe later needs no schema change. Anything unmeasured records `unmeasurable`, which derives to `activity: "unknown"`, never `"abandoned"`.

- [ ] **Step 1: Write the failing test (probes are stubbed; only parsing is tested)**

`tests/test_liveness_probes.py`:

```python
from mcpmeta import liveness


def test_parse_curl_output_extracts_status_and_final_url():
    out = "403\thttps://www.pulsemcp.com/\t1"
    assert liveness._parse_curl(out) == {
        "service_status": 403,
        "service_final_url": "https://www.pulsemcp.com/",
        "redirects": 1,
    }


def test_parse_curl_output_handles_zero_status():
    assert liveness._parse_curl("000\t\t0")["service_status"] is None


def test_block_reason_set_for_403():
    assert liveness._block_reason(403) == "http_403_bot_or_geo_block"
    assert liveness._block_reason(429) == "http_429_rate_limited"
    assert liveness._block_reason(200) is None


def test_registry_api_counts_are_parsed_from_metadata():
    """The official registry exposes ?updated_since= — the preferred method."""
    payload = {"servers": [{"name": "a"}, {"name": "b"}],
               "metadata": {"count": 2, "nextCursor": "a:1.0.0"}}
    got = liveness._parse_registry_page(payload)
    assert got == {"count": 2, "has_more": True}


def test_registry_api_page_without_cursor_reports_no_more():
    payload = {"servers": [], "metadata": {"count": 0}}
    assert liveness._parse_registry_page(payload)["has_more"] is False


def test_catalog_counts_bucket_commits_by_age():
    dates = ["2026-08-21", "2026-08-01", "2026-05-01", "2024-01-01"]
    from datetime import date
    got = liveness._bucket_commit_dates(dates, date(2026, 8, 31))
    assert got["catalog_last_entry_added"] == "2026-08-21"
    assert got["catalog_entries_added_30d"] == 2
    assert got["catalog_entries_added_90d"] == 2
```

- [ ] **Step 2: Run it to verify it fails**

Run: `cd scripts && python3 -m pytest ../tests/test_liveness_probes.py -v`
Expected: FAIL — `_parse_curl` not defined

- [ ] **Step 3: Append the probe helpers to `scripts/mcpmeta/liveness.py`**

```python
# --- probes -------------------------------------------------------------
import json
import subprocess
from datetime import timedelta

import requests

USER_AGENT = (
    "Mozilla/5.0 (compatible; CSA-MCP-Marketplace-Security/1.0; "
    "+https://modelcontextprotocol-security.io/)"
)


def _parse_curl(out: str) -> dict:
    code, eff, nred = (out.strip().split("\t") + ["", ""])[:3]
    status = int(code) if code.isdigit() and int(code) else None
    return {"service_status": status, "service_final_url": eff or None,
            "redirects": int(nred) if nred.isdigit() else 0}


def _block_reason(status: int | None) -> str | None:
    return {403: "http_403_bot_or_geo_block", 429: "http_429_rate_limited"}.get(status)


def _bucket_commit_dates(dates: list[str], today: date) -> dict:
    parsed = sorted((d for d in (_parse(x) for x in dates) if d), reverse=True)
    if not parsed:
        return {"catalog_last_entry_added": None,
                "catalog_entries_added_30d": None,
                "catalog_entries_added_90d": None}
    return {
        "catalog_last_entry_added": parsed[0].isoformat(),
        "catalog_entries_added_30d": sum(1 for d in parsed if (today - d).days < 30),
        "catalog_entries_added_90d": sum(1 for d in parsed if (today - d).days < 90),
    }


def probe_web(url: str, timeout: int = 20) -> dict:
    try:
        p = subprocess.run(
            ["curl", "-sS", "-o", "/dev/null", "-L", "--max-time", str(timeout),
             "--max-redirs", "5", "-A", USER_AGENT,
             "-w", "%{http_code}\t%{url_effective}\t%{num_redirects}", url],
            capture_output=True, text=True, timeout=timeout + 10)
        obs = _parse_curl(p.stdout) if p.returncode == 0 else {
            "service_status": None, "service_final_url": None, "redirects": 0}
    except Exception:
        obs = {"service_status": None, "service_final_url": None, "redirects": 0}
    obs.pop("redirects", None)
    obs["service_block_reason"] = _block_reason(obs["service_status"])
    obs["service_checked_at"] = date.today().isoformat()
    return obs


def probe_dns(host: str) -> dict:
    def dig(rtype: str) -> list[str]:
        try:
            p = subprocess.run(["dig", "+short", rtype, host],
                               capture_output=True, text=True, timeout=15)
            return [l for l in p.stdout.splitlines() if l.strip()]
        except Exception:
            return []
    addrs = dig("A") + dig("AAAA")
    return {"dns_resolves": bool(addrs), "dns_has_ns": bool(dig("NS"))}


def _parse_registry_page(payload: dict) -> dict:
    meta = payload.get("metadata") or {}
    return {"count": int(meta.get("count") or 0), "has_more": bool(meta.get("nextCursor"))}


def probe_registry_api(base_url: str, today: date | None = None) -> dict:
    """Catalog freshness for a registry implementing the MCP Registry OpenAPI.

    Preferred over git_log_path where available (spec §7.4 method 1): it
    measures the catalog directly rather than a repository that happens to
    contain it.
    """
    today = today or date.today()
    out = {"measurement_method": "unmeasurable", "catalog_last_entry_added": None,
           "catalog_entries_added_30d": None, "catalog_entries_added_90d": None,
           "catalog_size": None}
    counts = {}
    for label, days in (("catalog_entries_added_30d", 30), ("catalog_entries_added_90d", 90)):
        since = (today - timedelta(days=days)).strftime("%Y-%m-%dT00:00:00.000Z")
        try:
            r = requests.get(f"{base_url.rstrip('/')}/v0.1/servers",
                             params={"limit": 100, "updated_since": since},
                             headers={"User-Agent": USER_AGENT}, timeout=25)
            r.raise_for_status()
            counts[label] = _parse_registry_page(r.json())
        except Exception:
            return out
    out.update({
        "measurement_method": "api_updated_since",
        "catalog_entries_added_30d": counts["catalog_entries_added_30d"]["count"],
        "catalog_entries_added_90d": counts["catalog_entries_added_90d"]["count"],
    })
    # A non-empty 30-day window means at least one entry changed inside it;
    # the API gives no exact timestamp without paging the whole set, so the
    # conservative claim is "within the window", not a fabricated date.
    if out["catalog_entries_added_30d"]:
        out["catalog_last_entry_added"] = (today - timedelta(days=30)).isoformat()
    return out


def probe_github_catalog(repo: str, catalog_path: str, today: date | None = None) -> dict:
    """repo is 'owner/name'; catalog_path is the entry path, NOT the README
    unless the README genuinely is the catalog (see spec §7.4)."""
    today = today or date.today()
    try:
        p = subprocess.run(
            ["gh", "api", "--paginate",
             f"repos/{repo}/commits?path={catalog_path}&per_page=100"],
            capture_output=True, text=True, timeout=120)
        commits = json.loads(p.stdout) if p.stdout.strip().startswith("[") else []
    except Exception:
        commits = []
    if not commits:
        return {"measurement_method": "unmeasurable",
                "catalog_last_entry_added": None,
                "catalog_entries_added_30d": None,
                "catalog_entries_added_90d": None,
                "catalog_size": None}
    out = _bucket_commit_dates([c["commit"]["committer"]["date"] for c in commits], today)
    out["measurement_method"] = f"git_log_path:{catalog_path}"
    out["catalog_size"] = len(commits)
    return out
```

- [ ] **Step 4: Run the tests**

Run: `cd scripts && python3 -m pytest ../tests/ -v`
Expected: PASS (31 passed)

- [ ] **Step 5: Write the CLI**

`scripts/check_liveness.py`:

```python
#!/usr/bin/env python3
"""Refresh liveness.observations on every record, then re-derive verdicts.

Usage:
    scripts/check_liveness.py            # all records
    scripts/check_liveness.py --id mcpso # one record
    scripts/check_liveness.py --dry-run
"""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mcpmeta import liveness, record  # noqa: E402


def refresh(rec: dict, today: date) -> dict:
    obs = dict(rec.get("liveness", {}).get("observations") or {})
    host = urlsplit(rec["url"]).netloc
    obs.update(liveness.probe_web(rec["url"]))
    obs.update(liveness.probe_dns(host))
    rec.setdefault("liveness", {})["observations"] = obs
    rec["liveness"]["derived"] = liveness.derive(obs, rec["url"], today)
    return rec


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--id", help="only this record id")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    today = date.today()
    changed = 0
    for rec in record.load_all():
        if args.id and rec["id"] != args.id:
            continue
        before = rec.get("liveness", {}).get("derived", {})
        rec = refresh(rec, today)
        after = rec["liveness"]["derived"]
        moved = {k: (before.get(k), after[k]) for k in ("activity", "reachability")
                 if before.get(k) != after[k]}
        if moved:
            changed += 1
            print(f"  {rec['id']}: {moved}")
        if not args.dry_run:
            record.save(rec)
    print(f"{'would update' if args.dry_run else 'updated'} {changed} record(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 6: Commit**

```bash
chmod +x scripts/check_liveness.py
git add scripts/mcpmeta/liveness.py scripts/check_liveness.py tests/test_liveness_probes.py
git commit -m "feat(liveness): web/DNS/catalog probes and check_liveness CLI"
```

---

### Task 5: Generator — records to `marketplaces.json` and `marketplaces.csv`

**Files:**
- Create: `scripts/mcpmeta/generate.py`, `scripts/build_dataset.py`
- Test: `tests/test_generate.py`

**Interfaces:**
- Consumes: `mcpmeta.record.load_all`, `mcpmeta.schema.SCHEMA_URL`
- Produces: `generate.build_aggregate(records: list[dict]) -> dict`, `generate.build_csv_rows(records: list[dict]) -> tuple[list[str], list[list[str]]]`, `generate.CSV_COLUMNS: list[str]`, `generate.DATA_LICENSE: str`

- [ ] **Step 1: Write the failing test**

`tests/test_generate.py`:

```python
from mcpmeta import generate, schema

RECS = [
    {"$schema": schema.SCHEMA_URL, "id": "b", "name": "Bee", "url": "https://b.test",
     "status": "published", "taxonomy": {"type": "registry"},
     "operator": {"name": "Bee Inc"}, "scale": {"server_count": 12},
     "liveness": {"derived": {"activity": "active", "reachability": "ok"}}},
    {"$schema": schema.SCHEMA_URL, "id": "a", "name": "Ay", "url": "https://a.test",
     "status": "draft", "taxonomy": {"type": "tutorial"}},
]


def test_aggregate_is_sorted_by_id_and_carries_licence():
    agg = generate.build_aggregate(RECS)
    assert [m["id"] for m in agg["marketplaces"]] == ["a", "b"]
    assert agg["license"] == "CC-BY-4.0"
    assert agg["schema"] == schema.SCHEMA_URL
    assert agg["count"] == 2


def test_csv_has_stable_columns_and_sorted_rows():
    cols, rows = generate.build_csv_rows(RECS)
    assert cols == generate.CSV_COLUMNS
    assert [r[0] for r in rows] == ["a", "b"]


def test_csv_renders_missing_values_as_empty_not_the_string_none():
    _, rows = generate.build_csv_rows(RECS)
    assert "None" not in rows[0]


def test_csv_row_field_count_matches_header():
    """Keeps the generated file passing the existing scripts/validate_csv.py."""
    cols, rows = generate.build_csv_rows(RECS)
    assert all(len(r) == len(cols) for r in rows)
```

- [ ] **Step 2: Run it to verify it fails**

Run: `cd scripts && python3 -m pytest ../tests/test_generate.py -v`
Expected: FAIL — no `generate` module

- [ ] **Step 3: Implement**

`scripts/mcpmeta/generate.py`:

```python
"""Derive the published artifacts from the record store."""
from __future__ import annotations

from datetime import date

from . import schema

DATA_LICENSE = "CC-BY-4.0"

CSV_COLUMNS = [
    "id", "name", "type", "url", "operator", "status",
    "server_count", "activity", "reachability", "last_verified",
]


def _g(rec: dict, *path, default=None):
    cur = rec
    for key in path:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(key)
    return default if cur is None else cur


def build_aggregate(records: list[dict]) -> dict:
    ordered = sorted(records, key=lambda r: r["id"])
    return {
        "schema": schema.SCHEMA_URL,
        "license": DATA_LICENSE,
        "generated_at": date.today().isoformat(),
        "count": len(ordered),
        "marketplaces": ordered,
    }


def build_csv_rows(records: list[dict]) -> tuple[list[str], list[list[str]]]:
    rows = []
    for rec in sorted(records, key=lambda r: r["id"]):
        rows.append([
            rec["id"],
            rec["name"],
            _g(rec, "taxonomy", "type", default=""),
            rec["url"],
            _g(rec, "operator", "name", default=""),
            rec.get("status", ""),
            str(_g(rec, "scale", "server_count", default="")),
            _g(rec, "liveness", "derived", "activity", default=""),
            _g(rec, "liveness", "derived", "reachability", default=""),
            _g(rec, "provenance", "last_verified", default=""),
        ])
    return list(CSV_COLUMNS), rows
```

- [ ] **Step 4: Run the tests**

Run: `cd scripts && python3 -m pytest ../tests/ -v`
Expected: PASS (35 passed)

- [ ] **Step 5: Write the CLI**

`scripts/build_dataset.py`:

```python
#!/usr/bin/env python3
"""Regenerate data/marketplaces.json and data/marketplaces.csv from records.

Usage:
    scripts/build_dataset.py           # write artifacts
    scripts/build_dataset.py --check   # exit 1 if artifacts are stale (CI)
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mcpmeta import generate, record  # noqa: E402

DATA = Path(__file__).resolve().parent.parent / "data"
JSON_OUT = DATA / "marketplaces.json"
CSV_OUT = DATA / "marketplaces.csv"


def render() -> tuple[str, str]:
    recs = record.load_all()
    agg = generate.build_aggregate(recs)
    js = json.dumps(agg, indent=2, ensure_ascii=False) + "\n"

    cols, rows = generate.build_csv_rows(recs)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(cols)
    w.writerows(rows)
    return js, buf.getvalue()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="fail if the committed artifacts differ from a fresh build")
    args = ap.parse_args()

    js, cs = render()
    if args.check:
        stale = [p.name for p, new in ((JSON_OUT, js), (CSV_OUT, cs))
                 if not p.exists() or p.read_text(encoding="utf-8") != new]
        if stale:
            print(f"STALE: {', '.join(stale)} — run scripts/build_dataset.py", file=sys.stderr)
            return 1
        print("generated artifacts are up to date")
        return 0

    JSON_OUT.write_text(js, encoding="utf-8")
    CSV_OUT.write_text(cs, encoding="utf-8")
    print(f"wrote {JSON_OUT.name} and {CSV_OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

**Note on marking the CSV as generated:** no `# GENERATED FILE` banner is written into the CSV, because a comment line would break both `scripts/validate_csv.py`'s field-count check and every consumer's `csv.DictReader`. The JSON aggregate carries provenance in its `schema` / `license` / `generated_at` keys; for the CSV, CI's `--check` mode is what actually prevents hand edits, and `data/README.md` (Task 10) states it.

- [ ] **Step 6: Commit**

```bash
chmod +x scripts/build_dataset.py
git add scripts/mcpmeta/generate.py scripts/build_dataset.py tests/test_generate.py
git commit -m "feat(data): generator for marketplaces.json and marketplaces.csv"
```

---

### Task 6: Dataset validator

**Files:**
- Create: `scripts/validate_dataset.py`
- Test: `tests/test_validate_dataset.py`

**Interfaces:**
- Consumes: `mcpmeta.schema.validate_record`, `mcpmeta.vocab`, `mcpmeta.record.load_all`
- Produces: `validate_dataset.check_all(records: list[dict], repo_root: Path) -> list[str]`, `validate_dataset.check_freshness(records: list[dict], today: date, max_age_days: int = 180) -> list[str]`

Note the split: `check_all` returns **errors** (build-failing); `check_freshness` returns **warnings** (printed, non-failing). Spec §9.5 is explicit that staleness must not break the build — a marketplace nobody has re-verified recently is a prompt, not a defect.

- [ ] **Step 1: Write the failing test**

`tests/test_validate_dataset.py`:

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import validate_dataset as vd  # noqa: E402
from mcpmeta import schema  # noqa: E402

BASE = {"$schema": schema.SCHEMA_URL, "id": "a", "name": "A",
        "url": "https://a.test", "status": "draft",
        "taxonomy": {"type": "registry"}}


def test_clean_dataset_has_no_errors(tmp_path):
    assert vd.check_all([BASE], tmp_path) == []


def test_duplicate_ids_are_reported(tmp_path):
    errs = vd.check_all([BASE, dict(BASE)], tmp_path)
    assert any("duplicate id" in e for e in errs)


def test_duplicate_urls_are_reported(tmp_path):
    other = dict(BASE, id="b", name="B")
    errs = vd.check_all([BASE, other], tmp_path)
    assert any("duplicate url" in e for e in errs)


def test_level_without_evidence_is_reported(tmp_path):
    bad = dict(BASE, dimensions={"D5": {"applicable": True, "level": 2, "evidence": []}})
    errs = vd.check_all([bad], tmp_path)
    assert any("evidence" in e for e in errs)


def test_stale_last_verified_warns_but_is_not_an_error(tmp_path):
    """Spec §9.5: staleness is a warning, never a build failure."""
    from datetime import date
    old = dict(BASE, provenance={"last_verified": "2024-01-01", "sources": []})
    assert vd.check_all([old], tmp_path) == []
    warnings = vd.check_freshness([old], date(2026, 9, 1))
    assert any("last_verified" in w for w in warnings)


def test_recent_last_verified_does_not_warn(tmp_path):
    from datetime import date
    fresh = dict(BASE, provenance={"last_verified": "2026-08-31", "sources": []})
    assert vd.check_freshness([fresh], date(2026, 9, 1)) == []


def test_missing_evaluation_path_is_reported(tmp_path):
    bad = dict(BASE, evaluation={"evaluation_path": "nope/missing.md"})
    errs = vd.check_all([bad], tmp_path)
    assert any("evaluation_path" in e for e in errs)


def test_existing_evaluation_path_is_accepted(tmp_path):
    (tmp_path / "eval").mkdir()
    (tmp_path / "eval" / "a.md").write_text("x")
    ok = dict(BASE, evaluation={"evaluation_path": "eval/a.md"})
    assert vd.check_all([ok], tmp_path) == []
```

- [ ] **Step 2: Run it to verify it fails**

Run: `cd scripts && python3 -m pytest ../tests/test_validate_dataset.py -v`
Expected: FAIL — no `validate_dataset` module

- [ ] **Step 3: Implement**

`scripts/validate_dataset.py`:

```python
#!/usr/bin/env python3
"""Validate the marketplace record store.

Checks schema conformance, controlled vocabularies, referential
integrity and evidence discipline.

Usage:
    scripts/validate_dataset.py
"""
from __future__ import annotations

import sys
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mcpmeta import record, schema, vocab  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent


def check_all(records: list[dict], repo_root: Path) -> list[str]:
    errors: list[str] = []

    for rec in records:
        rid = rec.get("id", "<no id>")
        errors += [f"{rid}: {e}" for e in schema.validate_record(rec)]

        mtype = (rec.get("taxonomy") or {}).get("type")
        if mtype and mtype not in vocab.TYPES:
            errors.append(f"{rid}: type '{mtype}' not in the documented vocabulary")

        for dim, body in (rec.get("dimensions") or {}).items():
            if body.get("level") is not None and not body.get("evidence"):
                errors.append(f"{rid}/{dim}: level set without evidence")
            if body.get("applicable") is False and body.get("level") is not None:
                errors.append(f"{rid}/{dim}: not applicable but has a level")

        path = (rec.get("evaluation") or {}).get("evaluation_path")
        if path and not (repo_root / path).exists():
            errors.append(f"{rid}: evaluation_path does not exist: {path}")

    for field in ("id", "url"):
        for value, n in Counter(r.get(field) for r in records).items():
            if n > 1:
                errors.append(f"duplicate {field}: {value} ({n} records)")

    return errors


def check_freshness(records: list[dict], today: date, max_age_days: int = 180) -> list[str]:
    """Warnings, not errors. Stale verification is a prompt to re-check,
    not a reason to fail the build (spec §9.5)."""
    warnings = []
    for rec in records:
        raw = (rec.get("provenance") or {}).get("last_verified")
        if not raw:
            continue
        try:
            seen = date.fromisoformat(str(raw)[:10])
        except ValueError:
            warnings.append(f"{rec.get('id')}: unparseable last_verified: {raw!r}")
            continue
        age = (today - seen).days
        if age > max_age_days:
            warnings.append(f"{rec.get('id')}: last_verified is {age} days old ({raw})")
    return warnings


def main() -> int:
    records = record.load_all()
    errors = check_all(records, REPO_ROOT)
    warnings = check_freshness(records, date.today())
    print(f"  {'FAIL' if errors else 'ok  '}  {len(records)} record(s), "
          f"{len(errors)} issue(s), {len(warnings)} warning(s)")
    for w in warnings:
        print("    warning: " + w)
    for e in errors:
        print("    " + e, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run the tests**

Run: `cd scripts && python3 -m pytest ../tests/ -v`
Expected: PASS (43 passed)

- [ ] **Step 5: Commit**

```bash
chmod +x scripts/validate_dataset.py
git add scripts/validate_dataset.py tests/test_validate_dataset.py
git commit -m "feat(data): dataset validator with vocabulary and evidence checks"
```

---

### Task 7: Migration — legacy sources to records, with a conflict worklist

**Files:**
- Create: `scripts/mcpmeta/migrate.py`, `scripts/migrate_to_records.py`
- Test: `tests/test_migrate.py`

**Interfaces:**
- Consumes: `mcpmeta.record.slugify`, `mcpmeta.record.save`
- Produces: `migrate.parse_frontmatter(text: str) -> dict`, `migrate.parse_language_tags(text: str) -> dict[str, list[str]]`, `migrate.merge_sources(csv_row, frontmatter, langs, audit) -> tuple[dict, list[Conflict]]`, `migrate.Conflict` (dataclass: `record_id`, `field`, `values` — a `dict[str, str]` of source → value)

- [ ] **Step 1: Write the failing test**

`tests/test_migrate.py`:

```python
from mcpmeta import migrate


def test_parse_frontmatter_reads_scalar_keys():
    text = '---\ntitle: "Smithery"\ntype: "registry-api"\n---\n\n# Body\n'
    assert migrate.parse_frontmatter(text)["title"] == "Smithery"
    assert migrate.parse_frontmatter(text)["type"] == "registry-api"


def test_parse_frontmatter_returns_empty_without_frontmatter():
    assert migrate.parse_frontmatter("# Just a heading\n") == {}


def test_parse_language_tags_recovers_data_lost_everywhere_else():
    """[lang: xx] exists only in list-of-sources-marketplaces.md."""
    line = "- ShareMCP: https://sharemcp.com/ (source: https://github.com/x/y) — [lang: zh]\n"
    got = migrate.parse_language_tags(line)
    assert got["https://sharemcp.com/"] == ["zh"]


def test_parse_language_tags_splits_multi_language():
    line = "- MCP.so: https://mcp.so — [lang: en/zh/ja]\n"
    assert migrate.parse_language_tags(line)["https://mcp.so"] == ["en", "zh", "ja"]


def test_merge_records_conflict_instead_of_picking_a_winner():
    """Smithery is code-hosting in the CSV and registry-api in its own
    evaluation. Migration must surface this, never silently choose."""
    rec, conflicts = migrate.merge_sources(
        csv_row={"Marketplace Name": "Smithery", "Marketplace URL": "https://smithery.ai"},
        frontmatter={"title": "Smithery", "type": "registry-api"},
        langs={}, audit={}, csv_type="code-hosting",
    )
    assert any(c.field == "taxonomy.type" for c in conflicts)
    assert rec["taxonomy"]["type"] is None


def test_merge_leaves_unknown_fields_null_never_false():
    rec, _ = migrate.merge_sources(
        csv_row={"Marketplace Name": "X", "Marketplace URL": "https://x.test"},
        frontmatter={}, langs={}, audit={}, csv_type="registry",
    )
    assert rec["openness"]["marketplace_open_source"] is None
    assert rec["distribution"]["has_api"] is None
```

- [ ] **Step 2: Run it to verify it fails**

Run: `cd scripts && python3 -m pytest ../tests/test_migrate.py -v`
Expected: FAIL — no `migrate` module

- [ ] **Step 3: Implement**

`scripts/mcpmeta/migrate.py`:

```python
"""Convert the five legacy representations into records.

Conflicts are surfaced, never resolved. Where sources disagree the field
is written as null and a Conflict is emitted for human adjudication.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field as dc_field

import yaml

from . import record, vocab


@dataclass
class Conflict:
    record_id: str
    field: str
    values: dict[str, str] = dc_field(default_factory=dict)


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    try:
        data = yaml.safe_load(text[3:end])
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


_LANG_RE = re.compile(r"(https?://\S+?)[\s,)]*.*?\[lang:\s*([^\]]+)\]")


def parse_language_tags(text: str) -> dict[str, list[str]]:
    """Recover [lang: xx] tags, which exist ONLY in the prose sources file."""
    out: dict[str, list[str]] = {}
    for line in text.splitlines():
        m = _LANG_RE.search(line)
        if m:
            url = m.group(1).rstrip(".,);")
            out[url] = [p.strip() for p in re.split(r"[/,]", m.group(2)) if p.strip()]
    return out


def _empty(rid: str, name: str, url: str) -> dict:
    return {
        "id": rid, "name": name, "url": url, "status": "draft",
        "aliases": [], "source_code_url": None, "languages": [],
        "operator": {"name": None, "legal_entity": None, "country": None,
                     "contact_email": None},
        "taxonomy": {"type": None, "is_default_registry": None,
                     "is_aggregator": None, "is_meta_list": None},
        "custody": {"artifact_custody": None, "install_mechanisms": None,
                    "provenance": {"signing": None, "attestations": None,
                                   "sbom": None, "immutable_versions": None}},
        "execution": {"model": None, "runs_user_traffic": None,
                      "hosted_endpoint_pattern": None},
        "intake": {"mechanisms": None, "gate": None, "gate_evidence_url": None,
                   "accepts_unsolicited": None, "ingests_from": None,
                   "crawls": None, "curation_claim": None},
        "distribution": {"has_api": None, "api_spec_url": None,
                         "implements_mcp_registry_openapi": None, "has_cli": None,
                         "bulk_export_url": None, "data_license": None,
                         "rate_limit": None,
                         "mcp_access": {"first_party": None, "third_party": None,
                                        "urls": []}},
        "openness": {"marketplace_open_source": None, "license": None,
                     "catalog_data_open": None, "catalog_data_license": None},
        "feedback": {"abuse_report_url": None, "security_contact": None,
                     "security_txt": None, "vuln_disclosure_policy_url": None,
                     "takedown_policy_url": None, "observed_response": None},
        "scale": {"server_count": None, "server_count_asof": None,
                  "maintainers_count": None},
        "liveness": {"observations": {}, "derived": {}},
        "dimensions": {},
        "evaluation": {"tier_reached": None, "last_evaluated": None,
                       "evaluation_path": None, "operator_verified": None},
        "provenance": {"last_verified": None, "sources": [], "notes": None},
        "metadata": {},
    }


def _yes(v) -> bool | None:
    if v is None:
        return None
    s = str(v).strip().lower()
    return True if s in ("yes", "y", "true") else False if s in ("no", "n", "false") else None


def merge_sources(csv_row: dict, frontmatter: dict, langs: dict,
                  audit: dict, csv_type: str | None = None) -> tuple[dict, list[Conflict]]:
    name = (csv_row.get("Marketplace Name") or frontmatter.get("title") or "").strip()
    url = (csv_row.get("Marketplace URL") or frontmatter.get("url") or "").strip()
    rid = record.slugify(name)
    rec = _empty(rid, name, url)
    conflicts: list[Conflict] = []

    # type: CSV vs evaluation frontmatter may disagree
    fm_type = (frontmatter.get("type") or "").strip() or None
    candidates = {k: v for k, v in
                  {"data/marketplaces.csv": csv_type, "evaluation": fm_type}.items() if v}
    valid = {k: v for k, v in candidates.items() if v in vocab.TYPES}
    if len(set(candidates.values())) > 1:
        conflicts.append(Conflict(rid, "taxonomy.type", dict(candidates)))
        rec["taxonomy"]["type"] = None
    elif valid:
        rec["taxonomy"]["type"] = next(iter(valid.values()))
    elif candidates:
        conflicts.append(Conflict(rid, "taxonomy.type", dict(candidates)))

    rec["source_code_url"] = (csv_row.get("Source Code URL")
                              or frontmatter.get("source_code_url") or None) or None
    rec["taxonomy"]["is_aggregator"] = _yes(csv_row.get("Is Aggregator")
                                            or frontmatter.get("is_aggregator"))
    rec["taxonomy"]["is_meta_list"] = _yes(csv_row.get("Is List Of Marketplaces")
                                           or frontmatter.get("is_list_of_marketplaces"))
    rec["languages"] = langs.get(url, [])
    if frontmatter.get("operator"):
        rec["operator"]["name"] = str(frontmatter["operator"])
    if frontmatter.get("contact_email"):
        rec["operator"]["contact_email"] = str(frontmatter["contact_email"])
    if frontmatter.get("operator_jurisdiction"):
        rec["operator"]["country"] = str(frontmatter["operator_jurisdiction"])
    if frontmatter.get("last_evaluated"):
        rec["evaluation"]["last_evaluated"] = str(frontmatter["last_evaluated"])[:10]
    if frontmatter.get("security_email"):
        rec["feedback"]["security_contact"] = str(frontmatter["security_email"])

    count = frontmatter.get("server_count")
    if count is not None:
        digits = re.sub(r"[^\d]", "", str(count))
        if digits:
            rec["scale"]["server_count"] = int(digits)

    if audit:
        paths = (audit.get("web") or {}).get("paths") or {}
        if paths:
            rec["feedback"]["security_txt"] = bool(
                paths.get("/.well-known/security.txt") == 200)
        rec["provenance"]["sources"].append("working-data/audit-results")

    return rec, conflicts
```

- [ ] **Step 4: Run the tests**

Run: `cd scripts && python3 -m pytest ../tests/ -v`
Expected: PASS (49 passed)

- [ ] **Step 5: Write the migration CLI**

`scripts/migrate_to_records.py`:

```python
#!/usr/bin/env python3
"""One-shot migration of the legacy representations into records.

Reads:
  security-report/working-data/mcp-marketplaces.csv   (working tier)
  data/marketplaces.csv                               (stable tier, for type)
  security-report/evaluations/marketplaces/*.md       (frontmatter)
  security-report/working-data/list-of-sources-marketplaces.md  (languages)
  security-report/working-data/audit-results/<latest>/*.json

Writes:
  data/marketplaces/<id>.json
  docs/superpowers/plans/migration-conflicts.md

Usage:
    scripts/migrate_to_records.py --dry-run
    scripts/migrate_to_records.py
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mcpmeta import migrate, record  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
WD = ROOT / "security-report" / "working-data"
EVALS = ROOT / "security-report" / "evaluations" / "marketplaces"
CONFLICTS_OUT = ROOT / "docs" / "superpowers" / "plans" / "migration-conflicts.md"


def latest_audit_dir() -> Path | None:
    base = WD / "audit-results"
    dirs = sorted((p for p in base.glob("*") if p.is_dir()), reverse=True)
    return dirs[0] if dirs else None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    stable_types = {}
    stable_csv = ROOT / "data" / "marketplaces.csv"
    if stable_csv.exists():
        for row in csv.DictReader(stable_csv.open(encoding="utf-8")):
            stable_types[row["url"].rstrip("/")] = row.get("type")

    langs = migrate.parse_language_tags(
        (WD / "list-of-sources-marketplaces.md").read_text(encoding="utf-8"))

    frontmatters = {}
    for p in EVALS.glob("*.md"):
        if p.name == "000-template.md":
            continue
        fm = migrate.parse_frontmatter(p.read_text(encoding="utf-8", errors="replace"))
        if fm.get("url"):
            frontmatters[str(fm["url"]).rstrip("/")] = (fm, p)

    audit_dir = latest_audit_dir()
    all_conflicts, written = [], 0

    for row in csv.DictReader((WD / "mcp-marketplaces.csv").open(encoding="utf-8")):
        url_key = (row.get("Marketplace URL") or "").strip().rstrip("/")
        fm, eval_path = frontmatters.get(url_key, ({}, None))
        rid = record.slugify(row.get("Marketplace Name", ""))
        audit = {}
        if audit_dir and (audit_dir / f"{rid}.json").exists():
            audit = json.loads((audit_dir / f"{rid}.json").read_text(encoding="utf-8"))

        rec, conflicts = migrate.merge_sources(
            row, fm, langs, audit, csv_type=stable_types.get(url_key))
        if eval_path:
            rec["evaluation"]["evaluation_path"] = str(eval_path.relative_to(ROOT))
        all_conflicts += conflicts

        if args.dry_run:
            print(f"  would write {rec['id']}.json"
                  f"{'  (' + str(len(conflicts)) + ' conflict[s])' if conflicts else ''}")
        else:
            record.save(rec)
        written += 1

    lines = ["# Migration conflicts", "",
             "Fields where the legacy representations disagreed. Migration wrote "
             "`null` and left the decision here rather than guessing.", ""]
    for c in all_conflicts:
        lines.append(f"## `{c.record_id}` — `{c.field}`")
        for src, val in c.values.items():
            lines.append(f"- **{src}**: `{val}`")
        lines.append("")
    if not args.dry_run:
        CONFLICTS_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"{'would write' if args.dry_run else 'wrote'} {written} record(s), "
          f"{len(all_conflicts)} conflict(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 6: Commit**

```bash
chmod +x scripts/migrate_to_records.py
git add scripts/mcpmeta/migrate.py scripts/migrate_to_records.py tests/test_migrate.py
git commit -m "feat(data): migration from legacy representations with conflict worklist"
```

---

### Task 8: Run the migration and commit the 41 records

**Files:**
- Create: `data/marketplaces/*.json` (41), `docs/superpowers/plans/migration-conflicts.md`, `MIGRATION.md`
- Modify: `data/marketplaces.json`, `data/marketplaces.csv` (generated)

- [ ] **Step 1: Dry run and read the output**

```bash
cd /Volumes/MacMiniData/Users/kurt/GitHub/ModelContextProtocol-Security/mcpserver-marketplace
python3 scripts/migrate_to_records.py --dry-run
```

Expected: 41 records listed, with a conflict count. Do not proceed if it reports fewer than 41 — investigate the CSV read first.

- [ ] **Step 2: Run the migration for real**

```bash
python3 scripts/migrate_to_records.py
ls data/marketplaces/*.json | wc -l    # expect 41
```

- [ ] **Step 3: Validate, and fix any schema failures**

```bash
python3 scripts/validate_dataset.py
```

Expected: `ok  41 record(s), 0 issue(s)`. If records fail, the migration wrote something the schema rejects — fix `migrate.py` and re-run, rather than hand-editing records.

- [ ] **Step 4: Collect liveness for every record**

```bash
python3 scripts/check_liveness.py
python3 scripts/validate_dataset.py
```

- [ ] **Step 5: Build the generated artifacts**

```bash
python3 scripts/build_dataset.py
python3 scripts/build_dataset.py --check   # expect "up to date"
python3 scripts/validate_csv.py data/marketplaces.csv   # legacy checker still passes
```

- [ ] **Step 6: Write MIGRATION.md**

Create `MIGRATION.md` at the repo root recording: the date, the record count, which fields were derived mechanically versus carried over, the number of conflicts left for adjudication, and the note that `security-report/working-data/list-of-sources-marketplaces.md` is retained until its `[lang: xx]` tags are confirmed absorbed. Include the liveness summary produced in Step 4.

- [ ] **Step 7: Commit**

```bash
git add data/marketplaces data/marketplaces.json data/marketplaces.csv \
        docs/superpowers/plans/migration-conflicts.md MIGRATION.md
git commit -m "feat(data): migrate 41 marketplaces to per-entity records"
```

---

### Task 9: CI

**Files:**
- Create: `.github/workflows/validate-dataset.yml`, `.github/workflows/refresh-liveness.yml`
- Modify: `.github/workflows/validate-csv.yml` (scope note)

- [ ] **Step 1: Write the validation workflow**

`.github/workflows/validate-dataset.yml`:

```yaml
name: Validate dataset

on:
  pull_request:
    paths:
      - "data/**"
      - "scripts/**"
      - "tests/**"
      - ".github/workflows/validate-dataset.yml"
  push:
    branches: [main]
    paths: ["data/**", "scripts/**"]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements-dev.txt
      - name: Unit tests
        run: cd scripts && python3 -m pytest ../tests -v
      - name: Validate records
        run: python3 scripts/validate_dataset.py
      - name: Generated artifacts must not be stale
        run: python3 scripts/build_dataset.py --check
```

- [ ] **Step 2: Write the liveness refresh workflow**

`.github/workflows/refresh-liveness.yml`:

```yaml
name: Refresh liveness

on:
  schedule:
    - cron: "17 6 * * 1"      # Mondays, off the hour to avoid thundering herd
  workflow_dispatch:

permissions:
  contents: write
  pull-requests: write

jobs:
  refresh:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements-dev.txt
      - name: Probe liveness
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python3 scripts/check_liveness.py
          python3 scripts/build_dataset.py
      - uses: peter-evans/create-pull-request@v6
        with:
          branch: chore/liveness-refresh
          title: "chore(data): weekly liveness refresh"
          body: |
            Automated liveness refresh.

            Review the `activity` / `reachability` transitions before merging —
            a marketplace moving to `dead` or `suspended` is a finding, and a
            move to `blocked` usually means our probe was rejected, not that
            the site is down.
          commit-message: "chore(data): weekly liveness refresh"
```

- [ ] **Step 3: Note the older workflow's scope**

Add this comment at the top of `.github/workflows/validate-csv.yml`, below `name:`:

```yaml
# Field-count check on the GENERATED data/*.csv. Record-level validation
# lives in validate-dataset.yml; this remains as a cheap guard for the CSV
# artifact and for any hand-maintained CSV that has not yet been migrated.
```

- [ ] **Step 4: Verify locally**

```bash
cd scripts && python3 -m pytest ../tests -v && cd ..
python3 scripts/validate_dataset.py && python3 scripts/build_dataset.py --check
```

Expected: all pass.

- [ ] **Step 5: Commit and open the PR**

```bash
git add .github/workflows
git commit -m "ci: validate records, block stale artifacts, refresh liveness weekly"
git push -u origin feat/marketplace-data-model
gh pr create --title "feat: marketplace meta-registry data model" \
  --body "Implements docs/superpowers/specs/2026-08-31-mcp-marketplace-data-model-design.md. See MIGRATION.md and docs/superpowers/plans/migration-conflicts.md."
```

---

### Task 10: Documentation

**Files:**
- Modify: `CLAUDE.md`, `data/README.md`, `data/marketplaces/README.md`, `README.md`

- [ ] **Step 1: Update `CLAUDE.md`**

Replace the "Two-Tier Data Model" section with the record-store model: `data/marketplaces/<id>.json` is the source of truth; `marketplaces.json` and `marketplaces.csv` are generated and CI fails if edited by hand; add the four CLIs to the Commands section; update the CSV-validation section to point at `validate_dataset.py` as primary.

- [ ] **Step 2: Update `data/README.md` and `data/marketplaces/README.md`**

State that the CSV is generated, link the schema, document the ten dimensions and the `scored_by` vocabulary, note the CC-BY-4.0 data licence, and explain how to add a marketplace (create a record, run `build_dataset.py`).

- [ ] **Step 3: Update the root `README.md`**

Correct the broken link `./security-report/evaluations/mcp-clients/claude-desktop/` → `./security-report/evaluations/clients/claude-desktop/`, and add the dataset URLs.

- [ ] **Step 4: Verify and commit**

```bash
python3 scripts/validate_dataset.py && python3 scripts/build_dataset.py --check
git add CLAUDE.md README.md data/README.md data/marketplaces/README.md
git commit -m "docs: record store replaces the two-tier CSV model"
git push
```

---

## Follow-on work (not in this plan)

- **AI scoring pipeline** — populating D1–D10 with `scored_by: ai_evaluation` and the second validation pass. Separate spec and plan: it is prompt engineering with an evaluation harness, not TDD-able deterministic code.
- **Client dataset** — `client.v1.json` reusing these conventions (spec §13 item 4).
- **Re-scoring cadence and the operator dispute path** (spec §13.1).
- **Publication at vanity URLs** — `security-report/TODO.md` §10.
