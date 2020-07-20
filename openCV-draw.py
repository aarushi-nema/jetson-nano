import cv2
dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
while True:
    ret, frame= cam.read()
    frame=cv2.rectangle(frame, (300,220),(340,260), (255,0,0), 4)
    frame=cv2.circle(frame,(140,100),50,(0,255,0),4)
    frame=cv2.circle(frame,(400,100),30,(0,0,255),-1)
    fnt=cv2.FONT_HERSHEY_DUPLEX
    frame=cv2.putText(frame, 'My first text', (200,200),fnt,1,(255,0,150),2)
    frame=cv2.line(frame,(10,10),(630,470),(150,0,200),5)
    frame=cv2.arrowedLine(frame,(110,100),(630,470),(255,255,255),4)
    cv2.imshow('nanoCam', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()