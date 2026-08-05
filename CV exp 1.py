import cv2

# Read the image
image = cv2.imread(r"C:/users/hp/Downloads/image.jpeg")  # Replace with your image path

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load the image. Check the file path.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray_image, 100, 200)

    # Display the original image and edge-detected image
    cv2.imshow("Original Image", image)
    cv2.imshow("Canny Edge Detection", edges)

    # Save the edge-detected image (optional)
    cv2.imwrite("canny_edges.jpg", edges)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
