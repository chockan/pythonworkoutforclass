import pandas as pd
bank = pd.read_csv('Data/Bank.csv')
bank.head()

"""
Note that the head(n) method can be called on the new DataFrame bank.
 Head simply prints out the first n rows of the data frame so you can see if it imported okay.
 pd.read_csv('C:/Users/Michael Brydon/Data/Bank.csv") — all forward slashes
pd.read_csv(r'C:\Users\Michael Brydon\Data/Bank.csv") — mixture of slashes and backslashes with the "r" prefix
"""

#Here we use read_excel instead of read_csv. It is the same data, but in a different file format on my computer:

bankxl = pd.read_excel('Data/Bank.xlsx')
bankxl.head()

#As noted previously, objects in Python expose useful properties and methods. For example, we can confirm the size of the bank data frame with the shape property, which gives us the number of rows (209) and columns (9):

bank.shape
(208, 9)

#We can use the describe() method to generate some summary statistics:

bank.describe()

#Second, by default, the describe() method only summarizes the numerical columns. Recall that our data frame consists of nine columns. To see the issue, run the info() method:

bank.info()

"""
The process for replacing the two (string) “Object” columns with categories is similar to the one we used in R. 
The key is understanding how to reference columns in Python. Two possibilities:

square bracket notation: bank['Gender']

dot notation: bank.Gender

Of these two, square bracket notation is slightly more flexible because it permits column names with spaces, 
e.g., dataframe['column name']. The dot notation of this would fail because Python has no way of knowing 
what the space after “column” means: dataframe.column name.

Once we know how to reference a column (or a “Series” in Pandas-speak), we can run the type conversion method 
and specify “category” as the output data type:
"""
bank['Gender'].astype('category')
bank['Gender'] = bank['Gender'].astype('category')
bank['PCJob'] = bank['PCJob'].astype('category')
bank.describe(include='category')

for col in ['Gender', 'PCJob']:
    bankxl[col] = bankxl[col].astype('category')
    
bank.info()