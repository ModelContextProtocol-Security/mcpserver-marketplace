# Evaluation Tools

Automated security audit scripts for MCP marketplaces.

## Quick Start

```bash
# Run all checks on a marketplace
python audit.py https://mcp.so

# Include repository analysis
python audit.py https://mcp.so --repo https://github.com/chatmcp/mcpso

# Human-readable summary
python audit.py https://mcp.so --format summary
```

## Tools

### audit.py (Main CLI)

Unified CLI that orchestrates all check types.

```bash
# Full audit (domain + web)
python audit.py https://mcp.so

# Full audit with repo
python audit.py https://mcp.so --repo https://github.com/owner/repo

# Individual check types
python audit.py --domain mcp.so
python audit.py --web https://mcp.so
python audit.py --repo https://github.com/owner/repo

# Output formats
python audit.py https://mcp.so --format json     # JSON (default)
python audit.py https://mcp.so --format summary  # Human-readable
```

### mcp_audit/ Package

Modular checks organized by input type:

| Module | Input | Checks |
|--------|-------|--------|
| `domain.py` | hostname | DNS (A/AAAA/CNAME/NS/MX/TXT), TLS cert, provider detection, reverse DNS |
| `web.py` | URL | HTTP status, security headers, path probes, mixed content, trackers, social links, cookies |
| `repo.py` | repo URL | SECURITY.md, org verification, activity metrics, security features, advisories |

**Direct module usage:**
```bash
python -m mcp_audit.domain mcp.so
python -m mcp_audit.web https://mcp.so
python -m mcp_audit.repo https://github.com/owner/repo
```

### tier1_audit.py (Legacy)

Original audit script. Still works, but prefer `audit.py` for new work.

```bash
python tier1_audit.py https://mcp.so
```

### batch_audit_marketplaces.py

Batch processing for multiple marketplaces from CSV.

```bash
python batch_audit_marketplaces.py
```

## Check Details

### Domain Checks (`domain.py`)

| Check | Description |
|-------|-------------|
| DNS A/AAAA | IPv4 and IPv6 addresses |
| DNS CNAME | Canonical names (reveals CDN/hosting) |
| DNS NS | Nameservers (reveals DNS provider) |
| DNS MX | Mail servers (reveals email provider) |
| DNS TXT | TXT records (SPF, DKIM hints) |
| TLS Certificate | Issuer, validity, SAN, fingerprint |
| Provider Detection | Cloudflare, AWS, Vercel, Netlify, etc. |
| Reverse DNS | PTR records for IPs |

### Web Checks (`web.py`)

| Check | Description |
|-------|-------------|
| HTTP Status | Status code, redirect chain |
| Response Time | Request timing |
| Security Headers | HSTS, CSP, XFO, XCTO, Referrer-Policy, Permissions-Policy, COOP, CORP, COEP |
| Path Probes | /privacy, /terms, /security, /.well-known/security.txt, /status, /api, /docs, etc. |
| Mixed Content | HTTP resources on HTTPS pages |
| Tracker Detection | Google Analytics, GTM, Facebook Pixel, Hotjar, etc. |
| Social Links | GitHub, Discord, Twitter, LinkedIn, email |
| Cookies | Secure, HttpOnly, SameSite flags |

### Repo Checks (`repo.py`)

| Check | Description |
|-------|-------------|
| SECURITY.md | Security policy file |
| LICENSE | License type |
| CODE_OF_CONDUCT.md | Community guidelines |
| CONTRIBUTING.md | Contribution guidelines |
| Org Verification | GitHub verified organization badge |
| Activity Metrics | Stars, forks, issues, last commit |
| Security Features | Dependabot, code scanning, branch protection |
| Security Advisories | Published vulnerability advisories |
| Signed Commits | GPG-signed commits |

## Requirements

**System tools:**
- `curl` - HTTP requests
- `dig` - DNS lookups
- `openssl` - TLS certificate inspection

**Python:** 3.10+ (uses dataclasses, type hints)

**Optional:**
- `GITHUB_TOKEN` environment variable for higher API rate limits

## Output Integration

The audit output maps to the unified evaluation template:

| Audit Section | Template Section |
|---------------|------------------|
| `domain.dns` | Part 7.3 DNS & Hosting |
| `domain.tls` | Part 7.2 TLS Certificate |
| `domain.provider_hints` | Part 7.3 DNS & Hosting |
| `web.security_headers` | Part 7.1 Web Security Headers |
| `web.paths` | Part 7.4 Path Availability |
| `web.mixed_content` | Part 7.5 Mixed Content |
| `web.trackers` | Part 5.1.1 Third-Party Integrations |
| `web.social_links` | Part 7.6 Social/Contact Links |
| `repo.security_files` | Part 5.3 Security Policy |
| `repo.org_verification` | Part 4.1 Publisher Verification |
| `repo.activity` | Part 1.3 Scale & Activity |

## Example Output

```bash
$ python audit.py https://mcp.so --format summary

============================================================
MCP AUDIT SUMMARY
============================================================

## DOMAIN CHECKS
   Hostname: mcp.so
   Registrable domain: mcp.so

   DNS Records:
     A:     76.76.21.21
     AAAA:  none
     CNAME: none
     NS:    dns1.registrar-servers.com, dns2.registrar-servers.com

   TLS Certificate:
     Issuer:  CN=E6, O=Let's Encrypt, C=US
     Valid:   Nov 15 00:00:00 2024 GMT to Feb 13 23:59:59 2025 GMT

   Provider Hints: Vercel (IP range)

## WEB CHECKS
   URL: https://mcp.so
   Status: 200
   Response time: 245ms

   Security Headers:
     Present (3): strict_transport_security, x_content_type_options, referrer_policy
     Missing (6): content_security_policy, x_frame_options, ...

   Paths Found (200): /robots.txt, /sitemap.xml, /about

   Trackers Detected (2):
     - Google Analytics (analytics)
     - Cloudflare Analytics (analytics)

============================================================
```

## Related Files

- **Templates**: `../templates/marketplace-evaluation-unified-template.md`
- **Prompts**: `../prompts/marketplace-evaluation-prompt.md`
- **Working Data**: `../working-data/mcp-marketplaces.csv`
