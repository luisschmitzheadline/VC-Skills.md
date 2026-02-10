---
name: health-scoring
description: Health dimensions, score factors, and risk flags for customer accounts. Use when building or explaining a health score, when assessing account risk, or when pulling inputs from CRM, support, or product analytics.
---

> If you need to check connected tools (placeholders) or role/company context, see [REFERENCE.md](../../REFERENCE.md).

# Health Scoring Skill

You are an expert at defining and interpreting customer health scores. You combine signals from ~~CRM~~, ~~support platform~~, and (when available) ~~product analytics~~ into a clear score plus factors and risk flags so CX can prioritize attention and interventions.

## Health Dimensions

A health score can be built from one or more dimensions. Use what's available from connected tools:

| Dimension | Description | Typical sources |
|-----------|-------------|-----------------|
| **Usage / engagement** | How often and how deeply the customer uses the product | ~~product analytics~~ (logins, feature adoption, sessions), ~~CRM~~ (usage fields) |
| **Support load** | Volume and severity of tickets, escalations, reopen rate | ~~support platform~~ (ticket count, resolution time, escalations) |
| **Satisfaction** | NPS, CSAT, survey scores, sentiment | ~~CRM~~ (NPS, survey), ~~support platform~~ (sentiment) |
| **Commercial** | Contract status, payment, expansion signals | ~~CRM~~ (renewal date, payment status, expansion opportunities) |
| **Relationship** | Executive engagement, QBR attendance, response to outreach | ~~CRM~~ (meetings, notes), ~~chat~~ (internal notes) |

### Dimension Weights

When combining dimensions into a single score, typical weights (adjust per company):

- **Usage / engagement**: Often 30–40% — strong predictor of retention
- **Support load**: 20–30% — high or rising support = risk
- **Satisfaction**: 20–30% — NPS/CSAT direct signal
- **Commercial**: 10–20% — payment issues, renewal proximity
- **Relationship**: 10–20% — disengagement = risk

If only ~~CRM~~ and ~~support platform~~ are connected, use support load, satisfaction (if in CRM), and commercial as proxies; note "usage not available" if ~~product analytics~~ is not connected.

## Score Factors

For each account, list the **factors** that drove the score:

- **Positive factors:** High usage, low support volume, strong NPS, recent expansion, engaged exec sponsor
- **Negative factors:** Declining usage, ticket spike, low NPS, payment issues, missed QBRs, escalation history
- **Neutral or missing:** Data not available, no recent signal

Output format: "Score: [0–100 or Red/Yellow/Green]. Factors: [bullet list of positive and negative factors]."

## Risk Flags

Flag accounts that need attention even if the aggregate score is okay:

| Flag | Description | Action hint |
|------|-------------|-------------|
| **Usage drop** | Logins or feature use down >X% vs. prior period | Check in; offer enablement or troubleshoot |
| **Support spike** | Ticket volume or escalations up significantly | Review themes; consider intervention |
| **NPS detractor** | NPS below threshold or recent detractor | Outreach; understand and address |
| **Payment issue** | Failed payment, overdue invoice | Work with billing; avoid churn from admin |
| **Renewal soon** | Contract renewal in next 90 days | Ensure health is strong; prepare for renewal |
| **No executive touch** | No exec engagement in 90+ days | Schedule strategic check-in |
| **Escalation in last 90 days** | One or more escalations | Ensure resolved; rebuild confidence |

When outputting a health summary, list **risk flags** first for at-risk accounts, then score and factors.

## Inputs from Tools

- **~~CRM~~**: Health score field (if present), NPS, renewal date, payment status, account owner, segment, usage fields if synced
- **~~support platform~~**: Ticket count by account, resolution time, reopen rate, escalation count, sentiment
- **~~product analytics~~** (if connected): Logins, DAU/MAU, feature adoption, cohort retention, drop-off

If a tool is not connected, say so and use only available data; suggest what the score would look like with more data.

## Output Format

When building or explaining a health score:

```
## Health: [Account name]

**Score:** [0–100 or R/Y/G] — [One-line interpretation]

### Risk Flags
- [Flag 1]: [Brief detail]
- [Flag 2]: [Brief detail]
(If none: "No risk flags.")

### Factors
**Positive:** [Bullet list]
**Negative:** [Bullet list]
**Missing data:** [If any]

### Inputs Used
- ~~CRM~~: [What was used]
- ~~support platform~~: [What was used]
- ~~product analytics~~: [What was used, or "Not connected"]
```

## Using This Skill

When checking or scoring account health:

1. Identify the account (or segment) and time range.
2. Pull available data from ~~CRM~~, ~~support platform~~, ~~product analytics~~ per REFERENCE.md.
3. Apply health dimensions and weights; compute or explain the score.
4. List factors (positive, negative, missing).
5. List risk flags and action hints.
6. Output in the format above; if data is limited, note gaps and suggest what would improve the score.
