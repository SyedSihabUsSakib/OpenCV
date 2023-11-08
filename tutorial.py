import cv2

# image = cv2.imread("C:/Users/FSMB/Downloads/ababil.jpg") #BGR

# cv2.imshow("Test Image",img)
# cv2.waitKey()

#video Reading
# cap = cv2.VideoCapture(0)

# if(cap.isOpened()):
#     while(cap.isOpened()):
#         ret, frame = cap.read()
#         if(ret == True):
#             cv2.imshow(frame)
#             if(cv2.waitKey(2)==27):
#                 break



#Mini Paint Application

import numpy  as np

draw = False
mode = True
a,b = -1,-1

def onChange(value):
     global mode
     if(value==0):
        mode = True
     else:
        mode = False
#creating mouse callback function
def draw_circle(event, x, y, flags, params):
    global a,b,draw,mode
    if(event == cv2.EVENT_LBUTTONDOWN):
        draw = True
        a,b = x,y
    elif event == cv2.EVENT_MOUSEMOVE :
        if draw:
            if mode == True:
                # global newImg
                # newImg = img.copy()
                
                cv2.rectangle(img, (a,b), (x,y),(255,255,255),-1)
            else:
                # newImg = img.copy()
                cv2.circle(img, (x,y),(a-x),(255,255,255),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        if mode == True:
                # newImg = img.copy()
                cv2.rectangle(img, (a,b), (x,y),(255,255,255),-1)
        else:
                # newImg = img.copy()
                cv2.circle(img, (x,y),(a-x),(255,255,255),-1)

#creating a black image, a window and bind the function to the window
cv2.namedWindow("Track")
cv2.createTrackbar('Shape','Track',0,1,onChange)
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow("Painter")
cv2.setMouseCallback("Painter",draw_circle)
# global newImg
# newImg = img
while(True):
    cv2.imshow('Painter',img)
    if cv2.waitKey(20)==ord('q'):
        break
cv2.destroyAllWindows()

# cv2.imshow("Painter",img)
# cv2.waitKey(0)
# cv2.imshow("Painter",image)
# cv2.waitKey(0)
# cv2.destroyWindow("Painter")