#!/bin/bash
# add -hf and -vf for horizontal/vertical flips

DATE=$(date +"%Y-%m-%d_%H-%M-%S_%s")
mkdir -p /home/pi/camera
raspistill -o /home/pi/camera/$DATE.jpg
