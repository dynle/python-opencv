import cv2
import numpy as np


# function
def draw_circle(event,x,y,flags,params):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(fix_img,(x,y),radius=50,color=(0,0,255),thickness=8)


# showing the img
fix_img = cv2.imread("../DATA/dog_backpack.jpg")
# fix_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_circle)

while True:
    cv2.imshow('my_drawing',fix_img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destoryAllWindows()