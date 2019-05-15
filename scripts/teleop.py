#!/usr/bin/env python
import rospy
import time
import sys
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from ackermann_msgs.msg import AckermannDrive

class Node:

    def __init__(self):
        rospy.init_node('joy_telop_node')
        rospy.on_shutdown(self.shutdown)
        self.joy_subscriber = rospy.Subscriber("joy", Joy, self.joy_callback)
        self.joy_publisher = rospy.Publisher("cmd_vel", Twist, queue_size="1")

        
    def run(self):
        time.sleep(3) # sleep 1 second
        rospy.loginfo("starting joy_teleop_node")
        rospy.spin()


    def joy_callback(self, joy_data):
        #rospy.loginfo("%d %d %d", joy_data.buttons[0], joy_data.buttons[1], joy_data.buttons[3])
        data = Twist()
        #data.linear.x = joy_data.axes[4]
        #self.joy_publisher.publish(data)
    
        # if x button pressed
        if joy_data.buttons[1]:
            # if R2 and Not L2
            if not joy_data.buttons[6]:
                data.linear.x = joy_data.axes[4] # 1 to -1
                data.linear.x = 0.5*(-1*(data.linear.x)+1) # 0 to 1
                self.joy_publisher.publish(data)
                rospy.loginfo("recv %s", data.linear.x)


    def shutdown(self):
        rospy.logwarn("Shutting down")

if __name__ == "__main__":
    try:
        node = Node()
        node.run()
    except rospy.ROSInterruptException:
        pass
    rospy.logware("Exiting")
