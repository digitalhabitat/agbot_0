# Appending PATH enviorment variable

echo "# Adding checkusb command to be run from anywhere in the terminal" >> ~/.bashrc
echo "export PATH=\$PATH:~/catkin_ws/src/agbot_0/scripts" >> ~/.bashrc
export PATH=$PATH:~/catkin_ws/src/agbot_0/scripts

echo "you can now type use \"checkusb\" as a command"
echo "NOTE: You first must open a new terminal for changes to take effect" 