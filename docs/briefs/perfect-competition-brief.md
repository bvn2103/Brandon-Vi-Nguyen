---
type: brief
engagement: perfect-competition
capability: marginal-analysis
date: 2026-08-28
status: committed
hypothesis: "Allocate the 88 trees as 44 ultra-premium, 22 high-intensity, and 22 standard; given the labor limits and per-tree escalation rates, this allocation will maximize marginal profit."
---

# Perfect Competition — engagement brief

## The problem

A 1-acre mangosteen orchard must allocate 88 trees across three cultivation intensities over a 36-week season with $20,000 fixed operating costs. The operator chooses allocations subject to labor capacity and per-tree diminishing returns.

## Key assumptions

- Prices per intensity level are fixed and known.
- Labor per tree follows: `q × hours-per-week-per-tree × 36 × (1 + rate)^q`.
- Compounding applies per additional tree; later trees require more labor.
- Fixed costs are sunk; decisions follow marginal profit.
- Temporary labor is available at constant cost and can be reallocated across intensities.
- Tree spacing fits one acre without gaps.

## Hypothesis (simple)

Allocate the 88 trees as 44 ultra-premium, 22 high-intensity, and 22 standard; given the labor limits and per-tree escalation rates, this allocation will maximize marginal profit.

## Why (one sentence)

Ultra-premium trees have the lowest per-tree escalation, so they take the largest share; standard trees escalate fastest and therefore receive a smaller share, letting labor flow to the highest marginal returns.

## Condensed reasoning

- Assign capacity first to the lowest-escalation, highest-margin cells (ultra-premium), then to moderate-escalation cells (high-intensity), and last to high-escalation cells (standard) until labor binds.
- The 44/22/22 split uses integer-divisible groupings of 88 for clear allocation blocks and simplifies operational planning.

## Falsification checks

1. If high-intensity requires materially fewer than 22 trees, then its escalation or labor-hours per tree are higher than assumed.
2. If standard stops well before 22 trees, then standard escalation or marginal cost is underestimated.
3. If ultra-premium cannot reach 44 trees due to labor limits, then total labor availability or per-tree labor is overestimated.

Any of these outcomes indicates a different binding constraint (labor, prices, or physiology) and falsifies the hypothesis.
