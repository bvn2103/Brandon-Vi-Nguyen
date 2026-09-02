---
type: brief
engagement: perfect-competition
capability: marginal-analysis
date: 2026-09-02
status: committed
hypothesis: "Prioritize tomatoes up to their cap (20 beds), then allocate to mesclun, and use carrots to fill remaining capacity; given the labor limits and per-bed escalation rates, this ordering will maximize profit by exploiting tomatoes' high margin before their steep 10% diminishing returns becomes prohibitive."
---

# Perfect Competition — engagement brief

## The problem

A 64-bed market garden (four plots of 16 beds each) must allocate beds across three crops over a 36-week season with $20,000 fixed operating costs. The operator (the farmer) earns $50,000 annually and spends half her time in the field — 720 hours over the 36-week season, valued implicitly at $34.72/hour. Up to four temporary workers are available at $25,000 each for up to 1,440 hours each, an implied $17.36/hour.

Crops and parameters:
- **Tomatoes** — max 20 beds; revenue $8,800 per bed (season); 2.50 labor hours per bed per week (→ 90 hours/bed/season); $880 fertilizer per bed; 10.00% diminishing-returns escalation per additional bed
- **Carrots** — max 20 beds; revenue $2,094 per bed; 0.833 labor hours per bed per week (→ ~30 hours/bed/season); $440 fertilizer per bed; 2.50% escalation per bed
- **Mesclun** — max 30 beds; revenue $2,700 per bed; 1.25 labor hours per bed per week (→ 45 hours/bed/season); $880 fertilizer per bed; 1.25% escalation per bed

The caps sum to 70 against 64 beds, so not all three crops can be planted at their maximums — that tension drives the optimal allocation decision. The labor function used is the compounding escalation model: **Labor per bed = base_hours × (1 + escalation_rate)^q**, where q is the quantity (beds) of that crop and the exponent applies per additional unit. This creates the critical decision tension: which beds are worth planting given their rising labor cost?

## Key assumptions

- Prices and per-bed base yields are fixed and known for the season.
- Labor per bed follows the compounding labor function: base_labor_hours × (1 + crop_escalation)^q where q is beds planted of that crop.
- Fertilizer and other per-bed fixed costs are applied per planted bed.
- Temporary labor can be hired up to 1,440 hours at $17.36/hr; farmer time is limited to 720 hours and valued at $34.72/hr. Temps are cost-minimizing and are used first up to their cap; any remaining labor requirement draws on farmer time.
- Fixed costs ($20,000) are sunk for allocation decisions; choices follow marginal profit comparisons.
- Not all 64 beds need to be planted; planting any bed must generate positive marginal profit after labor escalation costs.

## Hypothesis (committed)

Prioritize tomatoes up to their cap (20 beds), then allocate to mesclun, and use carrots to fill remaining capacity; given the high initial margin on tomatoes ($8,800/bed) but steep (10.00%) diminishing returns and the lower escalation rates on mesclun (1.25%) and carrots (2.50%), this ordering will maximize profit. Tomatoes' high per-bed margin justifies planting more beds despite the escalation, but the 10% per-bed compounding makes the marginal cost curve steep, so other crops absorb remaining capacity where their lower escalation keeps labor manageable.

**Predicted allocation:**
- Tomatoes: 20 beds (maximized; high margin justifies escalation cost)
- Mesclun: 20 beds (next best margin and low escalation; fill to fill some remaining space)
- Carrots: 11 beds (fill remaining capacity; lower margin but lowest escalation)
- Total planted: 51 beds (13 beds left fallow; adding more beds would incur labor costs exceeding marginal revenue)

## Economic mechanism

The compounding-labor model creates the decision tension. For each crop c, total labor in hours is:

**Labor(q_c) = base_hours_per_week_c × 36 weeks × q_c × (1 + escalation_c)^q_c**

This means the *q-th bed* planted of crop c requires more labor than the (q-1)-th bed. The farmer and temporary workers have fixed budgets (720 + 1,440 = 2,160 total hours). As q grows for any crop, the per-bed escalation compounds, and eventually the marginal labor cost of adding another bed exceeds the marginal revenue.

**Why this matters for the decision:** Each crop has a different escalation rate, so the tradeoff between crops changes as beds are added. Tomatoes' 10% escalation is steep — planting 20 tomato beds requires 90 × 20 × 1.1^20 = 5,670 hours, far exceeding available labor. The optimal solution balances tomatoes' high margin against their steep escalation, mesclun's moderate margin and low escalation, and carrots' low margin and moderate escalation.

## Falsification checks

1. **If tomatoes appear in the optimal allocation at fewer than 10 beds,** then the assumed $8,800 per-bed revenue or 2.50 labor hours-per-week, or the 10.00% escalation rate, is higher than the true value (i.e., tomatoes are less profitable than assumed). The high margin is the only reason to prioritize tomatoes; if they drop out or fall well short of the cap, the margin assumption is wrong.

2. **If mesclun remains negligible (fewer than 5 beds) in the optimal allocation despite the low 1.25% escalation rate and $2,700 per-bed revenue,** then either its revenue or its base labor-hours are incorrectly specified. Mesclun's low escalation should make it highly attractive after tomatoes fill to their sweet spot.

3. **If carrots dominate the allocation (more than mesclun) despite lower per-bed revenue ($2,094 vs $2,700),** then the base labor-hours (0.833/week) or escalation rate (2.50%) for carrots must be lower than assumed, or mesclun's labor cost must be higher. Carrots should only dominate if their per-bed labor is genuinely lower and escalation lower, not because of a mis-specification.

4. **If total labor demand for the selected allocation exceeds 2,160 hours even when hiring all four temporary workers to their 1,440-hour cap,** then the base labor-hours per bed per week or the 36-week season length is incorrectly specified. This is the binding constraint for the problem.

## Next steps (analysis artifacts)

- I will add a short analysis file in `analysis/` showing the full integer search: a table of (T, M, C) allocations, total hours required, labor split between temps and farmer, revenue, costs, and net profit for the top 10 candidate allocations. This will show how the optimizer compares the hypothesized allocation against nearby candidates.
- Reply in the PR explaining the verification fix: I replaced the earlier mangosteen Stage 0 subject with the Stage 1 64-bed market garden problem, rebuilt the problem statement to name all farmers, beds, crops, prices, and labor rates, ran the integer marginal-analysis and committed the hypothesis before modeling to preserve the comparison in Stage 3.
