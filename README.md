# agbot_0 Workspace
-------------
## Quick teleop start-up
1. Turn on Emlid Reach RS+ (on the very top of the AgBot)
Make sure the Reach is in hotspot mode(verify with mobile app or check WiFi on mobile phone... might take a minute if turning on)
2. Connect phone to the Emlid Reach hotspot.
3. Press the precharge button located on the power box.
4. Turn on AgBot Main Power by turning the Red side mounted E-Switch (Clockwise)
5. Switch on Wireless relay power located on the Power Box(White LED on Wireless relay box will light)
6. Press the Lejin Wireless Remote Button 1 (White LED on Power Box will light).
7. Turn on the Nvidia TX2. (Amber rocker switch inside tool box enclosure)
8. SSH with Termius app or PC terminal with ```ssh nvidia@tegra-ubuntu```
9. Turn on DS4 Bluetooth controller
10. ```roslaunch agbot_0 rc.launch```

-------------
## Remote PC Setup
File structure assumptions on tx2:
```
nvidia@tegra-ubuntu:~/catkin_ws/src$ ls
agbot_0  CMakeLists.txt  jrk_motor_node  roboclaw_node
```
File structure assumptions on personal computer to roslaunch nodes remotly:
```
user@machine:~/catkin_ws/src$ ls
agbot_0  jrk_motor_node  mapviz  nmea_navsat_driver  roboclaw_node
```

## Basic rc-car startup
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

-------------

## Basic rc-car startup (with ssh)
Launching device nodes on the rpi directly within an ssh session:
```bash
$ ssh ubuntu@rc-car
$ sudo pigpiod
$ ros launch agbot_0 rpi.launch
```
***NOTE:*** The above commands assumes both machines, local and remote are connected on a common wifi network

-------------

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

### Early Testing Platform
+ #### rc-car 
	+ Raspberry Pi 3 B+ Flashed with Ubiquity Robotics Raspbeery Pi Image
	+ Steering Servo:
	+ Motor Controler: Roboclaw 2x15A
	+ Quadrature Encoder: JGA25-370-12V-201rpm (only encoder)
	+ GPS: Emlid Reach M+
	+ IMU + Compass: PhidgetSpatial Precision 3/3/3 (1044_0B)

### Main Systems and Hardware Devices

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
	
### Abstract Hardware Diagram
![HW_Diagram](https://raw.githubusercontent.com/digitalhabitat/agbot_0/master/images/agbot_system_diagram.png)

[Click here](https://www.draw.io/?title=agbot_system_diagram.png&url=https%3A%2F%2Fraw.githubusercontent.com%2Fdigitalhabitat%2Fagbot_0%2Fmaster%2Fimages%2Fagbot_system_diagram.png%3Ft%3D0) to edit this image in a browser (?t=0 to bypass caches). Use the [Chrome App](https://chrome.google.com/webstore/detail/drawio-desktop/pebppomjfocnoigkeepgbmcifnnlndla) for native PNG+XML 

