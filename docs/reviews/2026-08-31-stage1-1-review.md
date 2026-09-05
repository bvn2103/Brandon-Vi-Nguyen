<!-- PR TARGET: https://github.com/bvn2103/Brandon-Vi-Nguyen | Stage 1.1 -->
# Stage 1.1 review — engagement brief

**Brief:** [`docs/briefs/perfect-competition-brief.md`](https://github.com/bvn2103/Brandon-Vi-Nguyen/blob/main/docs/briefs/perfect-competition-brief.md)

> Re-graded 2026-09-04 against your fix of this morning. You have been reviewed on this before. You corrected both arithmetic errors, and correcting the second one made you change your prediction — which is the response I was hoping for and not the one I expected.

| Criterion | Where it stands |
|---|---|
| Problem restated in your own voice | Tightened. The case is all here and accurate, the hour conversions are right, and the season is stated as planted once. What is still open is that the crop parameters are a list rather than a reading of them, and you still do not say what it costs the farm to get this wrong. |
| Hypothesis names a specific mix | 12 tomato, 20 mesclun, 20 carrot, 52 beds planted and 12 fallow with the fallow beds explained. Unchanged in form and much better grounded — the 12 now comes from an argument rather than from the cap. |
| Economic mechanism | This is where the movement is. The labor pool is right — 720 + 5,760 = 6,480 — and the tomato arithmetic is right: 90 x 20 x 1.1^20 is about 12,110 hours, which is what you now write. And your conclusion followed the corrected arithmetic instead of surviving it: you moved tomatoes from the cap to roughly 12, at the point where marginal labor cost meets marginal revenue. What is still open is a small inconsistency — the 12 is justified partly as "leaving insufficient budget for other crops," which is a ceiling argument, and your own falsification section then says correctly that the ceiling never binds. Pick the marginal-cost story; it is the one you believe. |
| Falsifiability and process | Four conditions, each naming a number and the specific input it would indict, and the fourth is now the sharpest thing in the brief: "The labor pool of 6,480 hours is never exhausted at the optimum; the binding constraint is marginal cost per bed, not total hours available." That is the cost-driver-versus-binding-constraint distinction, stated before the model runs. What is still open is a tolerance on the thresholds. |

### You changed the prediction rather than the argument, and that is the harder move

The last review pointed out that your own arithmetic said 20 tomato beds could not be staffed while your hypothesis planted 20 of them. There were two ways out. You could soften the mechanism until it stopped contradicting the prediction, or you could keep the mechanism and move the prediction.

You moved the prediction, to about 12, and wrote the reason into the frontmatter: labor escalation, not the hour ceiling, determines where a crop stops. Almost everyone takes the other route, because editing a sentence feels smaller than editing a number.

The distinction you landed on is the one this case is built to teach. Labor never actually runs out at the answer — 6,480 hours are available and the optimum uses about 5,277. The bed that stops being worth planting stops because the hour that plants it costs more than the bed returns, not because there are no hours left. Two people in this cohort have written that down and you are one of them.

### The one inconsistency left, and it is one clause

Your predicted-allocation bullet says tomatoes stop at 12 because escalation costs become prohibitive, "leaving insufficient budget for other crops and approaching the marginal revenue limit." Those are two different reasons and only the second is yours.

"Insufficient budget for other crops" is a capacity argument — it says tomatoes stop because they would crowd out carrots and mesclun. Your falsification section says explicitly that capacity never binds. Drop the clause and the brief is internally airtight.

### Stage 1.2 is due 6 september

Your capabilities/marginal-analysis/spec.md is a 35-byte stub and you have promised an analysis file showing the full integer search. That search is a good idea and it is also the thing that will tell you whether 12 was right.

Write the specification first and commit it before the workbook — the commit order is graded, and your history so far has been clean on that. Put the labor function in with the exponent on q, and add two hand-checks: one tomato bed is 99 hours exactly, ten tomato beds are 2,334.37. Everything you have got wrong so far in this case has been arithmetic that a hand-check would have caught, and everything you have got right has been structural.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error.*

*Your score and the per-criterion breakdown are in your Lamaku comment, not here — this repository is public.*

— Adam
