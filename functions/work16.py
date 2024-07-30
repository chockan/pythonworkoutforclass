import cv2

# Load the pre-trained Haar Cascade XML file
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Check if the cascade file loaded correctly
if face_cascade.empty():
    raise IOError('Cannot load the cascade classifier xml file')

# Specify the path to the image
image_path = 'd:/python course/courses/python workout for class/functions/1.png'

# Load an image from file
img = cv2.imread(image_path)

# Check if the image is loaded properly
if img is None:
    raise IOError('Cannot load image')

# Convert the image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(imgGray, scaleFactor=1.2, minNeighbors=5)

# Draw rectangles around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the output
cv2.imshow('Detected Faces', img)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
