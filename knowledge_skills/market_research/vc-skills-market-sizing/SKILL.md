---
name: vc-market-sizing
description: "Bottom-up market sizing (TAM/SAM/SOM) for venture capital analysis. Use when: (1) sizing a startup's market opportunity, (2) calculating TAM/SAM/SOM for an investment memo or due diligence, (3) validating a company's market size claims, (4) comparing bottom-up vs top-down market estimates, (5) building ARPC-based revenue models by customer segment. Produces structured, source-backed market sizing with segment-level ARPC decomposition and top-down sanity check."
---

# VC Market Sizing

Bottom-up market sizing using the ARPC decomposition method, validated by a top-down sanity check. Designed for early-stage VC analysis (Seed through Series B).

## Core Formula

```
Market Size = Customer Count x ARPC x Penetration Rate
```

Where **ARPC** (Annual Revenue Per Customer) is decomposed as:

```
ARPC = Volume Per Customer (annual) x Price Per Unit
```

Customer Count is NEVER part of the ARPC formula. All values in USD, annualized.

## Workflow

### Step 1: Classify the Business Model

Determine the primary revenue model from available evidence (pricing pages, pitch decks, meeting notes). Select the ARPC formula that matches:

| Model | ARPC Formula | Example |
|-------|-------------|---------|
| Subscription | Months x $/month | 12 x $100/mo = $1,200/yr |
| Seat-based | Seats/customer x $/seat/yr | 15 seats x $120/seat = $1,800/yr |
| Transaction | Transactions/yr x $/txn | 1,200 txns x $5 = $6,000/yr |
| Take-rate | GMV/customer/yr x rate | $50K GMV x 3% = $1,500/yr |
| Usage | Units/yr x $/unit | 18,250 API calls x $0.01 = $182/yr |
| Hybrid | Stream 1 ARPC + Stream 2 ARPC + ... | $1,200 sub + $6,000 txn = $7,200/yr |

For monthly pricing, Volume = 12 months (not "1 subscription"). For annual pricing, Volume = 1.

### Step 2: Segment Customers

Create 3-8 **mutually exclusive** customer segments based on industry, company size, use case, or geography.

Rules:
- Classify each segment as **Target** (can use existing product) or **Adjacent** (requires new capabilities)
- Max 20% overlap between any two segments
- Never count service providers AND their clients as separate segments — pick the primary payer
- Each segment may have different revenue streams

### Step 3: Research Data Points

For each segment, research:

| Data Point | Source Priority |
|------------|---------------|
| TAM customer count | Industry reports, government census, trade associations |
| SAM customer count | Subset of TAM within company's current operating markets |
| Volume per customer | Company data, industry benchmarks, competitor metrics |
| Pricing | Company pricing page, competitor pricing, meeting notes |
| SAM penetration | Market research, adoption studies (typically 50-100%) |
| SOM penetration | Competitive analysis, market entry benchmarks (typically 5-15%) |

Never derive customer counts from market size reports (circular logic). Always cite sources.

### Step 4: Calculate ARPC Per Segment

**Single revenue stream:**
```
Segment ARPC = Volume/Customer/Year x Price/Unit
```

**Hybrid (multiple streams):**
```
Stream 1 ARPC = Volume_1 x Price_1
Stream 2 ARPC = Volume_2 x Price_2
Segment ARPC = Stream 1 + Stream 2
```

Validate: Volume units x Price units must cancel to $/year.

### Step 5: Calculate Market Sizes

For each segment:
```
TAM = TAM_Customers x ARPC
SAM = SAM_Customers x ARPC x SAM_Penetration
SOM = SAM_Customers x ARPC x SOM_Penetration
```

Adjacent segments: calculate TAM only (no SAM/SOM in totals).

Sum across all target segments for totals.

### Step 6: Top-Down Sanity Check

Run a parallel top-down estimate:
```
TAM = Industry Revenue x Category Spending Rate
SAM = TAM x Segment Filter x Geographic Filter
```

Compare bottom-up vs top-down. If they differ by more than 3x, investigate:
- Bottom-up ARPC may be unrealistic
- Customer counts may be inflated
- Geographic scope may be misaligned

Report: Overestimate / Adequate / Underestimate with confidence level.

## Output Format

Present results as three tables:

**Table 1: ARPC Breakdown**

| Segment | Type | Revenue Stream | Volume/Cust/Yr | Price | ARPC |
|---------|------|---------------|----------------|-------|------|

**Table 2: Market Size**

| Segment | Type | ARPC | TAM Customers | TAM ($) | SAM Customers | SAM Pen. | SAM ($) | SOM Pen. | SOM ($) |
|---------|------|------|--------------|---------|--------------|----------|---------|----------|---------|

**Table 3: Sources & Assumptions**

| Data Point | Value | Source | Notes |
|-----------|-------|--------|-------|

End with a summary:
```
TAM: $XXM    SAM: $XXM    SOM: $XXM
Top-down check: [Adequate/Overestimate/Underestimate] (confidence: High/Med/Low)
```

## Quality Checklist

Before finalizing, verify:
- [ ] All values in USD, annualized
- [ ] ARPC = Volume x Price (customer count NOT in ARPC)
- [ ] No segment overlap > 20%
- [ ] Customer counts from direct sources (not derived from market size)
- [ ] Each revenue stream calculated separately
- [ ] Adjacent segments have TAM only (no SAM/SOM in totals)
- [ ] Every number has a cited source
- [ ] Top-down sanity check completed

## Example: B2B SaaS Expense Management

**Business model:** Seat-based subscription + transaction fee (hybrid)

**Segments:**
- Target: Mid-market companies (100-1,000 employees) in the US
- Adjacent: Enterprise (1,000+ employees) in the US

**ARPC (Mid-market):**
- Stream 1 (Subscription): 45 seats x $8/seat/mo x 12 = $4,320/yr
- Stream 2 (Transaction fee): 2,400 expense reports/yr x $1.50/report = $3,600/yr
- Total ARPC: $4,320 + $3,600 = **$7,920/yr**

**Market size (Mid-market):**
- TAM: 85,000 companies x $7,920 = $673M
- SAM: 42,000 companies x $7,920 x 80% = $266M
- SOM: 42,000 companies x $7,920 x 8% = $27M

**Top-down check:** US expense management software market ~$3.2B (Gartner 2025). Mid-market = ~25% = $800M. Bottom-up TAM of $673M is within range. **Adequate** (High confidence).
