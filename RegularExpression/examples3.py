
# import re
# statement = "Please contact us at: support@datacamp.com, xyz@datacamp.com"

# #'addresses' is a list that stores all the possible match
# addresses = re.findall(r'[\w\.-]+@[\w\.-]+', statement)
# for address in addresses:
#     print(address)


#########################################################

#https://www.bu.edu/lernet/artemis/years/2011/slides/python.pdf


# import PyPDF2
# import re
# import requests

# the_idiot_url = 'https://www.bu.edu/lernet/artemis/years/2011/slides/python.pdf'

# def get_book(url):
#     # Sends a http request to get the PDF content
#     response = requests.get(url)
#     # Open the PDF file in binary mode
#     with open('python.pdf', 'wb') as f:
#         f.write(response.content)

#     # Open the PDF file
#     with open('python.pdf', 'rb') as f:
#         # Create a PDF reader object
#         pdf_reader = PyPDF2.PdfFileReader(f)
#         # Initialize an empty string to store the extracted text
#         text = ''
#         # Iterate through each page of the PDF
#         for page_num in range(pdf_reader.numPages):
#             # Extract text from the current page
#             text += pdf_reader.getPage(page_num).extractText()

#     return text

# def preprocess(sentence):
#     return re.sub('[^A-Za-z0-9.]+' , ' ', sentence).lower()

# book = get_book(the_idiot_url)
# processed_book = preprocess(book)
# print(processed_book)


import PyPDF2
import re
import requests

the_idiot_url = 'https://www.bu.edu/lernet/artemis/years/2011/slides/python.pdf'

def get_book(url):
    # Sends a http request to get the PDF content
    response = requests.get(url)
    # Open the PDF file in binary mode
    with open('python.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with open('python.pdf', 'rb') as f:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(f)
        # Initialize an empty string to store the extracted text
        text = ''
        # Iterate through each page of the PDF
        for page_num in range(len(pdf_reader.pages)):
            # Extract text from the current page
            text += pdf_reader.pages[page_num].extract_text()

    return text

def preprocess(sentence):
    #return re.sub('[^A-Za-z0-9.]+' , ' ', sentence).lower()
    return re.sub('Python' , ' ', sentence).lower()

book = get_book(the_idiot_url)
processed_book = preprocess(book)
print(processed_book)

