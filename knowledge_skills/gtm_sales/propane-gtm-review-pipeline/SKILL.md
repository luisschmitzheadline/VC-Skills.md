---
name: review-pipeline
description: Analyze pipeline health — prioritize deals, flag risks, hygiene issues, and produce a weekly action plan. Works standalone with CSV or pasted deals; supercharged when you connect ~~CRM~~ or ~~calendar~~. Trigger with "review my pipeline", "pipeline health check", or use the /review-pipeline command.
---

> If you need to check connected tools (placeholders) or role/company context, see [REFERENCE.md](../../REFERENCE.md).

# Review Pipeline

Assess pipeline health, prioritize deals by impact and closability, flag stale/stuck/single-threaded deals, and output a weekly action plan. This skill works with pipeline data you provide; when ~~CRM~~ is connected, it can pull pipeline automatically and update records.

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                     REVIEW PIPELINE                              │
├─────────────────────────────────────────────────────────────────┤
│  ALWAYS (works standalone)                                       │
│  ✓ Upload CSV from ~~CRM~~ or paste/describe deals                │
│  ✓ Health score: stage progression, activity, close dates, coverage │
│  ✓ Prioritization: rank by close date, size, stage, activity, risk │
│  ✓ Risk flags: stale, stuck, past close date, single-threaded   │
│  ✓ Hygiene audit: missing close date, amount, next step, contact │
│  ✓ Weekly action plan: what to focus on                         │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                       │
│  + ~~CRM~~: Pull pipeline automatically, update records             │
│  + Activity data for engagement scoring                         │
│  + Historical patterns for risk prediction                       │
│  + ~~calendar~~: Upcoming meetings per deal                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Prioritization Framework

| Factor | Weight | What to look for |
|--------|--------|------------------|
| Close date | 30% | Soonest close gets priority |
| Deal size | 25% | Larger deals = more focus |
| Stage | 20% | Later stage = more focus |
| Activity | 15% | Recent activity = healthier |
| Risk | 10% | Lower risk = safer bet |

User can ask for different weighting (e.g. "focus on big deals over soon deals").

---

## Output Structure

- **Pipeline health score:** Dimensions (stage progression, activity recency, close date accuracy, contact coverage) with issue counts.
- **Priority actions this week:** Ranked deals with why, action, impact.
- **Deal prioritization matrix:** Close this week / this month / nurture.
- **Risk flags:** Stale (no activity 14+ days), stuck (same stage 30+ days), past close date, single-threaded.
- **Hygiene issues:** Missing close date, amount, next step, primary contact.
- **Pipeline shape:** By stage, by close month, by deal size.
- **Recommendations:** This week / this month; deals to consider removing.

---

## Data Sources (per REFERENCE.md)

- **~~CRM~~** (if connected): Pipeline, activities, contacts. Enables auto-pull and record updates.
- **~~calendar~~** (if connected): Upcoming meetings per deal.
- If tools are not connected, use only CSV or user-provided pipeline.
