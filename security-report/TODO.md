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
