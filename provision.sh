#!/bin/bash
apt-get -y install python-pip
sudo apt-get install -y git
cd /vagrant
bash -xve ./test/travis_ros_install.bash
source ~/catkin_ws/devel/setup.bash
bash -xve ./test/travis_package_make.bash
source ~/catkin_ws/devel/setup.bash
rostest pimouse_ros test.launch
