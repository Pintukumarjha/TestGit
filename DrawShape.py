import cv2

image=cv2.imread('lena.jpg',1)

cv2.line(image,(0,0),(400,400),(255,0,0),5)
cv2.rectangle(image,(0,0),(400,400),(0,255,0),5)
cv2.circle(image,(200,200),100,(0,0,255),-1)

font=cv2.FONT_HERSHEY_COMPLEX

cv2.putText(image,"Hello",(100,100),font,4,(255,255,255),cv2.LINE_AA)
cv2.putText(image,"There",(100,220),font,4,(255,255,255),cv2.LINE_AA)

cv2.imshow('image',image)

#cv2.waitKey(10000)
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cv2.destroyAllWindows()