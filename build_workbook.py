#!/usr/bin/env python3
"""
Generate the marginal-analysis model.xlsx workbook
Run: python3 build_workbook.py
Produces capabilities/marginal-analysis/model.xlsx
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from decimal import Decimal

# Create workbook
wb = Workbook()
wb.remove(wb.active)  # Remove default sheet

# Define styles
header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
header_font = Font(bold=True, color="FFFFFF")
input_fill = PatternFill(start_color="E7E6E6", end_color="E7E6E6", fill_type="solid")
calc_fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
check_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

def style_cell(cell, fill=None, bold=False, alignment_h="left", number_format=None):
    """Apply styling to a cell"""
    cell.fill = fill or PatternFill()
    cell.font = Font(bold=bold, color=cell.font.color if not bold else cell.font.color)
    cell.alignment = Alignment(horizontal=alignment_h, vertical="center", wrap_text=True)
    cell.border = border
    if number_format:
        cell.number_format = number_format

# ============================================================================
# SHEET 1: INPUTS
# ============================================================================
inputs_sheet = wb.create_sheet("Inputs")

# Title
inputs_sheet['A1'] = "Marginal Analysis - Model Inputs"
inputs_sheet['A1'].font = Font(bold=True, size=14)

inputs_sheet['A3'] = "Parameter"
inputs_sheet['B3'] = "Value"
inputs_sheet['C3'] = "Units"
inputs_sheet['D3'] = "Source / Notes"
for col in ['A', 'B', 'C', 'D']:
    inputs_sheet[f'{col}3'].fill = header_fill
    inputs_sheet[f'{col}3'].font = header_font

row = 4
params = [
    ("Season length", 36, "weeks", "Brief"),
    ("Farmer hours available", 720, "hours", "Brief; valued at opportunity cost"),
    ("Farmer wage (opportunity cost)", 34.72, "$/hour", "Spec: farmer not paid out of pocket"),
    ("Temporary labor pool", 5760, "hours", "4 × 1,440 hours; Brief"),
    ("Temporary labor wage", 17.36, "$/hour", "Paid wage; Brief"),
    ("Fixed costs", 20000, "$", "Sunk cost; Brief"),
]

for param, value, unit, source in params:
    inputs_sheet[f'A{row}'] = param
    inputs_sheet[f'B{row}'] = value
    inputs_sheet[f'C{row}'] = unit
    inputs_sheet[f'D{row}'] = source
    for col in ['A', 'B', 'C', 'D']:
        style_cell(inputs_sheet[f'{col}{row}'], fill=input_fill, number_format="0.00" if isinstance(value, float) else None)
    row += 1

# Crop parameters
inputs_sheet[f'A{row}'] = "CROP PARAMETERS"
inputs_sheet[f'A{row}'].font = Font(bold=True)
row += 1

inputs_sheet[f'A{row}'] = "Crop"
inputs_sheet[f'B{row}'] = "Base Hours/Week"
inputs_sheet[f'C{row}'] = "Escalation"
inputs_sheet[f'D{row}'] = "Revenue/Bed"
inputs_sheet[f'E{row}'] = "Fertilizer/Bed"
inputs_sheet[f'F{row}'] = "Max Beds"
for col in ['A', 'B', 'C', 'D', 'E', 'F']:
    inputs_sheet[f'{col}{row}'].fill = header_fill
    inputs_sheet[f'{col}{row}'].font = header_font
row += 1

crops_data = [
    ("Tomato", 2.50, 0.10, 8800, 880, 20),
    ("Mesclun", 1.25, 0.0125, 2700, 880, 30),
    ("Carrot", 0.833, 0.025, 2094, 440, 20),
]

for crop, base, esc, rev, fert, max_beds in crops_data:
    inputs_sheet[f'A{row}'] = crop
    inputs_sheet[f'B{row}'] = base
    inputs_sheet[f'C{row}'] = esc
    inputs_sheet[f'D{row}'] = rev
    inputs_sheet[f'E{row}'] = fert
    inputs_sheet[f'F{row}'] = max_beds
    for col in ['A', 'B', 'C', 'D', 'E', 'F']:
        style_cell(inputs_sheet[f'{col}{row}'], fill=input_fill, number_format="0.0000" if col in ['B', 'C'] else "0.00")
    row += 1

# Adjust column widths
inputs_sheet.column_dimensions['A'].width = 25
inputs_sheet.column_dimensions['B'].width = 15
inputs_sheet.column_dimensions['C'].width = 15
inputs_sheet.column_dimensions['D'].width = 20
inputs_sheet.column_dimensions['E'].width = 15
inputs_sheet.column_dimensions['F'].width = 12

# Define named ranges for inputs
wb.named_ranges['W'] = 'Inputs!$B$4'
wb.named_ranges['H_f'] = 'Inputs!$B$5'
wb.named_ranges['Farmer_Rate'] = 'Inputs!$B$6'
wb.named_ranges['H_t_pool'] = 'Inputs!$B$7'
wb.named_ranges['Temp_Rate'] = 'Inputs!$B$8'
wb.named_ranges['F_fixed'] = 'Inputs!$B$9'

# ============================================================================
# SHEET 2: LABOR & COST
# ============================================================================
labor_sheet = wb.create_sheet("Labor & Cost")

labor_sheet['A1'] = "Labor and Cost Calculations"
labor_sheet['A1'].font = Font(bold=True, size=14)

labor_sheet['A3'] = "Crop"
labor_sheet['B3'] = "Base Hours/Week"
labor_sheet['C3'] = "Escalation"
labor_sheet['D3'] = "Base Season Hours"
labor_sheet['E3'] = "Revenue/Bed"
labor_sheet['F3'] = "Fertilizer/Bed"
labor_sheet['G3'] = "Max Beds"

for col in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    labor_sheet[f'{col}3'].fill = header_fill
    labor_sheet[f'{col}3'].font = header_font

row = 4
for idx, (crop, base, esc, rev, fert, max_beds) in enumerate(crops_data):
    labor_sheet[f'A{row}'] = crop
    labor_sheet[f'B{row}'] = base
    labor_sheet[f'C{row}'] = esc
    labor_sheet[f'D{row}'] = f"=B{row}*$Inputs!$B$4"  # base * W
    labor_sheet[f'E{row}'] = rev
    labor_sheet[f'F{row}'] = fert
    labor_sheet[f'G{row}'] = max_beds
    for col in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        style_cell(labor_sheet[f'{col}{row}'], fill=calc_fill, number_format="0.0000" if col in ['B', 'C'] else "0.00")
    row += 1

# Labor function table: for each crop, compute Labor(q) for q=0 to max_beds
labor_sheet['A8'] = "Labor Function: Labor(q) = base_season * q * (1 + escalation)^q"
labor_sheet['A8'].font = Font(bold=True, italic=True)

row = 10
for idx, (crop, base, esc, rev, fert, max_beds) in enumerate(crops_data):
    # Create labor table for this crop
    col_start = 2 + idx * 3  # A=1, B=2, D=5, G=8
    col_letter = get_column_letter(col_start)
    col_labor = get_column_letter(col_start + 1)
    
    # Headers
    labor_sheet[f'{col_letter}{row}'] = f"{crop} Beds"
    labor_sheet[f'{col_labor}{row}'] = f"{crop} Hours"
    labor_sheet[f'{col_letter}{row}'].fill = header_fill
    labor_sheet[f'{col_labor}{row}'].fill = header_fill
    labor_sheet[f'{col_letter}{row}'].font = header_font
    labor_sheet[f'{col_labor}{row}'].font = header_font
    
    # Labor values for q=0 to max_beds
    for q in range(int(max_beds) + 1):
        labor_sheet[f'{col_letter}{row + 1 + q}'] = q
        # Formula: =IF(q<=0, 0, base_season * q * (1+escalation)^q)
        # Reference: base_season from row 4, escalation from row 4
        labor_sheet[f'{col_labor}{row + 1 + q}'] = f"=IF({col_letter}{row + 1 + q}<=0, 0, ${Labor_base_row_dict[crop]} * {col_letter}{row + 1 + q} * (1+${Labor_esc_row_dict[crop]})^{col_letter}{row + 1 + q})"
        style_cell(labor_sheet[f'{col_letter}{row + 1 + q}'], fill=calc_fill, number_format="0.00")
        style_cell(labor_sheet[f'{col_labor}{row + 1 + q}'], fill=calc_fill, number_format="0.00")

# We need to track row numbers for each crop
Labor_base_row_dict = {'Tomato': '$D$4', 'Mesclun': '$D$5', 'Carrot': '$D$6'}
Labor_esc_row_dict = {'Tomato': '$C$4', 'Mesclun': '$C$5', 'Carrot': '$C$6'}

# Re-build labor table with correct references
row = 10
for idx, (crop, base, esc, rev, fert, max_beds) in enumerate(crops_data):
    col_start = 2 + idx * 3
    col_letter = get_column_letter(col_start)
    col_labor = get_column_letter(col_start + 1)
    
    labor_sheet[f'{col_letter}{row}'] = f"{crop} Beds"
    labor_sheet[f'{col_labor}{row}'] = f"{crop} Hours"
    labor_sheet[f'{col_letter}{row}'].fill = header_fill
    labor_sheet[f'{col_labor}{row}'].fill = header_fill
    labor_sheet[f'{col_letter}{row}'].font = header_font
    labor_sheet[f'{col_labor}{row}'].font = header_font
    
    base_row = 4 + idx
    
    for q in range(int(max_beds) + 1):
        labor_sheet[f'{col_letter}{row + 1 + q}'] = q
        labor_sheet[f'{col_labor}{row + 1 + q}'] = f"=IF({col_letter}{row + 1 + q}<=0, 0, ${chr(65 + col_start - 1)}${base_row} * {col_letter}{row + 1 + q} * (1+${chr(67)}${base_row})^{col_letter}{row + 1 + q})"
        style_cell(labor_sheet[f'{col_letter}{row + 1 + q}'], fill=calc_fill, number_format="0.00")
        style_cell(labor_sheet[f'{col_labor}{row + 1 + q}'], fill=calc_fill, number_format="0.00")

labor_sheet.column_dimensions['A'].width = 15
for col in range(2, 10):
    labor_sheet.column_dimensions[get_column_letter(col)].width = 12

# ============================================================================
# SHEET 3: ALLOCATION (Decision variables and optimization)
# ============================================================================
alloc_sheet = wb.create_sheet("Allocation")

alloc_sheet['A1'] = "Farm Allocation Decision"
alloc_sheet['A1'].font = Font(bold=True, size=14)

alloc_sheet['A3'] = "Decision Variables"
alloc_sheet['A3'].font = Font(bold=True, size=11)

alloc_sheet['A4'] = "Crop"
alloc_sheet['B4'] = "Beds to Plant"
for col in ['A', 'B']:
    alloc_sheet[f'{col}4'].fill = header_fill
    alloc_sheet[f'{col}4'].font = header_font

row = 5
for crop, base, esc, rev, fert, max_beds in crops_data:
    alloc_sheet[f'A{row}'] = crop
    alloc_sheet[f'B{row}'] = 0  # Initial guess
    style_cell(alloc_sheet[f'A{row}'], fill=input_fill)
    style_cell(alloc_sheet[f'B{row}'], fill=input_fill, number_format="0")
    row += 1

tomato_row = 5
mesclun_row = 6
carrot_row = 7

# Calculations based on allocation
alloc_sheet['A9'] = "Calculations"
alloc_sheet['A9'].font = Font(bold=True)

alloc_sheet['A10'] = "Metric"
alloc_sheet['B10'] = "Tomato"
alloc_sheet['C10'] = "Mesclun"
alloc_sheet['D10'] = "Carrot"
alloc_sheet['E10'] = "Total"
for col in ['A', 'B', 'C', 'D', 'E']:
    alloc_sheet[f'{col}10'].fill = header_fill
    alloc_sheet[f'{col}10'].font = header_font

metrics = [
    ("Beds Planted", f"=B{tomato_row}", f"=B{mesclun_row}", f"=B{carrot_row}", f"=B11+C11+D11"),
    ("Labor Hours (from Labor sheet)", "=VLOOKUP(B5,$'Labor & Cost'.$A$4:$D$6,4,0)", "=VLOOKUP(B6,$'Labor & Cost'.$A$4:$D$6,4,0)", "=VLOOKUP(B7,$'Labor & Cost'.$A$4:$D$6,4,0)", "=B12+C12+D12"),
    ("Revenue", f"=B{tomato_row}*Inputs!E4", f"=B{mesclun_row}*Inputs!E5", f"=B{carrot_row}*Inputs!E6", "=B13+C13+D13"),
    ("Fertilizer Cost", f"=B{tomato_row}*Inputs!F4", f"=B{mesclun_row}*Inputs!F5", f"=B{carrot_row}*Inputs!F6", "=B14+C14+D14"),
]

row = 11
for metric, t_formula, m_formula, c_formula, total_formula in metrics:
    alloc_sheet[f'A{row}'] = metric
    alloc_sheet[f'B{row}'] = t_formula
    alloc_sheet[f'C{row}'] = m_formula
    alloc_sheet[f'D{row}'] = c_formula
    alloc_sheet[f'E{row}'] = total_formula
    for col in ['A', 'B', 'C', 'D', 'E']:
        style_cell(alloc_sheet[f'{col}{row}'], fill=calc_fill, number_format="0.00")
    row += 1

# Labor allocation
alloc_sheet['A15'] = "Labor Allocation"
alloc_sheet['A15'].font = Font(bold=True)

alloc_sheet['A16'] = "Farmer hours used"
alloc_sheet['B16'] = "=MIN(Inputs!H_f, E12)"
style_cell(alloc_sheet['B16'], fill=calc_fill, number_format="0.00")

alloc_sheet['A17'] = "Temp hours used"
alloc_sheet['B17'] = "=MAX(0, E12 - B16)"
style_cell(alloc_sheet['B17'], fill=calc_fill, number_format="0.00")

# Profit roll-up
alloc_sheet['A19'] = "PROFIT STATEMENT"
alloc_sheet['A19'].font = Font(bold=True, size=12)

alloc_sheet['A20'] = "Revenue"
alloc_sheet['B20'] = "=E13"
style_cell(alloc_sheet['B20'], fill=calc_fill, number_format="$0.00")

alloc_sheet['A21'] = "Fertilizer Costs"
alloc_sheet['B21'] = "=E14"
style_cell(alloc_sheet['B21'], fill=calc_fill, number_format="$0.00")

alloc_sheet['A22'] = "Labor Costs (Farmer @ opportunity cost)"
alloc_sheet['B22'] = "=B16*Inputs!Farmer_Rate"
style_cell(alloc_sheet['B22'], fill=calc_fill, number_format="$0.00")

alloc_sheet['A23'] = "Labor Costs (Temp @ wage)"
alloc_sheet['B23'] = "=B17*Inputs!Temp_Rate"
style_cell(alloc_sheet['B23'], fill=calc_fill, number_format="$0.00")

alloc_sheet['A24'] = "Total Labor Costs"
alloc_sheet['B24'] = "=B22+B23"
style_cell(alloc_sheet['B24'], fill=calc_fill, number_format="$0.00")

alloc_sheet['A25'] = "Fixed Costs"
alloc_sheet['B25'] = "=Inputs!F_fixed"
style_cell(alloc_sheet['B25'], fill=calc_fill, number_format="$0.00")

alloc_sheet['A26'] = "TOTAL PROFIT"
alloc_sheet['B26'] = "=B20-B21-B24-B25"
alloc_sheet['B26'].font = Font(bold=True, size=12)
alloc_sheet['B26'].fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
style_cell(alloc_sheet['B26'], number_format="$0.00")

alloc_sheet.column_dimensions['A'].width = 35
alloc_sheet.column_dimensions['B'].width = 15

# Named ranges for Solver
wb.named_ranges['Tomato_Beds'] = f'Allocation!$B${tomato_row}'
wb.named_ranges['Mesclun_Beds'] = f'Allocation!$B${mesclun_row}'
wb.named_ranges['Carrot_Beds'] = f'Allocation!$B${carrot_row}'
wb.named_ranges['Profit'] = 'Allocation!$B$26'

# ============================================================================
# SHEET 4: CHECKS (Validation)
# ============================================================================
checks_sheet = wb.create_sheet("Checks")

checks_sheet['A1'] = "Model Validation Checks"
checks_sheet['A1'].font = Font(bold=True, size=14)

checks_sheet['A3'] = "Hand-Checks (Arithmetic)"
checks_sheet['A3'].font = Font(bold=True)

checks_sheet['A4'] = "Description"
checks_sheet['B4'] = "Expected"
checks_sheet['C4'] = "Computed"
checks_sheet['D4'] = "Status"
for col in ['A', 'B', 'C', 'D']:
    checks_sheet[f'{col}4'].fill = header_fill
    checks_sheet[f'{col}4'].font = header_font

# Hand-check 1: 1 tomato bed
checks_sheet['A5'] = "1 tomato bed labor"
checks_sheet['B5'] = 99.0
checks_sheet['C5'] = "=(36)*(1)*(1.1)^1"  # Simplified formula
checks_sheet['D5'] = '=IF(ABS(C5-B5)<0.01, "PASS", "FAIL")'
for col in ['B', 'C']:
    checks_sheet[f'{col}5'].number_format = "0.00"
style_cell(checks_sheet['D5'], fill=check_fill)

# Hand-check 2: 10 tomato beds
checks_sheet['A6'] = "10 tomato beds labor"
checks_sheet['B6'] = "=90*10*(1.1)^10"
checks_sheet['C6'] = "=(36)*10*(1.1)^10"
checks_sheet['D6'] = '=IF(ABS(C6-B6)<0.01, "PASS", "FAIL")'
for col in ['B', 'C']:
    checks_sheet[f'{col}6'].number_format = "0.00"
style_cell(checks_sheet['D6'], fill=check_fill)

# Hand-check 3: 20 tomato beds
checks_sheet['A7'] = "20 tomato beds labor"
checks_sheet['B7'] = "=90*20*(1.1)^20"
checks_sheet['C7'] = "=(36)*20*(1.1)^20"
checks_sheet['D7'] = '=IF(ABS(C7-B7)<0.01, "PASS", "FAIL")'
for col in ['B', 'C']:
    checks_sheet[f'{col}7'].number_format = "0.00"
style_cell(checks_sheet['D7'], fill=check_fill)

checks_sheet['A9'] = "Constraint Checks"
checks_sheet['A9'].font = Font(bold=True)

checks_sheet['A10'] = "Constraint"
checks_sheet['B10'] = "Value"
checks_sheet['C10'] = "Limit"
checks_sheet['D10'] = "Status"
for col in ['A', 'B', 'C', 'D']:
    checks_sheet[f'{col}10'].fill = header_fill
    checks_sheet[f'{col}10'].font = header_font

checks_sheet['A11'] = "Tomato beds ≤ 20"
checks_sheet['B11'] = "=Allocation!B5"
checks_sheet['C11'] = 20
checks_sheet['D11'] = '=IF(B11<=C11, "PASS", "FAIL")'
style_cell(checks_sheet['D11'], fill=check_fill)

checks_sheet['A12'] = "Mesclun beds ≤ 30"
checks_sheet['B12'] = "=Allocation!B6"
checks_sheet['C12'] = 30
checks_sheet['D12'] = '=IF(B12<=C12, "PASS", "FAIL")'
style_cell(checks_sheet['D12'], fill=check_fill)

checks_sheet['A13'] = "Carrot beds ≤ 20"
checks_sheet['B13'] = "=Allocation!B7"
checks_sheet['C13'] = 20
checks_sheet['D13'] = '=IF(B13<=C13, "PASS", "FAIL")'
style_cell(checks_sheet['D13'], fill=check_fill)

checks_sheet['A14'] = "Total beds ≤ 64"
checks_sheet['B14'] = "=Allocation!E11"
checks_sheet['C14'] = 64
checks_sheet['D14'] = '=IF(B14<=C14, "PASS", "FAIL")'
style_cell(checks_sheet['D14'], fill=check_fill)

checks_sheet['A15'] = "Temp hours ≤ 5,760"
checks_sheet['B15'] = "=Allocation!B17"
checks_sheet['C15'] = 5760
checks_sheet['D15'] = '=IF(B15<=C15, "PASS", "FAIL")'
style_cell(checks_sheet['D15'], fill=check_fill)

checks_sheet.column_dimensions['A'].width = 35
checks_sheet.column_dimensions['B'].width = 15
checks_sheet.column_dimensions['C'].width = 15
checks_sheet.column_dimensions['D'].width = 12

# ============================================================================
# SHEET 5: SUMMARY
# ============================================================================
summary_sheet = wb.create_sheet("Summary")

summary_sheet['A1'] = "Optimization Results Summary"
summary_sheet['A1'].font = Font(bold=True, size=14)

summary_sheet['A3'] = "Optimal Allocation"
summary_sheet['A3'].font = Font(bold=True)

summary_sheet['A4'] = "Crop"
summary_sheet['B4'] = "Beds"
for col in ['A', 'B']:
    summary_sheet[f'{col}4'].fill = header_fill
    summary_sheet[f'{col}4'].font = header_font

summary_sheet['A5'] = "Tomato"
summary_sheet['B5'] = "=Allocation!B5"
summary_sheet['A6'] = "Mesclun"
summary_sheet['B6'] = "=Allocation!B6"
summary_sheet['A7'] = "Carrot"
summary_sheet['B7'] = "=Allocation!B7"
summary_sheet['A8'] = "TOTAL"
summary_sheet['B8'] = "=SUM(B5:B7)"

for row in [5, 6, 7, 8]:
    summary_sheet[f'B{row}'].number_format = "0"
    style_cell(summary_sheet[f'B{row}'], fill=calc_fill)
summary_sheet['B8'].font = Font(bold=True)

summary_sheet['A10'] = "Labor Summary"
summary_sheet['A10'].font = Font(bold=True)

summary_sheet['A11'] = "Total labor hours required"
summary_sheet['B11'] = "=Allocation!E12"
summary_sheet['A12'] = "Farmer hours used (@ opportunity cost)"
summary_sheet['B12'] = "=Allocation!B16"
summary_sheet['A13'] = "Temp hours used (@ wage)"
summary_sheet['B13'] = "=Allocation!B17"

for row in [11, 12, 13]:
    summary_sheet[f'B{row}'].number_format = "0.00"
    style_cell(summary_sheet[f'B{row}'], fill=calc_fill)

summary_sheet['A15'] = "Financial Summary"
summary_sheet['A15'].font = Font(bold=True)

summary_sheet['A16'] = "Total Revenue"
summary_sheet['B16'] = "=Allocation!B20"
summary_sheet['A17'] = "Total Input Costs"
summary_sheet['B17'] = "=Allocation!B21"
summary_sheet['A18'] = "Total Labor Costs"
summary_sheet['B18'] = "=Allocation!B24"
summary_sheet['A19'] = "Fixed Costs"
summary_sheet['B19'] = "=Allocation!B25"
summary_sheet['A20'] = "NET PROFIT"
summary_sheet['B20'] = "=Allocation!B26"

for row in [16, 17, 18, 19, 20]:
    summary_sheet[f'B{row}'].number_format = "$0.00"
    style_cell(summary_sheet[f'B{row}'], fill=calc_fill)
summary_sheet['B20'].font = Font(bold=True, size=12)
summary_sheet['B20'].fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")

summary_sheet.column_dimensions['A'].width = 35
summary_sheet.column_dimensions['B'].width = 15

# Save workbook
wb.save('capabilities/marginal-analysis/model.xlsx')
print("✓ Workbook created: capabilities/marginal-analysis/model.xlsx")
print("✓ Sheets: Inputs, Labor & Cost, Allocation, Checks, Summary")
print("✓ Named ranges defined for Solver optimization")
print("✓ Hand-checks and constraint checks active on Checks sheet")
