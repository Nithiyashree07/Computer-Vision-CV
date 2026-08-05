import cv2

# Read the image
image = cv2.imread("C:/users/hp/Downloads/image.jpeg")   # Replace with your image file name

# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(image, (15, 15), 0)

    # Display the original image
    cv2.imshow("Original Image", image)

    # Display the blurred image
    cv2.imshow("Gaussian Blurred Image", blurred)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
