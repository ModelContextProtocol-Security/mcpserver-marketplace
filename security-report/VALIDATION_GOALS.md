# MCP Marketplace Evaluation - Validation System Goals

## 1. Primary Goal

To continuously and automatically verify the accuracy, completeness, and objectivity of the MCP marketplace security evaluations, ensuring the data and reports produced by the AI evaluation system are reliable and trustworthy.

## 2. Key Objectives

- **Validate the Discovery Process:** Systematically check if the discovery process is successfully identifying the breadth of the marketplace ecosystem and flag potential gaps or missed sources.
- **Validate Individual Evaluations:** Implement an AI-driven peer review where a second AI agent re-evaluates an initial AI assessment to detect errors, omissions, or misinterpretations.
- **Detect and Measure Bias:** Analyze evaluation outputs and prompts to identify and quantify any systematic bias (e.g., if certain types of marketplaces or languages are consistently scored differently).

## 3. Scope

#### In Scope
- The discovery process and its outputs (`list-of-sources-*.md`).
- The structured data files for marketplaces and clients (`mcp-marketplaces.csv`, `mcp-clients.csv`).
- The detailed markdown evaluation reports generated for each marketplace.
- The prompts and templates used to guide the AI evaluation process.

#### Out of Scope
- The security or performance of the underlying AI models themselves.
- The runtime security of interactions between MCP clients and servers (this is handled by other dedicated projects).
- The triggering logic for when to re-evaluate a marketplace (this will be handled by a separate meta framework).

## 4. Core Principles

- **AI-First, Human-On-the-Loop:** The system is built on AI-driven validation as the default. It produces summaries and analysis that empower human experts to review findings efficiently, rather than performing manual checks on everything.
- **Trust, but Verify:** No single AI's output is accepted without verification. Every evaluation is subject to an automated peer review process.
- **Full Traceability:** All validation actions, discrepancies found, and any subsequent human-driven corrections must be logged to provide a complete and auditable history of an evaluation's lifecycle.

## 5. Success Metrics

- **Correction Rate:** The number of verifiable errors (e.g., factual inaccuracies, missed endpoints) caught and corrected by the AI peer review process per evaluation cycle.
- **Bias Index:** A metric developed to track whether evaluations show a statistical bias towards or against certain marketplace types, languages, or regions. A reduction in this index over time indicates improvement.
- **Coverage Confidence Score:** A metric representing our confidence that we have discovered >90% of the active MCP marketplace ecosystem, to be tracked over time.

## 6. High-Level Methodology

The validation system will function based on the following workflow:

1.  An initial **Evaluation AI** performs the discovery and assessment tasks using the established prompts.
2.  A second **Validation AI** reviews the outputs of the first AI. This includes re-running parts of the evaluation and comparing the results to find discrepancies.
3.  The Validation AI generates a **Validation Report**, which summarizes the findings and highlights any significant differences, errors, or low-confidence assessments.
4.  Initially, **Human Experts** will manually review these Validation Reports to make final judgments and improve the system.
5.  Long-term, this process will be further automated to provide a high-level dashboard for **Human-On-the-Loop** oversight, allowing experts to focus only on the most critical, flagged issues.
