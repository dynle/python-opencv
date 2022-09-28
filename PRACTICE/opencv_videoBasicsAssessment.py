'''
Guide

1.Create a draw_circle function for the callback function
2.Use two events cv2.EVENT_LBUTTONDOWN and cv2.EVENT_LBUTTONUP
3.Use a boolean variable to keep track if the mouse has been clicked up and down based on the events above
4.Use a tuple to keep track of the x and y where the mouse was clicked.
5.You should be able to then draw a circle on the frame based on the x,y coordinates from the Event
'''

# Create a function based on a CV2 Event (Left button click)
import cv2

# mouse callback function
def draw_circle(event,x,y,flags,param):

    global center,clicked

    # get mouse click on down and track center
    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x,y)
        clicked = False
        
    # Use boolean variable to track if the mouse has been released
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


        
# Haven't drawn anything yet!
center = (0,0)
clicked = False

# Capture Video
cap = cv2.VideoCapture(0)

# Create a named window for connections
cv2.namedWindow('Program')

# Bind draw_rectangle function to mouse cliks
cv2.setMouseCallback('Program',draw_circle)


while True:
    # Capture frame-by-frame
    ret,frame = cap.read()

    # Use if statement to see if clicked is true
    if clicked:
        # Draw circle on frame
        cv2.circle(frame,center,70,(255,0,0),5)
        
    # Display the resulting frame
    cv2.imshow('Program',frame)
    
    # This command let's us quit with the "q" button on a keyboard.
    # Simply pressing X on the window won't work!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cap.destroyAllWindows()
