#!/usr/bin/env python3
import rospy
from your_package.msg import Data
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " Name: %s, ID: %i", data.name, data.id)
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", Data, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()