#!/usr/bin/env python3
"""
Integer-search analysis for the perfect-competition marginal-analysis.
Run: python3 analysis/integer_search.py
Produces a small results summary to stdout and writes analysis/results.md
"""
from math import isclose

# Parameters
W = 36
H_f = 720.0
H_t_pool = 5760.0
H_total = H_f + H_t_pool
F = 20000.0

# Crop params
crops = {
    'tomato': {
        'base_per_week': 2.50,
        'escalation': 0.10,
        'revenue': 8800.0,
        'fertilizer': 880.0,
        'max': 20,
    },
    'mesclun': {
        'base_per_week': 1.25,
        'escalation': 0.0125,
        'revenue': 2700.0,
        'fertilizer': 880.0,
        'max': 30,
    },
    'carrot': {
        'base_per_week': 0.833,
        'escalation': 0.025,
        'revenue': 2094.0,
        'fertilizer': 440.0,
        'max': 20,
    }
}

FARMER_RATE = 34.72
TEMP_RATE = 17.36

# Labor function
def labor_for_crop(crop_key, q):
    if q <= 0:
        return 0.0
    p = crops[crop_key]
    base_season = p['base_per_week'] * W
    return base_season * q * ((1 + p['escalation']) ** q)

# Marginal labor
def marginal_labor(crop_key, q):
    return labor_for_crop(crop_key, q) - labor_for_crop(crop_key, q-1)

# Hand-checks
assert isclose(labor_for_crop('tomato', 1), 99.0, rel_tol=1e-6), f"Hand-check failed for 1 tomato: {labor_for_crop('tomato',1)}"
# 10 tomato beds
# Expected ~2334.37
exp_10 = 90.0 * 10 * (1.1 ** 10)
assert isclose(labor_for_crop('tomato',10), exp_10, rel_tol=1e-6), "Hand-check failed for 10 tomato beds"
# 20 tomato beds
exp_20 = 90.0 * 20 * (1.1 ** 20)
assert isclose(labor_for_crop('tomato',20), exp_20, rel_tol=1e-6), "Hand-check failed for 20 tomato beds"

# Search domain
best = None
results = []
for T in range(0, crops['tomato']['max'] + 1):
    for M in range(0, crops['mesclun']['max'] + 1):
        for C in range(0, crops['carrot']['max'] + 1):
            if T + M + C > 64:
                continue
            # total labor hours per crop
            LT = labor_for_crop('tomato', T)
            LM = labor_for_crop('mesclun', M)
            LC = labor_for_crop('carrot', C)
            total_hours = LT + LM + LC
            # allocate farmer hours first (opportunity cost), then temp hours
            farmer_used = min(H_f, total_hours)
            temp_used = max(0.0, total_hours - farmer_used)
            # if temp_used exceeds pool, mark as infeasible (cannot hire beyond pool)
            if temp_used > H_t_pool:
                continue
            labor_cost = farmer_used * FARMER_RATE + temp_used * TEMP_RATE
            revenue = T * crops['tomato']['revenue'] + M * crops['mesclun']['revenue'] + C * crops['carrot']['revenue']
            input_costs = T * crops['tomato']['fertilizer'] + M * crops['mesclun']['fertilizer'] + C * crops['carrot']['fertilizer']
            profit = revenue - input_costs - labor_cost - F
            results.append((profit, T, M, C, total_hours, farmer_used, temp_used))
            if best is None or profit > best[0]:
                best = (profit, T, M, C, total_hours, farmer_used, temp_used)

# Sort top 10
results_sorted = sorted(results, key=lambda x: x[0], reverse=True)

# Write results file
with open('analysis/results.md', 'w') as f:
    f.write('# Integer search results\n\n')
    if best is None:
        f.write('No feasible allocations found within labor pools.\n')
    else:
        profit, T, M, C, total_hours, farmer_used, temp_used = best
        f.write(f'**Best allocation (by profit):** Tomatoes={T}, Mesclun={M}, Carrots={C}\n\n')
        f.write(f'- Total planted: {T+M+C}\n')
        f.write(f'- Total labor hours required: {total_hours:.2f}\n')
        f.write(f'- Farmer hours used: {farmer_used:.2f}\n')
        f.write(f'- Temp hours used: {temp_used:.2f}\n')
        f.write(f'- Total profit: ${profit:,.2f}\n\n')
        f.write('## Top 10 allocations by profit\n\n')
        for row in results_sorted[:10]:
            profit, T, M, C, total_hours, farmer_used, temp_used = row
            f.write(f'- Profit ${profit:,.2f}: T={T}, M={M}, C={C}, hours={total_hours:.2f} (farmer {farmer_used:.2f}, temp {temp_used:.2f})\n')

# Print summary to stdout
if best:
    profit, T, M, C, total_hours, farmer_used, temp_used = best
    print('Best allocation: Tomatoes={}, Mesclun={}, Carrots={}'.format(T, M, C))
    print('Total planted:', T+M+C)
    print('Total labor hours: {:.2f}'.format(total_hours))
    print('Farmer hours used: {:.2f}, Temp hours used: {:.2f}'.format(farmer_used, temp_used))
    print('Total profit: ${:,.2f}'.format(profit))
else:
    print('No feasible allocation found within labor pools')
