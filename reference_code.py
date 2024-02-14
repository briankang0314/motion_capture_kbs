# Written by Kyle Fricke & Vincent O'Sullivan, Engineer Your World
# Created in 2017, last updated in January 2020 (for Python 3)
# Use trackbars to filter the original video for four colors. 
# Display the original video and the filtered videos.
# Trackbars allow adjustment of the filters as the filtered videos display.
# Close windows when the Escape key is pressed. 

# Import OpenCV library for image processing, NumPy for digital image arrays.
import cv2
import numpy

# Create an object from the VideoCapture class that will capture images and
# video from the external webcam.
cap = cv2.VideoCapture(0)

# Create windows in which to display images and track bars.
cv2.namedWindow("Original")
cv2.namedWindow("Filtered C1")
cv2.namedWindow("Filtered C2")
cv2.namedWindow("Filtered C3")
cv2.namedWindow("Filtered C4")
cv2.namedWindow("Combined")
cv2.namedWindow("C1 Controls")
cv2.namedWindow("C2 Controls")
cv2.namedWindow("C3 Controls")
cv2.namedWindow("C4 Controls")

# Resize trackbar windows if trackbars do not display correctly.
cv2.resizeWindow("C1 Controls", 300, 300)
cv2.resizeWindow("C2 Controls", 300, 300)
cv2.resizeWindow("C3 Controls", 300, 300)
cv2.resizeWindow("C4 Controls", 300, 300)

# Create trackbars to adjust the color min and max values.
cv2.createTrackbar("C1 Blu Min", "C1 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C1 Blu Max", "C1 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C1 Grn Min", "C1 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C1 Grn Max", "C1 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C1 Red Min", "C1 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C1 Red Max", "C1 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C2 Blu Min", "C2 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C2 Blu Max", "C2 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C2 Grn Min", "C2 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C2 Grn Max", "C2 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C2 Red Min", "C2 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C2 Red Max", "C2 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C3 Blu Min", "C3 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C3 Blu Max", "C3 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C3 Grn Min", "C3 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C3 Grn Max", "C3 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C3 Red Min", "C3 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C3 Red Max", "C3 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C4 Blu Min", "C4 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C4 Blu Max", "C4 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C4 Grn Min", "C4 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C4 Grn Max", "C4 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C4 Red Min", "C4 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C4 Red Max", "C4 Controls", 0, 255, lambda x:None)

# Initialize while loop control variable.
key_pressed = 1

# In a loop, use trackbars to adjust the filter.
# Loop ends once the Escape key is pressed.
while (key_pressed != 27):

    # Capture one frame (image) of video, save the data in two variables.
    # The second variable, frame, contains the image data.
    ret, frame = cap.read()

    # Create and update a variable with the current position of the trackbar. 
    C1b_min = cv2.getTrackbarPos("C1 Blu Min", "C1 Controls") 
    C1b_max = cv2.getTrackbarPos("C1 Blu Max", "C1 Controls")
    C1g_min = cv2.getTrackbarPos("C1 Grn Min", "C1 Controls") 
    C1g_max = cv2.getTrackbarPos("C1 Grn Max", "C1 Controls")
    C1r_min = cv2.getTrackbarPos("C1 Red Min", "C1 Controls") 
    C1r_max = cv2.getTrackbarPos("C1 Red Max", "C1 Controls")   
    C2b_min = cv2.getTrackbarPos("C2 Blu Min", "C2 Controls") 
    C2b_max = cv2.getTrackbarPos("C2 Blu Max", "C2 Controls")
    C2g_min = cv2.getTrackbarPos("C2 Grn Min", "C2 Controls") 
    C2g_max = cv2.getTrackbarPos("C2 Grn Max", "C2 Controls")
    C2r_min = cv2.getTrackbarPos("C2 Red Min", "C2 Controls") 
    C2r_max = cv2.getTrackbarPos("C2 Red Max", "C2 Controls")   
    C3b_min = cv2.getTrackbarPos("C3 Blu Min", "C3 Controls") 
    C3b_max = cv2.getTrackbarPos("C3 Blu Max", "C3 Controls")
    C3g_min = cv2.getTrackbarPos("C3 Grn Min", "C3 Controls") 
    C3g_max = cv2.getTrackbarPos("C3 Grn Max", "C3 Controls")
    C3r_min = cv2.getTrackbarPos("C3 Red Min", "C3 Controls") 
    C3r_max = cv2.getTrackbarPos("C3 Red Max", "C3 Controls")   
    C4b_min = cv2.getTrackbarPos("C4 Blu Min", "C4 Controls") 
    C4b_max = cv2.getTrackbarPos("C4 Blu Max", "C4 Controls")
    C4g_min = cv2.getTrackbarPos("C4 Grn Min", "C4 Controls") 
    C4g_max = cv2.getTrackbarPos("C4 Grn Max", "C4 Controls")
    C4r_min = cv2.getTrackbarPos("C4 Red Min", "C4 Controls") 
    C4r_max = cv2.getTrackbarPos("C4 Red Max", "C4 Controls")   

    # Create variable with a list of filter boundaries.
    lower_C1 = [C1b_min, C1g_min, C1r_min]
    upper_C1 = [C1b_max, C1g_max, C1r_max]
    lower_C2 = [C2b_min, C2g_min, C2r_min]
    upper_C2 = [C2b_max, C2g_max, C2r_max]
    lower_C3 = [C3b_min, C3g_min, C3r_min]
    upper_C3 = [C3b_max, C3g_max, C3r_max]
    lower_C4 = [C4b_min, C4g_min, C4r_min]
    upper_C4 = [C4b_max, C4g_max, C4r_max]
    
    # Assign the proper data type to each of these new lists (arrays).
    lower_C1 = numpy.array(lower_C1, dtype = "uint8")
    upper_C1 = numpy.array(upper_C1, dtype = "uint8")
    lower_C2 = numpy.array(lower_C2, dtype = "uint8")
    upper_C2 = numpy.array(upper_C2, dtype = "uint8")
    lower_C3 = numpy.array(lower_C3, dtype = "uint8")
    upper_C3 = numpy.array(upper_C3, dtype = "uint8")
    lower_C4 = numpy.array(lower_C4, dtype = "uint8")
    upper_C4 = numpy.array(upper_C4, dtype = "uint8")

    # Create the masks to identify the colored regions.
    C1_mask = cv2.inRange(frame, lower_C1, upper_C1)
    C2_mask = cv2.inRange(frame, lower_C2, upper_C2)
    C3_mask = cv2.inRange(frame, lower_C3, upper_C3)
    C4_mask = cv2.inRange(frame, lower_C4, upper_C4)

    # Apply the mask to create the filtered image.
    filtered_C1 = cv2.bitwise_or(frame, frame, mask = C1_mask)
    filtered_C2 = cv2.bitwise_or(frame, frame, mask = C2_mask)
    filtered_C3 = cv2.bitwise_or(frame, frame, mask = C3_mask)
    filtered_C4 = cv2.bitwise_or(frame, frame, mask = C4_mask)

    # Combine the filtered images to see the "big picture".
    combined = cv2.bitwise_or(filtered_C1, filtered_C2)
    combined = cv2.bitwise_or(combined, filtered_C3)
    combined = cv2.bitwise_or(combined, filtered_C4)
   
    # Display the image data in the windows. Must be followed by waitKey().
    cv2.imshow("Original", frame)
    cv2.imshow("Filtered C1", filtered_C1)
    cv2.imshow("Filtered C2", filtered_C2)
    cv2.imshow("Filtered C3", filtered_C3)
    cv2.imshow("Filtered C4", filtered_C4)
    cv2.imshow("Combined", combined)
    
    # Wait 30 milliseconds for a key to be pressed.
    key_pressed = cv2.waitKey(30)
                
# Close the image file and close all windows.
cap.release()
cv2.destroyAllWindows()