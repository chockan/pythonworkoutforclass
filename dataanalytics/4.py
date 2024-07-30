"""
Pandas:
Pandas is a powerful library for data manipulation and analysis. It provides easy-to-use data structures and functionalities to work with structured data efficiently.

Brief Explanation:

Pandas introduces two main data structures: Series and DataFrame.
A Series is a one-dimensional array-like object that can hold data of any type.
A DataFrame is a two-dimensional tabular data structure with labeled axes (rows and columns).
Pandas offers various functions and methods for data manipulation, cleaning, transformation, and analysis.

"""
#########################################################
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)

# Performing basic operations
mean_salary = df['Salary'].mean()
print("Mean Salary:", mean_salary)
################################################

"""
BeautifulSoup:
BeautifulSoup is a Python library for web scraping, which helps extract data from HTML and XML files. It provides tools to parse and navigate HTML/XML documents.

Brief Explanation:

BeautifulSoup helps parse HTML/XML documents into a parse tree, allowing easy navigation and extraction of data.
It supports various parsers (like html.parser, lxml, and html5lib) for parsing HTML documents.
BeautifulSoup provides methods to search and extract specific elements or data from HTML/XML documents.
"""


from bs4 import BeautifulSoup
import requests

# Fetching HTML content from a website
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
response = requests.get(url)
html_content = response.text

# Parsing HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extracting specific data (e.g., title of the webpage)
title = soup.title
print("Title:", title.get_text())

# Finding specific elements
first_paragraph = soup.find('p')
print("First Paragraph:", first_paragraph.get_text())
