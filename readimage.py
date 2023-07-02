import cv2 

#read image
img = cv2. imread('solar-system.jpg')

#displaying image
#cv2. imshow('Display Image', img)

# Convert Colored Image To Grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#cv2. imshow('Display gray Image', gray_img)

#print(img)
print(gray_img)

cv2. waitKey(0)