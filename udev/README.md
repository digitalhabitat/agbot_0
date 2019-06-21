 
### Using persistent device names
excute `setup-udev.sh` to copy udev rules file to `/etc/udev/rules.d/` directory

***Note: Some devices like the two emlid gps devices are differentiated only by
there placement on the usb hub. For example in the 99-emlidreach.rules file...***

`ATTRS{devpath}=="2.1"` means port 1 on the hub

`ATTRS{devpath}=="2.2"` means port 2 on the hub

####  Persistent Device names currently used
+ `/dev/reach_m_plus`
+ `/dev/reach_r_plus`
+ `/dev/roboclaw`

***Note: The jrk does not support persisentent naming. We can expect `/dev/ttyACM*`***
