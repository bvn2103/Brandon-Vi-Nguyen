Reply to PR: verification fix and next steps

I corrected the labor-pool accounting and added the marginal-analysis specification and an integer-search analysis script.

Summary of verification fixes:
- Corrected combined labor pool to 6,480 hours (720 farmer + 5,760 temp).
- Recomputed 20 tomato beds labor requirement: ~12,110 hours (hand-check in spec).
- Changed the hypothesis justification to the marginal-cost interpretation: the optimal stopping point is where marginal labor cost per bed exceeds marginal revenue, not a capacity ceiling.

Files added:
- `capabilities/marginal-analysis/spec.md` — specification with labor function and hand-checks.
- `analysis/integer_search.py` — Python integer-search script implementing the spec and enumerating allocations.
- `analysis/results.md` — instructions and placeholder for script output.

Next steps I can do on request:
- Run the analysis script and commit the actual numeric results into `analysis/results.md`.
- Add plots or a CSV table of all feasible allocations.
- Open or comment on the PR with this reply text (I can create a PR comment if you want me to; ask and I'll add it). 

