Self-driving Car Engineer

Term 1
Project: Advanced Lane Finding

Calibrating your camera (#10)

---
import glob
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
%matplotlib inline


# Read in and make a list of calibration images
images = glob.glob('../calibration_images/calibration*.jpg')


# Read in a single calibration image
img = mpimg.imread('../calibration_images/calibration1.jpg')
plt.imshow(img)

# Arrays to store object points and image points from all the images
objpoints = [] # 3D points in real world space
imgpoints = [] # 2D points in image plane

# Prepare object points, like (0,0,0), (1,0,0), (2,0,0) ..., (7,5,0)
objp = np.zeros((6*8,3), np.float32)
objp[:,:2] = np.mgrid[0:8,0:6].T.reshape(-1,2) # x,y coordinates, shaped back into two columns

# Iterate through the files
for fname in images:
	# Read in each image
	img = mpimg.imread(fname)

	# Convert image to grayscale
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	# Find the chessboard corners
	ret, corners = cv2.findChessboardCorners(gray, (8,6), None)

	# If corners are found, add object points, image points
	if ret == True:
		imgpoint.append(corners)
		objpoints.append(objp)

		# Draw and display the corners
		img = cv2.drawChessboardCorners(img, (8,6), corners, ret)
		plt.imshow(img)


---
Note Regarding Corner Coordinates

Since the origin corner is (0,0,0) the final corner is (6,4,0) relative to this corner rather than (7,5,0).


Examples of Useful Code


Converting an image, imported by cv2 or the glob API, to grayscale:

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

Note: If you are reading in an image using mpimg.imread() this will read in an RGB image and you should convert to grayscale using cv2.COLOR_RGB2GRAY, but if you are using cv2.imread() or the glob API, as happens in this video example, this will read in a BGR image and you should convert to grayscale using cv2.COLOR_BGR2GRAY. We'll learn more about color conversions later on in this lesson, but please keep this in mind as you write your own code and look at code examples.


Finding chessboard corners (for an 8x6 board):

ret, corners = cv2.findChessboardCorners(gray, (8,6), None)


Drawing detected corners on an image:

img = cv2.drawChessboardCorners(img, (8,6), corners, ret)


Camera calibration, given object points, image points, and the shape of the grayscale image:

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)


Undistorting a test image:

dst = cv2.undistort(img, mtx, dist, None, mtx)


A note on image shape

The shape of the image, which is passed into the calibrateCamera function, is just the height and width of the image. One way to retrieve these values is by retrieving them from the grayscale image shape array gray.shape[::-1]. This returns the image width and height in pixel values like (1280, 960).

Another way to retrieve the image shape, is to get them directly from the color image by retrieving the first two values in the color image shape array using img.shape[1::-1]. This code snippet asks for just the first two values in the shape array, and reverses them. Note that in our case we are working with a greyscale image, so we only have 2 dimensions (color images have three, height, width, and depth), so this is not necessary.

It's important to use an entire grayscale image shape or the first two values of a color image shape. This is because the entire shape of a color image will include a third value -- the number of color channels -- in addition to the height and width of the image. For example the shape array of a color image might be (960, 1280, 3), which are the pixel height and width of an image (960, 1280) and a third value (3) that represents the three color channels in the color image which you'll learn more about later, and if you try to pass these three values into the calibrateCamera function, you'll get an error.
