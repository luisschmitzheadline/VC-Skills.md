---
name: gtm-strategy
description: Plan GTM strategy: motion (PLG, SLG, hybrid), segments, channels, capacity. Trigger with "plan GTM strategy", "GTM strategy for [product/segment]", or use the /plan-gtm-strategy command.
---

> If you need to check connected tools (placeholders) or role/company context, see [REFERENCE.md](../../REFERENCE.md).

# GTM Strategy

Plan GTM strategy: motion (PLG, SLG, hybrid), segments, channels, capacity, and key metrics. This skill works with user input and context; when ~~CRM~~ or ~~knowledge base~~ is connected, it can pull pipeline shape, win rates, and existing strategy docs.

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                     GTM STRATEGY                                  │
├─────────────────────────────────────────────────────────────────┤
│  ALWAYS (works standalone)                                       │
│  ✓ Gather: product, segment, current motion, goals               │
│  ✓ Structure: motion, segments, channels, capacity, metrics       │
│  ✓ Output: strategy brief with recommendations                   │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                       │
│  + ~~CRM~~: Pipeline shape, win rates, segment performance          │
│  + ~~knowledge base~~: Existing strategy docs, playbooks, benchmarks │
└─────────────────────────────────────────────────────────────────┘
```

---

## Output Structure

- **Motion:** PLG, SLG, or hybrid; rationale.
- **Segments:** Target segments, criteria, priority.
- **Channels:** Inbound, outbound, partners; allocation.
- **Capacity:** Team size, coverage model, quotas.
- **Metrics:** Key metrics (pipe gen, conversion, CAC, LTV).
- **Recommendations:** Next 90 days, risks, dependencies.

---

## Data Sources (per REFERENCE.md)

- **~~CRM~~** (if connected): Pipeline shape, win rates by segment/channel, capacity data.
- **~~knowledge base~~** (if connected): Strategy docs, playbooks, benchmarks.
- User input: Product, segment, goals, current motion.
