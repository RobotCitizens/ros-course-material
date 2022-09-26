#!/usr/bin/env python  
import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('tf_listener')

    listener = tf.TransformListener()

    
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/map', '/coke_can', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        print(f"trans: {trans}, rot: {rot}")