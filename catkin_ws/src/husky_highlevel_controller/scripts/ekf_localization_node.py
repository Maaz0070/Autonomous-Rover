#!/usr/bin/env python
import rospy #takke in ros python methods
from std_msgs.msg import String
import sensor_msgs
from math import sin, cos
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


#subscriber to scan topic
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/husky_velocity_controller/odom, String, callback)
    rospy.Subscriber("/imu/data", String, callback)
    rospy.Subscriber("/joint_states", String, callback)
    rospy.Subscriber("/velodyne/assembled_cloud_filtered", String, callback)
    rospy.spin()


if __name__ == '__main__':
    listener() 
    rospy.spin()

    
