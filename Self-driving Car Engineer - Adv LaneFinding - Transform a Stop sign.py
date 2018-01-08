Self-driving Car Engineer

Term 1
Project: Advanced Lane Finding

Transform a Stop sign (#15)

---
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
%matplotlib qt


# Read in a single Stop sign image
img = mpimg.imread('../road_images_video/stopsign.jpg')
plt.imshow(img)

---
%matplotlib inline

# Source image points

plt.imshow(img)
plt.plot(850, 220, '.') top right corner
plt.plot(865, 450, '.') bottom right corner
plt.plot(533, 350, '.') bottom left corner
plt.plot(535, 210, '.') top left corner

---
# Warp function
#Define perspektive transform function

def warp(img):

	# Define calibration box in source (original) and destination (desired or warped) coordinates

	img_size = (img.shape[1], img.shape[0])

	# Four source coordinates
	src = np.float32(
		[[850, 220],
		 [865, 450],
		 [533, 350],
		 [535, 210]])

	# Four desired coordinates (just eye-balled in the video)
	dst = np.float32(
		[[870, 240],
		 [870, 370],
		 [520, 370],
		 [520, 240]])

	# Compute the perspective transform, M
	M = cv2.getPerspectiveTransform(src, dst)

	# Create warped image - uses linear interpolation
	warped = cv2.warpPerspective(img, M, img_size, flags=cv2.INTER_LINEAR)

	return warped

---

%matplotlib inline

# Get perspective transform
warped_img = warp(img)

# Visualize undistortion
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))

ax1.set_title('Source image')
ax1.imshow(img)
ax2.set_title('Warped image')
ax2.imshow(warped_img)


---


Examples of Useful Code


Compute the perspective transform, M, given source and destination points:

M = cv2.getPerspectiveTransform(src, dst)


Compute the inverse perspective transform:

Minv = cv2.getPerspectiveTransform(dst, src)


Warp an image using the perspective transform, M:

warped = cv2.warpPerspective(img, M, img_size, flags=cv2.INTER_LINEAR)

Note: When you apply a perspective transform, choosing four source points manually, as we did in this video, is often not the best option. There are many other ways to select source points. For example, many perspective transform algorithms will programmatically detect four source points in an image based on edge or corner detection and analyzing attributes like color and surrounding pixels.
