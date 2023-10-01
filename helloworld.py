# Source: https://www.geeksforgeeks.org/introduction-to-opencv/

import cv2

def displayImage(file):
    cv2.imshow("Display", file)
    cv2.waitKey(0)      # waits for keypress to close window


# create a window to look at our images later
cv2.namedWindow("Display", cv2.WINDOW_AUTOSIZE)

image = cv2.imread('data/road.jpg')
displayImage(image)

h,w = image.shape[:2]   # 1st 2 vals stored in image r height n width
                        # counted in pixels (checked img properties)
print("Height = {}, Width = {}".format(h,w))

# extract RGB vals of indiv pixel
# OpenCV arranges channels in BGR order, 0th val is Blue not Red

(B, G, R) = image[100,100]      # pixel at 100, 100
print("R = {}, G = {}, B = {}".format(R,G,B))

# pass the channel to extract the val for specific channel
B = image[100,100,0]    # next 3 vals after pixel's H&W are B,G,R
print("B = {}".format(B))

# Extracting region of interest (ROI)
roi = image[100:500, 200:700]   # slicing pixels of image gives ROI
displayImage(roi)

# Resizing image
# resize() takes 2 params, image and dimensions
resize = cv2.resize(image, (800,800))   # aspect ratio not maintained
displayImage(resize)

# Resizing img with aspect ratio maintained
ratio = 800/w
dim = (800, int(h*ratio))
resize_aspect = cv2.resize(image, dim)  # maintains aspect ratio!
displayImage(resize_aspect)

# Rotating image
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, -45, 1.0)  # gen rotation matrix
rotated = cv2.warpAffine(image, matrix, (w, h))     # performing affine transformation
# getRotationMatrix2D() takes 3 args: center coords, angle in deg to rotate, scaling factor
#   returns 2x3 matrix of values derived from alpha (scale * cos(angle)) and beta (scale * sin(angle))
# warpAffine transforms source img using rotation matrix,
#   calculates new x,y coords of img and transforms it
displayImage(rotated)

# Drawing a Rectangle - in-place operation
# Displaying text - in-place operation
output = image.copy()
rectangle = cv2.rectangle(output, (1500, 900),(600,400),(255,0,0),4)
text = cv2.putText(output, "Hello world", (250,300),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,4,(0,0,255),2)
# rectangle drawn needs 2 vertices, color, linewidth
# text needs start bottom left corner coord, font, size, color, linewidth
displayImage(output)

cv2.destroyAllWindows()