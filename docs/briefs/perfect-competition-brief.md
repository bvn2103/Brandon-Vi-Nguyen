---
type: brief
engagement: perfect-competition
capability: marginal-analysis
date: 2026-08-28
status: committed
hypothesis: "On 1 acre of mangosteen, the farm should allocate 88 trees with optimal spacing and density, constrained by labor capacity and diminishing returns on maintenance hours per tree."
---

# Perfect Competition — engagement brief

## The problem

The farm operates a 1-acre mangosteen orchard within a 36-week harvest and maintenance season with a fixed $20,000 operational cost structure. The operator chooses how to allocate 88 mangosteen trees across the acre—deciding tree density, spacing configuration, and labor-intensive cultivation practices (pruning, pest management, fertigation)—subject to hard limits: maximum 88 trees per acre (the biological/spacing constraint), and a bed-equivalent cap of 20/20/30 for three cultivation intensity levels (standard, high-intensity, ultra-premium). The real constraint is labor: 720 hours of owner time plus access to up to four temp workers (1,440 hours each), for a maximum of 6,480 total labor hours across the season. Each cultivation level has a market price locked in based on fruit quality and yield (standard $8,800/acre equivalent, high-intensity $2,094/acre equivalent, ultra-premium at a price to be confirmed). The complication is diminishing returns on labor: as tree density increases and cultivation intensity rises, labor hours per tree compounds—10% escalation for standard care, 2.5% for high-intensity, 1.25% for ultra-premium approaches. This rising marginal cost means the optimal strategy is not simply "maximize tree density and push all trees to ultra-premium"—at some point, adding another tree or intensifying care becomes more expensive than its market return is worth. The question is where that crossover happens for each intensity level, and whether it's marginal cost that stops intensification or the biological cap.

## What I am assuming

- Market prices are fixed and deterministic per cultivation intensity level (no price risk)
- Labor hour formulas compound exactly as specified: `q × hours-per-week-per-tree × 36 × (1 + rate)^q`
- The compounding rate applies *per additional tree or intensity increment*, not total—so tree 88 costs much more to cultivate than tree 1
- Fixed costs of $20,000 are sunk and do not affect the allocation decision (only marginal profit matters)
- Temp worker availability is guaranteed at constant cost (no scarcity premium)
- No substitution constraints between cultivation levels in use of labor (labor can be allocated flexibly)
- Tree spacing follows agronomic best practice and doesn't create gaps in the 1-acre footprint
- Ultra-premium price is competitive with its marginal labor cost (assumption to test: if ultra-premium prices much higher, the allocation shifts to premium-heavy)

## Hypothesis

I expect the 88 mangosteen trees to be allocated as **20 trees under standard cultivation, 20 trees under high-intensity cultivation, and 48 trees under ultra-premium cultivation**, with standard and high-intensity hitting their bed-equivalent caps, and ultra-premium filling remaining labor capacity.

**Reasoning by diminishing returns:**

Standard care earns $8,800/acre equivalent but has a 10% labor-cost escalation rate per tree. The 1st tree is cheap to maintain; the 20th tree is roughly 6.7× more labor-intensive. I expect standard-care trees hit the 20-tree cap before marginal cost catches the $8,800 return—standard's high margin and the early trees' low labor cost should fill the cap.

High-intensity cultivation earns $2,094/acre equivalent with only 2.5% escalation per tree, so labor cost compounds more slowly. However, high-intensity is the weakest margin per dollar of labor invested. I expect high-intensity trees to stop at 20 trees (hitting the cap) because resource allocation to ultra-premium becomes more attractive beyond that point.

Ultra-premium has only 1.25% escalation per tree and fills remaining labor capacity. With standard at 20 and high-intensity at 20, I expect the operator fills remaining labor budget (approximately 6,480 − labor-for-20-standard − labor-for-20-high-intensity) with ultra-premium cultivation on 48 additional trees, leaving the 88th tree unallocated or minimally maintained.

The mechanism: standard stops at cap (highest margin per unit labor), high-intensity stops at its allocation ceiling (second-tier returns), ultra-premium stops at remaining labor capacity (fills the gap efficiently).

## How I would know I was wrong

1. **If high-intensity cultivation reaches fewer than 20 trees** — this would mean diminishing returns on high-intensity labor bite earlier than expected, or high-intensity labor hours per tree are higher than the formula implies. It would suggest the marginal cost floor for high-intensity is lower than I've estimated, and I've overallocated labor to other tiers.

2. **If standard cultivation stops before the 20-tree cap** — this would mean marginal labor cost for standard trees rises faster than the 10% rate implies, or tree 20 requires substantially more hours than the formula predicts. It would contradict my assumption about standard care's cost escalation and suggest tighter labor constraints.

3. **If ultra-premium cultivation stops at fewer than 40 trees due to labor exhaustion** — this would mean total labor hours available are significantly tighter than 6,480, or the per-tree labor requirements for standard and high-intensity at full caps are much higher than the formula suggests. It would point to a critical labor bottleneck I've underestimated.

Any of these outcomes would falsify the hypothesis and indicate a different binding constraint—whether that's labor availability, price/cost ratios, or tree physiology—than I've identified.

