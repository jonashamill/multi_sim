#!/usr/bin/env python3


import rospy
from smach import StateMachine
from smach_ros import SimpleActionState
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import math
import tf
import rospkg #import RosPack as rp



# waypoints = [
#     ['one', (2.1, 2.2), (0.0, 0.0, 5.2193522453308105,-0.1537688)],
#     ['two', (6.5, 4.43), (0.0, 0.0, 5.393279075622559,-0.12403528392314911)]
# ]


def read_waypoints(file_path):
    waypoints = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y, z, yaw_deg = map(float, line.strip().split(','))
            yaw_rad = math.radians(yaw_deg)
            quaternion = tf.transformations.quaternion_from_euler(0, 0, yaw_rad)
            waypoints.append([(x, y, z), quaternion])
    return waypoints



if __name__ == '__main__':
    rospy.init_node('patroller')

    robot_ns = rospy.get_namespace()
    robot_ns_path = robot_ns + "patroller" + robot_ns

    route = rospy.get_param(robot_ns_path + 'route')

    rp = rospkg.RosPack()
    package_path = rp.get_path('leo_navigation')
    CSV_path = (package_path + "/waypoints/" + route)

    waypoints = read_waypoints(CSV_path)

    patrol = StateMachine(['succeeded', 'aborted', 'preempted'])
    with patrol:
        for i,w in enumerate(waypoints):

            
            goal_pose = MoveBaseGoal()
            goal_pose.target_pose.header.frame_id = 'map'

            

            goal_pose.target_pose.pose.position.x = w[0][0]
            goal_pose.target_pose.pose.position.y = w[0][1]
            goal_pose.target_pose.pose.position.z = w[0][2]

            goal_pose.target_pose.pose.orientation.x = w[1][0]
            goal_pose.target_pose.pose.orientation.y = w[1][1]
            goal_pose.target_pose.pose.orientation.z = w[1][2]
            goal_pose.target_pose.pose.orientation.w = w[1][3]

            StateMachine.add(w[0], 
                SimpleActionState('move_base',MoveBaseAction, goal=goal_pose), 
                transitions={'succeeded':waypoints[(i+1) % len(waypoints)][0]})
            
            rospy.loginfo("Headed to waypoint" + robot_ns)
    
    patrol.execute()