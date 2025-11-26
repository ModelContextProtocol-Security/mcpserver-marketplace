# Security Checks for MCP Marketplaces and Clients

A checklist of security factors to evaluate.

## How to Contribute

**Think we're missing a check?** Submit a PR adding it, or file an issue describing what we should look for.

---

## Marketplace Checks

### Transparency

- [ ] **Provenance visible** - Can users see where servers come from?
- [ ] **Developer identified** - Is the developer/author clearly shown?
- [ ] **Official vs third-party** - Is there clear distinction?
- [ ] **Version information** - Is versioning visible?
- [ ] **Last updated date** - Can users see how fresh the data is?

### Verification

- [ ] **Domain validation** - For hosted servers, is domain verified?
- [ ] **GitHub org verification** - Are GitHub orgs verified with badges?
- [ ] **Vendor blessing** - Is there a process to verify official status?
- [ ] **Publisher identity** - Is publisher identity verified?

### Security Indicators

- [ ] **HTTPS required** - Are all connections HTTPS?
- [ ] **Server reachability** - Are listed servers tested for availability?
- [ ] **Security metadata** - Is security information displayed?
- [ ] **Known issues flagged** - Are vulnerabilities/issues shown?

### Feedback Mechanisms

- [ ] **Contact information** - Is there a way to contact operators?
- [ ] **Issue tracking** - Can problems be reported publicly?
- [ ] **Report button** - Can users flag specific listings?
- [ ] **Response time** - Are reports addressed promptly?

### Coverage

- [ ] **Hosted servers included** - Are vendor-hosted servers listed?
- [ ] **Official prioritized** - Are official servers given prominence?
- [ ] **Filtering available** - Can users filter by trust level?

---

## MCP Client Checks

### Discovery

- [ ] **Built-in marketplace** - Does client have curated server list?
- [ ] **Manual config** - Can users add servers manually?
- [ ] **Source transparency** - Is server source visible to users?

### Installation Security

- [ ] **Verification on install** - Are servers verified during install?
- [ ] **Warnings shown** - Are security warnings displayed?
- [ ] **Permissions declared** - Are required permissions shown?

### Runtime Security

- [ ] **Sandboxing** - Are servers sandboxed/isolated?
- [ ] **Filesystem isolation** - Is file access restricted?
- [ ] **Network isolation** - Is network access restricted?
- [ ] **Capability-based perms** - Are permissions granular?
- [ ] **User approval** - Does user approve actions?

### Credential Security

- [ ] **Secure storage** - Are credentials stored securely (keychain)?
- [ ] **No plaintext** - Are secrets not stored in plaintext config?

### Transparency

- [ ] **Provenance shown** - Can users see server origin?
- [ ] **Permissions visible** - Can users see what servers can do?
- [ ] **Activity logging** - Is server activity logged?

### Updates

- [ ] **Update mechanism** - Are servers updated?
- [ ] **Update verification** - Are updates verified/signed?
- [ ] **Rollback possible** - Can users revert to previous version?

### Enterprise

- [ ] **Admin controls** - Are there enterprise policy controls?
- [ ] **Allowlist support** - Can orgs restrict to approved servers?
- [ ] **Audit logging** - Is there audit trail for compliance?

---

## Adding New Checks

When proposing a new check, please include:

1. **What to check** - Clear description
2. **Why it matters** - Security rationale
3. **How to verify** - How an evaluator would check this
4. **Which category** - Marketplace, Client, or both
