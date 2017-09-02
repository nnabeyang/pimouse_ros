#!/bin/bash -xve
rsync -av --exclude='.git/' --exclude='.vagrant' ./ ~/catkin_ws/src/pimouse_ros/
cd ~/catkin_ws
catkin_make
