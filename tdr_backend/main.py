# from src.video_processor import extract_frames
# from src.object_tracker import run_tracking
# from src.collision_classifier import classify_collision
# from src.fault_estimator import estimate_fault
# from src.damage_detector import detect_damage

# VIDEO_PATH = "data/crash_sample.mp4"

# # Step 1: Frame extraction
# frames = extract_frames(VIDEO_PATH)

# # Step 2: Object tracking
# tracking_data = run_tracking(frames)

# # Step 3: Collision classification
# collision_type = classify_collision(tracking_data)

# # Step 4: Fault estimation
# fault = estimate_fault(tracking_data)

# # Step 5: Damage analysis
# damaged_parts, estimated_cost = detect_damage(frames)

# Output summary
# print("Collision Type:", collision_type)
# print("Fault:", fault)
# print("Damaged Parts:", damaged_parts)
# print("Estimated Repair Cost: $", estimated_cost)
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from video_processor import extract_frames
from object_tracker import run_tracking
from collision_classifier import classify_collision

VIDEO_PATH = "data/crash_sample.mp4"

# Extract frames and run tracking first
frames = extract_frames(VIDEO_PATH)
tracking_data = run_tracking(frames)

print("Sample tracking output:")
print(tracking_data[:3])  # Print first 3 entries

# NOW classify collision
collision_type = classify_collision(tracking_data)
print("Collision Type:", collision_type)
