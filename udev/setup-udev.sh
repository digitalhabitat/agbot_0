cp ~/catkin_ws/src/agbot_0/udev/*.rules /etc/udev/rules.d/
echo "udev rules file has been copied to /etc/udev/rules.d/"
sudo udevadm control --reload-rules && sudo service udev restart && sudo udevadm trigger
echo "changes should now take effect... if not you may need to restart the computer"

