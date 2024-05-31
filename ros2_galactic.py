#!/usr/bin/python3

import os

os.system("locale")

os.system("sudo apt update && sudo apt install locales -y")
os.system("sudo locale-gen en_US en_US.UTF-8")
os.system("sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8")
os.system("export LANG=en_US.UTF-8")

os.system("locale")

os.system("sudo apt install software-properties-common -y")
os.system("sudo add-apt-repository universe")

os.system("sudo apt update && sudo apt install curl -y")
os.system("sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg")

os.system("echo \"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main\" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null")

os.system("sudo apt update -y && sudo apt upgrade -y")
os.system("sudo apt install ros-galactic-ros-base -y")
os.system("sudo apt install python3-colcon-common-extensions -y")

#---------------------------------------------------------------------------------------------------------------------------
# edit ros2 foxy ~/.bashrc

# ~/.bashrc command

os.system("echo \"alias eb='code ~/.bashrc'\" >> ~/.bashrc")
os.system("echo \"alias sb='source ~/.bashrc'\" >> ~/.bashrc")

os.system("echo \"source /opt/ros/galactic/setup.bash\" >> ~/.bashrc")
os.system("echo \"alias ss='. install/setup.bash'\" >> ~/.bashrc")
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


