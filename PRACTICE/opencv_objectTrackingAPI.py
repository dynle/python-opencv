import cv2
import numpy as np
import time

# TrackerBoosting_create(), TrackerMIL_create(), TrackerKCF_create(), TrackerTLD_create(), TrackerMedianFlow_create()
tracker = cv2.legacy.TrackerMedianFlow_create()

tracker_name = str(tracker).split()[0][1:]

cap = cv2.VideoCapture(0)
# wait for the camera to be ready
time.sleep(0.1)

ret,frame = cap.read()

# special func allows us to draw on the very first frame our desired ROI
roi = cv2.selectROI(frame,False)

# initialize tracker with first frame and bounding box
ret = tracker.init(frame,roi)

while True:
    ret,frame = cap.read()
    
    success,roi = tracker.update(frame)
    
    (x,y,w,h) = tuple(map(int,roi))
    
    if success:
        p1 = (x,y)
        p2 = (x+w,y+h)
        cv2.rectangle(frame,p1,p2,(0,255,0),3)
    else:
        # trakcing failure
        cv2.putText(frame,"Failure to Detect Tracking!",(100,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3);
        
    # display tracker type on frame
    cv2.putText(frame,tracker_name,(20,400),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3);
        
    # display result
    cv2.imshow(tracker_name,frame)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
        
cap.release()
cv2.destroyAllWindows()