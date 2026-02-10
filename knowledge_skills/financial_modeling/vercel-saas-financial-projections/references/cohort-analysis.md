# Cohort Analysis for SaaS Revenue Projections

## Why Cohort Analysis?

Simple projection models assume uniform behavior across all customers. Reality:
- Different acquisition channels have different retention
- Pricing changes affect different cohorts differently
- Product changes impact new vs existing customers differently
- Seasonality affects cohorts differently

**Cohort analysis provides 20-40% more accurate projections than simple models.**

## Cohort Types

### 1. Time-Based Cohorts (Most Common)
Group customers by acquisition month/quarter

```
Cohort: Jan 2025
- All customers who first paid in January 2025
- Track their MRR month by month
- Calculate retention curves
```

### 2. Channel-Based Cohorts
Group by acquisition source

```
Channels:
- Organic Search
- Paid Ads
- Referrals
- Partner
- Direct Sales
```

### 3. Plan-Based Cohorts
Group by initial pricing tier

```
Plans:
- Free-to-Paid Converts
- Basic Plan
- Pro Plan
- Enterprise
```

### 4. ACV-Based Cohorts
Group by initial contract value

```
ACV Bands:
- <$1K/year
- $1K-$5K/year
- $5K-$25K/year
- >$25K/year
```

## Building a Cohort Analysis

### Step 1: Collect Data
Required data points per customer:
- First payment date (cohort assignment)
- Monthly revenue by month
- Churn date (if applicable)
- Plan/tier changes
- Expansion/contraction events

### Step 2: Create Cohort Matrix

```
| Cohort | M0 | M1 | M2 | M3 | M6 | M12 | M18 | M24 |
|--------|-----|-----|-----|-----|-----|------|------|------|
| Jan 24 | 100%| 92% | 87% | 84% | 78% | 68%  | 62%  | 58%  |
| Feb 24 | 100%| 91% | 86% | 82% | 75% | 65%  | 59%  | -    |
| Mar 24 | 100%| 93% | 89% | 86% | 80% | 72%  | -    | -    |
| Apr 24 | 100%| 90% | 85% | 81% | 74% | -    | -    | -    |
| May 24 | 100%| 94% | 91% | 88% | -   | -    | -    | -    |
| Jun 24 | 100%| 92% | 88% | -   | -   | -    | -    | -    |
| Jul 24 | 100%| 91% | -   | -   | -   | -    | -    | -    |
| Aug 24 | 100%| -   | -   | -   | -   | -    | -    | -    |
```

### Step 3: Calculate Retention Curves

```yaml
# Average across cohorts
average_retention:
  M1: 92%
  M3: 84%
  M6: 76%
  M12: 68%
  M24: 58%

# Derived monthly churn
implied_monthly_churn: ~3%

# Derived NRR (if including expansion)
nrr_annual: ~105% (68% × 1.54 expansion factor)
```

### Step 4: Project Future Revenue

For each existing cohort:
```
Future Revenue[M+n] = Current Revenue × (Retention[n] / Retention[current])

Example:
- Jan 24 cohort currently at M12 with $10K MRR
- Retention at M12: 68%
- Retention at M24: 58%
- Projected M24 MRR = $10K × (58% / 68%) = $8,529
```

For new cohorts:
```
New Cohort Revenue[Mn] = Starting MRR × Retention[Mn]

Example:
- New cohort starts with $5K MRR
- Apply retention curve
- M12 projection = $5K × 68% = $3,400
```

## Retention Curve Patterns

### Typical SaaS Retention Curve
```
M0:  100%
M1:  90-95% (initial churn)
M3:  80-88%
M6:  72-82%
M12: 60-75%
M24: 50-65%
M36: 45-60%
```

### Characteristics by Segment

**SMB SaaS:**
- Steep early churn (M1-M3)
- Stabilizes around M6-M12
- 55-70% annual retention

**Mid-Market SaaS:**
- Moderate early churn
- Better stabilization
- 70-85% annual retention

**Enterprise SaaS:**
- Low early churn
- Very stable after M3
- 85-95% annual retention

## Using Cohorts for Projections

### Method 1: Triangulation
```
1. Take oldest cohorts to see full curve
2. Project incomplete cohorts forward
3. Sum all cohort revenues by month
4. Add projected new cohort contributions
```

### Method 2: Rolling Averages
```
1. Calculate average retention at each month across cohorts
2. Apply this curve to all future projections
3. Adjust for observed trends (improving/declining retention)
```

### Method 3: Cohort LTV
```
LTV per Cohort = Sum of all future revenue from cohort
Total Future Revenue = Sum of (Remaining LTV per cohort)
```

## Cohort Health Indicators

### Positive Signals
- Newer cohorts showing better retention
- Expansion revenue increasing over time
- Longer time-to-churn trending up
- LTV:CAC improving by cohort

### Warning Signs
- Newer cohorts churning faster
- Early month churn increasing
- Expansion rates declining
- CAC increasing faster than LTV

## Advanced: Dollar Retention Cohorts

Track MRR instead of customer count:

```
| Cohort | $M0 | $M3 | $M6 | $M12 | NRR |
|--------|------|------|------|-------|------|
| Jan 24 | $10K | $10.5K | $11K | $10.8K | 108% |
| Feb 24 | $12K | $12.8K | $13.5K | $14K | 117% |
| Mar 24 | $8K | $8.2K | $8.8K | $9.2K | 115% |
```

**NRR = MRR at M12 / MRR at M0**

This captures:
- Customer churn (negative)
- Revenue contraction (negative)
- Revenue expansion (positive)
- Price increases (positive)

## Example: Building a Revenue Projection

### Scenario
- Current MRR: $50K
- 5 monthly cohorts
- Adding $10K new MRR per month
- Average retention curve: 95%/M1, 82%/M6, 68%/M12

### Existing Cohorts
```
| Cohort | Current Age | Current MRR | M12 Projection |
|--------|-------------|-------------|----------------|
| M1 (newest) | 1 mo | $10K | $10K × 68% = $6.8K |
| M2 | 2 mo | $9.5K | $9.5K × (68%/90%) = $7.2K |
| M3 | 3 mo | $9K | $9K × (68%/87%) = $7.0K |
| M4 | 4 mo | $8.5K | $8.5K × (68%/84%) = $6.9K |
| M5 (oldest) | 5 mo | $8K | $8K × (68%/82%) = $6.6K |
| **Total** | | **$45K** | **$34.5K** |
```

### New Cohorts (Next 12 Months)
```
| New Cohort | Starting MRR | M12 Projection |
|------------|--------------|----------------|
| Month 6 | $10K | $10K × 68% × (12-6)/12 = $3.4K |
| Month 7 | $10K | $10K × 72% × (12-7)/12 = $3.0K |
| ... | ... | ... |
| Month 12 | $10K | $10K × 95% × (12-12)/12 = $0 |
```

### Total M12 Projection
```
Existing Cohorts at M12: $34.5K
New Cohorts at M12: ~$25K
Total MRR at M12: ~$59.5K
ARR: $714K
```

## Cohort Analysis Tools

### Spreadsheet Setup
```
Columns: Month 0, Month 1, Month 2, ..., Month 36
Rows: Each cohort (by acquisition month)
Values: Either customer count or MRR
```

### Key Formulas (Excel/Sheets)
```
Retention Rate = Value[Mn] / Value[M0]
Churn Rate = 1 - (Value[Mn] / Value[Mn-1])
Average Retention = AVERAGE across cohorts for same month
LTV = SUM of row × ARPU × Gross Margin
```

### Visualization
- Cohort retention curves (line chart)
- Heatmap of retention by cohort/month
- Stacked area chart of revenue by cohort
