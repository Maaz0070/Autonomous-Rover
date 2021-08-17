#!/usr/bin/env python
import rospy #takke in ros python methods
import sensor_msgs
from math import sin, cos
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


#function takes in sensor input and the desired input and outputs the proportional factor times (feedback - setpoint)
    
def p_control(feedback, setpoint = 0):
    global k_p
    return k_p * (feedback - setpoint)

#takes in array and returns the index which carries the minimum value
def get_min_index(a_list):
    return [index for index in range(0, len(a_list)) if a_list[index] == min(a_list)][0]

#function takes in smallest index of laster values and returns the apporpiate angle to turn the rover
def get_angle(ranges_index, angle_min, angle_increment):
    return angle_min + ranges_index * angle_increment

def callback(data):
    global twist_pub
    
    dist  = min(data.ranges)

     # find angle at which smallest_dist was found
    angle = get_angle(get_min_index(data.ranges), data.angle_min, data.angle_increment)

    #display the distane and angle values to the temrinal
    rospy.loginfo("dist: %s, angle: %s" % (dist, angle))
    
    #sets v_x to make sure we are as close as possible to the pole
    v_x = p_control(dist, data.range_min) * cos(angle)

    #  LIDAR frame is flipped 180 deg from base frame so we negate our angle
    w_z = p_control(angle, 0) * -sin(angle)

    twist_msg = Twist()
    twist_msg.linear.x = v_x
    twist_msg.angular.z = w_z
    twist_pub.publish(twist_msg) 


#subscriber to scan topic
def listener(scan_topic, queue_size):
    rospy.Subscriber(scan_topic, LaserScan, callback, queue_size=queue_size)
    rospy.spin()


if __name__ == '__main__':
    # init-ing in main allows us to work with rospy API for name/node info right away
    rospy.init_node('husky_highlevel_controller')

    rospy.Subscriber('/scan', LaserScan, callback) 
    twist_pub = rospy.Publisher('husky_velocity_controller/cmd_vel', Twist, queue_size=10) 
    k_p = 0.5
    rospy.spin()

    
