from openpyxl import load_workbook
wb = load_workbook("sample_formula.xlsx")
ws = wb.active

for row in ws.values:
    for cell in ws.values:
        print(cell)
