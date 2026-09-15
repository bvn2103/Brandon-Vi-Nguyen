# Marginal-analysis specification

capability: marginal-analysis  
stage: perfect-competition-stage2  
created: 2026-09-04  
updated: 2026-09-11

## Objective

Produce an auditable Excel workbook at `capabilities/marginal-analysis/model.xlsx` that models the farm allocation decision exactly as specified here. This specification is the build contract: the workbook, verifier, and audit notes must all stay aligned with it.

## Inputs (named contract)

Every input must exist as a workbook-scoped named range, with the stated value, unit, and case source.

| Name | Value | Unit | Source / note |
|---|---:|---|---|
| `Season_Weeks` | 36 | weeks | Case scenario |
| `Farmer_Hours_Available` | 720 | hours | Case scenario; farmer hours are consumed before temporary labor |
| `Farmer_Hourly_Rate` | 34.72 | $/hour | Opportunity cost from case scenario |
| `Temp_Hours_Pool` | 5,760 | hours | 4 temporary workers × 1,440 hours each |
| `Temp_Hourly_Rate` | 17.36 | $/hour | Temporary labor wage from case scenario |
| `Fixed_Cost` | 20,000 | $ | Case scenario fixed cost |
| `Total_Bed_Cap` | 64 | beds | 4 plots × 16 beds |
| `Tomato_Base_Hours_Per_Week` | 2.50 | hours/week/bed | Case scenario |
| `Tomato_Dim_Pct` | 0.10 | decimal | Case scenario |
| `Tomato_Revenue_Per_Bed` | 8,800 | $/bed | Case scenario |
| `Tomato_Fertilizer_Per_Bed` | 880 | $/bed | Case scenario |
| `Tomato_Max_Beds` | 20 | beds | Case scenario |
| `Mesclun_Base_Hours_Per_Week` | 1.25 | hours/week/bed | Case scenario |
| `Mesclun_Dim_Pct` | 0.0125 | decimal | Case scenario |
| `Mesclun_Revenue_Per_Bed` | 2,700 | $/bed | Case scenario |
| `Mesclun_Fertilizer_Per_Bed` | 880 | $/bed | Case scenario |
| `Mesclun_Max_Beds` | 30 | beds | Case scenario |
| `Carrot_Base_Hours_Per_Week` | `2.5 / 3` exactly | hours/week/bed | Use the exact fraction, not a rounded display value |
| `Carrot_Dim_Pct` | 0.025 | decimal | Case scenario |
| `Carrot_Revenue_Per_Bed` | 2,094 | $/bed | Case scenario |
| `Carrot_Fertilizer_Per_Bed` | 440 | $/bed | Case scenario |
| `Carrot_Max_Beds` | 20 | beds | Case scenario |

## Workbook structure

The workbook must contain these sheets and purposes:

1. **`Inputs`** — all named inputs, units, and source notes.
2. **`Labor & Cost`** — the labor function by crop for integer bed counts, discrete marginal labor, standalone labor dollars, standalone marginal cost, and standalone crossing diagnostics.
3. **`Allocation`** — the three decision variables, per-crop roll-up, labor allocation, blended labor rate, fixed cost, and total profit.
4. **`Checks`** — live validation formulas for hand-checks, published reference checks, exact script checks, and feasibility constraints.
5. **`Summary`** — the audited optimal allocation, total hours, total dollars, final profit, standalone crossing summary, and the tomato MC dip note for Stage 3.

The workbook must open cleanly in Excel, with no `#REF!`, `#DIV/0!`, or `#NAME?` errors.

## Calculation logic (named-range notation only)

Use named inputs and logic, not cell addresses.

### Labor schedule

For each crop `c` and integer bed count `q`:

- `LABOR_HRS_c(q) = c_Base_Hours_Per_Week × Season_Weeks × q × (1 + c_Dim_Pct)^q`
- `MARGINAL_LABOR_HRS_c(q) = LABOR_HRS_c(q) - LABOR_HRS_c(q - 1)`

Set `LABOR_HRS_c(0) = 0` and `MARGINAL_LABOR_HRS_c(0) = 0`.

### Standalone labor dollars and marginal cost

For each crop’s standalone schedule, cost labor with the farm rule:

- farmer hours are consumed first, always
- the first `Farmer_Hours_Available` hours are valued at `Farmer_Hourly_Rate`
- remaining hours are valued at `Temp_Hourly_Rate`

Named logic:

- `STANDALONE_LABOR_DOLLARS_c(q) = MIN(Farmer_Hours_Available, LABOR_HRS_c(q)) × Farmer_Hourly_Rate + MAX(0, LABOR_HRS_c(q) - Farmer_Hours_Available) × Temp_Hourly_Rate`
- `STANDALONE_MC_c(q) = STANDALONE_LABOR_DOLLARS_c(q) - STANDALONE_LABOR_DOLLARS_c(q - 1)`
- `NET_CONTRIBUTION_c = c_Revenue_Per_Bed - c_Fertilizer_Per_Bed`

The workbook must expose the first `q` where `STANDALONE_MC_c(q) > NET_CONTRIBUTION_c`, then report the last profitable bed as `q - 1`.

Do not write into the spec that marginal cost is monotone. The workbook must implement the mechanism above and let the schedule reveal the shape.

### Allocation and P&L

Decision variables:

- `Tomato_Beds`
- `Mesclun_Beds`
- `Carrot_Beds`

Feasible region:

- `0 ≤ Tomato_Beds ≤ Tomato_Max_Beds`
- `0 ≤ Mesclun_Beds ≤ Mesclun_Max_Beds`
- `0 ≤ Carrot_Beds ≤ Carrot_Max_Beds`
- `Tomato_Beds + Mesclun_Beds + Carrot_Beds ≤ Total_Bed_Cap`
- `Temp_Hours_Used ≤ Temp_Hours_Pool`

Workbook roll-up:

- `Crop_Labor_Hours = LABOR_HRS_c(Beds)`
- `Total_Labor_Hours = Tomato_Labor_Hours + Mesclun_Labor_Hours + Carrot_Labor_Hours`
- `Farmer_Hours_Used = MIN(Farmer_Hours_Available, Total_Labor_Hours)`
- `Temp_Hours_Used = MAX(0, Total_Labor_Hours - Farmer_Hours_Used)`
- `Total_Labor_Dollars = Farmer_Hours_Used × Farmer_Hourly_Rate + Temp_Hours_Used × Temp_Hourly_Rate`
- `Blended_Labor_Rate = Total_Labor_Dollars / Total_Labor_Hours` when `Total_Labor_Hours > 0`, else `0`
- per-crop labor dollars in the P&L are allocated at `Crop_Labor_Hours × Blended_Labor_Rate`
- `Profit = Total_Revenue - Total_Fertilizer - Total_Labor_Dollars - Fixed_Cost`

The farmer-versus-temporary split is a farm-level fact. The per-crop P&L uses the blended rate above rather than assigning farmer hours crop-by-crop.

### Solver setup

The workbook must document the desktop Excel Solver setup explicitly:

- objective: maximize `Profit`
- changing cells: the three bed-count decision variables
- method: `GRG Nonlinear`
- decisions constrained to integers
- constraints listed clearly so a reviewer can enter them in desktop Excel and rerun from `0 / 0 / 0` and `20 / 0 / 0`

## Validation rules (acceptance criteria)

The workbook must compute these checks live:

### Hand-checks

- One tomato bed: `1 × 2.5 × 36 × 1.10 = 99.0` hours
- Ten tomato beds: `10 × 2.5 × 36 × 1.10^10 = 2,334.368214090002` hours
- Twenty tomato beds: `20 × 2.5 × 36 × 1.10^20 = 12,109.4999087861` hours

### Published reference checks

- Optimal mix: Tomatoes `10`, Mesclun `30`, Carrots `20` (60 beds total)
- Published season profit reference: approximately `$42,762`
- Standalone first-crossing results: Tomatoes `~10`, Carrots `~10`, Mesclun `~6` profitable beds

### Exact verification checks

- The workbook must match `analysis/integer_search.py`
- With the exact carrot fraction, the verification script’s best allocation remains `10 / 30 / 20`
- Exact script profit is `$42,761.66`, which is the published `$42,762` carried to the cent

### Workbook integrity checks

- All key constraint checks show `PASS`
- No error cells on any deliverable sheet
- Every calculated cell contains a formula, not a pasted value
- The workbook is auditable by reading formulas against these named inputs

## Required outputs

The workbook must report at minimum:

- optimal tomatoes, mesclun, and carrots bed counts
- total beds
- total labor hours
- farmer hours used
- temporary hours used
- total revenue
- total fertilizer
- total labor dollars
- blended labor rate
- fixed cost
- final profit
- standalone crossing summary for each crop
- a note that the tomato standalone marginal-cost dip appears around bed `6`, reserved for Stage 3 interpretation

## Commit order

This specification must be committed before the workbook artifact. Any clarification added during generation belongs here first, then the workbook is regenerated from the updated spec.

## Audit findings

### Audit dated 2026-09-11

1. **Hand-check audit** — Re-ran the tomato `q = 1`, `q = 10`, and `q = 20` labor figures against the workbook formulas and the Python verifier. This would have caught a dropped exponent, the m[...]
2. **Exact-carrot audit** — Updated the verifier to use `2.5 / 3` exactly and regenerated `analysis/results.md` and `analysis/results.csv`. This would have caught a rounded carrot input silentl[...]
3. **Standalone crossing audit** — Built the standalone farmer-first marginal-cost schedules so the workbook reports last-profitable beds of tomatoes `10`, mesclun `6`, and carrots `10`. This w[...]
4. **Published-versus-exact profit audit** — Compared the course's published `$42,762` against both the verifier and the workbook. Both return `$42,761.66`, the published figure to the cent. Th[...]
5. **Formula-structure audit** — Built all calculated workbook fields as formulas and configured a dedicated `Checks` sheet. This would have caught pasted values that look right once and fail a[...]
6. **Stage 3 note** — The tomato standalone marginal-cost schedule dips around bed `6` before rising again. It is recorded in the workbook summary and not interpreted here.

7. **Defects found and fixed, 2026-09-13** — Three defects surfaced in one audit pass. First, `Inputs!B6` and `Inputs!B8` held the wages as typed literals `34.72` and `17.36` rather than the de[...]

8. **Independent cross-check of intermediate marginal costs, 2026-09-13** — Recomputed the tomato standalone marginal-cost schedule outside the workbook, from the case parameters alone, and com[...]

9. **Global optimality rather than Solver path-dependence, 2026-09-13** — The standard check here is running Solver from 0/0/0 and 20/0/0 to see whether a local method gets stuck. I used a stronger check instead: `analysis/integer_search.py` enumerates every feasible integer allocation of the three crops under the bed caps, the 64-bed limit, and the 5,760-hour temporary pool, and returns 10 tomato / 30 mesclun / 20 carrot at `$42,761.66` as the global maximum. Exhaustive enumeration makes local optima moot, so path-dependence cannot hide a better answer. Worth noting that the 20/0/0 starting point is itself infeasible: 20 tomato beds alone demand 12,109 labor hours against a total pool of 6,480, so any solver starting there must first climb back into the feasible region.


