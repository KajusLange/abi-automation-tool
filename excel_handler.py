# excel_handler.py
from openpyxl import load_workbook

wb = load_workbook(filename="template_excel.xlsx")
ws = wb.active


def create_student_xlsx(student):
    # student info
    ws["B70"] = student.klasse
    ws["D70"] = student.name
    ws["G70"] = student.vorname
    ws["D73"] = student.pb
    ws["G73"] = student.wdh

    # final step
    wb.save(filename=f"{student.klasse}_{student.name}_{student.vorname}")


def adjust_row_count(groups):
    ws.row_dimensions.group(12 + groups[0], 21, hidden=True)
    ws.row_dimensions.group(25 + groups[1], 34, hidden=True)
    ws.row_dimensions.group(38 + groups[2], 47, hidden=True)
    ws.row_dimensions.group(51 + groups[3], 65, hidden=True)

    wb.save("debug.xlsx")