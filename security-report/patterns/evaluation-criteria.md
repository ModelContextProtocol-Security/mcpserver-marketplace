---
title: MCP Marketplace Evaluation Criteria and Identified Gaps
project: MCP Marketplace Security Evaluation
organization: Cloud Security Alliance - MCP Security Working Group
status: Draft
created: 2025-11-19
updated: 2025-11-19
version: 1.0
tags:
  - mcp-security
  - marketplace-evaluation
  - evaluation-criteria
  - security-gaps
meeting-minutes-source:
  - 2025-10-29 MCP Security Working Group
  - 2025-11-12 MCP Security Working Group
related-documents:
  - GOALS.md
  - PROJECT-SPECIFICATION.md (to be created)
---

# MCP Marketplace Evaluation Criteria and Identified Gaps

## Purpose

This document captures specific, actionable evaluation criteria for assessing MCP marketplaces, along with identified gaps and problems discovered during the working group discussions. These criteria will form the basis for the marketplace security evaluation project.

## Evaluation Criteria

### 1. Transparency and Information Disclosure

#### 1.1 Provenance Information

**Requirement**: Marketplaces should clearly display the source and origin of each MCP server.

**Evaluation Points**:
- Is the author/developer clearly identified?
- Is the source repository or hosting location visible?
- Can users easily determine if this is an official vendor server vs. third-party?
- Is version information provided?

**Examples from Discussion**:
- **Positive**: Claude Desktop used to show a "details" link that showed where connectors came from
- **Negative**: Claude Desktop removed this feature (regression identified in Nov 2025)
- **Negative**: MCP.so and other marketplaces don't prominently show source information

**Scoring Approach**:
- ✅ **Excellent**: Author, source URL, and official/third-party status clearly displayed
- ⚠️ **Partial**: Some information available but requires clicking through or investigation
- ❌ **Poor**: No provenance information readily available

#### 1.2 Logo Usage and Branding

**Requirement**: Vendor logos should only be used for officially sanctioned MCP servers.

**Evaluation Points**:
- Is the official vendor logo being used?
- Has the vendor authorized use of their logo?
- Is there clear indication if this is third-party vs. official?
- Do marketplace policies address logo usage?

**Examples from Discussion**:
- **Problem Identified**: Airtable MCP server in Claude Desktop uses Airtable logo but is developed by "Adam Jones" (domdomegg on GitHub)
- **Deceptive Signal**: PubMed connector using Anthropic logo instead of NIH/PubMed logo
- **User Impact**: "If I'm some junior user who's not looking into that level of detail, I look at that and think that's legit"

**Scoring Approach**:
- ✅ **Excellent**: Clear policy on logo usage; only official servers use vendor logos OR clear "unofficial" labeling
- ⚠️ **Partial**: Logos used but with some disclaimer or attribution
- ❌ **Poor**: Vendor logos used without verification or distinction between official/unofficial

#### 1.3 Developer Information

**Requirement**: Clear identification of who developed/maintains the MCP server.

**Evaluation Points**:
- Is the developer name visible?
- Is there a link to their GitHub/profile?
- For organizations, is the GitHub organization verified?
- Is contact information for the developer available?

**Examples from Discussion**:
- **Good Example**: Showing "Developed by Adam Jones" with link to GitHub
- **Missing**: Many marketplaces don't show developer information at all

**Scoring Approach**:
- ✅ **Excellent**: Developer clearly identified with verified credentials
- ⚠️ **Partial**: Developer name shown but not verified
- ❌ **Poor**: No developer identification

### 2. Vendor Verification

#### 2.1 Domain Validation

**Requirement**: For hosted MCP servers, verify the hosting domain matches the vendor.

**Evaluation Points**:
- Is the server hosted at the vendor's primary domain (e.g., vendor.com/mcp)?
- Is it a clear subdomain (e.g., mcp.vendor.com)?
- Is there verification that the vendor controls this domain?
- Are there warnings for suspicious domains?

**Examples from Discussion**:
- **High Trust**: MCP.Ramp.com (subdomain of main vendor site)
- **High Trust**: Huggingface.co/mcp (path on main vendor site)
- **Suspicious**: microsoft365.mcp.cloud.com (uses cloud.com, not official Microsoft domain)
- **Good Practice**: Vercel.com/mcp (main domain, clear path)

**Scoring Approach**:
- ✅ **Excellent**: Hosted at main vendor domain or verified subdomain
- ⚠️ **Suspicious**: Unusual domain structure or third-party domains
- ❌ **High Risk**: Completely unrelated domain

#### 2.2 GitHub Organization Verification

**Requirement**: For GitHub-hosted MCP servers, verify the organization controls the vendor domain.

**Evaluation Points**:
- Does the GitHub organization have the verified badge?
- Does the verified domain match the expected vendor domain?
- Is the repository in the verified organization (not just a random user account)?

**Examples from Discussion**:
- **Good Example**: github.com/elevenlabs - verified badge linking to elevenlabs.io
- **Good Example**: github.com/cloudsecurityalliance - verified badge linking to cloudsecurityalliance.org
- **Bad Example**: github.com/redhat is actually a random developer, not Red Hat
- **Problem**: "God bless redhat, but they have over 100 organizations scattered all over GitHub"

**Scoring Approach**:
- ✅ **Verified**: Organization has GitHub verified badge for correct domain
- ⚠️ **Unverified**: Organization exists but no verification
- ❌ **Suspicious**: Individual account or organization name doesn't match vendor

#### 2.3 Official Vendor Blessing

**Requirement**: Some mechanism to verify the vendor has approved this MCP server.

**Evaluation Points**:
- Is there documentation linking to this MCP server from vendor's official site?
- Does the vendor's documentation mention this marketplace listing?
- Is there a verification process for "official" designation?
- Is there a clear distinction between official and community servers?

**Examples from Discussion**:
- **Ideal**: Link from vendor's official documentation to their hosted MCP server
- **Problem**: "For all we know, maybe Airtable did bless this guy's MCP server, but we have no way to figure it out"
- **Need**: "If you're the marketplace, I would suggest, if somebody comes to you and says, I am the airtable.com MCP server, well, is that link validated with airtable.com to that GitHub repo"

**Scoring Approach**:
- ✅ **Excellent**: Clear verification process and "official" designation
- ⚠️ **Partial**: Some indication but not systematically verified
- ❌ **Poor**: No distinction between official and third-party servers

### 3. Security Indicators

#### 3.1 HTTPS Requirement

**Requirement**: All remotely hosted MCP servers must use HTTPS.

**Evaluation Points**:
- Is HTTPS enforced for all hosted servers?
- Are HTTP-only servers flagged or rejected?
- Is certificate validity checked?

**Examples from Discussion**:
- **Consensus**: "I would assume nobody's using HTTP... that would obviously be good, guys. If we're telling people to look at the connector URL, then to make damn sure that it better be HTTPS. And if it's not, if it's HTTP, then well, well, come on, it's 2025. You can get a certificate for free, right?"

**Scoring Approach**:
- ✅ **Excellent**: HTTPS required, HTTP rejected
- ⚠️ **Partial**: HTTPS recommended but not enforced
- ❌ **Poor**: HTTP connections allowed

#### 3.2 Connection Testing

**Requirement**: Marketplace should verify listed servers are reachable and responding.

**Evaluation Points**:
- Does the marketplace test that hosted servers are live?
- Are dead links flagged or removed?
- Is there indication of when a server was last verified?

**Examples from Discussion**:
- **Suggestion**: "You could use it to see, is it a secure protocol, but also you could see, does it connect at all? Like, is the link still live?"

**Scoring Approach**:
- ✅ **Excellent**: Active monitoring and verification of server availability
- ⚠️ **Partial**: Some verification but not regular
- ❌ **Poor**: No verification of server functionality

### 4. Feedback and Reporting Mechanisms

#### 4.1 Contact Information

**Requirement**: Marketplace operators should be easily contactable.

**Evaluation Points**:
- Is there a visible contact email?
- Is there a support channel (Discord, forum, etc.)?
- Is response time reasonable?

**Examples from Discussion**:
- **Initially Thought Missing**: MCP.so appeared to have no contact method
- **Actually Present**: MCP.so has support@mcp.so and Discord (found after deeper investigation)
- **Good Example**: MCP-servers.com has "contact at MCP servers"

**Scoring Approach**:
- ✅ **Excellent**: Multiple contact methods prominently displayed
- ⚠️ **Partial**: Contact method exists but hard to find
- ❌ **Poor**: No visible contact information

#### 4.2 Public Issue Tracking

**Requirement**: Issues and problems should be reportable and trackable publicly.

**Evaluation Points**:
- Is there a public issue tracker (GitHub Issues, etc.)?
- Can users report problems with specific MCP servers?
- Are issues addressed in reasonable timeframes?
- Is there transparency about known problems?

**Examples from Discussion**:
- **Found**: MCP.so uses GitHub issues, but "judging by the state of it, they don't close a lot of these. Unless there's 28 open"
- **Benefit**: "If there's a security problem and it gets reported sort of privately... if I find a security issue and I see it's already been reported publicly, especially if it's been reported publicly, like say a month or six months ago, now I have a much better idea of what to do. Maybe take it public or go to the press"

**Scoring Approach**:
- ✅ **Excellent**: Public issue tracker, issues actively managed
- ⚠️ **Partial**: Issue tracker exists but poorly maintained
- ❌ **Poor**: No public reporting mechanism

#### 4.3 Report Button / Flag Content

**Requirement**: Users should be able to flag problematic content directly.

**Evaluation Points**:
- Is there a "report" button on listings?
- Can users flag misleading information or security concerns?
- Is there a process for reviewing reports?

**Examples from Discussion**:
- **Identified Gap**: "The other thing we noticed is, there's like no report button as far as I can tell. Like, there's no way to complain or log a complaint, right?"

**Scoring Approach**:
- ✅ **Excellent**: Easy-to-find report mechanism with clear process
- ⚠️ **Partial**: Reporting possible but not obvious
- ❌ **Poor**: No reporting capability

### 5. Coverage and Completeness

#### 5.1 Hosted MCP Server Coverage

**Requirement**: Marketplaces should list both locally-installed AND remotely-hosted MCP servers.

**Evaluation Points**:
- Does the marketplace include hosted MCP servers?
- Are official vendor-hosted servers prioritized?
- Is there clear indication of hosting model (local vs. remote)?

**Examples from Discussion**:
- **Critical Gap**: "All of the MCP marketplaces that we looked at briefly, none of them, like they only linked to code MCP servers. None of them linked to the hosted MCP servers."
- **Impact**: "They're literally driving people towards third party MCP servers rather than saying like, hey, yeah, like cut and paste this URL from the vendor, boom, done, right?"
- **Specific Examples**:
  - Searching for "Vercel" returns third-party implementations
  - Official Vercel hosted server (mcp.vercel.com) not listed
  - Same problem with multiple vendors

**Scoring Approach**:
- ✅ **Excellent**: Comprehensive coverage including hosted servers, clearly marked
- ⚠️ **Partial**: Some hosted servers listed but incomplete
- ❌ **Poor**: Only lists locally-installed servers, ignoring hosted options

#### 5.2 Official vs. Community Distinction

**Requirement**: Clear labeling of official vendor servers vs. community/third-party alternatives.

**Evaluation Points**:
- Is there a visual indicator for official servers?
- Are community alternatives clearly labeled?
- Can users filter by official/community status?

**Examples from Discussion**:
- **Need Identified**: "Perhaps just having some sort of flag to indicate if it's official"
- **User Confusion**: Multiple Vercel implementations shown, but which is official?
- **Recommendation**: "If you're going to put the official corporate logo on the thing, there needs to be that kind of official corporate blessing, right?"

**Scoring Approach**:
- ✅ **Excellent**: Clear visual distinction, filterable
- ⚠️ **Partial**: Some indication but inconsistent
- ❌ **Poor**: No distinction made

### 6. Marketplace Type-Specific Criteria

#### 6.1 For Informational Marketplaces (MCP.so-style)

**Requirements**:
- Accurate links to source repositories
- Update frequency / staleness indicators
- Spam prevention
- Quality curation

**Evaluation Points**:
- How often is information updated?
- Are dead/broken links removed?
- Is there editorial curation or just automatic aggregation?

#### 6.2 For Code-Hosting Marketplaces (Smithery-style)

**Requirements**:
- Code integrity verification
- Malware scanning
- Supply chain security (2FA for publishers)
- Version control
- Namespace protection

**Evaluation Points**:
- Is uploaded code scanned?
- Are publisher accounts secured (2FA required)?
- Is there protection against typosquatting?
- Are dependencies tracked?

#### 6.3 For Built-in Marketplaces (Claude Desktop, ChatGPT)

**Requirements**:
- Vendor vetting transparency
- Curation criteria disclosure
- User ability to assess trustworthiness
- Stability (no feature regression)

**Evaluation Points**:
- What are the criteria for inclusion?
- Is there documentation of vetting process?
- Do users have enough information to assess trust?

**Regression Example**:
- **Problem**: Claude Desktop removed "details" link that showed connector provenance
- **Impact**: Users can no longer easily verify source of connectors
- **Quote**: "Two weeks ago, I would have said, hey, you know, cloud links to who it is and who built it... Okay, you know, not bad. Well, that's gone. Like they literally took it away at some update in the last two weeks."

#### 6.4 For Enterprise Gateways (Microsoft, Composio)

**Requirements**:
- Centralized management capabilities
- Policy enforcement
- Logging and audit
- Integration with enterprise IAM

**Evaluation Points**:
- Can enterprises enforce approved-only lists?
- Is comprehensive logging available?
- Integration with existing security tools?

## Identified Gaps and Problems

### Gap 1: Missing Hosted Servers in Marketplaces

**Severity**: Critical

**Description**: Informational marketplaces (MCP.so, awesome-mcp-servers, etc.) systematically ignore vendor-hosted MCP servers, only listing GitHub repositories for local installation.

**Impact**:
- Users directed to third-party implementations instead of official hosted servers
- Higher security risk (third-party code vs. vendor-hosted)
- Users miss the gold standard option (vendor-hosted at vendor domain)

**Evidence**:
- None of the major marketplaces reviewed showed hosted servers
- Vercel example: marketplace shows third-party implementations, not mcp.vercel.com
- Ramp example: not listed in marketplaces despite having MCP.ramp.com

**Recommendation**: Blog post highlighting this gap and encouraging marketplaces to list hosted servers

### Gap 2: Logo Misuse and Deceptive Trust Signals

**Severity**: High

**Description**: Vendor logos used on third-party MCP servers without clear indication that they're unofficial, creating false trust signals.

**Impact**:
- Users assume third-party implementations are official
- Vendor reputation at risk
- Users make uninformed trust decisions

**Evidence**:
- Airtable MCP in Claude Desktop: uses Airtable logo, developed by third-party
- PubMed connector: uses Anthropic logo instead of NIH/PubMed logo
- Quote: "If I'm some junior user who's not looking into that level of detail, I look at that and think that's legit"

**Recommendation**: Guidelines for logo usage in marketplaces; require official vendor authorization or clear "unofficial" labeling

### Gap 3: Provenance Information Regression

**Severity**: High

**Description**: Claude Desktop removed the "details" link that previously showed where connectors came from and who developed them.

**Impact**:
- Users cannot verify source of connectors
- Cannot determine if server is official or third-party
- Cannot assess country of origin (important for compliance)
- Organizational policies (e.g., no software from certain countries) cannot be enforced

**Evidence**:
- Feature existed in Claude Desktop as of ~Oct 2025
- Removed in update by ~Nov 12, 2025
- Extensions still have "details" but connectors do not

**Recommendation**: Feedback to Anthropic to restore this feature; documentation of why this matters

**Example User Need**: "Maybe my company's policy says I'm not allowed to use software from companies in a certain country or part of the world. Well, now I have no idea, do I?"

### Gap 4: Lack of Reporting Mechanisms

**Severity**: Medium

**Description**: Many marketplaces lack clear, accessible ways to report problems or security concerns.

**Impact**:
- Security issues may go unreported
- Users cannot flag misleading information
- No accountability mechanism

**Evidence**:
- Initial assessment: MCP.so appeared to have no contact method
- After investigation: found support@mcp.so and Discord, but not prominently displayed
- Many marketplaces have no "report this listing" button

**Recommendation**: All marketplaces should have prominent contact information and public issue tracking

### Gap 5: No Vendor Verification Process

**Severity**: High

**Description**: No standardized way to verify that a listed MCP server is officially sanctioned by the vendor whose logo/name it uses.

**Impact**:
- Impossible to distinguish official from unofficial servers
- Risk of malicious servers impersonating legitimate vendors
- Users cannot make informed trust decisions

**Evidence**:
- Quote: "For all we know, maybe Airtable did bless this guy's MCP server, but like, we have no way to figure it out"
- Multiple implementations of same vendor's MCP with no indication which is official
- No marketplace has verification badges or certification

**Recommendation**:
- Create verified vendor MCP server registry (CSA could maintain)
- Marketplaces could consume this registry
- GitHub organization verification as baseline

### Gap 6: Domain Validation Complexity

**Severity**: Medium

**Description**: Complex domain setups make it difficult to verify official status, especially with subdomains, defensive registrations, and third-party hosting.

**Impact**:
- Even security-savvy users struggle to determine legitimacy
- Average users have no chance of making correct determination
- Attackers could exploit complex domain structures

**Evidence**:
- microsoft365.mcp.cloud.com - is this official?
  - Cloud.ai is main domain
  - But using cloud.com (defensive registration)
  - Actually resolves to ghs.google-hosted.com
  - Quote: "This is exactly what I would do is I would register like cloud.something and target that country or market, you know, with, hey, this is the official one"
- If seen on Stack Overflow: "I would immediately assume that that's an attacker who is domain squatting or something"

**Recommendation**:
- Trust hierarchy: main domain > clear subdomain > complex domain setups
- Guidance on which domain patterns to trust
- Automated domain validation tools

### Gap 7: Third-Party vs. Official Not Distinguished

**Severity**: High

**Description**: Marketplaces do not clearly distinguish between official vendor implementations and third-party community implementations.

**Impact**:
- Users assume all listed servers are equally trustworthy
- Official implementations not given appropriate prominence
- Security-conscious users cannot find official option

**Evidence**:
- Search for vendor returns multiple implementations with no indication which is official
- LinkedIn example: unofficial API scraper shown without clear warning
- No filtering by official/community status

**Recommendation**:
- Visual badges for official vs. community
- Separate sections or filtering
- Priority/ranking for official implementations

### Gap 8: No Shared Verification Registry

**Severity**: Medium

**Description**: Each marketplace must independently verify vendor authenticity, leading to duplication of effort and inconsistent results.

**Impact**:
- Wasted effort across hundreds of marketplaces
- Inconsistent verification quality
- Barrier to entry for new marketplaces

**Evidence**:
- Quote: "I'm going to assume there's somewhere between a hundred and a thousand marketplaces in total. And I don't think it makes sense for those hundred marketplaces to each have to put the effort into validating that the ramp.com is mcp.ramp.com"
- Suggestion: "Why does everybody have to... when there could be like, here's a list of like very high quality vendor certified, vendor created, vendor approved, you know, MCP servers that like everybody tends to want to use"

**Recommendation**:
- CSA-maintained registry of verified vendor MCP servers
- Machine-readable format for marketplace consumption
- Evidence-based verification (links from vendor docs, domain verification)

## Evaluation Methodology

### Approach

1. **Catalog Phase**: Identify all MCP marketplaces (built-in, informational, code-hosting)

2. **Assessment Phase**: Evaluate each marketplace against criteria
   - Use scoring rubric (Excellent / Partial / Poor)
   - Document evidence for each assessment
   - Screenshot or archive examples

3. **Ranking Phase**: Create comparative ranking
   - Weight criteria by importance
   - Calculate overall scores
   - Identify leaders and laggards

4. **Publication Phase**: Publish results with evidence
   - Blog post summarizing findings
   - Detailed report with scoring
   - Recommendations for improvement

### Scoring Weights (Proposed)

**Critical Criteria** (30% each):
- Hosted Server Coverage (Gap 1)
- Logo Usage / Vendor Verification (Gap 2, Gap 5)
- Provenance Information (Gap 3)

**Important Criteria** (10% each):
- Contact/Reporting Mechanisms (Gap 4)
- HTTPS Enforcement
- Official vs. Community Distinction (Gap 7)
- GitHub Verification

**Future Consideration**:
- Domain validation tools
- Temporal monitoring (tracking changes over time)
- Shared registry consumption

## Trust Signals Users Should Look For

Based on the identified criteria, users should prioritize:

### Tier 1: Highest Trust
1. Built into trusted software (e.g., Claude Desktop built-in connectors)
2. Vendor-hosted at main domain (e.g., vendor.com/mcp or mcp.vendor.com)

### Tier 2: High Trust
3. GitHub organization with verified badge matching vendor domain
4. Linked from vendor's official documentation

### Tier 3: Moderate Trust
5. Listed in reputable marketplace with verification process
6. Clear developer attribution with track record

### Tier 4: Low Trust / "Wild West"
7. Third-party implementation without clear provenance
8. Unusual domain structures
9. No vendor relationship evident

## Next Steps

1. **Finalize Criteria**: Review and refine evaluation criteria with working group

2. **Develop Scoring Rubric**: Create detailed point system for each criterion

3. **Build Evaluation Tool**: Consider automation for some criteria (HTTPS checking, domain validation, GitHub verification)

4. **Identify Target Marketplaces**: Create comprehensive list of marketplaces to evaluate

5. **Conduct Pilot Evaluation**: Test criteria on 2-3 marketplaces, refine approach

6. **Full Evaluation**: Systematically assess all major marketplaces

7. **Publish Results**: Blog post, detailed report, recommendations

8. **Build Shared Registry**: Create verified vendor MCP server list as community resource

## References

### Meeting Discussion Highlights

**On HTTPS:**
> "If we're telling people to look at the connector URL, then to make damn sure that it better be HTTPS. And if it's not, if it's HTTP, then well, well, come on, it's 2025. You can get a certificate for free, right?"

**On Logo Usage:**
> "If I'm some junior user who's not looking into that level of detail, I look at that and think that's legit."

**On Missing Hosted Servers:**
> "All of the MCP marketplaces that we looked at briefly, none of them, like they only linked to code MCP servers. None of them linked to the hosted MCP servers."

**On Verification Challenge:**
> "For all we know, maybe Airtable did bless this guy's MCP server, but like, we have no way to figure it out."

**On Shared Registry Value:**
> "I don't think it makes sense for those hundred marketplaces to each have to put the effort into validating... when there could be like, here's a list of like very high quality vendor certified, vendor created, vendor approved... MCP servers"

**On Domain Complexity:**
> "This is exactly what I would do is I would register like cloud.something and target that country or market, you know, with, hey, this is the official one."

**On Provenance Loss:**
> "Two weeks ago, I would have said, hey, you know, cloud links to who it is and who built it... Okay, you know, not bad. Well, that's gone. Like they literally took it away."

---

## Document History

- **2025-11-19**: Initial criteria and gaps document created from meeting minutes analysis
- **Version 1.0**: Comprehensive capture of evaluation criteria and identified problems

## Related Documents

- GOALS.md (project goals and objectives)
- PROJECT-SPECIFICATION.md (to be created)
- PROJECT-PLAN.md (to be created)
- Verified Vendor Registry (to be created)
