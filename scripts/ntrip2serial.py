#!/usr/bin/env python
import rospy
import time
import math
import sys
import os # using enviroment variable for secrets
#  if enviroment varaible is missing run bash commmand... 
#  export InCORS_USER="{user_name_without_braces}"
#  export InCORS_USER="{password_without_braces}"
import subprocess

# This node calls a command line program str2str from rktlib that connects the tx2 to an NTRIP server for single site RTK correction data

# TODO: this only works for single site, since MAX, IMAX, NEAR require to Send NMEA GGA messages to the corrections provider which I could not figure out how to do with rtklib
# NOTE: iMAX, MAX, or NEAR and can still be used by configuring emlid correction input through the broswer interface just remember to disable this node to prevent multiple sign-ins 
# NOTE: Referenced material: 
# https://incors.in.gov/
# https://www.use-snip.com/kb/knowledge-base/subtle-issues-with-using-ntrip-client-nmea-183-strings/
# https://incors.in.gov/RT%20Products%20012914.pdf

class Node:

    def __init__(self):
        rospy.init_node('NTRIP_client_node')
        rospy.on_shutdown(self.shutdown)

        # input NTRIP client Parameters
        un_string = os.environ.get('InCORS_USER')
        self.USER_NAME = rospy.get_param("~user_name", os.environ.get('InCORS_USER')) 
        self.PASSWORD = rospy.get_param("~password", os.environ.get('InCORS_PASS'))
        self.IP_ADDRESS = rospy.get_param("~ip_address", "108.59.49.226")
        self.IP_PORT = rospy.get_param("~ip_port", "7071") # Single site, RTCM3.x
        self.MOUNT_POINT = rospy.get_param("~mount_point", "RTCM3_INMT") #indianapolis = RTCM3_INMT, west layfayette = RTCM3_INWL

        # ouput serial port parameters
        self.DEV_PORT = rospy.get_param("~serial_port", "ttyACM0") # must be pluged into specified port usb hub or might be ttyACMx check /dev directory
        self.BITRATE = rospy.get_param("~bitrate", "11520")
        self.BITSIZE = rospy.get_param("~databits", "8")
        self.PARITY = rospy.get_param("~partity", "n")
        self.STOPBIT = rospy.get_param("~stopbit", "1")
        self.FLOW_CONTROL = rospy.get_param("~flow_control", "n")
        
    def run(self):
        rospy.loginfo("NTRIP_client_node")
        #serial://port[:brate[:bsize[:parity[:stopb[:fctr]]]]]

        cmd_str1 = "str2str -in ntrip://"+self.USER_NAME+":"+self.PASSWORD+"@"+self.IP_ADDRESS+":"+self.IP_PORT+"/"+self.MOUNT_POINT
        cmd_str2 = " -out serial://"+self.DEV_PORT+":"+self.BITRATE+":"+self.BITSIZE+":"+self.PARITY+":"+self.STOPBIT+":"+self.FLOW_CONTROL
        full_cmd = cmd_str1 + cmd_str2
        print(full_cmd)
        list_files = os.system( full_cmd )
        #print("The exit code was: %d" % list_files.returncode)

        rospy.spin()

    def shutdown(self):
        rospy.logwarn("Shutting down")


if __name__ == "__main__":
    try:
        node = Node()
        node.run()
    except rospy.ROSInterruptException:
        pass
    rospy.logware("Exiting")
