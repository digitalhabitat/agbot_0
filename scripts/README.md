# agbot_0/scripts/

### ackermann2twist.py
A ROS node that converts a **ackermann** message topic from to **twist** messeage topic

### checkusb

A simple script to checks that the:

roboclaw 2x60A is connected and has battery power

Jrk G2 24v13 is connnected

### intro.txt
Introduction text that appears when bash is accessed

### roboclaw.py
Python library for roboclaw (needed for checkusb)

### setup-cmd.sh

This initializes `checkusb` to function  as a command

`export PATH=$PATH:~/catkin_ws/src/agbot_0/scripts` is appended to `~/bash.rc`

### setup-intro.sh

This initializes into.txt to appear when bash is accessed

`echo "$(cat ~/catkin_ws/src/agbot_0/scripts/intro.txt)` is append to `~/bash.rc`

### teleop.py

A ROS node that subscribes to **joy** message topics and publishes **ackermann** message topics

***TODO Rewrite telelop.py as a finite sate machine***

