import cv2
import numpy as np
dispW= 320
dispH= 240
flip=2
camSet= 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
while True:
    ret, frame= cam.read()
    #gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #b=cv2.split(frame)[0]
    #g=cv2.split(frame)[1]
    #r=cv2.split(frame)[2]
    b,g,r= cv2.split(frame)
    blank= np.zeros([240,320,1], np.uint8)
    blue= cv2.merge((b, blank, blank))
    green= cv2.merge((blank, g, blank))
    red= cv2.merge((blank, blank, r))
    r[:]= r[:]*0.1
    merge= cv2.merge((r,g,b))
    cv2.imshow('merge', merge)
    cv2.moveWindow('merge', 800,0)
    cv2.imshow('Blue', blue)
    cv2.moveWindow('Blue', 0, 300)
    cv2.imshow('Green', green)
    cv2.moveWindow('Green', 400, 300)
    cv2.imshow('Red', red)
    cv2.moveWindow('Red', 400,0)
    #cv2.imshow('Gray', gray)
    #cv2.moveWindow('Gray', 400, 0)
    cv2.imshow('nanoCam', frame)
    cv2.moveWindow('nanoCam', 0,0)
    #print(gray.shape)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()













