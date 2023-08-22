import cv2
import numpy as np


def empty(a):
    pass

'''def get_contours(img,imgc,Name):
    contours,hierarchy= cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    L=[]
    for i in contours:
        Ar=cv2.contourArea(i)
        #print(Ar)
        L.append(Ar)
        cv2.drawContours(imgc,i,-1,(0,0,255),3)
    cv2.imshow(Name, imgc)

    return L

def counter(L):

    J=0
    for i in L:
        J+=1
    print(J)




#loading image

Path= "Mate_resources/Before.png"
Path2= "Mate_resources/After.png"


cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",640,340)

cv2.createTrackbar("Hmin","Trackbar",0,179,empty)
cv2.createTrackbar("Hmax","Trackbar",179,179,empty)
cv2.createTrackbar("Smin","Trackbar",0,255,empty)
cv2.createTrackbar("Smax","Trackbar",255,255,empty)
cv2.createTrackbar("Vmin","Trackbar",0,255,empty)
cv2.createTrackbar("Vmax","Trackbar",255,255,empty)


img = cv2.imread(Path)

img2 = cv2.imread(Path2)

imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img2hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)


lower = np.array([0, 0, 229])
upper = np.array([158, 7, 255])

mask = cv2.inRange(imghsv,lower,upper)
mask2 = cv2.inRange(img2hsv, lower, upper)

imgcan=cv2.Canny(mask,50,50)
imgcan2=cv2.Canny(mask2,50,50)

L = get_contours(imgcan,img,"Before")
X = get_contours(imgcan2,img2,"After")

counter(L)
counter(X)

cv2.imshow("Before_Can", imgcan)
cv2.imshow("After_Can", imgcan2)
#cv2.imshow("Before", imgc)
#cv2.imshow("After", imgc2)
cv2.imshow("After_mask", mask2)
cv2.imshow("Before_mask", mask)
#cv2.imshow("seagrass_hsv", imghsv)
#cv2.imshow("seagrass_hsv2", img2hsv)

cv2.waitKey(0)'''


Path= "Mate_resources/Before.png"
Path2= "Mate_resources/After.png"


cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",640,340)

cv2.createTrackbar("Hmin","Trackbar",0,179,empty)
cv2.createTrackbar("Hmax","Trackbar",179,179,empty)
cv2.createTrackbar("Smin","Trackbar",0,255,empty)
cv2.createTrackbar("Smax","Trackbar",255,255,empty)
cv2.createTrackbar("Vmin","Trackbar",0,255,empty)
cv2.createTrackbar("Vmax","Trackbar",255,255,empty)

while True:
    img = cv2.imread(Path)

    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)




    h_min = cv2.getTrackbarPos("Hmin","Trackbar")
    h_max = cv2.getTrackbarPos("Hmax", "Trackbar")
    s_min = cv2.getTrackbarPos("Smin", "Trackbar")
    s_max = cv2.getTrackbarPos("Smax", "Trackbar")
    v_min = cv2.getTrackbarPos("Vmin", "Trackbar")
    v_max = cv2.getTrackbarPos("Vmax", "Trackbar")

    #print(h_min,h_max,s_min,s_max,v_min,v_max)


    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    """lower = np.array([0, 0, 229])
    upper = np.array([158, 7, 255])"""

    mask = cv2.inRange(imghsv,lower,upper)

    imgcan=cv2.Canny(mask,50,50)




    #cv2.imshow("seagrass_original", img)
    cv2.imshow("seagrass_hsv", imghsv)
    cv2.imshow("seagrass_mask", mask)
    #cv2.imshow("seagrass_original2", img2)



    cv2.waitKey(1)