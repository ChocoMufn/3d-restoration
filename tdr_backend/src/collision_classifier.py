import math
from collections import defaultdict

def calculate_angle(v1, v2):
    """Returns angle between two vectors in degrees"""
    dot = v1[0]*v2[0] + v1[1]*v2[1]
    mag1 = math.sqrt(v1[0]**2 + v1[1]**2)
    mag2 = math.sqrt(v2[0]**2 + v2[1]**2)
    if mag1 * mag2 == 0:
        return 0
    return math.degrees(math.acos(dot / (mag1 * mag2)))

def classify_collision(tracking_data):
    track_dict = defaultdict(list)

    # Group all bboxes by track ID
    for entry in tracking_data:
        track_dict[entry["track_id"]].append(entry)

    # Only compare between top 2 longest-tracked objects
    tracks = sorted(track_dict.items(), key=lambda x: len(x[1]), reverse=True)[:2]
    if len(tracks) < 2:
        return "Unknown"

    id1, t1 = tracks[0]
    id2, t2 = tracks[1]

    # Use first and last bboxes for each
    def get_vector(track):
        x_start = track[0]["bbox"][0]
        y_start = track[0]["bbox"][1]
        x_end = track[-1]["bbox"][0]
        y_end = track[-1]["bbox"][1]
        return (x_end - x_start, y_end - y_start)

    v1 = get_vector(t1)
    v2 = get_vector(t2)

    angle = calculate_angle(v1, v2)

    # Determine type
    if angle < 30:
        return "Rear-End"
    elif 150 < angle < 180:
        return "Head-On"
    elif 60 < angle < 120:
        return "Side Impact"
    elif 30 <= angle < 60 or 120 <= angle < 150:
        return "Corner"
    else:
        return "Sideswipe"
