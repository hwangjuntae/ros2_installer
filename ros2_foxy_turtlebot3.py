import os, sys

os.system("sudo apt-get install ros-foxy-gazebo-*")
os.system("sudo apt install ros-foxy-cartographer")
os.system("sudo apt install ros-foxy-cartographer-ros")
os.system("sudo apt install ros-foxy-navigation2")
os.system("sudo apt install ros-foxy-nav2-bringup")
os.system("sudo apt install ros-foxy-dynamixel-sdk")
os.system("sudo apt install ros-foxy-turtlebot3-msgs")
os.system("sudo apt install ros-foxy-turtlebot3")
os.system("echo \'export ROS_DOMAIN_ID=30 #TURTLEBOT3\' >> ~/.bashrc")

# os.system("")
