import numpy as np
import cv2


image = cv2.imread("images/more_shapes_example.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]

cv2.imshow("Original", image)
cv2.imshow("Gray", gray)
cv2.imshow("Thresh", thresh)

cv2.waitKey(0)
# find the external contours in the thresholded image and allocate memory
# for the convex hull image
(_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
hullImage = np.zeros(gray.shape[:2], dtype="uint8")

for (i, c) in enumerate(cnts):
    # compute the area of the contour along with the bounding box
    # to compute the aspect ratio
    area = cv2.contourArea(c)
    (x, y, w, h) = cv2.boundingRect(c)

    # compute the aspect ratio of the contour, which is simply the width
    # divided by the height of the bounding box
    aspectRatio = w / float(h)

    # use the area of the contour and the bounding box area to compute the extent
    extent = area / float(w * h)

    # compute the convex hull of the contour, then use the area of the
    # original contour and the area of the convex hull to compute the solidity
    hull = cv2.convexHull(c)
    hullArea = cv2.contourArea(hull)
    solidity = area / float(hullArea)

    # visualize the original contours and the convex hull and initialize
    # the name of the shape
    cv2.drawContours(hullImage, [hull], -1, 255, -1)
    cv2.drawContours(image, [c], -1, (240, 0, 159), 3)
    shape = "?"

    if aspectRatio >= 0.98 and aspectRatio <= 1.02:
        shape = "SQUARE"

    # width greater than the height
    elif aspectRatio >= 3.0 or aspectRatio <= 0.35:
        shape = "RECTANGLE"

    # solidity is sufficiently small, then we have a L-piece
    elif extent <= 0.65:
        shape = "L-PIECE"

    # if the solidity is sufficiently large, then we have a z-Piece
    elif solidity > 0.8:
        shape = "Z-PIECE"

    cv2.putText(image, shape, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                (240, 0, 159), 2)

    print "Contour #%d -- aspect ratio=%.2f, extent = %.2f, solidity=%.2f" % \
          (i + 1, aspectRatio, extent, solidity)
    cv2.imshow("Convex Hull", hullImage)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

