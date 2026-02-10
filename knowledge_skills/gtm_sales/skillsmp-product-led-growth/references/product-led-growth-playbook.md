# Product-Led Growth (PLG) Playbook

Use this reference only when you need deeper guidance beyond the overview and patterns.

## The PLG vs. Sales-Led Spectrum

Most companies are not pure PLG or pure sales-led. They exist on a spectrum, and the best companies eventually do both.

```
SALES-LED                                                      PRODUCT-LED
    |                                                               |
    v                                                               v
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Pure      │    │   Sales +   │    │   PLG +     │    │   Pure      │
│   Sales     │    │   Product   │    │   Sales     │    │   PLG       │
│             │    │   Assist    │    │   (PLS)     │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘

No free product    Demo/trial        Self-serve +       100% self-serve
Sales closes       before contract   sales for          monetization
all deals                            enterprise
```

**Key insight:** If you're sales-led, you'll be disrupted by competitors who add PLG. If you're PLG-only, you'll leave enterprise revenue on the table. The winning strategy is usually **both**.

---

## The PLG Funnel

The PLG funnel differs fundamentally from sales-led funnels:

```
SALES-LED FUNNEL                    PLG FUNNEL
────────────────                    ──────────

Website Visitor                     Website Visitor
      │                                   │
      ▼                                   ▼
Lead (form fill)                    Free Signup
      │                                   │
      ▼                                   ▼
MQL (marketing                      Activated User
     qualified)                     (hit aha moment)
      │                                   │
      ▼                                   ▼
SQL (sales                          PQA/PQL (usage
     qualified)                          qualified)
      │                                   │
      ▼                                   ▼
Opportunity                    ┌────────┴────────┐
      │                        │                 │
      ▼                        ▼                 ▼
Closed Won               Self-Serve         Sales-Assist
                         Purchase           (Enterprise)
```

**The key difference:** In PLG, qualification comes from **product usage**, not marketing engagement (opening emails, reading whitepapers). Usage is the leading indicator for success.

---

## The Three Conversion Paths

Once users are activated, there are three paths to revenue:

### Path 1: Self-Serve Monetization
User sees value → finds pricing page → enters credit card → pays

**Best for:**
- Contract values under ~$10,000
- Individual or SMB buyers
- Simple pricing

**Ceiling:** Self-serve tops out around $10K. Credit cards get flagged, buyers need approval above that amount.

### Path 2: Product-Qualified Lead (PQL) → Sales
User shows high usage → sales reaches out → closes deal

**Best for:**
- Mid-market and enterprise
- Contract values $15K-$500K+
- Users who need help navigating procurement

### Path 3: Marketing-Qualified Lead (MQL) + Usage → Sales
Marketing finds buyer at target account → connects them to existing usage → sales closes

**Best for:**
- Enterprise accounts where user ≠ buyer
- Accounts with usage but no decision-maker engaged

**Critical insight:** In enterprise, the user is rarely the buyer. You might have amazing usage at a Fortune 500, but zero PQLs because no decision-maker has signed up. Marketing must go find the buyer and connect them to usage.

---

## Product-Led Sales (PLS)

Product-Led Sales is the bridge between PLG and traditional sales. It uses product usage to create and qualify pipeline.

### When PLS Works

PLS makes sense when:
- You want to go **upmarket** (contract values $15K+)
- Self-serve monetization has hit its ceiling
- You have **enterprise-level value** beyond individual use cases

PLS does NOT work when:
- Users are primarily freelancers, contractors, or startups
- Your product solves only individual problems (no team/company value)
- You don't have usage data to qualify accounts

### The PLS Equation

```
Individual Use Case → Team Use Case → Enterprise Value
       (PLG)              (PLG)            (Sales)
```

**Example: Amplitude**
- Individual: "I need data to make better product decisions"
- Team: "Our product team needs shared analytics"
- Enterprise: "We need a data-driven culture across the company"

Sales can tell the enterprise story. Products do a poor job of communicating enterprise value — they show what individuals can do, not what organizations can achieve.

### PQA: Product-Qualified Account

PQA is the threshold of engagement that signals "now is the right time for sales to engage."

**Common PQA signals:**
- **User count:** 7+ users from one company (the magic number)
- **Volume:** High usage of core features (events tracked, boards created, etc.)
- **Velocity:** Sudden increase in user adds or feature usage
- **Behavioral signals:**
  - Admin role changes
  - Terms of use / privacy policy page views
  - Enterprise feature exploration

**How to build your PQA model:**

1. **Start with intuition:** Ask sales what signals excite them about an account
2. **Run regression analysis:** Compare accounts that closed vs. didn't — what usage patterns differ?
3. **Test causation:** Surface accounts that match the pattern but haven't converted — do they close at higher rates?
4. **Iterate with sales:** PQA is not static. Review quarterly with sales feedback.

### Finding the Buyer

The biggest mistake in PLS: assuming you have a buyer when you only have users.

```
PQA + PQL = Direct outreach (user is buyer)
PQA + No PQL = Marketing must find buyer externally
No PQA = Not ready for sales
```

**90% of PLS is converting usage into opportunity by finding a buyer outside the user base.**

---

## Freemium vs. Free Trial

| Freemium | Free Trial |
|----------|------------|
| Free forever with limited features | Full features for limited time |
| ~5% conversion rate | ~10-15% conversion rate |
| Better for: broad reach, viral products | Better for: complex products, shorter sales cycles |
| Risk: cannibalization | Risk: users don't see value in time |

### When to Choose Freemium

- Your product has viral/network effects (users invite users)
- Individual use case is valuable on its own
- You want maximum top-of-funnel reach
- Long time-to-enterprise-value (12+ months)

### When to Choose Free Trial

- Value requires full feature access
- You have a defined proof-of-concept workflow
- Shorter, more urgent buying cycles
- You can drive activation in 14-30 days

### Hybrid Approach

Many companies do both: freemium for individuals, free trial for teams evaluating enterprise.

---

## Activation: The Biggest Lever

Activation is where PLG lives or dies. Most free users never see value.

### The Aha Moment

The aha moment is the first time a user experiences the core value of your product.

**Examples:**
- Facebook: Add 7 friends in 10 days
- GitLab: 2 users use 2 features in 14 days
- Slack: 2,000 messages sent in a workspace

### Finding Your Aha Moment

1. **Brainstorm high-value actions** — What behaviors indicate users "get it"?
2. **Run correlation analysis** — For each action, compare 30-day retention and 90-day conversion rates
3. **Identify lift** — Which actions show highest correlation with retention AND conversion?
4. **Validate with experiments** — Push users toward the action. Does retention actually improve?

**Common aha moment components:**
- Core feature usage (not peripheral features)
- Collaboration/invites (for team products)
- Integration setup (for platform products)
- First successful workflow completion

### Reducing Time to Value

The faster users hit the aha moment, the more convert. Tactics:

**Do > Show > Tell**
- **Do:** Give them a warm start (templates, sample data, pre-configured setup)
- **Show:** Interactive demos, guided tours
- **Tell:** Onboarding emails, tooltips (least effective)

**Remove friction:**
- Minimize sign-up questions (4 screens max)
- Pre-populate with sample data so they can explore immediately
- Identify where users get stuck and build guardrails

---

## Monetization Awareness

**75% of freemium users don't know what you're selling.**

The biggest conversion lever is often not better features — it's making users aware that paid features exist.

### How to Measure

- **Qualitative:** Survey free users: "What features do you think are in our paid plan?"
- **Quantitative:** Track pricing page views per activated account

### How to Improve

1. **Feature walls:** When users hit a paid feature, show what it does and why it's valuable
2. **Usage walls:** "You've used 80% of your free storage. Upgrade for unlimited."
3. **Consistent UI:** Make all upgrade touchpoints visually consistent (e.g., gold color)
4. **Rule of three:** Users need to see upgrade opportunities 3+ times to remember them
5. **Design for every state:** Review paid features from free user's perspective — can they even see they exist?

---

## Building the PLG Team

### Initial Team (MVP)

Start with a **core growth squad:**
- Growth PM (lead) — strong in analytics, experimentation, funnel thinking
- Data Analyst — often the first hire; without data, you're directionless
- 1-2 Engineers (dedicated)
- Designer (can be shared initially)

**Key:** The Growth PM is different from a core PM. Growth PMs think in conversion rates, funnels, and metrics — more like sales/marketing than feature delivery.

### Evolving the Org

As PLG matures, you need cross-functional counterparts:

```
                    ┌─────────────────┐
                    │  Head of Growth │
                    │    (Product)    │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│ Growth        │    │ Growth        │    │ Product-Led   │
│ Marketing     │    │ Product       │    │ Sales         │
│               │    │               │    │               │
│ KPI: Quality  │    │ KPI: Activated│    │ KPI: PQL      │
│ signups       │    │ teams, PQAs   │    │ conversion    │
└───────────────┘    └───────────────┘    └───────────────┘
```

**Critical insight:** Product must own monetization metrics. If PLG lives only in marketing, it will fail within six months.

---

## PLG Timeline Benchmarks

| Metric | Benchmark |
|--------|-----------|
| Time from signup to enterprise contract | 12+ months |
| Freemium to paid conversion rate | ~5% |
| Free trial to paid conversion rate | ~10-15% |
| PQA threshold (users per account) | 7+ |
| Minimum viable self-serve contract | ~$10K max |
| Minimum viable sales-assist contract | ~$15K+ |

**Key insight:** PLG is a long game. You're building pipeline today from signups that happened 12 months ago.

---

## Applying PLG: Checklists

### Before Launching PLG

- [ ] Do we have an individual use case that one person can solve alone?
- [ ] Can users see value in minutes/hours, not days/weeks?
- [ ] Do we have product analytics instrumented?
- [ ] Is leadership committed to 12+ months of investment?
- [ ] Is product (not just marketing) accountable for conversion metrics?

### Designing Freemium/Trial

- [ ] What features belong in free vs. paid?
- [ ] Does the free tier create demand for paid (not satisfy it)?
- [ ] Have we defined our aha moment metric?
- [ ] Is there a clear upgrade path visible to free users?
- [ ] Is pricing simple enough for self-serve purchase?

### Building PQA/PQL Motion

- [ ] What usage signals indicate sales-readiness?
- [ ] Do we have buyer personas in our user base, or must we find them externally?
- [ ] Is sales trained on usage-based selling vs. cold outreach?
- [ ] Do we have feedback loops between sales and product on PQA quality?
- [ ] Are PQA accounts tracked separately from MQLs?

### Diagnosing Low Conversion

- [ ] Is activation the bottleneck? (Users signing up but not engaging)
- [ ] Is monetization awareness the bottleneck? (Users engaged but not aware of paid value)
- [ ] Is the checkout flow the bottleneck? (Users trying to buy but failing)
- [ ] Is pricing the bottleneck? (Users understand value but won't pay that amount)

---

## Common Mistakes Summary

1. **Launching PLG in marketing** — Product must own it
2. **Treating signups as MQLs** — They're not ready for sales
3. **No data foundation** — PLG without analytics is giving away your product for nothing
4. **Freemium that satisfies demand** — Free should create hunger for paid
5. **Expecting quick results** — PLG takes 12+ months to generate pipeline
6. **Ignoring activation** — Most users never see value
7. **Assuming user = buyer** — In enterprise, they rarely are
8. **Static PQA definitions** — Review and iterate quarterly
9. **Not profiling users on signup** — You need to know who they are
10. **Running PLG as an experiment** — It requires committed investment

---

