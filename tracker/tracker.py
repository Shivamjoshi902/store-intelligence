from ultralytics import YOLO
import cv2
from config.config_loader import load_config
from events.event_processor import create_event
from database.db import (
    initialize_database,
    save_event
)

initialize_database()

model = YOLO("yolov8n.pt")

events = []

entry_count = 0

entered_ids = set()

exit_count = 0

exited_ids = set()

occupancy = 0

config = load_config()

ENTRY_LINE_Y = config["entry_line_y"]

previous_positions = {}

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

    if results[0].boxes.id is not None:

        boxes = results[0].boxes.xyxy.cpu().numpy()
        track_ids = results[0].boxes.id.int().cpu().tolist()

        for box, track_id in zip(boxes, track_ids):

            x1, y1, x2, y2 = box

            center_y = int((y1 + y2) / 2)

            previous_y = previous_positions.get(
                track_id,
                center_y
            )

            previous_positions[track_id] = center_y

            if (
                previous_y < ENTRY_LINE_Y
                and center_y >= ENTRY_LINE_Y
                and track_id not in entered_ids
            ):

                entry_count += 1

                occupancy += 1

                entered_ids.add(track_id)

                event = create_event(
                    person_id=track_id,
                    event_type="entry"
                )

                events.append(event)

                save_event(event)

            if (
                previous_y > ENTRY_LINE_Y
                and center_y <= ENTRY_LINE_Y
                and track_id not in exited_ids
            ):

                exit_count += 1

                occupancy -= 1

                exited_ids.add(track_id)

                event = create_event(
                    person_id=track_id,
                    event_type="exit"
                )

                events.append(event)

                save_event(event)

    cv2.line(
        annotated_frame,
        (0, ENTRY_LINE_Y),
        (annotated_frame.shape[1], ENTRY_LINE_Y),
        (0, 255, 255),
        2
    )

    cv2.putText(
        annotated_frame,
        "ENTRY LINE",
        (20, ENTRY_LINE_Y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    cv2.putText(
        annotated_frame,
        f"Entries: {entry_count}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        annotated_frame,
        f"Exits: {exit_count}",
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.putText(
        annotated_frame,
        f"Occupancy: {occupancy}",
        (20, 130),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 0),
        2
    )

    cv2.putText(
        annotated_frame,
        f"Events: {len(events)}",
        (20, 170),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.imshow("Store Tracking", annotated_frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()