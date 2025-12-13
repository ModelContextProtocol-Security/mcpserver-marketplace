# MCP Marketplace Security Evaluation Project

Systematically evaluating MCP marketplaces, registries, directories, and how MCP clients handle server discovery and installation.

## Project Status

**Active** - 40+ marketplaces cataloged, 130+ clients tracked, comprehensive evaluations in progress.

See [TODO.md](./TODO.md) for long-term goals and roadmap.

---

## What We're Evaluating

### 1. MCP Marketplaces

Places where users discover MCP servers:

| Type | Description | Examples |
|------|-------------|----------|
| **Registry** | Programmatic API for discovery | Smithery, MCP Registry |
| **Directory** | Website listing with search | MCP.so, PulseMCP |
| **Code Hosting** | Hosts packages/source | Docker MCP Catalog |
| **PaaS/Hosted** | Runs servers for users | Smithery (hosted mode) |
| **Curated List** | Manually maintained | awesome-mcp-servers |
| **Client-Embedded** | Built into MCP client | Cline, LobeChat |

### 2. MCP Clients

How clients handle server installation, permissions, and security:

- Discovery/marketplace features
- Installation and runtime security
- Permission models and sandboxing
- Credential storage
- Update mechanisms

---

## Directory Structure

```
security-report/
├── README.md                          # You are here
├── TODO.md                            # Long-term goals and roadmap
├── MCP-MARKETPLACE-SECURITY-EVAL-*.md # Project governance docs
│
├── working-data/                      # Development datasets (snapshot for reports)
│   ├── mcp-marketplaces.csv           # Working list of 40+ marketplaces
│   ├── mcp-clients.csv                # Working list of 130+ MCP clients
│   ├── list-of-sources-*.md           # Data source documentation
│   ├── audit-results/                 # Batch audit output (JSON per marketplace)
│   │   └── YYYY-MM-DD/                # Date-stamped runs
│   │       ├── index.json             # Summary manifest
│   │       └── [marketplace].json     # Individual audit results
│   ├── scripts/                       # Data extraction scripts
│   │   ├── extract_mcp_clients.py
│   │   └── generate_marketplaces_from_csv.py
│   └── sources/                       # Raw HTML captures for reproducibility
│       └── [source files]
│
├── evaluations/                       # Security evaluation results
│   ├── marketplaces/                  # 40+ marketplace evaluations
│   │   ├── smithery-playground.md     # Comprehensive (code-hosting/PaaS)
│   │   ├── docker-mcp-catalog.md      # Comprehensive (curated catalog)
│   │   ├── mcp.so.md                  # Comprehensive (directory)
│   │   └── [40+ more...]
│   └── clients/                       # 130+ client evaluations
│       ├── claude-desktop/            # Detailed evaluation
│       └── [130+ client files]
│
├── prompts/                           # AI evaluation prompts
│   ├── marketplace-evaluation-prompt.md            # How to evaluate marketplaces
│   ├── marketplace-evaluation-validation-prompt.md # How to peer-review evaluations
│   ├── mcp-client-evaluation-prompt.md             # How to evaluate clients
│   ├── mcp-client-evaluation-validation-prompt.md  # How to peer-review client evals
│   ├── mcp-marketplace-discovery-prompt.md         # How to discover new marketplaces
│   └── mcp-client-marketplace-detection-prompt.md  # Detect marketplace features in clients
│
├── templates/                         # Evaluation templates
│   ├── marketplace-evaluation-unified-template.md  # Main template (questionnaire + report)
│   ├── marketplace-evaluation-outreach-template.md # Email templates for operators
│   └── mcp-client-evaluation.md
│
├── tools/                             # Automated evaluation tools
│   ├── audit.py                       # Main CLI for single-marketplace audits
│   ├── batch_audit.py                 # Batch processing from CSV
│   ├── mcp_audit/                     # Modular audit package
│   │   ├── domain.py                  # DNS, TLS, provider detection
│   │   ├── web.py                     # HTTP, headers, paths, trackers
│   │   └── repo.py                    # GitHub security analysis
│   └── tier1_audit.py                 # Legacy script (still works)
│
├── reports/                           # Published analysis reports
│   ├── mcp-marketplaces-report.md     # Marketplace discovery snapshot
│   └── mcp-client-marketplace-analysis-report.md  # Client marketplace features
│
├── patterns/                          # Reusable evaluation frameworks
│   ├── checks.md                      # Security checks we look for
│   ├── evaluation-criteria.md         # Detailed criteria and gaps
│   └── trust-signals.md               # What good looks like
│
└── research/                          # Background research
    └── lessons-from-package-registries.md
```

---

## Working Data vs Stable Data

This project uses a two-tier data model:

| Location | Purpose | Status |
|----------|---------|--------|
| `security-report/working-data/` | Development datasets with evaluation status columns | Active development |
| `../data/` (repo root) | Stable reference datasets | Synced when stable |

The `working-data/` directory contains snapshots used for security reports. Once data is validated and complete, it will be synced to the root `data/` directory.

---

## Datasets

### mcp-marketplaces.csv

Working list of MCP marketplaces with evaluation status:

| Column | Description |
|--------|-------------|
| Marketplace Name | Official name |
| Marketplace URL | Primary URL |
| Source Code URL | GitHub/GitLab if available |
| Is Marketplace | yes/no |
| Is Aggregator | yes/no (lists servers from multiple sources) |
| Is List Of Marketplaces | yes/no (meta-list) |
| Evaluation Status | Comprehensive / Tier 1-2 / Stub / Blocked |

**Current stats:** 40+ marketplaces cataloged

### mcp-clients.csv

Working list of MCP clients:

| Column | Description |
|--------|-------------|
| MCP Client Name | Official name |
| MCP Client Main URL | Primary URL |
| MCP Client Source Code URL | GitHub/GitLab if available |
| Listed In modelcontextprotocol.io | Yes/No |

**Current stats:** 130+ clients tracked

---

## Evaluation Tiers

### Marketplace Evaluations

| Tier | Description | Checks |
|------|-------------|--------|
| **Tier 0** | Classification | Type, delivery model, source accessibility |
| **Tier 1** | Automated/Observable | HTTPS, headers, DNS, policy endpoints, contact info |
| **Tier 2** | Manual Investigation | Privacy policy, ToS, publisher verification, moderation |
| **Tier 3** | Registry-Specific | 2FA, malware scanning, signing, provenance, isolation |

### Evaluation Status

| Status | Meaning |
|--------|---------|
| **Comprehensive** | Full Tier 0-3 evaluation with evidence |
| **Tier 1-2 moderate** | Automated + some manual checks |
| **Tier 1 basic** | Automated checks only |
| **Stub** | Minimal frontmatter, needs evaluation |
| **Blocked** | Site inaccessible (403, down, etc.) |

---

## Tools

See [tools/README.md](./tools/README.md) for full documentation.

### Automated Audit Package (`mcp_audit/`)

Modular Python package for security checks, organized by input type:

| Module | Input | Checks |
|--------|-------|--------|
| `domain.py` | hostname | DNS (A/AAAA/CNAME/NS/MX/TXT), TLS cert, provider detection |
| `web.py` | URL | HTTP, 9 security headers, path probes, trackers, social links |
| `repo.py` | repo URL | SECURITY.md, org verification, activity, security features |

```bash
# Single marketplace
python audit.py https://mcp.so --format summary

# With repository
python audit.py https://mcp.so --repo https://github.com/chatmcp/mcpso

# Individual checks
python -m mcp_audit.domain mcp.so
python -m mcp_audit.web https://mcp.so
python -m mcp_audit.repo https://github.com/owner/repo
```

### Batch Audit (`batch_audit.py`)

Runs audits on all marketplaces from CSV in parallel:

```bash
python batch_audit.py              # All 41 marketplaces
python batch_audit.py --dry-run    # Preview what would run
python batch_audit.py --limit 5    # Test with subset
```

### Pre-collected Audit Data

**Location:** `working-data/audit-results/YYYY-MM-DD/`

Batch audit results are stored as JSON files. Before manually running checks, look here first:

```
working-data/audit-results/2025-12-12/
├── index.json              # Summary of all audits
├── mcpso.json              # MCP.so domain + web + repo data
├── smithery-playground.json
└── ... (41 total)
```

Each JSON contains domain checks, web checks, and/or repo checks depending on the marketplace type.

---

## Templates

### Unified Marketplace Template

`templates/marketplace-evaluation-unified-template.md`

Single template serving three purposes:
1. **Questionnaire** - Structured Q&A for community engagement
2. **Report Format** - Final evaluation document
3. **Audit Target** - Fields populated by tier1_audit.py

**Sections:**
1. Identity & Classification
2. Discovery & Access
3. Server Delivery Model
4. Trust & Verification
5. Policies & Legal
6. Supply Chain Security
7. Technical Security Posture
8. Operator Transparency
9. Security Incidents
10. Delivery Method Security
11. Evaluator Assessment

### Outreach Template

`templates/marketplace-evaluation-outreach-template.md`

Email templates for contacting marketplace operators to verify findings before publication.

---

## Evaluation Lifecycle

This project uses a **two-AI model**: one AI creates evaluations, another AI validates them.

```
Discovery → Creation → Validation → Publication
```

| Phase | Description | Key Files |
|-------|-------------|-----------|
| **Discovery** | Find new marketplaces/clients | `prompts/mcp-marketplace-discovery-prompt.md` |
| **Creation** | Produce initial evaluation | `prompts/marketplace-evaluation-prompt.md` |
| **Validation** | Peer-review, catch errors | `prompts/marketplace-evaluation-validation-prompt.md` |
| **Publication** | Finalize, contact operator | `templates/marketplace-evaluation-outreach-template.md` |

**Why two AIs?** No single AI's output is accepted without verification. The validation step catches factual errors, omissions, and reduces bias. See [VALIDATION_GOALS.md](./VALIDATION_GOALS.md) for details.

For the full workflow, see [prompts/README.md](./prompts/README.md).

---

## How to Contribute

### Evaluate a Marketplace

1. **Check status**: Look in `working-data/mcp-marketplaces.csv` for current evaluation status
2. **Get audit data**: Check `working-data/audit-results/YYYY-MM-DD/` for pre-collected JSON data
   - If missing or stale, run `python audit.py <url>` to generate fresh data
3. **Read the prompt**: `prompts/marketplace-evaluation-prompt.md` explains the full evaluation process
4. **Use the template**: `templates/marketplace-evaluation-unified-template.md` is the target format
5. **Create evaluation**: Write markdown file in `evaluations/marketplaces/`
   - Use audit JSON to fill in Tier 1 (automated) sections
   - Manually investigate Tier 2-3 sections (policies, verification, security features)
6. **Validate**: Have another AI review using `prompts/marketplace-evaluation-validation-prompt.md`
7. **Update CSV**: Set new evaluation status in `working-data/mcp-marketplaces.csv`
8. **Submit PR**

### Evaluate an MCP Client

1. Check `working-data/mcp-clients.csv`
2. Read `prompts/mcp-client-evaluation-prompt.md`
3. Use `templates/mcp-client-evaluation.md`
4. Create evaluation in `evaluations/clients/`
5. **Validate**: Have another AI review using `prompts/mcp-client-evaluation-validation-prompt.md`
6. Submit PR

### Add a Missing Marketplace/Client

1. Add entry to appropriate CSV in `working-data/`
2. Create stub file in appropriate `evaluations/` subdirectory
3. Submit PR

### Improve Evaluation Criteria

1. Edit `patterns/checks.md` or `patterns/evaluation-criteria.md`
2. Update templates if needed
3. Submit PR

---

## Completed Evaluations

### Comprehensive Marketplace Evaluations

| Marketplace | Type | Key Findings |
|-------------|------|--------------|
| [Smithery](evaluations/marketplaces/smithery-playground.md) | Registry/PaaS | Largest registry (3200+ servers), June 2025 path traversal vuln (fixed 48hrs), 5.2% secret leak rate |
| [Docker MCP Catalog](evaluations/marketplaces/docker-mcp-catalog.md) | Curated Catalog | Signatures/provenance/SBOMs, PR review required, SECURITY.md present |
| [MCP.so](evaluations/marketplaces/mcp.so.md) | Directory | Missing security headers, no ToS, ghost API endpoints |
| [ToolHive](evaluations/marketplaces/toolhive-registry.md) | Registry | Container isolation, encrypted secrets, open source |

### MCP Client Evaluations

| Client | Date | Link |
|--------|------|------|
| Claude Desktop | 2025-11-19 | [Evaluation](./evaluations/clients/claude-desktop/) |

---

## Related Documents

- [TODO.md](./TODO.md) - Long-term goals and roadmap
- [VALIDATION_GOALS.md](./VALIDATION_GOALS.md) - Two-AI validation system
- [Project Goals](./MCP-MARKETPLACE-SECURITY-EVAL-GOALS.md) - Full project objectives
- [Evaluation Criteria](./patterns/evaluation-criteria.md) - Detailed criteria
- [Security Checks](./patterns/checks.md) - What we look for
- [Contributing Guidelines](./MCP-MARKETPLACE-SECURITY-EVAL-CONTRIBUTING.md) - How to participate

---

## License

This security research is provided for informational purposes. Evaluations are based on publicly available information and are subject to change as marketplaces evolve.
