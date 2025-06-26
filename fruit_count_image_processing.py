import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to display images
def display_image(title, img):
    plt.figure(figsize=(10, 8))
    if len(img.shape) == 2:
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

# Load the image
image_path = "image_path"
image = cv2.imread(image_path)
display_image("Original Image", image)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
display_image("Grayscale Image", gray)

# Apply Gaussian Blur to reduce noise, please adjust the parameter values 
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
display_image("Blurred Image", blurred)

# Use adaptive thresholding to handle uneven lighting, please adjust the parameter values
thresh = cv2.adaptiveThreshold(
    blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
)
display_image("Thresholded Image", thresh)

# Perform morphological operations to separate connected objects, please adjust the parameter values
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
display_image("Morphological Operations Result", morph)

# Find contours after watershed
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours and count them
count = 0
output = image.copy()
for contour in contours:
    area = cv2.contourArea(contour)
    if 1500 < area < 50000:  # Filter small noise and very large surrounding regions
        count += 1
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)

display_image("Final Detected Fruits", output)

# Print the count of fruits
print(f"Number of fruits detected: {count}")