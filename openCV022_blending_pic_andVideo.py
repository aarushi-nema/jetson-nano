import cv2
dispW=320
dispH=240
flip=2

#load image into cvLogo
cvLogo= cv2.imread('/home/aarushi/Desktop/pyPro/cv.jpg')
cvLogo= cv2.resize(cvLogo, (320, 240))
cv2.imshow('Original', cvLogo)
cv2.moveWindow('Original', 0, 300)

camSet= 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)

while True:
    ret, frame= cam.read()

    #blended live stream creation
    Blended= cv2.addWeighted(frame, 0.5, cvLogo, 0.5, 0)
    cv2.imshow('watermark', Blended)
    cv2.moveWindow('watermark', 380,0)

    cv2.imshow('nanoCam', frame)
    cv2.moveWindow('nanoCam', 0,0)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()