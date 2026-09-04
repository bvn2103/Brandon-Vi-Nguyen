---
type: brief
engagement: perfect-competition
capability: marginal-analysis
date: 2026-09-04
status: committed
hypothesis: "Prioritize tomatoes up to ~12 beds (where marginal labor cost meets marginal revenue), then allocate to mesclun, and use carrots to fill remaining capacity; labor escalation, not the 6,480-hour pool, determines where planting stops."
---

# Perfect Competition — engagement brief

## The problem

A 64-bed market garden (four plots of 16 beds each) must allocate beds across three crops over a 36-week season with $20,000 fixed operating costs. The operator (the farmer) earns $50,000 annually and has a limited amount of farmer-time; temporary labor can be hired at known rates. The decision is how many beds of each crop to plant this season to maximize profit given per-bed revenues, per-bed input costs, and a compounding labor escalation function.

Crops and parameters:
- **Tomatoes** — max 20 beds; revenue $8,800 per bed (season); 2.50 labor hours per bed per week (→ 90 hours/bed/season); $880 fertilizer per bed; 10.00% diminishing-returns escalation per added bed
- **Carrots** — max 20 beds; revenue $2,094 per bed; 0.833 labor hours per bed per week (→ ~30 hours/bed/season); $440 fertilizer per bed; 2.50% escalation per bed
- **Mesclun** — max 30 beds; revenue $2,700 per bed; 1.25 labor hours per bed per week (→ 45 hours/bed/season); $880 fertilizer per bed; 1.25% escalation per bed

The caps sum to 70 against 64 beds, so not all three crops can be planted at their maximums — that tension drives the optimal allocation decision. The labor function used is the compounding escalation model described below.

## Key assumptions

- Prices and per-bed base yields are fixed and known for the season.
- Labor per bed follows the compounding labor function: base_labor_hours × (1 + crop_escalation)^q where q is beds planted of that crop.
- Fertilizer and other per-bed fixed costs are applied per planted bed.
- Temporary labor can be hired up to 1,440 hours at $17.36/hr per worker; farmer time is limited to 720 hours and valued at $34.72/hr. Up to four temporary workers are available for a total pool of 5,760 temporary hours, so combined available hours are 720 + 5,760 = 6,480 total hours.
- Fixed costs ($20,000) are sunk for allocation decisions; choices follow marginal profit comparisons.
- Not all 64 beds need to be planted; planting any bed must generate positive marginal profit after labor escalation costs.

## Hypothesis (committed)

Prioritize tomatoes up to ~12 beds (where labor escalation costs reach the point that marginal hours cost more than marginal revenue), then allocate to mesclun, and use carrots to fill remaining capacity.

**Predicted allocation:**
- Tomatoes: 12 beds (labor escalation makes marginal hours cost exceed marginal revenue at the 12th bed; 90 × 12 × 1.1^12 ≈ 2,790 hours)
- Mesclun: 20 beds (low 1.25% escalation and strong revenue; total ≈ 1,960 hours)
- Carrots: 20 beds (fill remaining capacity within labor budget; total ≈ 983 hours)
- Total planted: 52 beds (12 beds left fallow; adding more beds would cause the marginal cost of the next bed to exceed its marginal revenue)

## Economic mechanism

The compounding-labor model creates the decision tension. For each crop c, total labor in hours is:

Labor(q_c) = base_hours_per_week_c × 36 weeks × q_c × (1 + escalation_c)^q_c

This means the q-th bed planted of crop c requires more labor than the (q-1)-th bed. The farmer and temporary workers have a combined budget of 720 + 5,760 = 6,480 total hours. As q grows for any crop, its marginal labor-hour requirement and thus marginal labor cost rise; the optimal allocation stops adding beds to a crop when the marginal revenue from an additional bed is no longer greater than the marginal labor (and input) cost of that bed.

Pick the marginal-cost story: in the model runs I expect the labor pool of 6,480 hours to remain unexhausted at the optimum, and the binding constraint to be marginal cost per bed, not total hours available.

## Falsification checks

1. **If tomatoes appear in the optimal allocation at fewer than 10 beds,** then the assumed $8,800 per-bed revenue or 2.50 labor hours-per-week base, or the 10.00% escalation rate, is higher than reality.

2. **If mesclun remains negligible (fewer than 5 beds) in the optimal allocation despite the low 1.25% escalation rate and $2,700 per-bed revenue,** then either its revenue or its base labor-hours estimates are wrong.

3. **If carrots dominate the allocation (more than mesclun) despite lower per-bed revenue ($2,094 vs $2,700),** then the base labor-hours (0.833/week) or escalation rate (2.50%) for carrots must be mis-specified.

4. **If the labor pool of 6,480 hours is exhausted at the optimum,** then the model's marginal-cost interpretation is falsified and total-hours capacity — not marginal cost per bed — would be the binding constraint. I expect the opposite: the labor pool will not be fully used and marginal cost will bind.

## Next steps (analysis artifacts)

- I will add a short analysis file in `analysis/` showing the full integer search: a table of (T, M, C) allocations, total hours required, labor split between temps and farmer, revenue, costs, and per-allocation marginal comparisons.
- I will add a specification file for the marginal-analysis capability before committing the workbook. That spec will include the labor function (with the exponent on q) and two hand-checks to catch arithmetic errors:
  - One tomato bed: 90 × 1 × 1.1^1 = 99 hours exactly.
  - Ten tomato beds: 90 × 10 × 1.1^10 ≈ 2,334.37 hours.
- Reply in the PR explaining the verification fix: I corrected the labor pool to 6,480 hours, recalculated the cost of 20 tomato beds (≈12,110 hours, not 5,670), and revised the hypothesis to allocate until marginal labor cost meets marginal revenue rather than using a capacity-ceiling argument.

