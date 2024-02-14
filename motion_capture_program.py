import cv2
import numpy as np
import math


"""
Set up the trackbars for color range adjustment.
This section initializes sliders to adjust color detection thresholds in a video feed.
"""
def setup_trackbars(range_filter):
    # Create a window named 'Trackbars' to hold our sliders.
    cv2.namedWindow("Trackbars", 0)
    
    # For each color component (Hue, Saturation, Value), create two sliders: MIN and MAX.
    # These sliders allow users to set the minimum and maximum values for color detection.
    for i, name in enumerate(["MIN", "MAX"]):
        for j in range(0, 3):
            cv2.createTrackbar(f"{name}_{range_filter[j]}", "Trackbars", 0, 255, lambda x: None)


"""
Function to read the current settings of the trackbars (sliders) for color detection.
"""
def get_trackbar_values(range_filter):
    values = []

    # Retrieve the current positions of the six sliders (MIN and MAX for Hue, Saturation, Value).
    for i, name in enumerate(["MIN", "MAX"]):
        for j in range(0, 3):
            v = cv2.getTrackbarPos(f"{name}_{range_filter[j]}", "Trackbars")
            values.append(v)

    return values


"""
This function finds the center points (centroids) of detected colored areas in the video.
i.e Calculate centroids of detected contours in the given mask.
"""
def calculate_centroids(mask):
    # Find contours in the mask
    # Detect edges and shapes (contours) in the masked image where our color is detected.
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # List to store centroids
    centroids = []

    for contour in contours:
        # Calculate the centroid of each shape using moments (a way of summing up pixel intensities).
        M = cv2.moments(contour)
        
        # Only calculate if the area is non-zero to avoid division by zero.
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            centroids.append((cX, cY))
        else:
            # Avoid division by zero
            cX, cY = 0, 0

    return centroids


"""
Place visual markers at each centroid in the video to show where the centers of colored areas are.
i.e. Draw centroids on the frame.
"""
def draw_centroids(frame, centroids):
    for (cX, cY) in centroids:
        # Draw a white circle at the centroid
        cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
    
    return frame


"""
Draw lines between centroids based on the given connections.
:param frame: The video frame on which to draw.
:param centroids: A list of (x, y) tuples representing the centroids.
:param connections: A list of tuples representing the indices of centroids to connect.
"""
def connect_centroids(frame, centroids, connections):
    for start_idx, end_idx in connections:
        start_point = centroids[start_idx]
        end_point = centroids[end_idx]
        # Draw a line between the specified pairs of centroids.
        cv2.line(frame, start_point, end_point, (0, 255, 0), 2)
    
    return frame


"""
Calculate the angle (in degrees) at pt2 formed by the line segments pt1-pt2 and pt2-pt3.
:param pt1, pt2, pt3: The (x, y) coordinates of the three points.
:return: The calculated angle in degrees.
"""
def calculate_angle(pt1, pt2, pt3):
    # Calculate the vectors from the points
    vector1 = (pt1[0] - pt2[0], pt1[1] - pt2[1])
    vector2 = (pt3[0] - pt2[0], pt3[1] - pt2[1])

    # Calculate the dot product between vectors
    dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]

    # Calculate the magnitudes of the vectors
    magnitude1 = math.sqrt(vector1[0]**2 + vector1[1]**2)
    magnitude2 = math.sqrt(vector2[0]**2 + vector2[1]**2)

    # Calculate the angle in radians and then convert to degrees
    angle_rad = math.acos(dot_product / (magnitude1 * magnitude2))
    angle_deg = math.degrees(angle_rad)

    return angle_deg


"""
Visualize the calculated angle on the video frame.
:param frame: The video frame on which to draw.
:param pt2: The point (x, y) where the angle is calculated.
:param angle: The angle value to be displayed.
"""
def draw_angle(frame, pt2, angle):
    cv2.putText(frame, f"{int(angle)} deg", (pt2[0] + 10, pt2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

def main():
    # Start capturing video from the webcam
    cap = cv2.VideoCapture(0)

    # Color range for HSV filtering, assuming RED as an example
    range_filter = 'HSV'
    setup_trackbars(range_filter)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Get current positions of the trackbars
        v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = get_trackbar_values("HSV")

        # Define the min and max HSV values
        lower = np.array([v1_min, v2_min, v3_min])
        upper = np.array([v1_max, v2_max, v3_max])

        # Threshold the HSV image to get only the colors in the range
        mask = cv2.inRange(hsv, lower, upper)

        # Bitwise-AND mask and original image
        result = cv2.bitwise_and(frame, frame, mask=mask)

        centroids = calculate_centroids(mask)

        result = draw_centroids(result, centroids)

        # Define connections based on your setup, e.g., [(0, 1), (1, 2)]
        connections = [(0, 1), (1, 2)]

        if len(centroids) >= len(connections) + 1:
            result = connect_centroids(result, centroids, connections)

            # Optionally, calculate and draw angles if there are enough points
            if len(centroids) > 2:
                angle = calculate_angle(centroids[0], centroids[1], centroids[2])
                draw_angle(result, centroids[1], angle)
        
        # Display the original and masked images
        cv2.imshow('Original', frame)
        cv2.imshow('Filtered', result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()