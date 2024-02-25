#!/usr/bin/env python3


import rospy
from smach import StateMachine
from smach_ros import SimpleActionState
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import math
import tf
import rospkg 

from datetime import datetime
from geometry_msgs.msg import Pose, Point, Quaternion, Twist
from actionlib_msgs.msg import GoalStatusArray
from tf.transformations import quaternion_from_euler
import pandas as pd




def read_waypoints(file_path):
    waypoints = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y, z, yaw_deg = map(float, line.strip().split(','))
            yaw_rad = math.radians(yaw_deg)
            quaternion = tf.transformations.quaternion_from_euler(0, 0, yaw_rad)
            waypoints.append([(x, y, z), quaternion])
    return waypoints


def getTime():

    #grabbing time and date to provide unique ID for logs
    dateTime = datetime.now()
    dtString = dateTime.strftime("%Y%m%d%H%M%S") #ISO 8601 Standard

    rosTimeUnf = rospy.Time.now()

    rosCorrentTime = datetime.fromtimestamp(rosTimeUnf.to_sec())

    rosTime = rosCorrentTime.strftime("%H:%M: %S")

    return dtString, rosTime


class Patroller():

    def __init__(self):

        rospy.init_node('patroller')  # initialize node

        # preprocessing --------------------------------------------------

        robot_ns = rospy.get_namespace()
        robot_ns = robot_ns + "patroller" + robot_ns

        # gets csv file path
        rp = rospkg.RosPack()
        package_path = rp.get_path('multi_sim')
        route = rospy.get_param(robot_ns + 'route')
        CSV_path = (package_path + "/waypoints/" + route)

        # converts waypoints text file into a list of points to follow
        df = pd.read_csv(CSV_path, sep=',', header=None)
        self.theta = list(df.loc[:, 3].values)
        wayp = df.loc[:, 0:2]
        self.waypoints = []
        wayp = wayp.values.tolist()
        for sublist in wayp:
            for item in sublist:
                self.waypoints.append(item)

        points_seq = self.waypoints  # heading angle for each waypoint
        yaweulerangles_seq = self.theta  # coordinates for each waypoint

        # Convert waypoint & heading values into a list of robot poses (quaternions?) -----------
        quat_seq = list()
        # List of goal poses:
        self.pose_seq = list()
        self.goal_cnt = rospy.get_param(robot_ns + 'start_node')
        for yawangle in yaweulerangles_seq:
            # Unpacking the quaternion list and passing it as arguments to Quaternion message constructor
            quat_seq.append(Quaternion(
                *(quaternion_from_euler(0, 0, yawangle*math.pi/180, axes='sxyz'))))
        n = 3
        # Returns a list of lists [[point1], [point2],...[pointn]]
        points = [points_seq[i:i+n] for i in range(0, len(points_seq), n)]
        for point in points:
            # Exploit n variable to cycle in quat_seq
            self.pose_seq.append(Pose(Point(*point), quat_seq[n-3]))
            n += 1

        # Create action client -------------------------------------------
        # self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        rospy.loginfo("Waiting for move_base action server...")
        wait = self.client.wait_for_server(rospy.Duration(5.0))
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
            return
        rospy.loginfo("Connected to move base server")
        rospy.loginfo("Starting goals achievements ...")

        # Initiate status subscriber
        self.status_subscriber = rospy.Subscriber(
            robot_ns + "move_base/status", GoalStatusArray, self.status_cb
        )

        # Create a Twist publisher to send velocity commands to the robot
        self.vel_pub = rospy.Publisher(robot_ns + 'cmd_vel', Twist, queue_size=10)


        self.patrol_count = 0
        self.tick = 0
        self.movebase_client()


if __name__ == '__main__':
    rospy.init_node('patroller')

    robot_ns = rospy.get_namespace()
    robot_ns_path = robot_ns + "patroller" + robot_ns

    route = rospy.get_param(robot_ns_path + 'route')

    patrols = rospy.get_param(robot_ns_path + 'patrols')

    rp = rospkg.RosPack()
    package_path = rp.get_path('multi_sim')
    CSV_path = (package_path + "/waypoints/" + route)



    waypoints = read_waypoints(CSV_path)

    for i in range (patrols):
        rospy.loginfo(robot_ns + " Patrol number: " + str(i))

        patrol = StateMachine(['succeeded', 'aborted', 'preempted'])
        with patrol:
            for i,w in enumerate(waypoints):

                
                goal_pose = MoveBaseGoal()
                goal_pose.target_pose.header.frame_id = 'map'
                goal_pose.target_pose.header.stamp = rospy.Time.now()

                

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
                
                
        rospy.loginfo(robot_ns + " Headed to waypoint")

    
        outcome = patrol.execute()
        rospy.loginfo("State machine transitioning, robot_ns: {}, waypoint: {}. {} moving to waypoint {}".format(robot_ns, i, outcome, (i+1) % len(waypoints)))


        