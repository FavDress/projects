from openpyxl import Workbook
import csv
from pathlib import Path


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """

    if (Path(xlsx_path).suffix != ".xlsx"):
        raise ValueError("Input file must be a XLSX file")

    if (Path(csv_path).suffix != ".csv"):
        raise ValueError("Output file must be a CSV file")
    
    if Path(csv_path).exists() is False:
        raise FileNotFoundError("File not found")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    
    data = []
    with open(csv_path, "r", encoding="utf-8") as iFile:
        rd = csv.reader(iFile)
        for row in rd:
            data.append(row)

    if len(data) == 0:
        wb.save(xlsx_path)
        raise ValueError("Input CSV file is empty")

    for row in data:
        ws.append(row)

    for col in ws.columns:
        length = max(len(str(cell.value)) for cell in col)
        ws.column_dimensions[col[0].column_letter].width = max(length, 8)
    
    wb.save(xlsx_path)