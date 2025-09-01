import cv2

def cartoonify(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 5)

    # Edge detection
    edges = cv2.adaptiveThreshold(gray_blur, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # Color filtering
    color = cv2.bilateralFilter(frame, d=9, sigmaColor=200, sigmaSpace=200)

    # Combine edges + color
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

# Capture from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cartoon_frame = cartoonify(frame)

    # Show original and cartoon
    cv2.imshow("Original", frame)
    cv2.imshow("Cartoon", cartoon_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
