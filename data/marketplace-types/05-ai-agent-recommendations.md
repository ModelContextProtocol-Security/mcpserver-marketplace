---
type_id: 5
name: AI Agent Recommendations
risk_level: highest
examples:
  - Claude recommending MCP servers in conversation
  - ChatGPT suggesting MCP servers
  - GitHub Copilot recommendations
  - Autonomous AI agents installing MCP servers
---

# AI Agent Recommendations

## Definition

AI assistants that recommend and potentially install MCP servers based on user requests. This is the **highest-risk category** because users trust AI judgment implicitly while AI agents may have no security verification capability.

## Characteristics

- Contextual recommendations based on user needs
- Natural language interface
- May install automatically or provide instructions
- Recommendations based on training data
- Limited ability to verify current security status
- May not have access to real-time security information

## Trust Model

- Users trust AI agent to make safe recommendations
- AI agent may lack security evaluation capabilities
- Recommendations may be based on outdated information
- No accountability mechanism for bad recommendations

## Security Opportunities

- Can integrate with security APIs for real-time checks
- Can provide security warnings before installation
- Can require user confirmation for installation
- Can learn from security incidents

## Security Risks

- **HIGHEST RISK CATEGORY**
- AI agent may not evaluate security at all
- Training data may include malicious servers
- No real-time verification of recommendations
- Users assume AI made safe choice
- Automated installation bypasses human review
- No audit trail of recommendation rationale

## Evaluation Priority

**Critical** - Represents future of MCP server discovery/installation, users have highest trust but least transparency, automated installation maximizes risk, no established security framework for AI recommendations.

## Critical Questions

1. What data sources does AI use for recommendations?
2. Does AI check security status before recommending?
3. What warnings does AI provide about security risks?
4. Is user confirmation required for installation?
5. Is recommendation rationale transparent?
6. What happens if AI recommends malicious server?

## Key Insight

In traditional software distribution, there's a clear distinction between "information" and "installation." With AI agents, this boundary dissolves - what humans read as a "review" the AI may interpret as a "recommendation" and act on it immediately.
