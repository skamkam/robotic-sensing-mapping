# Sarah Kam
# Morphological Processing notes and demonstration

# References:
# https://medium.com/perspectivesondatascience/preprocessing-with-computer-vision-part-vii-morphological-operations-ca850a701ea8
# https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html

"""
Morphological operations operate on an image - in this example, a black and white
image - to change the "foreground" (here, white pixels) in relation to the "background"
(here, black pixels).

We use morphological operations to pre-process or "clean" images. They can be used to perform:
- erosion: erode the boundaries of the foreground object
- dilation: dilate the foreground object
- opening: remove noise by eroding then dilating
- closing: fill in small holes in the foreground object by dilating then eroding
- gradient: finding an outline of the object by subtracting erosion from dilation
- top hat: finding objects "brighter" than surroundings by subtracting opened from original
- black hat: finding objects "darker" than surroundings by subtracting closed from original
"""

import cv2 as cv
import numpy as np

def displayImage(file):
    pass

def displayImage2(file):
    cv.imshow("Display", file)
    cv.waitKey(0)      # waits for keypress to close window

# create a window to look at our images later
cv.namedWindow("Display", cv.WINDOW_AUTOSIZE)

img = cv.imread('data/csc353_tree.png')
assert img is not None, "file could not be read, check with os.path.exists()"
displayImage(img)

# Create a kernel of 3x3 array filled with ones
kernel = np.ones((5,5),np.uint8)

# Erosion
erosion = cv.erode(img,kernel,iterations = 1)
displayImage(erosion)

# Dilation
dilation = cv.dilate(img,kernel,iterations = 1)
displayImage(dilation)

# Opening
#   opening by calling morphologyEx and MORPH_OPEN
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
displayImage(opening)
#   opening by explicitly eroding then dilating
opening2 = cv.dilate(erosion, kernel, iterations=1)
displayImage(opening2)

# Closing
#   closing by calling morphologyEx and MORPH_CLOSE
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
displayImage(closing)
#   closing by explicitly dilating then eroding
closing2 = cv.erode(dilation, kernel, iterations=1)
displayImage(closing2)

# Morphological Gradient
#   gradient by calling morphologyEx and MORPH_GRADIENT
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
displayImage(gradient)
#   gradient by subtracting the erosion of the image from the dilation
gradient2 = cv.subtract(dilation, erosion)
displayImage(gradient2)

# Top Hat Transformation
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
displayImage(tophat)
#   by subtracting the opened image from original
tophat2 = cv.subtract(img, opening)
displayImage(tophat2)

# Black Hat Transformation
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
displayImage2(blackhat)
#   by subtracting the closed image from original
blackhat2 = cv.subtract(img, closing)
displayImage2(blackhat2)