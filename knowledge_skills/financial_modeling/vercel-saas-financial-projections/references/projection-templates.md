# SaaS Financial Projection Templates

## Monthly Revenue Projection Model

### Input Variables
```yaml
inputs:
  # Starting Point
  current_mrr: [number]
  current_customers: [number]

  # Growth Drivers
  monthly_new_customers: [number]
  new_customer_arpu: [number]
  cac: [number]

  # Retention
  monthly_churn_rate: [%] # as decimal, e.g., 0.03 = 3%
  expansion_rate: [%] # monthly expansion revenue as % of base

  # Costs
  gross_margin: [%]
  opex_as_percent_revenue: [%]

  # Scenarios
  growth_adjustment_conservative: 0.7
  growth_adjustment_optimistic: 1.4
  churn_adjustment_conservative: 1.3
  churn_adjustment_optimistic: 0.7
```

### Monthly Calculation Loop
```
For each month M (1 to N):

1. Beginning MRR[M] = Ending MRR[M-1]

2. New MRR[M] = new_customers[M] × arpu

3. Expansion MRR[M] = Beginning MRR[M] × expansion_rate

4. Churned MRR[M] = Beginning MRR[M] × churn_rate

5. Net New MRR[M] = New MRR + Expansion MRR - Churned MRR

6. Ending MRR[M] = Beginning MRR[M] + Net New MRR[M]

7. Customers[M] = Customers[M-1] + new_customers - churned_customers
   where: churned_customers = Customers[M-1] × churn_rate

8. Revenue[M] = Ending MRR[M]

9. Gross Profit[M] = Revenue[M] × gross_margin

10. OPEX[M] = Revenue[M] × opex_rate (or fixed amount)

11. EBITDA[M] = Gross Profit[M] - OPEX[M]

12. Cash Flow[M] = EBITDA[M] - CAC × new_customers[M]
```

## Three-Scenario Projections Template

### Spreadsheet Structure
```
| Month | Conservative | Base | Optimistic |
|-------|--------------|------|------------|
| 1     | $X           | $X   | $X         |
| 2     | $X           | $X   | $X         |
| ...   | ...          | ...  | ...        |
| 12    | $X           | $X   | $X         |
| 24    | $X           | $X   | $X         |
| 36    | $X           | $X   | $X         |
| 60    | $X           | $X   | $X         |
```

### Scenario Adjustments
```yaml
conservative:
  new_customers: base × 0.7
  churn_rate: base × 1.3
  expansion_rate: base × 0.8
  cac: base × 1.2

base:
  # Use actual current metrics

optimistic:
  new_customers: base × 1.4
  churn_rate: base × 0.7
  expansion_rate: base × 1.3
  cac: base × 0.85
```

## 5-Year Projection Output Format

### Year Summary Table
```markdown
| Metric | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|--------|--------|--------|--------|--------|--------|
| **Revenue** |||||
| MRR (End) | $X | $X | $X | $X | $X |
| ARR | $X | $X | $X | $X | $X |
| Growth YoY | X% | X% | X% | X% | X% |
| **Customers** |||||
| Total | X | X | X | X | X |
| New | X | X | X | X | X |
| Churned | X | X | X | X | X |
| Net Add | X | X | X | X | X |
| **Unit Economics** |||||
| ARPU | $X | $X | $X | $X | $X |
| LTV | $X | $X | $X | $X | $X |
| CAC | $X | $X | $X | $X | $X |
| LTV:CAC | X:1 | X:1 | X:1 | X:1 | X:1 |
| **Profitability** |||||
| Gross Margin | X% | X% | X% | X% | X% |
| EBITDA | $X | $X | $X | $X | $X |
| EBITDA Margin | X% | X% | X% | X% | X% |
| **Efficiency** |||||
| Rule of 40 | X | X | X | X | X |
| Burn Multiple | X | X | X | X | X |
```

## Cohort-Based Revenue Model

### Cohort Template
```
For each cohort C acquired in month M:

Month 0 (Acquisition):
  Revenue[0] = new_customers × arpu

Month 1:
  Revenue[1] = Revenue[0] × (1 - monthly_churn) × (1 + expansion_rate)

Month N:
  Revenue[N] = Revenue[N-1] × (1 - monthly_churn) × (1 + expansion_rate)

Alternative (NRR-based):
  Revenue[12] = Revenue[0] × NRR (annual)
  Revenue[24] = Revenue[12] × NRR
  ...
```

### Cohort Analysis Table
```
| Cohort | M0 | M3 | M6 | M12 | M18 | M24 | LTV |
|--------|----|----|----|----- |-----|-----|-----|
| Jan 24 | $X | $X | $X | $X  | $X  | $X  | $X  |
| Feb 24 | $X | $X | $X | $X  | $X  | $X  | $X  |
| Mar 24 | $X | $X | $X | $X  | $X  | $X  | $X  |
| ...    |    |    |    |     |     |     |     |
```

## DCF Valuation Template

### Free Cash Flow Projection
```
For each year Y:

Revenue[Y] = ARR[Y]

COGS[Y] = Revenue[Y] × (1 - gross_margin)

Gross Profit[Y] = Revenue[Y] - COGS[Y]

OPEX[Y] = (
  sales_marketing[Y] +
  r_and_d[Y] +
  g_and_a[Y]
)

EBITDA[Y] = Gross Profit[Y] - OPEX[Y]

D&A[Y] = estimated_depreciation

EBIT[Y] = EBITDA[Y] - D&A[Y]

Taxes[Y] = EBIT[Y] × tax_rate (if profitable)

NOPAT[Y] = EBIT[Y] - Taxes[Y]

Free Cash Flow[Y] = NOPAT[Y] + D&A[Y] - CapEx[Y] - Delta_Working_Capital[Y]
```

### DCF Calculation
```
Discount Rate (WACC):
  Early Stage SaaS: 25-35%
  Growth Stage: 20-25%
  Mature: 12-18%

Present Value of FCF:
  PV = Sum of (FCF[Y] / (1 + WACC)^Y) for Y = 1 to N

Terminal Value:
  TV = FCF[N] × (1 + g) / (WACC - g)
  where g = terminal growth rate (typically 2-3%)

Present Value of Terminal:
  PV_TV = TV / (1 + WACC)^N

Enterprise Value:
  EV = PV of FCF + PV of Terminal Value

Equity Value:
  Equity = EV - Net Debt
```

### DCF Sensitivity Table
```
| Terminal Growth | WACC 20% | WACC 25% | WACC 30% |
|-----------------|----------|----------|----------|
| 2% | $X | $X | $X |
| 3% | $X | $X | $X |
| 4% | $X | $X | $X |
```

## Unit Economics Calculator

### LTV Calculation
```
Method 1: Simple LTV
LTV = ARPU × Gross Margin × (1 / Monthly Churn Rate)

Method 2: With Expansion
LTV = ARPU × Gross Margin × (NRR / (1 - NRR + Monthly Churn))

Method 3: Cohort-Based
LTV = Sum of (Monthly Revenue from Cohort × Gross Margin) over lifetime

Example:
ARPU = $50/month
Gross Margin = 75%
Monthly Churn = 3%
LTV = $50 × 0.75 × (1/0.03) = $1,250
```

### CAC Payback
```
CAC Payback (months) = CAC / (ARPU × Gross Margin)

Example:
CAC = $500
ARPU = $50
Gross Margin = 75%
Payback = $500 / ($50 × 0.75) = 13.3 months
```

### Magic Number
```
Magic Number = (ARR[Q] - ARR[Q-1]) / Sales_Marketing_Spend[Q-1]

Example:
Q1 ARR = $1,000,000
Q2 ARR = $1,200,000
Q1 S&M = $150,000
Magic Number = ($1,200,000 - $1,000,000) / $150,000 = 1.33
```

## Exit Valuation Calculator

### Revenue Multiple Method
```
Step 1: Determine Base Multiple
  - Use benchmark for your ARR band and growth rate
  - Typical range: 3-7x for bootstrapped

Step 2: Apply Adjustments
  Multiple = Base × (1 + NRR_adjustment + Growth_adjustment + Margin_adjustment + Rule40_adjustment)

Step 3: Calculate Enterprise Value
  EV = ARR × Adjusted Multiple

Example:
ARR = $2M
Base Multiple = 4x (bootstrapped median)
NRR = 110% → +0.5x adjustment
Growth = 50% → +1x adjustment
Adjusted Multiple = 4 + 0.5 + 1 = 5.5x
EV = $2M × 5.5 = $11M
```

### EBITDA Multiple Method
```
For profitable companies (>$1M EBITDA):

EV = EBITDA × Multiple

Multiple Selection:
  $1-3M EBITDA: 10-15x
  $3-5M EBITDA: 12-18x
  $5-10M EBITDA: 15-20x
  >$10M EBITDA: 18-25x

Example:
EBITDA = $500K
Multiple = 12x (lower end due to size)
EV = $500K × 12 = $6M
```
