import cv2

image = cv2.imread("butterfly.jpg") #read the image

#image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #convert the color

image = cv2.bitwise_not(image,cv2.COLOR_BGR2GRAY) # we can also use bitwise_not instead of cvtColor. It inverts the bits for the color

cv2.imshow("This is Processed Image", image) #show the processed image

cv2.waitKey(0) #tells cv2 to wait for an event
cv2.destroyAllWindows()