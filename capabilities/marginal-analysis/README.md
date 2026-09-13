# Marginal Analysis

This capability contains the Stage 2 Perfect Competition workbook deliverable and the specification it was built from.

- `spec.md` — the build contract and audit record
- `model.xlsx` — the workbook deliverable
- `results.md` — precision and validation audit notes (exact vs published rounded checks)

The workbook is the primary deliverable. The Python verifier at `analysis/integer_search.py` is an independent exhaustive-search check that confirms the workbook's final allocation and profit. It never writes to the workbook: a verifier that edits the artifact it verifies is no longer a check.

exercised in: **Perfect competition, 1.5-acre market garden** — [brief](../../docs/briefs/perfect-competition-brief.md) · [analysis](../../analysis/perfect-competition-analysis.md) · [memo](../../docs/decisions/perfect-competition-memo.md)
