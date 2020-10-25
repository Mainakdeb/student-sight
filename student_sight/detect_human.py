
import cv2
import numpy as np
#We are using OpenCV to achieve object detection from live frame

face_cascade = cv2.CascadeClassifier('student_sight/haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')
cap =  cv2.VideoCapture(-1)

def look_for_human(fcap = cap , ace_cascade = face_cascade):

    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray,5,1,1)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5,minSize=(50,50))
     
    if len(faces)!= 0:
        return True
    else:
        return False


