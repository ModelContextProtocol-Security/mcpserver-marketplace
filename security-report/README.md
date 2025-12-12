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
│   ├── tier1_audit.py                 # Security checks (headers, DNS, TLS, endpoints)
│   └── batch_audit_marketplaces.py    # Batch processing
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

### tier1_audit.py

Automated security checks for marketplaces:

```bash
python3 security-report/tools/tier1_audit.py https://example.com
```

**Checks performed:**
- HTTPS and redirect chain
- Security headers (HSTS, CSP, XFO, XCTO, Referrer-Policy, etc.)
- TLS certificate details
- DNS records and provider hints
- Policy endpoints (/privacy, /terms, /security, etc.)
- API endpoints (/api, /docs, /swagger, /openapi, etc.)
- Mixed content detection
- Social/contact link extraction

**Output:** JSON to stdout

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

## How to Contribute

### Evaluate a Marketplace

1. Check `working-data/mcp-marketplaces.csv` for status
2. Read `prompts/marketplace-evaluation-prompt.md`
3. Use `templates/marketplace-evaluation-unified-template.md`
4. Run `tools/tier1_audit.py` for automated checks
5. Create evaluation in `evaluations/marketplaces/`
6. Update CSV with new evaluation status
7. Submit PR

### Evaluate an MCP Client

1. Check `working-data/mcp-clients.csv`
2. Read `prompts/mcp-client-evaluation-prompt.md`
3. Use `templates/mcp-client-evaluation.md`
4. Create evaluation in `evaluations/clients/`
5. Submit PR

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
- [Project Goals](./MCP-MARKETPLACE-SECURITY-EVAL-GOALS.md) - Full project objectives
- [Evaluation Criteria](./patterns/evaluation-criteria.md) - Detailed criteria
- [Security Checks](./patterns/checks.md) - What we look for
- [Contributing Guidelines](./MCP-MARKETPLACE-SECURITY-EVAL-CONTRIBUTING.md) - How to participate

---

## License

This security research is provided for informational purposes. Evaluations are based on publicly available information and are subject to change as marketplaces evolve.
