from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

video_path = "videos/store_sample.mp4"

cap = cv2.VideoCapture(video_path)

while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    results = model.track(
        frame,
        persist=True,
        classes=[0],
        verbose=False,
        tracker="bytetrack.yaml"
    )

    annotated_frame = results[0].plot()

    cv2.imshow("Store Tracking", annotated_frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()