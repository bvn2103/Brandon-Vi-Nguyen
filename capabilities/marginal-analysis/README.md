# Marginal Analysis

This capability contains the Stage 2 Perfect Competition workbook deliverable and the specification it was built from.

- `spec.md` — the build contract and audit record
- `model.xlsx` — the workbook deliverable
- `results.md` — precision and validation audit notes (exact vs published rounded checks)
- `auditable_workbook_exactness.py` — idempotent workbook-fix script for exact implied rates and strict checks

The workbook is the primary deliverable. The Python verifier at `analysis/integer_search.py` is the independent exhaustive-search check used to confirm the workbook’s final allocation and profit.
Audit policy: exact model values are treated as canonical; published figures are treated as rounded references and validated separately.

exercised in: Perfect Competition Stage 2 spec → build → audit workflow
