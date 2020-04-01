#!/usr/bin/env python3

import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def read_image(image_file):
    return mpimg.imread(image_file)


def write_image(image_file, image):
    mpimg.imsave(image_file, image)


def find_chessboard_corners(img, nx, ny, display=True):

    img = img.copy()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)

    if ret == True and display == True:
        # Draw and display the corners
        cv2.drawChessboardCorners(img, (nx, ny), corners, ret)
        plt.imshow(img)

    assert ret == True, f"Could not locate chessboard corners!"

    return corners


def calibrate_camera(img, objpoints, imgpoints):
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
        objpoints, imgpoints, img.shape[1:], None, None
    )
    assert ret == True, f"Could not calibrate camera!"
    return mtx, dist, rvecs, tvecs


def undistort(img, mtx, dist):
    undist = cv2.undistort(img, mtx, dist, None, mtx)
    return undist
