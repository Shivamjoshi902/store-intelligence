from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

video_path = "videos/store_sample.mp4"

cap = cv2.VideoCapture(video_path)

while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    results = model(
        frame,
        classes=[0],
        verbose=False
    )

    annotated_frame = results[0].plot()

    cv2.imshow("Store Intelligence - Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()