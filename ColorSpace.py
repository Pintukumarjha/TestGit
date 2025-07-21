import cv2

image=cv2.imread('lena.jpg',1)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV Image', hsv)   # Display HSV image

cv2.waitKey(0)  

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

# Wait for any key press
cv2.destroyAllWindows()        # Close the window