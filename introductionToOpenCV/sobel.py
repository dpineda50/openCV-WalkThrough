import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="PAth to image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

#computing gradients
gX = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0)
gY = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=0, dy=1)

#convert gradients into 8-bit representations
gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

#combine images
sobelCombined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)

cv2.imshow("Sobel X", gX)
cv2.imshow("Sobel Y", gY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)