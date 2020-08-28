import cv2
dispW=640
dispH=480
flip=2
camSet= 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)

#load image
PL= cv2.imread('/home/aarushi/Desktop/pyPro/pl.jpg')
PL= cv2.resize(PL, (75, 75))
cv2.imshow('Original', PL)
cv2.moveWindow('Original', 700,0)

#convert to grayscale
PLGray= cv2.cvtColor( PL, cv2.COLOR_BGR2GRAY)

#thresholding
_, BGMask= cv2.threshold(PLGray, 240, 255, cv2.THRESH_BINARY)

#creating foreground mask
FGMask= cv2.bitwise_not(BGMask)

#creating forground
FG= cv2.bitwise_and(PL, PL, mask= FGMask)
cv2.imshow('FG', FG)
cv2.moveWindow('FG', 800, 200)

#defining dimentions of the moving box
BW=75
BH=75
XPos=10
YPos=10
dX=1
dY=1

while True:
    ret, frame= cam.read()
    #creating region of interest
    ROI= frame[YPos:YPos+BH, XPos:XPos+BW]
    #masking BGMask on region of interest
    ROIBG= cv2.bitwise_and(ROI, ROI, mask= BGMask)
    #combining ROI with the coloured logo
    ROInew= cv2.add(FG, ROIBG)
    #getting the ROI+logo combination on live video
    frame[YPos:YPos+BH, XPos:XPos+BW]=ROInew
    XPos=XPos+dX
    YPos=YPos+dY
    if(XPos+BW>=640 or XPos<=0):
        dX=dX*(-1)
    if(YPos+BH>=480 or YPos<=0):
        dY=dY*(-1)

    cv2.imshow('nanoCam', frame)
    cv2.moveWindow('nanoCam', 0,0)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()