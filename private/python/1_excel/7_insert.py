from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

ws.insert_rows(8,5)

wb.save("samlple_insert.xlsx")