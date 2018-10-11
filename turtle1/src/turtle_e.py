#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
from turtlesim.msg import Pose
import math
import time

if __name__ == "__main__":
	rospy.init_node("e")
	spawn=rospy.ServiceProxy("/spawn", Spawn)
	spawn(1,5,-(math.pi/2),"e_turtle")
	pub=rospy.Publisher('e_turtle/cmd_vel', Twist, queue_size=10)
	time.sleep(1)
	msg=Twist()
	msg.linear.x= 2
	msg.angular.z = 0
	pub.publish(msg)
	time.sleep(1)

	msg.linear.x= 2
	msg.angular.z = -math.pi/4
	pub.publish(msg)
	time.sleep(1)

