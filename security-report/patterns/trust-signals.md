# Trust Signals for MCP Servers

What "good" looks like when evaluating MCP server trustworthiness.

## Trust Signal Hierarchy

Users should prioritize trust signals in this order:

### Tier 1: Highest Trust

1. **Vendor-hosted at main domain**
   - URL pattern: `vendor.com/mcp` or `mcp.vendor.com`
   - Why: Vendor controls domain, has accountability
   - Example: `mcp.vercel.com`, `mcp.ramp.com`

2. **Built into trusted application**
   - Curated by application vendor (e.g., Claude Desktop built-in)
   - Why: Vendor reputation at stake, presumably vetted
   - Caveat: Verify what "curated" actually means

### Tier 2: High Trust

3. **GitHub organization with verified badge**
   - Verified badge links to vendor's domain
   - Example: github.com/elevenlabs (verified to elevenlabs.io)
   - Why: Domain ownership verified by GitHub

4. **Linked from vendor's official documentation**
   - Vendor docs point to specific MCP server
   - Why: Explicit vendor endorsement

### Tier 3: Moderate Trust

5. **Listed in reputable marketplace with verification**
   - Marketplace has documented verification process
   - Server has "verified" or "official" badge
   - Why: Third-party vetting provides some assurance

6. **Clear developer attribution with track record**
   - Known developer/maintainer with history
   - Active maintenance and issue response
   - Why: Reputation-based trust

### Tier 4: Lower Trust ("Wild West")

7. **Third-party implementation without clear provenance**
   - Unknown developer
   - No verification or official status
   - Why: Anyone can publish, minimal accountability

8. **Unusual domain structures**
   - Subdomains of generic cloud services
   - Domain doesn't match expected vendor
   - Why: May be legitimate, may be impersonation

9. **AI agent recommendation without verification**
   - AI suggested based on training data
   - No real-time security check
   - Why: AI may not evaluate trustworthiness

---

## Red Flags

### Immediate Concerns

- HTTP instead of HTTPS
- Domain typosquatting (googIe vs google)
- Logo/branding mismatch with actual vendor
- No developer attribution at all
- Requests excessive permissions without explanation

### Investigate Further

- Very new with no history
- Copied/forked from unknown source
- No documentation or sparse README
- Inactive/abandoned (no updates in 6+ months)
- Dependencies from unknown sources

---

## What Good Looks Like

### For Marketplaces

- Clear distinction between official and community servers
- Verification badges that mean something
- Security metadata displayed (scan results, known issues)
- Easy to see developer and source
- Responsive to security reports

### For MCP Clients

- Sandboxing by default
- Permissions shown before installation
- User approval for sensitive actions
- Secure credential storage
- Easy to remove/disable servers

### For Vendors

- Official MCP server hosted at vendor domain
- Linked from vendor's own documentation
- Clear versioning and update process
- Security contact for reports
- Transparent about what the server can access

---

## Contributing

**Think we're missing a trust signal?** File an issue or submit a PR.

**Have examples of good (or bad) trust signals?** Share them - real examples help.
