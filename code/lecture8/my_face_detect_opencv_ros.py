#!/usr/bin/env python3
import cv2
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import rospkg

rospack = rospkg.RosPack()
cap = cv2.VideoCapture(rospack.get_path("my_ros_opencv")+"/vdo/promote.mp4")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
bridge = CvBridge()
rospy.init_node("send_image_to_ros", anonymous=True)
pub = rospy.Publisher("test_image",Image,queue_size=10)
rate = rospy.Rate(30)
while not rospy.is_shutdown():
	ret, frame = cap.read()
	if not ret:
		break
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 4)
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
	pub.publish(bridge.cv2_to_imgmsg(frame,"bgr8"))
	rate.sleep()