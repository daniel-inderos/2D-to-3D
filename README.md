# 2D to 3D Video Converter

## Overview
This Python script uses ffmpeg to convert a 2D video into a side-by-side 3D video format suitable for viewing in a Virtual Reality (VR) headset. It processes the input video by resizing, cropping, and shifting the frames to create a stereoscopic effect.

## Features
- **Interactive Input:** Prompts the user for the input video file path.
- **Automatic Output:** Saves the output video in the same directory as the script.
- **Customizable Parameters:** Allows users to set custom zoom and shift values.
- **VR-Ready Output:** Creates a side-by-side 3D video compatible with VR headsets.

## Prerequisites
Before you can run this script, you'll need to have the following installed:
- Python 3.x
- ffmpeg-python library

You can install the required library using pip:

## Usage
To use this script, simply run it with Python. Make sure you have a video file named `input_video.mp4` in the same directory as the script, or modify the script to point to the location of your video file.

## Note
When viewing the output video in a VR headset set to side-by-side video, the 3d video might look distorted. If anyone knows how to fix it let me know in the Issues section.
