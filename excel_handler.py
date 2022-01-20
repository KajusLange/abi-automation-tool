# excel_handler.py
from openpyxl import load_workbook

wb = load_workbook(filename="template_excel.xlsx")
ws = wb.active
