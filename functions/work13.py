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

    def insert_data(self, start_row, start_col, columns_per_row=10, *data):
        try:
            start_row = int(start_row)
            start_col = int(start_col)
        except ValueError:
            print("Error: 'start_row' and 'start_col' must be integers.")
            return

        try:
            current_row = start_row
            for i, value in enumerate(data):
                current_col = start_col + (i % columns_per_row)
                if current_col == start_col and i > 0:
                    current_row += 1

                print(f"Inserting '{value}' into cell ({current_row}, {current_col})")
                self.worksheet.Cells(current_row, current_col).Value = value
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

# Usage Example
file_path = "d:/python course/Financial Sample.xlsx"
ex = ExcelAutomation(file_path)
ex.open_workbook()
ex.insert_data(702, 1, 10, "Data1", "Data2", "Data3", "Data4", "Data5", "Data6", "Data7", "Data8", "Data9", "Data10", "Data11", "Data12")
ex.save_data()
ex.close_data()

