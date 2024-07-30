import os
import win32com.client  # pip install pywin32

class ExcelAutomation:
    def __init__(self, file_path):
        self.file_path = file_path
        self.excel_app = win32com.client.Dispatch("Excel.Application")
        self.workbook = None
        self.worksheet = None

    def open_workbook(self):
        if not os.path.exists(self.file_path):
            print(f"Error: File '{self.file_path}' not found.")
            return
        try:
            self.workbook = self.excel_app.Workbooks.Open(self.file_path)
            self.worksheet = self.workbook.Worksheets(1)
        except Exception as e:
            print(f"Error opening workbook: {e}")

    def insert_data(self, start_row=702, start_col=1, *data):
        try:
            for offset, value in enumerate(data):
                row = start_row
                col = start_col + offset
                print(f"Inserting '{value}' into cell ({row}, {col})")
                self.worksheet.Cells(row, col).Value = value
        except Exception as e:
            print(f"Error inserting data: {e}")

    def update_data(self, cell, data):
        try:
            self.worksheet.Range(cell).Value = data
        except Exception as e:
            print(f"Error updating data: {e}")

    def delete_data(self, row):
        try:
            self.worksheet.Rows(row).Delete()
        except Exception as e:
            print(f"Error deleting data: {e}")

    def save_data(self):
        try:
            self.workbook.Save()
        except Exception as e:
            print(f"Error saving workbook: {e}")

    def close_data(self):
        try:
            self.excel_app.Quit()
        except Exception as e:
            print(f"Error closing Excel application: {e}")

# Usage
file_path = "d:/python course/Financial Sample.xlsx"
ex = ExcelAutomation(file_path)
ex.open_workbook()
ex.insert_data("Private", "Confidential", "Public", "Restricted", "Internal", "Secret")
# ex.update_data("A702", "")
# ex.delete_data(702)
ex.save_data()
ex.close_data()
