import cv2

# Read the image
image = cv2.imread("C:/Users/hp/Downloads/violin.jpg")   # Replace with your image file name

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Display the original image
    cv2.imshow("Original Image", image)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Display the outline (edges)
    cv2.imshow("Canny Edge Detection", edges)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
