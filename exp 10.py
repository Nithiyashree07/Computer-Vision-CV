import cv2

# Read the image
image = cv2.imread("C:/users/hp/Downloads/image.jpeg")   # Replace with your image file name

# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Rotate the image 90 degrees clockwise
    rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # Display the original image
    cv2.imshow("Original Image", image)

    # Display the rotated image
    cv2.imshow("90 Degree Clockwise Rotation", rotated)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
