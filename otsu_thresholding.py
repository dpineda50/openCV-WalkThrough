import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args = vars(ap.parse_args())

#load image, gray it, blur it
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow("Image", image)

# applying otsu, finds the optimal 'T' threshold value
(T, threshInv) = cv2.threshold(blurred, 0, 255,
                               cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Threshold: Otsu's value is {}".format(T), threshInv)

cv2.imshow("Output", cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)