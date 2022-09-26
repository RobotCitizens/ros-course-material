#!/usr/bin/env python3  
import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('tf_broadcaster_obj')
    br = tf.TransformBroadcaster()
    while not rospy.is_shutdown():
        br.sendTransform((1, 1, -0.2),
                        tf.transformations.quaternion_from_euler(0, 0, 0),  # type: ignore
                        rospy.Time.now(),
                        "coke_can",
                        "camera_link")