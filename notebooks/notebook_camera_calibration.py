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

cal_image_files = glob.glob("../camera_cal/*.jpg")
cal_image_files = sorted(cal_image_files, key = lambda x: int(re.findall(r"(\d+)\.jpg", x)[0]))

nx = 9 # The number of inside corners in x
ny = 5 # The number of inside corners in y

# Find corners on all images
chessboard_corners = []
for cal_image_file in cal_image_files:
    print(f"Processing {cal_image_file}")
    cal_image = utils.read_image(cal_image_file)
    cc = utils.find_chessboard_corners(cal_image, nx, ny)
    chessboard_corners.append(cc)

# +
# utils.calibrate_camera(img, objpoints, imgpoints)
# utils.undistort(img, mtx, dist)
