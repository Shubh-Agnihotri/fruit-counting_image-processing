# 🍎 Fruit Counting and Quality Detection using Image Processing

This repository contains Python implementations for:
1. Counting fruits in an image using image processing techniques.
2. Detecting unhealthy regions on fruits based on color segmentation.

---

## 📸 Fruit Counting

This module processes an image to **detect and count the number of fruits** present using OpenCV.

### 🔍 Techniques Used
- Grayscale conversion
- Gaussian blurring
- Adaptive thresholding
- Morphological operations
- Contour detection and bounding box filtering

### 🧪 File: `fruit_count_image_processing.py`

#### 🧾 Steps:
1. Load an image from the path `image_path`.
2. Preprocess it by converting to grayscale and applying Gaussian blur.
3. Apply adaptive thresholding to highlight fruit regions.
4. Use morphological operations to separate overlapping objects.
5. Detect external contours and filter them based on area.
6. Draw bounding boxes around detected fruits.
7. Output the total fruit count.

#### 📤 Output
- A visual output with bounding boxes drawn around detected fruits.
- Printed count:  
  `Number of fruits detected: X`

---

## 🍌 Fruit Quality Detection

This module analyzes a fruit image to estimate the **percentage of unhealthy (discolored) regions** using HSV color segmentation.

### 🧪 File: `fruit_quality_detection.py`

### 🎯 Approach:
- Convert the image to the HSV color space for better segmentation.
- Use color thresholding to isolate:
  - Total fruit area
  - Unhealthy regions (brown/greenish/pale zones)
- Calculate the overlap between fruit area and unhealthy zones.
- Compute the percentage of unhealthy area.

### 💡 Color Thresholds:
- **Fruit area**: Wide HSV range to capture all fruit pixels.
- **Unhealthy areas**:
  - Brown (rot)
  - Green (underripe)
  - Pale (fungal or overripe zones)

### 🧾 Output
- Visual of the original image.
- Printed result:
  `Percentage of Unhealthy Area: XX.XX%`

---

## ⚙️ Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Matplotlib (for fruit counting visualization)

Install dependencies:

```bash
pip install opencv-python numpy matplotlib

