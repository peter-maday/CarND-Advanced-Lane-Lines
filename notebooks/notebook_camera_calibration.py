# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.1
#   kernelspec:
#     display_name: Python 3.7.6 64-bit
#     language: python
#     name: python37664bite9d4ed6a001348e5938e61bf8e8a78cd
# ---

# # Calibrate camera

# %load_ext autoreload
# %autoreload 2
# %matplotlib inline

import glob
import matplotlib.pyplot as plt
import re

import utils

# +
nx = 9 # The number of inside corners in x
ny = 6 # The number of inside corners in y

import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt
import os
import scipy.io

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((ny*nx,3), np.float32)
objp[:,:2] = np.mgrid[0:nx,0:ny].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d points in real world space
imgpoints = [] # 2d points in image plane.

# Make a list of calibration images
images = glob.glob('../camera_cal/calibration*.jpg')
out_path = '../camera_cal/chessboard_corners'

# Step through the list and search for chessboard corners
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (nx,ny),None)

    # If found, add object points, image points
    if ret == True:
        objpoints.append(objp)
        imgpoints.append(corners)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (nx,ny), corners, ret)
        
        _, file_name = os.path.split(fname)
        os.makedirs(out_path, exist_ok=True)

        utils.write_image(os.path.join(out_path, file_name), img)
        
# Calibrate camera        
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img.shape[1:], None, None)

# Undistort calibration images
out_path = '../camera_cal/undistorted'
os.makedirs(out_path, exist_ok=True)
for fname in images:
    img = cv2.imread(fname)
    img = cv2.undistort(img, mtx, dist, None, mtx)
    _, file_name = os.path.split(fname)
    utils.write_image(os.path.join(out_path, file_name), img)
    
# Save calibration result
scipy.io.savemat("../camera_cal/camera_calibration.mat", {"mtx" : mtx, "dist" : dist})
