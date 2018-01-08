# **Advanced Lane Lines**

## Writeup

### Udacity Course, October 2017 cohort

**Self-Driving Car Engineer Nanodegree Program**

**Project 'Advanced Lane Lines', December 2017**

**Claus H. Rasmussen**

---

**Identify the lane boundaries in a video from a front-facing camera on a car**

---

**Advanced Lane Finding Project**

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[//]: # (Image References)

[cal3]: ./output_images/cal_images/calibration3.jpg "Calibration image no.3"
[dist_testimage2]: ./test_images/test2.jpg "Original, distorted Test image no. 2"
[undist_testimage2]: ./output_images/cal_images/test2_undistorted.jpg "Undistorted Test image no. 2"
[combined_binary_testimage2]: ./output_images/test2_combined_thresh.png "Binary Example"
[source_lines_image]: ./output_images/straight_lines1_undistorted.jpg "Undistorted image with Source points"
[warped_lines_image]: ./output_images/straight_lines1_warped.png "Warp Example"
[histogram]: ./output_images/test3_histogram.jpg "Histogram"
[image6]: ./examples/example_output.jpg "Output"
[video1]: ./project_video.mp4 "Video"

## [Rubric](https://review.udacity.com/#!/rubrics/571/view) Points

### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---

### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one.  You can submit your writeup as markdown or pdf.  [Here](https://github.com/udacity/CarND-Advanced-Lane-Lines/blob/master/writeup_template.md) is a template writeup for this project you can use as a guide and a starting point.  

This markdown file is the writeup.

The code referenced here can be found in the Jupyter Notebook `Advanced_Lane_Lines.ipynb`.


### Camera Calibration

#### 1. Briefly state how you computed the camera matrix and distortion coefficients. Provide an example of a distortion corrected calibration image.

The code for calculating the calibration and saving an image with the "object points" drawn upon it, can be found in code cell no. 3 in the function `find_obj_and_img_points()`. Saved images of all the calibration images can be found in `./output_images/cal_images/`.  

I start by preparing "object points", which will be the (x, y, z) coordinates of the chessboard corners in the world. Here I am assuming the chessboard is fixed on the (x, y) plane at z=0, such that the object points are the same for each calibration image.  Thus, `objp` is just a replicated array of coordinates, and `objpoints` will be appended with a copy of it every time I successfully detect all chessboard corners in a test image.  `imgpoints` will be appended with the (x, y) pixel position of each of the corners in the image plane with each successful chessboard detection.  

I then used the output `objpoints` and `imgpoints` to compute the camera calibration and distortion coefficients using the `cv2.calibrateCamera()` function.  I applied this distortion correction to the test image using the `cv2.undistort()` function. the code for these operations is located in code cells no. 5 and 6.

The reprojection_error is calculated : 0.154.
The code for this calculation originates from the [opencv docs](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_calib3d/py_calibration/py_calibration.html).

This is an example of the resulting image:

![alt text][cal3]


### Pipeline (single images)

#### 1. Provide an example of a distortion-corrected image.

To demonstrate this step, I will describe how I apply the distortion correction to one of the test images like this one:
![alt text][dist_testimage2]

First the camera calibration parameters are calculated using opencv's `calibrateCamera(...)` function (code cell no. 5).
Next, these params are given to opencv's `undistort(...)` function (code cell no. 6).
This is demonstrated in code cell no. 8, and the undistorted image ends up looking like this:

![alt text][undist_testimage2]


#### 2. Describe how (and identify where in your code) you used color transforms, gradients or other methods to create a thresholded binary image.  Provide an example of a binary image result.

I used a combination of color and gradient thresholds to generate a binary image, where I use the S-channel from a HLS version of the image, combined with a Sobel gradient threshold in the x direction in order to accentuate lines away from horizontal. The code is located in code cell no. 11.
Here's an example of my output for this step:

![alt text][combined_binary_testimage2]


#### 3. Describe how (and identify where in your code) you performed a perspective transform and provide an example of a transformed image.

The code for my perspective transform includes a function called `warp(...)`, which appears in code cell no. 14 of the IPython notebook.  The `warp(...)` function takes as inputs an image (`img`). It contains the warping parameters (hardcoded) *source* (`src`) and *destination* (`dst`) points.  I chose the hardcode the source and destination points by eye balling them in a test image (`straight_lines1.jpg`). This resulted in the following source and destination points:

| Source        | Destination   |
|:-------------:|:-------------:|
| 720, 470      | 980, 0        |
| 1130, 720     | 980, 720      |
| 200, 720      | 320, 720      |
| 570, 470      | 320, 0        |

This is the undistorted image with the source points added as points:

![alt text][source_lines_image]

I verified that my perspective transform was working as expected by drawing the `src` and `dst` points onto a test image and its warped counterpart to verify that the lines appear parallel in the warped image (see code cell no. 15).

![alt text][warped_lines_image]


#### 4. Describe how (and identify where in your code) you identified lane-line pixels and fit their positions with a polynomial?

To identify the lane pixels, I used a histogram on the lower half of the image using `np.sum(...)`, see testing in code cell no. 17 and actual implementation in the pipeline in my function `slide_windows(...)` in code cell no. 18.
Then I did some other stuff and fit my lane lines with a 2nd order polynomial kinda like this:

![alt text][histogram]

#### 5. Describe how (and identify where in your code) you calculated the radius of curvature of the lane and the position of the vehicle with respect to center.

I did this in lines # through # in my code in `my_other_file.py`

#### 6. Provide an example image of your result plotted back down onto the road such that the lane area is identified clearly.

I implemented this step in lines # through # in my code in `yet_another_file.py` in the function `map_lane()`.  Here is an example of my result on a test image:

![alt text][image6]

---

### Pipeline (video)

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (wobbly lines are ok but no catastrophic failures that would cause the car to drive off the road!).

Here's a [link to my video result](./project_video.mp4)

---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

Here I'll talk about the approach I took, what techniques I used, what worked and why, where the pipeline might fail and how I might improve it if I were going to pursue this project further.  
