import cv2

image = cv2.imread("images/contours_circles_and_squares.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# find the contours in the image
(_, cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
count = 0
# loop over the contours
for c in cnts:
    # approx the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, .01 * peri, True)

    # if the approximated contour has 4 vertices, then we are examining
    # a rectangle
    if True:#len(approx) == 4:
        count += 1
        # draw the outline of the contour and draw the text on the image
        cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.putText(image, "Rectangle", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 255, 0), 2)
print "%d rectangles were found!" % (count)
cv2.imshow("Image", image)
cv2.waitKey(0)