---
title: "ToolHive Registry Server (API)"
url: "https://github.com/stacklok/toolhive-registry-server"
source_code_url: "https://github.com/stacklok/toolhive-registry-server"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "registry-api (server)"
operator: "Stacklok, Inc."
last_evaluated: "2025-12-11"
evidence:
  - url: "https://github.com/stacklok/toolhive-registry-server"
    description: "Repository landing"
  - url: "https://raw.githubusercontent.com/stacklok/toolhive-registry-server/HEAD/README.md"
    description: "README: Implements MCP Registry API; OAuth/OIDC; PostgreSQL; multi-source sync"
  - url: "https://raw.githubusercontent.com/stacklok/toolhive-registry-server/HEAD/SECURITY.md"
    description: "Security policy present in repo"
  - url: "https://raw.githubusercontent.com/stacklok/toolhive-registry-server/HEAD/LICENSE"
    description: "License present"
---

# ToolHive Registry Server (API)

## Overview
ToolHive Registry Server (thv-registry-api) implements the official MCP Registry API. It aggregates multiple sources (API, Git, file, Kubernetes, managed) into a unified registry with OAuth/OIDC authentication, optional PostgreSQL backend, and background synchronization.

## Features
- Discovery/search: Via MCP Registry API endpoints; backed by PostgreSQL/in-memory services
- One‑click install: N/A (server deployment via Docker/Task)
- Curated list/recommendations: Yes (multi-source config, enterprise curation)
- API: Yes — standards-compliant MCP Registry API v0.1; extension API; OAuth/OIDC middleware
- Client integration: Powers ToolHive Enterprise UI and integrates with Operator; clients can consume Registry API

## Marketplace Classification (Tier 0)

Type: registry-api (code-hosting/server)

Discovery & Metadata Delivery:
- Repository: https://github.com/stacklok/toolhive-registry-server
- API: MCP Registry API v0.1; extension API; OAuth/OIDC
- Docs: `docs/` in repo; configuration guides; task automation

Code/Server Delivery:
- Source: Go project; build with `task build`; Docker tasks for local run
- Hosted execution: Enterprise/self-hosted server (not public SaaS)
- Container: Docker tasks provided (`task docker-up`)

Source Accessibility:
- Source code: Public (Apache 2.0 license)
- Security policy: SECURITY.md present in repo

## Security

### Tier 1: Automated/Observable Checks (GitHub pages)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | GitHub `HTTP/2 200` |
| TLS/security headers | ✅ Strong | HSTS, XFO=deny, XCTO=nosniff, CSP present (GitHub) |
| Policy endpoints | ✅ GitHub | `/security`, `/about`, `/privacy` available on GitHub domain |
| Mixed content | ✅ None | No HTTP subresource loads detected |

### Tier 2: Repository Security Signals

| Check | Status | Evidence |
|-------|--------|----------|
| SECURITY.md present | ✅ Yes | repo `SECURITY.md` 200 |
| License | ✅ Yes | LICENSE present (Apache 2.0) |
| CI/Badges | ✅ Yes | README shows release/build/coverage badges |
| AuthN model | ✅ Yes | OAuth2/OIDC, default secure mode |

### Security Score Summary (qualitative)

Strengths:
- Implements Registry API with OAuth/OIDC and multi-source sync
- SECURITY.md and LICENSE present; clear enterprise features (audit, auth)
- Docker/Task automation with fresh state and migrations

Unknowns:
- Public hosted instance details (N/A — intended self-hosted)
- Specific scanning/signing details for images (not applicable; server codebase)

Overall Assessment: Security-forward registry server with enterprise-ready auth and sync. Good repository hygiene and docs.

## Notes

New/Interesting:
- Multi-source federation: API, Git, file, Kubernetes, managed sources unified
- Background sync coordinator with configurable intervals and retry logic
- Extension API alongside MCP Registry API

## Audit Evidence (2025‑12‑11)

- Command: `python3 security-report/tools/tier1_audit.py https://github.com/stacklok/toolhive-registry-server`
- HTTP: GitHub HSTS/CSP/XFO/XCTO present; `HTTP/2 200`.
- Repo docs: README details OAuth/OIDC, PostgreSQL backend, sync; SECURITY.md and LICENSE present.
