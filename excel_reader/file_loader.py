# excel_reader/file_loader.py

from openpyxl import load_workbook


def load_excel(file_path):
    """
    Load Excel workbook and return workbook object.
    """

    workbook = load_workbook(file_path)

    return workbook