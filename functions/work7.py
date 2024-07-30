import os
import win32com.client  #  pip install pywin32

a="d:/python course/Financial Sample.xlsx"

class ExcelAutomation:

    def __init__(self,a):
        self.a=a
        self.b=win32com.client.Dispatch("Excel.Application")
        self.workbook=None
        self.worksh=None
        
    
    def open_workbook(self):
        try:
            self.workbook=self.b.Workbooks.Open(self.a)
            self.worksh=self.workbook.Worksheets(1)
        except Exception as e:
            print("error")
            
    def insert_data(self):
        self.worksh.Range("A702").Value = "Private"
        # self.worksheet.Range("B702").Value = "Private"
        # self.worksheet.Range("C702").Value = "Private"
        # self.worksheet.Range("D702").Value = "Private"
        # self.worksheet.Range("E702").Value = "Private"
        # self.worksheet.Range("F702").Value = "Private"
        data = ["Private"]*6  # Data to be inserted
        range_start = "A802"
        for i, value in enumerate(data):
            self.worksheet.Range(range_start).Offset(0, i).Value = value
        
    def update_data(self,c,d):
        self.worksheet.Range(c).Value = d
        
    def delete_data(self,e):
        self.worksheet.Rows(e).Delete()
        
    def save_data(self):
        self.workbook.Save()
    def close_data(self):
        self.b.Quit()
        
        

ex=ExcelAutomation(a)
ex.open_workbook()
ex.insert_data()
ex.update_data("A702","hhh")
ex.delete_data(702)
ex.save_data()
ex.close_data()