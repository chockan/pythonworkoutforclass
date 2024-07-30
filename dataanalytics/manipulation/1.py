# Importing the pandas library
import pandas as pd

# creating a dataframe object
student_register = pd.DataFrame()

# assigning values to the 
# rows and columns of the dataframe
student_register['Name'] = ['Abhijit','Smriti',
							'Akash', 'Roshni']
student_register['Age'] = [20, 19, 20, 14]
student_register['Student'] = [False, True,
							True, False]

print(student_register)

##########################################################
# creating a new pandas
# series object
new_person = pd.Series(['Mansi', 19, True], 
					index = ['Name', 'Age', 
								'Student'])

# using the .append() function
# to add that row to the dataframe
student_register._append(new_person, ignore_index = True)
print(student_register)

