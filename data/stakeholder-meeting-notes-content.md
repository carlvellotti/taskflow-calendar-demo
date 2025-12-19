# Stakeholder Meeting Notes — Calendar Integration

**Date:** November 20, 2024
**Attendees:** Sarah (VP Product), Mike (Engineering Director), Lisa (Head of Security), James (Sales Lead)

---

## Key Decisions

### Must-Have Requirements (from stakeholders)

1. **SSO Integration Required**
   - Lisa: "No new features ship without SSO. Non-negotiable for enterprise customers."
   - Must support SAML and OIDC
   - Need audit logging for all calendar data access

2. **Enterprise Compliance**
   - SOC 2 compliance documentation needed before launch
   - Data residency options for EU customers (GDPR)
   - Lisa: "Calendar data is PII. We need DPA templates ready."

3. **Outlook Support is Critical**
   - James: "70% of our enterprise pipeline uses Outlook. Google-only is a dealbreaker."
   - Must have feature parity between Google and Outlook
   - Mike: "Outlook API is trickier. Budget extra engineering time."

### Timeline

- **Target: Q2 Launch** (April-June)
- Sarah: "We promised the board a calendar integration in our H1 roadmap."
- Phased approach approved:
  - Phase 1 (April): One-way sync, Google Calendar
  - Phase 2 (May): Outlook support
  - Phase 3 (June): Two-way sync, team calendars

### Scope Changes from Original PRD

- ADD: SSO/SAML requirement
- ADD: SOC 2 compliance requirements
- ADD: Outlook support (was "nice to have", now "must have")
- ADD: Audit logging for calendar data access
- REMOVE: Apple Calendar from Phase 1 (move to Phase 4)
- MODIFY: Two-way sync pushed to Phase 3 (was Phase 2)

---

## Open Items

1. **Pricing decision needed**
   - Will calendar sync be free or paid feature?
   - Sarah to discuss with CEO by Nov 30

2. **Engineering capacity**
   - Mike needs to confirm team availability for Q2
   - May need contractor support for Outlook integration

3. **Beta customer list**
   - James to identify 5 enterprise customers for early access
   - Target: 3 Google, 2 Outlook users

---

## Action Items

| Owner | Action | Due |
|-------|--------|-----|
| PM (Carl) | Update PRD with new requirements | Nov 22 |
| Mike | Engineering estimate for SSO work | Nov 25 |
| Lisa | SOC 2 gap analysis | Nov 30 |
| James | Beta customer shortlist | Dec 1 |
| Sarah | Pricing recommendation | Nov 30 |

---

## Quotes to Remember

> "Calendar sync is the #1 requested feature from enterprise prospects. This is a revenue driver." — James

> "Security can't be an afterthought. Build it in from day one." — Lisa

> "I'd rather ship a solid Google integration in April than a buggy multi-platform version." — Mike
