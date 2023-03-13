import cv2
import handdetector as ha
cam = cv2.VideoCapture(0)
h = ha.Handdetector()
while(True):
    suc,img = cam.read()
    img = cv2.flip(img,1)
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = h.findhand(img)
    poslist = h.findposition(img)
    if(poslist):
        fingers = h.fingersup(poslist)
        if(fingers == [1,1,1,1,1]):
            print("paper")
        elif(fingers == [0,0,0,0,0]):
            print("stone")
        elif(fingers == [0,1,1,0,0]):
            print("scissor")
        else:
            pass
    cv2.imshow("Hands",img)
    if(cv2.waitKey(10) == ord('a')):
        break 
cam.release()
cv2.destroyAllWindows()