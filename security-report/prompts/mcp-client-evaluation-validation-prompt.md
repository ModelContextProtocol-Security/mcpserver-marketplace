# MCP Client Evaluation - Validation Prompt

**Objective:** To act as a skeptical security auditor and peer-reviewer, validating a pre-existing MCP *client* evaluation report. Your goal is to find inaccuracies, omissions, and biases in the original report.

**Inputs:**
1.  The name of the MCP Client and its primary URL (or app store link).
2.  The full markdown text of the original client evaluation report.

**Process:**

**1. Factual Verification (Documentation-Based)**
- From the original report, select 3-5 key claims (e.g., "sandboxing is partial," "credentials are NOT stored in the OS keychain," "permissions are shown to the user before install").
- For each claim, find the documentation URL, source code link, or other evidence cited in the report.
- Review the cited evidence to verify if it supports the claim. If no evidence is cited, perform a quick search of the client's documentation.
- Document whether the evidence **confirms** or **contradicts** the claim. If it contradicts, explain why.

**2. Gap Analysis (Completeness Check)**
- Review the structure of the official `mcp-client-evaluation.md` template. Did the original report fail to address any key sections (e.g., 'Runtime Security,' 'Transparency,' 'Enterprise Controls')?
- Perform a fresh web search for `"[Client Name]" + "security vulnerability" | "sandbox escape" | "data leak"`. Did the report miss any publicly disclosed security incidents related to its handling of extensions or servers?

**3. Bias and Consistency Analysis**
- Read the executive summary and the detailed findings. Does the summary accurately reflect the data in the report?
- Are there any internal contradictions? (e.g., the report claims "good transparency" but also notes that developer information is not displayed for installed servers).
- Does the final assessment (`Excellent`, `Good`, etc.) seem logical and justified based on the evidence presented?

**4. Output: The Validation Report**
- Generate a "Validation Report" in markdown format that includes the following sections:
    - **Overall Assessment:** Your confidence in the original report's accuracy (e.g., High, Medium, Low).
    - **Summary of Findings:** A brief overview of your conclusions.
    - **Confirmed Findings:** A list of the sampled claims that you successfully verified.
    - **Discrepancies Found:** A table detailing any claims that contradicted the original report (`Claim`, `Original Report's Conclusion`, `Your Conclusion`, `Reason for Difference`).
    - **Gaps Identified:** A list of missed checks or publicly known information that the original report should have included.
    - **Bias & Consistency Notes:** Your assessment of the report's objectivity and internal consistency.
    - **Recommendation:** `Accept Original Report`, `Accept with Minor Corrections`, or `Requires Full Re-evaluation`.
