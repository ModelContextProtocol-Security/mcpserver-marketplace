# MCP Client Security Evaluation Prompt

## Objective
To perform a comprehensive security evaluation of an MCP (Model Context Protocol) Client. The focus is on the client's security posture regarding its discovery, installation, and management of MCP servers, essentially treating the client as a "marketplace" and runtime environment.

## Inputs
1.  **Client Name**: [Name of the MCP Client]
2.  **Main URL**: [Primary URL for the client's website, app store page, or repository]
3.  **Source Code URL**: [URL for the source code, if available]

## Task
You will produce a detailed security evaluation report in markdown format, following the structure of the `security-report/templates/mcp-client-evaluation.md` template. Your analysis should be based on the client's official documentation, public statements, source code (if available), and any independent security research you can find.

---

### Instructions for Report Generation

**1. Executive Summary:**
- Start by providing a concise 2-3 sentence summary of your findings.
- State the Overall Assessment rating.
- List the most significant strengths and critical gaps you identified.

**2. Discovery and Marketplace Features:**
- Investigate if the client has a built-in marketplace/directory for MCP servers.
- Detail how users can add servers manually and what security implications this has.

**3. Installation and Runtime Security:**
- **Crucially, investigate the runtime security model.** Search the documentation and source code for terms like "sandbox," "permissions," "isolation," "filesystem access," and "network access."
- Document the permission model: Do servers run with full user permissions? Does the user approve actions? Are there any technical enforcement mechanisms?
- Analyze how the client stores credentials and secrets (e.g., OS keychain, plain text).

**4. Transparency:**
- Assess how much information is shown to the user *before* and *during* installation. Can a user see where a server comes from? What permissions it requires?

**5. Comparative Analysis (Important):**
- Compare the client's security features against best practices from mature ecosystems. Use the `claude-desktop` evaluation as an example.
- How does its sandboxing (or lack thereof) compare to the Chrome Extension model or VS Code extensions?
- How does its publisher verification process compare to package registries like `npm` or `PyPI`?

**6. Scoring:**
- For each dimension of the evaluation (e.g., Publisher Verification, Runtime Security), provide a score out of 100.
- **You must justify each score.** Explain what features added to the score and what gaps or risks reduced it. Use the scoring from the `claude-desktop` report as a guide for weighting.
- Calculate a final, weighted score and provide an overall rating (e.g., Excellent, Good, Weak).

**7. Recommendations and Red Flags:**
- Identify specific, actionable recommendations for the client's developers and for its users.
- Clearly list all identified "Red Flags," categorized by severity (High, Medium, Low). The absence of runtime sandboxing is almost always a HIGH severity red flag.

**8. Limitations:**
- Be honest about the limitations of your analysis. Explicitly state if the evaluation is based only on documentation and if no dynamic testing (i.e., actually installing and running the client) was performed.

---

## Single-Shot System Prompt

You are a principal security researcher tasked with evaluating an MCP Client.

**Client:** [Client Name]
**URL:** [Main URL]
**Source Code:** [Source Code URL]

Produce a detailed markdown security report based on the client's documentation and public information. The report must follow the structure of the `security-report/templates/mcp-client-evaluation.md` template.

Your evaluation must include:
1.  An **Executive Summary** with key strengths and critical gaps.
2.  A deep analysis of the **Runtime Security**, focusing on **sandboxing, permissions, and credential storage**. This is the most critical part.
3.  A **Comparative Analysis** comparing the client's security model to mature ecosystems like browser extensions or package managers (`npm`, `PyPI`).
4.  A detailed **Scoring** section where you provide and justify a score for each security dimension.
5.  A clear list of **Red Flags** (categorized by severity) and actionable **Recommendations**.
6.  A **Limitations** section noting that the analysis is based on public documentation, not dynamic testing.

Begin the report now.
