import win32com.client  #  pip install pywin32
a="d:/python course/Financial Sample.xlsx"

class ExcelAutomation:
    
    def __init__(self,a):
        self.a=a
        self.b=win32com.client.Dispatch("Excel.Application")
        self.workb=None
        self.worksh=None
        
        
    def open_workbook(self):
        try:
            self.workb=self.b.Workbooks.Open(self.a)
            self.worksh=self.workb.Worksheets(1)
        except Exception as e:
            print("error")
            
    def insert_data(self):
        self.worksh.Range("A702").Value = "Private"
        self.worksh.Range("B702").Value = "sachin"
        self.worksh.Range("C702").Value = "dravid"
        self.worksh.Range("D702").Value = "Private"
        self.worksh.Range("E702").Value = "Private"
        self.worksh.Range("F702").Value = "Private"
        
    def update_data(self,c,d):
        self.worksh.Range(c).Value = d
        
    def delete_data(self,e):
        self.worksh.Rows(e).Delete()
        
    def save_data(self):
        self.workb.Save()
    def close_data(self):
        self.b.Quit()
        
        
a=ExcelAutomation(a)
a.open_workbook()

#a.insert_data()
#a.update_data("A702","sky")
a.delete_data(702)
a.save_data()
a.close_data()