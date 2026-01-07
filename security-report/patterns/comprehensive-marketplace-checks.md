---
title: Comprehensive MCP Marketplace Security Checks
description: Complete checklist of all security-relevant data points to gather when evaluating an MCP marketplace
version: 1.0.0
created: 2025-01-07
updated: 2025-01-07
author: MCP Security Working Group
tags:
  - mcp-security
  - marketplace-evaluation
  - checklist
  - security-checks
usage: |
  This document is designed to be used by both humans and AI systems when evaluating
  MCP marketplaces. Each section contains checks to perform, why they matter, how to
  perform them, and what evidence to capture. Not all checks apply to all marketplace
  types - skip sections marked N/A for directory-only or informational marketplaces.
related:
  - marketplace-security-checklist.md
  - evaluation-criteria.md
  - trust-signals.md
  - ../tools/mcp_audit/
---

# Comprehensive MCP Marketplace Security Checks

This document provides an exhaustive list of data points to gather when evaluating an MCP marketplace's security posture, trustworthiness, and operational maturity.

---

## 1. Marketplace Classification

Understand what type of marketplace this is before diving into security checks.

### 1.1 Primary Type

Determine the primary function:

- **registry**: Provides programmatic API for discovery and installation (e.g., Smithery API)
- **directory**: Website listing servers with search/browse, links to external sources (e.g., mcp.so)
- **code-hosting**: Hosts actual server code/packages (e.g., npm-style registry)
- **paas**: Runs MCP servers on their infrastructure, users connect via URL (e.g., Smithery hosted)
- **client-embedded**: Built into a specific MCP client (e.g., Claude Desktop's server list)
- **curated-list**: Manually maintained list, often GitHub awesome-list style
- **hybrid**: Combination of above (document which components)

**Why it matters**: Security risks vary dramatically by type. A PaaS marketplace handling credentials has different risks than a directory that just links to GitHub repos.

**How to determine**:
- Visit the site - can you browse servers without an account?
- Is there an API? Check /api, /docs, developer documentation
- Can you install directly or does it link elsewhere?
- Does the marketplace run servers or just list them?

**Evidence to capture**:
- Primary type classification
- Secondary functions if hybrid
- Brief description of how it works

### 1.2 Basic Information

- **Official name**: As displayed on the site
- **Primary URL**: Main website
- **Tagline/description**: How they describe themselves
- **Launch date**: When did it start operating (check About page, WHOIS, Wayback Machine)
- **Server/listing count**: How many MCP servers are listed (check homepage, API)
- **Language(s)**: What languages is the UI available in
- **Geographic focus**: Global or region-specific

---

## 2. Marketplace Ownership & Control

Understanding who owns and controls the marketplace is critical for trust assessment.

### 2.1 Legal Entity

- **Legal entity name**: Official registered company name
- **Entity type**: Corporation, LLC, Foundation, Individual, Unknown
- **Parent company**: If subsidiary, who owns them
- **Incorporation jurisdiction**: Country/state of registration
- **Business registration ID**: If findable (Companies House, SEC, etc.)
- **Physical address**: Office location if disclosed

**How to find**:
- Check privacy policy - usually identifies the legal entity
- Check Terms of Service footer
- Check About page
- Search company registries (Companies House UK, Delaware Division of Corporations, etc.)
- LinkedIn company page

**Evidence to capture**:
- Exact legal entity name as stated in policies
- URL where this was found
- Jurisdiction

### 2.2 Key Personnel

- **Founders**: Who started it
- **CEO/Leadership**: Current leadership
- **Security contact**: Named security person if any
- **Team page**: Is the team publicly listed

**How to find**:
- About/Team page on website
- LinkedIn
- Crunchbase
- GitHub organization members (if open source)
- Blog post announcements

### 2.3 Funding & Business Model

- **Funding type**: VC-backed, bootstrapped, corporate-funded, community/nonprofit
- **Funding rounds**: Seed, Series A, etc. (check Crunchbase, PitchBook)
- **Total funding**: Amount raised if disclosed
- **Investors**: Notable investors
- **Revenue model**: Free, freemium, paid, enterprise, ads, data monetization
- **Pricing page**: URL to pricing if exists

**Why it matters**: Funding affects sustainability and incentives. Ad-supported marketplaces have different incentives than enterprise-focused ones. VC-backed may prioritize growth over security.

### 2.4 Domain Registration

- **Domain registrar**: Who registered the domain
- **Registration date**: When was domain first registered
- **Expiration date**: Is it close to expiring (risk of lapse)
- **Registrant**: Who owns it (often privacy-protected)
- **Name servers**: Who controls DNS

**How to check**:
```bash
whois example.com
```

**Evidence to capture**:
- Registration date
- Registrar
- Privacy protection status

### 2.5 Ownership History

- **Previous owners**: Has the domain/company changed hands
- **Acquisitions**: Has the marketplace been acquired
- **Pivots**: Has it changed purpose over time

**How to find**:
- Wayback Machine (web.archive.org) for historical snapshots
- News searches for acquisition announcements
- Crunchbase acquisition history

---

## 3. Operational Control

Who actually runs day-to-day operations and makes decisions.

### 3.1 Content Control

- **Who can add listings**: Staff only, verified publishers, anyone
- **Submission process**: Self-service, application, invitation-only
- **Review process**: Manual review, automated only, none
- **Moderation team**: Disclosed size/structure
- **Removal process**: How are bad listings removed

### 3.2 Governance

- **Decision-making**: Corporate, foundation board, community vote, DAO
- **Policy changes**: How are policy changes communicated
- **Transparency reports**: Published statistics on moderation, removals
- **Appeals process**: Can rejected submissions be appealed

### 3.3 Conflicts of Interest

- **Own servers promoted**: Does marketplace operator publish their own MCP servers
- **Paid placement**: Can publishers pay for prominence
- **Affiliate relationships**: Revenue from linking to certain servers
- **Vendor relationships**: Special relationships with certain vendors

---

## 4. Discovery & Metadata Delivery Methods

How users find and get information about MCP servers.

### 4.1 Website

- **URL**: Primary website address
- **Search functionality**: Keyword, semantic, filters available
- **Browse/categories**: Can browse by category
- **Sorting options**: By popularity, date, name, etc.
- **Responsive/mobile**: Works on mobile devices

### 4.2 Registry API

- **API exists**: Yes/No
- **API endpoint**: Base URL
- **API documentation**: URL to docs
- **Authentication required**: For read access
- **Rate limiting**: Limits on requests
- **API versioning**: How versions are handled
- **Response format**: JSON, XML, etc.

**How to check**:
- Look for /api, /docs, /api-docs, /swagger, /openapi.json
- Check developer documentation
- Try common API patterns: /api/v1/servers, /api/search

### 4.3 CLI Tool

- **CLI exists**: Yes/No
- **Package name**: npm/pip/brew package name
- **Source code**: URL to CLI source
- **Installation command**: How to install
- **Authentication**: How CLI authenticates
- **Capabilities**: What can CLI do (search, install, update, remove)

### 4.4 IDE/Editor Plugins

- **VS Code extension**: Marketplace link
- **JetBrains plugin**: Marketplace link
- **Neovim plugin**: Repository link
- **Other editors**: List any others

### 4.5 Browser Extension

- **Chrome extension**: Web Store link
- **Firefox addon**: AMO link
- **Permissions requested**: What permissions does it need

---

## 5. Code/Server Delivery Methods

How the actual MCP server code/functionality reaches users.

### 5.1 Delivery Methods Supported

Check all that apply:

- **Link to external source**: Points to GitHub/GitLab, user clones manually
- **Direct download**: Downloadable zip, tarball
- **Package manager**: npm install, pip install, etc.
- **Container image**: Docker/OCI image from registry
- **One-click install**: Installs directly to client config
- **Hosted execution**: Marketplace runs the server (PaaS model)
- **Source bundle**: Delivers source archive

### 5.2 Hosted Execution Details (if PaaS)

If the marketplace runs servers on behalf of users:

- **URL pattern**: e.g., server.smithery.ai/{name}/mcp
- **Supported transports**: HTTP, SSE, WebSocket
- **Geographic regions**: Where servers run
- **Resource limits**: CPU, memory, network limits
- **Timeout limits**: Request/connection timeouts
- **Scaling model**: Single instance, auto-scale

---

## 6. Marketplace Capabilities/Features

What features does the marketplace offer to users.

### 6.1 Discovery Features

- **Search**: Full-text, semantic, faceted
- **Filters**: By category, author, date, popularity, verified status
- **Sorting**: Options available
- **Categories/tags**: Taxonomy used
- **Recommendations**: "Similar servers", "Popular", etc.
- **Collections/lists**: User-created or curated collections

### 6.2 Server Detail Pages

- **Description**: Full description shown
- **Screenshots/demos**: Visual preview
- **Documentation**: Usage docs shown
- **Changelog**: Version history
- **Dependencies**: What it depends on
- **Compatibility**: Which clients supported

### 6.3 User Features

- **Accounts**: User accounts available
- **Favorites/bookmarks**: Save for later
- **Reviews/ratings**: User feedback
- **Comments**: Discussion on listings
- **Usage history**: Track what you've installed

### 6.4 Installation Features

- **Config generation**: Generates config snippets
- **One-click install**: Direct to client
- **Client-specific configs**: Claude Desktop, Cursor, etc.
- **Environment variable guidance**: How to set up secrets

---

## 7. Publisher Capabilities

What can publishers/developers do on the marketplace.

### 7.1 Publishing Workflow

- **Self-service**: Anyone can submit
- **Application required**: Must apply for publisher account
- **Invitation only**: Must be invited
- **Organization accounts**: Team publishing support

### 7.2 Publisher Features

- **Dashboard**: Publisher portal
- **Analytics**: Download/usage stats
- **Version management**: Publish new versions
- **Deprecation**: Mark versions deprecated
- **Transfer ownership**: Transfer to another publisher

### 7.3 Monetization

- **Paid servers**: Can charge for servers
- **Tips/donations**: Accept payments
- **Sponsorship**: Sponsor listings
- **Revenue share**: Marketplace takes cut

---

## 8. Source Accessibility

Can we audit the marketplace itself.

### 8.1 Marketplace Source Code

- **Source available**: Yes/No
- **Repository URL**: Link to source
- **License**: What license
- **Active development**: Recent commits
- **Contribution accepted**: Can community contribute

### 8.2 API Documentation

- **Public docs**: Documentation URL
- **OpenAPI/Swagger spec**: Machine-readable spec
- **Example code**: SDK, examples provided
- **Postman collection**: Pre-built API collection

### 8.3 Self-Hosting

- **Self-hostable**: Can run your own instance
- **Documentation**: Setup instructions
- **Docker/Helm**: Container deployment options

---

## 9. Server Metadata Provided

What information is shown per listing.

### 9.1 Basic Metadata

For each server listed, check if these are shown:

- **Name**: Server name
- **Description**: What it does
- **Author/publisher**: Who made it
- **Publisher verified**: Verification badge
- **Source URL**: Link to source code
- **Homepage**: Project homepage
- **License**: License type
- **Version**: Current version
- **Last updated**: When last modified
- **Created date**: When first published

### 9.2 Popularity Metrics

- **Downloads/installs**: Total count
- **Recent downloads**: Last week/month
- **Stars/likes**: User endorsements
- **Ratings**: Numeric rating
- **Reviews count**: Number of reviews

### 9.3 Technical Metadata

- **Supported transports**: stdio, HTTP, SSE
- **Supported clients**: Which MCP clients work
- **Required permissions**: What it needs access to
- **Tools provided**: List of MCP tools
- **Resources provided**: List of MCP resources
- **Prompts provided**: List of MCP prompts

### 9.4 Trust Signals

- **Verified badge**: Publisher verified
- **Official badge**: Vendor-official server
- **Security scanned**: Automated scan results
- **Audit status**: Third-party audit

---

## 10. MCP Client Integrations

How the marketplace integrates with MCP clients.

### 10.1 Known Client Integrations

For each major client, check:

- **Claude Desktop**: Integration type and depth
- **Claude Code**: Integration type and depth
- **Cursor**: Integration type and depth
- **Cline**: Integration type and depth
- **Continue**: Integration type and depth
- **Zed**: Integration type and depth
- **Other clients**: List any others

### 10.2 Integration Depth

For each integration:

- **Default source**: Is this marketplace the default
- **One-click install**: Can install without manual config
- **Config generation**: Generates config for this client
- **Live API pull**: Client fetches from marketplace API
- **Offline bundle**: Client has bundled copy
- **Search from client**: Can search marketplace from within client

### 10.3 Integration Trust Model

- **Who controls integration**: Marketplace, client vendor, third-party
- **Data flow**: What data goes between marketplace and client
- **Authentication**: How client authenticates to marketplace
- **Verification**: Does client verify servers from marketplace
- **Fallback**: What happens if marketplace is unavailable

---

## 11. CLI Tool Integrations

Command-line interface integrations.

### 11.1 Official CLI

- **Exists**: Yes/No
- **Name**: CLI tool name
- **Package**: How to install (npm, pip, brew, binary)
- **Source code**: Repository URL
- **Documentation**: Usage docs

### 11.2 CLI Capabilities

- **Search servers**: Find servers from CLI
- **Install servers**: Install to local config
- **Update servers**: Update existing installations
- **Remove servers**: Uninstall servers
- **Publish servers**: Publish new servers
- **Authentication**: Login/logout commands

### 11.3 CLI Security

- **Package signed**: Cryptographic signature
- **Checksum provided**: SHA256/SHA512 verification
- **Auto-update**: How updates work
- **Credential storage**: Where auth tokens stored

---

## 12. IDE/Editor Integrations

Editor plugin integrations.

### 12.1 VS Code

- **Extension exists**: Yes/No
- **Marketplace link**: VS Code Marketplace URL
- **Publisher**: Who published it
- **Installs**: Number of installs
- **Rating**: User rating
- **Permissions**: What permissions requested
- **Source code**: Repository URL

### 12.2 JetBrains

- **Plugin exists**: Yes/No
- **Marketplace link**: JetBrains Marketplace URL
- **Compatible IDEs**: IntelliJ, WebStorm, etc.
- **Downloads**: Number of downloads

### 12.3 Other Editors

- **Neovim**: Plugin repository
- **Emacs**: Package name
- **Vim**: Plugin name
- **Zed**: Built-in or extension
- **Others**: List any others

---

## 13. API Consumers & Cross-Marketplace

External systems that use this marketplace.

### 13.1 Known API Consumers

- **Tools using API**: List known tools
- **Services using API**: List known services
- **Other marketplaces**: Marketplaces that aggregate from this one

### 13.2 Cross-Marketplace Relationships

- **Aggregates from**: Other marketplaces this one pulls from
- **Aggregated by**: Other marketplaces that pull from this one
- **Data sharing**: Formal data sharing agreements
- **Syndication**: Content syndication arrangements

---

## 14. Integration Trust Model

Security implications of integrations.

### 14.1 Trust Boundaries

- **What data is shared**: With integrated clients/tools
- **Who can modify**: Can integrations modify marketplace data
- **Authentication method**: Between marketplace and integrations
- **Authorization scopes**: What permissions granted

### 14.2 Failure Modes

- **Marketplace down**: What happens to integrations
- **Stale data**: How long is cached data used
- **Rollback**: Can revert to previous state
- **Integrity verification**: How integrations verify data

---

## 15. DNS Checks

Domain Name System analysis.

### 15.1 DNS Records

Query and record these DNS records:

**A Records** (IPv4 addresses):
```bash
dig +short example.com A
```

**AAAA Records** (IPv6 addresses):
```bash
dig +short example.com AAAA
```

**CNAME Records** (aliases):
```bash
dig +short example.com CNAME
```

**NS Records** (nameservers):
```bash
dig +short example.com NS
```

**MX Records** (mail servers):
```bash
dig +short example.com MX
```

**TXT Records** (various policies):
```bash
dig +short example.com TXT
```

### 15.2 Email Security Records

**SPF Record**:
```bash
dig +short example.com TXT | grep spf
```

**DMARC Record**:
```bash
dig +short _dmarc.example.com TXT
```

**DKIM**: Requires knowing selector, usually found in email headers.

### 15.3 Reverse DNS

For each IP address found:
```bash
dig -x 1.2.3.4
```

### 15.4 Provider Detection

From DNS records, identify:

- **DNS provider**: Cloudflare, AWS Route53, Google Cloud DNS, etc.
- **Hosting provider**: Based on IP ranges and CNAMEs
- **CDN**: Cloudflare, Fastly, CloudFront, Akamai
- **Email provider**: Google Workspace, Microsoft 365, etc.

**Common patterns**:
- `*.ns.cloudflare.com` = Cloudflare DNS
- `*.awsdns-*.com` = AWS Route53
- CNAME to `*.cloudfront.net` = AWS CloudFront
- CNAME to `*.vercel-dns.com` = Vercel
- CNAME to `*.netlify.app` = Netlify
- CNAME to `*.github.io` = GitHub Pages

**Evidence to capture**:
- All DNS record values
- Identified providers
- Any anomalies or concerns

---

## 16. TLS/SSL Certificate Checks

Transport Layer Security analysis.

### 16.1 Certificate Details

Retrieve certificate:
```bash
echo | openssl s_client -servername example.com -connect example.com:443 2>/dev/null | openssl x509 -noout -text
```

Or for summary:
```bash
echo | openssl s_client -servername example.com -connect example.com:443 2>/dev/null | openssl x509 -noout -issuer -subject -dates -fingerprint -sha256
```

**Record**:
- **Issuer**: Certificate Authority (Let's Encrypt, DigiCert, Cloudflare, etc.)
- **Subject**: What domain(s) it's issued to
- **Valid from**: Not Before date
- **Valid until**: Not After date (check if expiring soon)
- **SHA256 fingerprint**: For verification
- **SAN (Subject Alternative Names)**: All domains covered

### 16.2 Certificate Quality

- **Certificate type**: DV, OV, or EV
- **Key size**: RSA 2048+, EC 256+
- **Signature algorithm**: SHA256 or better
- **Chain complete**: Full chain to root
- **Revocation status**: Not revoked (check OCSP)

### 16.3 TLS Configuration

Check with SSL Labs or similar:
```
https://www.ssllabs.com/ssltest/analyze.html?d=example.com
```

- **Protocols supported**: TLS 1.2, TLS 1.3 (TLS 1.0/1.1 should be disabled)
- **Cipher suites**: Strong ciphers only
- **Forward secrecy**: Supported
- **Grade**: A/B/C/D/F rating

---

## 17. HTTP Basic Checks

Basic HTTP behavior analysis.

### 17.1 HTTPS Enforcement

Check if HTTP redirects to HTTPS:
```bash
curl -sI http://example.com
```

- **HTTP behavior**: Redirects to HTTPS, serves content over HTTP, or connection refused
- **Redirect type**: 301 (permanent) vs 302 (temporary)
- **HSTS preload**: Check if in browser preload list

### 17.2 Response Analysis

```bash
curl -sI https://example.com
```

- **Status code**: 200, 301, 302, etc.
- **Response time**: How fast
- **Redirect chain**: All redirects followed
- **Final URL**: Where you end up

### 17.3 HTTP Methods

Check which methods are allowed:
```bash
curl -sI -X OPTIONS https://example.com
```

- **Allowed methods**: GET, POST, PUT, DELETE, OPTIONS
- **CORS headers**: Access-Control-Allow-Origin, etc.

---

## 18. HTTP Security Headers

Security header analysis.

### 18.1 Headers to Check

Retrieve all headers:
```bash
curl -sI https://example.com
```

Check for presence and value of:

**Strict-Transport-Security (HSTS)**:
- Forces HTTPS
- Good: `max-age=31536000; includeSubDomains; preload`
- Check: Long max-age, includeSubDomains, preload

**Content-Security-Policy (CSP)**:
- Prevents XSS, injection
- Check: Restrictive policy, no unsafe-inline/unsafe-eval

**X-Frame-Options**:
- Prevents clickjacking
- Good: `DENY` or `SAMEORIGIN`

**X-Content-Type-Options**:
- Prevents MIME sniffing
- Good: `nosniff`

**Referrer-Policy**:
- Controls referrer information
- Good: `strict-origin-when-cross-origin` or stricter

**Permissions-Policy** (formerly Feature-Policy):
- Controls browser features
- Check what's restricted

**Cross-Origin-Opener-Policy (COOP)**:
- Isolates browsing context
- Good: `same-origin`

**Cross-Origin-Resource-Policy (CORP)**:
- Controls resource sharing
- Good: `same-origin` or `same-site`

**Cross-Origin-Embedder-Policy (COEP)**:
- Controls embedding
- Good: `require-corp`

### 18.2 Header Analysis

For quick analysis, use:
- https://securityheaders.com/?q=example.com
- Browser developer tools → Network tab → Response headers

**Evidence to capture**:
- List of present headers with values
- List of missing headers
- Overall security header grade

---

## 19. Server Information

Information leaked by server headers.

### 19.1 Server Identification

From response headers, look for:

- **Server**: Web server software (nginx, Apache, cloudflare)
- **X-Powered-By**: Application framework (Express, PHP, ASP.NET)
- **Via**: Proxy/CDN information
- **X-AspNet-Version**: ASP.NET version
- **X-Generator**: CMS or generator

**Security note**: Detailed version information helps attackers. Good practice is to minimize or remove these headers.

### 19.2 CDN/Provider Detection

From headers, identify:

- **cf-ray**: Cloudflare
- **x-amz-***: AWS
- **x-vercel-***: Vercel
- **x-served-by**: Often indicates CDN

---

## 20. Policy & Legal Endpoints

Check for policy and legal pages.

### 20.1 Endpoints to Probe

For each endpoint, record status code and brief content summary:

```bash
curl -sI https://example.com/privacy
curl -sI https://example.com/privacy-policy
curl -sI https://example.com/terms
curl -sI https://example.com/tos
curl -sI https://example.com/terms-of-service
curl -sI https://example.com/legal
curl -sI https://example.com/about
curl -sI https://example.com/about-us
curl -sI https://example.com/contact
curl -sI https://example.com/contact-us
```

### 20.2 Content Analysis (if 200)

For each page that exists, review and note:

**Privacy Policy**:
- Legal entity name
- Data collected
- Third-party sharing
- Data retention
- User rights (GDPR, CCPA)
- Last updated date
- Contact for privacy requests

**Terms of Service**:
- Acceptable use
- Prohibited content
- Liability limitations
- Termination clauses
- Dispute resolution
- Governing law/jurisdiction

**About Page**:
- Company description
- Team information
- History/founding
- Mission statement

---

## 21. Security Disclosure Endpoints

Security-specific pages and files.

### 21.1 Endpoints to Probe

```bash
curl -sI https://example.com/security
curl -sI https://example.com/security/
curl -sI https://example.com/security.html
curl -sI https://example.com/security.txt
curl -sI https://example.com/.well-known/security.txt
```

### 21.2 security.txt Analysis

If security.txt exists (per RFC 9116), parse these fields:

```bash
curl -s https://example.com/.well-known/security.txt
```

- **Contact**: Security contact (email, URL, or phone)
- **Expires**: When this file expires
- **Encryption**: PGP key for encrypted reports
- **Acknowledgments**: URL to security hall of fame
- **Preferred-Languages**: Languages accepted for reports
- **Canonical**: Canonical URL for this file
- **Policy**: URL to vulnerability disclosure policy
- **Hiring**: URL to security jobs

**Evidence to capture**:
- Full security.txt contents
- Whether it's expired
- Contact method provided

### 21.3 Security Page Analysis

If /security page exists:
- Vulnerability disclosure policy
- Bug bounty program details
- Security contact
- PGP key
- Security certifications/audits
- Incident response SLA

---

## 22. Technical/Infrastructure Endpoints

Technical files and endpoints.

### 22.1 Standard Files

```bash
curl -s https://example.com/robots.txt
curl -s https://example.com/sitemap.xml
curl -sI https://example.com/status
curl -sI https://example.com/health
curl -sI https://example.com/healthz
curl -sI https://example.com/.well-known/
```

### 22.2 robots.txt Analysis

If exists, look for:
- Disallowed paths (may reveal admin areas, internal paths)
- Sitemap reference
- Crawl-delay settings

Interesting disallows to note:
- `/admin`, `/dashboard` - Admin areas
- `/api/internal` - Internal APIs
- `/debug`, `/test` - Debug endpoints

### 22.3 sitemap.xml Analysis

If exists:
- All public URLs (useful for understanding site structure)
- Last modification dates
- Priority hints

### 22.4 Status/Health Endpoints

If exists:
- Service status
- Version information
- Dependency health
- Uptime metrics

---

## 23. API Discovery Endpoints

API documentation and endpoints.

### 23.1 Endpoints to Probe

```bash
curl -sI https://example.com/api
curl -sI https://example.com/api/
curl -sI https://example.com/api/v1
curl -sI https://example.com/docs
curl -sI https://example.com/api-docs
curl -sI https://example.com/documentation
curl -sI https://example.com/swagger
curl -sI https://example.com/swagger.json
curl -sI https://example.com/swagger.yaml
curl -sI https://example.com/openapi.json
curl -sI https://example.com/openapi.yaml
curl -sI https://example.com/graphql
curl -sI https://example.com/graphql/playground
curl -sI https://example.com/graphiql
```

### 23.2 API Analysis (if found)

- **API type**: REST, GraphQL, gRPC
- **Documentation quality**: Complete, partial, none
- **Authentication**: None, API key, OAuth, JWT
- **Versioning**: URL path, header, query param
- **Rate limiting**: Documented limits
- **Response format**: JSON, XML

### 23.3 Ghost Endpoints

Note if endpoints return 200 but serve HTML (app shell) instead of API responses - this indicates catch-all routing, not actual API.

---

## 24. Content Analysis

Analysis of page content.

### 24.1 Mixed Content

Check for HTTP resources on HTTPS pages:
```bash
curl -s https://example.com | grep -oE 'http://[^"'"'"'<>]+'
```

- **HTTP links count**: How many http:// URLs
- **HTTP subresources**: Scripts, stylesheets, images loaded over HTTP
- **Samples**: Examples of mixed content found

**Exclude from concern**:
- http://localhost, http://127.0.0.1
- http://www.w3.org/ (schema URLs)
- http://schemas.* (XML schemas)

### 24.2 Third-Party Resources

Identify external resources loaded:

**Analytics/Tracking**:
- Google Analytics (google-analytics.com, gtag)
- Google Tag Manager (googletagmanager.com)
- Mixpanel, Amplitude, Segment
- Hotjar, FullStory, Heap
- PostHog, Plausible, Fathom

**Advertising**:
- Google AdSense (googlesyndication.com)
- DoubleClick (doubleclick.net)
- Facebook Pixel
- Twitter Ads
- LinkedIn Insight

**CDNs/External Resources**:
- Google Fonts
- Cloudflare CDN
- jsDelivr, cdnjs, unpkg

**Evidence to capture**:
- List of all third-party domains
- Purpose of each (analytics, ads, CDN, functionality)

### 24.3 Social Links Extraction

Find social media and contact links:
```bash
curl -s https://example.com | grep -oE 'https?://[^"'"'"'<>]*github\.com[^"'"'"'<>]*'
curl -s https://example.com | grep -oE 'https?://[^"'"'"'<>]*discord\.(gg|com)[^"'"'"'<>]*'
curl -s https://example.com | grep -oE 'https?://[^"'"'"'<>]*(twitter|x)\.com[^"'"'"'<>]*'
curl -s https://example.com | grep -oE 'https?://[^"'"'"'<>]*linkedin\.com[^"'"'"'<>]*'
curl -s https://example.com | grep -oE 'mailto:[^"'"'"'<>]*'
```

Record:
- GitHub organization/repo
- Discord server
- Twitter/X account
- LinkedIn page
- Contact emails
- YouTube channel

---

## 25. Cookie Analysis

Cookie security analysis.

### 25.1 Cookies Set

```bash
curl -sI https://example.com | grep -i set-cookie
```

For each cookie, analyze:
- **Name**: Cookie name
- **Secure flag**: Only sent over HTTPS
- **HttpOnly flag**: Not accessible to JavaScript
- **SameSite**: Strict, Lax, or None
- **Expiration**: Session or persistent
- **Domain/Path**: Scope of cookie

### 25.2 Cookie Security Assessment

- All session cookies should have Secure and HttpOnly
- Authentication cookies should have SameSite=Strict or Lax
- No sensitive data in cookie values

---

## 26. Contact & Reporting Mechanisms

How users can contact the marketplace and report issues.

### 26.1 Contact Methods

- **General email**: support@, contact@, hello@
- **Security email**: security@
- **Contact form**: /contact page with form
- **Phone**: Support phone number
- **Physical address**: Office address

### 26.2 Community Channels

- **Discord**: Server invite link
- **Slack**: Workspace link
- **Forum**: Community forum URL
- **GitHub Discussions**: If enabled on repo

### 26.3 Issue Reporting

- **Public issue tracker**: GitHub Issues, GitLab, Jira, etc.
- **Issue count**: Open issues, closed issues
- **Response time**: How fast are issues addressed
- **Issue templates**: Security issue template available

### 26.4 Security Reporting

- **Security contact**: Dedicated security email/form
- **Bug bounty**: Program details, platform (HackerOne, Bugcrowd)
- **PGP key**: For encrypted reports
- **Response SLA**: Committed response time
- **Safe harbor**: Legal protection for researchers

---

## 27. GitHub/Repository Checks

For marketplaces with public source code.

### 27.1 Repository Information

```bash
# Using GitHub API (or gh CLI)
gh api repos/owner/repo
```

- **Repository URL**: Full URL
- **Platform**: GitHub, GitLab, Bitbucket
- **Owner type**: Organization or individual
- **Visibility**: Public, private (if accessible)
- **Default branch**: main, master, etc.
- **Created date**: When repo was created
- **License**: License type

### 27.2 Activity Metrics

- **Stars**: Stargazer count
- **Forks**: Fork count
- **Watchers**: Subscriber count
- **Open issues**: Current open issues
- **Open PRs**: Current open pull requests
- **Last commit**: Date of most recent commit
- **Commit frequency**: Commits per week/month
- **Contributors**: Number of contributors
- **Last release**: Most recent release date

### 27.3 Security Files

Check for existence:
```bash
gh api repos/owner/repo/contents/SECURITY.md
gh api repos/owner/repo/contents/.github/SECURITY.md
gh api repos/owner/repo/contents/CODE_OF_CONDUCT.md
gh api repos/owner/repo/contents/CONTRIBUTING.md
```

- **SECURITY.md**: Vulnerability reporting process
- **CODE_OF_CONDUCT.md**: Community standards
- **CONTRIBUTING.md**: Contribution guidelines
- **LICENSE**: License file and type

### 27.4 Organization Verification

For GitHub organizations:
```bash
gh api orgs/orgname
```

- **Is organization**: vs individual account
- **Verified badge**: Organization is verified
- **Verified domain**: Domain linked to org
- **2FA required**: Org requires 2FA for members (if visible)

### 27.5 Security Features

- **Dependabot enabled**: Automated dependency updates
- **Code scanning enabled**: CodeQL or other SAST
- **Secret scanning enabled**: Detects leaked secrets
- **Branch protection**: Protected branches configured
- **Signed commits**: Commits are GPG signed
- **Security advisories**: Published CVEs/advisories

### 27.6 Repository Quality

- **README quality**: Comprehensive, has badges, clear instructions
- **Documentation**: Docs folder or wiki
- **Tests**: Test suite present
- **CI/CD**: GitHub Actions or other CI
- **Code coverage**: Coverage badges/reports
- **Linting**: Code quality checks

---

## 28. Trust & Verification Signals

How the marketplace establishes trust.

### 28.1 Publisher Verification

- **Verification exists**: Is there a verified publisher concept
- **Criteria documented**: What does "verified" mean
- **Process documented**: How to become verified
- **Verification levels**: Multiple tiers (verified, official, etc.)

### 28.2 Server Verification

- **Automated scanning**: Are servers scanned
- **Manual review**: Is there human review
- **Scan results visible**: Can users see scan results
- **Known vulnerabilities shown**: CVE display

### 28.3 Official vs Third-Party

- **Distinction made**: Is official vs community clear
- **Visual indicator**: Badge, label, section
- **Official criteria**: What makes something "official"
- **Vendor verification**: How vendor ownership is verified

### 28.4 Provenance Display

- **Source visible**: Can see source code link
- **Author visible**: Can see who made it
- **Version history**: Can see past versions
- **Commit/build link**: Can trace to specific commit

---

## 29. Publisher/Authentication Requirements

For marketplaces where users can publish.

### 29.1 Account Creation

- **Registration method**: Email, OAuth, invitation
- **Email verification**: Required
- **Identity verification**: Real identity required
- **Organization accounts**: Team support

### 29.2 Authentication Security

- **2FA available**: TOTP, SMS
- **2FA required**: Mandatory for publishers
- **Hardware keys**: WebAuthn/FIDO support
- **SSO/OAuth**: GitHub, Google, etc.
- **OAuth scopes**: What permissions requested

### 29.3 API Authentication

- **API tokens**: Personal access tokens
- **Token expiration**: Tokens expire
- **Token scopes**: Granular permissions
- **Token rotation**: Can rotate tokens
- **Credential storage**: Where tokens stored

### 29.4 Session Security

- **Session duration**: How long sessions last
- **Session invalidation**: Logout everywhere
- **Concurrent sessions**: Limits on sessions
- **Session binding**: IP, device binding

---

## 30. Known Vendor-Hosted Server Coverage

Does the marketplace list official vendor-hosted MCP servers.

### 30.1 Vendor Servers to Search For

Search the marketplace for these known vendor-hosted servers:

- **Vercel**: mcp.vercel.com
- **Ramp**: mcp.ramp.com
- **Stripe**: Stripe MCP
- **Linear**: Linear MCP
- **Cloudflare**: Cloudflare MCP
- **HuggingFace**: huggingface.co/mcp
- **Sentry**: Sentry MCP
- **Notion**: Notion MCP

### 30.2 Coverage Assessment

- **Vendor servers found**: List which are present
- **Vendor servers missing**: List which are absent
- **Third-party alternatives**: Are unofficial versions listed instead
- **Distinction clear**: Can users tell official from unofficial

---

## 31. Supply Chain Security

For code-hosting and PaaS marketplaces.

### 31.1 Code Integrity

- **Package signing**: Cryptographic signatures
- **Checksum verification**: SHA256/SHA512 hashes
- **Provenance attestation**: SLSA, Sigstore, etc.
- **Reproducible builds**: Can verify builds
- **SBOM**: Software Bill of Materials available

### 31.2 Dependency Security

- **Dependency scanning**: Automated vuln scanning
- **Vulnerability display**: CVEs shown to users
- **Dependency updates**: Automated or manual
- **Lock file required**: Deterministic installs
- **Dependency confusion protection**: Namespace protection

### 31.3 Namespace Security

- **Naming convention**: owner/name, scoped, flat
- **Typosquatting protection**: Similar name detection
- **Reserved names**: Vendor names protected
- **Name reuse policy**: What happens to deleted names

### 31.4 Build Security

- **Build isolation**: Builds sandboxed
- **Build logs**: Available to publisher
- **Build reproducibility**: Same input = same output
- **Build secrets**: How secrets handled in build

---

## 32. Hosted Execution/PaaS Checks

For marketplaces that run MCP servers.

### 32.1 Isolation

- **Process isolation**: Containers, VMs, etc.
- **Network isolation**: Network namespace, firewall
- **Filesystem isolation**: Read-only, tmpfs
- **Resource limits**: CPU, memory, network caps

### 32.2 Secret Management

- **Secret storage**: How credentials stored
- **Encryption**: At rest encryption
- **Access control**: Who can access secrets
- **Secret rotation**: Can rotate secrets
- **Secret exposure risk**: June 2025 Smithery-style vulns

### 32.3 Execution Environment

- **Runtime**: Node.js, Python, etc.
- **Runtime version**: Supported versions
- **Environment variables**: What's exposed
- **File system access**: What can be read/written
- **Network access**: What can be reached

### 32.4 Audit & Logging

- **Request logging**: Are requests logged
- **Audit trail**: Who did what when
- **Log access**: Can users access logs
- **Log retention**: How long kept
- **Security monitoring**: Anomaly detection

### 32.5 Data Residency

- **Execution region**: Where servers run
- **Data storage region**: Where data stored
- **Compliance**: SOC2, GDPR, HIPAA claims

---

## 33. Privacy & Data Collection

Privacy and data practices.

### 33.1 Data Collection

From privacy policy and observation:

- **Account data**: Email, name, profile
- **Usage data**: What you browse, install
- **Analytics data**: Page views, clicks
- **Device data**: Browser, OS, IP
- **Payment data**: If paid features

### 33.2 Data Sharing

- **Analytics providers**: Google Analytics, etc.
- **Advertising networks**: If any
- **Third-party services**: Payment, email, etc.
- **Data sales**: Is data sold
- **Government requests**: Policy on requests

### 33.3 Data Rights

- **Access rights**: Can request your data
- **Deletion rights**: Can delete account/data
- **Export rights**: Can export your data
- **Opt-out**: Can opt out of tracking
- **GDPR/CCPA compliance**: Claimed compliance

### 33.4 Retention

- **Data retention period**: How long data kept
- **Deletion policy**: What happens on account deletion
- **Backup retention**: How long backups kept

---

## 34. External Research & Reputation

Research the marketplace's reputation externally.

### 34.1 Search Queries to Run

**Reddit**:
```
site:reddit.com "{marketplace name}"
site:reddit.com "{marketplace name}" security
site:reddit.com "{marketplace name}" MCP
```

**Hacker News**:
```
site:news.ycombinator.com "{marketplace name}"
```

**Twitter/X**:
```
"{marketplace name}" MCP
"{marketplace name}" security
"{marketplace name}" vulnerability
```

**General**:
```
"{marketplace name}" MCP review
"{marketplace name}" MCP security
"{marketplace name}" vulnerability
"{marketplace name}" breach
"{marketplace name}" CVE
```

### 34.2 What to Look For

- **General sentiment**: Positive, negative, neutral
- **Security concerns raised**: Any red flags mentioned
- **Reliability issues**: Downtime, bugs reported
- **Customer experiences**: Support quality
- **Expert opinions**: Security researcher commentary
- **Comparisons**: How it compares to alternatives

### 34.3 Evidence to Capture

- Links to notable discussions
- Summary of sentiment
- Any security concerns raised
- Date of most recent significant discussion

---

## 35. Incident & Vulnerability History

Past security incidents and vulnerabilities.

### 35.1 CVE Search

```
site:cve.mitre.org "{marketplace name}"
site:nvd.nist.gov "{marketplace name}"
```

Or use CVE database search tools.

### 35.2 Security Advisories

- **Published advisories**: On their site, GitHub
- **Severity**: Critical, High, Medium, Low
- **Response time**: How fast were they fixed
- **Disclosure process**: Coordinated or not

### 35.3 Incident History

- **Known breaches**: Data breaches
- **Known outages**: Major downtime
- **Known vulnerabilities**: Publicly disclosed
- **Response quality**: How well handled

### 35.4 Bug Bounty History

- **Program exists**: HackerOne, Bugcrowd profile
- **Reports resolved**: Number of fixed issues
- **Bounties paid**: Total paid out
- **Response time**: Average time to fix

---

## 36. Community Trust Signals

Community indicators of trustworthiness.

### 36.1 Ecosystem Standing

- **Age**: How long has it operated
- **Official recognition**: Listed in official MCP docs
- **Client recommendations**: Recommended by which clients
- **Awesome-list inclusion**: In curated lists

### 36.2 Team Reputation

- **Founders known**: Public, reputable founders
- **Team background**: Security experience
- **Conference presence**: Talks, presentations
- **Publications**: Blog posts, papers

### 36.3 Backing & Support

- **Corporate backing**: Backed by known company
- **VC backing**: Reputable investors
- **Community backing**: Open source community
- **Foundation**: Nonprofit foundation

### 36.4 Transparency

- **Open source**: Code is open
- **Public roadmap**: Future plans shared
- **Changelog**: Changes communicated
- **Blog/updates**: Regular communication

---

## Appendix A: Command Reference

Quick reference for common audit commands.

### DNS

```bash
# All records
dig example.com ANY

# Specific records
dig +short example.com A
dig +short example.com AAAA
dig +short example.com CNAME
dig +short example.com NS
dig +short example.com MX
dig +short example.com TXT

# DNSSEC
dig +dnssec example.com

# Reverse DNS
dig -x 1.2.3.4
```

### TLS/SSL

```bash
# Certificate details
echo | openssl s_client -servername example.com -connect example.com:443 2>/dev/null | openssl x509 -noout -text

# Certificate summary
echo | openssl s_client -servername example.com -connect example.com:443 2>/dev/null | openssl x509 -noout -issuer -subject -dates

# Certificate chain
echo | openssl s_client -servername example.com -connect example.com:443 -showcerts 2>/dev/null
```

### HTTP

```bash
# Headers only
curl -sI https://example.com

# Follow redirects
curl -sIL https://example.com

# With timing
curl -sI -w "Time: %{time_total}s\n" https://example.com

# Full response
curl -s https://example.com
```

### WHOIS

```bash
whois example.com
```

### GitHub API

```bash
# Repo info
gh api repos/owner/repo

# Org info
gh api orgs/orgname

# Check file exists
gh api repos/owner/repo/contents/SECURITY.md
```

---

## Appendix B: Evidence Checklist

Minimum evidence to capture for each evaluation:

- [ ] Screenshots of key pages (homepage, about, privacy, security)
- [ ] Full HTTP headers from main URL
- [ ] DNS records (A, AAAA, NS, MX, TXT)
- [ ] TLS certificate details
- [ ] robots.txt contents
- [ ] security.txt contents (if exists)
- [ ] Privacy policy summary
- [ ] Terms of service summary
- [ ] Contact methods found
- [ ] Social links found
- [ ] Third-party services detected
- [ ] GitHub repo details (if applicable)
- [ ] Search result summaries for external research
- [ ] Any security concerns or red flags

---

## Appendix C: Red Flags Quick Reference

Immediate concerns:
- No HTTPS or invalid certificate
- No contact information
- No privacy policy
- Domain registered very recently
- WHOIS privacy on business site
- No way to report security issues
- Ghost endpoints (200 but wrong content)

Investigate further:
- Missing security headers
- Excessive tracking
- No Terms of Service
- Anonymous operators
- No issue tracker
- Unresponsive to contact attempts
- Bad reputation in searches
- Past security incidents with poor response

---

## Appendix D: Update History

| Date | Version | Changes |
|------|---------|---------|
| 2025-01-07 | 1.0.0 | Initial comprehensive checklist |
