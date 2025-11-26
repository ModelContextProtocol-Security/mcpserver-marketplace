# AI Usage Guidelines – MCP Marketplace Security Evaluation (v0.2)

**Owner**: Kurt Seifried, Chief Innovation Officer, Cloud Security Alliance
**Last Updated**: 2025-11-25
**Project**: MCP Marketplace Security Evaluation
**Parent Program**: CSA MCP Security
**Folder**: https://drive.google.com/drive/folders/1pGOYZDOOnm93QGe3fGWtLRPP_H3scj-L

---

## The Core Question

> **"How do I ultimately safely get an MCP server?"**

AI assistance helps us answer this question at scale, across all 8 marketplace types.

---

## Purpose

AI systems are now a primary tool for analyzing, evaluating, and understanding complex technical ecosystems.
This project **explicitly supports and encourages AI-assisted and AI-mediated contributions**, including from people who do not write code or who prefer to work conversationally with AI tools.

These guidelines define:  
- How AI tools **may** be used  
- How AI outputs should be **documented**  
- What the **expectations** are for quality, review, and transparency  
- How AI-mediated workflows integrate into working group processes

These guidelines apply to:  
- Marketplace evaluations  
- Documentation  
- Patterns and checks  
- Threat analyses  
- Metadata design  
- Future MCP Client/Server evaluation efforts

---

## Accepted Uses of AI

The following uses of AI **are encouraged**:

### ✔ Conversational analysis  
Participants may explore, question, or critique MCP marketplaces or listings by conversing with AI tools.

### ✔ AI-generated evaluation drafts  
A contributor may ask an AI system to generate an initial MCP marketplace evaluation using the standard template.

### ✔ AI-assisted summaries  
Contributors may request summaries of:  
- Marketplace behavior  
- Documentation  
- Security patterns  
- Risks  
- Checks or criteria  
- Repository structures  
- GTM/UX issues that affect security perception

### ✔ AI-generated insight reports  
A contributor may:  
1. Have a deep conversation with an AI system about a marketplace  
2. Ask the AI to summarize the discussion  
3. Submit the resulting report as a first-class contribution

### ✔ AI-assisted metadata extraction  
AI may be used to extract:  
- Scopes  
- Permissions  
- API behavior  
- Security-relevant metadata  
- Documentation gaps  
- Threat surfaces

### ✔ AI-assisted pattern creation  
AI may be used to draft new checks, policy fragments, documentation structures, or analysis prompts.

---

## Requirements for Using AI Output

### 1. **Disclose AI assistance**
In any evaluation or contribution, include a small header:

```
AI-Assistance: Yes
Tool: [name/model]
Method: [brief, e.g., "Draft generated from conversation with AI"]
```


Transparency builds trust and sets expectations.

---

### 2. **Human review is required**
AI output **must** be sanity-checked before submission:

- Correct obvious hallucinations  
- Remove incorrect technical claims  
- Validate references to specific MCP behavior  
- Ensure analysis reflects reality, not speculation

Human review may be light, but it is mandatory.

---

### 3. **Keep the conversation traceable (optional)**
If feasible, contributors may include:  
- Full transcript  
- Excerpts  
- Prompt history  

This is not required but can improve reproducibility.

---

### 4. **Do not submit raw hallucinated content**
Examples of unacceptable submissions:

- Evaluations of nonexistent marketplaces  
- Fabricated APIs or invented features  
- Security claims unsupported by documentation or behavior

Use AI responsibly and realistically.

---

## Prohibited Uses

### ✘ Using AI to impersonate someone else  
Submissions must be attributed honestly.

### ✘ Inserting AI content that cannot be reviewed  
All contributions must be inspectable by humans.

### ✘ Using AI to generate false trust signals on behalf of a vendor  
Marketplace evaluations must remain neutral.

---

## Practices That Improve Quality

- Provide the AI with the **TEMPLATE-evaluation.md** structure  
- Feed it real documentation, URLs, or code  
- Ask the AI to identify **unknowns, uncertainties, and missing information**  
- Use chain-of-thought *implicitly*, not explicitly (do not reveal raw reasoning traces in public docs)  
- Treat the AI as a structured brainstorming partner, not a source of truth

---

## Long-Term Vision

This AI usage model will extend to:

- **MCP Client Security Evaluation project**  
- **MCP Server Security Evaluation project**  

The goal is to build a **hybrid human–AI working group**, where:

- People contribute insights  
- AI creates structured drafts  
- Humans refine and integrate them  
- CSA governs quality, clarity, and neutrality

AI expands who can participate, not just who can write code.

---

# End of Document

