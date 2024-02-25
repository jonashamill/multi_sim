#!/usr/bin/env python3

import rospy
import math
import pandas as pd
import rospkg
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatus, GoalStatusArray
from geometry_msgs.msg import Pose, Point, Quaternion, Twist
from tf.transformations import quaternion_from_euler
from std_msgs.msg import Int32
import threading
import random
import os
from datetime import datetime
import csv
import socket

plasticMSG = 0
tagMSG = False
pauseMSG = False
timeList = []
beHaveList =[]


def plasticCallback(msg):

    global plasticMSG

    plasticMSG = msg.data

def tagCallback(msg):

    global tagMSG
    
    tagMSG = msg.data

def pauseCallback(msg):

    global pauseMSG

    pauseMSG = msg.data

def getTime():

    #grabbing time and date to provide unique ID for logs
    dateTime = datetime.now()
    dtString = dateTime.strftime("%Y%m%d%H%M%S") #ISO 8601 Standard

    rosTimeUnf = rospy.Time.now()

    rosCorrentTime = datetime.fromtimestamp(rosTimeUnf.to_sec())

    rosTime = rosCorrentTime.strftime("%H:%M: %S")

    return dtString, rosTime



def getPath():

    timenow, _ = getTime()

    rp = rospkg.RosPack()
    packagePath = rp.get_path('multi_sim')

    #getting hostName to determine different
    hostName = str(socket.gethostname())

    #Getting TTH Values
    timeThresholdLow = rospy.get_param("/timeThresholdLow")
    timeThresholdHigh = rospy.get_param("/timeThresholdHigh")

    #Getting trial number
    trial = rospy.get_param("/trial")

    path = os.path.join(packagePath, "logs")

    path = (packagePath + "/logs/" + hostName + "/TTH_" + str(timeThresholdLow) + "_" + str(timeThresholdHigh) + "_trial_" + str(trial) + "/extras/")


    if not os.path.exists(path):
        os.makedirs(path)

    fullpath = os.path.join(path, timenow + hostName + "_TTH_" + str(timeThresholdLow) + "_" + str(timeThresholdHigh) + "_trial_" + str(trial) + "_patlog.csv")

    print (fullpath)

    return path, fullpath

def makeFolder():

    path, _ = getPath()

    testFile = None

    # test folder permisions
    try:
        testFile = open(os.path.join(path, 'test.txt'), 'w+')
    except IOError:
        try:
            os.mkdir(path)
        except OSError:
            print("No log folder created")
        else:
            print("Log folder created")

    testFile.close()
    os.remove(testFile.name)


def saveCSV():
    
    _, filename = getPath()

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['ROS Time', 'Behaviour'])
        
        for i in range(len(beHaveList)):
            writer.writerow([timeList[i], beHaveList[i]])

class Patroller():

    def __init__(self):

        rospy.init_node('patroller')  # initialize node

        # preprocessing --------------------------------------------------

        robot_ns = rospy.get_namespace()

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
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
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

    def movebase_client(self):

        

        
        # if plasticMSG and tagMSG:
        #     rospy.loginfo("Pausing")

        #     t_end = rospy.Time.now() + rospy.Duration(10) #Wait for 10
        #     while rospy.Time.now() < t_end:
        #         vel_msg = Twist()
        #         # vel_msg.linear.x = -0.4
        #         vel_msg.angular.z = 0.2
        #         self.vel_pub.publish(vel_msg)
        #         #rospy.loginfo("midspin")

        #     rospy.loginfo("Pause Done")
        #     # Stop the robot
        #     vel_msg = Twist()
        #     self.vel_pub.publish(vel_msg)

        #     # Publish 'tag' as a ROS topic
        #     tagPub = rospy.Publisher('tagTopic', Int32, queue_size=10)
        #     tagPub.publish(False)


        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = self.pose_seq[self.goal_cnt]
        rospy.loginfo("Sending goal pose " +
                      str(self.goal_cnt+1)+" to Action Server")
        #rospy.loginfo(str(self.pose_seq[self.goal_cnt]))
        self.client.send_goal(goal)
        rospy.loginfo("==========* GOAL SENT *==========")
        
        

    def status_cb(self, msg):

        status = self.client.get_state()
        #rospy.loginfo(status)

        robot_ns = rospy.get_namespace()

        if status == 3:
            if self.tick == 1: # tick is one, returned home, done.
                rospy.loginfo("FIN")
                rospy.signal_shutdown("FIN")
                exit()
            self.goal_cnt +=1
            rospy.loginfo("Goal pose "+str(self.goal_cnt)+" reached")
            if rospy.get_param("/speed") == "slow":
                    rospy.loginfo("Spinning...")
                    self.spin_robot()
            if self.goal_cnt != rospy.get_param(robot_ns + "start_node"):#
                if self.goal_cnt == len(self.pose_seq):
                    self.goal_cnt = 0
                rospy.loginfo("Moving onto next goal...")
                self.movebase_client()
            else:
                rospy.loginfo("Final goal pose reached!")
                self.patrol_count += 1
                print(self.patrol_count)
                if self.patrol_count == rospy.get_param(robot_ns + "patrols"): # if done all the patrols return home, set tick to 1
                    goal = MoveBaseGoal()
                    goal.target_pose.header.frame_id = "map"
                    goal.target_pose.header.stamp = rospy.Time.now()
                    goal.target_pose.pose = self.pose_seq[rospy.get_param(robot_ns + "start_node")]
                    # rospy.loginfo("Returning to first waypoint")
                    # rospy.loginfo(str(self.pose_seq[rospy.get_param("~start_node")]))
                    self.client.send_goal(goal)
                    self.tick = 1
                    rospy.loginfo("==========* Returning Home *==========")
                else:
                    rospy.loginfo("Repeating patrol ...")
                    self.goal_cnt = rospy.get_param(robot_ns + "start_node")
                    self.movebase_client()

    def check_and_pause(self):

        global plasticMSG
        global tagMSG
        global pauseMSG
        global timeList
        global beHaveList


        usePlasticity = rospy.get_param("/usePlasticity")
        robot_ns = rospy.get_namespace()

        if usePlasticity:

            while not rospy.is_shutdown():  # Continuously check while the node is active

                rospy.Subscriber(robot_ns + 'plasticTopic', Int32, plasticCallback)

                rospy.Subscriber(robot_ns + 'tagTopic', Int32, tagCallback)

                if plasticMSG == 1 and tagMSG == True:
                    
                    rospy.loginfo('Plastic set to: %s', str(plasticMSG))

                    rospy.loginfo("Behaving")

                    ranDomNo = random.randrange(0,2)

                    _, timeNow = getTime()

                    t_end = rospy.Time.now() + rospy.Duration(5)  # Wait for 10 seconds
                    while rospy.Time.now() < t_end:
                        vel_msg = Twist()

                        

                        if ranDomNo == 1:
                            vel_msg.linear.x = 0.0
                            vel_msg.angular.z = 1.0

                            beHave = 'Spinning'

                        else:
                            vel_msg.linear.x = 0.0
                            vel_msg.angular.z = 0.0

                            beHave = 'Pausing'
                        
                        self.vel_pub.publish(vel_msg)

                    tagMSG = False

                    timeList.append(timeNow)
                    beHaveList.append(beHave)

                    _, timeNow = getTime()

                    timeList.append(timeNow)
                    beHaveList.append(beHave)
                    
                    
                    # Stop the robot
                    vel_msg = Twist()
                    self.vel_pub.publish(vel_msg)

                    rospy.loginfo(str(beHave) + " Behaviour Done")

                    # Publish 'tag' as a ROS topic
                    tagPub = rospy.Publisher(robot_ns + 'tagTopic', Int32, queue_size=10)
                    tagPub.publish(False)
        

    def run(self):
        # Start the check_and_pause method in a separate thread
        check_and_pause_thread = threading.Thread(target=self.check_and_pause)
        check_and_pause_thread.daemon = True  # Daemonize the thread so it stops when the main program exits
        check_and_pause_thread.start()

        # Continue with the rest of your logic (e.g., moving between waypoints)
        self.patrol_count = 0
        self.tick = 0
        self.movebase_client()

    # def pauseRobot(self):
    #     # Pause robot on the spot
    #     t_end = rospy.Time.now() + rospy.Duration(5) #Wait for 5
    #     while rospy.Time.now() < t_end:
    #         vel_msg = Twist()
    #         vel_msg.linear.x = 0.0
    #         self.vel_pub.publish(vel_msg)
    #         #rospy.loginfo("midspin")

    #     rospy.loginfo("Pause Done")
    #     # Stop the robot
    #     vel_msg = Twist()
    #     self.vel_pub.publish(vel_msg)

if __name__ == '__main__':
    try:

        patroller = Patroller()
        patroller.run()
        rospy.spin()

        rospy.on_shutdown(saveCSV)

        # theta.reverse()
        # waypoints.reverse()
        # MoveBaseSeq(waypoints,theta)
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation finished.")