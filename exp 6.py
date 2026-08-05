import cv2
import numpy as np

# Read the image
image = cv2.imread("C:/users/hp/Downloads/image.jpeg")   # Replace with your image file name

# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply Erosion
    eroded = cv2.erode(image, kernel, iterations=1)

    # Display the original image
    cv2.imshow("Original Image", image)

    # Display the eroded image
    cv2.imshow("Eroded Image", eroded)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
