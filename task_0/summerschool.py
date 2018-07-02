#! /usr/bin/env python

import time
import math
import matplotlib.pyplot as plt


class Pose:
	def __init__(self, x=0.0, y=0.0, theta=0.0):
		self.x = float(x)
		self.y = float(y)
		self.theta = float(theta)

def distance(p1 = Pose(), p2 = Pose()):
	return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)

class Commander:
	def __init__(self, pose=Pose()):
		self.pose = pose
	
	def send_command(self, forward, angle):
		N = 100.0
		for i in range(int(N)):
			self.pose.x = self.pose.x + forward/N*math.cos(self.pose.theta)
			self.pose.y = self.pose.y + forward/N*math.sin(self.pose.theta)
			self.pose.theta = self.pose.theta + angle/N
		

	def get_message(self, msg=Pose()):
		# put your code here
		# using incomming pose (msg) and current pose (self.pose) 
		# define forward and angle variables to move itself to incoming position
		self.send_command(forward, angle)

if __name__ == "__main__":
	p = Pose(5,5,0)
	c = Commander(Pose(0,0,-math.pi/2))
	plt.ion()
	fig = plt.figure()
	plt.axis([-1,11,-1,11])
	ax = fig.add_subplot(111)
	point_p, = ax.plot([],[],'ro')
	point_c, = ax.plot([],[],'bo')
	while (distance(p,c.pose) > 0.01):
		c.get_message(p)
		point_p.set_xdata([p.x, p.x+0.1*math.cos(p.theta)])
		point_p.set_ydata([p.y, p.y+0.1*math.sin(p.theta)])
		point_c.set_xdata([c.pose.x, c.pose.x+0.2*math.cos(c.pose.theta)])
		point_c.set_ydata([c.pose.y, c.pose.y+0.2*math.sin(c.pose.theta)])
		fig.canvas.draw()
		fig.canvas.flush_events()
		time.sleep(0.2)
