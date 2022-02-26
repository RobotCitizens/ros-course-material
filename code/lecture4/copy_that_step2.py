#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import SpawnRequest, Spawn

def get_cmd_vel(data):
    print(data)

if __name__ == "__main__":
    rospy.init_node("follow_that", anonymous=True)
    sub = rospy.Subscriber('/turtle1/cmd_vel', Twist, callback=get_cmd_vel)
    spawn_ser = rospy.ServiceProxy('/spawn', Spawn)
    spawn_ser(SpawnRequest(x=1.0, y=1.0, theta=0.0, name="turtle2"))
    rospy.spin()
