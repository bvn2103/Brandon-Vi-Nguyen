# Marginal-analysis specification

capability: marginal-analysis
created: 2026-09-04

Purpose

This specification defines the labor function, search domain, objective, and hand-checks for the "perfect-competition" marginal-analysis. Commit this file before adding the workbook so arithmetic and the search design are reviewable in the repository history.

Labor function (discrete, compounding escalation)

For crop c, with base_hours_per_week_c and escalation rate e_c (expressed as a decimal), and a season length of W = 36 weeks, the total labor required to plant q beds of crop c is:

Labor_c(q) = base_hours_per_week_c × W × q × (1 + e_c)^q

Discrete marginal labor for the q-th bed (the incremental hours required when going from q-1 to q beds) is computed as:

MarginalLabor_c(q) = Labor_c(q) - Labor_c(q-1)

Use the discrete difference above when computing marginal cost and when deciding whether the q-th bed is profitable.

Parameters (from the brief)

- Season length W = 36 weeks
- Farmer hours available H_f = 720 hours (valued at $34.72/hr)
- Temporary labor pool H_t_pool = 4 × 1,440 hours = 5,760 hours (paid at $17.36/hr)
- Combined available hours H_total = H_f + H_t_pool = 6,480 hours
- Fixed costs F = $20,000 (sunk for allocation decisions)

Crop base parameters

Tomatoes:
- base_hours_per_week = 2.50
- base_hours_per_season per bed = 2.50 × 36 = 90
- escalation e = 0.10
- revenue per bed = $8,800
- fertilizer per bed = $880
- max beds = 20

Mesclun:
- base_hours_per_week = 1.25
- base_hours_per_season per bed = 1.25 × 36 = 45
- escalation e = 0.0125
- revenue per bed = $2,700
- fertilizer per bed = $880
- max beds = 30

Carrots:
- base_hours_per_week = 0.833
- base_hours_per_season per bed ≈ 0.833 × 36 ≈ 29.988 ≈ 30 (use precise multiplier in code)
- escalation e = 0.025
- revenue per bed = $2,094
- fertilizer per bed = $440
- max beds = 20

Objective and accounting choices

- For allocation decisions compare marginal revenue to marginal cost (where marginal cost converts marginal labor into dollars using the marginal mix of farmer/time and temporary labor used).
- Account for farmer hours as an opportunity cost at $34.72/hr even if not paid out of pocket; temporary labor is paid at $17.36/hr. In profit calculations, include both farmer opportunity cost and temporary labor costs.
- Total profit = total_revenue - total_input_costs (fertilizer) - labor_costs (farmer_value_hours × $34.72 + temp_hours_paid × $17.36) - fixed_costs.
- When computing marginal cost dollars for the q-th bed, use MarginalLabor_c(q) apportioned first against remaining farmer hours (valued at $34.72) and then against temporary hours (paid at $17.36).

Search domain

Enumerate integer allocations (T, M, C) with:
- 0 ≤ T ≤ 20
- 0 ≤ M ≤ 30
- 0 ≤ C ≤ 20
- T + M + C ≤ 64 (cannot plant more beds than available)

Hand-checks (arithmetic asserts to include in the spec and run before committing analysis results)

- One tomato bed (q = 1): Labor = 90 × 1 × 1.1^1 = 99.0 hours exactly.
- Ten tomato beds (q = 10): Labor = 90 × 10 × 1.1^10 ≈ 2,334.37 hours.
- Twenty tomato beds (q = 20): Labor ≈ 90 × 20 × 1.1^20 ≈ 12,110 hours (sanity check against prior miscalculation).

Tolerances

- Numeric comparisons should use a tolerance of 1e-6 for floating-point equality when validating hand-checks.

Versioning and commit order

- This spec must be committed before the analysis workbook or scripts that produce results. The repository history (spec → analysis → workbook) is graded.
