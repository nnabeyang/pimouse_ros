#!/usr/bin/env python
#encoding: utf-8
import unittest, rostest
import rosnode, rospy
import time
from pimouse_ros.msg import MotorFreqs
from geometry_msgs.msg import Twist

class MotorTest(unittest.TestCase):
  def file_check(self, dev, value, message):
   with open("/dev/" + dev, "r") as f:
     self.assertEqual(f.readline(), str(value) + "\n", message)

  def test_node_exist(self):
    nodes = rosnode.get_node_names()
    self.assertIn('/motors', nodes, "node does not exist")

if __name__ == '__main__':
  time.sleep(3)
  rospy.init_node('travis_test_motors')
  rostest.rosrun('pimouse_ros', 'travis_test_motors', MotorTest)
