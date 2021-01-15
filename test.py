import numpy as np
import cv2
import time

stop_cascade = cv2.CascadeClassifier('stop.xml')
turn_right_cascade = cv2.CascadeClassifier('turn_right.xml')

cap = cv2.VideoCapture(0)
time.sleep(1)

frame_rate_calc = 1
freq = cv2.getTickFrequency()

while 1:
        t1 = cv2.getTickCount()
        ret, img = cap.read()
        resize = cv2.resize(img,(320,240))
        gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

        stop = stop_cascade.detectMultiScale(gray,1.4,6)
        turn_right = turn_right_cascade.detectMultiScale(gray,1.08,4)   

        for (x,y,w,h) in stop:
                cv2.rectangle(resize,(x,y),(x+w,y+h),(255,0,0),2)
                print('Found stop')

        for (x,y,w,h) in turn_right:
                cv2.rectangle(resize,(x,y),(x+w,y+h),(0,255,0),2)
                print('Found turn_right')
        
        cv2.putText(resize,"FPS: {0:.2f}".format(frame_rate_calc),(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1,cv2.LINE_AA)
        cv2.imshow('img',resize) 

        t2 = cv2.getTickCount()
        time1 = (t2-t1)/freq
        frame_rate_calc = 1/time1
       
        if cv2.waitKey(30) & 0xff == 27:
                break

cap.release()
cv2.destroyAllWindows()
