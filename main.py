import cv2
from HandTrackingModule import FindHands
import pyautogui

cap = cv2.VideoCapture(0)
detector = FindHands()

while True:
    succeed, img = cap.read()
    hand1_positions = detector.getPosition(img, range(21), draw=False)
    hand2_positions = detector.getPosition(img, range(21), hand_no=1, draw=False)
    for pos in hand1_positions:
        cv2.circle(img, pos, 5, (0,255,0), cv2.FILLED)
    for pos in hand2_positions:
        cv2.circle(img, pos, 5, (255,0,0), cv2.FILLED)
        
    if detector.index_finger_up(img) == "NO HAND FOUND":    
        pass
    
    elif detector.index_finger_up(img) and detector.middle_finger_up(img) and detector.ring_finger_up(img) and detector.little_finger_up(img):
        pyautogui.press('volumeup')
    else:
        pyautogui.press('volumedown')

        
    cv2.imshow("Image", img)
    if cv2.waitKey(10) == ord('q'):
        break
    