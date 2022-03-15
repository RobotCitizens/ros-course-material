#!/usr/bin/env python3

import cv2
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

bridge = CvBridge()

def show_image(data):
    frame = bridge.imgmsg_to_cv2(data)
    cv2.imshow("frame", frame)
    cv2.waitKey(1)

rospy.init_node("get_image_from_ros", anonymous=True)
sub = rospy.Subscriber("test_image",Image,show_image)
rospy.spin()