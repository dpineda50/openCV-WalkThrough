from matplotlib import pyplot as plt
import numpy as np
import cv2

def plot_histogram(image, title, mask=None):
    # grab the image channels, initlaize the tupe of colors and
    # the figure
    chans = cv2.split(image)
    colors = ("b", "r", "g")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    # loop over the image channels
    for (chan, color) in zip(chans, colors):
        # create a histogram for the current channel and plot it
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])


#load the image and plot a histogram for it
image = cv2.imread("images/horseshoe_bend.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
plot_histogram(image, "Histogram for Original Image")

#construct a mask for out image -- our mask will be BLACK for regions
# we want to IGNORE and WHITE for regions we want to EXAMINE

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (20, 50), (210, 90), 255, -1)
cv2.imshow("Mask", mask)

# what does masking our image look like?
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Applying the mask", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()

plot_histogram(image, "Histogram for Masked Image", mask=mask)

plt.show()