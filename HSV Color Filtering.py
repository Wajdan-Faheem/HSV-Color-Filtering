import cv2 as cv
import numpy as np
def nothing(x): 
    print(x)
cap = cv.VideoCapture(0)

cv.namedWindow('Tracking')

#Lower Range
cv.createTrackbar('Low_Hue','Tracking', 0,255,nothing)
cv.createTrackbar('Low_Saturation','Tracking', 0,255,nothing)
cv.createTrackbar('Low_Value','Tracking', 0,255,nothing)

#Higher Range
cv.createTrackbar('Up_Hue','Tracking', 255,255,nothing)
cv.createTrackbar('Up_Saturation','Tracking', 255,255,nothing)
cv.createTrackbar('Up_Value','Tracking', 255,255,nothing)

while cap.isOpened():
    _,frame = cap.read()

    #Upper Range
    Up_HUE = cv.getTrackbarPos('Up_Hue', 'Tracking')
    Up_SATURATION = cv.getTrackbarPos('Up_Saturation', 'Tracking')
    Up_VALUE = cv.getTrackbarPos('Up_Value', 'Tracking')

    #Lower Range    
    Low_HUE = cv.getTrackbarPos('Low_Hue', 'Tracking')
    Low_SATURATION = cv.getTrackbarPos('Low_Saturation', 'Tracking')
    Low_VALUE = cv.getTrackbarPos('Low_Value', 'Tracking')

    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    Lower_Bound = np.array([Low_HUE,Low_SATURATION,Low_VALUE])
    Upper_Bound = np.array([Up_HUE,Up_SATURATION,Up_VALUE]) 

    mask = cv.inRange(hsv, Lower_Bound,Upper_Bound)

    #Apply mask

    Final_Frame = cv.bitwise_and(frame,frame,mask=mask)

    cv.imshow('frame',frame)
    cv.imshow('mask', mask)
    cv.imshow('res',Final_Frame)

    k = cv.waitKey(1)
    if k == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
