# Evaluation Tools

Automated security audit scripts.

## Available Tools

### tier1_audit.py

Automated Tier 1 security checks for marketplace URLs.

```bash
python3 tier1_audit.py https://example.com
```

**Checks performed:**
- HTTP status and redirect chain
- Security headers (HSTS, CSP, XFO, XCTO, Referrer-Policy, Permissions-Policy)
- TLS certificate details (issuer, validity, fingerprint)
- DNS records (A, AAAA, CNAME, NS) and provider hints
- Policy endpoints (/privacy, /terms, /security, /robots.txt, etc.)
- API endpoints (/api, /docs, /swagger, /openapi)
- Mixed content detection
- Social/contact link extraction

**Output:** JSON to stdout

**Usage in evaluations:**
1. Run against marketplace URL
2. Paste JSON output into evaluation's "Audit Evidence" section
3. Use results to populate Part 7 (Technical Security Posture)

### batch_audit_marketplaces.py

Batch processing for multiple marketplaces.

```bash
python3 batch_audit_marketplaces.py
```

Reads from `working-data/mcp-marketplaces.csv` and audits all URLs.

## Requirements

```bash
pip install requests dnspython
```

## Output Integration

The tier1_audit.py output maps to the unified template:

| Audit Output | Template Section |
|--------------|------------------|
| `security_headers` | Part 7.1 Web Security Headers |
| `tls_certificate` | Part 7.2 TLS Certificate |
| `dns` | Part 7.3 DNS & Hosting |
| `path_checks` | Part 7.4 Path Availability |
| `mixed_content` | Part 7.5 Mixed Content |
| `social_links` | Part 7.6 Social/Contact Links |

## Related Files

- **Templates**: `../templates/marketplace-evaluation-unified-template.md` - Where audit results go
- **Prompts**: `../prompts/marketplace-evaluation-prompt.md` - How to use audit results
- **Working Data**: `../working-data/mcp-marketplaces.csv` - URL list for batch audits
