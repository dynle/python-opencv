import cv2
import numpy as np
import matplotlib.pyplot as plt

birds = cv2.imread('photobooth-bird-tumblr.png', cv2.IMREAD_UNCHANGED)
print("birds shape: ",birds.shape)
birds_width = birds.shape[1]
birds_height = birds.shape[0]

print('birds dimensions (HxW)',int(birds_height),"x",int(birds_width))

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect_face(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img)
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),10)
        
    return face_img

def adj_detect_face(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img,scaleFactor=1.2,minNeighbors=5)
    for (x,y,w,h) in face_rects:
        # cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),10)
        face_img[y-150:y-150+birds_height,x-110:x-110+birds_width,:] += birds[:,:,:3]
        # face_img[y:y+birds_height,x:x+birds_width-(birds_width-w)//2,:] += birds[:,:,:3]

    return face_img

cap = cv2.VideoCapture(0)

# get frame dimensions
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print('frame dimensions (HxW)',int(frame_height),"x",int(frame_width))

while True:
    ret,frame = cap.read(0)
    # print("frame shape: ",frame.shape)
    frame = adj_detect_face(frame)
    
    # masking red channel
    # frame[0:birds_height,0:birds_width,0] *= 1 - birds[:,:,3]
    # # masking green channel
    # frame[0:birds_height,0:birds_width,1] *= 1 - birds[:,:,3]
    # # masking blue channel
    # frame[0:birds_height,0:birds_width,2] *= 1 - birds[:,:,3]
    
    # now finally add the image in that mask
    # frame[0:birds_height,0:birds_width,:] += birds[:,:,:3]
    # frame[0:birds_height,0:birds_width,:] = birds
    
    cv2.imshow('VIDEO FACE DETECT',frame)
    
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()