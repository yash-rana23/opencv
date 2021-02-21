import cv2
import numpy as np
import math

def nothing(x):
    # any operation
    pass


cap = cv2.VideoCapture(0)
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("L-S", "Trackbars", 66, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 134, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 180, 180, nothing)
cv2.createTrackbar("U-S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 243, 255, nothing)
font = cv2.FONT_HERSHEY_COMPLEX
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")

    # Red color
    low_red = np.array([0, 77, 255])
    high_red = np.array([180, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    cv2.imshow("output", red)
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    areas = [cv2.contourArea(c) for c in contours]
    for cnt in contours:

      epsilon = 0.1 * cv2.arcLength(cnt, True)
      approx = cv2.approxPolyDP(cnt, epsilon, True)

      n = approx.ravel()
      i = 0

      for j in n:
          if(i % 2 == 0):
             x = n[i]
             y = n[i + 1]


           # String containing the co-ordinates.
             string = str(x) + " " + str(y)

             if (i == 0):
                # text on topmost co-ordinate.
                cv2.putText(frame, "Arrow tip", (x, y), font, 0.5, (255, 0, 0))

                atan = math.atan2(y, x)
                angle = math.degrees(atan)
                print("angle=", angle)
      i = i + 1

    cv2.imshow("output1", red)



    key = cv2.waitKey(1)
    if key == 27:
     break