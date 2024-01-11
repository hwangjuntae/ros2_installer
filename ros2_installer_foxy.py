#!/usr/bin/python3

import os, sys

#set locale
a1 = "sudo apt update -y && sudo apt install locales"
a2 = "sudo locale-gen en_US en_US.UTF-8"
a3 = "sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8"
a4 = "export LANG=en_US.UTF-8"
a5 = "locale"

#setup sources
a6 = "sudo apt install software-properties-common -y"
a7 = "sudo add-apt-repository universe"
a8 = "sudo apt update -y && sudo apt install curl -y"
a9 = "sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg"

temp = "\"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main\""
a10 = "echo " + temp + " | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null"



#install ros2 packages
a11 = "dpkg --get-selections | grep hold"
a12 = "sudo apt update -y && sudo apt upgrade -y"
a13 = "sudo apt install ros-foxy-desktop python3-argcomplete -y"
a14 = "sudo apt install ros-dev-tools -y"
a15 = "sudo apt install python3-colcon-common-extensions -y"

os.system(a1)
os.system(a2)
os.system(a3)
os.system(a4)
os.system(a5)
os.system(a6)
os.system(a7)
os.system(a8)
os.system(a9)
os.system(a10)
os.system(a11)
os.system(a12)
os.system(a13)
os.system(a14)
os.system(a15)

# edit ros2 foxy ~/.bashrc

# ~/.bashrc command

os.system("echo \"alias eb='code ~/.bashrc'\" >> ~/.bashrc")
os.system("echo \"alias sb='source ~/.bashrc'\" >> ~/.bashrc")

os.system("echo \"source /opt/ros/foxy/setup.bash\" >> ~/.bashrc")
os.system("echo \"alias cw='cd ~/ros2_ws'\" >> ~/.bashrc")
os.system("echo \"alias cs='cd ~/ros2_ws/src'\" >> ~/.bashrc")
os.system("echo \"alias ccd='colcon_cd'\" >> ~/.bashrc")
os.system("echo \"export ROS_DOMAIN_ID=30\" >> ~/.bashrc")
os.system("echo \"export ROS_NAMESPACE=robot1\" >> ~/.bashrc")

# build
os.system("echo \"alias cb='colcon build --symlink-install'\" >> ~/.bashrc")
os.system("echo \"alias cbp='colcon build --symlink-install --packages-select'\" >> ~/.bashrc")
os.system("echo \"alias cbu='colcon build --symlink-install --packages-up-to'\" >> ~/.bashrc")
os.system("echo \"alias ct='colcon test'\" >> ~/.bashrc")
os.system("echo \"alias ctp='colcon test --packages-select'\" >> ~/.bashrc")
os.system("echo \"alias ctr='colcon test-result'\" >> ~/.bashrc")

# topic list
os.system("echo \"alias rt='ros2 topic list'\" >> ~/.bashrc")
os.system("echo \"alias re='ros2 topic echo'\" >> ~/.bashrc")
os.system("echo \"alias rn='ros2 node list'\" >> ~/.bashrc")

# etc set
os.system("echo \"alias kill='killall -9 gazebo & killall -9 gzserver  & killall -9 gzclient'\" >> ~/.bashrc")
os.system("echo \"alias af='ament_flake8'\" >> ~/.bashrc")
os.system("echo \"alias ac='ament_cpplint'\" >> ~/.bashrc")

# test
os.system("echo \"alias testpub='ros2 run demo_nodes_cpp talker'\" >> ~/.bashrc")
os.system("echo \"alias testsub='ros2 run demo_nodes_cpp listener'\" >> ~/.bashrc")
os.system("echo \"alias testpubimg='ros2 run image_tools cam2image'\" >> ~/.bashrc")
os.system("echo \"alias testsubimg='ros2 run image_tools showimage'\" >> ~/.bashrc")

# os.system()


