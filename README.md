# agbot_0 Workspace
File structure assumptions:
```
~/catkin_ws/src/agbot_0
```
-------------
## Basic rc-car startup
To launch devices nodes remotely from a local machine on to the Raspberry Pi (rpi):
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
$ ssh ubnutu@rc-car
$ sudo pigpiod
$ ros launch agbot_0 rpi.launch
```
***NOTE:*** The above commands assumes both machines, local and remote are connected on a common wifi network

-------------

## ROS Device/Sensor Packages
+ #### Roboclaw
	+ TBA

+ #### Steering Controller (Jrk G2 24v13)
	+ TBA

+ #### Emlid Reach M+
	+ http://wiki.ros.org/nmea_navsat_driver
		+ nmea_serial_driver

+ #### PhidgetSpatial Precision 3/3/3 (1044_0B)
	+ http://wiki.ros.org/phidgets_imu
	+ http://wiki.ros.org/imu_filter_madgwick

+ #### Playstation 4 Controller
	+ http://wiki.ros.org/joy
	+ http://wiki.ros.org/joy_teleop	

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
	+ Nvidia Jetson TX2
	+ USB Hub
	+ Playstation DS4 Controller

+ #### Drive System
	+ Motor Controller: Roboclaw 2x60A
	+ Motor Encoder: US Digital (E2-500-375-NE-D-G-1)
	+ Motor: AmpFlow Gearmotor (E30-400-G)

+ #### Steering System
	+ Linear Acutor w/ Feedback: Glideforce LACT4P-12V-20
	+ Steering Controller: Jrk G2 24v13

+ #### Odometry and Localization System
	+ GPS: Emlid Reach M+
	+ IMU+Compass: PhidgetSpatial Precision 3/3/3 (1044_0B)
	+ INDOT RTK Corrections
	+ Drive System Encoders
	+ Visual Odometry: Intel RealSense D435

+ #### Wireless Network System
	+ 5 GHz Radio: Ubiquity Rocket M5
	+ Omnidirectional antenna: (Ubiquiti AMO-5G10)

+ #### Power System
	+ 12V LiFePO4 100 Ah Battery
	+ 12V Lead-Acid 21 Ah Battery
	
+ #### Mining System
	+ Relay Module
	+ 4-Way Solenoide: McMaster-Carr 6124k287
	+ Motor Controller: Roboclaw 2x15A
	+ Gear Motor: uxcell DC 12 Motor
	
### Abstract Hardware Diagram
![HW_Diagram](https://raw.githubusercontent.com/iupui-agbot/agbot_0/master/images/agbot_hw_system_diagram.png)

