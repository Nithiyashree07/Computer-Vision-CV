import cv2

# Read the video
cap = cv2.VideoCapture("C:/Users/hp/Videos/Screen Recordings/Screen Recording 2026-07-07 225052.mp4")   # Replace with your video file

if not cap.isOpened():
    print("Error: Cannot open video")
else:
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Video Finished")
            break

        cv2.imshow("Video", frame)

        # Press Q to exit
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
