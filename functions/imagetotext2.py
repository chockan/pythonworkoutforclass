import pytesseract
from PIL import Image

# Set the Tesseract command path explicitly
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Open the image file
image = Image.open('d:/React Tutorial/React workout/reacthooks images/useeffect&uselayout.JPG')

# Use tesseract to extract text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text (optional)
print(text)

# Save the extracted text to a file
with open('d:/React Tutorial/React workout/syntheticevents/hooks.md', 'a') as file:
    file.write(text)
