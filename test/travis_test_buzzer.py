#!/usr/bin/env python
import rospy, unittest, rostest, actionlib
import rosnode
import time
from pimouse_ros.msg import MusicAction, MusicResult, MusicFeedback, MusicGoal

class BuzzerTest(unittest.TestCase):
  def setUp(self):
    self.longMessage = True
    self.client = actionlib.SimpleActionClient("music", MusicAction)
    self.device_values = []

  def test_node_exist(self):
    nodes = rosnode.get_node_names()
    self.assertIn('/buzzer', nodes, "node does not exist")

  def test_music(self):
    goal = MusicGoal()
    goal.freqs = [100, 200, 300, 0]
    goal.durations = [2, 2, 2, 2]
    self.client.wait_for_server()
    self.client.send_goal(goal, feedback_cb=self.feedback_cb)
    self.client.wait_for_result()

    self.assertTrue(self.client.get_result(), "invalid result")
    self.assertEqual(goal.freqs, self.device_values, "invalid feedback")

  def feedback_cb(self, feedback):
    with open("/dev/rtbuzzer0", "r") as r:
      data = r.readline()
      self.device_values.append(int(data.rstrip()))
      
if __name__ == '__main__':
  time.sleep(3)
  rospy.init_node('travis_test_buzzer')
  rostest.rosrun('pimouse_ros', 'travis_test_buzzer', BuzzerTest)
