import mediapipe as mp
import cv2
class Handdetector:
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.results = None
    def findhand(self,img):
        self.results = self.hands.process(img)
        if self.results.multi_hand_landmarks:
            for handpoints in self.results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(img,handpoints,self.mp_hands.HAND_CONNECTIONS)
                return img
        else:
            return img
        
    def findposition(self,img):
        poslist = []
        if self.results.multi_hand_landmarks:
            myhand = self.results.multi_hand_landmarks[0]
            for id,lm in enumerate(myhand.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x * w),int(lm.y * h)
                poslist.append([id,cx,cy])
        return poslist
    def fingersup(self,poslist):
        fingers = []
        for i in range(1,21,4):
            j = i+3
            if(i == 1):
                if(poslist[i][1] > poslist[j][1]):
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
                if(poslist[i][2] > poslist[j][2]):
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers




