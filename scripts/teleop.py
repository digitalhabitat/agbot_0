#!/usr/bin/env python
import rospy
import time
import sys
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from ackermann_msgs.msg import AckermannDrive

temp = 0

class Node:

    def __init__(self):
        rospy.init_node('joy_telop_node')
        rospy.on_shutdown(self.shutdown)

        # Parameters
        self.MAX_FORWARD_VELOCITY = float(rospy.get_param("~max_forward_vel", "0.3")) # in m/s
        self.MAX_REVERSE_VELOCITY = float(rospy.get_param("~max_reverse_vel", "0.1")) # in m/s
        self.MAX_STEERING_ANGLE = float(rospy.get_param("~max_steering_angle", "0.7853982")) # in radians (45 deg)
        self.ACKERMANN_COMMAND = rospy.get_param("~ackermann_command", "ackermann")
        self.JOY_MSGS = rospy.get_param("~joy_msgs", "joy")

        # Subscribers and Publishers
        self.joy_subscriber = rospy.Subscriber(self.JOY_MSGS, Joy, self.joy_callback)
        self.ackermann_publisher = rospy.Publisher(self.ACKERMANN_COMMAND, AckermannDrive, queue_size="1")

        
    def run(self):
        rospy.loginfo("starting joy_teleop_node")
        rospy.spin()


    def joy_callback(self, joy):
        global temp
        data = AckermannDrive()
    
        # x button pressed behaves as a deadman, switch R2 is forward L2 is reverse
        
        # if x is engadged and L2 and not active
        if joy.buttons[1] and not joy.buttons[6]:
            if not joy.buttons[7]:
                temp = 1

            elif joy.buttons[7] and temp:
                # if rising edge on R2 drive forward
                # joy.axes[4] moves from 1 to -1
                data.speed = self.MAX_FORWARD_VELOCITY*0.5*(-1*(joy.axes[4])+1)
                # also send steering angle 
                # joy.axes[0] is left +1 to right -1
                # right turn should be positive steering angle
                data.steering_angle = -joy.axes[0]*0.7853981
                

         # if x is engadged and R2 and not active
        elif joy.buttons[1] and not joy.buttons[7]:
            if not joy.buttons[6]:
                temp = 1

            elif joy.buttons[6] and temp:
                # if rising edge on L2 drive reverse
                # joy.axes[3] from 1 to -1
                data.speed = self.MAX_REVERSE_VELOCITY*0.5*(joy.axes[3]-1)
                # also send steering angle 
                # joy.axes[0] is left +1 to right -1
                # right turn should be positive steering angle
                data.steering_angle = -joy.axes[0]*0.7853981
            
                

        # deadman switch activated
        elif (not joy.buttons[7] and temp) or not joy.buttons[1] or joy.buttons[6] or joy.buttons[0] or (not joy.buttons[6] and temp) or not joy.buttons[0] or joy.buttons[7] or joy.buttons[1]:
            temp = 0 

        self.ackermann_publisher.publish(data)

        

    def shutdown(self):
        rospy.logwarn("Shutting down")

if __name__ == "__main__":
    try:
        node = Node()
        node.run()
    except rospy.ROSInterruptException:
        pass
    rospy.logware("Exiting")
