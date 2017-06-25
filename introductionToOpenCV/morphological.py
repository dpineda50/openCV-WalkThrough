import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

#applying erosions
for i in xrange(0,3):
    eroded = cv2.erode(gray.copy(), None, iterations=i+1)
    cv2.imshow("Eroded {} times".format(i+1), eroded)
    cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Original", image)

#apply a series of dilations
for i in xrange(0,3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i+1)
    cv2.imshow("Dilated {} times".format(i+1), dilated)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (5, 5), (7, 7)]

#loop over kernels and apply opening operation
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernelSize)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSize[1]), opening)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing: ({}, {})".format(kernelSize[0], kernelSize[1]), closing)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)
#applying a morphological gradient operation
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Gradient: ({}, {})".format(kernelSize[0], kernelSize[1]), gradient)
    cv2.waitKey(0)
