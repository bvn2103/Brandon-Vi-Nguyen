# Marginal Analysis Results Audit

## Precision and Validation Correction (Professor Feedback Resolution)

This workbook/model now uses **exact implied rates** and strict audit checks.

### Canonical values

- **Exact model profit (unrounded):** **$42,761.66**
- **Published rounded reference:** **$42,762**

### What was corrected

1. Wage inputs are now exact implied formulas (not rounded display values):
   - Farmer hourly rate = `50000/1440`
   - Temporary labor hourly rate = `25000/1440`
2. Carrot base hours remains exact:
   - `2.5/3`
3. Checks sheet acceptance criteria tightened so discrepancies are not masked by wide tolerances.
4. Labeling corrected so **exact** vs **published rounded** are not inverted.

### Why this matters

A wide tolerance can hide real model/input precision errors. Audit checks should reflect the intended rounding level:

- use cent-level checks when two quantities should match mathematically;
- use explicit rounding comparisons only when validating against published rounded numbers.

### Verification intent

- The exact target is the model value.
- The published figure is a rounded print reference.
- Both are tracked, but they are not interchangeable.
