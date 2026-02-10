---
name: sales-playbook
description: Get or structure a sales playbook from ~~knowledge base~~ or context. Repeatable motions (who, when, how, assets) for discovery, demo, negotiation, and closing. Trigger with "get sales playbook", "what's our playbook for [motion]", or use the /get-sales-playbook command.
---

> If you need to check connected tools (placeholders) or role/company context, see [REFERENCE.md](../../REFERENCE.md).

# Sales Playbook

Get or structure a sales playbook with repeatable motions (who, when, how, assets) for discovery, demo, negotiation, and closing. This skill works with ~~knowledge base~~ when connected; otherwise structures a standard playbook from context and notes "Customize with your playbook from ~~knowledge base~~."

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                     SALES PLAYBOOK                                │
├─────────────────────────────────────────────────────────────────┤
│  ALWAYS (works standalone)                                       │
│  ✓ Structure motions: discovery, demo, negotiation, closing      │
│  ✓ Per motion: who (owner), when (trigger), how (steps), assets  │
│  ✓ Output: playbook doc with motions list + per-motion detail    │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                       │
│  + ~~knowledge base~~: Pull existing playbook doc, scripts, battlecards │
│  + ~~CRM~~: Stage-specific playbook steps, win/loss patterns       │
└─────────────────────────────────────────────────────────────────┘
```

---

## Output Structure

- **Motions list:** Discovery, Demo, Negotiation, Closing (or user-specified motions).
- **Per-motion detail:** Who (owner), When (trigger), How (steps), Assets (links or docs).
- **Source:** ~~knowledge base~~ or user-provided. If ~~knowledge base~~ not connected, note "Customize with your playbook from ~~knowledge base~~."

---

## Data Sources (per REFERENCE.md)

- **~~knowledge base~~** (if connected): Sales playbook doc, demo script, battlecards, case studies.
- **~~CRM~~** (if connected): Stage definitions, win/loss patterns (optional).
- User input: Motion type focus, custom motions.
