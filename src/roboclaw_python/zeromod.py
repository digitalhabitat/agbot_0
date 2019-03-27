#!/usr/bin/env python
#testing custom roboclaw ROS node
import time
from roboclaw import Roboclaw
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Quaternion, Twist

DEFAULT_TWIST_CMD_TOPIC = "~twist_command"
#Windows comport name
#rc = Roboclaw("COM9",115200)
#Linux comport name
rc = Roboclaw("/dev/ttyACM0",115200)


def callback(cmd_vel):
     rospy.loginfo(rospy.get_caller_id() + "I heard %f", (cmd_vel.linear.x))
     #SpeedAccelDistanceM1(self,address,accel,speed,distance,buffer)
     rc.SpeedAccelDistanceM1(address,0,int(cmd_vel.linear.x*3000),100000,1)
     #rc.SpeedAccelDistanceM1(address,0,int(cmd_vel.linear.x),100,1)
     #rc.SpeedM1(address, int(cmd_vel.linear.x))
     #rc.SpeedM1(address, int(cmd_vel.linear.x))
     #rc.SpeedM1(address, int(cmd_vel.linear.x))

def zeropy():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    #sub0 = rospy.Subscriber("chatter2", String, callback)
    sub1 = rospy.Subscriber("ds4/cmd_vel", Twist, callback, queue_size=1)
    rospy.init_node('talker', anonymous=True)
		# rospy.Subscriber("cmd_vel", Twist, self.cmd_vel_callback, queue_size=1)
    # Set up the Twist Subscriber
    rate = rospy.Rate(60) # 10hz 
    i = 0   
    while not rospy.is_shutdown():      
        enc1 = rc.ReadEncM1(address)
        speed1 = rc.ReadSpeedM1(address)
        hello_str = "hello world %s Encoder1: %d Speed1: %d" % (rospy.get_time(), enc1[1], speed1[1])

        rospy.loginfo(hello_str)
        pub.publish(hello_str)

        '''code below allows interupts to freely enter for a small period of time'''
        for i in range(500):
	        for j in range(500):
		        for k in range(500):
			        pass
        #rc.SpeedAccelDistanceM1(address,0,i,10000,1)
        #i = i + 1
        #if(i == 3000):
        #	i = 0
        #rate.sleep()


def displayspeed():
	enc1 = rc.ReadEncM1(address)
	enc2 = rc.ReadEncM2(address)
	speed1 = rc.ReadSpeedM1(address)
	speed2 = rc.ReadSpeedM2(address)

	print("Encoder1:"),
	if(enc1[0]==1):
		print enc1[1],
		print format(enc1[2],'02x'),
	else:
		print "failed",
	print "Encoder2:",
	if(enc2[0]==1):
		print enc2[1],
		print format(enc2[2],'02x'),
	else:
		print "failed " ,
	print "Speed1:",
	if(speed1[0]):
		print speed1[1],
	else:
		print "failed",
	print("Speed2:"),
	if(speed2[0]):
		print speed2[1]
	else:
		print "failed "

rc.Open()
address = 0x80
reset = rc.ResetEncoders(address)

version = rc.ReadVersion(address)
if version[0]==False:
	print "GETVERSION Failed"
else:
	print repr(version[1])


#while(1):
#	displayspeed()
if __name__ == '__main__':
	try:
		zeropy()
	except rospy.ROSInterruptException:
		pass

