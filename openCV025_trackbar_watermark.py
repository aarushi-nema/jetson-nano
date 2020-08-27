import cv2

def nothing():
    pass
#creating a window 'watermark'
cv2.namedWindow('WaterMark')
cv2.createTrackbar('BlendedVal', 'WaterMark', 50, 100, nothing)

dispW= 320
dispH= 240
flip=2

#loading an image
cvLogo= cv2.imread('/home/aarushi/Desktop/pyPro/cv.jpg')
cvLogo= cv2.resize(cvLogo, (320,240))
cv2.imshow('Original', cvLogo)
cv2.moveWindow('Original', 0, 300)

#convert to grayscale
cvLogoGray= cv2.cvtColor(cvLogo, cv2.COLOR_BGR2GRAY)

#threshold
_,BGMask= cv2.threshold(cvLogoGray, 180, 255, cv2.THRESH_BINARY)

#black-->white (bitwise not on BGMask)
FGMask= cv2.bitwise_not(BGMask)

#Colour on FGMask
FG= cv2.bitwise_and(cvLogo, cvLogo, mask= FGMask)

camSet= 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)

while True:
    ret, frame= cam.read()
    #Black logo on live video
    BG= cv2.bitwise_and(frame, frame, mask= BGMask)
    #get BlendedVal from trackbar
    BV=cv2.getTrackbarPos('BlendedVal', 'WaterMark')/100
    BV2=1-BV 
    #Blend frame and cvLogo
    Blended= cv2.addWeighted(frame, BV, cvLogo, BV2, 0)
    #creating a blended and fgmask and
    FG2= cv2.bitwise_and(Blended, Blended, mask= FGMask)
    #watermark
    watermark= cv2.add(BG,FG2)
    cv2.imshow('nanoCam', frame)
    cv2.moveWindow('nanoCam', 0,0)
    cv2.imshow('WaterMark', watermark)
    cv2.moveWindow('WaterMark', 400,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()