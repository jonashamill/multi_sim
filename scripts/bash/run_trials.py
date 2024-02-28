#!/usr/bin/env python3

import os
import time
import rospy

rospy.init_node("run_trials")

time.sleep(10)


os.system("roslaunch multi_sim start_exp.launch")