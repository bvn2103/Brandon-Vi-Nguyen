#!/usr/bin/env python3
"""Patch workbook precision/validation settings for marginal-analysis model.

This script updates capabilities/marginal-analysis/model.xlsx to:
- Use exact implied wage formulas (50000/1440 and 25000/1440)
- Keep carrot base hours exact as 2.5/3
- Tighten acceptance checks to cent-level tolerance where values should match
- Correct exact vs published labels/targets

It is designed to be idempotent and safe to re-run.
"""

from __future__ import annotations

from pathlib import Path
from openpyxl import load_workbook


ROOT = Path(__file__).resolve().parents[2]
WORKBOOK_PATH = ROOT / "capabilities" / "marginal-analysis" / "model.xlsx"


def set_if_different(cell, value):
    if cell.value != value:
        cell.value = value


def main() -> int:
    if not WORKBOOK_PATH.exists():
        raise FileNotFoundError(f"Workbook not found: {WORKBOOK_PATH}")

    wb = load_workbook(WORKBOOK_PATH)

    # --- Inputs sheet updates ---
    if "Inputs" in wb.sheetnames:
        ws = wb["Inputs"]
        # Expected layout from existing workbook spec.
        # B5: Farmer_Hourly_Rate
        # B6: Temp_Hourly_Rate
        # B10: Carrot_Base_Hours_Per_Week (exact fraction)
        set_if_different(ws["B5"], "=50000/1440")
        set_if_different(ws["B6"], "=25000/1440")
        set_if_different(ws["B10"], "=2.5/3")

    # --- Checks sheet updates ---
    if "Checks" in wb.sheetnames:
        ws = wb["Checks"]

        # Canonical labels/targets. These cells are chosen to match the existing workbook
        # discussed in review (D11/D12 checks and nearby summary rows).
        set_if_different(ws["A9"], "Exact model target profit")
        set_if_different(ws["B9"], 42761.66)

        set_if_different(ws["A10"], "Published rounded reference")
        set_if_different(ws["B10"], 42762)

        # Tighten tolerance checks.
        # D11: exact comparison should be within 1 cent.
        set_if_different(ws["D11"], '=IF(ABS(C11-B11)<=0.01,"PASS","FAIL")')

        # D12 previously allowed +/-10; tighten to cent-level unless intentionally rounding.
        # Here we enforce cent-level match as requested by professor feedback.
        set_if_different(ws["D12"], '=IF(ABS(C12-B12)<=0.01,"PASS","FAIL")')

    # --- Summary sheet text corrections (best effort) ---
    if "Summary" in wb.sheetnames:
        ws = wb["Summary"]
        # Update canonical narrative anchors if present in common cells.
        replacements = {
            "A2": "Exact profit (unrounded model):",
            "B2": 42761.66,
            "A3": "Published rounded reference:",
            "B3": 42762,
        }
        for ref, val in replacements.items():
            set_if_different(ws[ref], val)

    wb.save(WORKBOOK_PATH)
    print(f"Updated workbook: {WORKBOOK_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
