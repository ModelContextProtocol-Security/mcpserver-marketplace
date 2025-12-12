# Marketplace Operator Outreach Template

**Purpose**: Template for contacting marketplace operators to verify our evaluation findings.

---

## Email Subject Lines (Options)

- "MCP Marketplace Security Evaluation - Request for Verification"
- "We evaluated [MARKETPLACE_NAME] - please verify our findings"
- "[MARKETPLACE_NAME] included in MCP security research - your input requested"

---

## Email Template

```
Subject: MCP Marketplace Security Evaluation - [MARKETPLACE_NAME]

Hi [NAME/TEAM],

We're conducting a security-focused evaluation of MCP (Model Context Protocol)
marketplaces, registries, and directories as part of an open research project
to help users make informed decisions about where to discover and install MCP
servers.

We've completed an initial evaluation of [MARKETPLACE_NAME] based on publicly
available information, and we want to make sure our findings are accurate before
publishing.

**What we're asking:**
- Please review the attached questionnaire with our findings
- Correct any errors or fill in items marked "Unknown"
- Let us know if we've mischaracterized anything

**What we'll do with your response:**
- Update our evaluation with your corrections
- Note that the operator verified our findings (if you do)
- Give you an opportunity to address any gaps before publication

**Timeline:**
- We'd appreciate a response within [2 weeks / 30 days]
- If we don't hear back, we'll publish based on public information with a note
  that we reached out but didn't receive a response

**About this project:**
- Open source: [REPO_URL]
- Goal: Help users evaluate marketplace security, not rank or shame
- We welcome all corrections and will update our findings accordingly

The attached questionnaire covers:
- Basic identity and classification
- Trust and verification processes
- Privacy and security policies
- Supply chain security (if applicable)
- Technical security posture

Thank you for your time. We believe transparent security evaluation benefits
the entire MCP ecosystem.

Best regards,
[YOUR NAME]
[PROJECT NAME]
[CONTACT INFO]

---

Attached: [MARKETPLACE_NAME]-evaluation-questionnaire.md
```

---

## Follow-Up Template (No Response After 2 Weeks)

```
Subject: Re: MCP Marketplace Security Evaluation - [MARKETPLACE_NAME] (Follow-up)

Hi [NAME/TEAM],

I wanted to follow up on my previous email about our MCP marketplace security
evaluation.

We're planning to publish our findings on [DATE] and wanted to give you another
opportunity to review and correct our evaluation before then.

If we don't hear back, we'll publish based on publicly available information
and note that we attempted to contact you for verification.

You can still provide corrections after publication, and we'll update our
findings accordingly.

Best regards,
[YOUR NAME]
```

---

## Response Handling

### If Operator Responds Positively

1. Thank them for their time
2. Update evaluation with their corrections
3. Mark evaluation as "Operator Verified" with date
4. Ask if they'd like to be credited or remain anonymous

### If Operator Disputes Findings

1. Request specific evidence for disputed items
2. Update findings where evidence supports changes
3. Document the dispute if unresolved
4. Note "Operator disputed [X]" with their stated reason

### If Operator Requests Removal/Non-Publication

1. Explain that we're evaluating publicly available information
2. Offer to note their objections in the evaluation
3. Do not remove unless there's a legitimate reason (e.g., we got the wrong entity)

### If No Response

1. Mark as "Operator contacted [DATE], no response"
2. Publish based on public information
3. Leave door open for future corrections

---

## Outreach Tracking

| Marketplace | Contact Email | Date Sent | Follow-up Sent | Response | Status |
|-------------|---------------|-----------|----------------|----------|--------|
| | | | | | |

---

## Tips for Effective Outreach

1. **Be professional, not adversarial** - We're asking for help, not accusing
2. **Be specific about what we found** - Attach the actual questionnaire
3. **Give reasonable timelines** - 2 weeks is fair, 30 days is generous
4. **Make it easy to respond** - They can just annotate the questionnaire
5. **Acknowledge their work** - Many marketplaces are small teams doing good work
6. **Be transparent about publication** - They should know what we'll do with their response

---

## Finding Contact Information

Priority order for finding the right contact:

1. Security contact (security@, SECURITY.md)
2. Support/contact email on website
3. GitHub org email or maintainer contact
4. Privacy policy contact
5. Domain WHOIS (last resort)
6. Social media DM (if no other option)
