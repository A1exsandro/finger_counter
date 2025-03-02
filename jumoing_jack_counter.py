import cv2
import mediapipe as mp


video = cv2.VideoCapture(2)

while True:
  success, img = video.read()
  videoRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  
  cv2.imshow('Result', img)
  cv2.waitKey(2)
  