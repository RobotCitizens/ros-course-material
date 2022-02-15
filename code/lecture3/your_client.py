#!/usr/bin/env python3
from your_package.srv import Sum, SumResponse
import rospy

def user_sum():
    rospy.wait_for_service('sum')
    try:
        sum = rospy.ServiceProxy('sum', Sum)
        print("Please sum for me.")
        resp1 = sum(1,2)
        print(resp1)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    user_sum()