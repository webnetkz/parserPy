import numpy as np
import face_recognition
import cv2
import os

path = 'faces'
images = []
classNames = []
myList = os.listdir(path)
print(myList)