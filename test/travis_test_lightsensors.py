#!/usr/bin/env python
#encoding: utf-8
import unittest, rostest
import rosnode, rospy
import time
from pimouse_ros.msg import LightSensorValues

class LightsensorTest(unittest.TestCase):
  def setUp(self):
    self.count = 0
    rospy.Subscriber('/lightsensors', LightSensorValues, self.callback)
    self.values = LightSensorValues()
  def callback(self, data):
    self.count += 1
    self.values = data
  def test_node_exist(self):
    nodes = rosnode.get_node_names()
    self.assertIn('/lightsensors', nodes, "node does not exist")

if __name__ == '__main__':
  time.sleep(3)
  rospy.init_node('travis_test_lightsensors')
  rostest.rosrun('pimouse_ros', 'travis_test_lightsensors', LightsensorTest)
