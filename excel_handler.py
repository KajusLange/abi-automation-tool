# excel_handler.py
from openpyxl import load_workbook

wb = load_workbook(filename="template_excel.xlsx")
ws = wb.active


def adjust_row_count(g_one, g_two, g_three, g_four):
    ws.row_dimensions.group(12 + g_one, 21, hidden=True)
    ws.row_dimensions.group(25 + g_two, 34, hidden=True)
    ws.row_dimensions.group(38 + g_three, 47, hidden=True)
    ws.row_dimensions.group(51 + g_four, 65, hidden=True)
