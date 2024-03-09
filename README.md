# 2D to 3D video converter

## Overview
This Python script uses OpenCV to manipulate video frames by resizing and cropping the input video, then outputting the processed frames side by side in a new video file. This essentialy turns a 2d video to a 3d video and can be viewed in a Virtual Reality (VR) headset.

## Features
- **Resize Video Frames:** Increase the size of the video frames by a factor of 1.2.
- **Crop Video Frames:** Crop the left and right parts of the resized frame.
- **Combine Frames:** Place the cropped left and right frames side by side in the output video.

## Prerequisites
Before you can run this script, you'll need to have the following installed:
- Python 3.x
- OpenCV library for Python

You can install OpenCV using pip:
pip install opencv-python

## Usage
To use this script, simply run it with Python. Make sure you have a video file named `input_video.mp4` in the same directory as the script, or modify the script to point to the location of your video file.

## Note
When viewing the output video in a VR headset set to side-by-side video, the 3d video might look distorted. If anyone knows how to fix it let me know in the Issues section.
