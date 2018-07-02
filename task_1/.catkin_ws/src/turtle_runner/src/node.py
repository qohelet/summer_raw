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
		self.sub1 = rospy.Subscriber("/turtle1/pose",Pose,self.get_message)
		self.sub2 = rospy.Subscriber("/victim/pose",Pose,self.pose_update)
		self.pub = rospy.Publisher("/victim/cmd_vel",Twist,queue_size=10)
	
	def pose_update(self, msg=Pose):
		self.pose=msg
		
	def get_message(self, msg=Pose):
		msg_pub = Twist()
		msg_pub.linear.x = 1
		msg_pub.angular.z = (math.atan2(msg.y - self.pose.y,
		                                msg.x - self.pose.x) - 
		                     self.pose.theta)
		while (msg_pub.angular.z > math.pi):
			msg_pub.angular.z -= 2*math.pi
		while (msg_pub.angular.z < -math.pi):
			msg_pub.angular.z += 2*math.pi
		self.pub.publish(msg_pub)

if __name__ == "__main__":
	rospy.init_node("traveller")
	c = Commander(Pose(0.0,0.0,0.0,0.0,0.0))
	rospy.spin()
