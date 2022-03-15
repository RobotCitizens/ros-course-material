#!/usr/bin/env python3

import cv2
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import rospkg

rospack = rospkg.RosPack()
cap = cv2.VideoCapture(rospack.get_path("my_ros_opencv")+"/vdo/promote.mp4")
bridge = CvBridge()
rospy.init_node("send_image_to_ros", anonymous=True)
pub = rospy.Publisher("test_image",Image,queue_size=10)
rate = rospy.Rate(30)
while not rospy.is_shutdown():
	ret, frame = cap.read()
	if not ret:
		break
	pub.publish(bridge.cv2_to_imgmsg(frame,"bgr8"))
	rate.sleep()
