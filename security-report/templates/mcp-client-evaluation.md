# MCP Client Evaluation Template

Copy this template to evaluate an MCP client's marketplace behavior.

**Note**: This evaluates the client's role in MCP server discovery/installation, not general client security.

---

## Client Information

**Name**: [Client name]
**URL**: [Primary URL]
**Vendor**: [Who makes it]
**Type**: [desktop / ide / web / cli / framework]
**Evaluation Date**: [YYYY-MM-DD]
**Evaluator**: [Your name/handle]

---

## Executive Summary

[2-3 sentence summary of findings]

**Overall Assessment**: [Excellent / Good / Adequate / Weak / Failing]

**Key Strengths**:
-

**Key Gaps**:
-

---

## 1. Discovery and Marketplace Features

### 1.1 Built-in Marketplace
- Does the client have a built-in marketplace/directory?
- What is it called? (Extensions, Connectors, etc.)
- How many servers are available?
- How is the marketplace curated?

**Has Built-in Marketplace**: [Yes / No]
**Details**:

### 1.2 Manual Configuration
- Can users add MCP servers manually?
- What is the configuration method? (JSON file, GUI, CLI)
- What information is required?

**Allows Manual Config**: [Yes / No]
**Method**:
**Details**:

---

## 2. Installation Process

### 2.1 Installation Method
- How are servers installed? (one-click, config edit, etc.)
- What friction exists in the installation process?
- Are there security warnings during installation?

**Details**:

### 2.2 Verification
- Does the client verify server authenticity?
- Are signatures checked?
- Is the source validated?

**Assessment**: [Excellent / Partial / None]
**Details**:

---

## 3. Runtime Security

### 3.1 Sandboxing
- Are MCP servers sandboxed?
- Is there filesystem isolation?
- Is there network isolation?

**Has Sandboxing**: [Yes / No / Partial]
**Details**:

### 3.2 Permission Model
- What permissions do MCP servers get?
- Is there a capability-based system?
- Does user approve permissions?

**Permission Model**: [full-user / capability-based / user-approval / other]
**Details**:

### 3.3 Credential Storage
- How are API keys and credentials stored?
- Is there secure storage (OS keychain, etc.)?

**Details**:

---

## 4. Transparency

### 4.1 Provenance Display
- Can users see where servers come from?
- Is developer information shown?
- Can users distinguish official vs. third-party?

**Assessment**: [Excellent / Partial / Poor]
**Details**:

### 4.2 Permission Display
- Are required permissions shown before install?
- Can users see what servers can access?

**Assessment**: [Excellent / Partial / Poor]
**Details**:

---

## 5. Updates and Maintenance

### 5.1 Update Mechanism
- How are MCP servers updated?
- Are updates automatic or manual?
- Are updates verified/signed?

**Details**:

### 5.2 Removal
- Can users easily remove MCP servers?
- Is there a way to disable without removing?

**Details**:

---

## 6. Enterprise Controls

- Are there admin/policy controls?
- Can enterprises enforce allowlists?
- Is there centralized management?

**Has Enterprise Controls**: [Yes / No / Unknown]
**Details**:

---

## Red Flags Identified

### High Severity
-

### Medium Severity
-

### Low Severity
-

---

## Recommendations

### For Client Developer
1.

### For Users
1.

### For Enterprises
1.

---

## Critical Questions (from framework)

1. What verification does client perform on MCP servers?
2. Where do MCP servers come from?
3. Is automated security scanning performed?
4. What security guarantees does vendor make?
5. Is runtime sandboxing enforced?
6. Are permissions reviewed/approved by user?
7. How quickly are malicious servers removed?
8. Is vendor's security process transparent?
9. Is there an incident response process?
10. Can users report malicious servers easily?

**Score**: [X/10 clear Yes]

---

## Evidence Collected

- [ ] Installation tested
- [ ] Documentation reviewed
- [ ] Configuration examined
- [ ] Runtime behavior observed

**Limitations**:

---

## Document Metadata

**Evaluation Completed**: [YYYY-MM-DD]
**Time Invested**:
**Confidence Level**: [High / Medium / Low]
**Next Review**: [When should this be re-evaluated?]
