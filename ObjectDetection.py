import cv2
import numpy as np

image=cv2.imread('blue.jpg',1)

new_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

cv2.imshow('image',new_image)

cv2.waitKey(0)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cv2.destroyAllWindows()