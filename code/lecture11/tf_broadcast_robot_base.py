#!/usr/bin/env python3  
import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('tf_broadcaster_robot')
    br = tf.TransformBroadcaster()
    while not rospy.is_shutdown():
        br.sendTransform((1, 1, 0),
                        tf.transformations.quaternion_from_euler(0, 0, 1.0), # type: ignore
                        rospy.Time.now(),
                        "base_link",
                        "map")
        br.sendTransform((0, 0, 0.5),
                        tf.transformations.quaternion_from_euler(0, 0, 0), # type: ignore
                        rospy.Time.now(),
                        "camera_link",
                        "base_link")