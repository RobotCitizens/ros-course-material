#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import Int64MultiArray
import os
import rospkg

path = rospkg.RosPack().get_path("your_package")

os.chdir(path)

class PeopleDetection(object):

    def __init__(self):
        self.bridge = CvBridge()
        rospy.init_node("object_detect", anonymous=True)
        self.data_pub = rospy.Publisher("/vision/people_detect/data", Int64MultiArray, queue_size=10)
        self.img_pub = rospy.Publisher("/vision/people_detect/image", Image, queue_size=10)
        rospy.Subscriber("/usb_cam/image_raw", Image, self.update_frame_callback)
        rospy.wait_for_message("/usb_cam/image_raw", Image)

    def update_frame_callback(self, data):
        self.image = self.bridge.imgmsg_to_cv2(data, desired_encoding="bgr8") 

    def main(self):
        net = cv2.dnn.readNet("cfg/yolov3.weights", "cfg/yolov3.cfg")
        classes = []
        with open("cfg/coco.names", "r") as f:
            classes = [line.strip() for line in f.readlines()] 

        output_layers = [layer_name for layer_name in net.getUnconnectedOutLayersNames()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))
        
        while not rospy.is_shutdown():
            frame = self.image
            height, width, channels = frame.shape
            blob = cv2.dnn.blobFromImage(frame, scalefactor=0.00392, size=(320, 320), mean=(0, 0, 0), swapRB=True, crop=False)
            net.setInput(blob)
            outputs = net.forward(output_layers)
            boxes = []
            confs = []
            class_ids = []
            for output in outputs:
                for detect in output:
                    scores = detect[5:]
                    class_id = np.argmax(scores)
                    conf = scores[class_id]
                    if conf > 0.3:
                        center_x = int(detect[0] * width)
                        center_y = int(detect[1] * height)
                        w = int(detect[2] * width)
                        h = int(detect[3] * height)
                        x = int(center_x - w/2)
                        y = int(center_y - h / 2)
                        boxes.append([x, y, w, h])
                        confs.append(float(conf))
                        class_ids.append(class_id)
            indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)
            font = cv2.FONT_HERSHEY_PLAIN
            for i in range(len(boxes)):
                if i in indexes:
                    x, y, w, h = boxes[i]
                    label = str(classes[class_ids[i]])
                    if label == "person":
                        pub_data = Int64MultiArray()
                        pub_data.data = [x,y,w,h]
                        self.data_pub.publish(pub_data)
                        color = colors[i]
                        cv2.rectangle(frame, (x,y), (x+w, y+h), color, 2)
                        cv2.putText(frame, label, (x, y - 5), font, 1, color, 1)
            # Publish image into ROS topic
            img_data = self.bridge.cv2_to_imgmsg(frame, encoding = "passthrough")
            self.img_pub.publish(img_data)
            # Show by imshow
            # cv2.imshow("Image", frame)
            key = cv2.waitKey(1)
            if key == 27:
                break

if __name__ == "__main__":
    obj = PeopleDetection()
    obj.main()


    