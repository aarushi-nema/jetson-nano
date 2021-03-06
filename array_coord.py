import cv2
evt=-1
coord=[]
def click (event, x, y, flags, params):
    global pnt 
    global evt
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Mouse Event Was: ', event)
        pnt=(x,y)
        coord.append(pnt)
        print(coord)
        evt=event
dispW=640
dispH=480
flip=2
cv2.namedWindow('nanoCam')
cv2.setMouseCallback('nanoCam', click)
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
while True:
    ret, frame=cam.read()
    for pnts in coord:
        cv2.circle(frame, pnts, 5, (0,0,255), -1)
        font= cv2.FONT_HERSHEY_PLAIN
        myStr= str(pnts)
        cv2.putText(frame, myStr, pnts, font, 1, (255,0,0), 2 )   
    keyEvent= cv2.waitKey(1)
    cv2.imshow('nanoCam', frame)
    if keyEvent == ord('q'):
        break
    if keyEvent == ord('c'):
        coord=[]
cam.release()
cv2.destroyAllWindows()    