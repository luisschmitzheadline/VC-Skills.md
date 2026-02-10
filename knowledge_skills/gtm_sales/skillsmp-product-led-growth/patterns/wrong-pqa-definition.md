---
title: PQA Definition Based on Intuition, Not Data
impact: HIGH
tags: pqa, data, sales, qualification
---

## PQA Definition Based on Intuition, Not Data

PQA thresholds should emerge from correlation analysis of what actually predicts conversion — not from what seems logical to the product team.

**Incorrect (guessing at PQA thresholds):**

> **PQA Definition Meeting:**
>
> PM: "Let's say PQA is 10 users and 50 actions per week."
> Sales: "That sounds too high. Make it 3 users."
> PM: "Fine, 3 users and 20 actions."
>
> **Result:**
> - Sales gets flooded with low-intent accounts
> - Close rate on PQAs: 2%
> - Sales stops trusting the product channel
> - "PLG leads are garbage" becomes company lore

**Correct (data-driven PQA development):**

> **PQA Definition Process:**
>
> 1. **Gather intuition:** Ask sales what signals make them excited about an account
> 2. **Run regression:** Compare closed-won vs. closed-lost accounts on usage metrics:
>    - User count
>    - Feature breadth
>    - Usage velocity (change over time)
>    - Behavioral signals (admin changes, ToS views)
> 3. **Find thresholds:** Where do the curves separate? For this product: 7+ users, 3+ features used, usage growing week-over-week
> 4. **Test causation:** Surface accounts that meet criteria but haven't been contacted. Do they close at higher rates?
> 5. **Create feedback loop:** Monthly PQA quality review with sales. Adjust thresholds quarterly.
>
> **Result:**
> - PQA close rate: 15%
> - Sales trusts and prioritizes product-sourced pipeline
> - Model improves over time with feedback

**Why it matters:**

PQA is not a static definition you set once. It's a model that should be continuously refined based on what actually converts. Start simple (users + volume), then add sophistication (velocity, behavioral signals). Always validate with sales that PQAs feel right before scaling.
