import cv2
dispW=320
dispH=240
flip=2
#reading the image and storing it in cvLogo
cvLogo= cv2.imread('/home/aarushi/Desktop/pyPro/cv.jpg')
#resizing the image
cvLogo= cv2.resize(cvLogo,(320,240))
cv2.imshow('Original', cvLogo)
cv2.moveWindow('Original', 300, 290)

#for thresholding we need to convert the image to grayscale
cvLogoGray= cv2.cvtColor(cvLogo, cv2.COLOR_BGR2GRAY)
#display image
cv2.imshow('GrayLogo', cvLogoGray)
cv2.moveWindow('GrayLogo', 0, 300)
#for .threshold first argument is the source image
#second is the threshold  is the thrshold limit
# thrid is the maximum value assigned to the pixels exceeding threshold value  
_,BGMask=cv2.threshold(cvLogoGray, 180, 255, cv2.THRESH_BINARY)
cv2.imshow('BGMask', BGMask)
cv2.moveWindow('BGMask', 340, 0)
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
while True:
    ret, frame= cam.read()
    cv2.imshow('nanoCam', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()        