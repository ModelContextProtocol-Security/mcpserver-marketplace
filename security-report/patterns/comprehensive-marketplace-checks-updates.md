---
title: Comprehensive MCP Marketplace Security Checks - Lifecycle & Notifications Update
description: Additional checks for versioning, updates, notifications, deprecation, and emergency response
version: 1.0.0
created: 2025-01-07
updated: 2025-01-07
author: MCP Security Working Group
status: draft - to be merged into comprehensive-marketplace-checks.md
tags:
  - mcp-security
  - marketplace-evaluation
  - versioning
  - notifications
  - lifecycle
  - security-advisories
usage: |
  This document contains additional checks to be added to comprehensive-marketplace-checks.md.
  These checks focus on the lifecycle of MCP servers: versioning, updates, problem notifications,
  deprecation, and emergency response capabilities. These are critical for ongoing security
  but are often overlooked in initial marketplace evaluations.
related:
  - comprehensive-marketplace-checks.md
  - evaluation-criteria.md
---

# MCP Marketplace Checks: Lifecycle & Notifications

This document covers checks related to the ongoing lifecycle of MCP servers listed in marketplaces - how versions are managed, how users are notified of problems, and how bad servers can be removed or disabled.

---

## 37. Server Versioning

How the marketplace handles versions of MCP servers.

### 37.1 Version Display

- **Version number shown**: Is current version displayed on listing?
- **Version format**: Semantic versioning (1.2.3), date-based, or arbitrary?
- **Version history visible**: Can users see previous versions?
- **Version count**: How many versions are retained/shown?
- **Latest version highlighted**: Is "latest" clearly marked?

**How to check**:
- Visit a server detail page
- Look for version number, version dropdown, or history tab
- Check if API returns version information

**Evidence to capture**:
- Screenshot of version display
- Example version strings
- Whether history is accessible

### 37.2 Version Metadata

Per version, is this information available:

- **Release date**: When was this version published?
- **Changelog/release notes**: What changed?
- **Breaking changes flagged**: Are breaking changes highlighted?
- **Deprecation warnings**: Is version marked deprecated?
- **Minimum client version**: Required client compatibility?
- **Dependency versions**: What dependencies and their versions?

### 37.3 Version Selection

- **Pin to version**: Can users install specific versions?
- **Version ranges**: Can users specify version constraints (^1.0.0, ~1.2)?
- **Lock file support**: Does installation create reproducible lock?
- **Default version policy**: Always latest? Stable? User choice?

### 37.4 Version Immutability

- **Versions immutable**: Once published, can a version be modified?
- **Re-upload same version**: Can same version number be republished?
- **Yanking**: Can versions be removed but not replaced?
- **Version tombstones**: Are removed versions marked as such?

**Why immutability matters**: Mutable versions enable supply chain attacks where a "safe" version is later replaced with malicious code.

**Evidence to capture**:
- Policy documentation on version immutability
- Test: Can a publisher modify an existing version?

---

## 38. Update Mechanisms

How updates are distributed and managed.

### 38.1 Update Discovery

How do users learn about updates:

- **Marketplace shows "update available"**: Visual indicator on listing
- **Client shows "update available"**: In-app notification
- **Email notifications**: Opt-in/opt-out update emails
- **RSS/Atom feed**: Per-server or global update feed
- **Webhook notifications**: For automated systems
- **API endpoint for version check**: Programmatic version query

**How to check**:
- Install a server, wait for update, observe notification
- Check for RSS/feed links on marketplace
- Check API documentation for version endpoints
- Check notification settings in user account

### 38.2 Update Distribution

How updates reach users:

- **Manual update**: User must explicitly update
- **Prompted update**: User prompted but can decline
- **Auto-update**: Updates applied automatically
- **Staged rollout**: Updates rolled out gradually
- **Canary releases**: Early access to new versions

### 38.3 Update Verification

- **Update integrity**: Are updates verified (signature, checksum)?
- **Update authenticity**: Is update from legitimate source?
- **Rollback on failure**: If update fails, what happens?
- **Update audit log**: Record of what was updated when?

### 38.4 Rollback Capability

- **Rollback supported**: Can users revert to previous version?
- **Rollback method**: UI button, CLI command, config edit?
- **Rollback limitations**: How far back can you rollback?
- **Automatic rollback**: On failure, auto-revert?
- **Data migration**: What happens to data on rollback?

**Evidence to capture**:
- Documentation on update process
- Screenshot of update notification (if observable)
- Rollback instructions

---

## 38B. Marketplace-Provided Update Tooling

Some marketplaces provide their own update mechanisms (CLI, API, UI) rather than relying on users to manually update.

### 38B.1 Update Tools Provided

What update tooling does the marketplace offer:

- **CLI update command**: e.g., `smithery update`, `mcp update`
- **GUI update button**: One-click update in web UI
- **Bulk update**: Update all installed servers at once
- **Selective update**: Update specific servers
- **API endpoint**: Programmatic update trigger
- **Client plugin**: Update from within MCP client

**How to check**:
- Check CLI documentation for update commands
- Look for "Update" button on installed servers page
- Check API docs for update endpoints

### 38B.2 Update Process Control

- **Preview changes**: Can see what will change before updating
- **Dry run**: Test update without applying
- **Dependency resolution**: Handles dependency updates together
- **Conflict resolution**: How are conflicts handled
- **Atomic updates**: All-or-nothing updates

### 38B.3 Update Policies & Automation

Marketplace-level update policies:

- **Auto-update available**: Can enable automatic updates
- **Auto-update scope**:
  - All updates
  - Security updates only
  - Patch versions only (1.0.x)
  - Minor versions (1.x.0)
- **Auto-update opt-in vs opt-out**: Default behavior
- **Forced updates**: Can marketplace force critical updates?
- **Update schedule**: Can schedule update windows
- **Update frequency**: How often auto-updates run

### 38B.4 PaaS/Hosted Update Model

For marketplaces that run servers (PaaS model):

- **Who controls versions**: User or marketplace?
- **Version pinning**: Can users pin to specific version on hosted?
- **Auto-upgrade policy**: Are hosted servers auto-upgraded?
- **Upgrade notification**: Warning before hosted upgrade?
- **Downtime during updates**: Is there downtime?
- **Blue-green deployments**: Zero-downtime updates?
- **Rollback on failure**: Automatic rollback if update breaks?

### 38B.5 Update Verification & Safety

- **Pre-update checks**: Compatibility verification
- **Post-update validation**: Health check after update
- **Automatic rollback triggers**: What triggers rollback
- **Update logs**: Record of what was updated
- **Checksum verification**: Verify integrity during update
- **Signature verification**: Verify authenticity during update

### 38B.6 Enterprise Update Controls

For enterprise/team deployments:

- **Staged rollouts**: Update subset of users first
- **Approval workflow**: Require approval before updates
- **Change management integration**: ITSM/ticketing integration
- **Update windows**: Restrict updates to maintenance windows
- **Exemptions**: Exclude specific servers from auto-update
- **Audit logging**: Who approved/triggered updates

**Evidence to capture**:
- CLI update command documentation
- Screenshot of update UI
- Auto-update policy documentation
- PaaS version control documentation

---

## 39. Security Advisories

How security problems are communicated.

### 39.1 Advisory System Existence

- **Has advisory system**: Does marketplace publish security advisories?
- **Advisory location**: Where are advisories published?
  - Dedicated security page (/security/advisories)
  - GitHub Security Advisories
  - Separate security.txt contact
  - Blog posts
  - Email list
- **Advisory format**: Structured (CVE, GHSA) or ad-hoc?
- **Advisory history**: Archive of past advisories?

**How to check**:
- Search site for "advisory", "CVE", "vulnerability"
- Check /security, /advisories, /security/advisories
- Check GitHub repo Security tab
- Search for "[marketplace name] CVE" or "[marketplace name] vulnerability"

### 39.2 Advisory Content

When an advisory is published, does it include:

- **Affected servers**: Which servers are affected?
- **Affected versions**: Which versions specifically?
- **Severity rating**: CVSS score, Critical/High/Medium/Low
- **CVE identifier**: If applicable
- **Description**: What is the vulnerability?
- **Impact**: What can an attacker do?
- **Mitigation**: How to protect yourself?
- **Fixed version**: Which version fixes it?
- **Discovery credit**: Who found it?
- **Timeline**: When discovered, reported, fixed, disclosed?

### 39.3 Advisory Timeliness

- **Time to advisory**: How fast are advisories published after fix?
- **Coordinated disclosure**: Do they follow responsible disclosure?
- **Embargo policy**: How long before public disclosure?
- **Pre-notification**: Do major users get early warning?

### 39.4 Advisory Subscription

How users can subscribe to advisories:

- **Email subscription**: Sign up for security alerts
- **RSS/Atom feed**: Security advisory feed
- **GitHub watch**: Watch for security advisories
- **Webhook**: Automated notification
- **API**: Query for advisories programmatically
- **In-app alerts**: Notifications in marketplace UI
- **Client integration**: Alerts in MCP client

**Evidence to capture**:
- URL to advisory page/feed
- Example advisory (if any exist)
- Subscription options available
- Whether any advisories have been published historically

---

## 40. In-Client Security Warnings

How MCP clients are notified of problems with installed servers.

### 40.1 Client Warning Capability

Does the marketplace provide data that enables client warnings:

- **Vulnerability flag in API**: Can clients query if server has known vulns?
- **Deprecation flag in API**: Can clients query if server is deprecated?
- **Removal flag in API**: Can clients query if server was removed?
- **Severity data**: Is severity provided for client to display?
- **Message/description**: Is warning message provided?

### 40.2 Client Warning Display

For clients that integrate with this marketplace:

- **Warning on vulnerable server**: Does client show warning?
- **Warning on deprecated server**: Does client indicate deprecation?
- **Warning on removed server**: Does client warn if server was yanked?
- **Block execution option**: Can client block known-bad servers?
- **Forced update**: Can marketplace force client to update server?

### 40.3 Real-time vs Cached

- **Real-time checks**: Does client check status on each use?
- **Cached checks**: How often does client refresh status?
- **Offline behavior**: What happens if can't reach marketplace?
- **Staleness indicator**: Does client show when data is stale?

**Evidence to capture**:
- API documentation for vulnerability/status endpoints
- Client behavior when server has known issues
- Caching/refresh policy

---

## 41. Deprecation & End-of-Life

How servers are phased out.

### 41.1 Deprecation Process

- **Deprecation status exists**: Can servers be marked deprecated?
- **Deprecation visibility**: How is deprecation shown?
  - Banner on listing page
  - Badge/label
  - Separate deprecated section
  - Search filter for deprecated
- **Deprecation reason**: Is reason provided?
- **Replacement recommendation**: Is alternative suggested?
- **Deprecation timeline**: Is removal date announced?

### 41.2 Deprecation Notifications

When a server is deprecated:

- **Email to users**: Are installers notified by email?
- **In-app notification**: Alert in marketplace UI?
- **Client notification**: Warning in MCP client?
- **API flag**: Status in API response?

### 41.3 End-of-Life Policy

- **EOL policy documented**: Is there a documented EOL policy?
- **EOL timeline**: How long from deprecation to removal?
- **Grace period**: Warning period before removal?
- **Data preservation**: What happens to server data after EOL?

### 41.4 Migration Support

- **Migration guide**: Documentation for moving to alternative?
- **Automated migration**: Tools to help migrate?
- **Data export**: Can users export their data/config?

**Evidence to capture**:
- Deprecation policy documentation
- Example of deprecated server (if any)
- EOL timeline if documented

---

## 42. Server Removal & Yanking

How problematic servers are removed.

### 42.1 Removal Capabilities

- **Publisher can remove**: Can publisher delete their server?
- **Marketplace can remove**: Can marketplace staff remove servers?
- **Removal types**:
  - **Soft delete**: Hidden but data preserved
  - **Hard delete**: Completely removed
  - **Yank**: Removed from new installs but existing can use
  - **Quarantine**: Disabled pending investigation

### 42.2 Removal Triggers

What causes removal:

- **Publisher request**: Publisher wants to remove
- **Policy violation**: Violates ToS/content policy
- **Security issue**: Contains vulnerability or malware
- **Legal request**: DMCA, court order, etc.
- **Abandonment**: Inactive for extended period
- **Report threshold**: Enough user reports

### 42.3 Removal Process

- **Removal review**: Is there review before removal?
- **Publisher notification**: Is publisher notified before removal?
- **User notification**: Are users of server notified?
- **Appeal process**: Can removal be appealed?
- **Removal timeline**: How fast can bad servers be removed?

### 42.4 Post-Removal Behavior

When a server is removed:

- **Listing page**: What does the old URL show? (404, tombstone, redirect)
- **Existing installations**: Do they continue working?
- **Name reuse**: Can the name be claimed by someone else?
- **Name squatting protection**: Is removed name reserved?
- **Historical record**: Is there record it existed?

**Evidence to capture**:
- Removal policy documentation
- Example of removed server page (if accessible)
- Name reuse policy

---

## 43. Emergency Response & Kill Switch

Handling critical security emergencies.

### 43.1 Emergency Takedown

- **Emergency removal capability**: Can critical threats be removed immediately?
- **24/7 response**: Is there around-the-clock incident response?
- **Response SLA**: Documented response time for emergencies?
- **Emergency contact**: Dedicated emergency security contact?

### 43.2 Kill Switch Capability

Can the marketplace disable servers that are already installed:

- **Remote disable**: Can marketplace remotely disable a server?
- **Client integration required**: Does this require client support?
- **Blocklist/denylist**: Is there a blocklist clients can check?
- **Blocklist format**: How is blocklist distributed?
- **Blocklist update frequency**: Real-time or periodic?

### 43.3 Malware Response

When malware is discovered:

- **Detection method**: How is malware detected?
- **Containment**: How fast is it contained?
- **User notification**: How are affected users notified?
- **Remediation guidance**: What should users do?
- **Forensics**: Is there analysis of what the malware did?
- **Disclosure**: Is incident publicly disclosed?

### 43.4 Mass Notification Capability

For widespread issues:

- **Broadcast capability**: Can marketplace contact all users?
- **Targeted notification**: Can notify users of specific servers?
- **Multiple channels**: Email + in-app + other?
- **Notification verification**: How do users verify notification is legitimate?

### 43.5 Incident Communication

During incidents:

- **Status page**: Is there a status page?
- **Status page URL**: Where is it?
- **Incident updates**: How often are updates provided?
- **Post-incident report**: Is postmortem published?

**Evidence to capture**:
- Emergency contact information
- Status page URL
- Past incident responses (if any public)
- Blocklist/kill switch documentation

---

## 44. Audit Trail & Transparency

Logging and transparency of lifecycle events.

### 44.1 Public Audit Trail

What lifecycle events are publicly visible:

- **Version history**: All versions published
- **Publish dates**: When each version was published
- **Removal log**: Record of removed servers
- **Advisory history**: Past security advisories
- **Moderation actions**: Public log of takedowns

### 44.2 Publisher Audit Trail

What publishers can see:

- **Download/install counts**: Over time
- **Version adoption**: How many on each version
- **Geographic distribution**: Where users are
- **Error reports**: Crash/error data

### 44.3 User Audit Trail

What users can see about their activity:

- **Installation history**: What they've installed
- **Update history**: What was updated when
- **Notification history**: What alerts they've received

### 44.4 Transparency Reports

- **Transparency report published**: Regular reports on:
  - Takedown requests
  - Security incidents
  - Malware detected
  - Legal requests
- **Report frequency**: Annual, quarterly, etc.
- **Report URL**: Where published

**Evidence to capture**:
- What history is visible on server pages
- Whether transparency reports exist
- URL to any transparency reports

---

## 45. Communication Channels

Official communication channels for lifecycle events.

### 45.1 Official Channels

Document all official communication channels:

- **Blog**: URL, frequency of security-relevant posts
- **Twitter/X**: Handle, used for security announcements?
- **Mastodon**: Handle
- **Discord**: Server, security announcements channel?
- **Slack**: Workspace
- **Email list**: Security mailing list?
- **RSS feeds**: What feeds are available?
- **GitHub**: Security advisories, discussions

### 45.2 Channel Verification

How users can verify communications are legitimate:

- **Official domain**: All comms from official domain?
- **Signed emails**: GPG signed announcements?
- **Verified accounts**: Social media verified?
- **Canary/warrant canary**: Dead man's switch for legal pressure?

### 45.3 Channel Reliability

- **Response time**: How fast are channels monitored?
- **Redundancy**: Multiple channels for critical info?
- **Archive**: Are past communications archived?

**Evidence to capture**:
- List of all official channels with URLs
- How to subscribe to security notifications
- Verification methods available

---

## 46. Continuous Monitoring

Ongoing monitoring and health checks.

### 46.1 Server Health Monitoring

Does marketplace monitor listed servers:

- **Uptime monitoring**: Are hosted servers monitored?
- **Availability checks**: Are linked repos/URLs checked for liveness?
- **Stale detection**: Are abandoned servers flagged?
- **Link rot detection**: Are dead links identified?

### 46.2 Security Monitoring

- **Vulnerability scanning**: Ongoing scanning of servers?
- **Dependency monitoring**: Watch for vulnerable dependencies?
- **Behavioral monitoring**: Detect anomalous behavior?
- **Reputation monitoring**: Watch for negative reports?

### 46.3 Monitoring Transparency

- **Monitoring disclosed**: Do users know what's monitored?
- **Scan results visible**: Can users see scan results?
- **Health status public**: Is server health visible?
- **Last checked date**: When was server last verified?

**Evidence to capture**:
- What monitoring is disclosed
- Whether health/scan data is visible
- Freshness indicators on listings

---

## 47. User Notification Preferences

User control over notifications.

### 47.1 Notification Settings

What notification preferences can users configure:

- **Security alerts**: Critical vulnerability notifications
- **Update notifications**: New version available
- **Deprecation notices**: Server being phased out
- **Newsletter/marketing**: General updates
- **Per-server settings**: Configure per installed server

### 47.2 Notification Channels

Which channels can users choose:

- **Email**: To registered email
- **In-app**: Notifications in marketplace UI
- **Push**: Mobile/desktop push notifications
- **SMS**: Text messages (for critical alerts)
- **Webhook**: To user's endpoint

### 47.3 Notification Frequency

- **Immediate**: Real-time for critical issues
- **Daily digest**: Aggregated daily
- **Weekly digest**: Aggregated weekly
- **Threshold-based**: Only above certain severity

### 47.4 Required Notifications

Some notifications that cannot be disabled:

- **Critical security**: Users cannot opt out of critical security alerts
- **Legal/compliance**: Required legal notices
- **Account security**: Password reset, 2FA changes

**Evidence to capture**:
- Screenshot of notification preferences
- What notifications are mandatory
- Available channels

---

## Appendix: Comparison with Package Registries

How mature package registries handle these concerns:

### npm

- **Versioning**: Semantic versioning, version history visible
- **Updates**: `npm outdated`, `npm update`
- **Advisories**: `npm audit`, GitHub Advisory Database integration
- **Deprecation**: `npm deprecate` command, shown in CLI
- **Removal**: Unpublish within 72 hours, yank after that
- **Kill switch**: No remote disable, but advisories flag known bad

### PyPI

- **Versioning**: PEP 440, history visible
- **Updates**: `pip list --outdated`
- **Advisories**: OSV database, `pip-audit`
- **Deprecation**: Classifiers for development status
- **Removal**: Yank mechanism (PEP 592)
- **Kill switch**: No remote disable

### Chrome Web Store

- **Versioning**: Version in manifest
- **Updates**: Auto-update by default
- **Advisories**: No public advisory system
- **Deprecation**: Can mark as deprecated
- **Removal**: Google can remove, remotely disable
- **Kill switch**: Yes - can remotely disable malicious extensions

### MCP Marketplaces (Current State)

- **Versioning**: Varies, often poor or none
- **Updates**: Manual, no standard mechanism
- **Advisories**: None standardized
- **Deprecation**: Rare
- **Removal**: Possible but ad-hoc
- **Kill switch**: None known

---

## Appendix: Ideal State for MCP Ecosystem

What a mature MCP marketplace ecosystem should have:

### Minimum Viable Security

1. **Version numbers displayed** for all servers
2. **Security contact** for reporting vulnerabilities
3. **Ability to remove** malicious servers within 24 hours
4. **Email notification** to users of removed servers

### Better

5. **Security advisory system** with severity ratings
6. **Deprecation mechanism** with user notification
7. **RSS/webhook** for security alerts
8. **API flags** for client-side warnings
9. **Rollback capability** for updates

### Best Practice

10. **CVE assignment** for serious vulnerabilities
11. **Coordinated disclosure** process
12. **Blocklist/kill switch** for remote disable
13. **Transparency reports** on security incidents
14. **24/7 emergency response** capability
15. **Automated vulnerability scanning** continuous monitoring
16. **Version immutability** preventing supply chain attacks
17. **Signed packages** for integrity verification

---

## Appendix: Questions to Ask Marketplace Operators

When evaluating or engaging with marketplace operators:

1. How do you handle security vulnerabilities reported in listed servers?
2. How quickly can you remove a malicious server?
3. How do you notify users when a server they've installed has a security issue?
4. Do you have a security advisory system?
5. Can you remotely disable a server that turns out to be malicious?
6. What happens to existing users when a server is removed?
7. Do you monitor listed servers for vulnerabilities on an ongoing basis?
8. How can users subscribe to security notifications?
9. What is your incident response SLA?
10. Have you ever had to remove a malicious server? How did you handle it?

---

## Document History

| Date | Version | Changes |
|------|---------|---------|
| 2025-01-07 | 1.0.0 | Initial lifecycle & notifications checks |
