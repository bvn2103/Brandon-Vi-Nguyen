---
type: brief
engagement: perfect-competition
capability: marginal-analysis
date: 2026-09-02
status: committed
hypothesis: "Prioritize tomatoes up to ~12 beds (where marginal labor cost meets marginal revenue), then allocate to mesclun, and use carrots to fill remaining capacity; labor escalation, not the 6,480-hour ceiling, determines the binding constraint."
---

# Perfect Competition — engagement brief

## The problem

A 64-bed market garden (four plots of 16 beds each) must allocate beds across three crops over a 36-week season with $20,000 fixed operating costs. The operator (the farmer) earns $50,000 annually for up to 720 field hours; temporary workers are hired at $17.36/hr (up to four workers at 1,440 hours each). The season is planted once.

Crops and parameters:
- **Tomatoes** — max 20 beds; revenue $8,800 per bed (season); 2.50 labor hours per bed per week (→ 90 hours/bed/season); $880 fertilizer per bed; 10.00% diminishing-returns escalation per added bed
- **Carrots** — max 20 beds; revenue $2,094 per bed; 0.833 labor hours per bed per week (→ ~30 hours/bed/season); $440 fertilizer per bed; 2.50% escalation per bed
- **Mesclun** — max 30 beds; revenue $2,700 per bed; 1.25 labor hours per bed per week (→ 45 hours/bed/season); $880 fertilizer per bed; 1.25% escalation per bed

The caps sum to 70 against 64 beds, so not all three crops can be planted at their maximums — that tension drives the optimal allocation decision. The labor function used is the compounding escalation model: as q beds of a given crop are planted, each successive bed requires more labor due to congestion, harvest scheduling, or other per-crop bottlenecks.

## Key assumptions

- Prices and per-bed base yields are fixed and known for the season.
- Labor per bed follows the compounding labor function: base_labor_hours × (1 + crop_escalation)^q where q is beds planted of that crop.
- Fertilizer and other per-bed fixed costs are applied per planted bed.
- Temporary labor can be hired up to 1,440 hours at $17.36/hr per worker; farmer time is limited to 720 hours and valued at $34.72/hr. Up to four temporary workers are available for a total pool of 720 + 5,760 = 6,480 hours. Temps are cost-minimizing and are used first up to their cap; any remaining labor demand falls to the farmer.
- Fixed costs ($20,000) are sunk for allocation decisions; choices follow marginal profit comparisons.
- Not all 64 beds need to be planted; planting any bed must generate positive marginal profit after labor escalation costs.

## Hypothesis (committed)

Prioritize tomatoes up to ~12 beds (where labor escalation costs reach the point that marginal hours cost more than marginal revenue), then allocate to mesclun, and use carrots to fill remaining capacity. The binding constraint is not the labor ceiling itself but the escalation cost per bed: the bed that stops being worth planting is the one whose marginal hours cost more than the $8,800 it earns.

**Predicted allocation:**
- Tomatoes: 12 beds (labor escalation costs become prohibitive; 90 × 12 × 1.1^12 ≈ 2,790 hours, leaving insufficient budget for other crops and approaching the marginal revenue limit)
- Mesclun: 20 beds (low 1.25% escalation and strong revenue; total ~1,960 hours)
- Carrots: 20 beds (fill remaining capacity within labor budget; total ~983 hours)
- Total planted: 52 beds (12 beds left fallow; adding more beds would incur labor costs exceeding marginal revenue)

## Economic mechanism

The compounding-labor model creates the decision tension. For each crop c, total labor in hours is:

**Labor(q_c) = base_hours_per_week_c × 36 weeks × q_c × (1 + escalation_c)^q_c**

This means the *q-th bed* planted of crop c requires more labor than the (q-1)-th bed. The farmer and temporary workers have a combined budget of 720 + 5,760 = 6,480 total hours. As q grows for any crop, labor escalation rapidly consumes hours, raising the effective marginal cost per bed.

**Why this matters for the decision:** Each crop has a different escalation rate, so the tradeoff between crops changes as beds are added. Tomatoes' 10% escalation is steep — at 20 beds, 90 × 20 × 1.1^20 ≈ 12,110 hours, far beyond what's affordable. Mesclun's 1.25% escalation is gentle. Carrots fall in between. The optimal allocation balances revenue per bed against escalation cost, and for tomatoes, that balance tips well before the 20-bed cap.

## Falsification checks

1. **If tomatoes appear in the optimal allocation at fewer than 10 beds,** then the assumed $8,800 per-bed revenue or 2.50 labor hours-per-week base, or the 10.00% escalation rate, is higher than the true values — or labor is cheaper than assumed.

2. **If mesclun remains negligible (fewer than 5 beds) in the optimal allocation despite the low 1.25% escalation rate and $2,700 per-bed revenue,** then either its revenue or its base labor-hours (1.25/week) or escalation rate must be materially mis-specified.

3. **If carrots dominate the allocation (more than mesclun) despite lower per-bed revenue ($2,094 vs $2,700),** then the base labor-hours (0.833/week) or escalation rate (2.50%) for carrots must be significantly lower than estimated, or its revenue higher.

4. **If the marginal cost of the final planted bed exceeds its marginal revenue (i.e., a bed that *should* be planted is not because escalation costs it too much),** then labor costs or escalation rates are mis-specified, not the labor ceiling. The labor pool of 6,480 hours is never exhausted at the optimum; the binding constraint is marginal cost per bed, not total hours available.

## Next steps (analysis artifacts)

- I will add a short analysis file in `analysis/` showing the full integer search: a table of (T, M, C) allocations, total hours required, labor split between temps and farmer, revenue, costs, and profit. This will confirm whether the labor ceiling or the marginal-cost principle stops tomatoes at 12 or some other number.
- Reply in the PR explaining the verification fix: I corrected the labor pool to 6,480 hours, recalculated the cost of 20 tomato beds (12,110 hours, not 5,670), and revised the hypothesis to allocate 12 tomato beds where escalation cost meets marginal revenue, not the full cap. This ensures the brief's mechanism supports its prediction.
