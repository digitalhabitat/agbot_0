#!/usr/bin/env python
import rospy
import time
import math
import sys
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from ackermann_msgs.msg import AckermannDrive


class Node:

    def __init__(self):
        rospy.init_node('ackerman_to_twist_node')
        rospy.on_shutdown(self.shutdown)

        # Parameters
        self.WHEEL_BASE = float(rospy.get_param("~wheel_base", "1.18")) # distance between front and back tires in meters
        self.TWIST_COMMAND = rospy.get_param("~twist_command", "roboclaw/cmd_vel")
        self.ACKERMANN_COMMAND = rospy.get_param("~ackermann_command", "ackermann")

        # Subscribers and Publishers
        self.ackermann_subscriber = rospy.Subscriber(self.ACKERMANN_COMMAND, AckermannDrive, self.ackermann_callback)
        self.twist_publisher = rospy.Publisher(self.TWIST_COMMAND, Twist, queue_size="1")

        
    def run(self):
        rospy.loginfo("Starting ackerman_to_twist_node")
        rospy.spin()


    def ackermann_callback(self, ackermann):
        data = Twist()

        # see https://www.me.utexas.edu/~longoria/CyVS/notes/07_turning_steering/07_Turning_Kinematically.pdf
        data.linear.x = ackermann.speed
        data.angular.z = (ackermann.speed/self.WHEEL_BASE)*math.tan(ackermann.steering_angle)
        
        self.twist_publisher.publish(data)

    def shutdown(self):
        rospy.logwarn("Shutting down")

if __name__ == "__main__":
    try:
        node = Node()
        node.run()
    except rospy.ROSInterruptException:
        pass
    rospy.logware("Exiting")
