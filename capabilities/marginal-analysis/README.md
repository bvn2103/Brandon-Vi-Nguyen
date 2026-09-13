# Marginal Analysis

This capability contains the Stage 2 Perfect Competition workbook deliverable and the specification it was built from.

- `spec.md` — the build contract and audit record
- `model.xlsx` — the workbook deliverable
- `results.md` — precision and validation audit notes (exact vs published rounded checks)

The workbook is the primary deliverable. The Python verifier at `analysis/integer_search.py` is the independent exhaustive-search check used to confirm the workbook’s final allocation and profit 
Audit policy: exact model values are treated as canonical; published figures are treated as rounded references and validated separately.

exercised in: **Perfect competition, 1.5-acre market garden** — [brief](../../docs/briefs/perfect-competition-brief.md) · [analysis](../../analysis/perfect-competition-analysis.md) · [memo](../../docs/decisions/perfect-competition-memo.md)
