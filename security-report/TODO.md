# Project TODO and Long-Term Goals

This document tracks the strategic improvements and long-term goals for the MCP Marketplace Security Evaluation project.

## 1. Discovery Process Formalization

The goal is to create a fully automated, repeatable, and comprehensive discovery process.

- **[ ] Implement Scheduled Discovery:** Create a script or automated workflow (e.g., GitHub Action) to run the discovery process on a weekly or monthly basis.
- **[ ] Define and Automate Multi-Path Discovery:** The discovery process should ingest data from multiple paths:
    - **[ ] New Client Analysis:** When a new MCP client is discovered, automatically analyze it to identify which marketplaces it queries or recommends.
    - **[ ] Web Search:** Periodically run automated web searches for new marketplaces using the keywords defined in the discovery prompt.
    - **[ ] GitHub Search:** Continuously search GitHub for new projects that match marketplace criteria.
    - **[ ] Social/Community Monitoring:** Monitor specific communities like Reddit's `r/mcp` for mentions of new marketplaces.

## 2. Validation System Development (AI -> AI -> Human)

The core of our quality control will be an AI-driven validation system with a Human-On-the-Loop (HOTL) model.

- **[ ] Define Validation Goals:** Generate a formal `VALIDATION_GOALS.md` document outlining the specific objectives, scope, and success metrics for the validation system.
- **[ ] Implement AI Peer Review:** Design and build the process where one AI agent's evaluation is reviewed by a second, independent AI agent. This second agent's goal is to find errors, biases, and omissions in the first agent's work.
- **[ ] Develop Exception-Based Reporting for HOTL:** Create the mechanism to summarize the AI-vs-AI review process. This summary should only flag significant discrepancies, critical red flags, or low-confidence findings for human review, rather than requiring humans to review everything.

## 3. "Negative Space" Security Analysis

To understand what marketplaces are *not* listing, we will implement a control list.

- **[ ] Create and Maintain a Control List:** Develop a list of "control" MCP servers. This list should include:
    - Known high-quality, official vendor servers.
    - Known buggy or outdated servers.
    - Known malicious (but inert) or intentionally insecure servers.
    - Known typosquats of popular servers.
- **[ ] Implement Control List Auditing:** Create a process to periodically check marketplaces against this control list to measure their curation effectiveness and speed of moderation.

## 4. Advanced Evaluation Templates

As the project matures, we will need more specialized evaluation tools.

- **[ ] Develop Template for Unstructured Marketplaces:** Design a new evaluation template specifically for "Community Forums" and "AI Agent Recommendations." This will involve identifying new, relevant security signals for these less-structured environments (e.g., user reputation, voting patterns, scammer detection, resistance to prompt injection for AI agents).

## 5. Supply Chain Security Deep Analysis

Extend security evaluation to cover end-to-end supply chain risks beyond surface-level marketplace checks.

- **[ ] Build Pipeline Security Analysis:** Investigate how each marketplace handles builds/packaging. Key questions:
    - Is there build isolation between publishers? (June 2025 Smithery vuln was cross-build access)
    - What build configurations are accepted? (dockerBuildPath, custom scripts, etc.)
    - Can builds access secrets from other publishers?
    - Are build logs exposed or protected?
- **[ ] Dependency Chain Analysis:** Track transitive dependencies in MCP servers.
    - What npm/pip packages do popular servers depend on?
    - Are there common high-risk dependencies across many servers?
    - Can we detect dependency confusion attacks?
- **[ ] Scaffolding Tool Security:** Evaluate `npx create-*` and similar scaffolding tools offered by marketplaces.
    - What do they download/execute during scaffolding?
    - Are scaffolding packages verified?
    - Could a malicious scaffolding tool compromise new developers?

## 6. Submission/Onboarding Process Testing

Actually submit MCP servers to each marketplace to experience and document their onboarding process.

- **[ ] Create Test MCP Servers:** Build simple, legitimate MCP servers for testing submission processes. Consider:
    - A security-scanning MCP server (useful product + tests submission)
    - A "marketplace picker" MCP server that helps users choose marketplaces
    - A deliberately minimal/placeholder server to test rejection criteria
- **[ ] Document Submission Flow Per Marketplace:** For each major marketplace:
    - **[ ] Claude Desktop:** Document their form-based submission process, review timeline, rejection criteria
    - **[ ] Smithery:** Document GitHub OAuth flow, publishing process, verification requirements
    - **[ ] mcp.run:** Document submission and review process
    - **[ ] mcp.so:** Document how servers get listed (if curated vs automated)
    - **[ ] Others as discovered
- **[ ] Track Review Timelines:** Record how long each marketplace takes to review submissions.
- **[ ] Test Rejection Criteria:** Attempt to understand what gets rejected by submitting edge cases:
    - Servers with no description
    - Servers with minimal functionality
    - Servers with aggressive permission requests
    - Near-typosquats of popular servers (ethical testing only)
- **[ ] Document Appeal Processes:** If rejected, document whether and how to appeal.

## 7. Marketplace Comparison Tooling

Build tools to help users compare and choose marketplaces.

- **[ ] MCP Server to Help Pick Marketplaces:** Build an MCP server that:
    - Queries multiple marketplaces for a given search term
    - Compares results across marketplaces
    - Shows which marketplace has more servers for a category
    - Highlights trust/verification differences
- **[ ] Marketplace Security Scorecard:** Create a standardized scorecard format for comparing marketplaces:
    - Security score (based on evaluation)
    - Server count
    - Review process (manual vs automated)
    - Verification badges (and their meaning)
    - Incident history
    - Data collection practices

## 8. Ongoing Evaluation Maintenance

Keep evaluations current as marketplaces evolve.

- **[ ] Quarterly Re-evaluation:** Schedule re-evaluation of major marketplaces quarterly to catch:
    - New security features
    - Policy changes
    - Security incidents
    - Growth/decline in server count
- **[ ] Monitor Security Incidents:** Set up alerts for:
    - CVEs mentioning MCP
    - GitGuardian/security blog posts about MCP
    - Security-related GitHub issues in marketplace repos
- **[ ] Track Marketplace Response to Research:** Document how marketplaces respond to:
    - Our published evaluations
    - Security research from others
    - Feature requests for security improvements

## 9. Advanced Analysis and Tooling

To move beyond documentation-based reviews and validate security claims with practical evidence.

- **[ ] Implement Practical Dynamic Analysis (The Dynamic Analysis Gap):** Acknowledge that documentation review is insufficient for complete security validation. Develop a methodology to install and run MCP clients and servers in an isolated (sandboxed) environment to observe actual runtime behavior. This is critical for verifying:
    - Filesystem access (what files are read/written?)
    - Network activity (what domains are contacted?)
    - Enforcement of claimed security controls (do permission prompts actually block actions?)
    - Secure storage of secrets.

- **[ ] Develop Standardized Security Test Tooling (The Tooling Gap):** Build a suite of tools to support dynamic analysis. This tooling is a foundational capability needed for the marketplace, client, and server security projects.
    - **[ ] Create a "Malicious-but-Harmless" Test MCP Server:** A server designed to probe the security boundaries of a client. It would attempt actions like:
        - Reading sensitive files (`~/.ssh/id_rsa`).
        - Writing files outside of an expected directory.
        - Making unauthorized network calls.
        - Testing for prompt fatigue or bypass vulnerabilities.
    - **[ ] Develop Client/Server Interaction Loggers:** Tools to intercept and log the traffic between a client and a server to analyze the protocol usage and data being exchanged.