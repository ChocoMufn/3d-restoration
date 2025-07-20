import cv2
import os
from tqdm import tqdm

def extract_frames(video_path, output_dir="data/frames", every_n_frames=1):
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    frame_idx = 0
    saved_frames = []

    if not cap.isOpened():
        raise Exception(f"Could not open video {video_path}")

    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in tqdm(range(total), desc="Extracting frames"):
        success, frame = cap.read()
        if not success:
            break

        if i % every_n_frames == 0:
            frame_path = os.path.join(output_dir, f"frame_{frame_idx:04d}.jpg")
            cv2.imwrite(frame_path, frame)
            saved_frames.append(frame_path)
            frame_idx += 1

    cap.release()
    return saved_frames
