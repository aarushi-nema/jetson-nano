import cv2

def nothing():
    pass

cv2.namedWindow('Blended')
cv2.createTrackbar('BlendedValue', 'Blended', 50, 100, nothing)

dispW=320
dispH=240
flip=2

#load image
cvLogo= cv2.imread('/home/aarushi/Desktop/pyPro/cv.jpg')
cvLogo= cv2.resize(cvLogo, (320,240))
cv2.imshow('Original', cvLogo)
cv2.moveWindow('Original', 0, 300)

#convert to gray color
cvLogoGray= cv2.cvtColor(cvLogo, cv2.COLOR_BGR2GRAY)

#threshold
_, BGMask= cv2.threshold(cvLogoGray, 180, 255, cv2.THRESH_BINARY)

#not of BGMask
FGMask= cv2.bitwise_not(BGMask)

#and cvLogo, mask-FGMask
FG= cv2.bitwise_and(cvLogo, cvLogo, mask= FGMask)

camSet= 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
while True:
    ret, frame= cam.read()
    #combining live video and BGMask(thresholded cvLogo)
    BG= cv2.bitwise_and(frame, frame, mask= BGMask)
    #masking coloured cvLogo on love video
    color_mask= cv2.add(BG,FG)
    #getting blend values from trackbar
    BV=cv2.getTrackbarPos('BlendedValue', 'Blended')/100
    BV2=1-BV
    print(BV)
    print(" ")
    #blending cvLogo and live video
    Blended= cv2.addWeighted(frame,BV,cvLogo, BV2, 0)
    cv2.imshow('Blended', Blended)
    cv2.moveWindow('Blended', 400, 0)

    cv2.imshow('nanoCam', frame)
    cv2.moveWindow('nanoCam', 0,0)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()