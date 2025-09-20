import cv2
import numpy as np

img = cv2.imread("Python-Logo.jpg", cv2.IMREAD_COLOR)

# Check if image was loaded successfully
if img is None:
    print("ERROR: Could not load image! Check file path and permissions.")
else:
    print(f"Image shape: {img.shape}")
    print(f"Unique pixel values: {np.unique(img)}")
    print(f"Data type: {img.dtype}")