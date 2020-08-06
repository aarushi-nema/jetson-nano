import cv2
dispW=320
dispH=240
flip=2

cvLogo= cv2.imread('/home/aarushi/Desktop/pyPro/cv.jpg')
cvLogo= cv2.resize(cvLogo, (320,240))
cv2.imshow('Original', cvLogo)
cv2.moveWindow('Original', 0, 300)

cvLogoGray= cv2.cvtColor(cvLogo, cv2.COLOR_BGR2GRAY)

_,BGMask= cv2.threshold(cvLogoGray, 180, 255, cv2.THRESH_BINARY)
FGMask= cv2.bitwise_not(BGMask)
FG= cv2.bitwise_and(cvLogo, cvLogo, mask= FGMask)
cv2.imshow('FG', FG)
cv2.moveWindow('FG', 380, 0)

camSet= 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
while True:
    ret, frame= cam.read()
    BG= cv2.bitwise_and(frame, frame, mask= BGMask)
    color_mask= cv2.add(BG, FG)
    cv2.imshow('color_mask', color_mask)
    cv2.moveWindow('color_mask', 380, 300)
    cv2.imshow('nanoCam', frame)
    cv2.moveWindow('nanoCam', 0,0)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()