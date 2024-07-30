import pytesseract
from PIL import Image

# Set the Tesseract command path explicitly
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

image = Image.open('d:/Data Analytics videos/hypintro.jpg')

# Use tesseract to extract text from image
text = pytesseract.image_to_string(image)

print(text)



