import cv2

# Read the image
image = cv2.imread("C:/users/hp/Downloads/image.jpeg")   # Replace with your image file name

# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Histogram Equalization
    equalized = cv2.equalizeHist(gray)

    # Display the original grayscale image
    cv2.imshow("Original Grayscale Image", gray)

    # Display the histogram equalized image
    cv2.imshow("Histogram Equalized Image", equalized)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
