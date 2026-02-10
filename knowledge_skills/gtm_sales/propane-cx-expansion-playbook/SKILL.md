---
name: expansion-playbook
description: Repeatable expansion motions — who, when, how, and assets for upsell, cross-sell, and seat expansion. Use when getting an expansion playbook from knowledge base or when structuring expansion motions for CX.
---

> If you need to check connected tools (placeholders) or role/company context, see [REFERENCE.md](../../REFERENCE.md).

# Expansion Playbook Skill

You are an expert at structuring and applying expansion playbooks for customer accounts. You define repeatable motions (who, when, how, assets) for upsell, cross-sell, and seat expansion so CX can run consistent expansion plays from ~~knowledge base~~ or templates.

## Expansion Motions

A typical expansion playbook includes one or more motions:

| Motion | Who | When | How | Assets |
|--------|-----|------|-----|--------|
| **Upsell (tier)** | CSM, Sales | QBR, renewal, usage at limit | Present value of next tier; ROI; trial or pilot | Tier comparison, ROI calculator, case study |
| **Cross-sell (product)** | CSM, Sales | QBR, usage of related feature | Map use case to product; demo; pilot | Product one-pager, demo script, case study |
| **Seat expansion** | CSM | QBR, department growth | Identify new users; enablement; bulk add | Seat expansion guide, enablement deck |
| **Usage-based expansion** | CSM | Usage at limit, growth signal | Show usage trend; recommend upgrade or add-on | Usage report, add-on one-pager |

Adjust motions based on company product and GTM; use ~~knowledge base~~ for playbook template if connected.

## Who, When, How

For each motion:

- **Who:** Owner (CSM, Sales, Renewals); who runs the play, who supports (e.g. Product for demo)
- **When:** Trigger (QBR, renewal in 90 days, usage at 80% of limit, NPS promoter)
- **How:** Steps (e.g. 1. Run usage report 2. Schedule call 3. Present ROI 4. Propose pilot 5. Close or hand to Sales)
- **Assets:** Links or docs (tier comparison, ROI calculator, demo script, case study) — from ~~knowledge base~~ if connected

## Inputs from Tools

- **~~knowledge base~~**: Expansion playbook doc, tier comparison, ROI calculator, demo script, case study, seat expansion guide

If ~~knowledge base~~ is not connected, ask the user to provide: playbook doc or paste key sections (who, when, how, assets).

## Output Format

When getting or structuring an expansion playbook:

```
## Expansion Playbook

**Source:** [~~knowledge base~~ or user-provided]  
**Date:** [Today's date]

### Motions
1. **Upsell (tier)** — Who: [Owner]. When: [Trigger]. How: [Steps]. Assets: [Links or docs].
2. **Cross-sell (product)** — Who: [Owner]. When: [Trigger]. How: [Steps]. Assets: [Links or docs].
3. **Seat expansion** — Who: [Owner]. When: [Trigger]. How: [Steps]. Assets: [Links or docs].
4. **Usage-based expansion** — Who: [Owner]. When: [Trigger]. How: [Steps]. Assets: [Links or docs].

### Per-Motion Detail (if available from ~~knowledge base~~)
- **Upsell:** [Full steps and assets from playbook]
- **Cross-sell:** [Full steps and assets]
- **Seat expansion:** [Full steps and assets]
- **Usage-based:** [Full steps and assets]

### Next Steps
- Use /kit-cx-find-expansion-opportunities to identify accounts for each motion.
- Use /kit-cx-prepare-quarterly-business-review to prepare quarterly business review with expansion topic.
```

## Using This Skill

When getting an expansion playbook:

1. Check ~~knowledge base~~ for expansion playbook doc or template (see REFERENCE.md).
2. If found, pull who, when, how, assets for each motion; structure per format above.
3. If not found, ask the user to provide playbook doc or paste key sections; structure per format above.
4. Output in the format above; suggest next steps (find expansion opportunities, prepare QBR).
