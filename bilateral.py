import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, display it, and construct the list of bilateral
# filtering parameters that we are going to explore
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for (diameter, sigmaColor, sigmaSpace) in params:
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    title = "Blurred d={}, sc={}, ss={}".format(diameter, sigmaColor, sigmaSpace)
    cv2.imshow(title, blurred)
    cv2.waitKey(0)