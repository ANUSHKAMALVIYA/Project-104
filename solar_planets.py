import cv2 

img= cv2.imread('solar-system.jpg')

solarsystem = img[120:360,400:500]

img[0:240, 500:600] = solarsystem

text_to_show = "solar_system"

cv2.putText(img,  
           "sun",
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Mercury",
           (0, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Venus",
           (2, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Mars",
           (3, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Earth",
           (5, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Jupiter",
           (7, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Saturn",
           (8, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Uranus",
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Neptune",
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )
cv2.imshow("output",img)

cv2.waitKey(0)