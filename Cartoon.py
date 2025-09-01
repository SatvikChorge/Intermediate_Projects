import cv2
import matplotlib.pyplot as plt

# Load image
img = cv2.imread(r"C:\Users\My PC\OneDrive\Pictures\Pictures\memories\IMG_20240818_203209_877.jpg")

# Convert to RGB (OpenCV loads in BGR)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Step 1: Edge Detection
gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
blur = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(blur, 255,
                              cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY, 9, 9)

# Step 2: Color Filtering
color = cv2.bilateralFilter(img_rgb, d=9, sigmaColor=200, sigmaSpace=200)

# Step 3: Combine edges + color
cartoon = cv2.bitwise_and(color, color, mask=edges)

# Show results
plt.figure(figsize=(10,8))
plt.subplot(1,3,1); plt.imshow(img_rgb); plt.title("Original")
plt.subplot(1,3,2); plt.imshow(edges, cmap='gray'); plt.title("Edges")
plt.subplot(1,3,3); plt.imshow(cartoon); plt.title("Cartoonified")
plt.show()
