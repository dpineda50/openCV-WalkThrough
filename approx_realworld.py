import cv2

image = cv2.imread("images/dog.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 75, 200)

cv2.imshow("Original", image)
cv2.imshow("Edge Map", edged)
cv2.waitKey(0)

(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:7]
for c in cnts:
    # approximate the contour and initialize the contour color
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.1 * peri, True)

    # show the difference in number of vertices between the original
    # and the approximated contours
    print "original: {}, approx: {}".format(len(c), len(approx))

    # if the approximated contour has 4 vertices, then we ahve found
    # our rectangle
    if len(approx) == 4:
        # draw the outline on the image
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)

cv2.imshow("Output", image)
cv2.waitKey(0)

