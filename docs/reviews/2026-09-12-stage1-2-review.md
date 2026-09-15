@bvn2103

Reviewed below, criterion by criterion. This is entered.

CRITERION BY CRITERION

* **Spec completeness — inputs, structure, calculation flow** — Twenty-two inputs, each with a value, a unit and a source. The labor schedule, the standalone cost rule and the allocation roll-up are all in named-range notation with no cell addresses. **Both costing conventions are stated** — permanent-first, *and* per-crop P&L allocated at the blended rate, with the farm-level-fact sentence — and you are one of the few who then actually implemented the blended allocation in the workbook rather than only describing it. The instruction *"Do not write into the spec that marginal cost is monotone. The workbook must implement the mechanism above and let the schedule reveal the shape"* is the right way to specify a result you do not want to prejudge. Marked down because two inputs carry rounded values (below).
* **Spec validation rules** — Hand-checks at q = 1, 10 and 20 quoted to twelve decimals, published reference checks, integrity checks, and an exact cross-check against your own Python. All committed before the build. What costs you here is not coverage but calibration: the acceptance criterion itself enshrines a figure that is $6.67 wrong, and the tolerance on the published check figure was set wide enough to let it through. See below.
* **Workbook satisfies the contract** — Five sheets exactly as specified, 521 formulas, zero error cells, a live `Checks` sheet with real PASS/FAIL formulas rather than asserted text, and the Solver setup documented for a reviewer to rerun. The mix is right at 10 / 20 / 30 and every labor-hour figure is exact. Profit is not: $42,768.33 against $42,761.66. Decision variables also ship preloaded at the optimum rather than demonstrating a run.
* **Audit note** — Full marks. Six numbered findings, every one of them ending in what the check would have caught — which is the exact discipline the criterion asks for and which most people substitute with "checked, correct." Finding 2, regenerating `results.md` and `results.csv` after switching to the exact carrot fraction, is a real defect caught and closed.

**THE WORKBOOK IS REAL NOW, AND IT IS A GOOD ONE**

The hold last sweep was not about your economics — those were already right. It was that your model
lived in `integer_search.py` and `results.md`, and the stage asks for an auditable workbook. That is
resolved, and not minimally: `Inputs`, `Labor & Cost`, `Allocation`, `Checks`, `Summary`, exactly the
five sheets your spec named, with the `Checks` sheet holding live comparison formulas that recompute
rather than asserting a verdict in text.

Your hand-checks are exact. I recomputed both:

| Check | Yours | Mine |
|---|---|---|
| Tomato labor, q = 10 | 2,334.368214090002 | 2,334.36821409 |
| Tomato labor, q = 20 | 12,109.4999087861 | 12,109.49990879 |

And your standalone crossings — tomatoes 10, mesclun 6, carrots 10 — are all three correct against my
schedules, using your own `NET_CONTRIBUTION = price − fertilizer` convention, which is an equivalent
and perfectly legitimate way to frame the comparison.

**YOU CAUGHT ONE ROUNDING TRAP AND CANONIZED THE OTHER TWO**

This is the finding, and it is worth sitting with because your method was right and you stopped one
step early.

For carrots you wrote exactly the right instruction:

> `Carrot_Base_Hours_Per_Week` | `2.5 / 3` exactly | **Use the exact fraction, not a rounded display value**

You understood that a printed number can be a rounded display of a ratio. Then, four rows up:

> `Farmer_Hourly_Rate` | 34.72 | $/hour | Opportunity cost from case scenario
> `Temp_Hourly_Rate` | 17.36 | $/hour | Temporary labor wage from case scenario

Those two are rounded displays as well — of `50,000 / 1,440` = $34.7222… and `25,000 / 1,440` =
$17.3611…. The case calls them *implied* rates for exactly that reason.

I isolated each variant against my model, at 10 / 20 / 30:

| Inputs | Profit |
|---|---|
| All three exact | **$42,761.66** |
| **Wages rounded, carrots exact** | **$42,768.33** ← your workbook |
| Carrot hours rounded only | $42,768.49 |
| All three rounded | $42,775.16 |

Your workbook returns **$42,768.3282562054**. That is the wages-rounded variant to ten decimal places.
Your total labor dollars read $104,111.67 against a true $104,118.34 — $6.67 light, all of it in those
two cells. Apply your own carrot rule to the two wages and the gap goes to zero.

**THE PART THAT MATTERS MORE THAN THE $6.67**

You did not merely carry the error — you made it the standard:

> **Exact verification checks:** Exact script profit is `$42,768.33` when rounded to cents
> **Published-versus-exact profit audit** — Kept the course's published `$42,762` figure as an
> approximate acceptance check and the exact script profit `$42,768.33` as the precise verifier.

That has it the wrong way round. $42,761.66 is the exact figure; $42,762 is it, rounded for print.
$42,768.33 is your model's output carrying two rounded inputs. You labelled the approximation "exact"
and the exact value "approximate," and then built your acceptance criteria on top of that.

And your `Checks` sheet shows precisely how it survived:

> `D12: =IF(ABS(C12-B12)<=10,"PASS","FAIL")` → PASS

A ±$10 tolerance against a $6.67 discrepancy. The check could not have failed. Compare with `D11`,
where you demanded agreement within a cent — against your own figure, so it passed too. Between them,
neither check could report the problem.

This is worth more to you than the dollars. A tolerance is a claim about how much error you are
willing to not notice, and the moment you pick one wide enough to cover the gap you are worried about,
the check stops being a check. You already know the discipline — your audit finding 4 says the
published figure is there to catch "a workbook that matched a rounded reference while still disagreeing
with the actual model," which is the right idea pointed at the wrong number.

**WHERE THIS LEAVES YOU**

This is entered and the hold is lifted. The workbook is genuinely good, the audit discipline is full marks, and
the economics were never in question. Two cells and one re-labelled acceptance criterion stand between
this and the mid-90s.

---

**How to reply to this review.** Comment on this pull request with what you changed, or push another
commit to `main` and say so here. If you disagree with something, say that too — a disagreement you
can support is worth more to me than a correction you make because I asked. This stage is still open.

