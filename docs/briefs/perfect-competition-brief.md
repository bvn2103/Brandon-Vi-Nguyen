---
type: brief
engagement: perfect-competition
capability: marginal-analysis
date: 2026-08-28
status: committed
hypothesis: "Allocate 88 mangosteen trees as 44 ultra-premium, 22 high-intensity, and 22 standard to maximize marginal profit under labor constraints; use integer-divisible groupings (factors of 88) for clean composition."
---

# Perfect Competition — engagement brief

## The problem

A 1-acre mangosteen orchard must allocate 88 trees across three cultivation intensities over a 36-week season with $20,000 fixed operating costs. The operator chooses allocations subject to labor capacity and per-tree diminishing returns.

## Key assumptions

- Prices per intensity level are fixed and known.
- Labor per tree compounds as specified: `q × hours-per-week-per-tree × 36 × (1 + rate)^q`.
- Compounding applies per additional tree; later trees require more labor.
- Fixed costs are sunk; decisions follow marginal profit.
- Temporary labor is available at constant cost and can be reallocated across intensities.
- Tree spacing fits one acre without gaps.

## Hypothesis

Allocate 88 trees as: 44 ultra-premium, 22 high-intensity, 22 standard. These integer-divisible groupings align with factors of 88 so modules compose cleanly. Given the specified escalation rates and labor limits, this allocation maximizes marginal profit by assigning highest-margin, low-escalation trees first and filling remaining capacity with higher-escalation types.

## Reasoning (condensed)

- Standard care has the highest base margin but a 10% per-tree escalation; its marginal return falls fastest.
- High-intensity has moderate escalation (2.5%) and lower margin per labor dollar than standard.
- Ultra-premium has the lowest escalation (1.25%) and can absorb remaining labor capacity with acceptable margins.
- Allocating by 44/22/22 assigns capacity to the lowest-escalation, higher-margin cells first, then to progressively higher-escalation cells until labor binds.

## Falsification checks

1. If high-intensity requires fewer than 22 trees, its escalation or labor-hours are higher than assumed.
2. If standard stops before 22 trees, standard escalation or marginal cost is underestimated.
3. If ultra-premium cannot reach 44 trees due to labor limits, total labor availability or per-tree labor is overestimated.

Any of these outcomes indicates a different binding constraint (labor, prices, or physiology) and falsifies the hypothesis.
