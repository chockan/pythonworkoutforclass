import csv
import pandas as pd
import openpyxl


# # # Importing from CSV file using csv module
# with open('d:/python course/amazon_data.csv', 'r') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)

# Importing from Excel file using pandas
# df = pd.read_csv('d:/python course/amazon_data.csv')
# print(df.head())


################################################
bankxl = pd.read_excel('d:/python course/Book1.xlsx')
bankxl.head()
print(bankxl.head())
print(bankxl.shape)
print(bankxl.describe())
print(bankxl.info())


######################################