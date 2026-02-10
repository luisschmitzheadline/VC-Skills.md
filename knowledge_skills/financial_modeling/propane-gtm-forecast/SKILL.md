---
name: forecast
description: Generate weighted sales forecasts with best/likely/worst scenarios, commit vs. upside breakdown, and gap analysis. Works standalone with CSV or pasted pipeline; supercharged when you connect ~~CRM~~. Trigger with "forecast my pipeline", "weighted forecast for this quarter", or use the /forecast command.
---

> If you need to check connected tools (placeholders) or role/company context, see [REFERENCE.md](../../REFERENCE.md).

# Forecast

Build a weighted sales forecast with stage-based probabilities, commit vs. upside, and gap-to-quota analysis. This skill works with pipeline data you provide; when ~~CRM~~ is connected, it can pull pipeline automatically and use historical win rates.

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                        FORECAST                                  │
├─────────────────────────────────────────────────────────────────┤
│  ALWAYS (works standalone)                                       │
│  ✓ Upload CSV or paste/describe pipeline deals                  │
│  ✓ Set quota and timeline                                       │
│  ✓ Apply stage probabilities (default or custom)                │
│  ✓ Weighted forecast: best / likely / worst case                │
│  ✓ Commit vs. upside breakdown                                  │
│  ✓ Gap analysis and recommendations                             │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                      │
│  + ~~CRM~~: Pull pipeline automatically, real-time data             │
│  + Historical win rates by stage, segment, deal size             │
│  + Activity signals for risk scoring                            │
│  + Track forecast over time                                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## Stage Probabilities (Default)

| Stage | Default Probability |
|-------|---------------------|
| Closed Won | 100% |
| Negotiation / Contract | 80% |
| Proposal / Quote | 60% |
| Evaluation / Demo | 40% |
| Discovery / Qualification | 20% |
| Prospecting / Lead | 10% |

User can override. Map their stage names to these bands when needed.

---

## Output Structure

- **Summary:** Quota, closed to date, open pipeline, weighted forecast, gap, coverage ratio.
- **Forecast scenarios:** Best / likely / worst case with assumptions.
- **Pipeline by stage:** Deal count, total value, probability, weighted value.
- **Commit vs. upside:** High-confidence commit deals; upside deals with risk factors.
- **Risk flags:** Stale close dates, no activity, unrealistic close.
- **Gap analysis:** Amount needed to hit quota; options (accelerate, revive, new pipeline).

---

## Data Sources (per REFERENCE.md)

- **~~CRM~~** (if connected): Pipeline, historical win rates, activity. Enables automatic refresh and tracking.
- If ~~CRM~~ is not connected, use only CSV or user-provided pipeline and quota.
