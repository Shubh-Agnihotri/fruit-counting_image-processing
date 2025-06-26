import cv2
import numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('image_path')

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#for fruit area
lower_fruit = np.array([0, 50, 50])
upper_fruit = np.array([180, 255, 255])
fruit_mask = cv2.inRange(hsv, lower_fruit, upper_fruit)

#for unhealthy areas
lower_brown = np.array([10, 100, 20])
upper_brown = np.array([30, 255, 200])

lower_green = np.array([25, 30, 20])
upper_green = np.array([85, 255, 150])

lower_pale = np.array([10, 20, 150])
upper_pale = np.array([20, 100, 255])

mask_brown = cv2.inRange(hsv, lower_brown, upper_brown)
mask_green = cv2.inRange(hsv, lower_green, upper_green)

unhealthy_mask = mask_brown | mask_green

unhealthy_fruit_mask = cv2.bitwise_and(unhealthy_mask, fruit_mask)

fruit_area = cv2.countNonZero(fruit_mask)
unhealthy_area = cv2.countNonZero(unhealthy_fruit_mask)
percentage_unhealthy = (unhealthy_area / fruit_area) * 100 if fruit_area > 0 else 0

print(f"Percentage of Unhealthy Area: {percentage_unhealthy:.2f}%")

cv2_imshow(image)