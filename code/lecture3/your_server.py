#!/usr/bin/env python3
from your_package.srv import Sum, SumResponse
import rospy

def server_callback(req):
    print("Returning [%s + %s = %s]"%(req.A, req.B, (req.A + req.B)))
    return SumResponse(req.A + req.B)

def sum_server():
    rospy.init_node('sum_server')
    s = rospy.Service('sum', Sum, server_callback)
    print("Ready to sum.")
    rospy.spin()

if __name__ == "__main__":
    sum_server()