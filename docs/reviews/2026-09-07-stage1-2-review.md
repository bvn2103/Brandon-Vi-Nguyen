<!-- PR TARGET: https://github.com/bvn2103/Brandon-Vi-Nguyen | Stage 1.2 -->
# Stage 1.2 review — spec, build, audit

**Spec:** [`capabilities/marginal-analysis/spec.md`](https://github.com/bvn2103/Brandon-Vi-Nguyen/blob/main/capabilities/marginal-analysis/spec.md)

> Graded 2026-09-07 against the specification and analysis you committed on 4 September. Your model is correct — I ran your script and it returns the right allocation — but the stage's deliverable is an Excel workbook and there is not one in your repository.

| Criterion | Where it stands |
|---|---|
| Spec completeness — inputs, structure, calculation flow | The economics half of this document is genuinely good. The labor function is stated precisely, discrete marginal labor is defined explicitly as Labor(q) minus Labor(q-1) rather than left to be guessed at, every crop parameter is present, and the search domain is written as inequalities a builder can implement directly. The best line in it is the accounting choice: you charge the farmer's hours as an opportunity cost at $34.72 even though they are not paid out of pocket, and you say so and defend it. Almost no specification in this cohort states an accounting convention at all. What is missing is everything about the artifact — no sheet structure, no outputs section, no rounding or display conventions, and no statement of what the workbook must contain, which matters because the workbook is what the document is supposed to be a contract for. |
| Spec validation rules | Three hand-checks with exact expected values — 99.0 hours at one tomato bed, 2,334.37 at ten, and about 12,110 at twenty — plus a numeric tolerance, and they are implemented as asserts that actually run and would actually stop the script. That is real validation and better than a list of intentions. What is absent is everything around it: no constraint checks on the result, no rule about formula errors, no cross-check against an independent source, and nothing that tests the search itself. The twenty-bed check is a good instinct — you added it specifically to catch the miscalculation from your brief. |
| Workbook satisfies the contract | There is no workbook. The stage names capabilities/marginal-analysis/model.xlsx and that path does not exist. What exists is analysis/integer_search.py, and it is a correct, reproducible, exhaustive enumeration: I ran it and it returns 10 tomato, 30 mesclun and 20 carrot at $42,775.16, which is the right allocation and within about $13 of the published profit. The $13 is entirely the rounded $34.72 and $17.36 rates and carrot hours at 0.833 rather than 2.5/3. As a model it satisfies the calculation contract, and it gets partial credit for that. It is not the deliverable, and the reason is not bureaucratic: the workbook is the artifact a business reader can open, trace and audit cell by cell, and building one is the skill this stage exists to teach. |
| Audit note | analysis/results.md records the hand-checks and reconciles revenue, fertilizer, labor and fixed costs line by line, which is a real reconciliation. But there are no audit findings in the sense the stage means — nothing saying what a check would have caught, what you tested, or what changed as a result. And the file and the script do not agree with each other, which is worth reconciling before it becomes a habit. |

> Held rather than entered. Nothing is recorded against you while this stage is still open.

### The analysis is right and it is in the wrong tool

I want to be clear about what you have, because it is more than the score suggests. You wrote a specification, committed it, then wrote an exhaustive integer search over the full feasible grid — every combination of tomato, mesclun and carrot beds inside the caps and the 64-bed limit, with infeasible labor allocations excluded — and it returns the profit-maximising mix. That is a proof of global optimality, not a solver's opinion, and it is the strongest way to answer this question.

The gap is the artifact. The deliverable is capabilities/marginal-analysis/model.xlsx, and the reason it is a workbook is that the audience for this work opens spreadsheets. A reviewer can click a cell in Excel and see the formula that produced it. Nobody outside a technical team will read your Python to check your carrot cost.

You are not starting over. Your script is the specification of the workbook, already written and already tested — the sheets, the inputs, the labor function, the farmer-first allocation and the profit roll-up all exist in it. Rebuilding it in Excel with named ranges and a Solver setup is a transcription with a Solver run on the end, not a new analysis.

### The results file and the script disagree

I ran the committed script from a clean copy of the repository. It prints total labor hours of 5,276.82 and a profit of $42,775.16, and it writes its own analysis/results.md with a top-ten table in profit order.

The results.md that is committed says 5,276.91 hours and $42,773.64, gives carrot labor as 982.88 hours where the script computes 982.78, and carries a five-line "top candidate allocations" list that is not in profit order — it puts twelve tomato beds at about $40,258 above eleven at about $41,668, and the script says eleven beds is $42,184.98.

None of this changes your answer, which is the same either way. But the file opens with the line that it is generated by running the integer-search analysis, and it is not the file the script produces. If you hand-wrote the summary after running the script, say so in the file — a hand-written summary of a computed result is completely legitimate, and labelling it protects you. If you think I have this wrong, tell me in the thread and I will recheck.

The cheap fix is to let the script own the file: run it from the repository root and commit whatever it writes, with any commentary added underneath a heading that says it is commentary.

### What to do, in order

- Build capabilities/marginal-analysis/model.xlsx. Inputs on their own sheet as values with units and sources; a labor and cost sheet; a marginal-cost schedule per crop; the decision cells and Solver setup; a checks sheet. Every calculated cell a formula referencing named inputs.

- Use 2.5/3 for carrot hours and 50000/1440 and 25000/1440 for the two rates rather than the rounded display figures, and your $13 disappears.

- Move your three hand-checks onto the checks sheet as live formulas with PASS or FAIL, and add constraint checks — beds within caps, total beds at or under 64, temporary hours within the pool.

- Extend the specification with a Structure section naming those sheets and an Outputs section naming what the model must report, then write the audit findings against the finished workbook.

### One repository note

You moved BIO.md and RESUME.md into profile/ on 6 September. The reorganisation is sensible and the redirect notes are a thoughtful touch, but RESUME.md at the repository root is one of the fourteen canonical paths the portfolio checklist reads, and a redirect note is not the file.

Nothing is being taken away from you for it — your Stage 0 score stands and scores in this course do not go down. It is worth knowing because the same checklist is read again at the end of the term. Keeping a real RESUME.md at the root, with profile/ holding the longer material, satisfies both.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your spec into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then correct the spec, not the workbook.** This is the rule that makes the stage work: when a check fails, you fix the specification and regenerate, so the document keeps describing what was actually built.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*Your score and the per-criterion breakdown are in your Lamaku comment, not here — this repository is public.*

— Adam
