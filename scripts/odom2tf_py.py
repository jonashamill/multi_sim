#!/usr/bin/env python3

import rospy
import tf
from nav_msgs.msg import Odometry

topic = "odometry_merged"
child_frame = "base_footprint"

def odom_callback(odom):
    br = tf.TransformBroadcaster()
    odom_pose = odom.pose.pose
    pose_translation = (odom_pose.position.x, odom_pose.position.y, odom_pose.position.z)
    pose_rotation = (odom_pose.orientation.x, odom_pose.orientation.y, odom_pose.orientation.z, odom_pose.orientation.w)
    br.sendTransform(pose_translation, pose_rotation, odom.header.stamp, odom.header.frame_id, child_frame)

def main():
    rospy.init_node("odom2tf")
    global topic, child_frame
    topic = rospy.get_param("~odom_topic", topic)
    child_frame = rospy.get_param("~child_frame_id", child_frame)
    rospy.Subscriber(topic, Odometry, odom_callback)
    rospy.spin()

if __name__ == '__main__':
    main()
