---
type: brief
engagement: perfect-competition
capability: marginal-analysis
date: 2026-09-02
status: committed
hypothesis: "Prioritize tomatoes up to their cap, then allocate to mesclun, and use carrots to fill remaining capacity; given the labor limits and per-bed escalation rates, this ordering will maximize marginal profit. Concretely, the marginal-profit optimization suggests planting 5 tomatoes, 8 mesclun, and 11 carrots."
---

# Perfect Competition — engagement brief

## The problem

A 64-bed market garden (four plots of 16 beds) must allocate beds across three crops over a 36-week season with $20,000 fixed operating costs. The operator (farmer) earns $50,000 and spends half her time in the field — 720 field hours at an implied opportunity cost of $34.72/hour. Up to four temporary workers are available (totaling up to 1,440 hours) at an implied cost of $17.36/hour. The manager must choose how many beds to plant of each crop subject to bed caps, labor availability, and per-bed diminishing labor returns.

Crops and parameters:
- Tomatoes — max 20 beds; revenue $8,800 per bed (season); 2.50 labor hours per bed per week (→ 90 hours/bed/season); $880 fertilizer per bed; 10.00% diminishing-returns escalation per additional bed.
- Carrots — max 20 beds; revenue $2,094 per bed; 0.833 labor hours per bed per week (→ ~30 hours/bed/season); $440 fertilizer per bed; 2.50% per bed escalation.
- Mesclun — max 30 beds; revenue $2,700 per bed; 1.25 labor hours per bed per week (→ 45 hours/bed/season); $880 fertilizer per bed; 1.25% per bed escalation.

The caps sum to 70 against 64 beds, so not all three crops can be planted at their maximums — that tension drives the optimal allocation decision. The labor function used is the repository's compounding labor function with beds substituted for trees: total labor for q beds in a crop = q × (hours-per-week-per-bed) × 36 × (1 + rate)^q.

## Key assumptions

- Prices and per-bed base yields are fixed and known for the season.
- Labor per bed follows the compounding labor function above (beds in place of trees).
- Fertilizer and other per-bed fixed costs are applied per planted bed.
- Temporary labor can be hired up to 1,440 hours at $17.36/hr; farmer time is limited to 720 hours and valued at $34.72/hr. Temps are used first (cost-minimizing) up to their cap; any remaining labor is farmer time. Total labor demand must be ≤ 2,160 hours.
- Fixed costs are sunk for allocation decisions; choices follow marginal profit comparisons.

## Hypothesis (simple)

Prioritize tomatoes up to their cap, then allocate to mesclun, and use carrots to fill remaining capacity; given the high initial margin on tomatoes but steep (10%) diminishing returns and the low escalation rates for mesclun, this ordering of allocation will maximize marginal profit. The marginal-profit integer optimization (pricing farmer time at $34.72/hr and temps at $17.36/hr) yields the concrete allocation below: 5 tomatoes, 8 mesclun, 11 carrots.

## Optimal integer allocation (result)

- Tomatoes: 5 beds
- Mesclun: 8 beds
- Carrots: 11 beds
- Total planted beds: 24 (beds may be left fallow if that increases profit; planting all 64 beds is not required and would be infeasible given labor escalation.)

Worked numbers (season totals)

- Season hours per bed (base): Tomatoes 2.50×36 = 90 hr; Mesclun 1.25×36 = 45 hr; Carrots 0.833×36 ≈ 30 hr.
- Total labor (compounding formula):
  - Tomatoes (q=5): 5 × 90 × 1.1^5 = 724.73 hours
  - Mesclun (q=8): 8 × 45 × 1.0125^8 = 397.60 hours
  - Carrots (q=11): 11 × 30 × 1.025^11 = 433.16 hours
  - Grand total labor = 1,555.49 hours (≤ 2,160 available)
- Labor staffing and cost (temps used first):
  - Temps used: 1,440 hours × $17.36 = $24,998.40
  - Farmer hours used: 1,555.49 − 1,440 = 115.49 hours × $34.72 = $4,011.05
  - Total labor cost = $29,009.45
- Revenue and non-labor costs:
  - Revenue: 5×$8,800 + 8×$2,700 + 11×$2,094 = $88,634
  - Fertilizer: 5×$880 + 8×$880 + 11×$440 = $16,280
- Profit accounting:
  - Net before fixed costs = Revenue − Fertilizer − Labor cost = $43,344.55
  - After fixed operating costs ($20,000) = $23,344.55 (this is the reported operating profit under the brief assumptions)

Why this allocation beats nearby allocations

- Tomatoes have high per-bed margin but the 10% per-bed escalation makes larger tomato blocks rapidly more labor-intensive; the compounding labor function makes large tomato allocations infeasible.
- The optimizer trades the high initial per-bed margin on tomatoes against their steep escalation to find the sweet spot (q=5) where marginal profit of another tomato bed falls below planting additional mesclun or carrots.
- Mesclun and carrots absorb the remaining profitable slots where their lower escalation rates keep marginal labor costs manageable.

## Falsification checks (adapted)

1. If tomatoes do not appear in the optimizer's final allocation (i.e., optimal q_tomatoes = 0), then the assumed 10% escalation or hours-per-week for tomatoes or the price per bed is incorrect (or the labor cost assumptions changed). This would falsify the hypothesis that tomatoes should be prioritized.
2. If mesclun remains negligible in the optimal solution despite its low escalation rate, then its revenue or escalation assumptions are likely incorrect.
3. If carrots dominate despite lower per-bed revenue, then hours-per-week or labor-cost assumptions are wrong (carrots would only dominate if their labor-hours were mis-specified or wages were much higher for other crops).
4. If total labor demand for the selected allocation exceeds 2,160 even when hiring all temps, then the compounding labor function or hours-per-week estimates are wrong.

## Mechanism (transfer from Stage 0)

The compounding-labor mechanism transfers unchanged with beds in place of trees: additional beds in the same crop raise the per-bed labor requirement by the crop-specific escalation rate, so marginal labor per new bed grows with q and shifts which crop has the highest marginal profit.

## Next steps (analysis artifacts)

- I will add a short analysis file in analysis/ showing the full integer search (tables of (T,M,C), total hours, labor split, revenue, costs, and net profit) so you can see the optimizer's comparisons and the marginal-profit table I used to select (5,8,11). That file will be committed and linked from this brief.
- Reply in the PR explaining the verification fix: I replaced the mangosteen Stage 0 subject with the Stage 1 64-bed problem, rebuilt the problem statement and hypothesis, ran the integer marginal-profit optimization consistent with the repo's labor function, and updated the brief with the feasible, optimal integer allocation and worked numbers.


