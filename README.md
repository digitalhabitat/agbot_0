# agbot_0

IUPUI's robot for the 2019 Mining for Microbes and Microfauna Agbot Challenge

![AgBot Photo](https://raw.githubusercontent.com/digitalhabitat/agbot_0/master/images/agbot_photo0.jpg)

## Quick start up

To get the agbot moving perform the following steps

0. Switch on the 12 volt Logic battery by fliping the amber rocker switch inside the tool box encolsure.
1. Turn on the Nvidia TX2 by pressing the right most button. (Green LED on TX2 will light)
2. Connect a computer or phone to the TX2 hotspot or the local wifi 
3. Switch on the AgBot's main power by turning the red mounted E-Switch. (Clockwise) ***THIS IS THE ONBOARD EMERGENCY STOP***
4. Switch on the *Lejin Wireless Relay* power located on the Power Box. (White LED on Wireless relay box will light)
5. On the *Lejin Wireless Remote* press button 1. (White LED on Power Box will light). ***THIS IS THE WIRELESS EMERGENCY STOP***
6. Connect to the TX2 via SSH `ssh nvidia@tegra-ubuntu` (If using a phone use the Terminus App)
7. Turn on the PS4 controller
8. In the terminal enter `checkusb` (This verifies the drive and steering system is ready)
9. In the terminal enter `roslaunch agbot_0 rc.launch` ( Ctrl-C to terminate program)
10. Holding ✕... To drive forward gently press R2. To drive reverse gently press L2. Use left joystick to steer.

## Table of Contents

[Precautions and Troubleshooting](https://github.com/digitalhabitat/agbot_0#precautions-and-troubleshooting)

[Local Machine Setup](https://github.com/digitalhabitat/agbot_0#local-machine-setup)

[ROS Packages & Launch files (To run on the agbot runing roscore)](https://github.com/digitalhabitat/agbot_0#ros-packages--launch-files-to-run-on-the-agbot-runing-roscore)

[ROS Packages & Launch files (To run on remote PC)](https://github.com/digitalhabitat/agbot_0#ros-packages--launch-files-to-run-on-remote-pc)

[Main System and Hardware Devices](https://github.com/digitalhabitat/agbot_0#main-systems-and-hardware-devices)

[Abstract Diagram](https://github.com/digitalhabitat/agbot_0#abstract-hardware-diagram)

[Wiring Diagram](https://github.com/digitalhabitat/agbot_0#wiring-diagram)


## Precautions and Troubleshooting

+ The agbot does not stop moving or shows delayed control
	+ The Drive motors will go into a run away state if the wheel encoders are disconnected or intermittent. Ensure that the wheel encoder wire connections are properly attached and secure. Verify safe functionality on a jack stand before operating on the the lab floor. Always be ready to press button 1 on the wireless relay remote to activate the Emergency Stop in case this event occurs. ***NEVER STAND DIRECTLY IN FRONT OR BEHIND THE AGBOT***
	+ The PID controller configuration may need additional tunning.
	+ Delayed control around 1-2 sec at worst is typical.

+ `ssh nvidia@tegra-ubuntu` is not working
	+ The IP address of the TX2 is liable to changing. It might be necessary to accesses the local wifi router setup page or use a network scanner app to verify the IP address of the TX2 replacing `ssh nvidia@tegra-ubuntu` with `ssh nvidia@192.168.X.XXX` This IP address can be mapped to the hostname `tegra-ubuntu` by appending `etc/hosts` file on Linux.
	+ It maybe neccesary physically log onto the machine and verify network connenction with Ubiquity antenna. 

+ The TX2 does not turn on
	+ Ensure the Batteries are fully charged
	+ Check Voltage at the ouput of the 12V regulator.
	+ Check Fuse
	+ Disconnect the barrel plug on the TX2 and wait 15 seconds then reconnect the barrel plug
	+ Attach Battery to Charger while attempting to turn on the TX2
	+ Use diffently Power Suppply. Sometimes the LiFePO4 battery is more reliable.

+ The TX2 loses power when operating
	+ The TX2 and be powered by either the LiFePO4 battery or the Lead Acid Battery. The drive motors can cause system brown-outs on the LiFePO4 Power Supply. To avoid the TX2 reseting, use the Lead-Acid Batteries or a separate Power Supply.

+ The PS2 controller is not working
	+ The PS2 controller may need to be charged. A glowing orange light will indicate it is properly charging.

+ `catkin buid` is failing
	+ the dependencies have not been properly updated in 'agbot_0/package.xml' for this project. You may need to inspect the build error message to figure out which software package could not be found. The solution usually looks something like this... `sudo apt install ros-kinetic-some_package` or `sudo apt install some_library` or you may be able to just run `rodep update`

+ The Drive motors are not working
	+ Run 'checkusb' and verify the Roboclaw is properly wired and recieving 12V
	+ Reset power
	+ Alternate usb ports or bypass the usb hub and connect directly to the tx2.
	+ The PID controller configuration may need additional tunning.
	+ See [udev](https://github.com/digitalhabitat/agbot_0/tree/master/udev)

+ The Steering is not working
	+ Run 'checkusb' and verify the Jrk is properly and recieving 12V
	+ Reset power
	+ Alternate usb ports or bypass the usb hub and connect directly to the tx2.
	+ The PID controller configuration may need additional tunning.
	+ See [udev](https://github.com/digitalhabitat/agbot_0/tree/master/udev)

+ `roslaunch agbot_0 main.launch` is not working
	+ `main.launch` and `ekf.launch` are the most pertinent files for this project. Locailization is has only been experimentally verified for this project. It will be neccesary to play with the parameters or comment out sections to pinpoint the root cause. `main.launch` was intended to be launch from a remote linux PC on the same newtork to use MapViz and other GUIs. The PS2 controller has yet to be configured to connect through the remote linux PC, so its range will be limited to Bluetooth.

## Local Machine Setup  
File structure assumptions on tx2:
```
nvidia@tegra-ubuntu:~/catkin_ws/src$ ls
agbot_0  CMakeLists.txt  jrk_motor_node  roboclaw_node
```
File structure assumptions on local machine to roslaunch nodes remotely:
```
user@machine:~/catkin_ws/src$ ls
agbot_0  jrk_motor_node  mapviz  nmea_navsat_driver  roboclaw_node
```

To launch devices nodes remotely from a local machine on to the TX2:
```bash
$ export ROS_MASTER_URI='http://rc-car.local:11311'
$ ros launch agbot_0 rpi.launch
```
***NOTE:*** "$ export ROS_MASTER_URI=" only needs to be run once for a given terminal. The following command can use to set the envirment variable for every new terminal.
```bash
echo "ROS_MASTER_URI=http://rc-car.local:11311" >> ~/.bashrc 
```
This can also done by manually editing ~/.bashrc

## ROS Packages & Launch files (To run on the agbot runing roscore)
+ #### Roboclaw
	+ https://github.com/digitalhabitat/roboclaw_node
		+ [roboclaw.launch](launch/include/roboclaw.launch)

+ #### Steering Controller (Jrk G2 24v13)
	+ https://github.com/digitalhabitat/jrk_motor_node
		+ [jrk.launch](launch/include/jrk.launch)

+ #### Emlid Reach M+
	+ http://wiki.ros.org/nmea_navsat_driver (building from source, nmea_serial_driver)
		+ [emlid_gps.launch](launch/include/emlid_gps.launch)

+ #### PhidgetSpatial Precision 3/3/3 (1044_0B)
	+ http://wiki.ros.org/phidgets_imu
	+ http://wiki.ros.org/imu_filter_madgwick
		+ [phidget_imu.launch](launch/include/phidget_imu.launch)
	
+ #### Tinkerforge Brick 2.0 (Not yet utilized)
	+ https://github.com/droter/tinkerforge_imu_v2
		+ https://github.com/gus484/ros-tinkerforge_sensors

+ #### Playstation 4 Controller & Teleoperation (with bluetooth and ackermann-to-twist topic converserion nodes)
	+ http://wiki.ros.org/joy
	+ http://wiki.ros.org/joy_teleop
		+ [teleop.launch](launch/include/teleop.launch)

+ #### Localization (Sensor Fusion)
	+ http://wiki.ros.org/robot_localization
		+ [ekf.launch](launch/include/ekf.launch)

## ROS Packages & Launch files (To run on remote PC)
+ #### Vizualization
	+ http://wiki.ros.org/mapviz
	+ http://wiki.ros.org/rviz
		+ [mapviz.launch](launch/include/mapviz.launch)
		+ [rviz.launch](launch/include/rviz.launch)
	
+ #### Playstation 4 controller (launch file for Teleop over wifi not developed yet)

+ #### Debuging Tools
	+ http://wiki.ros.org/rqt_graph
	+ http://wiki.ros.org/rqt_tf_tree
	+ http://wiki.ros.org/rqt_robot_monitor
	+ http://wiki.ros.org/rqt_logger_level
	+ http://wiki.ros.org/rqt_console
		+ [tf_and_node.launch](launch/include/tf_and_node.launch)

## Main Systems and Hardware Devices

+ #### Computer System
	+ [Nvidia Jetson TX2](https://developer.nvidia.com/embedded/buy/jetson-tx2-devkit)
	+ [7-Port USB Hub](https://www.amazon.com/Anker-7-Port-Adapter-Charging-iPhone/dp/B014ZQ07NE)
	+ [Playstation DS4 Controller](https://www.amazon.com/DualShock-Wireless-Controller-PlayStation-Black-4/dp/B01LWVX2RG/ref=sr_1_3?crid=2YIUM2G6CQ5XL&keywords=ps4+controller&qid=1559175826&s=electronics&sprefix=ps+4+con%2Celectronics%2C149&sr=1-3)

+ #### Drive System (RWD)
	+ Motor Controller: [Roboclaw 2x60A](https://www.pololu.com/product/3289) 
	+ Motor Encoders: [US Digital (E2-500-375-NE-D-G-1)](https://www.usdigital.com/products/encoders/incremental/rotary/kit/E2)
	+ Motors: [AmpFlow Gearmotor (E30-400-G)](http://www.ampflow.com/ampflow_gearmotors.htm)

+ #### Steering System
	+ Linear Acutor w/ Feedback: [Glideforce LACT4P-12V-20](https://www.pololu.com/product/2305)
	+ Steering Controller: [Jrk G2 24v13](https://www.pololu.com/product/3147)

+ #### Odometry and Localization System
	+ GPS: [Emlid Reach M+](https://emlid.com/reach/)
	+ GPS: [Emlid Reach RS+](https://emlid.com/reachrs/)
	+ GPS Antenna: [Tallysman GNSS antenna for Reach M+](https://store.emlid.com/product/tallysman-multi-gnss-antenna/)
	+ IMU+Compass: [PhidgetSpatial Precision 3/3/3 (1044_0B)](https://www.phidgets.com/?tier=3&catid=10&pcid=8&prodid=1038)
	+ IMU+Compass: [Tinkerforge IMU Brick 2.0](https://www.tinkerforge.com/en/shop/bricks/imu-v2-brick.html)
	+ RTK Base Station: [INDOT RTK Corrections](https://incors.in.gov/rtk.aspx)
	+ Drive System Encoders
	+ Visual Odometry: [Intel RealSense D435](https://store.intelrealsense.com/buy-intel-realsense-depth-camera-d435.html)

+ #### Wireless Network System
	+ 5 GHz Radio: [Ubiquity Rocket M5](https://store.ui.com/collections/wireless/products/rocket-m5)
	+ Omnidirectional antenna: [Ubiquiti AMO-5G10](https://store.ui.com/collections/wireless/products/5ghz-airmax-omni-10dbi-rocket-kit)

+ #### Power System
	+ [12V LiFePO4 100 Ah Battery](https://battlebornbatteries.com/shop/12v-lifepo4-deep-cycle-battery/)
	+ 2x12V Lead-Acid 7Ah Batteries(For Computer and Roboclaw logic battery
)	
+ #### Mining System
	+ [Lejin Wireless Relay, 8 channel-12V](https://www.amazon.com/Lejin-Wireless-Multifunction-Empanender-Transmitter/dp/B07944GQ6C)
	+ 4-Way Solenoide: [McMaster-Carr 6124k287](https://www.mcmaster.com/6124k287)
	+ Motor Controller: [Roboclaw 2x15A](https://www.pololu.com/product/3285)
	+ Gear Motor: [uxcell DC 12 Motor](https://www.amazon.com/dp/B0788CMXGP/ref=twister_B07CSWCZRV?_encoding=UTF8&psc=1)

+ #### Early Testing Platform
	+ Raspberry Pi 3 B+ Flashed with Ubiquity Robotics Raspbeery Pi Image
	+ Steering Servo:
	+ Motor Controler: Roboclaw 2x15A
	+ Quadrature Encoder: JGA25-370-12V-201rpm (only encoder)
	+ GPS: Emlid Reach M+
	+ IMU + Compass: PhidgetSpatial Precision 3/3/3 (1044_0B)

## Abstract Hardware Diagram
![HW_Diagram](https://raw.githubusercontent.com/digitalhabitat/agbot_0/master/images/agbot_system_diagram.png)

[Click here](https://www.draw.io/?title=agbot_system_diagram.png&url=https%3A%2F%2Fraw.githubusercontent.com%2Fdigitalhabitat%2Fagbot_0%2Fmaster%2Fimages%2Fagbot_system_diagram.png%3Ft%3D0) to edit this image in a browser (?t=0 to bypass caches). Use the [Chrome App](https://chrome.google.com/webstore/detail/drawio-desktop/pebppomjfocnoigkeepgbmcifnnlndla) for native PNG+XML 

## Wiring Diagram
![HW_Diagram](https://raw.githubusercontent.com/digitalhabitat/agbot_0/master/images/wiring_diagram.png)
[Click here](https://www.draw.io/?title=wiring_diagram.png&url=https%3A%2F%2Fraw.githubusercontent.com%2Fdigitalhabitat%2Fagbot_0%2Fmaster%2Fimages%2Fwiring_diagram.png%3Ft%3D0) to edit this image in a browser (?t=0 to bypass caches). Use the [Chrome App](https://chrome.google.com/webstore/detail/drawio-desktop/pebppomjfocnoigkeepgbmcifnnlndla) for native PNG+XML 
