 
### To use persistent device names
### excute setup-udev.sh to copy udev rules file to /etc/udev/rules.d/ directory

#### Note: Some devices like the twwo emlid gps devices are differentiated only by
#### there placement on the usb hub. Refer to the post-it labeling proper connection
#### see ATTRS{devpath}=="2.1" in the .rules file (means port 1 on hub )

####  Persistent Device names currently used
/dev/reach_m_plus
/dev/reach_r_plus
/dev/roboclaw