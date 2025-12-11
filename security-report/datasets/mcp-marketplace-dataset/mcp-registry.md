---
title: "MCP Registry"
url: "https://registry.modelcontextprotocol.io/docs"
source_code_url: "https://github.com/modelcontextprotocol/registry"
is_marketplace: no
is_aggregator: no
is_list_of_marketplaces: no
language: "en"
type: "official registry api"
operator: "Model Context Protocol"
last_evaluated: "2025-12-11"
evidence:
  - url: "https://registry.modelcontextprotocol.io/docs"
    description: "Docs site"
  - url: "https://registry.modelcontextprotocol.io/openapi.json"
    description: "OpenAPI JSON present"
  - url: "https://registry.modelcontextprotocol.io/openapi.yaml"
    description: "OpenAPI YAML present"
  - url: "https://github.com/modelcontextprotocol/registry"
    description: "Registry repo"
---

# MCP Registry

## Overview
Official MCP Registry API endpoint and documentation. Provides list/search endpoints for MCP servers; consumed by clients and aggregators.

## Features
- Discovery/search: Yes (API)
- API: Yes (OpenAPI available at `/openapi.json` and `/openapi.yaml`)
- Client integration: Yes (intended for programmatic consumption)

## Marketplace Classification (Tier 0)

Type: official registry api

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 200` |
| TLS/security headers | ⚠️ Partial | HSTS present; CSP/XFO/XCTO not visible on docs response |
| No mixed content | ✅ Yes | 0 HTTP subresource loads detected |
| API docs | ✅ Yes | `/openapi.json` and `/openapi.yaml` present |

DNS/Hosting:
- NS: Cloudflare (todd/chin)
- CNAME: `prod.registry.modelcontextprotocol.io` → A: 34.61.200.254

## Notes

New/Interesting:
- OpenAPI spec includes rich schemas for server metadata and security-relevant fields (e.g., icons, variables, package integrity fields).
