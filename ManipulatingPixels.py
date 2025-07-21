import cv2

image=cv2.imread('lena.jpg',1)

#print(image)

# this is for manipulating with pixels

'''image[100,100]=(255,255,255)

cv2.imshow('image',image)
cv2.waitKey(0)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cv2.destroyAllWindows()



#print(image[100,100])'''

# this is for get the size of image

print(image.shape)
print(image.size)

a=image[0:100,0:100]

image[100:200,100:200]=a

cv2.imshow('image',image)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cv2.destroyAllWindows()