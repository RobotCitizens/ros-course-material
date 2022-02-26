#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def get_cmd_vel(data):
    print(data)

if __name__ == "__main__":
    rospy.init_node("follow_that", anonymous=True)
    sub = rospy.Subscriber('/turtle1/cmd_vel', Twist, callback=get_cmd_vel)
    rospy.spin()
