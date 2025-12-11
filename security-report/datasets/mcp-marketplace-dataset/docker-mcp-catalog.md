---
title: "Docker MCP Catalog"
url: "https://hub.docker.com/mcp"
source_code_url: "https://github.com/docker/mcp-registry"
is_marketplace: yes
is_aggregator: yes
is_list_of_marketplaces: no
language: "en"
type: "code-linking + curated catalog"
operator: "Docker, Inc."
contact_email: "security@docker.com (for security disclosures; see Docker security policy)"
last_evaluated: "2025-12-11"
evidence:
  - url: "https://hub.docker.com/mcp"
    description: "Catalog landing page (Cloudflare; HSTS, XFO, XCTO present)"
  - url: "https://github.com/docker/mcp-registry"
    description: "Official Docker MCP Registry repo (curation flow, two submission types)"
  - url: "https://raw.githubusercontent.com/docker/mcp-registry/HEAD/README.md"
    description: "README: enterprise security claims (signatures, provenance, SBOMs) for Docker-built images"
  - url: "https://raw.githubusercontent.com/docker/mcp-registry/HEAD/CONTRIBUTING.md"
    description: "Contribution process; review required; CI checks; uses forms for test credentials"
  - url: "https://raw.githubusercontent.com/docker/mcp-registry/HEAD/LICENSE"
    description: "MIT license for the catalog repo"
  - url: "https://raw.githubusercontent.com/docker/mcp-registry/HEAD/.github/SECURITY.md"
    description: "Docker-wide SECURITY policy (present in .github/SECURITY.md)"
  - url: "https://hub.docker.com/robots.txt"
    description: "robots.txt present"
  - url: "https://hub.docker.com/sitemap.xml"
    description: "sitemap.xml present"
  - url: "https://hub.docker.com/mcp/robots.txt"
    description: "/robots.txt 200"
  - url: "https://hub.docker.com/mcp/sitemap.xml"
    description: "/sitemap.xml 200"
---

# Docker MCP Catalog

## Overview
Docker MCP Catalog is Docker’s curated MCP server catalog surfaced at `hub.docker.com/mcp`, Docker Desktop’s MCP Toolkit, and the `mcp` namespace on Docker Hub. The associated `docker/mcp-registry` repository documents the contribution workflow and enforcement model.

## Features
- Discovery/search: Yes (via Docker Hub UI; curated presentation)
- One‑click install: Partial (Docker Desktop integration for MCP Toolkit)
- Curated list/recommendations: Yes (review by Docker team required)
- API: ❓ Unknown (no public catalog API documented)
- Client integration: Yes (Docker Desktop MCP Toolkit)

## Marketplace Classification (Tier 0)

Type: hybrid (code-linking/categorized catalog; Docker may build and host images)

Discovery & Metadata Delivery:
- Website: https://hub.docker.com/mcp (present)
- Registry API: none documented for the catalog itself (Docker Hub APIs exist for images)
- CLI: Docker Desktop / Docker CLI integration (indirect)
- IDE plugin: none specific
- Client integration: Docker Desktop’s MCP Toolkit
- Browser extension: none

Code/Server Delivery:
- Link to source: Yes (curated entries link back to upstream GitHub repos)
- Local installation via CLI: Yes (containerized servers via Docker)
- Package download: Container images (Docker Hub)
- Hosted execution (PaaS/SaaS): No (runs locally in containers)
- Container image: Yes (Docker-built or self-provided images)
- Source bundle: N/A

Source Accessibility:
- Marketplace source code: https://github.com/docker/mcp-registry (catalog metadata + tooling)
- API docs: none specific to `/mcp` catalog (Docker Hub/image APIs exist)
- Self-hostable: N/A (catalog is operated by Docker)

Server Coverage:
- Lists vendor-hosted servers: No (focus is on containerized local execution)
- Distinguishes hosted vs local: Yes (Docker-built vs self-provided image paths; local container model)
- Vendor-hosted servers found: N/A (model is local container execution)

## Security

### Tier 1: Automated/Observable Checks (2025‑12‑11)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Yes | `HTTP/2 200` via Cloudflare |
| TLS certificate | ✅ Yes | Cloudflare edge |
| No mixed content | ✅ Yes | No HTTP subresource loads; textual `http://desktop.docker.com/mcp/...` references |
| Security headers | ✅ Good | HSTS present; X-Frame-Options: deny; X-Content-Type-Options: nosniff |
| Contact information | ✅ Yes | Docker security contact via corporate security policy |
| Issue tracker | ✅ Yes | GitHub issues in `docker/mcp-registry` |
| Provenance visible | ✅ Partial | Entries link to upstream repos; Docker-built images include signing/provenance per README |
| Official vs third‑party distinction | ✅ Yes | Two submission models: Docker-built (enhanced security) vs self-provided |
| Last updated timestamps | ❓ Unknown | Not directly shown on catalog landing, present in Git repos/images metadata |

DNS/CDN and Hosting:
- CNAME: `hub.docker.com.cdn.cloudflare.net` (Cloudflare CDN)
- NS (docker.com): AWS Route 53 (`ns-207.awsdns-25.com`, etc.)
- Provider: Cloudflare CDN; Docker.com DNS on AWS Route 53

### Tier 2: Manual Investigation

| Check | Status | Notes |
|-------|--------|-------|
| Privacy policy exists | ✅ Yes | Docker privacy/legal are on `www.docker.com/legal/` (not on hub subpaths) |
| Terms of service | ✅ Yes | Docker ToS via corporate legal pages |
| Legal entity identified | ✅ Yes | Docker, Inc. |
| Data collection disclosed | ✅ Yes | Corporate privacy pages |
| Publisher verification documented | ✅ Yes | Contribution process requires Docker review; PR + CI |
| Moderation policy public | ✅ Partial | Non-compliant servers may be removed (README) |
| Report button | ✅ Yes | Issues in repo; Docker support channels |
| Vulnerability disclosure policy | ✅ Yes | Docker SECURITY policy in `.github/SECURITY.md` |
| Badge criteria/process | ✅ Partial | Docker-built path promises signatures, provenance, SBOMs; criteria implied in CONTRIBUTING |

### Tier 3: Registry‑Specific (code-hosting/containerized execution)

| Check | Status | Notes |
|-------|--------|-------|
| 2FA required for publishers | ✅ Yes | Docker and GitHub org security norms; contributors via PR review |
| Token scopes/expiry | ✅ Yes | GitHub workflows; Docker image signing/provenance noted |
| Malware/dependency scanning | ✅ Likely | Docker Hub/scan tools; README claims security checks before publish |
| Namespace/typosquatting protection | ✅ Yes | Curated namespace; Docker review gate |
| Runtime isolation | ✅ Yes | Local container isolation (Docker Desktop) |
| Package signing/provenance | ✅ Yes | Docker-built images include signatures, SBOMs, provenance (per README) |

### Security Score Summary (qualitative)

Strengths:
- Curated process with PR review and CI
- Local container isolation avoids host arbitrary code execution
- Docker-built images: signatures, provenance, SBOMs, auto-updates (per README)
- Strong baseline security headers via Cloudflare (HSTS, XFO, XCTO)

Weaknesses / Unknowns:
- Catalog API not documented; catalog freshness not displayed on landing
- Mixed model (Docker-built vs self-provided) requires users to note which they’re using

Overall Assessment: Stronger posture due to curation, container isolation, and documented security enhancements for Docker-built images. Considered a safer on-ramp for MCP servers in enterprise/dev environments.

## Notes

New/Interesting:
- The hub page embeds textual references to `http://desktop.docker.com/mcp/catalog/v2/...` endpoints (likely internal/static catalog assets used by Desktop); not active subresource loads.
- The GitHub README explicitly commits to Docker-built image security features: signatures, provenance attestation, and SBOMs — uncommon among current MCP catalogs.
- `.github/SECURITY.md` is present in the org-level scaffolding for security disclosures.

## Delivery Method Security

- Website: Cloudflare CDN; HSTS, XFO, XCTO headers; corporate legal on `www.docker.com/legal`.
- API: No public catalog API documented; Docker Hub APIs for images exist.
- CLI/Local: Container isolation for local execution; Docker Desktop integration.
- Client Integration: Docker Desktop MCP Toolkit consumes the catalog.

## Vendor‑Hosted Coverage Test

How tested:
- Focus is on containerized/local servers; vendor-hosted URLs not expected.

Result: N/A by design; catalog curates containerized servers.

## Red Flags

- None critical observed. Minor unknown: lack of public docs for a catalog API.

## Recommendations

For Operator:
- Consider publishing a minimal catalog API spec or update cadence metrics for transparency.

For Users:
- Prefer Docker-built images to benefit from signatures, SBOMs, and provenance; review each server’s README and configuration/secrets model before enabling.

## Audit Evidence (2025‑12‑11)

- Command: `python3 security-report/tools/tier1_audit.py https://hub.docker.com/mcp`
- HTTP: `HTTP/2 200`; Cloudflare; HSTS; X-Frame-Options: deny; X-Content-Type-Options: nosniff.
- DNS: CNAME `hub.docker.com.cdn.cloudflare.net`; docker.com NS: AWS Route 53.
- Mixed content: 0 HTTP subresources; ~49 textual `http://desktop.docker.com/mcp/...` links.
- Policy endpoints on hub subdomain: `/robots.txt` 200; `/sitemap.xml` 200; privacy/terms hosted on `www.docker.com/legal/`.
- Repo docs: README affirms signatures/provenance/SBOMs; CONTRIBUTING describes PR review; LICENSE MIT; SECURITY policy present at org-level `.github/SECURITY.md`.

### Automated Audit (PoC) — 2025-12-11

- HTTP status chain: HTTP/2 200
- Provider hints: Cloudflare (Server header), Cloudflare (cf-ray)
- DNS: A=hub.docker.com.cdn.cloudflare.net., 104.18.43.187, 172.64.144.69; CNAME=hub.docker.com.cdn.cloudflare.net.; NS=ns-207.awsdns-25.com., ns-568.awsdns-07.net., ns-1289.awsdns-33.org.
- Security headers: HSTS=max-age=31536000, XFO=deny, XCTO=nosniff
- Mixed content: http_subresources=0; http_literals=49
- Policy endpoints 200: /robots.txt, /sitemap.xml
- API endpoints 200: (none)
- Social links detected: 54 (showing up to 5)
  - x: 
  - github: https://github.com/docker/mcp-registry/blob/main/CONTRIBUTING.md
  - github: https://github.com/awslabs/mcp/tree/666202ec3c13ac2ca9f9490b80c6eb19d25a8b10/src/core-mcp-server\
  - github: https://github.com/awslabs/mcp\
  - github: https://github.com/brave/brave-search-mcp-server/tree/42138c5f768c1a2e2ca5801e52d45ba0868d6c49\

How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.

