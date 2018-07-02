#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
from turtlesim.msg import Pose
import math
import time

class Commander:
	def __init__(self, pose=Pose()):
		self.pose = pose
		spawn = rospy.ServiceProxy("/spawn",Spawn)
		spawn(pose.x,pose.y,pose.theta,"victim")
		self.subOwnPose = rospy.Subscriber("/victim/pose",Pose,self.pose_update)
	
	def pose_update(self, msg=Pose):
		self.pose=msg
		
	def get_message(self, msg=Pose):
		# put your code here
		# define where a target is and provide a command message for moving

if __name__ == "__main__":
	rospy.init_node("traveller")
	c = Commander(Pose(0.0,0.0,0.0,0.0,0.0))
	rospy.spin()
