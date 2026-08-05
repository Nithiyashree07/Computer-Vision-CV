import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("C:/Users/hp/Downloads/violin.jpg")   # Replace with your image file name

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Define colors for each channel
    colors = ('b', 'g', 'r')

    # Calculate and display histogram for each color channel
    for i, color in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    # Add labels and title
    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")

    # Show histogram
    plt.show()
