---
name: roi-calculator
description: Build an ROI calculator or value model for deals. Inputs: cost savings, efficiency gains, revenue impact. Output: ROI %, payback period, value summary. Trigger with "create ROI calculator for [deal/segment]", "value model for [product]", or use the /create-roi-calculator command.
---

> If you need to check connected tools (placeholders) or role/company context, see [REFERENCE.md](../../REFERENCE.md).

# ROI Calculator

Build an ROI calculator or value model for a deal or segment. Inputs: cost savings, efficiency gains, revenue impact (user or ~~CRM~~). Output: ROI %, payback period, value summary. Use for proposals and business case conversations.

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                     ROI CALCULATOR                                │
├─────────────────────────────────────────────────────────────────┤
│  ALWAYS (works standalone)                                       │
│  ✓ Gather: deal/segment, cost drivers, efficiency/revenue levers │
│  ✓ Model: savings + gains + revenue impact vs. investment         │
│  ✓ Output: ROI %, payback period, value summary table             │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                       │
│  + ~~CRM~~: Deal context, segment, existing value props            │
│  + ~~knowledge base~~: ROI templates, value frameworks, case studies │
└─────────────────────────────────────────────────────────────────┘
```

---

## Output Structure

- **Assumptions:** Cost drivers, efficiency gains, revenue impact, investment.
- **Results:** ROI %, payback period (months), total value (Year 1, Year 3).
- **Value summary table:** Category, Annual value, Notes.
- **Talking points:** How to present the ROI in a call or proposal.

---

## Data Sources (per REFERENCE.md)

- **~~CRM~~** (if connected): Deal context, segment, industry, existing value props.
- **~~knowledge base~~** (if connected): ROI templates, value frameworks, case studies.
- User input: Deal/segment, cost drivers, efficiency/revenue levers, investment.
