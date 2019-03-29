#!/usr/bin/env python

import rospy
import std_msgs
from ackermann_msgs.msg import AckermannDrive
import time
import pigpio
import sys


MIN_WIDTH = 500
MAX_WIDTH = 2500		 	
HOME_WIDTH = 1500
step = 10
width = MIN_WIDTH
gpio_num = 4 

class Node:



    def __init__(self):
        rospy.init_node('rpi_servo_node')
        rospy.on_shutdown(self.shutdown)
        rospy.Subscriber('ackermann_steering', AckermannDrive, self.servo_callback)
	self.pi = pigpio.pi()		
        if not self.pi.connected:
            rospy.logfatal("...pi not connnected")
            rospy.signal_shutdown("pi not connected")
 
        
    def run(self):
        global MIN_WIDTH, MAX_WIDTH, step, width
	self.pi.set_servo_pulsewidth(gpio_num, HOME_WIDTH)
        # home steering postion
        time.sleep(3) # sleep 1 second
        rospy.logerr("starting node")
        rospy.spin()
        """
        #### For testing purposes
        while True:
		for i in range(MIN_WIDTH, MAX_WIDTH, step):
                    rospy.logwarn("i = %d",i)
                    self.pi.set_servo_pulsewidth(gpio_num, i)
                    time.sleep(0.1)
                self.pi.set_servo_pulsewidth(gpio_num, MIN_WIDTH)
                time.sleep(3)
        """


    def servo_callback(self, AckermannDrive):
	scale = 300/0.35
	offset = 1500
        target=AckermannDrive.steering_angle*scale + offset
        self.pi.set_servo_pulsewidth(gpio_num, int(target))
        ###### p.ChangeDutyCycle(target)
        ###### print("about to write", target)
        rospy.logerr("target %f", target)

    def shutdown(self):
        rospy.logwarn("Shutting down")
        self.pi.set_servo_pulsewidth(gpio_num, HOME_WIDTH)
        self.pi.stop()

if __name__ == "__main__":
    try:
        node = Node()
        node.run()
    except rospy.ROSInterruptException:
        pass
    rospy.logware("Exiting")

    self.pi.set_servo_pulsewidth(gpio_num, HOME_WIDTH)
    self.pi.stop()
