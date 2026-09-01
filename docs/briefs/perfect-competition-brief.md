---
type: brief
engagement: perfect-competition
capability: marginal-analysis
date: 2026-09-01
status: committed
hypothesis: "Prioritize tomatoes up to their cap, then allocate to mesclun, and use carrots to fill remaining capacity; given the labor limits (720 farmer hours + up to 1,440 temp hours) and per-bed escalation rates, this ordering will maximize marginal profit. Exact integer bed allocation to be determined by marginal-profit optimization."
---

# Perfect Competition — engagement brief

## The problem

A 64-bed market garden (four plots of 16 beds) must allocate beds across three crops over a 36-week season with $20,000 fixed operating costs. The operator (farmer) earns $50,000 and spends half her time in the field — 720 field hours at an implied opportunity cost of $34.72/hour. Up to four temporary workers are available (totaling up to 1,440 hours) at an implied cost of $17.36/hour. The manager must choose how many beds to plant of each crop subject to bed caps, labor availability, and per-bed diminishing labor returns.

Crops and parameters:
- Tomatoes — max 20 beds; revenue $8,800 per bed (season); 2.50 labor hours per bed per week (→ 90 hours/bed/season); $880 fertilizer per bed; 10.00% diminishing-returns escalation per additional bed.
- Carrots — max 20 beds; revenue $2,094 per bed; 0.833 labor hours per bed per week (→ ~30 hours/bed/season); $440 fertilizer per bed; 2.50% per bed escalation.
- Mesclun — max 30 beds; revenue $2,700 per bed; 1.25 labor hours per bed per week (→ 45 hours/bed/season); $880 fertilizer per bed; 1.25% per bed escalation.

The caps sum to 70 against 64 beds, so not all three crops can be planted at their maximums — that tension drives the optimal allocation decision.

## Key assumptions

- Prices and per-bed base yields are fixed and known for the season.
- Labor per bed follows the compounding labor function used elsewhere in this repository, with beds substituted for trees (additional beds in the same crop raise the per-bed labor requirement by the crop-specific escalation rate).
- Fertilizer and other per-bed fixed costs are applied per planted bed.
- Fixed costs are sunk for allocation decisions; choices follow marginal profit comparisons.
- Temporary labor can be hired up to the available hours and is priced at the stated constant rate; farmer time is valued at the stated opportunity cost.
- Bed spacing and other physical constraints allow up to 64 beds to be used without re-layout costs.

## Hypothesis (simple)

Prioritize tomatoes up to their cap, then allocate to mesclun, and use carrots to fill remaining capacity; given the high initial margin on tomatoes but steep (10%) diminishing returns and the low escalation rates for mesclun, this ordering of allocation will maximize marginal profit. Exact integer bed allocation will be derived by marginal-profit optimization that explicitly prices farmer time and temporary labor.

## Why (one sentence)

Tomatoes start with the highest per-bed margin but escalate fastest, so they should be filled first up to the point where their marginal profit falls below the next-best crop; mesclun's low escalation makes it the natural second choice, and carrots' low-hours requirement makes them appropriate fillers.

## Condensed reasoning

- Start by allocating beds to the crop with the highest initial marginal profit per bed (tomatoes), but stop allocation before escalation erodes marginal profit below alternatives; tomatoes' cap (20) is likely to bind in ranking but the exact stopping point depends on escalation.
- Allocate next to the crop with the lowest escalation rate (mesclun) because additional beds there add less labor escalation per marginal bed.
- Use carrots to fill remaining beds where their low-hours requirement and lower fertilizer cost still yield positive marginal profit after labor is allocated to tomatoes and mesclun.
- Labor constraint: total field-hours required by the chosen allocation (farmer + hired temps) must not exceed 720 farmer-hours + up to 1,440 temp-hours at the stated marginal labor prices. If marginal labor shortages appear, marginal profits are adjusted by the marginal cost of labor (temps at $17.36/hr, farmer time at $34.72/hr).
- The cap sum (70) > available beds (64) creates the binding trade-off that determines which crops get reduced allocations.

## Falsification checks

1. If tomatoes do not approach their cap in the optimal allocation, then either the 10% escalation or per-bed labor/fertilizer or market price for tomatoes is worse than assumed (falsifying the hypothesis).
2. If mesclun remains small despite its low escalation, then its assumed low escalation or revenue is incorrect.
3. If carrots dominate allocations despite lower per-bed revenue, then labor-hours per bed or labor costs are mis-specified (carrots becoming relatively cheap on a labor-hours basis).
4. If total labor required by the hypothesized ranking cannot be met even when hiring temps at their stated cost, then the labor function or hours-per-week estimates are wrong.

Any of these outcomes indicates a different binding constraint (labor, prices, or crop physiology) and falsifies the hypothesis.

## Next steps (analysis to commit with brief)

- Run a marginal-profit integer optimization over (tomatoes, mesclun, carrots) with caps (20,30,20) and total beds ≤ 64 using the repository's compounding-labor function, pricing farmer hours at $34.72/hr and temporary labor at $17.36/hr (temps used first for cost minimization, then farmer hours). Record the optimal integer allocation and the marginal profit table in the analysis folder and update this brief with the explicit allocation and a worked falsification table.
