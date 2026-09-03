<!-- PR TARGET: https://github.com/bvn2103/Brandon-Vi-Nguyen | Stage 1.1 (2.5 pts) -->
# Stage 1.1 review — engagement brief · **82 / 100** (B-) · 2.05 / 2.5 pts

**Brief:** [`docs/briefs/perfect-competition-brief.md`](https://github.com/bvn2103/Brandon-Vi-Nguyen/blob/main/docs/briefs/perfect-competition-brief.md)

> Re-graded 2026-09-02 against your rewrite. The previous 37 was a hold, not a grade, because the brief was about a mangosteen orchard rather than this case. You rewrote it for the right farm and kept everything that was already good about it. As promised, there is no penalty for the delay.

| Criterion | Earned | Notes |
|---|---|---|
| Problem restated in your own voice | 26 / 30 | Up from 8. The case is all there now and it is accurate: 64 beds in four plots of 16, the 36-week season, $20,000 fixed, the farmer at $50,000 for 720 field hours, temporary workers at $25,000 for 1,440 hours each, and the three crops with prices, caps, labor hours, fertilizer, and rates. You also converted hours per bed-week into hours per bed-season — 90, 30, and 45 — which most people did not bother to do and which is what makes the labor argument checkable. Four points off because the middle of the section is the case table restated in prose, and because you never say what it costs to decide this badly. The season is planted once; that sentence belongs here. |
| Hypothesis names a specific mix | 25 / 25 | Tomatoes 20, mesclun 20, carrots 11, 51 planted and 13 fallow, with the fallow beds explained rather than left over. Three integers, all inside their caps, summing under 64. That is exactly what this criterion asks for, and stating the fallow beds as a deliberate choice is the part most people miss. |
| Economic mechanism | 14 / 25 | The engine is right and you state it correctly, exponent on q and all. Two arithmetic errors cost the points, and one of them contradicts your own prediction — see below. Up from 12 all the same, because the reasoning about why different escalation rates change the trade-off between crops as beds are added is sound and it is yours. |
| Falsifiability and process | 17 / 20 | Up from 12, and this is the strongest section of the brief. Four conditions, each with a number, each naming the specific input it would indict rather than just saying the hypothesis failed. The second — mesclun staying under 5 beds despite the low escalation rate would mean its revenue or base hours are mis-specified — is the kind of condition that tells you where to look, not just that you were wrong. Three points off because the fourth rests on the labor figure that is wrong. Committed before any modeling, canonical path. |
| **Final** | **82 / 100** | entered — hold lifted |

### The two numbers to fix, and why the second one matters most

First: the labor pool. You write "The farmer and temporary workers have fixed budgets (720 + 1,440 = 2,160 total hours)." There are up to four temporary workers at 1,440 hours each, which you say correctly two paragraphs earlier in your assumptions. The pool is 720 + 5,760 = 6,480 hours. Your fourth falsification condition then says the model fails "if total labor demand exceeds 2,160 hours even when hiring all four temporary workers to their 1,440-hour cap," which contradicts itself inside one sentence — four workers at 1,440 is 5,760 on its own.

Second: "planting 20 tomato beds requires 90 × 20 × 1.1^20 = 5,670 hours." Run it again. 1.1 to the twentieth is about 6.7275, and 90 × 20 × 6.7275 is about 12,110 hours, not 5,670. The conclusion you draw from it — that 20 tomato beds is far beyond the labor available — is right, and it is more dramatically right than you realized.

That is the part worth sitting with. Your own arithmetic says 20 tomato beds cannot be planted, and your hypothesis puts tomatoes at 20. A brief whose mechanism argues against its own prediction is the one thing Stage 3 cannot recover from, because there is no honest way to write the comparison.

### What i would do with that, before the Solver runs

You do not need the model to fix this. You need one more line of the arithmetic you already did.

The 6,480-hour pool is the ceiling. Mesclun at 30 beds takes 30 × 1.25 × 36 × 1.0125^30, about 1,960 hours. Carrots at 20 take about 983. That is roughly 2,940 for two crops at their caps, leaving about 3,540 for tomatoes — and 90q × 1.1^q passes 3,540 hours somewhere around 12 beds. So the labor ceiling alone rules out your 20.

Then ask the sharper question, which is not about the ceiling at all: labor never actually runs out at the answer. It gets expensive. The bed that stops being worth planting is the one whose marginal hours cost more than the $8,800 it earns, and that happens before the hours are gone. Revise the tomato number to whatever that reasoning gives you and say which of the two — the ceiling or the price — you think stops the crop first. That is a real prediction and it is the one Stage 3 will be about.

### Why this is entered and what it reflects

82 is a real grade on a real brief. The 37 was never a judgment about your work — it was a subject mismatch, and you fixed it in two days without being asked twice.

What carried over is worth naming: the labor function with the exponent on q was correct in the mangosteen version and it is correct here, and it is still the single most commonly mangled thing in this case. Your falsification section was the best one under 80 in the cohort when it was about the wrong farm, and it is now among the better ones about the right farm. The rewrite kept the parts that were good rather than starting over, which is the right instinct.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief, this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule for this stage: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error — Stage 3 asks you to explain the gap, and a brief quietly edited to be right afterwards has nothing left to explain.*

— Adam
