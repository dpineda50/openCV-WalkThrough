import argparse
import cv2

#construct the argument parser and  parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-o", "--output", help="Name of the output image (grayscale)", default='out.jpg')
args = vars(ap.parse_args())

# load the image and conver it to grayscale
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply histogram equalization to stretch the contrast of our image
eq = cv2.equalizeHist(image)

# show out images -- notice how the contrast of the second image has
# been stretched
cv2.imshow("Original", image)
cv2.imshow("Histogram Equalization", eq)
cv2.waitKey(0)

