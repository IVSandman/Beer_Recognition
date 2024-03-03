import cv2
import numpy as np

# Define BGR color ranges for IPA, Lager, and Stout beer glasses
amber_color_bgr = np.array([35, 40, 55])  # Green color for IPA
lager_color_bgr = np.array([85, 255, 255])  # Red color for Lager
dunkel_color_bgr = np.array([11, 15, 20]) #Sample 2 # Black
#stout_color_bgr = np.array([37, 30, 37])
#stout_color_bgr = np.array([32,34,42])
min_contour_area = 650 # Minimum contour area to display the name tag

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    # Convert BGR colors to HSV colors
    amber_color_hsv = cv2.cvtColor(np.uint8([[amber_color_bgr]]), cv2.COLOR_BGR2HSV)[0][0]
    lager_color_hsv = cv2.cvtColor(np.uint8([[lager_color_bgr]]), cv2.COLOR_BGR2HSV)[0][0]
    dunkel_color_hsv = cv2.cvtColor(np.uint8([[dunkel_color_bgr]]), cv2.COLOR_BGR2HSV)[0][0]

    # Threshold the frame based on HSV color ranges
    amber_mask = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV),
                           np.array([amber_color_hsv[0] - 10, 100, 100]),
                           np.array([amber_color_hsv[0] + 10, 255, 255]))

    lager_mask = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV),
                           np.array([lager_color_hsv[0] - 10, 100, 100]),
                           np.array([lager_color_hsv[0] + 10, 255, 255]))

    dunkel_mask = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV),
                           np.array([dunkel_color_hsv[0] - 20, 10, 10]),
                           np.array([dunkel_color_hsv[0] + 10, 115, 115]))

    #stout_mask = cv2.inRange(frame, stout_color_bgr - np.array([10, 10, 10]), stout_color_bgr + np.array([10, 10, 10]))

    # Find contours in the masks and draw squares around detected beer glasses
    contours_amber, _ = cv2.findContours(amber_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours_amber:
        if cv2.contourArea(contour) > min_contour_area:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, 'Amber Ale', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    contours_lager, _ = cv2.findContours(lager_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours_lager:
        if cv2.contourArea(contour) > min_contour_area:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, 'Lager', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    contours_dunkel, _ = cv2.findContours(dunkel_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours_dunkel:
        if cv2.contourArea(contour) > min_contour_area:
           x, y, w, h = cv2.boundingRect(contour)
           cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
           cv2.putText(frame, 'Dunkel', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    #contours_stout, _ = cv2.findContours(stout_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #for contour in contours_stout:
        #if cv2.contourArea(contour) > min_contour_area:
            #x, y, w, h = cv2.boundingRect(contour)
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (178, 52, 174), 2)
            #cv2.putText(frame, 'Stout', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2)

    cv2.imshow('Beer Glass Detection_2', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
