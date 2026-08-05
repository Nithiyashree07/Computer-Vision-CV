import cv2
import numpy as np

# Read the image
image = cv2.imread("C:/Users/hp/Downloads/violin.jpg")   # Replace with your image file name

# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Create a 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply Dilation
    dilated = cv2.dilate(image, kernel, iterations=1)

    # Display the original image
    cv2.imshow("Original Image", image)

    # Display the dilated image
    cv2.imshow("Dilated Image", dilated)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
