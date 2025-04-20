import cv2
import numpy as np

# Read the image and convert it to grayscale
img = cv2.imread('rose.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Read the blank image
blank = cv2.imread("white-bg.jpg")

# Initial thresholding to create the 'thresh' variable
ret, thresh = cv2.threshold(gray_img, 127, 255, 0)


# Callback function for the trackbar
def change_thresh(val):
    global thresh, gray_img, blank
    ret, thresh = cv2.threshold(gray_img, val, 255, 0)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Make a copy of blank for drawing contours
    blank_with_contours = blank.copy()
    cv2.drawContours(blank_with_contours, contours, -1, (0, 0, 255), 2)

    cv2.imshow("Binary Image", thresh)
    cv2.imshow('Original with Contours', blank_with_contours)


# Create a window named "threshold" for the trackbar
cv2.namedWindow("threshold")
cv2.resizeWindow("threshold", 800, 800)

# Create the trackbar
cv2.createTrackbar("threshold", "threshold", 127, 255, change_thresh)

# Display the original and grayscale images
cv2.imshow('Original', img)
cv2.imshow("Gray-Scale", gray_img)
cv2.imshow("Binary Image", thresh)
cv2.imshow('Original with Contours', blank)

# Wait for a key press and destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()