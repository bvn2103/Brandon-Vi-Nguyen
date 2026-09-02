<!-- PR TARGET: https://github.com/bvn2103/Brandon-Vi-Nguyen | Stage 1.1 (2.5 pts) -->
# Stage 1.1 review — engagement brief · **37 / 100** (F) · 0.93 / 2.5 pts

**Brief:** [`docs/briefs/perfect-competition-brief.md`](https://github.com/bvn2103/Brandon-Vi-Nguyen/blob/main/docs/briefs/perfect-competition-brief.md)

> Graded 2026-08-31. I am not entering this score. There is a fully written brief in your repository and the mechanics in it are among the most accurate anyone produced — but it is about a different case, and the numbers this one turns on are not in it. That reads to me as a misread assignment rather than weak work, so this is a hold and a re-grade, not a grade. Fix the subject and I will re-score it with no penalty for the delay.

| Criterion | Earned | Notes |
|---|---|---|
| Problem restated in your own voice | 8 / 30 | Well written, and not this problem. The case is a 64-bed market garden choosing how many beds of tomatoes, carrots, and mesclun to plant. Your brief is a one-acre mangosteen orchard allocating 88 trees across three cultivation intensities. The farmer, the beds, the three crops, the prices, the caps, and the labor rates do not appear anywhere. The eight points are for the structure and the framing, which are correct — you have a decision, a horizon, a fixed cost, and a constraint, and you state them cleanly. |
| Hypothesis names a specific mix | 5 / 25 | 44 ultra-premium, 22 high-intensity, 22 standard. It is specific and it is committed, which is why it is not zero. But it allocates the wrong quantity across categories that do not exist in the case, so there is nothing for a model of this case to confirm or contradict. Stage 3 compares your prediction against your workbook; this prediction and that workbook are about different things. |
| Economic mechanism | 12 / 25 | The mechanism is right and you transcribed the engine of the case exactly: "Labor per tree follows: q x hours-per-week-per-tree x 36 x (1 + rate)^q." That formula, with the exponent on q rather than a flat multiplier, is the single thing most likely to be got wrong in this case, and you have it correct. You also have the two consequences right — that compounding applies per additional unit, and that fixed costs are sunk so decisions follow marginal profit. What stops this being 20 or better is that no quantity is ever supplied. "Ultra-premium trees have the lowest per-tree escalation" is asserted with no rate behind it, and "prices per intensity level are fixed and known" is stated without ever saying what they are. The formula is exact; nothing is put into it. |
| Falsifiability and process | 12 / 20 | Structurally the best falsification section of any brief scoring under 80 in this cohort. Three checks, each naming a specific observation and the assumption it would break — "If ultra-premium cannot reach 44 trees due to labor limits, then total labor availability or per-tree labor is overestimated" — and a closing line tying all three back to the binding constraint. That is what the section is supposed to do, and nine of the eighteen graded briefs still have the circular version instead. The deduction is only that it falsifies claims about an orchard that does not exist. Your prompt log records the critique session and the commit is dated before any modeling, which is the right sequence and is credited. |
| **Final** | **37 / 100** | earned on merit |

### What i think happened, and why this is a hold rather than a grade

You scored 100 on Stage 0. Your repository is one of the cleanest in the cohort. This brief is organized, edited, and internally consistent, and it reproduces the case's labor function more accurately than most of the briefs that are about the right farm. Nothing about it looks like someone who did not do the work.

What it looks like is a brief written against a scenario that got substituted somewhere early — possibly a worked example an assistant generated to illustrate the method, which then became the subject. Your prompt log confirms the mangosteen version was there from the first commit on 28 August and was refined rather than reconsidered on the 29th.

So I am not entering 37. It would describe the effort inaccurately and it would be the wrong signal about what to fix.

### What to actually do, and it is less work than it looks

Do not start over. The skeleton you have is good and the parts that transfer are the hard parts.

The case is on the Stage 1 page. The farm has 64 beds, in four plots of 16, and a 36-week season. Fixed costs are $20,000. The farmer earns $50,000 and spends half her time in the field — 720 field hours at an implied $34.72 an hour. Up to four temporary workers are available at $25,000 each for up to 1,440 hours, an implied $17.36 an hour. Three crops:

- Tomatoes — max 20 beds, $8,800 per bed, 2.50 labor hours per bed per week, $880 fertilizer per bed, 10.00% diminishing returns per bed

- Carrots — max 20 beds, $2,094 per bed, 0.833 labor hours per bed per week, $440 fertilizer per bed, 2.50% per bed

- Mesclun — max 30 beds, $2,700 per bed, 1.25 labor hours per bed per week, $880 fertilizer per bed, 1.25% per bed

The labor function is the one you already wrote, with beds in place of trees. The caps sum to 70 against 64 beds, so not all three can be maxed and something has to give — that tension is the decision.

Your three falsification checks map across almost unchanged: substitute the crop for the intensity tier and the cap for the tree count and they still work. Your mechanism paragraph transfers as written. What has to be rebuilt is the problem statement and the hypothesis, and the hypothesis now has real rates to reason from, which will make it stronger than the one you have.

Say the word when it is committed and I will re-grade it. No penalty for the turnaround.

### One thing worth saying

The reason I am spending this many words on a brief about the wrong subject is that the thinking in it is good. You wrote a correct compounding-labor model from a standing start and then wrote falsification conditions that could actually fail — which is the thing three quarters of this cohort has not managed on the second attempt.

The failure here is a verification failure, not an analytical one: you did not check the subject against the source. That is worth noticing now rather than in Stage 1.2, where the same habit produces a workbook that is internally perfect and answers a question nobody asked.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief, this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule for this stage: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error — Stage 3 asks you to explain the gap, and a brief quietly edited to be right afterwards has nothing left to explain.*

— Adam
