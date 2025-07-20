from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import cv2

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # You can try 'yolov8m.pt' or 'yolov8l.pt' for more accuracy later
tracker = DeepSort(max_age=15)  # Tracks for 15 frames if object disappears

def run_tracking(frame_paths):
    tracking_results = []

    for frame_path in frame_paths:
        frame = cv2.imread(frame_path)
        if frame is None:
            continue

        # Detect vehicles (YOLO class IDs for car, bus, truck, motorcycle)
        results = model.predict(source=frame, classes=[2, 3, 5, 7], conf=0.4, verbose=False)[0]

        detections = []
        for box in results.boxes.data.tolist():
            x1, y1, x2, y2, conf, cls = box
            detections.append(([x1, y1, x2 - x1, y2 - y1], conf, "vehicle"))

        # Run DeepSORT on detections
        tracks = tracker.update_tracks(detections, frame=frame)
        for track in tracks:
            if not track.is_confirmed():
                continue
            tracking_results.append({
                "track_id": track.track_id,
                "frame_path": frame_path,
                "bbox": track.to_ltrb()
            })

    return tracking_results
