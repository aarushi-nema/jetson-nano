import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars', 400, 0)

cv2.createTrackbar('hueLower', 'Trackbars', 50, 179, nothing)
cv2.createTrackbar('hueHigher', 'Trackbars', 100, 179, nothing)
cv2.createTrackbar('satLower', 'Trackbars', 100, 255, nothing)
cv2.createTrackbar('satHigher', 'Trackbars', 255, 255, nothing)
cv2.createTrackbar('valLower', 'Trackbars', 100, 255, nothing)
cv2.createTrackbar('valHigher', 'Trackbars', 255, 255, nothing)

dispW= 640
dispH= 480
flip=2
camSet= 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam= cv2.VideoCapture(camSet)
while True:
    #ret, frame= cam.read()
    smarties= cv2.imread('smarties.png')
    smarties= cv2.resize(smarties, (320, 240))
    cv2.imshow('smarties', smarties)
    cv2.moveWindow('smarties', 0,0)
    
    hsv= cv2.cvtColor(smarties, cv2.COLOR_BGR2HSV)
    
    hueLow= cv2.getTrackbarPos('hueLower', 'Trackbars')
    hueHigh= cv2.getTrackbarPos('hueHigher', 'Trackbars')
    
    satLow= cv2.getTrackbarPos('satLower', 'Trackbars')
    satHigh= cv2.getTrackbarPos('satHigher', 'Trackbars')
    
    valLow= cv2.getTrackbarPos('valLower', 'Trackbars')
    valHigh= cv2.getTrackbarPos('valHigher', 'Trackbars')

    l_b= np.array([hueLow, satLow, valLow])
    u_b= np.array([hueHigh, satHigh, valHigh])

    FGMask= cv2.inRange(hsv, l_b, u_b)
    cv2.imshow('FGMask', FGMask)
    cv2.moveWindow('FGMask', 0, 350)
    
    FG= cv2.bitwise_and(smarties, smarties, mask= FGMask)
    cv2.imshow('FG', FG)

    if cv2.waitKey(1)  == ord('q'):
        break
cam.release()
cv2.destroyAllWindow()