import cv2
import numpy

# Create an object from the VideoCapture class that will capture images and
# video from the external webcam.
cap = cv2.VideoCapture(0)

# Create windows in which to display images and trackbars.
cv2.namedWindow("Filtered Dots")





# Create trackbars to adjust the color min and max values for each dot.
cv2.createTrackbar("Dot1 Hue Min", "Filtered Dots", 0, 179, lambda x: None)
cv2.createTrackbar("Dot1 Hue Max", "Filtered Dots", 0, 179, lambda x: None)
cv2.createTrackbar("Dot1 Saturation Min", "Filtered Dots", 0, 255, lambda x: None)
cv2.createTrackbar("Dot1 Saturation Max", "Filtered Dots", 0, 255, lambda x: None)
cv2.createTrackbar("Dot1 Value Min", "Filtered Dots", 0, 255, lambda x: None)
cv2.createTrackbar("Dot1 Value Max", "Filtered Dots", 0, 255, lambda x: None)
cv2.createTrackbar("Dot2 Hue Min", "Filtered Dots", 0, 179, lambda x: None)
cv2.createTrackbar("Dot2 Hue Max", "Filtered Dots", 0, 179, lambda x: None)
cv2.createTrackbar("Dot2 Saturation Min", "Filtered Dots", 0, 255, lambda x: None)
cv2.createTrackbar("Dot2 Saturation Max", "Filtered Dots", 0, 255, lambda x: None)
cv2.createTrackbar("Dot2 Value Min", "Filtered Dots", 0, 255, lambda x: None)
cv2.createTrackbar("Dot2 Value Max", "Filtered Dots", 0, 255, lambda x: None)
cv2.createTrackbar("Dot3 Hue Min", "Filtered Dots", 0, 179, lambda x: None)
cv2.createTrackbar("Dot3 Hue Max", "Filtered Dots", 0, 179, lambda x: None)
cv2.createTrackbar("Dot3 Saturation Min", "Filtered Dots", 0, 255, lambda x: None)
cv2.createTrackbar("Dot3 Saturation Max", "Filtered Dots", 0, 255, lambda x: None)
cv2.createTrackbar("Dot3 Value Min", "Filtered Dots", 0, 255, lambda x: None)
cv2.createTrackbar("Dot3 Value Max", "Filtered Dots", 0, 255, lambda x: None)
cv2.createTrackbar("Dot4 Hue Min", "Filtered Dots", 0, 179, lambda x: None)
cv2.createTrackbar("Dot4 Hue Max", "Filtered Dots", 0, 179, lambda x: None)
cv2.createTrackbar("Dot4 Saturation Min", "Filtered Dots", 0, 255, lambda x: None)
cv2.createTrackbar("Dot4 Saturation Max", "Filtered Dots", 0, 255, lambda x: None)
cv2.createTrackbar("Dot4 Value Min", "Filtered Dots", 0, 255, lambda x: None)
cv2.createTrackbar("Dot4 Value Max", "Filtered Dots", 0, 255, lambda x: None)



# Initialize while loop control variable.
key_pressed = 1

# In a loop, use trackbars to adjust the filter.
# Loop ends once the Escape key is pressed.
while key_pressed != 27:

    # Capture one frame (image) of video, save the data in two variables.
    # The second variable, frame, contains the image data.
    ret, frame = cap.read()

    # Convert the frame from BGR to HSV color space.
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    dot1_hue_min = cv2.getTrackbarPos("Dot1 Hue Min", "Filtered Dots")
    dot1_hue_max = cv2.getTrackbarPos("Dot1 Hue Max", "Filtered Dots")
    dot1_saturation_min = cv2.getTrackbarPos("Dot1 Saturation Min", "Filtered Dots")
    dot1_saturation_max = cv2.getTrackbarPos("Dot1 Saturation Max", "Filtered Dots")
    dot1_value_min = cv2.getTrackbarPos("Dot1 Value Min", "Filtered Dots")
    dot1_value_max = cv2.getTrackbarPos("Dot1 Value Max", "Filtered Dots")
    dot2_hue_min = cv2.getTrackbarPos("Dot2 Hue Min", "Filtered Dots")
    dot2_hue_max = cv2.getTrackbarPos("Dot2 Hue Max", "Filtered Dots")
    dot2_saturation_min = cv2.getTrackbarPos("Dot2 Saturation Min", "Filtered Dots")
    dot2_saturation_max = cv2.getTrackbarPos("Dot2 Saturation Max", "Filtered Dots")
    dot2_value_min = cv2.getTrackbarPos("Dot2 Value Min", "Filtered Dots")
    dot2_value_max = cv2.getTrackbarPos("Dot2 Value Max", "Filtered Dots")
    dot3_hue_min = cv2.getTrackbarPos("Dot3 Hue Min", "Filtered Dots")
    dot3_hue_max = cv2.getTrackbarPos("Dot3 Hue Max", "Filtered Dots")
    dot3_saturation_min = cv2.getTrackbarPos("Dot3 Saturation Min", "Filtered Dots")
    dot3_saturation_max = cv2.getTrackbarPos("Dot3 Saturation Max", "Filtered Dots")
    dot3_value_min = cv2.getTrackbarPos("Dot3 Value Min", "Filtered Dots")
    dot3_value_max = cv2.getTrackbarPos("Dot3 Value Max", "Filtered Dots")
    dot4_hue_min = cv2.getTrackbarPos("Dot4 Hue Min", "Filtered Dots")
    dot4_hue_max = cv2.getTrackbarPos("Dot4 Hue Max", "Filtered Dots")
    dot4_saturation_min = cv2.getTrackbarPos("Dot4 Saturation Min", "Filtered Dots")
    dot4_saturation_max = cv2.getTrackbarPos("Dot4 Saturation Max", "Filtered Dots")
    dot4_value_min = cv2.getTrackbarPos("Dot4 Value Min", "Filtered Dots")
    dot4_value_max = cv2.getTrackbarPos("Dot4 Value Max", "Filtered Dots")


    # Define the lower and upper bounds for each colored dot.
    lower_dot1 = numpy.array([dot1_hue_min, dot1_saturation_min, dot1_value_min])
    upper_dot1 = numpy.array([dot1_hue_max, dot1_saturation_max, dot1_value_max])
    lower_dot2 = numpy.array([dot2_hue_min, dot2_saturation_min, dot2_value_min])
    upper_dot2 = numpy.array([dot2_hue_max, dot2_saturation_max, dot2_value_max])
    lower_dot3 = numpy.array([dot3_hue_min, dot3_saturation_min, dot3_value_min])
    upper_dot3 = numpy.array([dot3_hue_max, dot3_saturation_max, dot3_value_max])
    lower_dot4 = numpy.array([dot4_hue_min, dot4_saturation_min, dot4_value_min])
    upper_dot4 = numpy.array([dot4_hue_max, dot4_saturation_max, dot4_value_max])
   

    # Create masks to identify the colored dots.
    mask_dot1 = cv2.inRange(hsv_frame, lower_dot1, upper_dot1)
    mask_dot2 = cv2.inRange(hsv_frame, lower_dot2, upper_dot2)
    mask_dot3 = cv2.inRange(hsv_frame, lower_dot3, upper_dot3)
    mask_dot4 = cv2.inRange(hsv_frame, lower_dot4, upper_dot4)

    # Combine the masks to create a single mask.
    combined_mask = mask_dot1 + mask_dot2 + mask_dot3 + mask_dot4

    # Apply the mask to create the filtered image.
    filtered_dots = cv2.bitwise_and(frame, frame, mask=combined_mask)

    # Calculate centroids of the markers.
    contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    centroids = []
    for cnt in contours:
        M = cv2.moments(cnt)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            centroids.append((cX, cY))
            cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)

    # Draw line segments from the center of the image to each marker's centroid.
    center_of_image = (frame.shape[1] // 2, frame.shape[0] // 2)
    for centroid in centroids:
        cv2.line(frame, center_of_image, centroid, (255, 255, 255), 2)

    # Display the filtered dots.
    cv2.imshow("Filtered Dots", frame)

    # Wait 30 milliseconds for a key to be pressed.
    key_pressed = cv2.waitKey(30)

# Close the image file and close all windows.
cap.release()
cv2.destroyAllWindows()
