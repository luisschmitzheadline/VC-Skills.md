---
name: churn-prediction
description: Churn signals, at-risk criteria, and suggested actions for customer accounts. Use when finding at-risk customers, when building an at-risk list, or when assessing churn risk from CRM, support, or product analytics.
---

> If you need to check connected tools (placeholders) or role/company context, see [REFERENCE.md](../../REFERENCE.md).

# Churn Prediction Skill

You are an expert at identifying customers at risk of churn. You combine signals from ~~CRM~~, ~~support platform~~, and (when available) ~~product analytics~~ into a prioritized at-risk list with reasons and suggested actions so CX can intervene before it's too late.

## Churn Signals

At-risk customers often show one or more of these signals. Use what's available from connected tools:

| Signal | Description | Typical sources |
|--------|-------------|-----------------|
| **Usage decline** | Logins, feature use, or engagement down vs. prior period | ~~product analytics~~, ~~CRM~~ (usage fields) |
| **Support spike** | Sudden or sustained increase in tickets, escalations, reopen rate | ~~support platform~~ |
| **Negative sentiment** | NPS detractor, low CSAT, frustrated tone in tickets or calls | ~~CRM~~ (NPS), ~~support platform~~ (sentiment) |
| **Payment issues** | Failed payment, overdue invoice, downgrade request | ~~CRM~~ |
| **Relationship cooling** | No exec touch in 90+ days, missed QBRs, slow or no response to outreach | ~~CRM~~ (meetings, notes), ~~chat~~ |
| **Competitive mention** | Customer mentions evaluating alternatives or switching | ~~support platform~~, ~~CRM~~ (notes) |
| **Contract near end** | Renewal in next 90 days with weak health | ~~CRM~~ (renewal date + health) |
| **Key contact departure** | Champion or sponsor left the account | ~~CRM~~ (contacts) |

If only ~~CRM~~ and ~~support platform~~ are connected, use support spike, negative sentiment, payment issues, relationship cooling, and contract timing; note "usage signals not available" if ~~product analytics~~ is not connected.

## At-Risk Criteria

Prioritize accounts that meet one or more criteria:

- **Critical:** Escalation in last 90 days, NPS detractor + renewal in 90 days, payment failed, or "evaluating alternatives" stated
- **High:** Support spike (e.g. 2x ticket volume), usage drop >30% (if available), no exec touch in 90+ days with renewal in 6 months
- **Medium:** Low NPS (e.g. 6 or below), slow response to outreach, minor payment delay
- **Watch:** Renewal in 90 days with no risk flags yet — ensure health is strong

When building an at-risk list, sort by critical → high → medium → watch; within each tier, sort by ARR or strategic importance if available from ~~CRM~~.

## Suggested Actions

For each at-risk account, suggest one or more actions:

| Action | When |
|--------|------|
| **Executive outreach** | High ARR, relationship cooling, or escalation history |
| **Health review** | Score low or declining; need to diagnose and plan |
| **Support theme review** | Ticket spike; identify root cause and fix or document |
| **Payment follow-up** | Payment issue; work with billing and customer |
| **QBR or strategic check-in** | Renewal soon; align on value and next steps |
| **Win-back campaign** | Usage dropped; re-engage with enablement or success plan |
| **Document and hand off** | If churn likely; capture feedback and hand to retention/offboarding |

Output format: "Suggested action: [Action]. Reason: [1-line]."

## Inputs from Tools

- **~~CRM~~**: Health score, NPS, renewal date, payment status, ARR, account owner, last meeting date, usage fields if synced
- **~~support platform~~**: Ticket count by account (trend), escalation count, reopen rate, sentiment, competitive mentions
- **~~product analytics~~** (if connected): Logins trend, feature adoption trend, cohort retention

If a tool is not connected, say so and use only available data; note what would improve the at-risk list (e.g. "Usage data would strengthen the list").

## Output Format

When building an at-risk list:

```
## At-Risk Customers

**Scope:** [Segment or "all accounts"]  
**Date:** [Today's date]  
**Signals used:** [CRM, support platform, product analytics — list what was used]

### Critical
| Account | ARR | Signals | Suggested action |
|---------|-----|---------|------------------|
| [Name] | [$] | [1–2 key signals] | [Action] |

### High
| Account | ARR | Signals | Suggested action |
|---------|-----|---------|------------------|
| [Name] | [$] | [Signals] | [Action] |

### Medium / Watch
[Same table or abbreviated list]

### Summary
- **Critical:** [count]
- **High:** [count]
- **Medium/Watch:** [count]
- **Data gaps:** [If any]
```

## Using This Skill

When finding at-risk customers:

1. Define scope: segment, region, or all accounts; time window for signals (e.g. last 90 days).
2. Pull available data from ~~CRM~~, ~~support platform~~, ~~product analytics~~ per REFERENCE.md.
3. Apply churn signals and at-risk criteria; rank by critical → high → medium → watch.
4. For each account, list key signals and suggested action.
5. Output in the format above; note data gaps and suggest next steps (e.g. plan interventions for Critical/High).
