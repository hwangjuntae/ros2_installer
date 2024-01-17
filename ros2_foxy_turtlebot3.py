import os, sys

os.system("sudo apt-get install ros-foxy-gazebo-* -y")
os.system("sudo apt install ros-foxy-cartographer -y")
os.system("sudo apt install ros-foxy-cartographer-ros -y")
os.system("sudo apt install ros-foxy-navigation2 -y")
os.system("sudo apt install ros-foxy-nav2-bringup -y")
os.system("sudo apt install ros-foxy-dynamixel-sdk -y")
os.system("sudo apt install ros-foxy-turtlebot3-msgs -y")
os.system("sudo apt install ros-foxy-turtlebot3 -y")
os.system("echo \'export ROS_DOMAIN_ID=30 #TURTLEBOT3\' >> ~/.bashrc")

# os.system("")
