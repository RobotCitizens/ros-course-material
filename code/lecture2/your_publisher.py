#!/usr/bin/env python3
import rospy
from your_package.msg import Data
def talker():
    pub = rospy.Publisher('chatter', Data, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        name = 'Test'
        id = 10
        pub_data = Data(name=name, id=id)
        rospy.loginfo(pub_data)
        pub.publish(pub_data)
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass