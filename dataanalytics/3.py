import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Salary': [50000, 60000, 70000, 80000]}
df = pd.DataFrame(data)

# # Exporting DataFrame to CSV
# df.to_csv('data.csv', index=False)
# # Exporting DataFrame to Excel
df.to_excel('Book1.xlsx', index=False)
# # Exporting DataFrame to JSON
# df.to_json('data.json', orient='records')
#####################################################
#Exporting Data to CSV (Using csv module):

import csv

# # Assuming data is a list of dictionaries
data = [{'Name': 'Alice', 'Age': 25, 'Salary': 50000},
        {'Name': 'Bob', 'Age': 30, 'Salary': 60000},
        {'Name': 'Charlie', 'Age': 35, 'Salary': 70000},
        {'Name': 'David', 'Age': 40, 'Salary': 80000}]

# Exporting data to CSV
with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'Salary']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in data:
        writer.writerow(row)


#######################################################
# from openpyxl import Workbook

# # Create a new Workbook
# wb = Workbook()
# ws = wb.active

# # Assuming data is a list of dictionaries
# data = [{'Name': 'Alice', 'Age': 25, 'Salary': 50000},
#         {'Name': 'Bob', 'Age': 30, 'Salary': 60000},
#         {'Name': 'Charlie', 'Age': 35, 'Salary': 70000},
#         {'Name': 'David', 'Age': 40, 'Salary': 80000}]

# # Write data to Excel
# ws.append(['Name', 'Age', 'Salary'])
# for row in data:
#     ws.append([row['Name'], row['Age'], row['Salary']])

# # Save the Workbook
# wb.save('data.xlsx')

#######################################################
